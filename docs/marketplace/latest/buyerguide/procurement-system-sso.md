# Enabling SSO for procurement system integration

You can enable single sign-on (SSO) for your AWS Marketplace procurement system integration by
passing your IAM Identity Center access portal URL as a query parameter in the punchout configuration.
When enabled, users who access AWS Marketplace through your procurement system are automatically
redirected to your organization's SSO login page instead of the standard AWS sign-in
page.

###### Note

This SSO configuration is compatible with any identity provider supported by IAM Identity Center,
including Okta, Microsoft Entra ID, and the built-in IAM Identity Center directory.

## Prerequisites

Before you enable SSO for procurement system integration, you must have the
following:

- An active procurement system integration with AWS Marketplace. For setup instructions, see
  [Configuring AWS Marketplace to integrate with Coupa](procurement-system-integration-coupa.md "procurement-system-integration-coupa.md") or
  [Configuring AWS Marketplace to integrate with SAP Ariba](procurement-system-integration-ariba.md "procurement-system-integration-ariba.md").
- An IAM Identity Center instance with an access portal URL. For setup instructions, see
  [Enabling IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
  _IAM Identity Center User Guide_.
- Users who will access AWS Marketplace must be provisioned in IAM Identity Center with
  appropriate permission sets. For more information, see
  [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the
  _IAM Identity Center User Guide_. Contact your IAM or identity team
  if you have questions about user provisioning.
- Administrative access to your procurement system (Coupa or SAP Ariba) to modify
  the punchout supplier URL.

## How SSO for procurement system integration works

When you configure SSO for procurement system integration, the authentication flow works
as follows:

1. A user in your procurement system initiates a punchout session. The procurement
   system sends the `idc_url` parameter along with the cXML PunchOutSetupRequest.
2. AWS Marketplace reads the `idc_url` parameter and redirects the user to your
   IAM Identity Center access portal URL instead of the standard AWS sign-in page.
3. The user authenticates through your organization's identity provider. This follows
   your organization's standard authentication policies, including any multi-factor
   authentication (MFA) requirements.
4. After authentication, IAM Identity Center issues a session token and the user is
   redirected back to the AWS Marketplace punchout session to browse and request products.

## Step 1: Find your IAM Identity Center access portal URL

Use the following procedure to locate your IAM Identity Center access portal URL.

###### To find your IAM Identity Center access portal URL

1. Open the IAM Identity Center console at
   [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. In the navigation pane, choose **Settings**.
3. On the **Identity source** tab, locate the **AWS access
   portal URL**.
4. Copy this URL.

Your access portal URL looks similar to the following example:

`https://d-1234567890.awsapps.com/start`

For more information, see
[Customizing the AWS access portal URL](../../../singlesignon/latest/userguide/howtochangeURL.md "../../../singlesignon/latest/userguide/howtochangeURL.md")
in the _IAM Identity Center User Guide_.

## Step 2: Add the idc\_url parameter to your punchout supplier URL

In your procurement system (Coupa or SAP Ariba), append the `idc_url` query
parameter to the AWS Marketplace punchout supplier URL. The `idc_url` value is your
IAM Identity Center instance access portal URL.

**Example:**

```
https://eprocurement.marketplace.us-east-1.amazonaws.com/v1/punchout/setup?idc_url=https://d-1234567890.awsapps.com/start
```

## Step 3: (Optional) Configure relay state for direct console access

If you want users to land on a specific AWS console page after SSO authentication,
configure a relay state in your IAM Identity Center permission set. Without a relay state,
users land on the AWS Management Console after authenticating.

Configuring a relay state is optional, but strongly recommended.

###### To configure relay state

1. Open the IAM Identity Center console at
   [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. Under **Multi-account permissions**, choose **Permission
   sets**.
3. Choose the permission set your procurement users use.
4. Choose **Edit**.
5. Under **Relay state**, enter:
   `https://console.aws.amazon.com/marketplace`
6. Choose **Save changes**.

For more information, see
[Set relay state for quick access to the
AWS Management Console](../../../singlesignon/latest/userguide/howtopermrelaystate.md "../../../singlesignon/latest/userguide/howtopermrelaystate.md") in the _IAM Identity Center User Guide_.

## Requirements and limitations

SSO requirements and limitations| Requirement | Details |
| --- | --- |
| Parameter is optional | If the `idc_url` parameter is omitted, users see the standard AWS sign-in page. |
| No domain validation | AWS Marketplace does not validate the domain in the `idc_url` parameter. The procurement<br>administrator is responsible for providing the correct IAM Identity Center access portal URL. |
| Supported identity providers | Any identity provider supported by IAM Identity Center, including Okta, Microsoft Entra ID,<br>and the built-in IAM Identity Center directory. |

## Troubleshooting

The following table describes common issues and their resolutions.

SSO troubleshooting| Issue | Cause | Resolution |
| --- | --- | --- |
| Users see the standard AWS sign-in page | The `idc_url` parameter is missing or was not saved correctly. | Verify the supplier URL contains `?idc_url=<your-url>` and<br>confirm the change was saved. |
| SSO page loads but authentication fails | The IAM Identity Center URL is incorrect or the user is not provisioned. | Verify the access portal URL by opening it directly in a browser. Confirm the<br>user is provisioned in IAM Identity Center. |
| Users prompted to sign in again during session | IAM Identity Center session duration is shorter than the punchout session. | Review session duration settings in IAM Identity Center under<br>**Settings**, **Authentication**. |
