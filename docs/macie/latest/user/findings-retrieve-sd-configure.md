# Configuring Macie to retrieve sensitive data

samples

You can optionally configure and use Amazon Macie to retrieve and reveal samples of sensitive
data that Macie reports in individual findings. The samples can help you verify the nature of the
sensitive data that Macie found. They can also help you tailor your investigation of an affected
Amazon Simple Storage Service (Amazon S3) object and bucket. You can retrieve and reveal sensitive data samples in all the
AWS Regions where Macie is currently available except the Asia Pacific (Osaka) and
Israel (Tel Aviv) Regions.

When you retrieve and reveal sensitive data samples for a finding, Macie uses data in the
corresponding sensitive data discovery result to locate occurrences of sensitive data in the
affected S3 object. Macie then extracts samples of those occurrences from the affected object.
Macie encrypts the extracted data with an AWS Key Management Service (AWS KMS) key that you specify, temporarily
stores the encrypted data in a cache, and returns the data in your results for the finding. Soon
after extraction and encryption, Macie permanently deletes the data from the cache unless
additional retention is temporarily required to resolve an operational issue.

To retrieve and reveal sensitive data samples for findings, you first need to configure and
enable settings for your Macie account. You also need to configure supporting resources and
permissions for your account. The topics in this section guide you through the process of
configuring Macie to retrieve and reveal sensitive data samples, and managing the status of the
configuration for your account.

###### Topics

