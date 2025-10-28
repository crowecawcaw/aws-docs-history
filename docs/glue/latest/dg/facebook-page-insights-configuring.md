# Configuring Facebook Page Insights

Before you can use AWS Glue to transfer data from Facebook Page Insights, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- Facebook Standard accounts are accessed directly through Facebook.
- User authentication is needed to generate the access token.
- The Facebook Page Insights connector implements the User Access Token OAuth flow.
- The connector uses OAuth2.0 to authenticate our API requests to Facebook Page Insights. This falls under Multi-Factor Authentication (MFA) architecture, which is a superset of 2FA. It is web-based authentication.
- User needs to grant permissions to access the endpoints. For accessing the user's data, endpoint authorization is handled through permissions and features.
