import requests
import json
import csv
from urllib.parse import urlencode
import os

def get_data(address, page_size):
    if not isinstance(address, str):
        raise ValueError("Address must be a string")
    if not isinstance(page_size, int) or page_size <= 0:
        raise ValueError("Page size must be a positive integer")

    url = "https://www.booking.com/dml/graphql"
    
    query_params = build_query_params()
    headers = build_headers()
    file_path = './listings.csv'
    print(f"Attempting to save to: {os.path.abspath(file_path)}")

    payload = {
        "operationName": "FullSearch",
        "variables": {
            "input": {
                "acidCarouselContext": None,
                "childrenAges": [],
                "dates": {
                    "checkin": "2024-06-18",
                    "checkout": "2024-06-19"
                },
                "doAvailabilityCheck": False,
                "encodedAutocompleteMeta": None,
                "enableCampaigns": True,
                "filters": {
                    "selectedFilters": "distance=3000"
                },
                "selectedFilterSources": [
                    "PREVIOUS"
                ],
                "flexibleDatesConfig": {
                    "broadDatesCalendar": {
                        "checkinMonths": [],
                        "los": [],
                        "startWeekdays": []
                    },
                    "dateFlexUseCase": "DATE_RANGE",
                    "dateRangeCalendar": {
                        "checkin": [
                            "2024-06-18"
                        ],
                        "checkout": [
                            "2024-06-19"
                        ]
                    }
                },
                "forcedBlocks": None,
                "location": {
                    "searchString": "Bangalore",
                    "destType": "LATLONG",
                    "latitude": 41.8804017,
                    "longitude": -87.6302038
                },
                "metaContext": {
                    "metaCampaignId": 0,
                    "externalTotalPrice": None,
                    "feedPrice": None,
                    "hotelCenterAccountId": None,
                    "rateRuleId": None,
                    "dragongateTraceId": None,
                    "pricingProductsTag": None
                },
                "nbRooms": 1,
                "nbAdults": 1,
                "nbChildren": 0,
                "showAparthotelAsHotel": True,
                "needsRoomsMatch": False,
                "optionalFeatures": {
                    "forceArpExperiments": True,
                    "testProperties": False
                },
                "pagination": {
                    "rowsPerPage": 50,
                    "offset": 0
                },
                "rawQueryForSession": "/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4AofIxbMGwAIB0gIkNDFkMDkyZDktMDFlZC00NzMxLTkyMjMtNGFhYWIxNjEwMjg12AIF4AIB&sid=aa4f62f572ac5f487c282f0f11ec409c&aid=304142&ss=Bangalore&ssne=Bangalore&ssne_untouched=Bangalore&lang=en-gb&src=index&dest_id=-2090174&dest_type=city&checkin=2024-06-18&checkout=2024-06-19&group_adults=1&no_rooms=1&group_children=0&nflt=distance%3D3000",
                "referrerBlock": None,
                "sbCalendarOpen": False,
                "sorters": {
                    "selectedSorter": None,
                    "referenceGeoId": None,
                    "tripTypeIntentId": None
                },
                "travelPurpose": 2,
                "seoThemeIds": [],
                "useSearchParamsFromSession": True,
                "merchInput": {
                    "testCampaignIds": []
                }
            },
            "carouselLowCodeExp": False
        },
        "extensions": {},
        "query": """query FullSearch($input: SearchQueryInput!, $carouselLowCodeExp: Boolean!) {
          searchQueries {
            search(input: $input) {
              ...FullSearchFragment
              __typename
            }
            __typename
          }
        }

        fragment FullSearchFragment on SearchQueryOutput {
          banners {
            ...Banner
            __typename
          }
          breadcrumbs {
            ... on SearchResultsBreadcrumb {
              ...SearchResultsBreadcrumb
              __typename
            }
            ... on LandingPageBreadcrumb {
              ...LandingPageBreadcrumb
              __typename
            }
            __typename
          }
          carousels {
            ...Carousel
            __typename
          }
          destinationLocation {
            ...DestinationLocation
            __typename
          }
          entireHomesSearchEnabled
          dateFlexibilityOptions {
            enabled
            __typename
          }
          flexibleDatesConfig {
            broadDatesCalendar {
              checkinMonths
              los
              startWeekdays
              losType
              __typename
            }
            dateFlexUseCase
            dateRangeCalendar {
              flexWindow
              checkin
              checkout
              __typename
            }
            __typename
          }
          filters {
            ...FilterData
            __typename
          }
          filtersTrackOnView {
            type
            experimentHash
            value
            __typename
          }
          appliedFilterOptions {
            ...FilterOption
            __typename
          }
          recommendedFilterOptions {
            ...FilterOption
            __typename
          }
          pagination {
            nbResultsPerPage
            nbResultsTotal
            __typename
          }
          tripTypes {
            ...TripTypesData
            __typename
          }
          results {
            ...BasicPropertyData
            ...MatchingUnitConfigurations
            ...PropertyBlocks
            ...BookerExperienceData
            priceDisplayInfoIrene {
              ...PriceDisplayInfoIrene
              __typename
            }
            licenseDetails {
              nextToHotelName
              __typename
            }
            isTpiExclusiveProperty
            propertyCribsAvailabilityLabel
            mlBookingHomeTags
            trackOnView {
              experimentTag
              __typename
            }
            __typename
          }
          searchMeta {
            ...SearchMetadata
            __typename
          }
          sorters {
            option {
              ...SorterFields
              __typename
            }
            __typename
          }
          oneOfThreeDeal {
            ...OneOfThreeDeal
            __typename
          }
          zeroResultsSection {
            ...ZeroResultsSection
            __typename
          }
          rocketmilesSearchUuid
          previousSearches {
            ...PreviousSearches
            __typename
          }
          frontierThemes {
            ...FrontierThemes
            __typename
          }
          merchComponents {
            ...MerchRegionIrene
            __typename
          }
          wishlistData {
            numProperties
            __typename
          }
          seoThemes {
            id
            caption
            __typename
          }
          __typename
        }

        fragment BasicPropertyData on SearchResultProperty {
          acceptsWalletCredit
          basicPropertyData {
            accommodationTypeId
            id
            isTestProperty
            location {
              address
              city
              countryCode
              __typename
            }
            pageName
            ufi
            photos {
              main {
                highResUrl {
                  relativeUrl
                  __typename
                }
                lowResUrl {
                  relativeUrl
                  __typename
                }
                highResJpegUrl {
                  relativeUrl
                  __typename
                }
                lowResJpegUrl {
                  relativeUrl
                  __typename
                }
                __typename
              }
              __typename
            }
            reviewScore: reviews {
              score: totalScore
              reviewCount: reviewsCount
              totalScoreTextTag {
                translation
                __typename
              }
              showScore
              secondaryScore
              secondaryTextTag {
                translation
                __typename
              }
              showSecondaryScore
              __typename
            }
            externalReviewScore: externalReviews {
              score: totalScore
              reviewCount: reviewsCount
              showScore
              totalScoreTextTag {
                translation
                __typename
              }
              __typename
            }
            starRating {
              value
              symbol
              caption {
                translation
                __typename
              }
              tocLink {
                translation
                __typename
              }
              showAdditionalInfoIcon
              __typename
            }
            isClosed
            paymentConfig {
              installments {
                minPriceFormatted
                maxAcceptCount
                __typename
              }
              __typename
            }
            __typename
          }
          badges {
            caption {
              translation
              __typename
            }
            closedFacilities {
              startDate
              endDate
              __typename
            }
            __typename
          }
          customBadges {
            showSkiToDoor
            showBhTravelCreditBadge
            showOnlineCheckinBadge
            __typename
          }
          description {
            text
            __typename
          }
          displayName {
            text
            translationTag {
              translation
              __typename
            }
            __typename
          }
          geniusInfo {
            benefitsCommunication {
              header {
                title
                __typename
              }
              items {
                title
                __typename
              }
              __typename
            }
            geniusBenefits
            geniusBenefitsData {
              hotelCardHasFreeBreakfast
              hotelCardHasFreeRoomUpgrade
              sortedBenefits
              __typename
            }
            showGeniusRateBadge
            __typename
          }
          location {
            displayLocation
            mainDistance
            publicTransportDistanceDescription
            skiLiftDistance
            beachDistance
            nearbyBeachNames
            beachWalkingTime
            geoDistanceMeters
            __typename
          }
          mealPlanIncluded {
            mealPlanType
            text
            __typename
          }
          persuasion {
            autoextended
            geniusRateAvailable
            highlighted
            preferred
            preferredPlus
            showNativeAdLabel
            nativeAdId
            nativeAdsCpc
            nativeAdsTracking
            sponsoredAdsData {
              isDsaCompliant
              legalEntityName
              sponsoredAdsDesign
              __typename
            }
            __typename
          }
          policies {
            showFreeCancellation
            showNoPrepayment
            enableJapaneseUsersSpecialCase
            __typename
          }
          ribbon {
            ribbonType
            text
            __typename
          }
          recommendedDate {
            checkin
            checkout
            lengthOfStay
            __typename
          }
          showGeniusLoginMessage
          hostTraderLabel
          soldOutInfo {
            isSoldOut
            messages {
              text
              __typename
            }
            alternativeDatesMessages {
              text
              __typename
            }
            __typename
          }
          nbWishlists
          visibilityBoosterEnabled
          showAdLabel
          isNewlyOpened
          propertySustainability {
            isSustainable
            tier {
              type
              __typename
            }
            facilities {
              id
              __typename
            }
            certifications {
              name
              __typename
            }
            chainProgrammes {
              chainName
              programmeName
              __typename
            }
            levelId
            __typename
          }
          seoThemes {
            caption
            __typename
          }
          relocationMode {
            distanceToCityCenterKm
            distanceToCityCenterMiles
            distanceToOriginalHotelKm
            distanceToOriginalHotelMiles
            phoneNumber
            __typename
          }
          bundleRatesAvailable
          __typename
        }

        fragment Banner on Banner {
          name
          type
          isDismissible
          showAfterDismissedDuration
          position
          requestAlternativeDates
          merchId
          title {
            text
            __typename
          }
          imageUrl
          paragraphs {
            text
            __typename
          }
          metadata {
            key
            value
            __typename
          }
          pendingReviewInfo {
            propertyPhoto {
              lowResUrl {
                relativeUrl
                __typename
              }
              lowResJpegUrl {
                relativeUrl
                __typename
              }
              __typename
            }
            propertyName
            urlAccessCode
            __typename
          }
          nbDeals
          primaryAction {
            text {
              text
              __typename
            }
            action {
              name
              context {
                key
                value
                __typename
              }
              __typename
            }
            __typename
          }
          secondaryAction {
            text {
              text
              __typename
            }
            action {
              name
              context {
                key
                value
                __typename
              }
              __typename
            }
            __typename
          }
          iconName
          flexibleFilterOptions {
            optionId
            filterName
            __typename
          }
          trackOnView {
            type
            experimentHash
            value
            __typename
          }
          dateFlexQueryOptions {
            text {
              text
              __typename
            }
            action {
              name
              context {
                key
                value
                __typename
              }
              __typename
            }
            isApplied
            __typename
          }
          __typename
        }

        fragment Carousel on Carousel {
          aggregatedCountsByFilterId
          carouselId
          position
          contentType
          hotelId
          name
          soldoutProperties
          priority
          themeId
          frontierThemeIds
          title {
            text
            __typename
          }
          slides {
            captionText {
              text
              __typename
            }
            name
            photoUrl
            subtitle {
              text
              __typename
            }
            type
            title {
              text
              __typename
            }
            action {
              context {
                key
                value
                __typename
              }
              __typename
            }
            __typename
          }
          __typename
        }

        fragment DestinationLocation on DestinationLocation {
          name {
            text
            __typename
          }
          inName {
            text
            __typename
          }
          countryCode
          ufi
          __typename
        }

        fragment FilterData on Filter {
          trackOnView {
            type
            experimentHash
            value
            __typename
          }
          trackOnClick {
            type
            experimentHash
            value
            __typename
          }
          name
          field
          category
          filterStyle
          title {
            text
            translationTag {
              translation
              __typename
            }
            __typename
          }
          subtitle
          options {
            parentId
            genericId
            trackOnView {
              type
              experimentHash
              value
              __typename
            }
            trackOnClick {
              type
              experimentHash
              value
              __typename
            }
            trackOnSelect {
              type
              experimentHash
              value
              __typename
            }
            trackOnDeSelect {
              type
              experimentHash
              value
              __typename
            }
            trackOnViewPopular {
              type
              experimentHash
              value
              __typename
            }
            trackOnClickPopular {
              type
              experimentHash
              value
              __typename
            }
            trackOnSelectPopular {
              type
              experimentHash
              value
              __typename
            }
            trackOnDeSelectPopular {
              type
              experimentHash
              value
              __typename
            }
            ...FilterOption
            __typename
          }
          filterLayout {
            isCollapsable
            collapsedCount
            __typename
          }
          stepperOptions {
            min
            max
            default
            selected
            title {
              text
              translationTag {
                translation
                __typename
              }
              __typename
            }
            field
            labels {
              text
              translationTag {
                translation
                __typename
              }
              __typename
            }
            trackOnView {
              type
              experimentHash
              value
              __typename
            }
            trackOnClick {
              type
              experimentHash
              value
              __typename
            }
            trackOnSelect {
              type
              experimentHash
              value
              __typename
            }
            trackOnDeSelect {
              type
              experimentHash
              value
              __typename
            }
            trackOnClickDecrease {
              type
              experimentHash
              value
              __typename
            }
            trackOnClickIncrease {
              type
              experimentHash
              value
              __typename
            }
            trackOnDecrease {
              type
              experimentHash
              value
              __typename
            }
            trackOnIncrease {
              type
              experimentHash
              value
              __typename
            }
            __typename
          }
          sliderOptions {
            min
            max
            minSelected
            maxSelected
            minPriceStep
            minSelectedFormatted
            currency
            histogram
            selectedRange {
              translation
              __typename
            }
            __typename
          }
          __typename
        }

        fragment FilterOption on Option {
          optionId: id
          count
          selected
          urlId
          source
          additionalLabel {
            text
            translationTag {
              translation
              __typename
            }
            __typename
          }
          value {
            text
            translationTag {
              translation
              __typename
            }
            __typename
          }
          starRating {
            value
            symbol
            caption {
              translation
              __typename
            }
            showAdditionalInfoIcon
            __typename
          }
          __typename
        }

        fragment LandingPageBreadcrumb on LandingPageBreadcrumb {
          destType
          name
          urlParts
          __typename
        }

        fragment MatchingUnitConfigurations on SearchResultProperty {
          matchingUnitConfigurations {
            commonConfiguration {
              name
              unitId
              bedConfigurations {
                beds {
                  count
                  type
                  __typename
                }
                nbAllBeds
                __typename
              }
              nbAllBeds
              nbBathrooms
              nbBedrooms
              nbKitchens
              nbLivingrooms
              nbUnits
              unitTypeNames {
                translation
                __typename
              }
              localizedArea {
                localizedArea
                unit
                __typename
              }
              __typename
            }
            unitConfigurations {
              name
              unitId
              bedConfigurations {
                beds {
                  count
                  type
                  __typename
                }
                nbAllBeds
                __typename
              }
              apartmentRooms {
                config {
                  roomId: id
                  roomType
                  bedTypeId
                  bedCount: count
                  __typename
                }
                roomName: tag {
                  tag
                  translation
                  __typename
                }
                __typename
              }
              nbAllBeds
              nbBathrooms
              nbBedrooms
              nbKitchens
              nbLivingrooms
              nbUnits
              unitTypeNames {
                translation
                __typename
              }
              localizedArea {
                localizedArea
                unit
                __typename
              }
              unitTypeId
              __typename
            }
            __typename
          }
          __typename
        }

        fragment PropertyBlocks on SearchResultProperty {
          blocks {
            blockId {
              roomId
              occupancy
              policyGroupId
              packageId
              mealPlanId
              __typename
            }
            finalPrice {
              amount
              currency
              __typename
            }
            originalPrice {
              amount
              currency
              __typename
            }
            onlyXLeftMessage {
              tag
              variables {
                key
                value
                __typename
              }
              translation
              __typename
            }
            freeCancellationUntil
            hasCrib
            blockMatchTags {
              childStaysForFree
              __typename
            }
            thirdPartyInventoryContext {
              isTpiBlock
              __typename
            }
            __typename
          }
          __typename
        }

        fragment PriceDisplayInfoIrene on PriceDisplayInfoIrene {
          badges {
            name {
              translation
              __typename
            }
            tooltip {
              translation
              __typename
            }
            style
            identifier
            __typename
          }
          chargesInfo {
            translation
            __typename
          }
          displayPrice {
            copy {
              translation
              __typename
            }
            amountPerStay {
              amount
              amountRounded
              amountUnformatted
              currency
              __typename
            }
            __typename
          }
          priceBeforeDiscount {
            copy {
              translation
              __typename
            }
            amountPerStay {
              amount
              amountRounded
              amountUnformatted
              currency
              __typename
            }
            __typename
          }
          rewards {
            rewardsList {
              termsAndConditions
              amountPerStay {
                amount
                amountRounded
                amountUnformatted
                currency
                __typename
              }
              breakdown {
                productType
                amountPerStay {
                  amount
                  amountRounded
                  amountUnformatted
                  currency
                  __typename
                }
                __typename
              }
              __typename
            }
            rewardsAggregated {
              amountPerStay {
                amount
                amountRounded
                amountUnformatted
                currency
                __typename
              }
              copy {
                translation
                __typename
              }
              __typename
            }
            __typename
          }
          useRoundedAmount
          discounts {
            amount {
              amount
              amountRounded
              amountUnformatted
              currency
              __typename
            }
            name {
              translation
              __typename
            }
            description {
              translation
              __typename
            }
            itemType
            productId
            __typename
          }
          excludedCharges {
            excludeChargesAggregated {
              copy {
                translation
                __typename
              }
              amountPerStay {
                amount
                amountRounded
                amountUnformatted
                currency
                __typename
              }
              __typename
            }
            excludeChargesList {
              chargeMode
              chargeInclusion
              chargeType
              amountPerStay {
                amount
                amountRounded
                amountUnformatted
                currency
                __typename
              }
              __typename
            }
            __typename
          }
          taxExceptions {
            shortDescription {
              translation
              __typename
            }
            longDescription {
              translation
              __typename
            }
            __typename
          }
          __typename
        }

        fragment BookerExperienceData on SearchResultProperty {
          bookerExperienceContentUIComponentProps {
            ... on BookerExperienceContentLoyaltyBadgeListProps {
              badges {
                variant
                key
                title
                popover
                logoSrc
                logoAlt
                __typename
              }
              __typename
            }
            ... on BookerExperienceContentFinancialBadgeProps {
              paymentMethod
              backgroundColor
              hideAccepted
              __typename
            }
            __typename
          }
          __typename
        }

        fragment SearchMetadata on SearchMeta {
          availabilityInfo {
            hasLowAvailability
            unavailabilityPercent
            totalAvailableNotAutoextended
            __typename
          }
          boundingBoxes {
            swLat
            swLon
            neLat
            neLon
            type
            __typename
          }
          childrenAges
          dates {
            checkin
            checkout
            lengthOfStayInDays
            __typename
          }
          destId
          destType
          guessedLocation {
            destId
            destType
            destName
            __typename
          }
          maxLengthOfStayInDays
          nbRooms
          nbAdults
          nbChildren
          userHasSelectedFilters
          customerValueStatus
          isAffiliateBookingOwned
          affiliatePartnerChannelId
          affiliateVerticalType
          geniusLevel
          __typename
        }

        fragment SearchResultsBreadcrumb on SearchResultsBreadcrumb {
          destId
          destType
          name
          __typename
        }

        fragment SorterFields on SorterOption {
          type: name
          captionTranslationTag {
            translation
            __typename
          }
          tooltipTranslationTag {
            translation
            __typename
          }
          isSelected: selected
          __typename
        }

        fragment OneOfThreeDeal on OneOfThreeDeal {
          id
          uuid
          winnerHotelId
          winnerBlockId
          priceDisplayInfoIrene {
            displayPrice {
              amountPerStay {
                amountRounded
                amountUnformatted
                __typename
              }
              __typename
            }
            __typename
          }
          locationInfo {
            name
            inName
            destType
            __typename
          }
          destinationType
          commonFacilities {
            id
            name
            __typename
          }
          tpiParams {
            wholesalerCode
            rateKey
            rateBlockId
            bookingRoomId
            supplierId
            __typename
          }
          properties {
            priceDisplayInfoIrene {
              priceBeforeDiscount {
                amountPerStay {
                  amountRounded
                  amountUnformatted
                  __typename
                }
                __typename
              }
              displayPrice {
                amountPerStay {
                  amountRounded
                  amountUnformatted
                  __typename
                }
                __typename
              }
              __typename
            }
            basicPropertyData {
              id
              name
              pageName
              photos {
                main {
                  highResUrl {
                    absoluteUrl
                    __typename
                  }
                  __typename
                }
                __typename
              }
              location {
                address
                countryCode
                __typename
              }
              reviews {
                reviewsCount
                totalScore
                __typename
              }
              __typename
            }
            blocks {
              thirdPartyInventoryContext {
                rateBlockId
                rateKey
                wholesalerCode
                tpiRoom {
                  bookingRoomId
                  __typename
                }
                supplierId
                __typename
              }
              __typename
            }
            __typename
          }
          __typename
        }

        fragment TripTypesData on TripTypes {
          beach {
            isBeachUfi
            isEnabledBeachUfi
            __typename
          }
          ski {
            isSkiExperience
            isSkiScaleUfi
            __typename
          }
          __typename
        }

        fragment ZeroResultsSection on ZeroResultsSection {
          title {
            text
            __typename
          }
          primaryAction {
            text {
              text
              __typename
            }
            action {
              name
              __typename
            }
            __typename
          }
          paragraphs {
            text
            __typename
          }
          type
          __typename
        }

        fragment PreviousSearches on PreviousSearch {
          childrenAges
          __typename
        }

        fragment FrontierThemes on FrontierTheme {
          id
          name
          selected
          __typename
        }

        fragment MerchRegionIrene on MerchComponentsResultIrene {
          regions {
            id
            components {
              ... on PromotionalBannerIrene {
                promotionalBannerCampaignId
                contentArea {
                  title {
                    ... on PromotionalBannerSimpleTitleIrene {
                      value
                      __typename
                    }
                    __typename
                  }
                  subTitle {
                    ... on PromotionalBannerSimpleSubTitleIrene {
                      value
                      __typename
                    }
                    __typename
                  }
                  caption {
                    ... on PromotionalBannerSimpleCaptionIrene {
                      value
                      __typename
                    }
                    ... on PromotionalBannerCountdownCaptionIrene {
                      campaignEnd
                      __typename
                    }
                    __typename
                  }
                  buttons {
                    variant
                    cta {
                      ariaLabel
                      text
                      targetLanding {
                        ... on OpenContextSheet {
                          sheet {
                            ... on WebContextSheet {
                              title
                              body {
                                items {
                                  ... on ContextSheetTextItem {
                                    text
                                    __typename
                                  }
                                  ... on ContextSheetList {
                                    items {
                                      text
                                      __typename
                                    }
                                    __typename
                                  }
                                  __typename
                                }
                                __typename
                              }
                              buttons {
                                variant
                                cta {
                                  text
                                  ariaLabel
                                  targetLanding {
                                    ... on DirectLinkLanding {
                                      urlPath
                                      queryParams {
                                        name
                                        value
                                        __typename
                                      }
                                      __typename
                                    }
                                    ... on LoginLanding {
                                      stub
                                      __typename
                                    }
                                    ... on DeeplinkLanding {
                                      urlPath
                                      queryParams {
                                        name
                                        value
                                        __typename
                                      }
                                      __typename
                                    }
                                    ... on ResolvedLinkLanding {
                                      url
                                      __typename
                                    }
                                    __typename
                                  }
                                  __typename
                                }
                                __typename
                              }
                              __typename
                            }
                            __typename
                          }
                          __typename
                        }
                        ... on SearchResultsLandingIrene {
                          destType
                          destId
                          checkin
                          checkout
                          nrAdults
                          nrChildren
                          childrenAges
                          nrRooms
                          filters {
                            name
                            value
                            __typename
                          }
                          __typename
                        }
                        ... on DirectLinkLandingIrene {
                          urlPath
                          queryParams {
                            name
                            value
                            __typename
                          }
                          __typename
                        }
                        ... on LoginLandingIrene {
                          stub
                          __typename
                        }
                        ... on DeeplinkLandingIrene {
                          urlPath
                          queryParams {
                            name
                            value
                            __typename
                          }
                          __typename
                        }
                        ... on SorterLandingIrene {
                          sorterName
                          __typename
                        }
                        __typename
                      }
                      __typename
                    }
                    __typename
                  }
                  __typename
                }
                designVariant {
                  ... on DesktopPromotionalFullBleedImageIrene {
                    image: image {
                      id
                      url(width: 814, height: 138)
                      alt
                      overlayGradient
                      primaryColorHex
                      __typename
                    }
                    colorScheme
                    signature
                    __typename
                  }
                  ... on DesktopPromotionalImageLeftIrene {
                    imageOpt: image {
                      id
                      url(width: 248, height: 248)
                      alt
                      overlayGradient
                      primaryColorHex
                      __typename
                    }
                    colorScheme
                    signature
                    __typename
                  }
                  ... on DesktopPromotionalImageRightIrene {
                    imageOpt: image {
                      id
                      url(width: 248, height: 248)
                      alt
                      overlayGradient
                      primaryColorHex
                      __typename
                    }
                    colorScheme
                    signature
                    __typename
                  }
                  ... on MdotPromotionalFullBleedImageIrene {
                    image: image {
                      id
                      url(width: 358, height: 136)
                      alt
                      overlayGradient
                      primaryColorHex
                      __typename
                    }
                    colorScheme
                    signature
                    __typename
                  }
                  ... on MdotPromotionalImageLeftIrene {
                    imageOpt: image {
                      id
                      url(width: 128, height: 128)
                      alt
                      overlayGradient
                      primaryColorHex
                      __typename
                    }
                    colorScheme
                    signature
                    __typename
                  }
                  ... on MdotPromotionalImageRightIrene {
                    imageOpt: image {
                      id
                      url(width: 128, height: 128)
                      alt
                      overlayGradient
                      primaryColorHex
                      __typename
                    }
                    colorScheme
                    signature
                    __typename
                  }
                  ... on MdotPromotionalImageTopIrene {
                    imageOpt: image {
                      id
                      url(width: 128, height: 128)
                      alt
                      overlayGradient
                      primaryColorHex
                      __typename
                    }
                    colorScheme
                    signature
                    __typename
                  }
                  ... on MdotPromotionalIllustrationLeftIrene {
                    imageOpt: image {
                      id
                      url(width: 200, height: 200)
                      alt
                      overlayGradient
                      primaryColorHex
                      __typename
                    }
                    colorScheme
                    signature
                    __typename
                  }
                  ... on MdotPromotionalIllustrationRightIrene {
                    imageOpt: image {
                      id
                      url(width: 200, height: 200)
                      alt
                      overlayGradient
                      primaryColorHex
                      __typename
                    }
                    colorScheme
                    signature
                    __typename
                  }
                  __typename
                }
                __typename
              }
              ... on MerchCarouselIrene @include(if: $carouselLowCodeExp) {
                carouselCampaignId
                __typename
              }
              __typename
            }
            __typename
          }
          __typename
        }"""
    }

    # Update the payload with the input parameters
    payload['variables']['input']['location']['searchString'] = address
    payload['variables']['input']['pagination']['rowsPerPage'] = page_size

    response = requests.post(
        url,
        params=query_params,
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        raise Exception(f"Error: Received response code {response.status_code}. Response body: {response.text}")

    result = response.json()
    search_results = result.get('data', {}).get('searchQueries', {}).get('search', {}).get('results', [])

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Listing ID', 'Listing Title', 'Page Name', 'Amount'])
        
        for row in search_results:
            # writer.writerow([
            #     row.get('basicPropertyData', {}).get('id'),
            #     row.get('displayName', {}).get('text'),
            #     row.get('basicPropertyData', {}).get('pageName'),
            #     row.get('priceDisplayInfoIrene', {}).get('priceBeforeDiscount', {}).get('displayPrice', {}).get('amountPerStay', {}).get('amount')
            # ])
            writer.writerow([
                row.get('basicPropertyData', {}).get('id', 'N/A'),
                row.get('displayName', {}).get('text', 'N/A'),
                row.get('basicPropertyData', {}).get('pageName', 'N/A'),
                row.get('priceDisplayInfoIrene', {}).get('priceBeforeDiscount', {}).get('displayPrice', {}).get('amountPerStay', {}).get('amount', 'N/A') if row.get('priceDisplayInfoIrene') else 'N/A'
            ])

def build_query_params():
    params = {
        "label": "gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4AofIxbMGwAIB0gIkNDFkMDkyZDktMDFlZC00NzMxLTkyMjMtNGFhYWIxNjEwMjg12AIF4AIB",
        "sid": "aa4f62f572ac5f487c282f0f11ec409c",
        "aid": "304142",
        "ss": "Bangalore",
        "ssne": "Bangalore",
        "ssne_untouched": "Bangalore",
        "lang": "en-gb",
        "src": "index",
        "dest_id": "-2090174",
        "dest_type": "city",
        "checkin": "2024-06-18",
        "checkout": "2024-06-19",
        "group_adults": "1",
        "no_rooms": "1",
        "group_children": "0",
        "nflt": "distance=3000"
    }
    return params

def build_headers():
    return {
        "accept": "*/*",
        "accept-language": "en-GB,en;q=0.7",
        "content-type": "application/json",
        "cookie": "px_init=0; pcm_consent=analytical%3Dtrue%26countryCode%3DIN%26consentId%3Def552b9e-a259-4741-ad3a-e66db563ec9c%26consentedAt%3D2024-02-29T14%3A48%3A18.689Z%26expiresAt%3D2024-08-27T14%3A48%3A18.689Z%26implicit%3Dtrue%26marketing%3Dtrue%26regionCode%3DKA%26regulation%3Dnone%26legacyRegulation%3Dnone; bkng_sso_session=e30; bkng_sso_ses=e30; _pxhd=l1VHnFED432P4U6wG-B5VP9%2F46XzrG7Qv8lfOB8g2HN265AlW8BB6AP98WWPzjdhLQAwiMtiKf4LV5y2pbS6QQ%3D%3D%3AM4mRLb4ORiG5aLq5Mil%2FFBL%2FucckryNyUxrxSgFtrF2L4x310dL3r9Rv%2FuUltSC3pk4Y%2FfIlRNQYFKAUNBPs04UgQNbn1ani1YpbAZT%2FCfc%3D; pxcts=aa860a0d-d711-11ee-9e8d-f6ec8a89a25b; bs=%7B%22gc%22%3A1%7D; qr_is_sr=fast-click; 11_srd=%7B%22features%22%3A%5B%7B%22id%22%3A5%7D%5D%2C%22score%22%3A3%2C%22detected%22%3Afalse%7D; pcm_personalization_disabled=0; bkng_sso_auth=CAIQsOnuTRpmCvN2T1sxcM7wXLWbcQd6z0Cm6xaWBO9rQxOB9/ONnhf71l2kwxfJx3auoJfKUWOVHJrK5KkdNUhEkYNeJoe9o5Hmu7Iu65+ZJcWj+P6CJfn52bjP2LuDh1KKqYp9F5++eAAWsxbP; cors_js=1; BJS=-; aws-waf-token=eb71beb8-98b5-4eb6-bd21-9e817d992a68:HgoAikFJbishAAAA:kePYlBJb55HsoBGxx/Z8QHWZLfDjB298StazgQnecolRTcEM6kKLCfCbCrpHiiBkezeXlm2gIInb6zD96VJvKg6kWj4LUPTB3JIHc1Ueo4zmWJtW4kiUv1AMXkQf7itB3jWZzrxrfqQsjlEOJIE9izvW948rpf1aM47INlA/elWfva4dwgh7wMu+LXf88F0W7HIKOslLXyvaBKgZ; bkng=11UmFuZG9tSVYkc2RlIyh9YSvtNSM2ADX0BnR0tqAEmju3Hqww3f4xH1FWtu0PhSoE1GWriV3TDLv6gfUX9GITdglHqvXFXqI0DxpljqO8ImGlmzozNwIe1y9El%2Fk0KPyzFeJWurckAlX9ymWsW87Y3ZXs8HUZ1fkIFCFwjEGGJWczz4jdBC7DL0nNNu8G9sT6axa5eWgMRgwPTYXp7lgk5A%3D%3D; lastSeen=0",
        "origin": "https://www.booking.com",
        "referer": "https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4AofIxbMGwAIB0gIkNDFkMDkyZDktMDFlZC00NzMxLTkyMjMtNGFhYWIxNjEwMjg12AIF4AIB&sid=aa4f62f572ac5f487c282f0f11ec409c&aid=304142&ss=Bangalore&ssne=Bangalore&ssne_untouched=Bangalore&lang=en-gb&src=index&dest_id=-2090174&dest_type=city&checkin=2024-06-18&checkout=2024-06-19&group_adults=1&no_rooms=1&group_children=0&nflt=distance%3D3000",
        "sec-ch-ua": '"Brave";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "x-booking-context-action-name": "searchresults_irene",
        "x-booking-context-aid": "304142",
        "x-booking-csrf-token": "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIiwiaWF0IjoxNzE4NzA3MjU3LCJleHAiOjE3MTg3OTM2NTd9.gA_WWPhKkgTxDbcyKB-uFUsf_obvRlbvoXZdZFmcJ6EkASNrqdWTR52ltzPSWG_WgOBQBZYGklU3KfhgMTWldg",
        "x-booking-et-serialized-state": "E2VhNDBFc4_90QQbS9aUekVBL5O2uMzHdM99N6US3R1fVugRNyessdEVjxWsuup9I",
        "x-booking-pageview-id": "cd2e4b1c6a810062",
        "x-booking-site-type-id": "1",
        "x-booking-topic": "capla_browser_b-search-web-searchresults"
    }

# Example usage
get_data('Bangalore', 30)