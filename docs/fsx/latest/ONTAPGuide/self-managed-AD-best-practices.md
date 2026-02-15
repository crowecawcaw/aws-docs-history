# Best practices for working with Active Directory

Here are some suggestions and guidelines that you should consider when joining Amazon FSx for NetApp ONTAP
SVMs to your self-managed Microsoft Active Directory. Note that these are recommended as best
practices, but not required.

###### Topics

- [Delegating permissions to your Amazon FSx service
  account](#connect_delegate_privileges "#connect_delegate_privileges")
- [Keeping your Active Directory configuration updated with
  Amazon FSx](#keep-ad-config-updated "#keep-ad-config-updated")
- [Using security groups to limit traffic within your
  VPC](#least-privilege-sg-rules "#least-privilege-sg-rules")
- [Creating outbound security group rules for your file system's
  network interface](#sg-rules-fsx-eni "#sg-rules-fsx-eni")
- [Storing Active Directory credentials using AWS Secrets Manager](#bp-store-ad-creds-using-secret-manager "#bp-store-ad-creds-using-secret-manager")

## Delegating permissions to your Amazon FSx service

account

Make sure to configure the service account that you provide to Amazon FSx with the minimum
permissions required. In addition, separate the Organizational Unit (OU) from other domain
controller concerns.

To join Amazon FSx SVMs to your domain, make sure that the service account has delegated
permissions. Members of the **Domain Admins** group have sufficient
permissions to perform this task. However, as a best practice, use a service account that only
has the minimum permissions necessary to do this. The following procedure demonstrates how to
delegate only the permissions necessary to join FSx for ONTAP SVMs to your domain.

Perform this procedure on a machine that's joined to your directory and has the Active
Directory User and Computers MMC snap-in installed.

###### To create a service account for your Microsoft Active Directory domain

1. Make sure that you're logged in as a domain administrator for your Microsoft Active Directory domain.
2. Open the **Active Directory User and Computers** MMC snap-in.
3. In the task pane, expand the domain node.
4. Locate and open the context (right-click) menu for the OU that you want to modify, and
   then choose **Delegate Control**.
5. On the **Delegation of Control Wizard** page,
   choose **Next**.
6. Choose **Add** to add a specific user or a specific group for
   **Selected users and groups**, and then choose
   **Next**.
7. On the **Tasks to Delegate** page, choose **Create a custom task
   to delegate**, and then choose **Next**.
8. Choose **Only the following objects in the folder**, and then choose
   **Computer objects**.
9. Choose **Create selected objects in this folder** and **Delete
   selected objects in this folder**. Then choose **Next**.
10. Under **Show these permissions**, ensure that **General** and
    **Property-specific** are selected.
11. For **Permissions**, choose the following:
    - **Reset Password**
    - **Read and write Account Restrictions**
    - **Validated write to DNS host name**
    - **Validated write to service principal name**
    - **Write msDS-SupportedEncryptionTypes**

12. Choose **Next**, and then choose **Finish**.
13. Close the **Active Directory User and Computers** MMC snap-in.

###### Important

Don't move computer objects that Amazon FSx creates in the OU after your SVMs are created. Doing
so will cause your SVMs to become misconfigured.

## Keeping your Active Directory configuration updated with

Amazon FSx

For uninterrupted availability of your Amazon FSx SVMs, update an SVM's self-managed Active
Directory (AD) configuration when you change your self-managed AD setup.

For example, suppose that your AD uses a time-based password reset policy. In this case, as
soon as the password is reset, make sure to update the service account password with Amazon FSx. To do
this, use the Amazon FSx console, Amazon FSx API, or AWS CLI. Similarly, if the DNS server IP addresses
change for your Active Directory domain, as soon as the change occurs update the DNS server IP
addresses with Amazon FSx.

If there's an issue with the updated self-managed AD configuration, the SVM state switches
to **Misconfigured**. This state shows an error message and a recommended
action beside the SVM description in the console, API, and CLI. If an issue with your SVM's AD
configuration occurs, be sure to take the recommended corrective action for the configuration
properties. If the issue is resolved, verify that your SVM's state changes to
**Created**.

For more information, see [Updating existing SVM Active Directory configurations using the AWS Management Console, AWS CLI, and API](update-svm-ad-config.md "update-svm-ad-config.md") and
[Modify an Active Directory configuration using the ONTAP CLI](manage-svm-ad-config-ontap-cli.md#using-ontap-cli-to-modify-ad "manage-svm-ad-config-ontap-cli.md#using-ontap-cli-to-modify-ad").

## Using security groups to limit traffic within your

VPC

To limit network traffic in your virtual private cloud (VPC), you can implement the
principle of least privilege in your VPC. In other words, you can limit permissions to the
minimum ones necessary. To do this, use security group rules. To learn more, see [Amazon VPC security groups](limit-access-security-groups.md#fsx-vpc-security-groups "limit-access-security-groups.md#fsx-vpc-security-groups").

## Creating outbound security group rules for your file system's

network interface

For greater security, consider configuring a security group with outbound traffic rules.
These rules should allow outbound traffic only to your self-managed AD domains
controllers or within the subnet or security group. Apply this security group to the VPC
associated with your Amazon FSx file system's elastic network interface. To learn more, see
[File System Access Control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").

## Storing Active Directory credentials using AWS Secrets Manager

You can use AWS Secrets Manager to securely store and manage your Microsoft Active Directory domain join service account credentials. This approach eliminates the need to store sensitive credentials in plaintext in application code or configuration files, strengthening your security posture.

You can also configure IAM policies to manage access to your secrets, and set up automatic rotation policies for your passwords.

#### Step 1: Create a KMS key

Create a KMS key to encrypt and decrypt your Active Directory credentials in Secrets Manager.

###### To create a key

###### Note

For **Encryption Key**, create a new key, don't use the AWS default KMS key. Be sure to create the AWS KMS key in the same Region that contains the SVM that you want to join to your Active Directory.

1. Open the AWS KMS console at https://console.aws.amazon.com/kms.
2. Choose **Create key**.
3. For **Key Type**, choose **Symmetric**.
4. For **Key Usage**, choose **Encrypt and decrypt**.
5. For **Advanced options**, do the following:
   1. For **Key material origin**, choose **KMS**.
   2. For **Regionality**, choose **Single-Region key** and choose **Next**.

6. Choose **Next**.
7. For **Alias**, provide a name for the KMS key.
8. (Optional) For **Description**, provide a description of the KMS key.
9. (Optional) For **Tags**, provide a tag for the KMS key and choose **Next**.
10. (Optional) For **Key administrators**, provide the IAM users and roles authorized to manage this key.
11. For **Key deletion**, keep the box selected for **Allow key administrators** to delete this key and choose **Next**.
12. (Optional) For **Key users**, provide the IAM users and roles authorized to use this key in cryptographic operations. Choose **Next**.
13. For **Key policy**, choose **Edit** and include the following to the policy **Statement** to allow Amazon FSx to use the KMS key and choose **Next**. Make sure to replace the `us-west-2` to the AWS Region where the file system is deployed and `123456789012` to your AWS account ID.

```
{
    "Sid": "Allow FSx to use the KMS key",
    "Version": "2012-10-17",
    "Effect": "Allow",
    "Principal": {
        "Service": "fsx.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
    ],
    "Resource": "arn:aws:kms:`us-west-2`:`123456789012`:key/*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "secretsmanager.`us-west-2`.amazonaws.com",
            "aws:SourceAccount": "`123456789012`"
        },
        "ArnLike": {
            "aws:SourceArn": [
                "arn:aws:fsx:`us-west-2`:`123456789012`:file-system/*",
                "arn:aws:fsx:`us-west-2`:`123456789012`:storage-virtual-machine/fs-*/svm-*"
            ]
        }
    }
}
```

14. Choose **Finish**.

###### Note

You can set more granular access control by modifying the `Resource` and `aws:SourceArn` fields to target specific secrets and file systems.

#### Step 2: Create an AWS Secrets Manager secret

###### To create a secret

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. For **Secret type**, choose **Other type of secret**.
4. For **Key/value pairs**, do the following to add your two keys:
   1. For the first key, enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME`.
   2. For the value of the first key, enter only the username (without the domain prefix) of the AD user.
   3. For the second key, enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD`.
   4. For the value of the second key, enter the password that you created for the AD user on your domain.

5. For **Encryption key**, enter the ARN of the KMS key that you created in a previous step and choose **Next**.
6. For **Secret name**, enter a descriptive name that helps you find your secret later.
7. (Optional) For **Description**, enter a description for the secret name.
8. For **Resource permission**, choose **Edit**.

Add the following policy to the permission policy to allow Amazon FSx to use the secret, then choose **Next**. Make sure to replace the `us-west-2` to the AWS Region where the file system is deployed and `123456789012` to your AWS account ID.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "fsx.amazonaws.com"
            },
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret"
            ],
            "Resource": "arn:aws:secretsmanager:`us-west-2`:`123456789012`:secret:*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`123456789012`"
                },
                "ArnLike": {
                    "aws:SourceArn": [
                        "arn:aws:fsx:`us-west-2`:`123456789012`:file-system/*",
                        "arn:aws:fsx:`us-west-2`:`123456789012`:storage-virtual-machine/fs-*/svm-*"
                    ]
                }
            }
        }
    ]
}
```

9. (Optional) You can configure Secrets Manager to rotate your credentials automatically. Choose **Next**.
10. Choose **Finish**.

#### Step 1: Create a KMS key

Create a KMS key to encrypt and decrypt your Active Directory credentials in Secrets Manager.

To create a KMS key, use the AWS CLI command [create-key](../../../cli/latest/reference/kms/create-key.md "../../../cli/latest/reference/kms/create-key.md").

In this command, set the `--policy` parameter to specify the key policy that defines permissions for the KMS key. The policy must include the following:

- The service principal for Amazon FSx, which is `fsx.amazonaws.com`.
- Required KMS actions: `kms:Decrypt` and `kms:DescribeKey`.
- Resource ARN pattern for your AWS Region and account.
- Condition keys that restrict key usage:
  - `kms:ViaService` to ensure requests come through Secrets Manager.
  - `aws:SourceAccount` to limit to your account.
  - `aws:SourceArn` to restrict to specific Amazon FSx file systems.

The following example creates a symmetric encryption KMS key with a policy that allows Amazon FSx to use the key for decryption and key description operations. The command automatically retrieves your AWS account ID and Region, then configures the key policy with these values to ensure proper access controls between Amazon FSx, Secrets Manager, and the KMS key. Make sure your AWS CLI environment is in the same region as the SVM that will join the Active Directory.

```
# Set region and get Account ID
REGION=${AWS_REGION:-$(aws configure get region)}
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

# Create Key
KMS_KEY_ARN=$(aws kms create-key --policy "{
  \"Version\": \"2012-10-17\",
  \"Statement\": [
    {
      \"Sid\": \"Enable IAM User Permissions\",
      \"Effect\": \"Allow\",
      \"Principal\": {
        \"AWS\": \"arn:aws:iam::$ACCOUNT_ID:root\"
      },
      \"Action\": \"kms:*\",
      \"Resource\": \"*\"
    },
    {
      \"Sid\": \"Allow FSx to use the KMS key\",
      \"Effect\": \"Allow\",
      \"Principal\": {
        \"Service\": \"fsx.amazonaws.com\"
      },
      \"Action\": [
        \"kms:Decrypt\",
        \"kms:DescribeKey\"
      ],
      \"Resource\": \"*\",
      \"Condition\": {
        \"StringEquals\": {
          \"kms:ViaService\": \"secretsmanager.$REGION.amazonaws.com\",
          \"aws:SourceAccount\": \"$ACCOUNT_ID\"
        },
        \"ArnLike\": {
          \"aws:SourceArn\": [
            \"arn:aws:fsx:$REGION:$ACCOUNT_ID:file-system/*\",
            \"arn:aws:fsx:$REGION:$ACCOUNT_ID:storage-virtual-machine/fs-*/svm-*\"]
        }
      }
    }
  ]
}" --query 'KeyMetadata.Arn' --output text)

