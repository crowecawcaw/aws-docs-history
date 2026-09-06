

# Creating SMTP credentials using Mail Manager
<a name="smtp-credentials-mail-manager"></a>

You can use Mail Manager to create SMTP credentials from the SES console. The console creates the supporting Mail Manager resources for you, including a [Traffic policies and policy statements](eb-filters.md), a [Rule sets and rules](eb-rules.md), an IAM role, and an authenticated [Ingress endpoints](eb-ingress.md).

In Regions where both options are available, we recommend using Mail Manager because it's available in all AWS Regions — including opt-in Regions and the European Sovereign Cloud — and the console creates and configures the required resources for you. The IAM user credential flow described in [Obtaining Amazon SES SMTP credentials](smtp-credentials.md) remains available in the Regions where it's currently supported.

**Region availability**  
In opt-in Regions and the European Sovereign Cloud, Mail Manager is the only option for creating SMTP credentials. In all other Regions, you can use either Mail Manager (recommended) or the IAM user credential flow.

## Prerequisites
<a name="smtp-credentials-mail-manager-prereqs"></a>

Before you create SMTP credentials with Mail Manager, verify that your IAM user or role has permissions to perform the following actions:
+ Create Mail Manager [Traffic policies and policy statements](eb-filters.md)
+ Create Mail Manager [Rule sets and rules](eb-rules.md)
+ Create Mail Manager [Ingress endpoints](eb-ingress.md)
+ Create IAM roles. If you provide your own role instead, it must include the permissions described in [Permission policy for *Send to internet* rule action](eb-policies.md#eb-policies-internet).
+ If you choose to auto-generate a password, the `secretsmanager:GetRandomPassword` permission for AWS Secrets Manager. For more information, see [GetRandomPassword](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html) in the *AWS Secrets Manager API Reference*.

## To create SMTP credentials using Mail Manager
<a name="smtp-credentials-mail-manager-procedure"></a>

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. Choose **SMTP settings** in the left navigation pane.

1. Choose **Create SMTP credentials**. In Regions that offer both options, select **Mail Manager** (recommended).

1. For **Ingress endpoint name**, enter a name for your ingress endpoint or use the auto-populated default name.

1. For **Authentication type**, choose one of the following:
   + **SMTP password** – Enter a custom password or choose **Auto-generate** to create one automatically. The password must be 8–64 characters and include at least one uppercase letter, one lowercase letter, one digit, and one special character.
   + **Secret** – Select an existing secret in AWS Secrets Manager, or create a new secret. The secret must be an **Other type of secret** with a key/value pair in which the key is `password` and the value is your password. For more information about configuring the secret, see [Creating an ingress endpoint in the SES console](eb-ingress.md#eb-ingress-create-console).

1. Choose **Create SMTP credentials**. The console creates a traffic policy, rule set, IAM role, and authenticated ingress endpoint with auto-generated names.

1. Wait for the ingress endpoint status to become **Active**. The console displays provisioning progress.

1. Choose **Download .csv** to save your credentials. The .csv file contains the SMTP endpoint, port, username (raw and base64-encoded), and password (raw and base64-encoded).

**Important**  
You cannot retrieve your password after you leave this page. Download the .csv file or copy your credentials before closing the dialog.

**Note**  
After you create your credentials, you can change the password or secret at any time on the ingress endpoint details page. For more information, see [Ingress endpoints](eb-ingress.md).

## Advanced settings
<a name="smtp-credentials-mail-manager-advanced"></a>

The form includes an optional **Advanced settings** section where you can customize the following options:
+ **Traffic policy** – Select an existing traffic policy or create a new one with a custom name.
+ **Rule set** – Select an existing rule set or create a new one with a custom name.
+ **IAM role** – Enter the ARN of an existing IAM role or create a new role in the IAM console. If you create the role yourself, it must include the permissions described in [Permission policy for *Send to internet* rule action](eb-policies.md#eb-policies-internet).
+ **Network type** – Choose **Public** (default) or **Private**. If you choose **Private**, you must provide a Amazon VPC endpoint ID. For more information, see [Receiving email through Amazon VPC endpoints](eb-ingress.md#eb-ingress-vpc-endpoint).
+ **IP address type** (public only) – Choose **IPv4** (default) or **Dual-stack**.

If you don't expand the advanced settings, default values are used and new resources are created automatically.

## Error handling
<a name="smtp-credentials-mail-manager-troubleshooting"></a>

The following table describes errors that might occur during the creation process and how to resolve them.


| Error | Cause | Solution | 
| --- | --- | --- | 
| Resource creation failed | Your IAM user or role doesn't have permissions to create one of the required resources (traffic policy, rule set, IAM role, or ingress endpoint). | Verify that you have the permissions listed in [Prerequisites](#smtp-credentials-mail-manager-prereqs), and then choose Retry. Any resources that were already created are rolled back automatically. | 
| Ingress endpoint provisioning failed | An error occurred while provisioning the ingress endpoint. | Check the status of the ingress endpoint in Mail Manager. The error banner includes a link to Mail Manager for further troubleshooting. | 
| Password generation failed | Your IAM user or role doesn't have the secretsmanager:GetRandomPassword permission. | Enter a custom password manually, or add the permission and try again. | 
| Provisioning timeout | The console stopped checking the ingress endpoint status after 10 minutes before it reached Active. | Use the link provided in the timeout message to check the current status of your ingress endpoint in Mail Manager. | 