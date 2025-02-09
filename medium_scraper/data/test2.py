import re
import sys
import requests
sys.path.append('..')
from medium_scraper import __init__
from datetime import date, datetime, timedelta, timezone, tzinfo
from scraper.models import * 
from bs4 import BeautifulSoup
import json

# sq = Archives.objects.order_by("url").distinct("url").values_list()
# for x in sq:
#     print(x)
# Archives.objects.filter()
# Archives.objects.all().delete()

# bs = BeautifulSoup(open('medium_scraper/Untitled-1.html',  encoding="utf8"),'html.parser')
# href = bs.select_one("div > div > div:nth-child(2) > a")["href"]
# sel = bs.select_one("div > div > div:nth-child(3) > a")["href"]
# bs = BeautifulSoup(requests.get("https://towardsdatascience.com/archive/2020/05/16").text, 'html.parser')


# headers = {"accept": "*/*",
# "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
# "apollographql-client-name": "lite",
# "apollographql-client-version": "main-20210709-201441-e2b0667512",
# "content-type": "application/json",
# "graphql-operation": "VisitorQuery",
# "medium-frontend-app": "lite/main-20210709-201441-e2b0667512",
# "medium-frontend-path": "/@marcopeixeiro/followers",
# "medium-frontend-route": "ShowUserFollowers",
# "ot-tracer-sampled": "true",
# "ot-tracer-spanid": "78f6e1bd1a71eb49",
# "ot-tracer-traceid": "78ab18fab8c64e18",
# "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
# "sec-ch-ua-mobile": "?0",
# "sec-fetch-dest": "empty",
# "sec-fetch-mode": "cors",
# "sec-fetch-site": "same-origin",
# "referrer": "https://medium.com/@marcopeixeiro/followers",
# "referrerPolicy": "strict-origin-when-cross-origin",
# "medium-frontend-path":"/@marcopeixeiro/followers",
# "graphql-operation":"VisitorQuery"
# }
headers = {"accept": "*/*",
"accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
"apollographql-client-name": "lite",
"apollographql-client-version": "main-20210709-201441-e2b0667512",
"content-type": "application/json",
"graphql-operation": "VisitorQuery",
"medium-frontend-app": "lite/main-20210709-201441-e2b0667512",
"medium-frontend-path": "/@marcopeixeiro/followers",
"medium-frontend-route": "ShowUserFollowers",
"ot-tracer-sampled": "true",
"ot-tracer-spanid": "78f6e1bd1a71eb49",
"ot-tracer-traceid": "78ab18fab8c64e18",
"sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
"sec-ch-ua-mobile": "?0",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"referrer": "https://medium.com/@marcopeixeiro/followers",
"referrerPolicy": "strict-origin-when-cross-origin",
}


