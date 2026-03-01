# Setting up SSO for CloudWatch dashboard sharing

To set up dashboard sharing through a third-party single sign-on provider that
supports SAML, follow these steps.

###### Important

We strongly recommend that you do not share dashboards using a non-SAML SSO
provider. Doing so causes a risk of inadvertently allowing third parties to
access your account's dashboards.

###### To set up an SSO provider to enable dashboard sharing

1. Integrate the SSO provider with Amazon Cognito. For more information,
   see [Integrating Third-Party SAML Identity Providers with Amazon Cognito User Pools](../../../cognito/latest/developerguide/cognito-user-pools-integrating-3rd-party-saml-providers.md "../../../cognito/latest/developerguide/cognito-user-pools-integrating-3rd-party-saml-providers.md").
2. Download the metadata XML file from your SSO provider.
3. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
4. In the navigation pane, choose **Settings**.
5. In the **Dashboard sharing** section, choose **Configure**.
6. Choose **Manage SSO providers**.

This opens the Amazon Cognito console in the US East (N. Virginia) Region
(us-east-1). If you don't see any **User Pools**, the Amazon Cognito
console might have opened in a different Region. If so, change the Region to
**US East (N. Virginia) us-east-1** and proceed with
the next steps. 7. Choose the **CloudWatchDashboardSharing** pool. 8. In the navigation pane, choose **Social and external providers**. 9. Choose **Add identity provider**. 10. Choose **SAML**. 11. Enter a name for your SSO provider in **Provider name**. 12. Choose **Select file**, and select the
metadata XML file that you downloaded in step 2. 13. Choose **Create provider**.
