from gql import gql

mutationweb_resetPassword = gql('''
	mutation web_resetPassword($token: String!, $password: String!) {
		passwordResetToNew(passwordResetToken: $token, password: $password){
			token
		}
	}
''')

mutationweb_userSignup = gql('''
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

mutationweb_resubscribe = gql('''
	mutation web_resubscribe($paymentPlanId: String) {
		resubscribe(paymentPlanId: $paymentPlanId)
	}
''')

mutationweb_cancelSubscription = gql('''
	mutation web_cancelSubscription($userId: String!) {
		cancelActiveSubscription(
			userId: $userId
		)
	}
''')

mutationweb_cancelUserSubscription = gql('''
	mutation web_cancelUserSubscription( $userId: String, $provider: String! ) {
		userSubscriptionCancel( userId: $userId, provider: $provider ) {
			subscriptionCanceled
			redirectUrl
		}
	}
''')

mutationweb_updateUserData = gql('''
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

mutationweb_followPodcast = gql('''
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

mutationweb_downgradeSubscription = gql('''
	mutation web_downgradeSubscription($paymentPlanId: String) {
		resubscribe(paymentPlanId: $paymentPlanId)
	}
''')

mutationweb_upgradeSubscription = gql('''
	mutation web_upgradeSubscription($paymentPlanId: String!) {
		upgradeSubscription(paymentPlanId: $paymentPlanId)
	}
''')

mutationweb_payAdyen = gql('''
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

mutationweb_adyenDetails = gql('''
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

mutationweb_setMainCard = gql('''
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

mutationweb_giftCardCodeRedeem = gql('''
	mutation web_giftCardCodeRedeem( $code: String!) {
		giftCardCodeRedeem(code: $code) {
			status
			subscriptionEndDate
			error
		}
	}
''')

mutationweb_externalSubscriptionClaim = gql('''
	mutation web_externalSubscriptionClaim($subscription: ExternalProviderManagedSubscriptionInput!) {
		externalSubscriptionClaim(subscription: $subscription) {
			claimDatetime
			product
			subscriptionId
			subscriptionStatus
		}
	}
''')

mutationweb_removeContactPermission = gql('''
	mutation web_removeContactPermission($id: String!) {
		userConsentRecordDelete( id: $id )
	}
''')

mutationweb_registerContactPermission = gql('''
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