data0 =  "{\"operationName\":\"UserProfileFollowersHandler\",\"variables\":{\"id\":null,\"username\":\"@marcopeixeiro\",\"paging\":{\"from\":\"134bffde3b\",\"limit\":8}},\"query\":\"query UserProfileFollowersHandler($username: ID, $id: ID, $paging: PagingOptions) {\\n  userResult(username: $username, id: $id) {\\n    __typename\\n    ... on User {\\n      id\\n      followersUserConnection(paging: $paging) {\\n        pagingInfo {\\n          next {\\n            from\\n            limit\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      ...UserCanonicalizer_user\\n      ...UserProfileFollowersScreen_user\\n      __typename\\n    }\\n  }\\n}\\n\\nfragment UserCanonicalizer_user on User {\\n  id\\n  username\\n  hasSubdomain\\n  customDomainState {\\n    live {\\n      domain\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment UserProfileFollowersScreen_user on User {\\n  id\\n  ...PublisherFollowers_publisher\\n  ...UserProfileMetadata_user\\n  __typename\\n}\\n\\nfragment PublisherFollowers_publisher on Publisher {\\n  id\\n  customStyleSheet {\\n    id\\n    ...CustomBackgroundWrapper_customStyleSheet\\n    ...CustomThemeProvider_customStyleSheet\\n    ...MetaHeader_customStyleSheet\\n    __typename\\n  }\\n  followersUserConnection(paging: $paging) {\\n    ...PublisherFollowList_userConnection\\n    __typename\\n  }\\n  ...MetaHeader_publisher\\n  ... on User {\\n    twitterScreenName\\n    socialStats {\\n      followerCount\\n      __typename\\n    }\\n    __typename\\n    id\\n  }\\n  ... on Collection {\\n    subscriberCount\\n    __typename\\n    id\\n  }\\n  __typename\\n}\\n\\nfragment CustomBackgroundWrapper_customStyleSheet on CustomStyleSheet {\\n  id\\n  global {\\n    colorPalette {\\n      background {\\n        ...getHexFromColorValue_colorValue\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment getHexFromColorValue_colorValue on ColorValue {\\n  rgb\\n  alpha\\n  __typename\\n}\\n\\nfragment CustomThemeProvider_customStyleSheet on CustomStyleSheet {\\n  id\\n  ...customDefaultBackgroundTheme_customStyleSheet\\n  ...customStyleSheetFontTheme_customStyleSheet\\n  __typename\\n}\\n\\nfragment customDefaultBackgroundTheme_customStyleSheet on CustomStyleSheet {\\n  id\\n  global {\\n    colorPalette {\\n      primary {\\n        colorPalette {\\n          ...customDefaultBackgroundTheme_colorPalette\\n          __typename\\n        }\\n        __typename\\n      }\\n      background {\\n        colorPalette {\\n          ...customDefaultBackgroundTheme_colorPalette\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment customDefaultBackgroundTheme_colorPalette on ColorPalette {\\n  highlightSpectrum {\\n    ...ThemeUtil_colorSpectrum\\n    __typename\\n  }\\n  defaultBackgroundSpectrum {\\n    ...ThemeUtil_colorSpectrum\\n    __typename\\n  }\\n  tintBackgroundSpectrum {\\n    ...ThemeUtil_colorSpectrum\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ThemeUtil_colorSpectrum on ColorSpectrum {\\n  backgroundColor\\n  ...ThemeUtilInterpolateHelpers_colorSpectrum\\n  __typename\\n}\\n\\nfragment ThemeUtilInterpolateHelpers_colorSpectrum on ColorSpectrum {\\n  colorPoints {\\n    ...ThemeUtil_colorPoint\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ThemeUtil_colorPoint on ColorPoint {\\n  color\\n  point\\n  __typename\\n}\\n\\nfragment customStyleSheetFontTheme_customStyleSheet on CustomStyleSheet {\\n  id\\n  global {\\n    fonts {\\n      font1 {\\n        name\\n        __typename\\n      }\\n      font2 {\\n        name\\n        __typename\\n      }\\n      font3 {\\n        name\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment MetaHeader_customStyleSheet on CustomStyleSheet {\\n  id\\n  header {\\n    headerScale\\n    horizontalAlignment\\n    __typename\\n  }\\n  ...MetaHeaderBackground_customStyleSheet\\n  ...MetaHeaderEngagement_customStyleSheet\\n  ...MetaHeaderLogo_customStyleSheet\\n  ...MetaHeaderNavVertical_customStyleSheet\\n  ...MetaHeaderTagline_customStyleSheet\\n  ...MetaHeaderThemeProvider_customStyleSheet\\n  __typename\\n}\\n\\nfragment MetaHeaderBackground_customStyleSheet on CustomStyleSheet {\\n  id\\n  header {\\n    headerScale\\n    backgroundImageDisplayMode\\n    backgroundImageVerticalAlignment\\n    backgroundColorDisplayMode\\n    backgroundColor {\\n      ...getHexFromColorValue_colorValue\\n      ...getOpaqueHexFromColorValue_colorValue\\n      __typename\\n    }\\n    secondaryBackgroundColor {\\n      ...getHexFromColorValue_colorValue\\n      __typename\\n    }\\n    postBackgroundColor {\\n      ...getHexFromColorValue_colorValue\\n      __typename\\n    }\\n    backgroundImage {\\n      ...MetaHeaderBackground_imageMetadata\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment MetaHeaderBackground_imageMetadata on ImageMetadata {\\n  id\\n  originalWidth\\n  __typename\\n}\\n\\nfragment getOpaqueHexFromColorValue_colorValue on ColorValue {\\n  rgb\\n  __typename\\n}\\n\\nfragment MetaHeaderEngagement_customStyleSheet on CustomStyleSheet {\\n  ...MetaHeaderNav_customStyleSheet\\n  __typename\\n  id\\n}\\n\\nfragment MetaHeaderNav_customStyleSheet on CustomStyleSheet {\\n  id\\n  navigation {\\n    navItems {\\n      ...MetaHeaderNav_headerNavigationItem\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment MetaHeaderNav_headerNavigationItem on HeaderNavigationItem {\\n  name\\n  tagSlugs\\n  ...MetaHeaderNavLink_headerNavigationItem\\n  __typename\\n}\\n\\nfragment MetaHeaderNavLink_headerNavigationItem on HeaderNavigationItem {\\n  name\\n  ...getNavItemHref_headerNavigationItem\\n  __typename\\n}\\n\\nfragment getNavItemHref_headerNavigationItem on HeaderNavigationItem {\\n  href\\n  type\\n  tags {\\n    id\\n    normalizedTagSlug\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment MetaHeaderLogo_customStyleSheet on CustomStyleSheet {\\n  id\\n  header {\\n    nameColor {\\n      ...getHexFromColorValue_colorValue\\n      __typename\\n    }\\n    nameTreatment\\n    postNameTreatment\\n    logoImage {\\n      ...MetaHeaderLogo_imageMetadata\\n      __typename\\n    }\\n    logoScale\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment MetaHeaderLogo_imageMetadata on ImageMetadata {\\n  id\\n  originalWidth\\n  originalHeight\\n  ...PublisherLogo_image\\n  __typename\\n}\\n\\nfragment PublisherLogo_image on ImageMetadata {\\n  id\\n  originalHeight\\n  originalWidth\\n  __typename\\n}\\n\\nfragment MetaHeaderNavVertical_customStyleSheet on CustomStyleSheet {\\n  id\\n  navigation {\\n    navItems {\\n      ...MetaHeaderNavLink_headerNavigationItem\\n      __typename\\n    }\\n    __typename\\n  }\\n  ...MetaHeaderNav_customStyleSheet\\n  __typename\\n}\\n\\nfragment MetaHeaderTagline_customStyleSheet on CustomStyleSheet {\\n  id\\n  header {\\n    taglineColor {\\n      ...getHexFromColorValue_colorValue\\n      __typename\\n    }\\n    taglineTreatment\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment MetaHeaderThemeProvider_customStyleSheet on CustomStyleSheet {\\n  id\\n  ...useMetaHeaderTheme_customStyleSheet\\n  __typename\\n}\\n\\nfragment useMetaHeaderTheme_customStyleSheet on CustomStyleSheet {\\n  ...customDefaultBackgroundTheme_customStyleSheet\\n  global {\\n    colorPalette {\\n      primary {\\n        colorPalette {\\n          tintBackgroundSpectrum {\\n            ...ThemeUtil_colorSpectrum\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  header {\\n    backgroundColor {\\n      colorPalette {\\n        tintBackgroundSpectrum {\\n          ...ThemeUtil_colorSpectrum\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    postBackgroundColor {\\n      colorPalette {\\n        tintBackgroundSpectrum {\\n          ...ThemeUtil_colorSpectrum\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    backgroundImage {\\n      id\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n  id\\n}\\n\\nfragment MetaHeader_publisher on Publisher {\\n  __typename\\n  name\\n  ...MetaHeaderEngagement_publisher\\n  ...MetaHeaderLogo_publisher\\n  ...MetaHeaderNavVertical_publisher\\n  ...MetaHeaderTagline_publisher\\n  ...MetaHeaderThemeProvider_publisher\\n  ...MetaHeaderActions_publisher\\n  ...MetaHeaderTop_publisher\\n  ... on Collection {\\n    id\\n    favicon {\\n      id\\n      __typename\\n    }\\n    tagline\\n    ...CollectionNavigationContextProvider_collection\\n    __typename\\n  }\\n  ... on User {\\n    id\\n    bio\\n    __typename\\n  }\\n}\\n\\nfragment CollectionNavigationContextProvider_collection on Collection {\\n  id\\n  domain\\n  slug\\n  isAuroraVisible\\n  __typename\\n}\\n\\nfragment MetaHeaderEngagement_publisher on Publisher {\\n  __typename\\n  ...MetaHeaderNav_publisher\\n  ...PublisherAboutLink_publisher\\n  ...PublisherFollowButton_publisher\\n  ...PublisherFollowerCount_publisher\\n  ...UserProfileBooksLink_publisher\\n  ... on Collection {\\n    creator {\\n      id\\n      __typename\\n    }\\n    __typename\\n    id\\n  }\\n  ... on User {\\n    ...UserProfileCatalogsLink_publisher\\n    ...AutoFollowWrapper_user\\n    ...UserSubscribeButton_user\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment MetaHeaderNav_publisher on Publisher {\\n  id\\n  ...MetaHeaderNavLink_publisher\\n  __typename\\n}\\n\\nfragment MetaHeaderNavLink_publisher on Publisher {\\n  id\\n  ...getNavItemHref_publisher\\n  __typename\\n}\\n\\nfragment getNavItemHref_publisher on Publisher {\\n  id\\n  ...publisherUrl_publisher\\n  __typename\\n}\\n\\nfragment publisherUrl_publisher on Publisher {\\n  id\\n  __typename\\n  ... on Collection {\\n    ...collectionUrl_collection\\n    __typename\\n    id\\n  }\\n  ... on User {\\n    ...userUrl_user\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment collectionUrl_collection on Collection {\\n  id\\n  domain\\n  slug\\n  __typename\\n}\\n\\nfragment userUrl_user on User {\\n  __typename\\n  id\\n  customDomainState {\\n    live {\\n      domain\\n      __typename\\n    }\\n    __typename\\n  }\\n  username\\n  hasSubdomain\\n}\\n\\nfragment PublisherAboutLink_publisher on Publisher {\\n  __typename\\n  id\\n  ... on Collection {\\n    slug\\n    __typename\\n    id\\n  }\\n  ... on User {\\n    ...userUrl_user\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment PublisherFollowButton_publisher on Publisher {\\n  __typename\\n  ... on Collection {\\n    ...CollectionFollowButton_collection\\n    __typename\\n    id\\n  }\\n  ... on User {\\n    ...UserFollowButton_user\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment CollectionFollowButton_collection on Collection {\\n  __typename\\n  id\\n  name\\n  canToggleEmail\\n  slug\\n  ...collectionUrl_collection\\n  ...SusiClickable_collection\\n}\\n\\nfragment SusiClickable_collection on Collection {\\n  ...SusiContainer_collection\\n  __typename\\n  id\\n}\\n\\nfragment SusiContainer_collection on Collection {\\n  name\\n  ...SignInOptions_collection\\n  ...SignUpOptions_collection\\n  __typename\\n  id\\n}\\n\\nfragment SignInOptions_collection on Collection {\\n  id\\n  name\\n  __typename\\n}\\n\\nfragment SignUpOptions_collection on Collection {\\n  id\\n  name\\n  __typename\\n}\\n\\nfragment UserFollowButton_user on User {\\n  ...UserFollowButtonSignedIn_user\\n  ...UserFollowButtonSignedOut_user\\n  __typename\\n  id\\n}\\n\\nfragment UserFollowButtonSignedIn_user on User {\\n  id\\n  __typename\\n}\\n\\nfragment UserFollowButtonSignedOut_user on User {\\n  id\\n  ...SusiClickable_user\\n  __typename\\n}\\n\\nfragment SusiClickable_user on User {\\n  ...SusiContainer_user\\n  __typename\\n  id\\n}\\n\\nfragment SusiContainer_user on User {\\n  ...SignInOptions_user\\n  ...SignUpOptions_user\\n  __typename\\n  id\\n}\\n\\nfragment SignInOptions_user on User {\\n  id\\n  name\\n  __typename\\n}\\n\\nfragment SignUpOptions_user on User {\\n  id\\n  name\\n  __typename\\n}\\n\\nfragment PublisherFollowerCount_publisher on Publisher {\\n  __typename\\n  id\\n  ... on Collection {\\n    slug\\n    subscriberCount\\n    __typename\\n    id\\n  }\\n  ... on User {\\n    socialStats {\\n      followerCount\\n      __typename\\n    }\\n    username\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment AutoFollowWrapper_user on User {\\n  id\\n  name\\n  viewerEdge {\\n    id\\n    isAllowEdsEnabled\\n    isFollowing\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment UserProfileBooksLink_publisher on Publisher {\\n  __typename\\n  id\\n  ... on User {\\n    ...userUrl_user\\n    bookAuthor {\\n      ... on Author {\\n        id\\n        __typename\\n      }\\n      __typename\\n      id\\n    }\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment UserProfileCatalogsLink_publisher on Publisher {\\n  __typename\\n  id\\n  ... on User {\\n    ...userUrl_user\\n    homePostsPublished: homepagePostsConnection(paging: {limit: 1}) {\\n      posts {\\n        id\\n        __typename\\n      }\\n      __typename\\n    }\\n    viewerEdge {\\n      tabLinkCatalogsConnection: catalogsConnection(\\n        pagingOptions: {limit: 1}\\n        type: LISTS\\n      ) {\\n        catalogs {\\n          id\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n      id\\n    }\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment UserSubscribeButton_user on User {\\n  id\\n  name\\n  viewerEdge {\\n    id\\n    isFollowing\\n    __typename\\n  }\\n  viewerIsUser\\n  newsletterV3 {\\n    id\\n    ...NewsletterV3Promo_newsletterV3\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment NewsletterV3Promo_newsletterV3 on NewsletterV3 {\\n  slug\\n  name\\n  description\\n  ...NewsletterV3AmpButton_newsletterV3\\n  ...NewsletterV3SubscribeButton_newsletterV3\\n  ...NewsletterV3SubscribeByEmail_newsletterV3\\n  __typename\\n  id\\n}\\n\\nfragment NewsletterV3AmpButton_newsletterV3 on NewsletterV3 {\\n  id\\n  collection {\\n    ...collectionDefaultBackgroundTheme_collection\\n    __typename\\n    id\\n  }\\n  __typename\\n}\\n\\nfragment collectionDefaultBackgroundTheme_collection on Collection {\\n  colorPalette {\\n    ...collectionDefaultBackgroundTheme_colorPalette\\n    __typename\\n  }\\n  customStyleSheet {\\n    id\\n    ...collectionDefaultBackgroundTheme_customStyleSheet\\n    __typename\\n  }\\n  __typename\\n  id\\n}\\n\\nfragment collectionDefaultBackgroundTheme_colorPalette on ColorPalette {\\n  ...customDefaultBackgroundTheme_colorPalette\\n  __typename\\n}\\n\\nfragment collectionDefaultBackgroundTheme_customStyleSheet on CustomStyleSheet {\\n  id\\n  ...customDefaultBackgroundTheme_customStyleSheet\\n  __typename\\n}\\n\\nfragment NewsletterV3SubscribeButton_newsletterV3 on NewsletterV3 {\\n  id\\n  name\\n  slug\\n  type\\n  user {\\n    name\\n    username\\n    __typename\\n    id\\n  }\\n  collection {\\n    slug\\n    ...SusiClickable_collection\\n    ...collectionDefaultBackgroundTheme_collection\\n    __typename\\n    id\\n  }\\n  ...SusiClickable_newsletterV3\\n  __typename\\n}\\n\\nfragment SusiClickable_newsletterV3 on NewsletterV3 {\\n  ...SusiContainer_newsletterV3\\n  __typename\\n  id\\n}\\n\\nfragment SusiContainer_newsletterV3 on NewsletterV3 {\\n  ...SignInOptions_newsletterV3\\n  ...SignUpOptions_newsletterV3\\n  __typename\\n  id\\n}\\n\\nfragment SignInOptions_newsletterV3 on NewsletterV3 {\\n  id\\n  name\\n  __typename\\n}\\n\\nfragment SignUpOptions_newsletterV3 on NewsletterV3 {\\n  id\\n  name\\n  __typename\\n}\\n\\nfragment NewsletterV3SubscribeByEmail_newsletterV3 on NewsletterV3 {\\n  id\\n  slug\\n  collection {\\n    ...collectionDefaultBackgroundTheme_collection\\n    ...collectionUrl_collection\\n    __typename\\n    id\\n  }\\n  __typename\\n}\\n\\nfragment MetaHeaderLogo_publisher on Publisher {\\n  __typename\\n  id\\n  name\\n  ... on Collection {\\n    logo {\\n      ...MetaHeaderLogo_imageMetadata\\n      ...PublisherLogo_image\\n      __typename\\n      id\\n    }\\n    __typename\\n    id\\n  }\\n  ...auroraHooks_publisher\\n}\\n\\nfragment auroraHooks_publisher on Publisher {\\n  __typename\\n  ... on Collection {\\n    isAuroraEligible\\n    isAuroraVisible\\n    viewerEdge {\\n      id\\n      isEditor\\n      __typename\\n    }\\n    __typename\\n    id\\n  }\\n  ... on User {\\n    isAuroraVisible\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment MetaHeaderNavVertical_publisher on Publisher {\\n  id\\n  ...PublisherAboutLink_publisher\\n  ...MetaHeaderNav_publisher\\n  ...MetaHeaderNavLink_publisher\\n  __typename\\n}\\n\\nfragment MetaHeaderTagline_publisher on Publisher {\\n  __typename\\n  ... on Collection {\\n    tagline\\n    __typename\\n    id\\n  }\\n  ... on User {\\n    bio\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment MetaHeaderThemeProvider_publisher on Publisher {\\n  __typename\\n  customStyleSheet {\\n    ...MetaHeaderThemeProvider_customStyleSheet\\n    __typename\\n    id\\n  }\\n  ... on Collection {\\n    colorPalette {\\n      ...customDefaultBackgroundTheme_colorPalette\\n      __typename\\n    }\\n    __typename\\n    id\\n  }\\n}\\n\\nfragment MetaHeaderActions_publisher on Publisher {\\n  __typename\\n  ...MetaHeaderPubMenu_publisher\\n  ...SearchWidget_publisher\\n  ... on Collection {\\n    id\\n    creator {\\n      id\\n      __typename\\n    }\\n    customStyleSheet {\\n      navigation {\\n        navItems {\\n          name\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n      id\\n    }\\n    ...CollectionAvatar_collection\\n    ...CollectionMetabarActionsPopover_collection\\n    ...MetaHeaderActions_collection_common\\n    __typename\\n  }\\n  ... on User {\\n    id\\n    ...UserAvatar_user\\n    __typename\\n  }\\n}\\n\\nfragment MetaHeaderPubMenu_publisher on Publisher {\\n  __typename\\n  ... on Collection {\\n    id\\n    slug\\n    name\\n    ...MutePopoverOptions_collection\\n    __typename\\n  }\\n  ... on User {\\n    id\\n    ...MutePopoverOptions_creator\\n    __typename\\n  }\\n}\\n\\nfragment MutePopoverOptions_collection on Collection {\\n  id\\n  __typename\\n}\\n\\nfragment MutePopoverOptions_creator on User {\\n  id\\n  __typename\\n}\\n\\nfragment SearchWidget_publisher on Publisher {\\n  __typename\\n  ... on Collection {\\n    id\\n    slug\\n    name\\n    domain\\n    __typename\\n  }\\n  ... on User {\\n    id\\n    name\\n    __typename\\n  }\\n  ...algoliaSearch_publisher\\n}\\n\\nfragment algoliaSearch_publisher on Publisher {\\n  __typename\\n  id\\n}\\n\\nfragment CollectionAvatar_collection on Collection {\\n  name\\n  avatar {\\n    id\\n    __typename\\n  }\\n  ...collectionUrl_collection\\n  __typename\\n  id\\n}\\n\\nfragment CollectionMetabarActionsPopover_collection on Collection {\\n  id\\n  slug\\n  isAuroraEligible\\n  isAuroraVisible\\n  newsletterV3 {\\n    id\\n    slug\\n    __typename\\n  }\\n  ...collectionUrl_collection\\n  __typename\\n}\\n\\nfragment MetaHeaderActions_collection_common on Collection {\\n  creator {\\n    id\\n    __typename\\n  }\\n  __typename\\n  id\\n}\\n\\nfragment UserAvatar_user on User {\\n  __typename\\n  username\\n  id\\n  name\\n  imageId\\n  mediumMemberAt\\n  ...userUrl_user\\n}\\n\\nfragment MetaHeaderTop_publisher on Publisher {\\n  __typename\\n  ... on Collection {\\n    slug\\n    ...CollectionMetabarActionsPopover_collection\\n    ...CollectionAvatar_collection\\n    ...MetaHeaderTop_collection\\n    __typename\\n    id\\n  }\\n  ... on User {\\n    username\\n    id\\n    __typename\\n  }\\n}\\n\\nfragment MetaHeaderTop_collection on Collection {\\n  id\\n  creator {\\n    id\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment PublisherFollowList_userConnection on UserConnection {\\n  __typename\\n  users {\\n    __typename\\n    bio\\n    id\\n    name\\n    ...PublisherAvatar_publisher\\n    ...PublisherFollowButton_publisher\\n    ...userUrl_user\\n  }\\n}\\n\\nfragment PublisherAvatar_publisher on Publisher {\\n  __typename\\n  ... on Collection {\\n    id\\n    ...CollectionAvatar_collection\\n    __typename\\n  }\\n  ... on User {\\n    id\\n    ...UserAvatar_user\\n    __typename\\n  }\\n}\\n\\nfragment UserProfileMetadata_user on User {\\n  id\\n  username\\n  name\\n  bio\\n  imageId\\n  twitterScreenName\\n  socialStats {\\n    followerCount\\n    followingCount\\n    __typename\\n  }\\n  ...UserProfileNav_user\\n  ...userUrl_user\\n  __typename\\n}\\n\\nfragment UserProfileNav_user on User {\\n  id\\n  navItems {\\n    title\\n    href: url\\n    __typename\\n  }\\n  __typename\\n}\\n\"}"

