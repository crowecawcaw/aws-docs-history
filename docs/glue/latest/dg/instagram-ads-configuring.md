

# Configuring Instagram Ads
<a name="instagram-ads-configuring"></a>

Before you can use AWS Glue to transfer data from Instagram Ads, you must meet these requirements:

## Minimum requirements
<a name="instagram-ads-configuring-min-requirements"></a>

The following are minimum requirements:
+ Instagram Standard accounts are accessed indirectly through Facebook.
+ User authentication is needed to generate the access token.
+ The Instagram Ads SDK connector will be implementing the *User Access Token OAuth* flow.
+ We are using OAuth2.0 to authenticate our API requests to Instagram Ads. This web-based authentication falls under the Multi-Factor Authentication (MFA) architecture, which is a superset of 2FA.
+ The user needs to grant permissions to access the end points. For accessing the user's data, endpoint authorization is handled through [permissions](https://developers.facebook.com/docs/permissions) and [features](https://developers.facebook.com/docs/features-reference).

## Getting OAuth 2.0 credentials
<a name="instagram-ads-configuring-creating-instagram-ads-oauth2-credentials"></a>

To obtain API credentials so that you can make authenticated calls to your instance, see [Graph API](https://developers.facebook.com/docs/graph-api/).