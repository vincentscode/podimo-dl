from gql import gql, Client

mutationWebFollowPodcast = gql('''
  mutation web_followPodcast(
    $follow: Boolean!,
    $podcastId: String!
  ) {
    podcastFollow(
      follow: $follow,
      podcastId: $podcastId
    ) {
      isFollowing
    }
  }
''')

mutationWebCancelSubscription = gql('''
  mutation web_cancelSubscription($userId: String!) {
    cancelActiveSubscription(
      userId: $userId
    )
  }
''')


mutationWebCancelUserSubscription = gql('''
  mutation web_cancelUserSubscription( $userId: String, $provider: String! ) {
    userSubscriptionCancel( userId: $userId, provider: $provider ) {
      subscriptionCanceled
      redirectUrl
    }
  }
''')
