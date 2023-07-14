from gql import gql

queryPodcastImageAndTitleQuery = gql('''

query PodcastImageAndTitleQuery($podcastId: String!) {
  myPodcastById(podcastId: $podcastId) {
    id
    coverImageUrl
    title
  }
}
''')

queryMyPodcastById = gql('''

query MyPodcastById($podcastId: String!) {
  myPodcastById(podcastId: $podcastId) {
    id
    title
  }
}
''')

queryPodcastsMy = gql('''

query PodcastsMy {
  podcastsMy(limit: 300) {
    id
    title
  }
}
''')

queryUserPayoutDetailsQuery = gql('''

query UserPayoutDetailsQuery($userId: String!) {
  getPayoutPlanDetailsByUserId(userId: $userId) {
    ... on PayoutDetailsBusiness {
      id
      businessName
      businessVat
      emailForInvoice
      email
      street
      city
      postCode
      country
      iban
      accountNumber
      bic
      holder
      state
      bankName
    }
    ... on PayoutDetailsPrivate {
      id
      firstName
      lastName
      email
      street
      city
      postCode
      country
      iban
      accountNumber
      bic
      holder
      state
    }
  }
}
''')

queryHomeRssClaimsMyPending = gql('''

query HomeRssClaimsMyPending($title: String) {
  rssClaimsMyPending(limit: 100, title: $title) {
    id
    email
    rssClaimFlow
    rssClaimApproved
    rssClaimRejected
    podcast {
      id
      payoutAvailable
      coverImageUrl
      title
      followerCount
      episodesSummary {
        exclusiveEpisodeCount
        notExclusiveEpisodeCount
      }
    }
  }
}
''')

queryHomePodcastsMy = gql('''

query HomePodcastsMy($title: String) {
  podcastsMy(limit: 300, title: $title) {
    coverImageUrl
    id
    title
    description
    followerCount
    payoutAvailable
    open
    payoutPlan {
      title
      type
    }
    importPayoutPlan {
      title
      type
    }
  }
}
''')

queryHomePodcastsMyWithEpisodesCounts = gql('''

query HomePodcastsMyWithEpisodesCounts($title: String) {
  podcastsMy(limit: 300, title: $title) {
    coverImageUrl
    id
    title
    description
    followerCount
    episodesSummary {
      exclusiveEpisodeCount
      notExclusiveEpisodeCount
    }
    payoutAvailable
    open
    payoutPlan {
      title
      type
    }
    importPayoutPlan {
      title
      type
    }
  }
}
''')

queryStatisticsDataQuery = gql('''

query StatisticsDataQuery($podcastId: String!, $dateFrom: DateTime!, $dateTo: DateTime!, $timezone: String!) {
  podcastData: myPodcastById(podcastId: $podcastId) {
    id
    title
    datetime
    followerCount
    ratingScore {
      score
      total
    }
  }
  subscriberCountChange: getPodcastFollowers(
    podcastId: $podcastId
    dateFrom: $dateFrom
    dateTo: $dateTo
    timezone: $timezone
    grouping: TOTAL
  ) {
    value
  }
  allTimesStreams: getPodcastTotalStreams(podcastId: $podcastId) {
    streams
  }
  streamsChange: getPodcastStreamsChange(podcastId: $podcastId, dateFrom: $dateFrom, dateTo: $dateTo) {
    streams
  }
  allTimesCompletionRate: getPodcastCompleteRating(podcastId: $podcastId) {
    percent
  }
}
''')

queryChartsDataQuery = gql('''

query ChartsDataQuery($podcastId: String!, $dateFrom: DateTime!, $dateTo: DateTime!) {
  uniqueListenersByDayDataList: getPodcastUniqueListenPerDay(
    podcastId: $podcastId
    dateFrom: $dateFrom
    dateTo: $dateTo
  ) {
    x: date
    y: value
  }
  streamsByDayDataList: getPodcastStreamsPerDay(podcastId: $podcastId, dateFrom: $dateFrom, dateTo: $dateTo) {
    x: date
    y: value
  }
}
''')

queryEpisodesStatsDataQuery = gql('''

query EpisodesStatsDataQuery(
  $podcastId: String!
  $dateFrom: DateTime!
  $dateTo: DateTime!
  $limit: Int!
  $offset: Int!
  $sorting: EpisodeStatsTableSortingEnum!
) {
  episodesDataList: getPodcastEpisodesTable(
    podcastId: $podcastId
    dateFrom: $dateFrom
    dateTo: $dateTo
    limit: $limit
    offset: $offset
    sorting: $sorting
  ) {
    episode {
      id
      title
      imageUrl
    }
    releaseDate
    streams
    completionRate
    rating
  }
}
''')

queryMyPodcastQuery = gql('''

query MyPodcastQuery($podcastId: String!) {
  myPodcastById(podcastId: $podcastId) {
    id
    title
    datetime
  }
}
''')

queryPodcastEpisodeQuery = gql('''

query PodcastEpisodeQuery($podcastId: String!, $episodeId: String!) {
  myPodcastEpisodeById(podcastId: $podcastId, episodeId: $episodeId) {
    id
    title
    ratingScore {
      total
      score
    }
    totalStreams
    completionRate
    datetime
  }
}
''')

