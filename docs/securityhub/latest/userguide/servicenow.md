# Integrations for ServiceNow

This topic describes how to access the Security Hub console to configure an integration for ServiceNow ITSM.
Before completing any of the procedures in this topic, you must have a subscription to ServiceNow ITSM before you can add this integration.
For more information, see [the pricing page](https://www.servicenow.com/lpgp/pricing-itsm.html "https://www.servicenow.com/lpgp/pricing-itsm.html") on the ServiceNow website.

For accounts in an organization, only the delegated administrator can configure an integration.
The delegated administrator can manually use the create ticket feature for any member account findings.
Additionally, the delegated administrator can use [automation rules](security-hub-v2-automation-rules.md "security-hub-v2-automation-rules.md") to automatically create tickets for any findings associated with member accounts.
When defining an automation rule, the delegated administrator can set criteria, which can include all member accounts or specific member accounts.
For information about setting a delegated administrator, see [Setting a delegated administrator account in Security Hub](security-hub-v2-set-da.md "security-hub-v2-set-da.md").

For accounts not in an organization, all aspects of this feature are available.

## Prerequisites - configure ServiceNow environment

You must complete the following prerequisites before configuring an integration for ServiceNow ITSM.
Otherwise, your integration between ServiceNow ITSM and Security Hub will not work.

### 1. Install Security Hubfindings integration for IT Service Management (ITSM)

The following procedure describes how to install Security Hub plugin.

1. Sign into your ServiceNow ITSM instance, and then open the application navigator.
2. Navigate to the [ServiceNow Store](https://store.servicenow.com/store "https://store.servicenow.com/store").
3. Search for _Security Hub findings integration for IT Service Management (ITSM)_, and then choose **Get** to install the application.

###### Note

In the settings for the Security Hub application, choose which action to take when new Security Hub findings are sent to your ServiceNow ITSM environment.
You can choose **Do nothing**, **Create incident**, **Create problem**, or **Create both (incident/problem)**.

### 2. Configure the Client Credentials grant type for inbound OAuth requests

You must configure this grant type for inbound OAuth requests.
For more information, see [Client Credentials grant type for Inbound OAuth is supported](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1645212 "https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1645212") in the ServiceNow Support webpage.

### 3. Create an OAuth application

If you already created an OAuth application, you can skip this prerequisite.
For information about creating an OAuth application, see [Setting up OAuth](https://www.servicenow.com/docs/csh?topicname=client-credentials.html&version=latest "https://www.servicenow.com/docs/csh?topicname=client-credentials.html&version=latest").

## Prerequisites - configure AWS Secrets Manager

To use Security Hub's integration with ServiceNow, the credentials for your ServiceNow OAuth application must be stored in Secrets Manager.
Storing your credentials in Secrets Manager allows you to have control and visibility into the use of the credentials while also allowing Security Hub to use the credentials to integrate with your ServiceNow instance.
To store your credentials in Secrets Manager, you must use a customer managed AWS KMS key to protect the secrets.
This AWS KMS key allows you to protect the secrets while stored at rest and also allows a policy to be attached to the key which gives Security Hub permissions to access the key that is protecting the secret.

Use the following steps to configure Secrets Manager for your ServiceNow credentials.

### Step 1: Attach a policy to your AWS KMS key

To successfully configure your ServiceNow integration, you must first give Security Hub permissions to use the AWS KMS key that will be associated with your ServiceNow credentials in Secrets Manager.

###### To modify the AWS KMS key policy for Security Hub to access your ServiceNow credentials

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. Select an existing AWS KMS key or perform the steps to [Create a new key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS KMS Developer Guide_.
4. In the **Key policy** section, choose **Edit**.
5. If **Switch to policy view** is displayed, choose it to display the Key policy, and then choose **Edit**.
6. Copy the following policy block to your AWS KMS key policy, to grant Security Hub permission to use your key.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Sid": "Enable IAM User Permissions",
        "Effect": "Allow",
        "Principal": {
            "AWS": "arn:aws:iam::`your-account-id`:root"
        },
        "Action": "kms:*",
        "Resource": "*"
        },
        {
        "Sid": "Allow Security Hub connector service to decrypt secrets",
        "Effect": "Allow",
        "Principal": {
            "Service": "connector.securityhub.amazonaws.com"
        },
        "Action": "kms:Decrypt",
        "Resource": "*",
        "Condition": {
            "StringEquals": {
            "kms:ViaService": "secretsmanager.`your-region`.amazonaws.com"
            },
            "StringLike": {
            "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:`your-region`:`your-account-id`:secret:ServiceNow*"
            }
        }
        }
    ]
    }
```

7. Edit the policy by replacing the following values in the policy example:
   - Replace `your-account-id` with your AWS account ID.
   - Replace `your-region` with your AWS region (for example, `us-east-1`).

8. If you added the policy statement before the final statement, add a comma before adding this statement. Make sure that the JSON syntax of your AWS KMS key policy is valid.
9. Choose **Save**.
10. (Optional) Copy the key ARN to a notepad for use in the later steps.

### Step 2: Create the secret in Secrets Manager

Create a secret in Secrets Manager that will store your ServiceNow credentials. Security Hub will access this secret when interacting with your ServiceNow environment.

Follow the steps [To create a secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_. After you create your secret, copy the Secret ARN as you will need this when creating your Security Hub connector.

When creating the secret, ensure you configure the following:

**Secret type**

Other type of secret

**Key/value pairs (Plaintext format)**

```
{
    "ClientId": "`your-servicenow-client-id`",
    "ClientSecret": "`your-servicenow-client-secret`"
    }
```

###### Note

The field names must be exactly `ClientId` and `ClientSecret` (case-sensitive). Security Hub requires these exact names to retrieve the credentials.

**Encryption key**

Use the AWS KMS key you configured in Step 1

**Resource policy**

Use the following resource policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "connector.securityhub.amazonaws.com"
        },
        "Action": "secretsmanager:GetSecretValue",
        "Resource": "arn:aws:secretsmanager:`your-region`:`your-account-id`:secret:ServiceNow*",
        "Condition": {
            "StringEquals": {
            "aws:SourceAccount": "`your-account-id`",
            "aws:SourceArn": "arn:aws:securityhub:`your-region`:`your-account-id`:*"
            }
        }
        }
    ]
    }
```

Now that your secret is configured, you can create a Security Hub connector using the CreateConnectorV2 API or AWS Console. You'll need to provide:

- **InstanceName**: Your ServiceNow instance URL (for example, `your-instance.service-now.com`)
- **SecretArn**: The ARN of the secret you created in this procedure

## Configure an integration for ServiceNow ITSM

Security Hub can create incidents or problems automatically in ServiceNow ITSM.

###### To configure an integration for ServiceNow ITSM

1. Sign in to your AWS account with your credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1](https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1 "https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1").
2. From the navigation pane, choose **Management**, and then choose **Integrations**.
3. Under **ServiceNow ITSM**, choose **Add integration**.
4. For **Details**, enter a name for your integration, and determine whether to enter an optional description for your integration.
5. For **Encryptions** choose how you want to encrypt your integration credentials within Security Hub.
   - **Use AWS owned key** - With this option a Security Hub owned service key will be used to encrypt your integration credential data within Security Hub.
   - **Choose a different KMS key (advanced)** - With this option you choose an AWS KMS key that you have created which you want to be used for encrypting your integration credential data within Security Hub.
     For information about how to create an AWS KMS key, see [Create a AWS KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.
     If you choose to use your own key you must add policy statements to the KMS key that allow Security Hub access to the key.
     See [AWS KMS key policies for Security Hub ticketing integrations](securityhub-v2-integrations-key-policy.md "securityhub-v2-integrations-key-policy.md") for details on the necessary policies.

###### Note

You cannot change these settings once you complete this configuration.
However, If you choose **Customized key**, you can edit your customized key policy at any time. 6. For **Credentials**, enter your ServiceNow ITSM URL, and the ARN of your AWS Secrets Manager secret that was generated in the prerequisites section. 7. For **Tags**, determine whether to create and add an optional tag to your integration. 8. Choose **Add integration**.
After you complete the configuration, you can view your configured integrations in the **Configured integrations** tab.

Once you have configured your integration with ServiceNow you can test the connection to confirm that everything is configured properly in your ServiceNow environment and in Security Hub.
See the [Testing configured ticketing integrations](securityhub-v2-test-ticket-integration.md "securityhub-v2-test-ticket-integration.md") for more details.
