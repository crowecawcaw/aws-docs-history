# Implementing customer managed KMS keys in AWS IAM Identity Center

Customer managed keys are AWS Key Management Service keys that you create, own, and manage. To implement a customer managed KMS key for encryption at rest in AWS IAM Identity Center, follow these steps:

###### Important

Some AWS managed applications cannot be used with AWS IAM Identity Center configured with a customer managed KMS key. See [AWS managed applications
that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md "awsapps-that-work-with-identity-center.md").

1. [Step 1: Identify use cases for your organization](#identify-use-cases "#identify-use-cases") - To define correct permissions for use of the KMS key you need to identify the relevant use cases across your organization. The KMS key permissions consist of KMS key policy statements and identity-based policies that work together to allow appropriate IAM principals to use the KMS key for their specific use cases.
2. [Step 2: Prepare KMS key policy statements](#choose-kms-key-policy-statements "#choose-kms-key-policy-statements") - Choose pertinent KMS key policy statement templates based on the use cases identified in Step 1, and fill in required identifiers and IAM principal names. Start with the baseline KMS key policy statements, and if your security policies require it, refine them as described in Advanced KMS key policy statements.
3. [Step 3: Create a customer managed KMS key](#create-customer-managed-kms-key "#create-customer-managed-kms-key") - Create a KMS key in AWS KMS that meets the IAM Identity Center requirements, and add the KMS key policy statements prepared in Step 2 to the KMS key policy.
4. [Step 4: Configure IAM policies for cross-account use of the KMS key](#configure-iam-policies-kms-key "#configure-iam-policies-kms-key") - Choose pertinent IAM policy statement templates based on the use cases identified in Step 1, and prepare them for use by filling in the key ARN. Then, allow the IAM principals for each specific use case to use the KMS key across accounts by adding the prepared IAM policy statements to the principals' IAM policies.
5. [Step 5: Configure the KMS key in IAM Identity Center](#configure-kms-key-in-iam-identity-center "#configure-kms-key-in-iam-identity-center") - Enable the customer managed KMS key in your IAM Identity Center instance to use it for encryption at rest.

###### Important

Before proceeding with this step, thoroughly validate all KMS key permissions configured in the previous steps. Once completed, IAM Identity Center will begin using the KMS key for encryption at rest.

## Step 1: Identify use cases for your organization

Before creating and configuring your customer managed KMS key, identify your
use cases and prepare the required KMS key permissions. Refer to [AWS KMS Developer Guide](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") for more information on the KMS key policy.

IAM principals that call the IAM Identity Center service APIs require permissions. For example, a delegated administrator can be authorized to use these APIs through a permission set policy. When IAM Identity Center is configured with a customer managed key, IAM principals must also have permissions to use the KMS API through the IAM Identity Center service APIs. You define these KMS API permissions in two places: the KMS key policy and in the IAM policies associated with the IAM principals.

The KMS key permissions consist of:

1. KMS key policy statements that you specify on the KMS key during its creation in [Step 3: Create a customer managed KMS key](#create-customer-managed-kms-key "#create-customer-managed-kms-key").
2. IAM policy statements for IAM principals that you specify in [Step 4: Configure IAM policies for cross-account use of the KMS key](#configure-iam-policies-kms-key "#configure-iam-policies-kms-key") after you create the KMS key.

The following table specifies the relevant use cases and IAM principals that need permissions to use your KMS key.

| Use case                                                                                                                                                                                           | IAM principals that need permissions to use the KMS key                                                                                                                                                                                                                                                          | Required/Optional |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Use of AWS IAM Identity Center                                                                                                                                                                     | • Administrators of AWS IAM Identity Center<br>• IAM Identity Center service and the associated Identity Store service                                                                                                                                                                                           | Required          |
| Use of AWS managed applications with IAM Identity Center                                                                                                                                           | • Administrators of AWS managed applications<br>• AWS managed applications<br>• [Service roles](../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-role") that AWS managed applications assume to call IAM Identity Center service APIs | Optional          |
| Use of AWS Control Tower on the AWS IAM Identity Center instance it enabled                                                                                                                        | • AWS Control Tower administrators                                                                                                                                                                                                                                                                               | Optional          |
| SSO to Amazon EC2 Windows instances with AWS IAM Identity Center                                                                                                                                   | • IAM principals authorized to perform SSO to Amazon EC2 Windows instances                                                                                                                                                                                                                                       | Optional          |
| Any other use case that makes calls to IAM Identity Center service APIs with IAM principals, such as customer managed applications, permission set provisioning workflows, or AWS Lambda functions | • IAM principals used by these workflows to call IAM Identity Center service APIs                                                                                                                                                                                                                                | Optional          |

###### Note

Multiple IAM principals listed in the table require AWS KMS API permissions. However, to protect your user and group data in IAM Identity Center, only IAM Identity Center and Identity Store services directly call the AWS KMS API.

## Step 2: Prepare KMS key policy statements

After identifying the use cases relevant to your organization, you can prepare the corresponding KMS key policy statements.

1. Choose the KMS key policy statements that match the use cases for your organization. Begin with the baseline policy templates. If you need more specific policies based on your security requirements, you can modify the policy statements using the examples in [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md"). For guidance on this decision, see [Considerations for choosing baseline vs. advanced KMS key policy statements](considerations-for-customer-managed-kms-keys-advanced.md#kms-policy-considerations-advanced-vs-baseline "considerations-for-customer-managed-kms-keys-advanced.md#kms-policy-considerations-advanced-vs-baseline"). In addition, each baseline
   section in [Baseline KMS key and IAM policy statements](baseline-KMS-key-policy.md "baseline-KMS-key-policy.md") includes relevant considerations.
2. Copy the relevant policies to an editor and insert the required identifiers and IAM principal names in the KMS key policy statements. For help finding the values of the referenced identifiers, see [Find the required identifiers](#insert-the-required-identifiers "#insert-the-required-identifiers").

Following are baseline policy templates for each use case. Only the first set of permissions for AWS IAM Identity Center is required to use a KMS key. We recommend that you review the applicable subsections for additional use case-specific information.

- [Baseline KMS key policy statements for use of IAM Identity Center (required)](baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-iam-identity-center-mandatory "baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-iam-identity-center-mandatory")
- [Baseline KMS key and IAM policy statements for use of AWS managed applications](baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-aws-managed-applications "baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-aws-managed-applications")
- [Baseline KMS key statement for use of AWS Control Tower](baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-specific-use-cases "baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-specific-use-cases")
- [Baseline KMS key and IAM policy statements for use of IAM Identity Center to Amazon Elastic Compute Cloud Windows instances](baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-sso-to-amazon-ec2-windows-instances "baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-sso-to-amazon-ec2-windows-instances")
- [Baseline KMS key and IAM policy statements for use of custom workflows with IAM Identity Center](baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-custom-workflows-with-iam-identity-center "baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-custom-workflows-with-iam-identity-center")

###### Important

Exercise caution when modifying KMS key policies for keys already in use by IAM Identity Center. While IAM Identity Center validates encryption and decryption permissions when you initially configure a KMS key, it cannot verify subsequent policy changes. Inadvertently removing necessary permissions could disrupt your IAM Identity Center's normal operation. For guidance troubleshooting common errors related to customer managed keys in IAM Identity Center, refer to [Troubleshoot customer managed keys in AWS IAM Identity Center](cmk-related-errors.md "cmk-related-errors.md").

###### Note

IAM Identity Center and its associated Identity Store require service-level permissions to use your customer managed KMS key. This requirement extends to AWS managed applications that call IAM Identity Center service APIs using service credentials. For other use cases where IAM Identity Center service APIs are called with [forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md"), only the initiating IAM principal (such as an administrator) needs KMS key permissions. Notably, end users using the AWS access portal and AWS managed applications don't need direct KMS key permissions, as they are granted through the respective services.

## Step 3: Create a customer managed KMS key

You can create a customer managed key using the AWS Management Console or the AWS KMS APIs. While creating the key, add the KMS key policy statements you prepared in Step 2 into the KMS key policy. For detailed instructions, including guidance on the default KMS key policy, see the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

The key must meet the following requirements:

- The KMS key must be in the same AWS Region as the IAM Identity Center instance
- You can choose either a multi-Region or a single-Region key. To remain forward-compatible with your future use cases across multiple AWS Regions, we recommend choosing a multi-Region key
- The KMS key must be a symmetric key configured for "encrypt and decrypt" usage
- The KMS key must be in the same AWS Organizations management account as the organization instance of IAM Identity Center

## Step 4: Configure IAM policies for cross-account use of the KMS key

Any IAM principal that uses the IAM Identity Center service APIs from another AWS account, such as IAM Identity Center delegated administrators, also needs an IAM policy statement that allows use of the KMS key through these APIs.

For each use case identified in step 1:

1. Locate the pertinent IAM policy statement templates in Baseline KMS key and IAM policy statements.
2. Copy the templates to an editor and fill in the key ARN, which is now available following the creation of the KMS key in step 3. For help finding the key ARN value, see [Find the required identifiers](#insert-the-required-identifiers "#insert-the-required-identifiers").
3. In the AWS Management Console, locate the IAM policy of the IAM principal that is associated with the use case. The location of this policy varies depending on the use case and how access is granted.
   - For access granted directly in IAM, you can locate IAM principals, such as IAM roles in the IAM console.
   - For access granted through IAM Identity Center, you can locate the pertinent permission set in the IAM Identity Center console.

4. Add the use case-specific IAM policy statements to the IAM role and save the change.

###### Note

The IAM policies described here are identity-based policies. While such policies can be attached to IAM users, groups, and roles, we recommend the use of IAM roles when possible. See the IAM user guide for more information about IAM roles versus IAM users.

**Additional configuration in some AWS managed applications**

Some AWS managed applications require you to configure a service role to allow the applications to use the IAM Identity Center service APIs. If your organization uses AWS managed applications with IAM Identity Center, complete the following steps for each deployed application:

1. See the application's user guide to confirm whether the permissions have been updated to include KMS key-related permissions for use of the application with IAM Identity Center.
2. If so, update the permissions as instructed in the application's user guide to avoid disruption to the application's operations.

###### Note

If you're unsure whether an AWS managed application uses these permissions, we recommend that you check the user guides of all deployed AWS managed applications. You only need to perform this configuration once for each application that requires the configuration.

## Step 5: Configure the KMS key in IAM Identity Center

###### Important

Before proceeding with this step:

- Verify that your AWS managed applications are compatible with customer managed KMS keys. For a list of compatible applications, see [AWS managed applications that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md "awsapps-that-work-with-identity-center.md"). If you have incompatible applications, do not proceed.
- Configure the necessary permissions for use of the KMS key. Without proper permissions, this step may fail or disrupt IAM Identity Center administration, the use of AWS managed applications, and other use cases that require KMS key permissions. For more information, see [Step 1: Identify use cases for your organization](#identify-use-cases "#identify-use-cases").
- Ensure that permissions for AWS managed applications and customer managed applications that call IAM Identity Center service APIs with IAM roles also allow the use of the KMS key via IAM Identity Center service APIs. Some AWS managed applications require you to configure permissions, such as a service role, for the use of these APIs. Refer to the User Guide of each deployed AWS managed application to confirm whether you need to add specific KMS key permissions.

### Specify a KMS key when enabling new organization instance of IAM Identity Center

When enabling a new organization instance of IAM Identity Center, you can specify a customer managed KMS key during setup. This ensures the instance uses your key for encryption at rest from the start. Before you start, refer to [Considerations for customer managed KMS keys and advanced KMS key policies](considerations-for-customer-managed-kms-keys-advanced.md "considerations-for-customer-managed-kms-keys-advanced.md").

1. On the **Enable IAM Identity Center** page, expand the **Encryption at rest** section.
2. Choose **Manage Encryption**.
3. Choose **Customer managed key**.
4. For **KMS key**, do one of the following:
   1. Choose **Select from your KMS keys** and select the key you created from the dropdown list.
   2. Choose **Enter KMS key ARN** and enter the full ARN of your key.

5. Choose **Save**.
6. Choose **Enable** to complete the setup.

For more information, see [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md").

### Change the key configuration for an existing organization instance of IAM Identity Center

You can change your customer managed KMS key to another key or switch to an AWS owned key at any time.

Console
**To change your KMS key configuration**

1. Open the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Additional settings** tab.
4. Choose **Manage encryption**.
5. Choose one of the following:
   1. **Customer managed key** - Select a different customer managed key from the dropdown or enter a new key ARN.
   2. **AWS owned key** - Switch to the default encryption option.

6. Choose **Save**.

AWS CLI
**To change an existing organization instance of IAM Identity Center to use KMS customer managed key**

```
aws sso-admin update-instance \
    --instance-arn arn:aws:sso:::instance/ssoins-1234567890abcdef \
    --encryption-configuration \
        KeyType=CUSTOMER_MANAGED_KEY,KmsKeyArn=arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab

```

**To change an existing organization instance of IAM Identity Center to use AWS owned key**

```
aws sso-admin update-instance \
    --instance-arn arn:aws:sso:::instance/ssoins-1234567890abcdef \
    --encryption-configuration KeyType=AWS_OWNED_KMS_KEY
```

**Customer managed key considerations**

- Updating the KMS key configuring for IAM Identity Center operation has no effect on active user sessions in your IAM Identity Center. You can continue using the AWS access portal, the IAM Identity Center console, and IAM Identity Center service APIs during this process.
- When switching to a new KMS key, IAM Identity Center validates that it can use the key successfully for encryption and decryption. If you made a mistake during the setup of the key policy or IAM policy, the console will show an explanatory error message, and the previous KMS key will remain in use.
- The default annual KMS key rotation will take place automatically. You can refer to the [AWS KMS Developer Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") for information on topics such as [key rotation](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md"), [monitoring AWS KMS keys](../../../kms/latest/developerguide/monitoring-overview.md "../../../kms/latest/developerguide/monitoring-overview.md") and [controlling access to key deletion](../../../kms/latest/developerguide/deleting-keys-adding-permission.md "../../../kms/latest/developerguide/deleting-keys-adding-permission.md").

###### Important

If the customer managed KMS key in use by your IAM Identity Center instance is deleted, disabled, or inaccessible due to an incorrect KMS key policy, your workforce users and IAM Identity Center administrators will not be able to use IAM Identity Center. The loss of access can be temporary (a key policy can be corrected) or permanent (a deleted key cannot be restored) depending on the circumstances. We recommend you
[restrict access](../../../kms/latest/developerguide/deleting-keys-adding-permission.md "../../../kms/latest/developerguide/deleting-keys-adding-permission.md") to critical operations, such as deleting or disabling the KMS key. Also, we recommend that your organization set up
[AWS break-glass access procedures](../../../wellarchitected/latest/devops-guidance/ag.sad.md "../../../wellarchitected/latest/devops-guidance/ag.sad.md") to ensure your privileged users can access AWS in the unlikely event that IAM Identity Center is inaccessible.

### Find the required identifiers

When configuring permissions for your customer managed KMS key, you'll need specific AWS
resource identifiers to complete the key policy and IAM policy statement templates. Insert
the required identifiers (for example, organization ID) and IAM principal names in the KMS
key policy statements.

Below is a guide to locating these identifiers in the AWS Management Console.

**IAM Identity Center Amazon Resource Name (ARN) and Identity Store ARN**

An IAM Identity Center instance is an AWS resource with its own unique ARN such as
arn:aws:sso:::instance/ssoins-1234567890abcdef. The ARN follows the pattern documented in
the IAM Identity Center resource types section of the Service Authorization Reference.

Every IAM Identity Center instance has an associated Identity Store that stores the
user and group identities. An Identity Store has a unique identifier called Identity Store
ID (for example, d-123456789a). The ARN follows the pattern documented in the Identity Store
resource types section of the [Service Authorization Reference](../../../service-authorization/latest/reference/list_awsiamidentitycenterdirectory.md "../../../service-authorization/latest/reference/list_awsiamidentitycenterdirectory.md").

You can find both the ARN and the Identity Store ID values on the Settings page of your
IAM Identity Center. The Identity store ID is in the Identity source tab.

**AWS Organizations ID**

If you want to specify an organization ID (for example, o-exampleorg1) in your key policy you can
find its value in the Settings page of your IAM Identity Center and Organizations
consoles. The ARN follows the pattern documented in the Organizations resource types
section of the Service Authorization Reference.

**KMS key ARN**

You can find the ARN of a KMS key in the AWS KMS console. Choose Customer managed keys on
the left, click the key whose ARN you want to look up, and you'll see it in the General
configuration section. The ARN follows the pattern documented in the AWS KMS resource
types section of the Service Authorization Reference.

See the AWS Key Management Service Developer Guide for more information about Key policies
in AWS KMS and troubleshooting AWS KMS permissions. For more information about IAM
policies and their JSON representation see the IAM User Guide.