queryEpisodeStatsDataQuery = gql('''

query EpisodeStatsDataQuery($podcastId: String!, $episodeId: String!, $dateFrom: DateTime!, $dateTo: DateTime!) {
  streamsChange: getEpisodeStreamsChange(
    podcastId: $podcastId
    episodeId: $episodeId
    dateFrom: $dateFrom
    dateTo: $dateTo
  ) {
    streams
  }
  newListenersByDayDataList: getEpisodeUniqueListenPerDay(
    episodeId: $episodeId
    podcastId: $podcastId
    dateFrom: $dateFrom
    dateTo: $dateTo
  ) {
    x: date
    y: value
  }
  streamsByDayDataList: getEpisodeStreamsPerDay(
    episodeId: $episodeId
    podcastId: $podcastId
    dateFrom: $dateFrom
    dateTo: $dateTo
  ) {
    x: date
    y: value
  }
}
''')

queryPodcastsMyQuery = gql('''

query PodcastsMyQuery($limit: Int) {
  podcastsMy(limit: $limit) {
    coverImageUrl
    id
    title
  }
}
''')

queryDefaultPayoutPlanQuery = gql('''

query DefaultPayoutPlanQuery {
  getDefaultPayoutPlans {
    id
    type
    title
  }
  getDefaultImportPayoutPlans {
    id
    type
    title
  }
}
''')

queryCreateEpisodeButtonPodcastQuery = gql('''

query CreateEpisodeButtonPodcastQuery($podcastId: String!) {
  myPodcastById(podcastId: $podcastId) {
    id
    payoutPlan {
      type
    }
  }
}
''')

queryPodcastEpisodes = gql('''

query PodcastEpisodes($podcastId: String!, $limit: Int!, $offset: Int!) {
  podcastEpisodes(converted: false, published: false, podcastId: $podcastId, offset: $offset, limit: $limit) {
    id
    id
    description
    datetime
    podcastId
    podcastName
    publishDatetime
    status
    tags
    title
    imageUrl
    deepLink
    payoutPlan {
      shortTitle
    }
  }
}
''')

queryOverviewQuery = gql('''

query OverviewQuery($userId: String!, $podcastId: String!) {
  myPodcastById(podcastId: $podcastId) {
    id
    itunesId
    followerCount
    deepLink
    ratingScore {
      score
      total
    }
    payoutPlan {
      type
      premium
    }
    source
    episodesSummary {
      exclusiveEpisodeCount
      notExclusiveEpisodeCount
    }
    isNews
  }
  getPaymentProfiles(userId: $userId, podcastId: $podcastId) {
    id
    balance
    currency
  }
  podcastTransactionHistory(podcastId: $podcastId, limit: 100, offset: 0) {
    id
    datetime
    confirmed
    amount
    currency
    reason
    status
    type
    invoiceUrl
    cancelExternalNote
  }
  checkBalanceClaimStatus(podcastId: $podcastId)
}
''')

queryAudioResourceQuery = gql('''

query AudioResourceQuery($resourceId: String!) {
  resource: audioResource(resourceId: $resourceId) {
    id
    status
    url
  }
}
''')

queryVideoResourceQuery = gql('''

query VideoResourceQuery($resourceId: String!) {
  resource: videoResource(resourceId: $resourceId) {
    id
    status
    url
    imageUrl
  }
}
''')

querystreamMediaResource = gql('''

query streamMediaResource($resourceId: String!) {
  resource: streamMediaResource(resourceId: $resourceId) {
    id
    status
    url
    imageUrl
  }
}
''')

queryImageResourceQuery = gql('''

query ImageResourceQuery($resourceId: String!) {
  resource: imageResource(resourceId: $resourceId) {
    id
    status
    url
  }
}
''')

queryUsePodcastsExistQuery = gql('''

query UsePodcastsExistQuery($search: String!) {
  podcastsAutocomplete(search: $search) {
    id
    title
    coverImageUrl
    rss
  }
}
''')

queryCategoriesQuery = gql('''

query CategoriesQuery {
  podcastCategories(all: false) {
    id
    title
    subcategories {
      id
      title
    }
  }
}
''')

queryPodcastsItemQuery = gql('''

query PodcastsItemQuery($podcastId: String!) {
  myPodcastById(podcastId: $podcastId) {
    videos {
      id
      imageUrl
      mainTrailer
      title
      url
      status
    }
    images {
      coverImageUrl
      artworkUrl
      artworkOutstretchedUrl
    }
    coverImages {
      coverImageId
      coverImageUrl
      status
    }
    authorName
    datetime
    subcategoriesId
    coverImageId
    description
    id
    open
    title
    regions
    podcastType
    explicitContent
    webAddress
    language
    itunesId
    tags
    source
  }
}
''')

queryNewsEpisodeSegments = gql('''

query NewsEpisodeSegments($episodeId: String!) {
  newsEpisodeSegments(episodeId: $episodeId) {
    id
    title
    articleTitle
    articleUrl
    duration
    imageId
    imageUrl
    timestamp
  }
}
''')

queryPodcastEpisodesItem = gql('''

query PodcastEpisodesItem($podcastId: String!, $episodeId: String!) {
  myPodcastEpisodeById(podcastId: $podcastId, episodeId: $episodeId) {
    authorName
    audioId
    audioUrl
    duration
    audioStatus
    description
    id
    imageId
    imageUrl
    imageStatus
    publishDatetime
    tags
    title
    explicitContent
    deepLink
    introDuration
    streamMedia {
      id
      duration
      imageUrl
      status
      type
      url
    }
    payoutPlan {
      type
      premium
    }
  }
}
''')

queryEpisodeCreatePodcastQuery = gql('''

query EpisodeCreatePodcastQuery($podcastId: String!) {
  myPodcastById(podcastId: $podcastId) {
    id
    coverImageUrl
    coverImageId
    source
    isNews
  }
}
''')