data = "{\"operationName\":\"VisitorQuery\",\"variables\":{},\"query\":\"query VisitorQuery {\\n  visitor {\\n    id\\n    isBot\\n    geolocation {\\n      country\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}"

# fp = open("medium_scraper/data.json", "w")
# data = json.dump(json.loads(data), fp)
# fp = open("medium_scraper/data.json", "r")
# data = json.load(fp)
# fp = open("medium_scraper/headers.json", "r")
# headers = json.load(fp)

# print(type(data))
# print(type(headers))
# re = requests.post(url="https://medium.com/_/graphql", headers=headers, json=data)
# print(re.content)
# /html/body/script[4]/text()

# res = requests.get(url="https://medium.com/@marcopeixeiro/followers")

# bs = BeautifulSoup(res.text, "html.parser")

# nach reihenfolge - nicht sehr zuverlässig, vll mit regex suchen
# x = bs.findAll("script")[5].string

# a = re.search("(?<=window.__APOLLO_STATE__ = ).*",x).group(0)

# a_json = json.loads(a)

# a_json = list(a_json.items())

# root_query = a_json[0]
# user_id_0 = a_json[1][1]["id"]
# user_id_0 = a_json[1][1]["username"]
# user_id_1 = a_json[2][1]["id"]
# user_id_2 = a_json[3][1]["id"]
# user_id_3 = a_json[4][1]["id"]

# # user
# user =  a_json[1][1]
# user_id = user["id"]
# info = user["bio"]
# full_name = user["name"]
# user_name = user["username"]
# image_id = user["imageId"]
# follower_count = user["followerCount"]
# following_count = user["followingCount"]
# url = "mediu.com/"+user_name
# # followers
# for i in range(2, 9):
#     ser =  a_json[i][1]
#     user_id = user["id"]
#     info = user["bio"]
#     full_name = user["name"]
#     user_name = user["username"]
#     image_id = user["imageId"]
#     follower_count = user["followerCount"]
#     following_count = user["followingCount"]
#     url = "medium.com/@"+user_name

#     Users.objects.update_or_create(user_name = user_name, defaults={"medium_id":user_id, "user_name":user_name, "full_name":full_name, "info":info , "follower_count":follower_count , "following_count":following_count , "url":url , "image_id":image_id})

# (medium_id, user_name = , full_name = , info = , followers = , following = , url = , member_since = , image_id = )

# fp = open("medium_scraper/data/headers.json", "w")
# json.dump(headers, fp)

# usrs = Users.objects.filter(last_updated__isnull=False).values("url", "last_updated")

# for u in usrs:
#     print(u["last_updated"])


user = Users.objects.all().values()

print()