echo "KMS Key ARN: $KMS_KEY_ARN"
```

###### Note

You can set more granular access control by modifying the `Resource` and `aws:SourceArn` fields to target specific secrets and file systems.

#### Step 2: Create an AWS Secrets Manager secret

To create a secret for Amazon FSx to access your Active Directory, use the AWS CLI command [create-secret](../../../cli/latest/reference/secretsmanager/create-secret.md "../../../cli/latest/reference/secretsmanager/create-secret.md") and set the following parameters:

- `--name`: The identifier for your secret.
- `--description`: A description of the secret's purpose.
- `--kms-key-id`: The ARN of the KMS key you created in [Step 1](#create-kms-key-cli "#create-kms-key-cli") for encrypting the secret at rest.
- `--secret-string`: A JSON string containing your AD credentials in the following format:
  - `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME`: Your AD service account username without the domain prefix, such as `svc-fsx`. **Don't** provide the domain prefix, such as `CORP\svc-fsx`.
  - `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD`: Your AD service account password

- `--region`: The AWS Region where your SVM will be created. This defaults to your configured region if `AWS_REGION` is not set.

After creating the secret, attach a resource policy using the [put-resource-policy](../../../cli/latest/reference/logs/put-resource-policy.md "../../../cli/latest/reference/logs/put-resource-policy.md") command, and set the following parameters:

- `--secret-id`: The name or ARN of the secret to attach the policy to. The following example uses `FSxSecret` as the `--secret-id`.
- `--region`: The same AWS Region as your secret.
- `--resource-policy`: A JSON policy document that grants Amazon FSx permission to access the secret. The policy must include the following:
  - The service principal for Amazon FSx, which is `fsx.amazonaws.com`.
  - Required Secrets Manager actions: `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret`.
  - Resource ARN pattern for your AWS Region and account.
  - The following condition keys that restrict access:
    - `aws:SourceAccount` to limit to your account.
    - `aws:SourceArn` to restrict to specific Amazon FSx file systems.

The following example creates a secret with the required format and attaches a resource policy that allows Amazon FSx to use the secret. This example automatically retrieves your AWS account ID and Region, then configures the resource policy with these values to ensure proper access controls between Amazon FSx and the secret.

Make sure to replace the `KMS_KEY_ARN` with the ARN from the key you created in [Step 1](#create-kms-key-cli "#create-kms-key-cli"), `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME`, and `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD` with your Active Directory service account credentials. Additionally, verify that your AWS CLI environment is configured for the same region as the SVM that will join the Active Directory.

```
# Set region and get account ID
REGION=${AWS_REGION:-$(aws configure get region)}
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