queryPodcastPreviewQuery = gql('''

query PodcastPreviewQuery($rssUrl: String!) {
  rssClaimCheckByUrl(rssUrl: $rssUrl) {
    ... on RssClaimFeedFlow {
      feedPreview {
        data {
          title
          imageUrl
          email
        }
      }
    }

    ... on RssClaimExistFlow {
      podcast {
        id
        title
        coverImageUrl
      }
      feedPreview {
        data {
          email
        }
      }
    }
  }
}
''')

queryPayoutsQuery = gql('''

query PayoutsQuery {
  payoutClaims {
    id
    title
    status
    createdAt
    totalAmount
    currency
    invoiceNumber
    canceledExternalNote
  }
}
''')

queryNewPayoutsQuery = gql('''

query NewPayoutsQuery {
  payoutClaimInitialData {
    title
    claimedPodcasts {
      id
      podcast {
        id
        title
        coverImageUrl
      }
      amount
      currency
      items {
        status
        id
        amount
        currency
        reason
        createdAt
      }
    }
  }
}
''')

queryPayoutQuery = gql('''

query PayoutQuery($payoutId: String!) {
  payoutClaimById(id: $payoutId) {
    id
    status
    totalAmount
    currency
    createdAt
    title
    canceledExternalNote
    invoice {
      pdfUrl
    }
  }
  payoutClaimedPodcasts(claimId: $payoutId) {
    id
    status
    podcast {
      id
      title
      coverImageUrl
    }
    amount
    canceledExternalNote
    currency
    items {
      status
      id
      amount
      currency
      reason
      createdAt
    }
  }
}
''')

queryAffiliationCampaignsPartnerStatsQuery = gql('''

query AffiliationCampaignsPartnerStatsQuery {
  affiliationCampaignsPartnerStats {
    totalBalance
    totalClicks
    totalPaidAmount
    totalConversionsCount
  }
}
''')

queryAffiliationCampaignPartnerDataFind = gql('''

query AffiliationCampaignPartnerDataFind {
  affiliationCampaignPartnerDataFind(offset: 0, limit: 100) {
    id
    balance
    paidAmount
    clicks
    termsAndConditionsApprovedDatetime
    campaignId
    trackingLinkTemplate
    conversionsCount
    campaign {
      title
      status
      startDatetime
      endDatetime
      termsAndConditionsDescription
      termsAndConditionsPdfUrl
    }
  }
}
''')

queryEpisodePodcastItemQuery = gql('''

query EpisodePodcastItemQuery($podcastId: String!) {
  podcastById(podcastId: $podcastId) {
    id
    coverImageId
    coverImageUrl
    payoutPlan {
      premium
    }
    source
    isNews
  }
}
''')

queryRegionSettings = gql('''

query RegionSettings($region: String!) {
  regionSettings(region: $region) {
    id
    analytics
    payouts
    studioDisclaimers
    studioDisclaimerText
    showPayoutMenu
  }
}
''')

queryGetPodcastTotalStreams = gql('''

query GetPodcastTotalStreams($podcastId: String!) {
  getPodcastTotalStreams(podcastId: $podcastId) {
    streams
  }
}
''')

queryRssClaimRejectById = gql('''

mutation RssClaimRejectById($id: String!) {
  rssClaimRejectById(id: $id) {
    id
  }
}
''')

queryRssClaimResendEmailById = gql('''

mutation RssClaimResendEmailById($claimId: String!) {
  rssClaimResendEmailById(id: $claimId) {
    claimId
  }
}
''')

queryBusinessPayoutDetailsMutation = gql('''

mutation BusinessPayoutDetailsMutation(
  $userId: String!
  $businessName: String!
  $email: String!
  $street: String!
  $city: String!
  $postCode: String!
  $country: String!
  $iban: String
  $accountNumber: String
  $bic: String!
  $holder: String!
  $terms: Boolean!
  $state: String
  $businessVat: String!
  $bankName: String!
  $emailForInvoice: String
) {
  updateBusinessPayoutPlanDetails(
    userId: $userId
    businessName: $businessName
    email: $email
    street: $street
    city: $city
    postCode: $postCode
    country: $country
    iban: $iban
    accountNumber: $accountNumber
    bic: $bic
    holder: $holder
    terms: $terms
    state: $state
    businessVat: $businessVat
    bankName: $bankName
    emailForInvoice: $emailForInvoice
  ) {
    id
  }
}
''')

queryPrivatePayoutDetailsMutation = gql('''

mutation PrivatePayoutDetailsMutation(
  $userId: String!
  $firstName: String!
  $lastName: String!
  $email: String!
  $street: String!
  $city: String!
  $postCode: String!
  $country: String!
  $iban: String
  $accountNumber: String
  $bic: String!
  $holder: String!
  $terms: Boolean!
  $state: String
) {
  updatePrivatePayoutPlanDetails(
    userId: $userId
    firstName: $firstName
    lastName: $lastName
    email: $email
    street: $street
    city: $city
    postCode: $postCode
    country: $country
    iban: $iban
    accountNumber: $accountNumber
    bic: $bic
    holder: $holder
    terms: $terms
    state: $state
  ) {
    id
  }
}
''')

queryPodcastCreate = gql('''

mutation PodcastCreate($podcast: PodcastInput!) {
  podcastCreate(podcast: $podcast) {
    id
  }
}
''')

queryPodcastUpdate = gql('''

mutation PodcastUpdate($podcast: PodcastInput!, $podcastId: String!) {
  podcastUpdate(podcast: $podcast, podcastId: $podcastId) {
    authorName
    datetime
    categories {
      subcategories {
        id
      }
    }
    coverImageUrl
    coverImageId
    description
    id
    open
    title
    regions
    podcastType
    explicitContent
    webAddress
    language
    evergreen
    maleOriented
  }
}
''')

