AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Encrypt Amazon EBS volumes that AWS Cloud9 uses

This topic shows how you can encrypt Amazon EBS
volumes
tfor
EC2 instances used by AWS Cloud9 development environments.

Amazon EBS encryption encrypts the following data:

- Data at rest in the volume
- All data that moves between the volume and the instance
- All snapshots that are created from the volume
- All volumes that are created from those snapshots
  You have two encryption options for Amazon EBS volumes that are used by
  AWS Cloud9 EC2 development environments:

- Encryption by default – You can configure your
  AWS account to enforce the encryption of the new EBS volumes and snapshot copies that
  you create. Encryption by default is enabled at the level of an AWS Region. So, you
  can't enable it for individual volumes or snapshots in that Region. In addition, Amazon EBS
  encrypts the volume that's created when you launch an instance. So, you must enable this
  setting before you create an EC2 environment. For more information, see [Encryption by
  default](../../../ebs/latest/userguide/ebs-encryption.md#encryption-by-default "../../../ebs/latest/userguide/ebs-encryption.md#encryption-by-default") in the _Amazon EC2 User Guide_.
- Encryption of an existing Amazon EBS volume used by an
  EC2 environment – You can encrypt specific Amazon EBS volumes that are already
  created for EC2 instances. This option involves using the AWS Key Management Service (AWS KMS) to manage
  access to the encrypted volumes. For the relevant procedure, see [Encrypt an existing Amazon EBS volume that AWS Cloud9
  uses](#encrypting-existing-volume "#encrypting-existing-volume").

###### Important

If your AWS Cloud9 IDE uses Amazon EBS volumes that are encrypted by default, the AWS Identity and Access Management
service-linked role for AWS Cloud9 requires access to the AWS KMS key for these EBS volumes.
If access isn't provided, the AWS Cloud9 IDE might fail to launch and debugging might be
difficult.

To provide access, add the service-linked role for AWS Cloud9,
`AWSServiceRoleForAWSCloud9`, to the KMS key that's used by your Amazon EBS
volumes. For more information about this task, see [Create an AWS Cloud9 IDE that uses Amazon EBS volumes with default encryption](../../../prescriptive-guidance/latest/patterns/create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption.md "../../../prescriptive-guidance/latest/patterns/create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption.md") in
_AWS Prescriptive Guidance Patterns_.

## Encrypt an existing Amazon EBS volume that AWS Cloud9

uses

Encrypting an existing Amazon EBS volume involves using AWS KMS to create a KMS key. After
you create a snapshot of the volume to replace, you use the KMS key to encrypt a copy of
the snapshot.

Next, you create an encrypted volume with that snapshot. Then, you replace the
unencrypted volume by detaching it from the EC2 instance and attaching the encrypted volume.

Finally, you must update the key policy for the customer managed key to enable access for the
AWS Cloud9 service role.

###### Note

The following procedure focuses on using a customer managed key to encrypt a volume. You can
also use an AWS managed key for an AWS service in your account. The alias for Amazon EBS is
`aws/ebs`. If you choose this default option for encryption, skip step 1
where you create a customer managed key. Also, skip step 8 where you update the key policy. This is
because you can't change the key policy for an AWS managed key.

###### To encrypt an existing Amazon EBS volume

1.  In the AWS KMS console, create a symmetric KMS key. For more information, see [Creating
    symmetric KMS key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.
2.  In the Amazon EC2 console, stop the Amazon EBS-backed instance used by the environment. You
    can [stop the instance using the console or
    the command line](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md").
3.  In the navigation pane of the Amazon EC2 console, choose **Snapshots**
    [to create a
    snapshot of the existing volume](../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md#ebs-create-snapshot "../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md#ebs-create-snapshot") that you want to encrypt.
4.  In the navigation pane of the Amazon EC2 console, choose **Snapshots**
    [to copy the snapshot](../../../AWSEC2/latest/UserGuide/ebs-copy-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-copy-snapshot.md"). In the
    **Copy snapshot** dialog box, do the following to enable
    encryption:

        * Choose **Encrypt this snapshot**.
        * For **Master Key**, select the KMS key that you created
         earlier. (If you're using an AWS managed key, keep the **(default)
         aws/ebs** setting.)

5.  [Create a new volume from the encrypted snapshot](../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md#ebs-create-volume-from-snapshot "../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md#ebs-create-volume-from-snapshot").

###### Note

New Amazon EBS volumes that are created from encrypted snapshots are automatically
encrypted. 6. [Detach the old Amazon EBS
volume](../../../ebs/latest/userguide/ebs-detaching-volume.md "../../../ebs/latest/userguide/ebs-detaching-volume.md") from the Amazon EC2 instance. 7. [Attach the new encrypted
volume](../../../ebs/latest/userguide/ebs-attaching-volume.md "../../../ebs/latest/userguide/ebs-attaching-volume.md") to the Amazon EC2 instance. 8. Update the key policy for the KMS key [using the
AWS Management Console default view, AWS Management Console policy view, or AWS KMS API](../../../kms/latest/developerguide/key-policy-modifying.md#key-policy-modifying-how-to "../../../kms/latest/developerguide/key-policy-modifying.md#key-policy-modifying-how-to"). Add the following
key policy statements to allow the AWS Cloud9 service,
`AWSServiceRoleForAWSCloud9`, to access the KMS key.

###### Note

If you're using an AWS managed key, skip this step.

```
{
    "Sid": "Allow use of the key",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:{Partition}:iam::{AccountId}:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9"
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*"
   },
   {
    "Sid": "Allow attachment of persistent resources",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:{Partition}:iam::{AccountId}:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9"
    },
    "Action": [
        "kms:CreateGrant",
        "kms:ListGrants",
        "kms:RevokeGrant"
    ],
    "Resource": "*",
    "Condition": {
        "Bool": {
            "kms:GrantIsForAWSResource": "true"
        }
    }
}
```

9. Restart the Amazon EC2
   instance. For more information about restarting an Amazon EC2 instance, see [Stop and start your instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md").
