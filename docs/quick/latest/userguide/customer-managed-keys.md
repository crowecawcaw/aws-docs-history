

# Encrypting your AWS Quick data with AWS Key Management Service customer managed keys

AWS Quick enables you to encrypt your AWS Quick data with the keys you have stored in AWS Key Management Service. This provides you with the tools to audit access to data and satisfy regulatory security requirements. If you need to do so, you have the option to immediately lock down access to your data by revoking access to AWS KMS keys. The use of your AWS KMS keys by AWS Quick is logged in AWS CloudTrail. You can use these events to verify which key protects a resource. These events record AWS KMS key use. Administrators and auditors can use these events to trace when and where your AWS KMS keys were used. For application-level activity in AWS Quick, see [Incident response, logging, and monitoring in AWS Quick](incident-response-logging-and-monitoring.md). 

To create customer managed KMS keys, you use AWS Key Management Service (AWS KMS) in the same AWS account and AWS Region as the AWS Quick resource. An AWS Quick administrator can then use a customer managed KMS key to encrypt your AWS Quick data and control access. 

You can create and manage customer managed KMS keys in the AWS Quick console or with the AWS Quick APIs. For more information about creating and managing customer managed KMS keys with the AWS Quick APIs, see [Key management operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/cmk-operations.html).

