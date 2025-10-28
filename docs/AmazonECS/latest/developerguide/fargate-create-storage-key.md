# Create an encryption key for Fargate

ephemeral storage for Amazon ECS

Create a customer managed key to encrypt data stored on Fargate ephemeral storage.

###### Note

Fargate ephemeral storage encryption with customer managed keys isn't available for Windows task
clusters.

Fargate ephemeral storage encryption with customer managed keys isn't available on
`platformVersions` earlier than `1.4.0`.

Fargate reserves space on an ephemeral storage that's only used by Fargate, and you're not billed
for the space. Allocation might differ from non-customer managed key tasks, but the total space remains
the same. You can view this change in tools like `df`.

Multi-Region keys are not supported for Fargate ephemeral
storage.

KMS key aliases are not supported for Fargate ephemeral storage.

To create a customer managed key (CMK) to encrypt ephemeral storage for Fargate in AWS KMS, follow these
steps.

1.  Navigate to the [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2.  Follow the instructions for [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the [AWS Key Management Service Developer
    Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").
3.  When creating your AWS KMS key, make sure to provide Fargate service relevant AWS KMS operation
    permissions in the key policies. The following API operations must be permitted in the policy to
    use your customer managed key with your Amazon ECS cluster resources.

        * `kms:GenerateDataKeyWithoutPlainText` ‐ Call
         `GenerateDataKeyWithoutPlainText` to generate an encrypted data key from the
         provided AWS KMS key.
        * `kms:CreateGrant` ‐ Adds a grant to a customer managed key. Grants
         control access to a specified AWS KMS key, which allows access to grant operations that Amazon ECS
         Fargate requires. For more information about [Using Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md"), see the [AWS Key Management Service Developer
         Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md"). This allows Amazon ECS Fargate to do the following:




        	+ Call `Decrypt` to AWS KMS to get the encryption key to decrypt the
        	 ephemeral storage data.
        	+ Set up a retiring principal to allow the service to
        	 `RetireGrant`.
        * `kms:DescribeKey` ‐ Provides the customer managed key details to allow
         Amazon ECS to validate the key if it's symmetric and enabled.

    The following example shows a AWS KMS key policy that you would apply to the target key for
    encryption. To use the example policy statements, replace the `user input
 placeholders` with your own information. As always, only configure the permissions
    that you need, but you'll need to provide AWS KMS with permissions to at least one user to avoid errors.

```
{
      "Sid": "Allow generate data key access for Fargate tasks.",
      "Effect": "Allow",
      "Principal": { "Service":"fargate.amazonaws.com" },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:ecs:clusterAccount": [
            "`customerAccountId`"
          ],
          "kms:EncryptionContext:aws:ecs:clusterName": [
             "`clusterName`"
          ]
        }
      },
      "Resource": "*"
    },
    {
      "Sid": "Allow grant creation permission for Fargate tasks.",
      "Effect": "Allow",
      "Principal": { "Service":"fargate.amazonaws.com" },
      "Action": [
        "kms:CreateGrant"
      ],
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:ecs:clusterAccount": [
            "`customerAccountId`"
          ],
          "kms:EncryptionContext:aws:ecs:clusterName": [
             "`clusterName`"
          ]
        },
       "ForAllValues:StringEquals": {
          "kms:GrantOperations": [
             "Decrypt"
          ]
       }
      },
      "Resource": "*"
    },
    {
      "Sid": "Allow describe key permission for cluster operator - CreateCluster and UpdateCluster.",
      "Effect": "Allow",
      "Principal": { "AWS":"arn:aws:iam::`customerAccountId`:role/`customer-chosen-role`" },
      "Action": [
        "kms:DescribeKey"
      ],
      "Resource": "*"
    }
```

Fargate tasks use the `aws:ecs:clusterAccount` and
`aws:ecs:clusterName` encryption context keys for cryptographic
operations with the key. Customers should add these permissions to restrict access
to a specific account and/or cluster. Use the cluster name and not the ARN when
you specify the cluster.

For more information, see [Encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") in the
[AWS KMS Developer
Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

When creating or updating a cluster, you have the option to use the condition key
`fargateEphemeralStorageKmsKeyId`. This condition key allows customers to have more
granular control of the IAM policies. Updates to the `fargateEphemeralStorageKmsKeyId`
configuration only take effect on new service deployments.

The following is an example of allowing customers to grant permissions to only a specific set of
approved AWS KMS keys.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:CreateCluster",
 "ecs:UpdateCluster"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ecs:fargate-ephemeral-storage-kms-key": "arn:aws:kms:`us-west-2`:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
 }
 }
 }
 ]
}`

```

Next is an example for denying attempts to remove AWS KMS keys that are already associated with a
cluster.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": [
 "ecs:CreateCluster",
 "ecs:UpdateCluster"
 ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "ecs:fargate-ephemeral-storage-kms-key": "true"
 }
 }
 }
}`

```

Customers can see if their unmanaged tasks or service tasks are encrypted using the key by using
the AWS CLI `describe-tasks`, `describe-cluster`, or
`describe-services` commands.

For more information, see [Condition keys for AWS KMS](../../../kms/latest/developerguide/policy-conditions.md "../../../kms/latest/developerguide/policy-conditions.md") in the
[AWS KMS Developer
Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

AWS Management Console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. Choose **Clusters** in the left navigation and either
   **Create cluster** in the top right, or choose an existing
   cluster. For an existing cluster, choose **Update cluster** in the top
   right.
3. Under the **Encryption** section of the workflow, you'll have the
   option to select your AWS KMS key under **Managed storage** and
   **Fargate ephemeral storage**. You can also choose to
   **Create an AWS KMS key** from here.
4. Choose **Create** once you finish creating your new cluster or
   **Update**, if you were updating an existing one.

AWS CLI
The following is an example of creating a cluster and configuring your Fargate ephemeral
storage using the AWS CLI (replace the `red` values with your
own):

```
aws ecs create-cluster --cluster `clusterName` \
--configuration '{"managedStorageConfiguration":{"fargateEphemeralStorageKmsKeyId":"arn:aws:kms:`us-west-2`:`012345678901`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"}}'
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:`us-west-2`:`012345678901`:cluster/`clusterName`",
        "clusterName": "`clusterName`",
        "configuration": {
            "managedStorageConfiguration": {
                "fargateEphemeralStorageKmsKeyId": "arn:aws:kms:`us-west-2`:`012345678901`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
            }
        },
        "status": "ACTIVE",
        "registeredContainerInstancesCount": 0,
        "runningTasksCount": 0,
        "pendingTasksCount": 0,
        "activeServicesCount": 0,
        "statistics": [],
        "tags": [],
        "settings": [],
        "capacityProviders": [],
        "defaultCapacityProviderStrategy": []
    },
    "clusterCount": 5
}
```

AWS CloudFormation
The following is an example template of creating a cluster and configuring your Fargate
ephemeral storage using the AWS CloudFormation (replace the `red` values with your
own):

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyCluster:
    Type: AWS::ECS::Cluster
    Properties:
      ClusterName: "`clusterName`"
      Configuration:
        ManagedStorageConfiguration:
          FargateEphemeralStorageKmsKeyId: "arn:aws:kms:`us-west-2`:`012345678901`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"

```
