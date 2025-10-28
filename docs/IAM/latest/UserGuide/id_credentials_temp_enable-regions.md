# Manage AWS STS in an AWS Region

A Regional endpoint is the URL of the entry point within a particular region for an AWS
web service. AWS recommends using Regional AWS Security Token Service (AWS STS) endpoints instead of the global
endpoint to reduce latency, build in redundancy, and increase session token validity. Although
the global (legacy) AWS STS endpoint `https://sts.amazonaws.com` is highly available,
it’s hosted in a single AWS Region, US East (N. Virginia), and like other endpoints, it
doesn’t provide automatic failover to endpoints in other Regions.

- **Reduce latency** – By making your AWS STS calls
  to an endpoint that is geographically closer to your services and applications, you can
  access AWS STS services with lower latency and better response times.
- **Build in redundancy** – You can limit the
  effects of a failure within a workload to a limited number of components with a
  predictable scope of impact containment. Using regional AWS STS endpoints lets you align
  the scope of your components with the scope of your session tokens. For more information
  about this reliability pillar, see [Use fault isolation to protect your workload](../../../wellarchitected/latest/reliability-pillar/use-fault-isolation-to-protect-your-workload.md "../../../wellarchitected/latest/reliability-pillar/use-fault-isolation-to-protect-your-workload.md") in the _AWS
  Well-Architected Framework_.
- **Increase session token validity** – Session
  tokens from Regional AWS STS endpoints are valid in all AWS Regions. Session tokens from
  the global STS endpoint are valid only in AWS Regions that are enabled by default. If
  you intend to enable a new Region for your account, you can use session tokens from
  Regional AWS STS endpoints. If you choose to use the global endpoint, you must change the
  Region compatibility of AWS STS session tokens for the global endpoint. Doing so ensures
  that tokens are valid in all AWS Regions.
  For a list of AWS STS Regions and their endpoints, see [AWS STS Regions and endpoints](id_credentials_temp_region-endpoints.md "id_credentials_temp_region-endpoints.md").

###### Note

