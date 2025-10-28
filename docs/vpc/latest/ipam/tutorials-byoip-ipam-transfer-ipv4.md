# Tutorial: Transfer a BYOIP IPv4 CIDR to IPAM

Follow these steps to transfer an existing IPv4 CIDR to IPAM. If you already have an IPv4
BYOIP CIDR with AWS, you can move the CIDR to IPAM from a public IPv4 pool. You cannot
move an IPv6 CIDR to IPAM.

This tutorial assumes you have already successfully brought an IP address range to AWS using the process described in [Bring your own IP addresses (BYOIP) in Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md") and now you want to transfer that IP address range to IPAM. If you are bringing a new IP address to AWS for the first time,
complete the steps in [Tutorial: Bring your IP addresses to IPAM](tutorials-byoip-ipam.md "tutorials-byoip-ipam.md").

If you transfer a public IPv4 pool to IPAM, there is no impact on existing allocations.
Once you transfer a public IPv4 pool to IPAM, depending on the resource type, you may be
able to monitor the existing allocations. For more information, see [Monitor CIDR usage by resource](monitor-cidr-compliance-ipam.md "monitor-cidr-compliance-ipam.md").

###### Note

- This tutorial assumes you have already completed the steps in [Create an IPAM](create-ipam.md "create-ipam.md").
- Each step of this tutorial must be done by one of two AWS accounts:
  - The account for the IPAM administrator. In this tutorial, this account will be called the IPAM account.
  - The account in your organization which owns the BYOIP CIDR. In this tutorial, this account will be called the BYOIP CIDR owner account.

###### Contents

- [Step 1: Create AWS CLI named profiles and IAM roles](#tutorials-byoip-ipam-ipv4-console-1 "#tutorials-byoip-ipam-ipv4-console-1")
- [Step 2: Get your IPAM’s public scope
  ID](#tutorials-byoip-ipam-transfer-ipv4-2 "#tutorials-byoip-ipam-transfer-ipv4-2")
- [Step 3: Create an IPAM pool](#tutorials-byoip-ipam-transfer-ipv4-3 "#tutorials-byoip-ipam-transfer-ipv4-3")
- [Step 4: Share the IPAM pool using AWS RAM](#tutorials-byoip-ipam-transfer-ipv4-4 "#tutorials-byoip-ipam-transfer-ipv4-4")
- [Step 5: Transfer an existing BYOIP IPV4 CIDR to IPAM](#tutorials-byoip-ipam-transfer-ipv4-5 "#tutorials-byoip-ipam-transfer-ipv4-5")
- [Step 6: View the CIDR in IPAM](#tutorials-byoip-ipam-transfer-ipv4-6 "#tutorials-byoip-ipam-transfer-ipv4-6")
- [Step 7: Cleanup](#tutorials-byoip-ipam-transfer-ipv4-7 "#tutorials-byoip-ipam-transfer-ipv4-7")

## Step 1: Create AWS CLI named profiles and IAM roles

To complete this tutorial as a single AWS user, you can use AWS CLI named profiles to switch
from one IAM role to another. [Named profiles](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles") are
collections of settings and credentials that you
refer to when using the `--profile` option with the AWS CLI.
For more
information about how to create IAM roles and named profiles for AWS accounts, see
[Using an IAM role in the AWS CLI](../../../cli/latest/userguide/cli-configure-role.md "../../../cli/latest/userguide/cli-configure-role.md").

Create one role and one named profile for each of the three AWS accounts you will use in this tutorial:

- A profile called `ipam-account` for the AWS account that is the IPAM administrator.
- A profile called `byoip-owner-account` for the AWS account in your organization which owns the BYOIP CIDR.

After you have created the IAM roles and named profiles, return to this page and go to the next step. You will notice throughout the rest of this tutorial that the sample AWS CLI commands use the `--profile` option with one of the named profiles to indicate which account must run the command.

## Step 2: Get your IPAM’s public scope

ID

Follow the steps in this section to get your IPAM’s public scope ID. This step should
be performed by the `ipam-account` account.

Run the following command to get your public scope ID.

```
aws ec2 describe-ipams --region `us-east-1` --profile `ipam-account`
```

In the output, you'll see your public scope ID. Note the values for `PublicDefaultScopeId`. You will need it in the next step.

```
{
 "Ipams": [
        {
            "OwnerId": "123456789012",
            "IpamId": "ipam-090e48e75758de279",
            "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
            "PublicDefaultScopeId": "ipam-scope-0087d83896280b594",
            "PrivateDefaultScopeId": "ipam-scope-08b70b04fbd524f8d",
            "ScopeCount": 2,
            "Description": "my-ipam",
            "OperatingRegions": [
                {
                    "RegionName": "us-east-1"
                },
                {
                    "RegionName": "us-west-2"
                }
            ],
            "Tags": []
        }
    ]
}
```

## Step 3: Create an IPAM pool

Follow the steps in this section to create an IPAM pool. This step should be performed
by the `ipam-account` account. The IPAM pool you create must be a
top-level pool with the `--locale` option matching the BYOIP CIDR AWS
Region. You can only transfer a BYOIP to a top-level IPAM pool.

###### Important

When you create the pool, you must include `--aws-service ec2`. The service you select determines the AWS service where the CIDR will be advertisable. Currently, the only option is `ec2`, which means that the CIDRs allocated from this pool will be advertisable for the Amazon EC2 service (for Elastic IP addresses) and the Amazon VPC service (for CIDRs associated with VPCs).

###### To create an IPv4 address pool for the transferred BYOIP CIDR using the

AWS CLI

1. Run the following command to create an IPAM pool. Use the ID of the public
   scope of the IPAM that you retrieved in the previous step.

```
aws ec2 create-ipam-pool --region `us-east-1` --profile `ipam-account` --ipam-scope-id `ipam-scope-0087d83896280b594` --description `"top-level-pool"` --locale `us-west-2` --aws-service ec2 --address-family `ipv4`
```

In the output, you'll see `create-in-progress`, which indicates that pool creation is in progress.

```
{
    "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-0a03d430ca3f5c035",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0a03d430ca3f5c035",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "Locale": "us-west-2",
        "PoolDepth": 1,
        "State": "create-in-progress",
        "Description": "top-level-pool",
        "AutoImport": false,
        "AddressFamily": "ipv4",
        "Tags": [],
        "AwsService": "ec2"
    }
}
```

2. Run the following command until you see a state of
   `create-complete` in the output.

```
aws ec2 describe-ipam-pools --region `us-east-1` --profile `ipam-account`
```

The following example output shows the state of the pool. You will need the
**OwnerId** in the next step.

```
{
    "IpamPools": [
        {
            "OwnerId": "123456789012",
            "IpamPoolId": "ipam-pool-0a03d430ca3f5c035",
            "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0a03d430ca3f5c035",
            "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
            "IpamScopeType": "public",
            "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
            "Locale": "us-west-2",
            "PoolDepth": 1,
            "State": "create-complete",
            "Description": "top-level-pool",
            "AutoImport": false,
            "AddressFamily": "ipv4",
            "Tags": [],
            "AwsService": "ec2"
        }
    ]
}
```

## Step 4: Share the IPAM pool using AWS RAM

Follow the steps in this section to share an IPAM pool using AWS RAM so that another AWS account can transfer an existing BYOIP IPV4 CIDR to the IPAM pool and use the IPAM pool. This
step should be performed by the `ipam-account` account.

###### To share an IPv4 address pool using the

AWS CLI

1. View the AWS RAM permissions available for IPAM pools. You need both ARNs to complete the steps
   in this section.

```
aws ram list-permissions --region `us-east-1` --profile `ipam-account` --resource-type ec2:IpamPool
```

```
{
    "permissions": [
        {
           "arn": "arn:aws:ram::aws:permission/AWSRAMDefaultPermissionsIpamPool",
           "version": "1",
           "defaultVersion": true,
           "name": "AWSRAMDefaultPermissionsIpamPool",
           "resourceType": "ec2:IpamPool",
           "status": "ATTACHABLE",
           "creationTime": "2022-06-30T13:04:29.335000-07:00",
           "lastUpdatedTime": "2022-06-30T13:04:29.335000-07:00",
           "isResourceTypeDefault": true
        },
        {
            "arn": "arn:aws:ram::aws:permission/AWSRAMPermissionIpamPoolByoipCidrImport",
            "version": "1",
            "defaultVersion": true,
            "name": "AWSRAMPermissionIpamPoolByoipCidrImport",
            "resourceType": "ec2:IpamPool",
            "status": "ATTACHABLE",
            "creationTime": "2022-06-30T13:03:55.032000-07:00",
            "lastUpdatedTime": "2022-06-30T13:03:55.032000-07:00",
            "isResourceTypeDefault": false
        }
    ]
}
```

2. Create a resource share to enable the `byoip-owner-account` account to
   import BYOIP CIDRs to IPAM. The value for `--resource-arns` is the
   ARN of the IPAM pool that you created in the previous section. The value for
   `--principals` is the account ID of the BYOIP CIDR owner account.
   The value for `--permission-arns` is the ARN of the
   `AWSRAMPermissionIpamPoolByoipCidrImport` permission.

```
aws ram create-resource-share --region `us-east-1` --profile `ipam-account` --name `PoolShare2` --resource-arns `arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0a03d430ca3f5c035` --principals `111122223333` --permission-arns arn:aws:ram::aws:permission/AWSRAMPermissionIpamPoolByoipCidrImport
```

```
{
    "resourceShare": {
        "resourceShareArn": "arn:aws:ram:us-east-1:123456789012:resource-share/7993758c-a4ea-43ad-be12-b3abaffe361a",
        "name": "PoolShare2",
        "owningAccountId": "123456789012",
        "allowExternalPrincipals": true,
        "status": "ACTIVE",
        "creationTime": "2023-04-28T07:32:25.536000-07:00",
        "lastUpdatedTime": "2023-04-28T07:32:25.536000-07:00"
        }
}
```

3. (Optional) If you want to allow the `byoip-owner-account` account to
   allocate IP address CIDRS from the IPAM pool to public IPv4 pools after the
   transfer is complete, copy the ARN for
   `AWSRAMDefaultPermissionsIpamPool` and create a second resource
   share. The value for `--resource-arns` is the ARN of the IPAM pool
   that you created in the previous section. The value for
   `--principals` is the account ID of the BYOIP CIDR owner account.
   The value for `--permission-arns` is the ARN of the
   `AWSRAMDefaultPermissionsIpamPool` permission.

```
aws ram create-resource-share --region `us-east-1` --profile `ipam-account` --name `PoolShare1` --resource-arns `arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0a03d430ca3f5c035` --principals `111122223333` --permission-arns arn:aws:ram::aws:permission/AWSRAMDefaultPermissionsIpamPool
```

```
{
    "resourceShare": {
        "resourceShareArn": "arn:aws:ram:us-east-1:123456789012:resource-share/8d1e229b-2830-4cf4-8b10-19c889235a2f",
        "name": "PoolShare1",
        "owningAccountId": "123456789012",
        "allowExternalPrincipals": true,
        "status": "ACTIVE",
        "creationTime": "2023-04-28T07:31:25.536000-07:00",
        "lastUpdatedTime": "2023-04-28T07:31:25.536000-07:00"
        }
}
```

As a result of creating the resource share in RAM, the byoip-owner-account account can
now move CIDRs to IPAM.

## Step 5: Transfer an existing BYOIP IPV4 CIDR to IPAM

Follow the steps in this section to transfer an existing BYOIP IPV4 CIDR to IPAM. This
step should be performed by the `byoip-owner-account`
account.

###### Important

Once you bring an IPv4 address range to AWS, you can use all of the IP addresses in the range, including the first address (the network address) and the last address (the broadcast address).

To transfer the BYOIP CIDR to IPAM, the BYOIP CIDR owner must have these permissions
in their IAM policy:

- `ec2:MoveByoipCidrToIpam`
- `ec2:ImportByoipCidrToIpam`

###### Note

You can use either the AWS Management Console or the AWS CLI for this step.

AWS Management Console

###### To transfer a BYOIP CIDR to the IPAM pool:

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/")
   as the `byoip-owner-account` account.
2. In the navigation pane, choose **Pools**.
3. Choose the top-level pool created and shared in this
   tutorial.
4. Choose **Actions** > **Transfer BYOIP
   CIDR**.
5. Choose **Transfer BYOIP CIDR**.
6. Choose your BYOIP CIDR.
7. Choose **Provision**.

Command line
Use the following AWS CLI commands transfer a BYOIP CIDR to the IPAM pool using the AWS CLI:

1. Run the following command to transfer the CIDR. Ensure that the
   `--region` value is the AWS Region of the BYOIP CIDR.

```
aws ec2 move-byoip-cidr-to-ipam --region `us-west-2` --profile `byoip-owner-account` --ipam-pool-id `ipam-pool-0a03d430ca3f5c035` --ipam-pool-owner `123456789012` --cidr `130.137.249.0/24`
```

In the output, you'll see the CIDR pending provision.

```
{
    "ByoipCidr": {
        "Cidr": "130.137.249.0/24",
        "State": "pending-transfer"
    }
}
```

2. Ensure that the CIDR has been transferred. Run the following
   command until you see a state of `complete-transfer` in the output.

```
aws ec2 move-byoip-cidr-to-ipam --region `us-west-2`  --profile `byoip-owner-account` --ipam-pool-id `ipam-pool-0a03d430ca3f5c035` --ipam-pool-owner `123456789012` --cidr `130.137.249.0/24`
```

The following example output shows the state.

```
{
    "ByoipCidr": {
        "Cidr": "130.137.249.0/24",
        "State": "complete-transfer"
    }
}
```

## Step 6: View the CIDR in IPAM

Follow the steps in this section to view the CIDR in IPAM. This step should be
performed by the `ipam-account` account.

###### To view the transferred BYOIP CIDR in IPAM pool using the AWS CLI

- Run the following command to view the allocation managed in IPAM. Ensure that
  the `--region` value is the AWS Region of the BYOIP CIDR.

```
aws ec2 get-ipam-pool-allocations --region `us-west-2`  --profile `ipam-account` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987`
```

The output shows the allocation in IPAM.

```
{
    "IpamPoolAllocations": [
        {
            "Cidr": "130.137.249.0/24",
            "IpamPoolAllocationId": "ipam-pool-alloc-5dedc8e7937c4261b56dc3e3eb53dc46",
            "ResourceId": "ipv4pool-ec2-0019eed22a684e0b3",
            "ResourceType": "ec2-public-ipv4-pool",
            "ResourceOwner": "111122223333"
        }
    ]
}
```

## Step 7: Cleanup

Follow the steps in this section to remove the resources you created in this tutorial.
This step should be performed by the `ipam-account` account.

###### To cleanup the resources created in this tutorial using the AWS CLI

1. To delete the IPAM pool shared resource, run the following command to get the first resource
   share ARN:

```
aws ram get-resource-shares --region `us-east-1` --profile `ipam-account` --name `PoolShare1` --resource-owner SELF
```

```
{
    "resourceShares": [
        {
            "resourceShareArn": "arn:aws:ram:us-east-1:123456789012:resource-share/8d1e229b-2830-4cf4-8b10-19c889235a2f",
            "name": "PoolShare1",
            "owningAccountId": "123456789012",
            "allowExternalPrincipals": true,
            "status": "ACTIVE",
            "creationTime": "2023-04-28T07:31:25.536000-07:00",
            "lastUpdatedTime": "2023-04-28T07:31:25.536000-07:00",
            "featureSet": "STANDARD"
        }
    ]
}

```

2. Copy the resource share ARN and use it to delete the IPAM pool resource share.

```
aws ram delete-resource-share --region `us-east-1` --profile `ipam-account` --resource-share-arn `arn:aws:ram:us-east-1:123456789012:resource-share/8d1e229b-2830-4cf4-8b10-19c889235a2f`
```

```
{
    "returnValue": true
}
```

3. If you created an additional resource share in [Step 4: Share the IPAM pool using AWS RAM](#tutorials-byoip-ipam-transfer-ipv4-4 "#tutorials-byoip-ipam-transfer-ipv4-4"), repeat the previous two steps
   to get the second resource share ARN for `PoolShare2` and delete the
   second resource share.
4. Run the following command to get the allocation ID for the BYOIP CIDR. Ensure
   that the `--region` value matches the AWS Region of the BYOIP
   CIDR.

```
aws ec2 get-ipam-pool-allocations --region `us-west-2`  --profile `ipam-account` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987`
```

The output shows the allocation in IPAM.

```
{
    "IpamPoolAllocations": [
        {
            "Cidr": "130.137.249.0/24",
            "IpamPoolAllocationId": "ipam-pool-alloc-5dedc8e7937c4261b56dc3e3eb53dc46",
            "ResourceId": "ipv4pool-ec2-0019eed22a684e0b3",
            "ResourceType": "ec2-public-ipv4-pool",
            "ResourceOwner": "111122223333"
        }
    ]
}
```

5. Release the CIDR from the public IPv4 pool. When you run the command in this
   section, the value for `--region` must match the Region of your
   IPAM.

This step must be done by the `byoip-owner-account`
account.

```
aws ec2 deprovision-public-ipv4-pool-cidr --region `us-east-1`  --profile `byoip-owner-account` --pool-id `ipv4pool-ec2-0019eed22a684e0b3` --cidr `130.137.249.0/24`
```

6. View your BYOIP CIDRs again and ensure there are no more provisioned
   addresses. When you run the command in this section, the value for
   `--region` must match the Region of your IPAM.

This step must be done by the `byoip-owner-account`
account.

```
aws ec2 describe-public-ipv4-pools --region `us-east-1` --profile `byoip-owner-account`
```

In the output, you'll see the IP addresses count in your public IPv4 pool.

```
{
    "PublicIpv4Pools": [
        {
            "PoolId": "ipv4pool-ec2-0019eed22a684e0b3",
            "Description": "",
            "PoolAddressRanges": [],
            "TotalAddressCount": 0,
            "TotalAvailableAddressCount": 0,
            "NetworkBorderGroup": "us-east-1",
            "Tags": []
        }
    ]
}
```

7. Run the following command to delete the top-level pool.

```
aws ec2 delete-ipam-pool --region `us-east-1`  --profile `ipam-account` --ipam-pool-id `ipam-pool-0a03d430ca3f5c035`
```

In the output, you can see the delete state.

```
{
    "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-0a03d430ca3f5c035",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0a03d430ca3f5c035",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "Locale": "us-east-1",
        "PoolDepth": 2,
        "State": "delete-in-progress",
        "Description": "top-level-pool",
        "AutoImport": false,
        "Advertisable": true,
        "AddressFamily": "ipv4",
        "AwsService": "ec2"
    }
}
```
