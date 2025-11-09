# FIPS Endpoints for User Streaming Sessions

If you use SAML 2.0 or a streaming URL to authenticate users, you can configure FIPS-compliant connections for your users' streaming sessions.

To use a FIPS-compliant connection for users who authenticate using SAML 2.0, specify an WorkSpaces Applications FIPS endpoint when you configure the relay state of your federation. For more information about constructing a relay state URL for identity federation using SAML 2.0, see [Setting Up SAML](external-identity-providers-setting-up-saml.md "external-identity-providers-setting-up-saml.md").

To configure a FIPS-compliant connection for users who authenticate through a
streaming URL, specify an WorkSpaces Applications FIPS endpoint when you call the [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") or
[CreateImageBuilderStreamingURL](../APIReference/API_CreateImageBuilderStreamingURL.md "../APIReference/API_CreateImageBuilderStreamingURL.md") operation from the AWS CLI or an AWS
SDK. A user who connects to a streaming instance using the resulting URL is
connected through a FIPS-compliant connection. The following example uses the WorkSpaces Applications
FIPS endpoint in the US East (Virginia) Region to generate a FIPS-compliant
streaming URL:

```
`aws appstream create-streaming-url --stack-name` `stack-name` `--fleet-name` `fleet-name` `--user-id` `user-id` `--endpoint-url https://appstream2-fips.us-east-1.amazonaws.com`
```
