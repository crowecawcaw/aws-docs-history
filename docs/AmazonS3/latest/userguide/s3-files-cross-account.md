# Tutorial: Mount an S3 file system across accounts

You can access an S3 file system from compute resources in a different AWS account
than the file system owner account. This is called cross-account access. With cross-account
access, teams in different accounts can share the same file system without duplicating
data.

Cross-account access requires network connectivity on port 2049, DNS resolution of the
file system mount target, and S3 Files permissions that allow access from the remote
account.

In this tutorial, you configure cross-account access from an Amazon EC2 instance using the
AWS Management Console. Account A owns the S3 file system, and Account B owns the
EC2 instance that connects to it.

## Prerequisites

Before you begin, make sure that you have the following:

- An S3 file system with mount targets in Account A. For more
  information, see [Getting started with S3
  Files](s3-files-getting-started.md "s3-files-getting-started.md").
- An EC2 instance running in Account B with [amazon-efs-utils](https://github.com/aws/efs-utils "https://github.com/aws/efs-utils") v3.0.0 or
  later.
- An [IAM role for attaching
  your file system to AWS compute resources](s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role "s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role") attached to your EC2
  instance.
- A [file system
  policy](s3-files-file-system-policies-creating.md "s3-files-file-system-policies-creating.md") that grants Account B permissions for
  `s3files:ClientMount` and
  `s3files:ClientWrite`.
- Non-overlapping VPC CIDRs in Account A and Account B.
- Both accounts meet all S3 Files prerequisites. For more information, see
  [S3 Files prerequisites](s3-files-prereq-policies.md "s3-files-prereq-policies.md").

### Example values used in this tutorial

This tutorial uses the following example values. Replace them with your own
values.

| Item                             | Value                                                     |
| -------------------------------- | --------------------------------------------------------- |
| Account A (S3 Files account)     | `111111111111`                                            |
| Account B (EC2 instance account) | `222222222222`                                            |
| S3 file system ID                | `fs-0123456abcdef0189`                                    |
| Region                           | `us-east-1`                                               |
| S3 Files DNS name                | ``{az_id}`.fs-0123456abcdef0189.s3files.us-east-1.on.aws` |
| EC2 instance role (Account B)    | `ec2-instance-role`                                       |

## Step 1: Record file system network details

In Account A, record the following network details from your file system.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **General purpose buckets**, then choose
   the bucket linked to your S3 file system.
3. Choose the **File systems** tab, choose your file
   system, then choose the **Mount targets**
   tab.
4. Verify that mount targets exist in each Availability Zone you plan to connect
   from.
5. Record the following values for use in later steps:

   - VPC ID of the file system
   - AZ IDs (for example, `use1-az1`,
     `use1-az2`)
   - IPv4 address of each mount target (mapped to each AZ ID)
   - Security group ID of the mount targets

## Step 2: Create a VPC peering connection

###### CIDR ranges must not overlap

VPC peering requires that your CIDR ranges do not overlap. Verify this before
proceeding.

1. In both accounts, verify that the VPC has the following DNS settings enabled.
   In the VPC console, choose your VPC, then choose **Edit VPC
   settings**:

   - **DNS resolution (enableDnsSupport):**
     Enabled
   - **DNS hostnames (enableDnsHostnames):**
     Enabled

2. In Account B, open the VPC console, choose **Peering
   Connections**, then choose **Create peering
   connection**. Enter the following values:

   - **VPC ID (Requester):** VPC of the EC2
     instance (Account B)
   - **Account:** Another Account, then enter
     `111111111111`
   - **Region:**
     `us-east-1`
   - **VPC ID (Accepter):** VPC of the S3 file
     system (Account A)

3. In Account A, open the VPC console, choose **Peering
   Connections**, find the pending request, then choose **Actions**, **Accept
   request**. Verify that the status changes to **Active**.

## Step 3: Add routes

**In Account B (EC2 instance account):**

1. Open the VPC console, choose **Route Tables**,
   and select the route table for the EC2 instance's subnet.
2. Choose **Edit routes**, then choose **Add route**:

   - **Destination:** CIDR of the S3 Files VPC
     in Account A
   - **Target:** Select **Peering Connection**, then select the peering connection
     you created in Step 2

**In Account A (S3 Files account):**

1. Open the VPC console, choose **Route Tables**,
   and select the route table for the S3 Files VPC.
2. Choose **Edit routes**, then choose **Add route**:

   - **Destination:** CIDR of the EC2 instance
     VPC in Account B
   - **Target:** Select **Peering Connection**, then select the peering connection
     you created in Step 2

## Step 4: Configure security groups

The mount target security group in Account A must allow inbound NFS traffic from the
EC2 instance in Account B. The EC2 instance security group in Account B must allow
outbound NFS traffic to the mount target.

1. In the VPC console, choose **Security Groups**,
   then select the mount target security group you noted in Step 1.
2. Choose **Edit inbound rules** and add the
   following rule:

   - **Type:** NFS
   - **Port:** 2049
   - **Source:** Choose **Custom**, then enter the EC2 security group ID from
     Account B

3. Verify that the EC2 instance security group in Account B allows outbound TCP
   on port 2049.

| Security Group           | Rule Type | Protocol | Port | Source/Destination                      |
| ------------------------ | --------- | -------- | ---- | --------------------------------------- |
| EC2 instance (Account B) | Outbound  | TCP      | 2049 | Mount target security group (Account A) |
| Mount target (Account A) | Inbound   | TCP      | 2049 | EC2 instance security group (Account B) |

## Step 5: Add a file system policy

In Account A, add a file system policy that grants the Account B role permission to
mount. S3 Files evaluates this policy on every mount request. The mount fails without it,
regardless of network or DNS configuration.

1. Open the Amazon S3 console, choose your bucket, then choose the **File systems** tab.
2. Select your file system, then choose **Edit file system
   policy**.
3. Add a policy that grants the Account B role permission to mount. The following
   example policy grants `s3files:ClientMount` and
   `s3files:ClientWrite` to the EC2 instance role in
   Account B:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCrossAccountMount",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::222222222222:role/ec2-instance-role" },
            "Action": [
                "s3files:ClientMount",
                "s3files:ClientWrite"
            ],
            "Resource": "arn:aws:s3files:us-east-1:111111111111:file-system/fs-0123456abcdef0189"
        }
    ]
}
```

## Step 6: Create Route 53 hosted zones

In Account B, create private hosted zones so the EC2 instance can resolve the file
system DNS names. S3 Files uses DNS names in the following format to route mount requests
to the correct Availability Zone:

```
{az_id}.{fs_id}.s3files.{region}.on.aws
```

Create one private hosted zone for each AZ ID that has a mount target. For each
AZ ID:

1. Open the Route 53 console, choose **Hosted
   Zones**, then choose **Create hosted
   zone**. Enter the following values:

   - **Domain name:**
     ``{az_id}`.fs-0123456abcdef0189.s3files.us-east-1.on.aws`
   - **Type:** Private hosted zone
   - **Region:**
     `us-east-1`
   - **VPC ID:** VPC of the EC2 instance in
     Account B

2. Choose **Create hosted zone**.
3. Choose **Create record** and enter the following
   values:

   - **Record name:** (leave blank)
   - **Record type:** A
   - **Value:** IPv4 address of the mount
     target for that AZ ID (from Step 1)

4. Choose **Create records**.
5. Repeat for all AZ IDs that you plan to connect from.

**Example:**

| Hosted Zone Domain Name                                  | A Record Value               |
| -------------------------------------------------------- | ---------------------------- |
| `use1-az1.fs-0123456abcdef0189.s3files.us-east-1.on.aws` | Mount target IP for use1-az1 |
| `use1-az2.fs-0123456abcdef0189.s3files.us-east-1.on.aws` | Mount target IP for use1-az2 |
| `use1-az4.fs-0123456abcdef0189.s3files.us-east-1.on.aws` | Mount target IP for use1-az4 |

## Step 7: Configure IAM permissions

Attach an IAM role to the EC2 instance in Account B. The role must include the
following permissions to mount and access the file system:

- **The `AmazonS3FilesClientFullAccess` managed
  policy (or equivalent)** — This policy grants the EC2
  instance permission to connect to and interact with S3 Files file
  systems.
- **An inline policy granting S3 object access to the
  cross-account bucket** — This policy grants the EC2 instance
  permission to read objects directly from the S3 bucket in Account A.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3ObjectReadAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::BUCKET_NAME_ACCOUNT_A/*"
        },
        {
            "Sid": "S3BucketListAccess",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::BUCKET_NAME_ACCOUNT_A"
        }
    ]
}
```