queryUpdatePodcastPayoutPlanMutation = gql('''

mutation UpdatePodcastPayoutPlanMutation($podcastId: String!, $payoutPlanId: String!) {
  updatePayoutPlanToPodcast(podcastId: $podcastId, payoutPlanId: $payoutPlanId) {
    payoutPlan {
      payoutPlanId
    }
  }
}
''')

queryClaimPaymentProfilePayout = gql('''

mutation ClaimPaymentProfilePayout($profileId: String!) {
  claimPaymentProfilePayout(profileId: $profileId) {
    id
  }
}
''')

queryPodcastEpisodesItemDelete = gql('''

mutation PodcastEpisodesItemDelete($podcastId: String!, $episodeId: String!) {
  podcastEpisodeDelete(podcastId: $podcastId, episodeId: $episodeId) {
    id
  }
}
''')

queryNewsEpisodeSegmentsDeleteAll = gql('''

mutation NewsEpisodeSegmentsDeleteAll($episodeId: String!) {
  newsEpisodeSegmentsDeleteAll(episodeId: $episodeId)
}
''')

queryNewsEpisodeSegmentCreate = gql('''

mutation NewsEpisodeSegmentCreate($input: NewsEpisodeSegmentInput!) {
  newsEpisodeSegmentCreate(input: $input) {
    id
    title
    articleTitle
    articleUrl
    duration
    imageId
    imageUrl
    timestamp
  }
}
''')

queryNewsEpisodeSegmentUpdate = gql('''

mutation NewsEpisodeSegmentUpdate($input: NewsEpisodeSegmentInput!) {
  newsEpisodeSegmentUpdate(input: $input) {
    id
    title
    articleTitle
    articleUrl
    duration
    imageId
    imageUrl
    timestamp
  }
}
''')

queryNewsEpisodeSegmentDelete = gql('''

mutation NewsEpisodeSegmentDelete($id: String!) {
  newsEpisodeSegmentDelete(id: $id)
}
''')

queryUploadsAudioFromUrl = gql('''

mutation UploadsAudioFromUrl($url: String!) {
  uploadsAudioFromUrl(url: $url) {
    id
  }
}
''')

queryUploadsVideoEpisodeFromUrl = gql('''

mutation UploadsVideoEpisodeFromUrl($url: String!) {
  uploadsVideoEpisodeFromUrl(url: $url) {
    id
  }
}
''')

queryPodcastEpisodesItemUpdate = gql('''

mutation PodcastEpisodesItemUpdate($podcastId: String!, $episode: PodcastEpisodeInput!, $episodeId: String!) {
  podcastEpisodeUpdate(episode: $episode, podcastId: $podcastId, episodeId: $episodeId) {
    authorName
    audioId
    audioUrl
    audioStatus
    description
    id
    imageId
    imageUrl
    imageStatus
    publishDatetime
    tags
    title
    explicitContent
    deepLink
    introDuration
    payoutPlan {
      type
    }
  }
}
''')

queryUserVerificationForm = gql('''

mutation UserVerificationForm($firstname: String!, $lastName: String!, $terms: Boolean) {
  userVerificationForm(firstName: $firstname, lastName: $lastName, terms: $terms) {
    id
    firstName
    lastName
  }
}
''')

queryPodcastNewsletterSwitchOnMutation = gql('''

mutation PodcastNewsletterSwitchOnMutation {
  userConsentRecordInsert(data: { type: PODCAST_NEWSLETTER }) {
    id
  }
}
''')

queryPodcastTipsNewsletterSwitchOnMutation = gql('''

mutation PodcastTipsNewsletterSwitchOnMutation {
  userConsentRecordInsert(data: { type: CREATOR_TIPS_NEWS_LETTER }) {
    id
  }
}
''')

queryPodcastExistClaimMutation = gql('''

mutation PodcastExistClaimMutation($podcastId: String!) {
  claimPodcastAsOwner(podcastId: $podcastId) {
    email
    claimId
  }
}
''')

queryClaimByUrlAsOwnerMutation = gql('''

mutation ClaimByUrlAsOwnerMutation($rssClaim: RssClaimFeedInput!) {
  rssClaimSubmitByUrlAsOwner(rssClaim: $rssClaim) {
    ... on RssClaimResponseSuccess {
      __typename
      sent
      email
      claimId
    }

    ... on RssClaimResponseNotTrusted {
      __typename
      sent
      email
      claimId
    }
  }
}
''')

queryRssClaimRejectByIdOnClaimFlow = gql('''

mutation RssClaimRejectByIdOnClaimFlow($id: String!) {
  rssClaimRejectById(id: $id) {
    id
  }
}
''')

queryRssClaimResendEmailByIdOnClaimFlow = gql('''

mutation RssClaimResendEmailByIdOnClaimFlow($claimId: String!) {
  rssClaimResendEmailById(id: $claimId) {
    claimId
  }
}
''')

queryClaimPayoutMutation = gql('''

mutation ClaimPayoutMutation($items: [String!]!, $title: String!) {
  payoutClaimCreate(items: $items, title: $title) {
    id
  }
}
''')