AWS has made changes to the AWS Security Token Service (AWS STS) global endpoint
(`https://sts.amazonaws.com`) in Regions [enabled by default](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") to
enhance its resiliency and performance. AWS STS requests to the global endpoint are
automatically served in the same AWS Region as your workloads. These changes will not be
deployed to opt-in Regions. We recommend that you use the appropriate AWS STS regional
endpoints. For more information, see [AWS STS global endpoint
changes](id_credentials_temp_region-endpoints.md#reference_sts_global_endpoint_changes "id_credentials_temp_region-endpoints.md#reference_sts_global_endpoint_changes").

###### Topics

- [Activating and deactivating AWS STS in an
  AWS Region](#sts-regions-activate-deactivate "#sts-regions-activate-deactivate")
- [Writing code to use AWS STS
  Regions](#id_credentials_temp_enable-regions_writing_code "#id_credentials_temp_enable-regions_writing_code")
- [Managing global endpoint session tokens](#sts-regions-manage-tokens "#sts-regions-manage-tokens")

## Activating and deactivating AWS STS in an

AWS Region

When you activate AWS STS endpoints for a Region, AWS STS can issue temporary credentials to
users and roles in your account that make an AWS STS request. Those credentials can then be
used in any Region that is enabled by default or is manually enabled. For Regions that are
enabled by default, you must activate the Regional AWS STS endpoint in the account where the
temporary credentials are generated. It does not matter whether a user is signed into the
same account or a different account when they make the request. When requesting temporary
credentials for a role in another AWS account using a Region that is manually enabled,
the target account (the account containing the role) must enable that Region for AWS STS
operations. This ensures that the temporary security credentials can be generated
correctly.

For example, imagine a user in account A wants to send an `sts:AssumeRole`
API request to the [AWS STS Regional
endpoint](id_credentials_temp_region-endpoints.md "id_credentials_temp_region-endpoints.md")
`https://sts.ap-southeast-3.amazonaws.com`. The request is for temporary
credentials for the role named `Developer` in account B. Because the request is
to create credentials for an entity in account B, account B must have the
`ap-southeast-3` Region enabled. Users from account A (or any other account)
can call the `ap-southeast-3` AWS STS endpoint to request credentials for account
B whether or not the Region is activated in their accounts. To learn more, see [Enable or
disable AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md").

###### Note

Active Regions are available to everyone that uses temporary credentials in that
account. To control which IAM users or roles can access the Region, use the
`aws:RequestedRegion` condition key in your permissions policies.

###### To activate or deactivate AWS STS in a Region that is enabled by default

(console)

1. Sign in as a root user or a user with permissions to perform IAM administration
   tasks.
2. Open the [IAM console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home") and
   in the navigation pane choose [**Account
   settings**](https://console.aws.amazon.com/iam/home?#account_settings "https://console.aws.amazon.com/iam/home?#account_settings").
3. In the **Security Token Service (STS)** section
   **Endpoints**, find the Region that you want to configure, and
   then choose **Active** or **Inactive** in the
   **STS status** column.
4. In the dialog box that opens, choose **Activate** or
   **Deactivate**.

For Regions that must be enabled, we activate AWS STS automatically when you enable the
Region. After you enable a Region, AWS STS is always active for the Region and you cannot
deactivate it. To learn about enabling Regions that are disabled by default, see [Specifying which AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management
Reference Guide_.

## Writing code to use AWS STS

Regions

After you activate a Region, you can direct AWS STS API calls to that Region. The
following Java code snippet demonstrates how to configure an
`AWSSecurityTokenService` object to make requests to the Europe (Milan)
(eu-south-1) Region.

```
EndpointConfiguration regionEndpointConfig = new EndpointConfiguration("https://sts.eu-south-1.amazonaws.com", "eu-south-1");
AWSSecurityTokenService stsRegionalClient = AWSSecurityTokenServiceClientBuilder.standard()
.withCredentials(credentials)
.withEndpointConfiguration(regionEndpointConfig)
.build();
```

AWS STS recommends that you make calls to a Regional endpoint. To learn how to manually
enable a Region, see [Specify which AWS Regions
your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management Reference
Guide_.

In the example, the first line instantiates an `EndpointConfiguration` object
called `regionEndpointConfig`, passing the URL of the endpoint and the
AWS Region as the parameters.

To learn how to set AWS STS regional endpoints using an environment variable for AWS
SDKs, see [AWS STS Regionalized
endpoints](../../../sdkref/latest/guide/feature-sts-regionalized-endpoints.md "../../../sdkref/latest/guide/feature-sts-regionalized-endpoints.md") in the _AWS SDKs and Tools Reference Guide_.

For all other language and programming environment combinations, refer to the [documentation for the relevant SDK](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").

## Managing global endpoint session tokens

Most AWS Regions are enabled for operations in all AWS services by default. Those
Regions are automatically activated for use with AWS STS. Some Regions, such as Asia Pacific
(Hong Kong), must be manually enabled. To learn more about enabling and disabling
AWS Regions, see [Specify which AWS Regions
your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management Reference
Guide_. When you enable these AWS Regions, they are automatically activated
for use with AWS STS. You cannot activate the AWS STS endpoint for a Region that is disabled.
Session tokens that are valid in all AWS Regions include more characters than tokens that
are valid in Regions that are enabled by default. Changing this setting might affect
existing systems where you temporarily store tokens.

You can change this setting using the AWS Management Console, AWS CLI, or AWS API.

###### To change the Region compatibility of session tokens for the global endpoint

(console)

1. Sign in as a root user or a user with permissions to perform IAM administration
   tasks. To change the compatibility of session tokens, you must have a policy that
   allows the `iam:SetSecurityTokenServicePreferences` action.
2. Open the [IAM console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home"). In
   the navigation pane, choose **Account settings**.
3. Under **Security Token Service (STS)** section **Session
   Tokens from the STS endpoints**. The **Global endpoint**
   indicates `Valid only in AWS Regions enabled by default`. Choose
   **Change**.
4. In the **Change region compatibility** dialog box, select
   **All AWS Regions**. Then choose **Save
   changes**.

###### Note

Session tokens that are valid in all AWS Region include more characters than
tokens that are valid in Regions that are enabled by default. Changing this
setting might affect existing systems where you temporarily store tokens.

###### To change the Region compatibility of session tokens for the global endpoint

(AWS CLI)

Set the session token version. Version 1 tokens are valid only in AWS Regions that
are available by default. These tokens do not work in manually enabled Regions, such as
Asia Pacific (Hong Kong). Version 2 tokens are valid in all Regions. However, version 2 tokens
include more characters and might affect systems where you temporarily store
tokens.

- [`aws iam set-security-token-service-preferences`](../../../cli/latest/reference/iam/set-security-token-service-preferences.md "../../../cli/latest/reference/iam/set-security-token-service-preferences.md")

###### To change the Region compatibility of session tokens for the global endpoint (AWS

API)

Set the session token version. Version 1 tokens are valid only in AWS Regions that
are available by default. These tokens do not work in manually enabled Regions, such as
Asia Pacific (Hong Kong). Version 2 tokens are valid in all Regions. However, version 2 tokens
include more characters and might affect systems where you temporarily store
tokens.

- [`SetSecurityTokenServicePreferences`](../APIReference/API_SetSecurityTokenServicePreferences.md "../APIReference/API_SetSecurityTokenServicePreferences.md")