Replace `BUCKET_NAME_ACCOUNT_A` with the name of the S3
bucket in Account A.

###### Note

For the complete list of required base policies for your compute resource, see
[IAM role for attaching your
file system to AWS compute resources](s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role "s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role").

## Step 8: Mount the file system

[Connect
to your EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in Account B and run the following commands.

1. Create a mount point:

```
sudo mkdir /mnt/s3files
```

2. Mount the file system:

```
sudo mount -t s3files fs-0123456abcdef0189 /mnt/s3files
```

3. Verify the mount:

```
df -h /mnt/s3files
ls /mnt/s3files
```

## Troubleshooting

Use the following information to resolve common issues when mounting an S3 file system
across accounts.

Mount fails with a DNS resolution error
Verify that both VPCs have `enableDnsSupport` and
`enableDnsHostnames` enabled. Verify that the Route 53 private hosted
zones are associated with the correct VPC in Account B and that A records point
to the correct mount target IP addresses.

Mount hangs or times out
Verify that the VPC peering connection status is **Active**. Verify that route tables in both accounts
have entries for the peer VPC CIDR pointing to the peering connection. Verify
that the mount target security group allows inbound TCP on port 2049 from the
EC2 instance security group.

Permission denied on file operations
Verify that the EC2 instance IAM role has both the
`AmazonS3FilesClientFullAccess` managed policy and the inline S3
object access policy attached. Verify that the file system policy in Account A
grants `s3files:ClientMount` and `s3files:ClientWrite` to
the Account B role.