queryAffiliationCampaignTermsAndConditionsApprove = gql('''

mutation AffiliationCampaignTermsAndConditionsApprove($assignationId: String!) {
  affiliationCampaignTermsAndConditionsApprove(assignationId: $assignationId) {
    id
    balance
    paidAmount
    clicks
    termsAndConditionsApprovedDatetime
    campaignId
    trackingLinkTemplate
    campaign {
      title
      status
      startDatetime
      endDatetime
      termsAndConditionsDescription
      termsAndConditionsPdfUrl
    }
  }
}
''')

queryUserUiSettingsUpdate = gql('''

mutation UserUiSettingsUpdate($userUiSettingsUpdate: UserUISettingsInput!) {
  userUiSettingsUpdate(UserUISettings: $userUiSettingsUpdate) {
    studioUILanguage
  }
}
''')

queryMyUserUpdate = gql('''

mutation MyUserUpdate($myUser: MyUserUpdateInput!) {
  myUserUpdate(myUser: $myUser) {
    id
  }
}
''')

queryPodcastEpisodesNewItemCreate = gql('''

mutation PodcastEpisodesNewItemCreate($podcastId: String!, $episode: PodcastEpisodeInput!) {
  podcastEpisodeCreate(episode: $episode, podcastId: $podcastId) {
    id
  }
}
''')

queryPodcastAutocomplete = gql('''

query PodcastAutocomplete($search: String!) {
  podcastsAutocomplete(search: $search) {
    id
    title
    coverImageUrl
  }
}
''')

queryTokenWithCredentials = gql('''
query TokenWithCredentials($email: String!, $password: String!, $scope: UserScope!) {
  tokenWithCredentials(email: $email, password: $password, scope: $scope) {
  token
  emailVerified
  emailVerifyRequired
  frozenAccount
  __typename
}
}
''')

queryRegistrationPreFillQuery = gql('''

query RegistrationPreFillQuery($email: String!, $password: String!) {
  registrationPreFill(email: $email, password: $password) {
    email
    firstName
    lastName
    region
    token
  }
}
''')

queryUserProfileAffiliationDataQuery = gql('''

query UserProfileAffiliationDataQuery {
  affiliationCampaignPartnerDataFind(offset: 0, limit: 1) {
    id
  }
}
''')

queryUserPofileQuery = gql('''

query UserPofileQuery {
  userProfile {
    id
    firstName
    region
    originalRegion
    middleName
    lastName
    displayName
    email
  }
  payoutClaimAvailable
  userHavePayoutDetails
  userSettings {
    newsletterModalShownDatetime
    enableVideoUploadDatetime
    enableVideoTrailerUploadDatetime
  }
  podcastNewsletter: userConsentRecord(recordType: PODCAST_NEWSLETTER) {
    id
  }
  podcastTipsNewsletter: userConsentRecord(recordType: CREATOR_TIPS_NEWS_LETTER) {
    id
  }
}
''')

queryTokenTest = gql('''

query TokenTest($jwt: String!) {
  tokenTest(jwt: $jwt) {
    token
    emailVerified
    emailVerifyRequired
    frozenAccount
  }
}
''')

queryDisablePodcastAsOwner = gql('''

mutation DisablePodcastAsOwner($podcastId: String!) {
  disablePodcastAsOwner(id: $podcastId) {
    email
  }
}
''')

queryVerifyEmail = gql('''

mutation VerifyEmail($token: String!) {
  verifyEmail(token: $token) {
    token
  }
}
''')

query = gql('''

mutation Free12MonthStudioPremium($token: String!) {
  free12MonthStudioPremium(token: $token) {
    token
  }
}
''')

queryRemovePodcastMutation = gql('''

mutation RemovePodcastMutation($code: String!) {
  disablePodcastByCode(code: $code) {
    id
    podcast {
      id
      title
    }
    status
  }
}
''')

queryClaimPodcastMutation = gql('''

mutation ClaimPodcastMutation($code: String!) {
  claimPodcastFromEmail(code: $code) {
    id
    podcast {
      id
      title
    }
    status
  }
}
''')

queryVerifyRssClaimByCodeMutation = gql('''

mutation VerifyRssClaimByCodeMutation($code: String!) {
  rssClaimFromEmail(code: $code) {
    podcast {
      id
      coverImageUrl
      title
    }
  }
}
''')

query = gql('''
	query ($showID: String!) {
		publicPodcastById(
			podcastId: $showID
		) {
			title
			coverImageUrl
			authorName
			ratingCount
			ratingScore
			badge
			episodes(limit: 1) {
				duration
			}
		}
	}
''')

queryweb_getShow = gql('''
	query web_getShow($showID: String!, $region: String) {
		publicPodcastById (
			podcastId: $showID
		) {
			id
			badge
			title
			coverImageUrl
			followerCount
			ratingScore
			ratingCount
			description
			audioTrailers
			authorName
			videos {
				id
				url
			}
			categories {
				id
				title
			}
			episodes {
				id
				description
				ratingScore
				ratingCount
				imageUrl
				title
				publishDatetime
				duration
			}
		}
		publicPodcastCategories(region: $region) {
			id
			translations {
				region
				title
			}
		}
	}
''')

queryweb_publicResourceById = gql('''
	query web_publicResourceById($showID: String!, $region: String!) {
		publicResourceById (
			resourceId: $showID
			region: $region
		) {
			... on PublicPodcastResource {
				id
				badge
				title
				images {
					cover {
						url
					}
				}
				followerCount
				ratingScore
				ratingCount
				description
				audioTrailers
				authorName
				videoTrailers {
					id
					url
				}
				categories {
					id
					title
					translations {
						region
						title
					}
				}
				episodes {
					id
					description
					ratingScore
					ratingCount
					imageUrl
					title
					publishDatetime
					duration
				}
				texts {
					name
					text
				}
			}
			... on PublicAudiobook {
				id
				title
				images {
					cover {
						url
					}
				}
				description
				authorNames
				videoTrailers {
					id
					url
				}
				texts {
					name
					text
				}
			}
		}
	}
''')

