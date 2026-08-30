NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Amazon EBS configuration

Amazon Elastic Block Store (Amazon EBS) is the default target storage type for AWS Transform MGN. This guide covers
how to configure Amazon EBS volume types, encryption settings, and per-server disk type
customization.

## Replication template settings

These settings are configured in the replication template and apply to all source servers
by default.

### Amazon EBS volume type

Choose the default **Amazon EBS volume type**
to be used by the replication servers for large disks.

Each disk has minimum and maximum sizes and varying performance metrics and
pricing. Learn more about Amazon EBS volume types in [this Amazon EBS article.](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md")

The best practice is to not change the default Amazon EBS volume type, unless there
is a business need for doing so.

###### Note

This option only affects disks over 500 GiB (by default, smaller disks
always use Magnetic HDD volumes).

The default **Lower cost, Throughput Optimized HDD
(st1)** option uses slower, less expensive disks.

You might want to use this option if:

- You want to keep costs low
- Your large disks do not change frequently
- You are not concerned with how long the initial sync process will take

The **Faster, General Purpose SSD (gp3)** option
uses faster, but more expensive disks.

You might want to use this option if:

- Your source server has disks with a high write rate or if you want
  faster performance in general
- You want to speed up the initial sync process
- You are willing to pay more for speed

###### Note

You can customize the Amazon EBS volume type used by each disk within each
source server in that source server's settings. [Learn more about changing individual source server volume types.](#staging-disk "#staging-disk")

### Amazon EBS encryption

Choose whether to use the default or custom Amazon **EBS
encryption**. This option will encrypt your replicated data at rest
on the Staging Area Subnet disks and the replicated disks.

- Default – The default Amazon EBS encryption Volume Encryption Key will be
  used (which can be an Amazon EBS-managed key or a CMK).
- Custom – You will need to enter a custom customer-managed key (CMK) in
  the regular key ID format.

If you select the **Custom** option, the
**EBS encryption key** box appears. Enter
the ARN or key ID of a customer-managed CMK from your account or another
AWS account. Enter the encryption key (such as a cross-account KMS key) in the
regular key ID format (KMS key example: 123abcd-12ab-34cd-56ef-1234567890ab).

To create a new AWS Key Management Service key, choose **Create an AWS KMS
key**. You will be redirected to the Key Management Service (KMS)
Console where you can create a new key to use.

Learn more about Amazon EBS Volume Encryption in [this Amazon EBS article](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md").

###### Important

Reversing the encryption option after data replication has started will
cause data replication to start from the beginning.

#### Using an AWS KMS Customer Managed Key (CMK) for encryption

If you decide to use a Customer Managed Key (CMK), or if your default
Amazon EBS encryption key is a CMK, you will need to add additional permissions
to the key to allow AWS Transform MGN to use it.

To modify the existing key policy using the AWS Management Console
_policy view_.

1. Navigate to the AWS KMS Console and select the AWS KMS key you plan to
   use with AWS MGN.
2. Scroll to **Key policy** and choose
   **Switch to policy view**.
3. Choose **Edit** and add the following
   JSON statements to the **Statement**
   field.

```

    {
      "Sid": "Allow AWS Services permission to describe a customer managed key for encryption purposes",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::$ACCOUNT_ID:root"
      },
      "Action": [
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:CallerAccount": [
            "$ACCOUNT_ID"
          ]
        },
        "Bool": {
          "aws:ViaAWSService": "true"
        }
      }
    },
    {
      "Sid": "Allow AWS MGN permissions to use a customer managed key for EBS encryption",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::$ACCOUNT_ID:root"
      },
      "Action": [
        "kms:CreateGrant"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:CallerAccount": [
            "$ACCOUNT_ID"
          ],
          "kms:GranteePrincipal": [
            "arn:aws:iam::$ACCOUNT_ID:role/aws-service-role/mgn.amazonaws.com/AWSServiceRoleForApplicationMigrationService"
          ]
        },
        "ForAllValues:StringEquals": {
          "kms:GrantOperations": [
            "CreateGrant",
            "DescribeKey",
            "Encrypt",
            "Decrypt",
            "GenerateDataKey",
            "GenerateDataKeyWithoutPlaintext"
          ]
        },
        "Bool": {
          "aws:ViaAWSService": "true"
        }
      }
    },
    {
      "Sid": "Allow EC2 to use this key on behalf of the current AWS Transform MGN user, during target launches",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::$ACCOUNT_ID:root",
          "arn:aws:iam::$ACCOUNT_ID:role/aws-service-role/mgn.amazonaws.com/AWSServiceRoleForApplicationMigrationService"
        ]
      },
      "Action": [
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:CallerAccount": [
            "$ACCOUNT_ID"
          ],
          "kms:ViaService": "ec2.$REGION.amazonaws.com"
        }
      }
    }

```

###### Important

    * Replace `$ACCOUNT_ID` with the
     AWS account ID you are migrating into.
    * Replace `$REGION` with the AWS Region you
     are migrating into.
    * The last statement can be made stricter by ensuring
     the principal refers to users who are going to perform
     [StartTest](../APIReference/API_StartTest.md "../APIReference/API_StartTest.md") or [StartCutover](../APIReference/API_StartCutover.md "../APIReference/API_StartCutover.md") API calls

4. Choose **Save changes**.

###### Note

If you are using a Customer Managed Key (CMK) from another account,
you need to take an additional step from within that account to allow
the service to use the CMK.

From the account in which you want to stage MGN replication servers,
create a grant that delegates the relevant permissions to the
appropriate service-linked role. The Grantee Principal element of the
grant is the ARN of the appropriate service-linked role. The key-id is
the ARN of the key.

The following is an example [create-grant](../../../cli/latest/reference/kms/create-grant.md "../../../cli/latest/reference/kms/create-grant.md") CLI command that gives the service-linked role
named **AWSServiceRoleForApplicationMigrationService** in account
111122223333 permissions to use the customer-managed key in account 444455556666.

aws kms create-grant \

--region us-west-2 \

--key-id
arn:aws:kms:us-west-2:444455556666:key/1a2b3c4d-5e6f-1a2b-3c4d-5e6f1a2b3c4d
\

--grantee-principal
arn:aws:iam::111122223333:role/aws-service-role/mgn.amazonaws.com/AWSServiceRoleForApplicationMigrationService
\

--operations "Encrypt" "Decrypt" "ReEncryptFrom" "ReEncryptTo"
"GenerateDataKey" "GenerateDataKeyWithoutPlaintext" "DescribeKey"
"CreateGrant"

For this command to succeed, the user making the request must have
permissions for the CreateGrant action.

## Server-level settings

These settings can be customized per source server or group of source servers.

### Change staging disk type

You can change the Amazon EBS volume disk type for each disk or for a group of disks.

To change the Amazon EBS volume disk type, select the circle to the left of each disk name and
choose **Change staging disk type**.

On the **Change staging disk type** dialog, select the type
of Amazon EBS volume to use for the disk or group of disks.

Select the **AUTO** option if you want AWS Transform MGN to
automatically select the most cost-effective Amazon EBS volume disk type for each disk based on the
disk size and type based on the option you defined in the **Replication
settings** (either the default **Lower cost, Throughput Optimized
HDD (st1)** option or the **Faster, General Purpose SSD
(gp3)** option).

AWS Transform MGN uses a single replication server per 15 source disks. Selecting the **AUTO** option ensures that the fewest number of replication servers
are used, resulting in increased cost savings.

###### Note

AWS Transform MGN always uses Amazon EBS magnetic volumes for disks that are under 500 GiB in size
when the **AUTO** option is selected.

If you do not want AWS Transform MGN to automatically select a disk, you can select a disk
manually. Select the disk type from the **EBS volume type** menu.

###### Note

When replicating into an AZ, ensure that the AZ supports the staging disk type chosen.

For certain disks, you can configure the amount of IOPS to be allocated per GB of disk
space under **IOPS**. You can allocate up to 50 IOPS per GB.
64,000 IOPS are available for Nitro-based instances. Other instances are guaranteed up to
32,000 IOPS. The maximum IOPS per instance is 80,000.

Choose **Change** to confirm the change.

For **General Purpose SSD (gp3)** disks, you can also
set the **Throughput**. General Purpose SSD (gp3) volumes have
a baseline performance of 125 MiB/s. You can provision additional throughput of 0.25 MiB/s per
provisioned IOPS up to a maximum of 1,000 MiB/s (at 4,000 IOPS or higher).

Choose **Change** to confirm the change.
