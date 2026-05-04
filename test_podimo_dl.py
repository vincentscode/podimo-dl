import importlib.util
import unittest
from pathlib import Path
from unittest.mock import MagicMock

_spec = importlib.util.spec_from_file_location(
    "podimo_dl", Path(__file__).parent / "podimo-dl.py"
)
podimo_dl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(podimo_dl)


class GetPodcastEpisodesTest(unittest.TestCase):
    def setUp(self):
        self.api = podimo_dl.PodimoAPI()
        self.api.public_client = MagicMock()

    def test_single_short_page_returns_immediately(self):
        self.api.public_client.execute.return_value = {
            "podcastEpisodes": [{"id": "a"}, {"id": "b"}],
        }

        result = self.api.get_podcast_episodes("pod-1", page_size=100)

        self.assertEqual(result, [{"id": "a"}, {"id": "b"}])
        self.assertEqual(self.api.public_client.execute.call_count, 1)
        call = self.api.public_client.execute.call_args_list[0]
        self.assertEqual(
            call.kwargs["variable_values"],
            {"podcastId": "pod-1", "limit": 100, "offset": 0},
        )

    def test_paginates_until_short_page(self):
        full_page = [{"id": str(i)} for i in range(100)]
        tail = [{"id": str(i)} for i in range(100, 150)]
        self.api.public_client.execute.side_effect = [
            {"podcastEpisodes": full_page},
            {"podcastEpisodes": tail},
        ]

        result = self.api.get_podcast_episodes("pod-1", page_size=100)

        self.assertEqual(len(result), 150)
        self.assertEqual(result[0]["id"], "0")
        self.assertEqual(result[-1]["id"], "149")

        offsets = [
            c.kwargs["variable_values"]["offset"]
            for c in self.api.public_client.execute.call_args_list
        ]
        self.assertEqual(offsets, [0, 100])

    def test_stops_on_empty_page(self):
        full_page = [{"id": str(i)} for i in range(3)]
        self.api.public_client.execute.side_effect = [
            {"podcastEpisodes": full_page},
            {"podcastEpisodes": []},
        ]

        result = self.api.get_podcast_episodes("pod-1", page_size=3)

        self.assertEqual(len(result), 3)
        self.assertEqual(self.api.public_client.execute.call_count, 2)


if __name__ == "__main__":
    unittest.main()