queryweb_getModalContentEpisode = gql('''
	query web_getModalContentEpisode($showId: String!, $episodeId: String!) {
		publicPodcastEpisodeById(
			podcastId: $showId
			episodeId: $episodeId
		) {
			id
			description
			podcastId
			imageUrl
			title
			ratingCount
			ratingScore
			publishDatetime
			duration
		}
	}
''')

queryweb_getModalContentPodcast = gql('''
	query web_getModalContentPodcast($showId: String!) {
		publicPodcastById(
			podcastId: $showId
		) {
			id
			title
			coverImageUrl
			audioTrailers
			ratingCount
			ratingScore
			followerCount
			description
		}
	}
''')

queryweb_getPremiumShows = gql('''
	query web_getPremiumShows($showId: String!) {
		publicPodcastById (
			podcastId: $showId
		) {
			coverImageUrl
			id
			title
			audioTrailers
		}
	}
''')

queryweb_getEpisode = gql('''
	query web_getEpisode($episodeId: String!, $podcastId: String!) {
		publicPodcastEpisodeById (
			episodeId: $episodeId
			podcastId: $podcastId
		) {
			id
			description
			podcastId
			imageUrl
			title
			ratingScore
			ratingCount
			publishDatetime
			duration

		}
	}
''')

queryweb_getEpisodePodcast = gql('''
	query web_getEpisodePodcast($podcastId: String!) {
		publicPodcastById (
			podcastId: $podcastId
		) {
			title
			id
			episodes {
				id
				description
				ratingScore
				ratingCount
				imageUrl
				title
				publishDatetime
				duration
			}
		}
	}
''')

queryweb_GetEpisodeAudio = gql('''
	query web_GetEpisodeAudio( $hash: String! ) {
		publicPodcastEpisodeAudio(
			hash: $hash
		) {
			duration
			url
		}
	}
''')

queryweb_getRefererData = gql('''
	query web_getRefererData($referer: String!) {
		refererByRefererCode(
			referer: $referer
		) {
			duration
			unit
		}
	}
''')

queryweb_getPasswordResetEmail = gql('''
	query web_getPasswordResetEmail( $token: String! ) {
		passwordResetUser( passwordResetToken: $token ) {
			email
		}
	}
''')

queryweb_forgotPassword = gql('''
	query web_forgotPassword( $email: String! ) {
		passwordReset(
			email: $email
			source: WEB
		) {
			sent
		}
	}
''')

queryweb_freeDaysCount = gql('''
	query web_freeDaysCount($paymentPlanId: String!, $region: String!) {
		freeDaysCount(
			paymentPlanId: $paymentPlanId
			region: $region
		) {
			days
		}
	}
''')

queryweb_registerFbUser = gql('''
	query web_registerFbUser(
		$locale: String,
		$facebookToken: String!,
		$referer: String,
		$region: String,
		$clickId: String,
		$appsFlyerId: String,
		$paymentRequired: Boolean,
		$facebookFBC: String,
		$facebookFBP: String,
		$facebookPixelId: String
	) {
		tokenWithFacebookToken(
			scope: MOBILE,
			facebookToken: $facebookToken,
			locale: $locale,
			source: WEB,
			referer: $referer,
			region: $region,
			paymentRequired: $paymentRequired,
			clickId: $clickId,
			appsFlyerId: $appsFlyerId
			facebookFBC: $facebookFBC
			facebookFBP: $facebookFBP
			facebookPixelId: $facebookPixelId
		) {
			token
			isNewUser
		}
	}
''')

queryweb_autoLogin = gql('''
	query web_autoLogin(
		$autoLoginToken: String!
		$locale: String!
	) {
		tokenWithAutoLoginToken(
			autoLoginToken: $autoLoginToken
			locale: $locale
			source: WEB
		) {
			token
		}
	}
''')

queryweb_logInUser = gql('''
	query web_logInUser($email: String!, $password: String!) {
		tokenWithCredentials(
			email: $email
			password: $password
		) {
			token
			isNewUser
		}
	}
''')

queryweb_tokenTest = gql('''
	query web_tokenTest($jwt:String!) {
		tokenTest(
			jwt: $jwt
		) {
			token
		}
	}
''')

queryweb_getUserData = gql('''
	query web_getUserData{
		userProfile {
			id
			displayName
			email
			role
			datetime
			firstName
			lastName
			paymentPlan
			region
			exPremium
			isMigratedToPremiumPlus
			referer
			podcasts {
				artworkUrl
				id
				title
			}
			subscription {
				... on UserSubscriptionPlanFree {
					description
					finishesDatetime
					startedDatetime
				}
				... on UserSubscriptionPlanFreeTrail {
					description
					finished
					started
					finishesDatetime
					startedDatetime
				}
				... on UserSubscriptionPlanPremium {
					productId
					description
					startedDatetime
					nextBilling
					name
					paymentPeriod
					paymentMethod
					isPlus
					canCancel
					promoCode
				}
			}
		}
	}
''')

queryweb_getCreditCardInfo = gql('''
	query web_getCreditCardInfo($userId: String!) {
		userPaymentSubscription(
			userId: $userId
		) {
			id
			datetime
			status
			endDate
			productId
			price
			currency
			cardSummary
			cardHolderName
			cardExpiryDate
			cardType
		}
	}
''')

