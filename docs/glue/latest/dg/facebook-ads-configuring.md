# Configuring Facebook Ads

Before you can use AWS Glue to transfer data from Facebook Ads, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- Facebook Standard accounts are accessed directly through Facebook.
- User authentication is needed to generate the access token.
- The Facebook Ads SDK connector will be implementing the _User Access Token OAuth_ flow.
- We are using OAuth2.0 to authenticate our API requests to Facebook Ads. This web-based authentication falls under the Multi-Factor Authentication (MFA) architecture, which is a superset of 2FA.
- The user needs to grant permissions to access the end points. For accessing the user's data, endpoint authorization is handled through [permissions](https://developers.facebook.com/docs/permissions "https://developers.facebook.com/docs/permissions") and [features](https://developers.facebook.com/docs/features-reference "https://developers.facebook.com/docs/features-reference").

## Getting OAuth 2.0 credentials

To obtain API credentials so that you can make authenticated calls to your instance, see [REST API](https://developers.facebook-ads.com/rest-api/ "https://developers.facebook-ads.com/rest-api/") in the Facebook Ads Developer Guide.
