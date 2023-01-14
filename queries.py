from gql import gql, Client

queryTokenWithCredentialsScoped = gql('''
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

queryTokenWithCredentials = gql('''
  query TokenWithCredentials($email: String!, $password: String!) {
    tokenWithCredentials(email: $email, password: $password) {
      token
      emailVerified
      emailVerifyRequired
      frozenAccount
      __typename
    }
  }
''')

queryRequestPasswordReset = gql('''
  query RequestPasswordReset($email: String!, $source: UserSource!) {
    passwordReset(email: $email, source: $source) {
      sent
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

queryPodcastImageAndTitleQuery = gql('''
  query PodcastImageAndTitleQuery($podcastId: String!) {
    myPodcastById(podcastId: $podcastId) {
      id
      coverImageUrl
      title
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

queryPodcastEpisodesQuery = gql('''
  query PodcastEpisodesQuery($podcastId: String!, $limit: Int!, $offset: Int!, $sorting: PodcastEpisodeSorting, $ignoreTrailers: Boolean) {
    podcastEpisodes(
      podcastId: $podcastId
      converted: true
      published: true
      limit: $limit
      offset: $offset
      sorting: $sorting
      ignoreTrailers: $ignoreTrailers
    ) {
      ...EpisodeBase
      __typename
    }
  }
  
  fragment EpisodeBase on PodcastEpisode {
    accessLevel
    audio {
      url
      duration
      hlsUrl
      __typename
    }
    artist
    description
    datetime
    id
    imageUrl
    podcastName
    title
    thumbnailUrl
    podcastId
    ratingScore {
      score
      total
      __typename
    }
    premiumBadge
    evergreen
    isMarkedAsPlayed
    streamMedia {
      duration
      id
      imageUrl
      status
      type
      url
      bandwidths {
        quality
        rate
        type
        __typename
      }
      __typename
    }
    introDuration
    type: source
    __typename
  }
''')

queryWebDoSearchAudiobook = gql('''
  query web_doSearch($search: String!, $region: String!) {
    publicSearch (search: $search, region: $region, searchType: AUDIOBOOK) {
      __typename
      ... on PublicAudiobook {
        id
        title
        coverImageUrl
        authorNames
        badge
        __typename
      }
    }
  }
''')

queryWebDoSearchPodcast = gql('''
query web_doSearch($search: String!, $region: String!) {
  publicSearch(search: $search, region: $region, searchType: PODCAST) {
    __typename
    ... on PublicPodcast {
      id
      title
      coverImageUrl
      authorName
      badge
      __typename
    }
  }
}
''')

queryWebGetCreditCardInfo = gql('''
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

queryWebGetPayments = gql('''
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

queryWebGetPaymentCards = gql('''
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
      __typename
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
        __typename
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
        __typename
      }
      __typename
    }
  }
''')

queryProfileResultsQuery = gql('''
  query ProfileResultsQuery {
    userProfile {
      ...UserProfileFragment
      __typename
    }
  }

  fragment UserProfileFragment on User {
    id
    displayName
    regionMetadata {
      region
      isPremiumPlusEnabled
      __typename
    }
    datetime
    role
    exPremium
    paymentPlan
    subscription {
      __typename
      ... on UserSubscriptionPlanFreeTrail {
        finished
        isPlus
        __typename
      }
      ... on UserSubscriptionPlanPremium {
        isPlus
        paymentPeriod
        __typename
      }
    }
    __typename
  }
''')



queryAudiobookResultsQuery = gql('''
query AudiobookResultsQuery($id: String!) {
  audiobookById(id: $id) {
    ...AudiobookScreenFragment
    __typename
  }
}

fragment AudiobookScreenFragment on Audiobook {
  id
  title
  authorNames
  authors {
    name
    id
    __typename
  }
  narrators {
    name
    __typename
  }
  accessLevel
  description
  yearOfBookPublication
  publisherName
  duration
  ...AudiobookCoverImageFragment
  ...AudiobookLanguageFragment
  ...AudioBookUserStateFragment
  __typename
}

fragment AudiobookCoverImageFragment on Audiobook {
  coverImage {
    url
    mainColor
    __typename
  }
  __typename
}

fragment AudiobookLanguageFragment on Audiobook {
  language {
    isoLanguage
    localisedLanguage
    __typename
  }
  __typename
}

fragment AudioBookUserStateFragment on Audiobook {
  userState {
    progress
    listenTime
    isAddedToLibrary
    isMarkedAsPlayed
    __typename
  }
  __typename
}
''')