queryweb_getMyPodcasts = gql('''
	query web_getMyPodcasts {
		podcastsFollowed {
			id
			thumbnailUrl
			title
		}
	}
''')

queryweb_getPayments = gql('''
	query web_getPayments( $userId: String ) {
		userPaymentTransactions(
			userId: $userId
		) {
			id
			datetime
			status
			price
			currency
			cardSummary
			cardExpiryDate
			cardType
			transactionId
			invoiceUrl
			paymentMethod
		}
	}
''')

queryweb_upgradePriceCheck = gql('''
	query web_upgradePriceCheck($paymentPlanId: String!) {
		upgradePrice(
			paymentPlanId: $paymentPlanId
		) {
			price
			currency
		}
	}
''')

queryweb_getPaymentProviders = gql('''
	query web_getPaymentProviders($region: String!, $userId: String!) {
		getPaymentProviders(
			region: $region
			userId: $userId
		) {
			type
		}
	}
''')

queryweb_initPaymentPlan = gql('''
	query web_initPaymentPlan($region: String!, $source: String, $name: String) {
		getPaymentPlan(
			region: $region
			source: $source
			name: $name
		) {
			id
			price
			currency
			duration
			unit
			freeTrial
			freeTrialUnit
			bonus
			bonusUnit
		}
	}
''')

queryweb_initAdyen = gql('''
	query web_initAdyen($country: String!, $region: String!, $userId: String!, $paymentPlanId: String!, $change: Boolean, $locale: String){
		getAdyenPaymentMethods(
			region: $region
			countryCode: $country
			userId: $userId
			paymentPlanId: $paymentPlanId
			change: $change
			locale: $locale
		){
			groups {
				name
				types
				groupType
			}
			oneClickPaymentMethods {
				name
				type
				paymentMethodData
				recurringDetailReference
				supportsRecurring
				group {
					type
					name
					paymentMethodData
				}
			}
			paymentMethods {
				brands
				group {
					type
					name
					paymentMethodData
				}
				name
				paymentMethodData
				supportsRecurring
				type
				extraConfiguration {
					amount {
						value
						currency
					}
					paypal {
						merchantId
					}
				}
				details {
					key
					type
					optional
					value
					items {
						name
						id
					}
				}
			}
		}
	}
''')

queryweb_getPaymentCards = gql('''
	query web_getPaymentCards($userId: String!) {
		getPaymentCards(
			userId: $userId
		) {
			id
			datetime
			main
			cardSummary
			expiryDate
			type
		}
	}
''')

queryweb_getUserDailyFeed = gql('''
	query web_getUserDailyFeed($limit: Float) {
		userDailyFeed (
			limit: $limit
		) {
			items {
				... on UserDailyFeedRecommendedPremier {
					podcast {
						id
						coverImageUrl
						title
					}
				}
				... on UserDailyFeedRecommendedPodcast {
					label
					podcast {
						id
						coverImageUrl
						title
					}
				}
			}
		}
	}
''')

queryweb_signUpWithApple = gql('''
	query web_signUpWithApple(
		$authorizationCode: String!,
		$identityToken: String!,
		$personalInfo: ApplePersonalInfo,
		$locale: String,
		$region: String,
		$appsFlyerId: String,
		$referer: String,
		$paymentRequired: Boolean
	) {
		tokenWithAppleToken (
			authorizationCode: $authorizationCode,
			identityToken: $identityToken,
			personalInfo: $personalInfo,
			source: WEB,
			locale: $locale,
			region: $region,
			appsFlyerId: $appsFlyerId,
			referer: $referer
			paymentRequired: $paymentRequired
		) {
			emailVerified
			emailVerifyRequired
			frozenAccount
			isNewUser
			token
		}
	}
''')

querywebG_signInWithGoogle = gql('''
	query webG_signInWithGoogle(
		$identityToken: String!,
		$locale: String,
		$region: String,
		$appsFlyerId: String,
		$referer: String,
		$paymentRequired: Boolean,
		$facebookFBC: String,
		$facebookFBP: String,
		$facebookPixelId: String
	) {
		tokenWithGoogleToken(
			source: WEB,
			identityToken: $identityToken,
			locale: $locale,
			region: $region,
			appsFlyerId: $appsFlyerId,
			referer: $referer,
			paymentRequired: $paymentRequired,
			facebookFBC: $facebookFBC,
			facebookFBP: $facebookFBP,
			facebookPixelId: $facebookPixelId
		) {
			token,
			isNewUser
		}
	}
''')

queryweb_getCategories = gql('''
	query web_getCategories($region: String) {
		publicPodcastCategories (
			region: $region
		) {
			id
			title
			coverImageUrl
		}
	}
''')

queryweb_autoLoginToken = gql('''
	query web_autoLoginToken {
		autologinCreateToken {
			token
		}
	}
''')

queryweb_getBillingsSettings = gql('''
	query web_getBillingsSettings($id: String!) {
		getBillingSettings(id: $id) {
			productId
			hasAuthorizedPaymentMethod
			paymentMethods {
				cardDetails {
					cardSummary
					cardType
					validThrough
				}
				type
				main
				creationDate
			}
		}
	}
''')

queryweb_getUserContactPermission = gql('''
	query web_getUserContactPermission {
		userConsentRecord( recordType: NEWSLETTER ) {
			type
			id
		}
	}
''')

queryweb_getSuccessScreenEditorsPlaylist = gql('''
	query web_getSuccessScreenEditorsPlaylist($region: String!) {
		publicEditorsCollections(region: $region) {
			items(limit: 3) {
				... on PublicPodcastResource {
					id
					images {
						cover {
							url
						}
					}
				}
				... on PublicAudiobook {
					id
					images {
						cover {
							url
						}
					}
				}
			}
		}
	}
''')