- [Before you
  begin](#findings-retrieve-sd-configure-prereqs "#findings-retrieve-sd-configure-prereqs")
- [Configuring and enabling
  Macie settings](#findings-retrieve-sd-configure-enable "#findings-retrieve-sd-configure-enable")
- [Disabling Macie
  settings](#findings-retrieve-sd-configure-manage "#findings-retrieve-sd-configure-manage")

###### Tip

For recommendations and examples of policies that you might use to control access to this
functionality, see the following blog post on the _AWS Security
Blog_: [How to use
Amazon Macie to preview sensitive data in S3 buckets](https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-preview-sensitive-data-in-s3-buckets/ "https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-preview-sensitive-data-in-s3-buckets/").

## Before you begin

Before you configure Amazon Macie to retrieve and reveal sensitive data samples for findings,
complete the following tasks to ensure that you have the resources and permissions that you
need.

###### Tasks

- [Step 1: Configure a repository
  for sensitive data discovery results](#findings-retrieve-sd-configure-sddr "#findings-retrieve-sd-configure-sddr")
- [Step 2: Determine how to
  access affected S3 objects](#findings-retrieve-sd-configure-s3access "#findings-retrieve-sd-configure-s3access")
- [Step 3: Configure an
  AWS KMS key](#findings-retrieve-sd-configure-key "#findings-retrieve-sd-configure-key")
- [Step 4: Verify your
  permissions](#findings-retrieve-sd-configure-permissions "#findings-retrieve-sd-configure-permissions")

These tasks are optional if you've already configured Macie to retrieve and reveal sensitive
data samples and only want to change your configuration settings.

### Step 1: Configure a repository for

sensitive data discovery results

When you retrieve and reveal sensitive data samples for a finding, Macie uses data in the
corresponding sensitive data discovery result to locate occurrences of sensitive data in the affected S3 object.
Therefore, it's important to verify that you configured a repository for your sensitive data discovery results.
Otherwise, Macie won't be able to locate sensitive data samples that you want to retrieve and
reveal.

To determine whether you've configured this repository for your account, you can use the
Amazon Macie console: choose **Discovery results** (under
**Settings**) in the navigation pane. To do this programmatically, use the
[GetClassificationExportConfiguration](../APIReference/classification-export-configuration.md "../APIReference/classification-export-configuration.md") operation of the Amazon Macie API. To learn more
about sensitive data discovery results and how to configure this repository, see [Storing and retaining
sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md").

### Step 2: Determine how to access

affected S3 objects

To access affected S3 objects and retrieve sensitive data samples from them, you have two
options. You can configure Macie to use your AWS Identity and Access Management (IAM) user credentials. Or you can
configure Macie to assume an IAM role that delegates access to Macie. You can use either
configuration with any type of Macie account—the delegated Macie administrator account for an
organization, a Macie member account in an organization, or a standalone Macie account. Before
you configure the settings in Macie, determine which access method you want to use. For details
about the options and requirements for each method, see [Configuration options for
retrieving samples](findings-retrieve-sd-options.md "findings-retrieve-sd-options.md").

If you plan to use an IAM role, create and configure the role before you configure the
settings in Macie. Also ensure that the trust and permissions policies for the role meet all
requirements for Macie to assume the role. If your account is part of an organization that
centrally manages multiple Macie accounts, work with your Macie administrator to first determine whether
and how to configure the role for your account.

### Step 3: Configure an AWS KMS key

When you retrieve and reveal sensitive data samples for a finding, Macie encrypts the
samples with an AWS Key Management Service (AWS KMS) key that you specify. Therefore, you need to determine which
AWS KMS key you want to use to encrypt the samples. The key can be an existing KMS key from
your own account, or an existing KMS key that another account owns. If you want to use a key
that another account owns, obtain the Amazon Resource Name (ARN) of the key. You'll need to
specify this ARN when you enter the configuration settings in Macie.

The KMS key must be a customer managed, symmetric encryption key. It must also be a
single-Region key that's enabled in the same AWS Region as your Macie account. The KMS key
can be in an external key store. However, the key might then be slower and less reliable than a
key that’s managed entirely within AWS KMS. If latency or an availability issue prevents Macie
from encrypting sensitive data samples that you want to retrieve and reveal, an error occurs and
Macie doesn't return any samples for the finding.

In addition, the key policy for the key must allow the appropriate principals (IAM roles,
IAM users, or AWS accounts) to perform the following actions:

- `kms:Decrypt`
- `kms:DescribeKey`
- `kms:GenerateDataKey`

###### Important

As an additional layer of access control, we recommend that you create a dedicated
KMS key for encryption of sensitive data samples that are retrieved, and restrict use of the
key to only those principals who must be allowed to retrieve and reveal sensitive data samples.
If a user isn't allowed to perform the preceding actions for the key, Macie rejects their
request to retrieve and reveal sensitive data samples. Macie doesn't return any samples for the
finding.

For information about creating and configuring KMS keys, see [Create a KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_. For information about using key policies to manage
access to KMS keys, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

### Step 4: Verify your

permissions

Before you configure the settings in Macie, also verify that you have the permissions that
you need. To verify your permissions, use AWS Identity and Access Management (IAM) to review the IAM policies that
are attached to your IAM identity. Then compare the information in those policies to the
following list of actions that you must be allowed to perform.

Amazon Macie

For Macie, verify that you're allowed to perform the following actions:

- `macie2:GetMacieSession`
- `macie2:UpdateRevealConfiguration`

The first action allows you to access your Macie account. The second action allows you
to change your configuration settings for retrieving and revealing sensitive data samples.
This includes enabling and disabling the configuration for your account.

Optionally verify that you're also allowed to perform the
`macie2:GetRevealConfiguration` action. This action allows you to retrieve your
current configuration settings and the current status of the configuration for your
account.

AWS KMS

If you plan to use the Amazon Macie console to enter the configuration settings, also
verify that you're allowed to perform the following AWS Key Management Service (AWS KMS) actions:

- `kms:DescribeKey`
- `kms:ListAliases`

These actions allow you to retrieve information about the AWS KMS keys for your
account. You can then choose one of these keys when you enter the settings.

IAM

If you plan to configure Macie to assume an IAM role to retrieve and reveal sensitive
data samples, also verify that you're allowed to perform the following IAM action:
`iam:PassRole`. This action allows you to pass the role to Macie, which in turn
allows Macie to assume the role. When you enter the configuration settings for your account,
Macie can also then verify that the role exists in your account and is configured
correctly.

If you're not allowed to perform the requisite actions, ask your AWS administrator for
assistance.

## Configuring and enabling Macie

settings

After you verify that you have the resources and permissions that you need, you can
configure the settings in Amazon Macie and enable the configuration for your account.

If your account is part of an organization that centrally manages multiple Macie accounts,
note the following before you configure or subsequently change the settings for your
account:

- If you have a member account, work with your Macie administrator to determine whether and how to
  configure the settings for your account. Your Macie administrator can help you determine the correct
  configuration settings for your account.
- If you have a Macie administrator account and you change your settings for accessing affected S3
  objects, your changes might affect other accounts and resources for your organization. This
  depends on whether Macie is currently configured to assume an AWS Identity and Access Management (IAM) role to
  retrieve sensitive data samples. If it is and you reconfigure Macie to use IAM user
  credentials, Macie permanently deletes existing settings for the IAM role—the name of
  the role and the external ID for your configuration. If your organization subsequently chooses
  to use IAM roles again, you'll need to specify a new external ID in the trust policy for the
  role in each applicable member account.

For details about the configuration options and requirements for either type of account, see [Configuration options for
retrieving samples](findings-retrieve-sd-options.md "findings-retrieve-sd-options.md").

To configure the settings in Macie and enable the configuration for your account, you can
use the Amazon Macie console or the Amazon Macie API.

Console
Follow these steps to configure and enable the settings by using the Amazon Macie
console.

###### To configure and enable Macie settings

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to configure and enable Macie to retrieve and reveal
   sensitive data samples.
3. In the navigation pane, under **Settings**, choose **Reveal
   samples**.
4. In the **Settings** section, choose **Edit**.
5. For **Status**, choose **Enable**.
6. Under **Access**, specify the access method and settings that you want
   to use when retrieving sensitive data samples from affected S3 objects:
   - To use an IAM role that delegates access to Macie, choose **Assume an IAM
     role**. If you choose this option, Macie retrieves the samples by assuming the
     IAM role that you created and configured in your AWS account. In the **Role
     name** box, enter the name of the role.
   - To use the credentials of the IAM user who requests the samples, choose
     **Use IAM user credentials**. If you choose this option, each user of
     your account uses their individual IAM identity to retrieve the samples.

7. Under **Encryption**, specify the AWS KMS key that you want to use
   to encrypt sensitive data samples that are retrieved:
   - To use a KMS key from your own account, choose **Select a key from your
     account**. Then, in the **AWS KMS key** list, choose the key
     to use. The list displays existing, symmetric encryption KMS keys for your
     account.
   - To use a KMS key that another account owns, choose **Enter the ARN of a key
     from another account**. Then, in the **AWS KMS key ARN**
     box, enter the Amazon Resource Name (ARN) of the key to use—for example,
     `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.

8. When you finish entering the settings, choose **Save**.

Macie tests the settings and verifies that they're correct. If you configured Macie to
assume an IAM role, Macie also verifies that the role exists in your account and the trust
and permissions policies are configured correctly. If there's an issue, Macie displays a
message that describes the issue.

To address an issue with the AWS KMS key, refer to the requirements in the [preceding topic](#findings-retrieve-sd-configure-key "#findings-retrieve-sd-configure-key") and specify a KMS key
that meets the requirements. To address an issue with the IAM role, start by verifying that
you entered the correct role name. If the name is correct, ensure that the role’s policies
meet all requirements for Macie to assume the role. For these details, see [Configuring
an IAM role to access affected S3 objects](findings-retrieve-sd-options.md#findings-retrieve-sd-options-s3access-role-configuration "findings-retrieve-sd-options.md#findings-retrieve-sd-options-s3access-role-configuration"). After you address
any issues, you can save and enable the settings.

###### Note

If you're the Macie administrator for an organization and you configured Macie to assume an
IAM role, Macie generates and displays an external ID after you save the settings for your
account. Note this ID. The trust policy for the IAM role in each of your applicable member
accounts must specify this ID. Otherwise, you won't be able to retrieve sensitive data
samples from S3 objects that the accounts own.

API
To configure and enable the settings programmatically, use the [UpdateRevealConfiguration](../APIReference/reveal-configuration.md "../APIReference/reveal-configuration.md") operation of the Amazon Macie API. In your request, specify
the appropriate values for the supported parameters:

- For the `retrievalConfiguration` parameters, specify the access method and
  settings that you want to use when retrieving sensitive data samples from affected S3
  objects:
  - To assume an IAM role that delegates access to Macie, specify
    `ASSUME_ROLE` for the `retrievalMode` parameter and specify the
    name of the role for the `roleName` parameter. If you specify these settings,
    Macie retrieves the samples by assuming the IAM role that you created and configured in
    your AWS account.
  - To use the credentials of the IAM user who requests the samples, specify
    `CALLER_CREDENTIALS` for the `retrievalMode` parameter. If you
    specify this setting, each user of your account uses their individual IAM identity to
    retrieve the samples.

###### Important

If you don't specify values for these parameters, Macie sets the access method
(`retrievalMode`) to `CALLER_CREDENTIALS`. If Macie is currently
configured to use an IAM role to retrieve the samples, Macie also permanently deletes the
current role name and external ID for your configuration. To keep these settings for an
existing configuration, include the `retrievalConfiguration` parameters in your
request and specify your current settings for those parameters. To retrieve your current
settings, use the [GetRevealConfiguration](../APIReference/reveal-configuration.md "../APIReference/reveal-configuration.md")
operation or, if you're using the AWS Command Line Interface (AWS CLI), run the [get-reveal-configuration](../../../cli/latest/reference/macie2/get-reveal-configuration.md "../../../cli/latest/reference/macie2/get-reveal-configuration.md") command.

- For the `kmsKeyId` parameter, specify the AWS KMS key that you want to
  use to encrypt sensitive data samples that are retrieved:
  - To use a KMS key from your own account, specify the Amazon Resource Name (ARN), ID,
    or alias for the key. If you specify an alias, include the `alias/`
    prefix—for example, `alias/ExampleAlias`.
  - To use a KMS key that another account owns, specify the ARN of the key—for
    example, `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`. Or specify the ARN of the alias for the
    key—for example, `arn:aws:kms:us-east-1:111122223333:alias/ExampleAlias`.

- For the `status` parameter, specify `ENABLED` to enable the
  configuration for your Macie account.

In your request, also ensure that you specify the AWS Region in which you want to
enable and use the configuration.

To configure and enable the settings by using the AWS CLI, run the [update-reveal-configuration](../../../cli/latest/reference/macie2/update-reveal-configuration.md "../../../cli/latest/reference/macie2/update-reveal-configuration.md") command and specify the appropriate values for the
supported parameters. For example, if you're using the AWS CLI on Microsoft Windows, run the
following command:

```
`C:\>` `aws macie2 update-reveal-configuration ^
--region `us-east-1` ^
--configuration={\"kmsKeyId\":\"`arn:aws:kms:us-east-1:111122223333:alias/ExampleAlias`\",\"status\":\"ENABLED\"} ^
--retrievalConfiguration={\"retrievalMode\":\"`ASSUME_ROLE`\",\"roleName\":\"`MacieRevealRole`\"}`
```

Where:

- `us-east-1` is the Region in which to enable and use the
  configuration. In this example, the US East (N. Virginia) Region.
- `arn:aws:kms:us-east-1:111122223333:alias/ExampleAlias` is the ARN of the alias for the
  AWS KMS key to use. In this example, the key is owned by another account.
- `ENABLED` is the status of the configuration.
- `ASSUME_ROLE` is the access method to use. In this example,
  assume the specified IAM role.
- `MacieRevealRole` is the name of the IAM role for Macie to
  assume when retrieving sensitive data samples.

The preceding example uses the caret (^) line-continuation character to improve
readability.

When you submit your request, Macie tests the settings. If you configured Macie to assume
an IAM role, Macie also verifies that the role exists in your account and the trust and
permissions policies are configured correctly. If there's an issue, your request fails and
Macie returns a message that describes the issue. To address an issue with the AWS KMS key,
refer to the requirements in the [preceding
topic](#findings-retrieve-sd-configure-key "#findings-retrieve-sd-configure-key") and specify a KMS key that meets the requirements. To address an issue with
the IAM role, start by verifying that you specified the correct role name. If the name is
correct, ensure that the role’s policies meet all requirements for Macie to assume the role.
For these details, see [Configuring
an IAM role to access affected S3 objects](findings-retrieve-sd-options.md#findings-retrieve-sd-options-s3access-role-configuration "findings-retrieve-sd-options.md#findings-retrieve-sd-options-s3access-role-configuration"). After you address
the issue, submit your request again.

If your request succeeds, Macie enables the configuration for your account in the
specified Region and you receive output similar to the following.

```
`{
 "configuration": {
 "kmsKeyId": "arn:aws:kms:us-east-1:111122223333:alias/ExampleAlias",
 "status": "ENABLED"
 },
 "retrievalConfiguration": {
 "externalId": "o2vee30hs31642lexample",
 "retrievalMode": "ASSUME_ROLE",
 "roleName": "MacieRevealRole"
 }
}`
```

Where `kmsKeyId` specifies the AWS KMS key to use to encrypt sensitive data
samples that are retrieved, and `status` is the status of the configuration for
your Macie account. The `retrievalConfiguration` values specify the access method
and settings to use when retrieving the samples.

###### Note

If you're the Macie administrator for an organization and you configured Macie to assume an
IAM role, note the external ID (`externalId`) in the response. The trust policy
for the IAM role in each of your applicable member accounts must specify this ID.
Otherwise, you won't be able to retrieve sensitive data samples from affected S3 objects that
the accounts own.

To subsequently check the settings or status of the configuration for your account, use
the [GetRevealConfiguration](../APIReference/reveal-configuration.md "../APIReference/reveal-configuration.md") operation or, for the AWS CLI, run the [get-reveal-configuration](../../../cli/latest/reference/macie2/get-reveal-configuration.md "../../../cli/latest/reference/macie2/get-reveal-configuration.md") command.

## Disabling Macie settings

You can disable the configuration settings for your Amazon Macie account at any time. If you
disable the configuration, Macie retains the setting that specifies which AWS KMS key to use
to encrypt sensitive data samples that are retrieved. Macie permanently deletes the Amazon S3 access
settings for the configuration.

###### Warning

When you disable the configuration settings for your Macie account, you also permanently
delete current settings that specify how to access affected S3 objects. If Macie is currently
configured to access affected objects by assuming an AWS Identity and Access Management (IAM) role, this includes: the
name of the role, and the external ID that Macie generated for the configuration. These settings
can't be recovered after they're deleted.

To disable the configuration settings for your Macie account, you can use the Amazon Macie
console or the Amazon Macie API.

Console
Follow these steps to disable the configuration settings for your account by using the
Amazon Macie console.

###### To disable Macie settings

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to disable the configuration settings for your Macie
   account.
3. In the navigation pane, under **Settings**, choose **Reveal
   samples**.
4. In the **Settings** section, choose **Edit**.
5. For **Status**, choose **Disable**.
6. Choose **Save**.

API
To disable the configuration settings programmatically, use the [UpdateRevealConfiguration](../APIReference/reveal-configuration.md "../APIReference/reveal-configuration.md") operation of the Amazon Macie API. In your request, ensure
that you specify the AWS Region in which you want to disable the configuration. For the
`status` parameter, specify `DISABLED`.

To disable the configuration settings by using the AWS Command Line Interface (AWS CLI), run the [update-reveal-configuration](../../../cli/latest/reference/macie2/update-reveal-configuration.md "../../../cli/latest/reference/macie2/update-reveal-configuration.md") command. Use the `region` parameter to
specify the Region in which you want to disable the configuration. For the `status`
parameter, specify `DISABLED`. For example, if you're using the AWS CLI on Microsoft
Windows, run the following command:

```
`C:\>` `aws macie2 update-reveal-configuration --region `us-east-1` --configuration={\"status\":\"DISABLED\"}`
```

Where:

- `us-east-1` is the Region in which to disable the
  configuration. In this example, the US East (N. Virginia) Region.
- `DISABLED` is the new status of the configuration.

If your request succeeds, Macie disables the configuration for your account in the
specified Region and you receive output similar to the following.

```
`{
 "configuration": {
 "status": "DISABLED"
 }
}`
```

Where `status` is the new status of the configuration for your Macie
account.

If Macie was configured to assume an IAM role to retrieve sensitive data samples, you can
optionally delete the role and the role's permissions policy. Macie doesn't delete these
resources when you disable the configuration settings for your account. In addition, Macie
doesn't use these resources to perform any other tasks for your account. To delete the role and
its permissions policy, you can use the IAM console or the IAM API. For more information, see [Deleting roles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the
_AWS Identity and Access Management User Guide_.