The following rules apply to using customer managed KMS keys with AWS Quick resources: 
+ AWS Quick doesn't support asymmetric AWS KMS keys.
+ You can have multiple customer managed KMS keys and one default customer managed KMS key per AWS account per AWS Region.
+ By default, AWS Quick resources are encrypted with AWS Quick–native encryption strategies.
+ Data currently encrypted by a customer managed KMS key will stay encrypted by the key.
+ Accounts configured with a customer managed KMS key do not support chat memory. For more information, see [Memory and response personalization](using-quick-chat.md#chat-memory).

**Note**  
If you use AWS Key Management Service with AWS Quick, you are billed for access and maintenance as described in the [AWS Key Management Service Pricing page](https://aws.amazon.com/kms/pricing). In your billing statement, the costs are itemized under AWS KMS and not under AWS Quick.

Where a customer managed KMS key does not apply, AWS Quick protects data with AWS owned or service-managed keys.

Database server certificates that are not managed by AWS are the responsibility of the customer and should be signed by a trusted CA. For more information, see [Network and database configuration requirements](configure-access.md).

Use the following topics to learn more about using customer managed KMS keys with AWS Quick. To learn more about data encryption in AWS Quick, see [Data protection in AWS Quick](sec-data-protection.md).

**Topics**
+ [Customer managed KMS key scope](#customer-managed-keys-scope)
+ [Amazon Q data key](#customer-managed-keys-q-data-key)
+ [Add a customer managed KMS key to your account](#customer-managed-keys-create-key)
+ [Verify the key used by AWS Quick](#customer-managed-keys-verify-key)
+ [Changing the default customer managed KMS key](#customer-managed-keys-change-default-key)
+ [Removing the default customer managed KMS key](#customer-managed-keys-remove-cmks)
+ [Auditing customer managed KMS key usage in CloudTrail](#customer-managed-key-audit)
+ [Revoking access to a customer managed KMS key](#customer-managed-key-revoke-access)
+ [Recovering encrypted AWS Quick data](#customer-managed-key-recovery)

## Customer managed KMS key scope
<a name="customer-managed-keys-scope"></a>

AWS Quick uses resource-specific encryption at rest. Support for a customer managed KMS key, and the way that key is applied, differs by resource type. If a resource type is not listed in the following table, do not assume that a customer managed KMS key applies to it.

AWS Quick applies customer managed KMS keys in two ways:
+ **Account default key.** Participating resource types select the account default key when data is written or when a resource-level key association is created. Changing the default affects future writes or resources that resolve it, but does not automatically re-encrypt existing content. The exact lifecycle is resource-specific.
+ **Amazon Q data key.** Amazon Q data uses a single account-level key that is set the first time Amazon Q data is created in your account and **cannot be changed afterward**. To use a customer managed KMS key for Amazon Q data, register it as your account default key *before* you create any Amazon Q data.

Customer managed KMS key support requires an AWS Quick Enterprise subscription.

A customer managed KMS key must be a symmetric AWS KMS key in the same AWS account and AWS Region as the AWS Quick resource. You can configure one default customer managed KMS key for each AWS Quick account and Region.

Your key policy must allow the AWS Quick service principals that use the key. Your key policy must permit both `quicksight.amazonaws.com` and `qbusiness.amazonaws.com`. This applies when the same key serves as both your default customer managed KMS key and the Amazon Q data key. Omitting `qbusiness.amazonaws.com` can cause knowledge base sync operations to fail.

AWS Quick uses AWS KMS grants to encrypt and decrypt your data with a customer managed KMS key, and creates these grants on your behalf. If a key policy or service control policy restricts `kms:CreateGrant` for the AWS Quick service principals, encryption operations can fail. Retiring a grant removes AWS Quick access to the key for that resource.

Enabling automatic key rotation in AWS KMS rotates the key material without changing the key ARN, so it does not change how AWS Quick uses the key and requires no action in AWS Quick. Rotating to a *different* AWS KMS key is a default-key change; see the following scope table for how each resource type behaves. The Amazon Q data key cannot be moved to a different key.

To see both values for your account, call `DescribeKeyRegistration`. The response returns your registered keys in `KeyRegistration` and your Amazon Q data key in `QDataKey`. The `QDataKey` value is read-only.

Key registration support follows AWS Quick Region availability. Individual AWS Quick features and their customer managed KMS key integrations might have narrower Region or account availability; see the documentation for that feature and use `DescribeKeyRegistration` to inspect your account.

For more information about supported AWS Regions, see [AWS Regions and related information](regions.md).


| AWS Quick resource type | Key used | When it applies | Existing-resource behavior | 
| --- | --- | --- | --- | 
| SPICE dataset | Account default key | A new dataset uses the default key at creation. | To move an existing dataset to a new default key, perform a full refresh. | 
| Report artifact from a dashboard snapshot, scheduled report, export, or dashboard | Account default key | A newly generated artifact uses the current default key. | Existing artifacts remain encrypted with their existing key and are not re-encrypted. | 
| Data-source credentials, OAuth tokens, and OAuth client applications | Account default key | Encrypted at creation with the current default key. | Re-encrypted with the current default key whenever the credential is updated or an OAuth token is refreshed. If no default key is registered, AWS Quick uses a service-managed key. | 
| Flows – definitions, publication data, run/session state, history, and uploaded-file names | Account default key | Participating Flow content uses the current default key when written. | Existing encrypted content remains tied to the key recorded when it was written; changing the default does not automatically re-encrypt it. | 
| Automate – participating group and trigger content; validated inbound-email content, attachments, and email sender, subject, and attachment-name audit fields | Account default key | Applies only to these participating Automate stores where the integration is available. | Existing records retain the key used for encryption. Other Automate-owned persistence, including workflow/deployment/run data, execution artifacts, and credentials, uses service-controlled keys rather than the account default key. | 
| Research – artifacts, documents, reports/exports, and encrypted record fields | Account default key associated at Research creation | A new Research resource associates the current default key when available; otherwise AWS Quick uses service encryption. To use a customer managed KMS key for a Research resource, register it as your default key before creating the resource – a Research resource created without a key association cannot be moved to one later. | Existing Research resources remain associated with their creation-time key when the account default changes. All content in the resource, including new writes, continues to use the creation-time key. | 
| Amazon Q data – knowledge bases, spaces and space uploads, conversations, agents, actions, extensions (including extension access configuration), topics, and Quick Index | Amazon Q data key | Set the first time Amazon Q data is created in the account, from the default key registered at that moment. | Cannot be changed. Not affected when you change or remove the default key. | 

## Amazon Q data key
<a name="customer-managed-keys-q-data-key"></a>

AWS Quick protects Amazon Q data with a single account-level key called the Amazon Q data key. AWS Quick sets this key the first time Amazon Q data is created in your account:
+ If a default customer managed KMS key is registered at that moment, the Amazon Q data key is set to that key and `QDataKey.QDataKeyType` is `CMK`.
+ If no default key is registered, AWS Quick uses an AWS owned key and `QDataKey.QDataKeyType` is `AWS_OWNED`.

**The Amazon Q data key cannot be changed after it is set.** Changing or removing your default customer managed KMS key does not change it, and does not return an account to an AWS owned key. To use a customer managed KMS key for Amazon Q data, register that key as your account default key before you create any Amazon Q data.

To check the current value, call `DescribeKeyRegistration` and read the `QDataKey` field.

**Important**  
If the key referenced by your Amazon Q data key becomes unavailable, Amazon Q data becomes inaccessible and creating new Amazon Q resources fails. A key can become unavailable if it is disabled, if access is denied, or if it is scheduled for deletion. Because the Amazon Q data key cannot be changed, removing the key registration does not resolve this. Registering a different customer managed KMS key also does not resolve this. The only way to restore Amazon Q functionality is to restore the original key: re-enable it, restore access to it, or cancel its pending deletion. If the key has been permanently deleted, Amazon Q data encrypted with it cannot be recovered. To restore Amazon Q functionality, you must unsubscribe from AWS Quick and subscribe again. This permanently deletes all of your AWS Quick data. Before you disable, deny access to, or schedule deletion of any AWS KMS key, call `DescribeKeyRegistration` and confirm the key is not your Amazon Q data key.

## Add a customer managed KMS key to your account
<a name="customer-managed-keys-create-key"></a>

Before you begin, make sure that you have an IAM role that grants the admin user access to the AWS Quick admin key management console. For more information on the required permissions, see [IAM identity-based policies for AWS Quick: using the admin key management console](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html#security_iam_id-based-policy-examples-admin-key-management-console).

You can add keys that already exist in AWS KMS to your AWS Quick account, so that you can encrypt your AWS Quick data.

To learn more about how you can create a key to use in AWS Quick, see the [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

**To add a new customer managed KMS key to your AWS Quick account.**

1. On the AWS Quick start page, choose **Manage AWS Quick**, and then choose **KMS keys**.

1. On the **KMS keys** page, choose **Manage**. The **KMS keys** dashboard opens.

1. On the **KMS Keys** dashboard, choose **Select key**.

1. On the **Select key** pop-up box, choose **Key** to open the list. Then, select the key that you want to add. 

   If your key isn't in the list, you can manually enter the key's ARN.

1. (Optional) Select the **Use as default encryption key for all new data in the current region of this AWS Quick account** to set the selected key as your default key. A badge appears next to the default key to indicate its status.

   When you choose a default key, new data for participating resource types is encrypted with that key. Support and lifecycle differ by resource type; see [Customer managed KMS key scope](#customer-managed-keys-scope).

1. (Optional) Add more keys by repeating the previous steps in this procedure. While you can add as many keys as you want, you can only have one default key at one time.

## Verify the key used by AWS Quick
<a name="customer-managed-keys-verify-key"></a>

When a key is used, an audit log is created in AWS CloudTrail. You can use the log to track the key's usage. If you need to know which key the AWS Quick data is encrypted by, you can find this information in CloudTrail.

To learn more about which data can be managed with the key, see [Encrypting your AWS Quick data with AWS Key Management Service customer managed keys](customer-managed-keys.md).

**Verify the customer managed KMS key that's currently used by a SPICE dataset**

1. Navigate to your CloudTrail log. For more information, see [Logging AWS Quick operations with AWS CloudTrail](monitoring-cloudtrail.md#logging-using-cloudtrail).

1. Locate the most recent grant events for the SPICE dataset, using the following search arguments: 
   + The event name (`eventName`) contains `Grant`.
   + The request parameters `requestParameters` contain the AWS Quick ARN for the dataset.

   ```
   {
   "eventVersion": "1.08",
   "userIdentity": {
   "type": "AWSService",
   "invokedBy": "quicksight.amazonaws.com"
   },
   "eventTime": "2022-10-26T00:11:08Z",
   "eventSource": "kms.amazonaws.com",
   "eventName": "CreateGrant",
   "awsRegion": "us-west-2",
   "sourceIPAddress": "quicksight.amazonaws.com",
   "userAgent": "quicksight.amazonaws.com",
   "requestParameters": {
   "constraints": {
       "encryptionContextSubset": {
           "aws:quicksight:arn": "arn:aws:quicksight:us-west-2:111122223333:{{dataset/12345678-1234-1234-1234-123456789012}}"
       }
   },
   "retiringPrincipal": "quicksight.amazonaws.com",
   "keyId": "arn:aws:kms:us-west-2:111122223333:key/{{87654321-4321-4321-4321-210987654321}}",
   "granteePrincipal": "quicksight.amazonaws.com",
   "operations": [
       "Encrypt",
       "Decrypt",
       "DescribeKey",
       "GenerateDataKey"
   ]
   },
   ....
   }
   ```

1. Depending on the event type, one of the following applies:

   **`CreateGrant`** – You can find the most recently used customer managed KMS key in the key ID (`keyID`) for the last `CreateGrant` event for the SPICE dataset. 

   **`RetireGrant`** – If latest CloudTrail event of the SPICE datasets is `RetireGrant`, there is no key ID and the resource is no longer customer managed KMS key encrypted.

**Verify the customer managed KMS key that's currently used when generating report artifacts**

1. Navigate to your CloudTrail log. For more information, see [Logging AWS Quick operations with AWS CloudTrail](monitoring-cloudtrail.md#logging-using-cloudtrail).

1. Locate the most recent `GenerateDataKey` events for the report execution, using the following search arguments:
   + The event name (`eventName`) contains `GenerateDataKey` or `Decrypt`.
   + The request parameters (`requestParameters`) contain the AWS Quick ARN for the analysis or dashboard the report was generated for.

   ```
   {
       "eventVersion": "1.11",
       "userIdentity": {
           "type": "AWSService",
           "invokedBy": "quicksight.amazonaws.com"
       },
       "eventTime": "2025-07-23T23:33:46Z",
       "eventSource": "kms.amazonaws.com",
       "eventName": "GenerateDataKey",
       "awsRegion": "us-west-2",
       "sourceIPAddress": "quicksight.amazonaws.com",
       "userAgent": "quicksight.amazonaws.com",
       "requestParameters": {
           "keyId": "arn:aws:kms:us-west-2:111122223333:key/{{87654321-4321-4321-4321-210987654321}}",
           "keySpec": "AES_256",
           "encryptionContext": {
               "aws:quicksight:arn": "arn:aws:quicksight:us-west-2:111122223333:{{dashboard/1ca456fe-eb34-4250-805c-b1b9350bd164}}",
               "aws:s3:arn": "arn:aws:s3:::{{amazon-quick-owned-bucket}}"
           }
       },
       ...
   }
   ```

1. `aws:s3:arn` is the AWS Quick owned S3 bucket where your report artifacts are stored.

1. If you no longer see `GenerateDataKey`, then new report executions are no longer customer managed KMS key encrypted. Existing report artifacts will remain encrypted.

**Verify the customer managed KMS key that's currently used for data-source credentials**

1. Navigate to your CloudTrail log. For more information, see [Logging AWS Quick operations with AWS CloudTrail](monitoring-cloudtrail.md#logging-using-cloudtrail).

1. Locate the most recent `Encrypt` events for the data source, using the following search arguments:
   + The event name (`eventName`) is `Encrypt`.
   + The request parameters (`requestParameters`) contain the encryption context `aws:quicksight:arn` with the AWS Quick ARN for the data source.

   ```
   {
       "eventVersion": "1.11",
       "userIdentity": {
           "type": "AWSService",
           "invokedBy": "quicksight.amazonaws.com"
       },
       "eventTime": "2025-07-23T23:33:46Z",
       "eventSource": "kms.amazonaws.com",
       "eventName": "Encrypt",
       "awsRegion": "us-west-2",
       "sourceIPAddress": "quicksight.amazonaws.com",
       "userAgent": "quicksight.amazonaws.com",
       "requestParameters": {
           "keyId": "arn:aws:kms:us-west-2:111122223333:key/{{87654321-4321-4321-4321-210987654321}}",
           "encryptionContext": {
               "aws:quicksight:arn": "arn:aws:quicksight:us-west-2:111122223333:{{datasource/example-data-source-id}}"
           }
       },
       ...
   }
   ```

1. The `keyId` on the most recent `Encrypt` event is the key currently protecting the credential. Credentials are re-encrypted with the current default key whenever the credential is updated or an OAuth token is refreshed, so the most recent event reflects the key in use.

## Changing the default customer managed KMS key
<a name="customer-managed-keys-change-default-key"></a>

You can change the default key to another key that already exists in the **KMS keys** dashboard. When you change the default key, new writes and new resources for participating resource types use the new key. Existing content remains encrypted with the key that was in effect when it was written; how and whether it moves to the new key differs by resource type – for example, a SPICE dataset moves on its next full refresh, data-source credentials move on their next update or token refresh, and report artifacts are never re-encrypted. The Amazon Q data key is not affected. For more information, see [Customer managed KMS key scope](#customer-managed-keys-scope).

To learn more about which data can be managed with the key, see [Encrypting your AWS Quick data with AWS Key Management Service customer managed keys](customer-managed-keys.md).

**To change the default key to an existing key**

1. On the AWS Quick start page, choose **Manage AWS Quick**, and then choose **KMS keys**.

1. Choose **MANAGE** to open the **KMS keys** dashboard.

1. Navigate to the key that you want to set as your new default. Choose **Actions** (three dots) on the row of the key that you want to open the key's menu. 

1. Choose **Set as default**, and then choose **Set**.

The selected key is now your default key.

## Removing the default customer managed KMS key
<a name="customer-managed-keys-remove-cmks"></a>

Removing your default customer managed KMS key ends the use of that key for **new resources or writes that resolve the account default key**. Removing the key does not delete the AWS KMS key, change the key that protects existing resources, change your Amazon Q data key, or remove encryption at rest.

Where no customer managed KMS key applies, AWS Quick continues to protect data with its own encryption. Existing resources remain encrypted with the key they were created with.

**Important**  
Before you remove your default customer managed KMS key, call `DescribeKeyRegistration` and confirm that the key is not your Amazon Q data key. If the key is your Amazon Q data key, removing it from the default registration does not change the Amazon Q data key, but future Amazon Q resource behavior depends on continued access to that key. For more information, see [Amazon Q data key](#customer-managed-keys-q-data-key).

**To remove the default customer managed KMS key**

1. On the AWS Quick start page, choose **Manage AWS Quick**, and then choose **KMS keys**.

1. On the **KMS keys** page, choose **Manage** to open the **KMS keys** dashboard.

1. Choose **Actions** (three dots) on the row of the default key, and then choose **Delete**.

1. In the pop-up box that appears, choose **Remove**.

## Auditing customer managed KMS key usage in CloudTrail
<a name="customer-managed-key-audit"></a>

You can audit your account's customer managed KMS key usage in AWS CloudTrail. To audit your key usage, log in to your AWS account, open CloudTrail, and choose **Event history**.

**Note**  
Amazon Q data key use appears in CloudTrail as a single account-level key rather than as per-resource grants. `DescribeKeyRegistration` is the authoritative source for the current Amazon Q data key value.

## Revoking access to a customer managed KMS key
<a name="customer-managed-key-revoke-access"></a>

You can revoke access to your customer managed KMS keys. When you revoke access to a key that is used to encrypt your AWS Quick data, access to it is denied, and operations that depend on the key can fail until you undo the revoke. The following methods are examples of how you can revoke access: 
+ Turn off the key in AWS KMS.
+ Add a `Deny` policy to your AWS Quick AWS KMS policy in IAM.

**Important**  
Before you revoke access to a AWS KMS key, call `DescribeKeyRegistration` and confirm the key is not your Amazon Q data key. If you revoke access to your Amazon Q data key, Amazon Q data becomes inaccessible and creating new Amazon Q resources fails. This is not reversible by registering a different customer managed KMS key. For more information, see [Amazon Q data key](#customer-managed-keys-q-data-key).

To learn more about which data can be managed with the key, see [Encrypting your AWS Quick data with AWS Key Management Service customer managed keys](customer-managed-keys.md).

Use the following procedure to revoke access to your customer managed KMS keys in AWS KMS.

**To turn off a customer managed KMS key in AWS Key Management Service**

1. Log in to your AWS account, open AWS KMS, and choose **Customer managed keys**.

1. Select the key that you want to turn off.

1. Open the **Key actions** menu and choose **Disable**.

The following is a revocation example that uses a `Deny` policy in AWS Identity and Access Management (IAM) to prevent further use of the customer managed KMS key. Use `"Service": "quicksight.amazonaws.com"` as the principal and the ARN of the key as the resource. Deny the following actions: `"kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:DescribeKey"`.

**Important**  
After you revoke access by using any method, it can take up to 15 minutes for the data to become inaccessible.

## Recovering encrypted AWS Quick data
<a name="customer-managed-key-recovery"></a>

The following procedure applies when access to a AWS KMS key has been revoked (for example, by disabling the key or adding a `Deny` policy), but the key itself still exists in AWS KMS.

**Important**  
If the AWS KMS key has been permanently deleted, data encrypted with it cannot be recovered. AWS KMS enforces a waiting period before key deletion; if the key is still pending deletion, you can cancel the scheduled deletion to restore it. If the permanently deleted key is your Amazon Q data key, Amazon Q functionality can only be restored by unsubscribing from AWS Quick and subscribing again, which permanently deletes all of your AWS Quick data.

**To recover AWS Quick data while its access is revoked**

1. Restore access to the customer managed KMS key. Usually, this is enough to recover the AWS Quick data.

1. Test the AWS Quick data to check if you can see it.

1. (Optional) If a SPICE dataset is not fully recovered even after you restore access to the customer managed KMS key, perform a full refresh on the dataset. Full refresh applies only to SPICE datasets; it is not applicable to other resource types such as conversations, spaces, agents, or actions.

To learn more about which data can be managed with the key, see [Encrypting your AWS Quick data with AWS Key Management Service customer managed keys](customer-managed-keys.md).