queryweb_getPlanDescription = gql('''
	query web_getPlanDescription($paymentPlanCode: String, $paymentPlanid: String) {
		getPlanDescription(paymentPlanCode: $paymentPlanCode, paymentPlanId: $paymentPlanid) {
			name
			id
		}
	}
''')

queryweb_resetPassword = gql('''
	mutation web_resetPassword($token: String!, $password: String!) {
		passwordResetToNew(passwordResetToken: $token, password: $password){
			token
		}
	}
''')

queryweb_userSignup = gql('''
	mutation web_userSignup(
		$email: String!,
		$password: String!,
		$firstName: String!,
		$lastName: String,
		$referer: String,
		$region: String,
		$clickId: String,
		$appsFlyerId: String,
		$paymentRequired: Boolean,
		$facebookFBC: String,
		$facebookFBP: String,
		$facebookPixelId: String
	) {
		registrationWithEmail( payload: {
			role: MOBILE
			email: $email
			password: $password
			firstName: $firstName
			lastName: $lastName
			referer: $referer
			source: WEB
			region: $region
			paymentRequired: $paymentRequired
			clickId: $clickId
			appsFlyerId: $appsFlyerId
			facebookFBC: $facebookFBC
			facebookFBP: $facebookFBP
			facebookPixelId: $facebookPixelId
		}) {
			token
			isNewUser
		}
	}
''')

queryweb_resubscribe = gql('''
	mutation web_resubscribe($paymentPlanId: String) {
		resubscribe(paymentPlanId: $paymentPlanId)
	}
''')

queryweb_cancelSubscription = gql('''
	mutation web_cancelSubscription($userId: String!) {
		cancelActiveSubscription(
			userId: $userId
		)
	}
''')

queryweb_cancelUserSubscription = gql('''
	mutation web_cancelUserSubscription( $userId: String, $provider: String! ) {
		userSubscriptionCancel( userId: $userId, provider: $provider ) {
			subscriptionCanceled
			redirectUrl
		}
	}
''')

queryweb_updateUserData = gql('''
	mutation web_updateUserData($myUser: MyUserUpdateInput!) {
		myUserUpdate(
			myUser: $myUser
		) {
			id
			displayName
			email
			role
			datetime
			firstName
			lastName
			paymentPlan
			region
			subscription {
				... on UserSubscriptionPlanFree {
					description
					finishesDatetime
					startedDatetime
				}
				... on UserSubscriptionPlanFreeTrail {
					description
					finished
					started
					finishesDatetime
					startedDatetime
				}
				... on UserSubscriptionPlanPremium {
					description
					startedDatetime
					nextBilling
					name
					paymentPeriod
				}
			}
		}
	}
''')

queryweb_followPodcast = gql('''
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

queryweb_downgradeSubscription = gql('''
	mutation web_downgradeSubscription($paymentPlanId: String) {
		resubscribe(paymentPlanId: $paymentPlanId)
	}
''')

queryweb_upgradeSubscription = gql('''
	mutation web_upgradeSubscription($paymentPlanId: String!) {
		upgradeSubscription(paymentPlanId: $paymentPlanId)
	}
''')

queryweb_payAdyen = gql('''
	mutation web_payAdyen($authorizationOnly: Boolean, $payload: AdyenPaymentInput!, $userId: String!, $paymentPlanId: String!, $change: Boolean) {
		postAdyenPayment(
			payload: $payload
			userId: $userId
			paymentPlanId: $paymentPlanId
			change: $change
			authorizationOnly: $authorizationOnly
		) {
			id
			details {
				key
				type
				optional
				value
			}
			redirect
			refusalReason
			refusalReasonCode
			resultCode
			action
		}
	}
''')

queryweb_adyenDetails = gql('''
	mutation web_adyenDetails($payload: AdyenPaymentDetailsInput!, $userId: String!, $paymentPlanId: String!, $change: Boolean) {
		postAdyenPaymentDetails (
			payload: $payload
			userId: $userId
			paymentPlanId: $paymentPlanId,
			change: $change
		) {
			id
			details {
				key
				type
				optional
				value
			}
			redirect
			refusalReason
			refusalReasonCode
			resultCode
			action
		}
	}
''')

queryweb_setMainCard = gql('''
	mutation web_setMainCard($cardId: String!) {
		setMainPaymentCard(
			cardId: $cardId
		) {
			id
			datetime
			main
			cardSummary
			expiryDate
			type

		}
	}
''')

queryweb_giftCardCodeRedeem = gql('''
	mutation web_giftCardCodeRedeem( $code: String!) {
		giftCardCodeRedeem(code: $code) {
			status
			subscriptionEndDate
			error
		}
	}
''')

queryweb_externalSubscriptionClaim = gql('''
	mutation web_externalSubscriptionClaim($subscription: ExternalProviderManagedSubscriptionInput!) {
		externalSubscriptionClaim(subscription: $subscription) {
			claimDatetime
			product
			subscriptionId
			subscriptionStatus
		}
	}
''')

queryweb_removeContactPermission = gql('''
	mutation web_removeContactPermission($id: String!) {
		userConsentRecordDelete( id: $id )
	}
''')

queryweb_registerContactPermission = gql('''
	mutation web_registerContactPermission($userId: String) {
		userConsentRecordInsert(
			data: {
				type: NEWSLETTER
				userId: $userId
			}
		) {
			id
			datetime
			type
			ip
		}
	}
''')