# Replace with your KMS key ARN from Step 1
KMS_KEY_ARN="`arn:aws:kms:us-east-2:123456789012:key/1234542f-d114-555b-9ade-fec3c9200d8e`"

# Replace with your Active Directory credentials
AD_USERNAME="`Your_Username`"
AD_PASSWORD="`Your_Password`"

# Create the secret
SECRET_ARN=$(aws secretsmanager create-secret \
  --name "`FSxSecret`" \
  --description "Secret for FSx access" \
  --kms-key-id "$KMS_KEY_ARN" \
  --secret-string "{\"CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME\":\"$AD_USERNAME\",\"CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD\":\"$AD_PASSWORD\"}" \
  --region "$REGION" \
  --query 'ARN' \
  --output text)

echo "Secret created with ARN: $SECRET_ARN"

# Attach the resource policy with proper formatting
aws secretsmanager put-resource-policy \
  --secret-id "`FSxSecret`" \
  --region "$REGION" \
  --resource-policy "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [
      {
        \"Effect\": \"Allow\",
        \"Principal\": {
          \"Service\": \"fsx.amazonaws.com\"
        },
        \"Action\": [
          \"secretsmanager:GetSecretValue\",
          \"secretsmanager:DescribeSecret\"
        ],
        \"Resource\": \"$SECRET_ARN\",
        \"Condition\": {
          \"StringEquals\": {
            \"aws:SourceAccount\": \"$ACCOUNT_ID\"
          },
          \"ArnLike\": {
            \"aws:SourceArn\": [
              \"arn:aws:fsx:$REGION:$ACCOUNT_ID:file-system/*\",
              \"arn:aws:fsx:$REGION:$ACCOUNT_ID:storage-virtual-machine/fs-*/svm-*\"]
          }
        }
      }
    ]
  }"

echo "Resource policy attached successfully"
```

###### Note

You can set more granular access control by modifying the `Resource` and `aws:SourceArn` fields to target specific secrets and file systems.
