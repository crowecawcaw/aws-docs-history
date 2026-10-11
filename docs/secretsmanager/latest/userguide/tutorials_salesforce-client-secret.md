

# Create a Salesforce client secret
<a name="tutorials_salesforce-client-secret"></a>

In this tutorial, you create a Salesforce client secret and store it in AWS Secrets Manager as a [managed external secret](managed-external-secrets.md), turn on managed rotation, and then test the rotated credentials by exchanging them for an access token. This tutorial takes approximately 20–30 minutes to complete.

This tutorial uses AWS services that might incur charges to your AWS account, including charges for the secret you store in Secrets Manager and, if you choose to use one, a customer managed key. For more information, see [Pricing](intro.md#asm_pricing).

**Note**  
This tutorial uses the [SalesforceClientSecret](mes-partner-salesforce.md) secret type as an example. Other managed external secrets types follow a similar flow. You create the secret using the format the integration partner defines, turn on managed rotation, and then use the rotated credentials. For the list of onboarded partners and their required secret formats, see [Integration Partners](mes-partners.md).

Before you begin this tutorial, make sure you have the following.
+ A Salesforce account (developer or otherwise) that allows you to create External Client Apps (ECAs).
+ Administrative permissions to your AWS account. In a production setting, it is a best practice to use different roles for different tasks. For example, a role that manages secrets in your organization would create the secret, and a separate role would use the secret at runtime. For the tutorial steps, we recommend you continue using the same identity. For information about how to set up permissions in a production environment, see [Authentication and access control for AWS Secrets Manager](auth-and-access.md).

**Topics**
+ [Step 1: Create an External Client App and enable OAuth](#tutorials_salesforce-client-secret_step1)
+ [Step 2: Create the managed external secret and enable rotation](#tutorials_salesforce-client-secret_step2)
+ [Step 3: Test the rotated credentials](#tutorials_salesforce-client-secret_step3)
+ [Step 4: Clean up resources](#tutorials_salesforce-client-secret_step4)
+ [Next steps](#tutorials_salesforce-client-secret_nextsteps)

## Step 1: Create an External Client App and enable OAuth
<a name="tutorials_salesforce-client-secret_step1"></a>

The first step is to create an External Client App (ECA) in Salesforce and configure it for OAuth so that Secrets Manager can rotate the client secret. For the full Salesforce procedure, see [Set up authorization with an External Client App](https://developer.salesforce.com/docs/platform/accsdk/guide/acc-sdk-setup-auth-external.html) in the Salesforce documentation.

As you set up the ECA, make sure you configure the following:
+ At the org level, enable **Allow access to External Client App consumer secrets via REST API**. This setting allows Secrets Manager to retrieve and rotate the consumer secret through the Salesforce REST API.
+ On the ECA, enable the OAuth scope **Manage user data via APIs (api)**.
+ On the ECA, enable **Enable Client Credentials Flow**.
+ On the ECA, enable **Enable Token Exchange Flow** and **Require secret for Token Exchange Flow**.

After you create the ECA, gather the values you need to store in the secret in the next step:
+ The **consumer key** (client ID) and **consumer secret** (client secret) from the ECA Manager OAuth settings.
+ Your Salesforce My Domain base URL, for example `https://{{MyDomainName}}.my.salesforce.com`.
+ The **app ID** and **consumer ID** for the ECA. These correspond to the `external_client_app_identifier` and `consumer_id` fields in the Salesforce documentation. To learn how to retrieve these values, see [Stage OAuth Credentials](https://help.salesforce.com/s/articleView?id=xcloud.eca_stage_oauth_credentials.htm&type=5) in the Salesforce documentation.

For a description of each field required in the secret, see [Salesforce Client Secret](mes-partner-salesforce.md).

## Step 2: Create the managed external secret and enable rotation
<a name="tutorials_salesforce-client-secret_step2"></a>

Next, you store the Salesforce client secret in Secrets Manager as a managed external secret and turn on managed rotation. With managed rotation, you don't create or maintain a Lambda rotation function. Secrets Manager rotates the secret for you.

**To create the secret and turn on rotation (console)**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following:

   1. For **Secret type**, choose the Salesforce client secret managed external secret type (**SalesforceClientSecret**).

   1. Enter the secret value fields for the Salesforce client secret: the consumer key, consumer secret, base URI, app ID, and consumer ID. For a description of each field, see [Salesforce Client Secret](mes-partner-salesforce.md).

   1. For **Encryption key**, choose **aws/secretsmanager** to use the AWS managed key for Secrets Manager. There is no cost for using this key. You can also use your own customer managed key. For information about the costs of using a customer managed key, see [Pricing](intro.md#asm_pricing).

   1. Choose **Next**.

1. On the **Configure secret** page, enter a descriptive **Secret name** and **Description**, and then choose **Next**.

1. On the **Configure rotation** page, do the following. For managed external secrets, rotation is enabled by default during secret creation.

   1. Confirm that **Automatic rotation** is turned on.

   1. Under **Rotation metadata**, for **API version** (`apiVersion`), enter your Salesforce organization's API version. This field is required. It must be in the format `v{{XX.X}}`, where {{X}} is a numeric character, and must be at least `v65.0`. If you want Secrets Manager to rotate the secret using a separate set of administrative credentials, also provide the admin secret ARN. For a description of each metadata field, see [Salesforce Client Secret](mes-partner-salesforce.md).

   1. In **Service permissions for secret rotation**, choose **Create a new role** to automatically create an IAM role with the permissions Secrets Manager needs to rotate the secret. By default, permissions are scoped to the integration partner in the AWS Region where the secret is created. For more information, see [Security and permissions](mes-security.md).

   1. Under **Rotation schedule**, enter your schedule in UTC time zone, for example rotate automatically every 30 days.

   1. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

For more ways to configure rotation for a managed external secret, including the AWS AWS CLI, see [Rotate Secrets Manager managed external secrets](rotate-secrets_external.md).

## Step 3: Test the rotated credentials
<a name="tutorials_salesforce-client-secret_step3"></a>

The last step is to confirm that the rotated credentials work by retrieving the secret value and exchanging the credentials for a Salesforce access token.

**To retrieve the secret value (console)**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. On the **Secrets** page, choose your secret.

1. On the **Secret details** page, scroll down and choose **Retrieve secret value**. Note the current `consumerKey` and `consumerSecret` values.

**Note**  
Confirm that the `consumerKey` and `consumerSecret` values have actually changed from the values you originally stored. If they haven't changed, wait a couple of minutes and check again. If they still haven't changed, check AWS CloudTrail for any `RotationFailed` events for the secret, which include details about why rotation failed. For more information, see [My managed external secret is not rotating](troubleshoot.md#troubleshoot-mes-not-rotating).

Next, use the retrieved credentials to request an access token from Salesforce. Replace {{MyDomainName}} with your Salesforce My Domain name, and replace {{consumerKey}} and {{consumerSecret}} with the values you retrieved.

```
curl -X POST "https://{{MyDomainName}}.my.salesforce.com/services/oauth2/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id={{consumerKey}}" \
  -d "client_secret={{consumerSecret}}"
```

If the credentials are valid, Salesforce returns a JSON response that contains an `access_token`. Receiving an access token confirms that the rotated credentials work.

When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. See [Mitigate the risks of using the AWS CLI to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md).

## Step 4: Clean up resources
<a name="tutorials_salesforce-client-secret_step4"></a>

To avoid incurring ongoing charges, delete the resources you created in this tutorial when you no longer need them: the secret and the IAM rotation role that Secrets Manager created. Deleting the secret also stops automatic rotation.

**To delete the secret (console)**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. On the **Secrets** page, choose your secret.

1. In the **Secret details** section, choose **Actions**, and then choose **Delete secret**.

1. In the **Disable secret and schedule deletion** dialog box, enter a waiting period, and then choose **Schedule deletion**. Secrets Manager makes the secret inaccessible immediately and schedules it for deletion after the recovery window. For more information, see [Delete an AWS Secrets Manager secret](manage_delete-secret.md).

**To delete the rotation role (console)**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/), and then choose **Roles**.

1. Find the role that Secrets Manager created for rotation, select it, and then choose **Delete**. For more information, see [Deleting roles or instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html) in the *IAM User Guide*.

## Next steps
<a name="tutorials_salesforce-client-secret_nextsteps"></a>
+ To learn more about managed external secrets and the partners Secrets Manager integrates with, see [Using AWS Secrets Manager managed external secrets to manage Third Party secrets](managed-external-secrets.md).
+ To review the required secret value and rotation metadata fields for Salesforce, see [Salesforce Client Secret](mes-partner-salesforce.md).
+ For more ways to set up rotation for a managed external secret, see [Rotate managed external secrets](rotate-secrets_external.md).
+ You can improve performance and reduce costs by caching secrets. For more information, see [Get secrets from AWS Secrets Manager](retrieving-secrets.md).
+ To learn about the cost of using Secrets Manager, see [Pricing](intro.md#asm_pricing).