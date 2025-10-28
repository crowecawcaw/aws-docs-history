# Bring your own IPv6 CIDR to IPAM using only the AWS CLI

Follow these steps to bring an IPv6 CIDR to IPAM and allocate a VPC using only the AWS CLI.

If you do not need to advertise your IPv6 addresses over the Internet, you can provision a private GUA IPv6 address to an IPAM. For more information, see [Enable provisioning private IPv6 GUA CIDRs](enable-prov-ipv6-gua.md "enable-prov-ipv6-gua.md").

###### Important

- This tutorial assumes you have already completed the steps in the following sections:
  - [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md "enable-integ-ipam.md").
  - [Create an IPAM](create-ipam.md "create-ipam.md").

- Each step of this tutorial must be done by one of three AWS Organizations accounts:
  - The management account.
  - The member account configured to be your IPAM administrator in [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md "enable-integ-ipam.md"). In this tutorial, this account will be called the IPAM account.
  - The member account in your organization which will allocate CIDRs from an IPAM pool. In this tutorial, this account will be called the member account.

###### Contents

- [Step 1: Create AWS CLI named profiles and IAM roles](#tutorials-create-profiles "#tutorials-create-profiles")
- [Step 2: Create an IPAM](#tutorials-byoip-ipam-ipv6-2 "#tutorials-byoip-ipam-ipv6-2")
- [Step 3: Create an IPAM pool](#tutorials-byoip-ipam-ipv6-3 "#tutorials-byoip-ipam-ipv6-3")
- [Step 4: Provision a CIDR to the top-level pool](#tutorials-byoip-ipam-ipv6-4 "#tutorials-byoip-ipam-ipv6-4")
- [Step 5: Create a Regional pool within the
  top-level pool](#tutorials-byoip-ipam-ipv6-5 "#tutorials-byoip-ipam-ipv6-5")
- [Step 6: Provision a CIDR to the Regional pool](#tutorials-byoip-ipam-ipv6-6 "#tutorials-byoip-ipam-ipv6-6")
- [Step 7. Share the Regional pool](#tutorials-byoip-ipam-ipv4-console-4-deux "#tutorials-byoip-ipam-ipv4-console-4-deux")
- [Step 8: Create a VPC using the IPv6 CIDR](#tutorials-byoip-ipam-ipv6-8 "#tutorials-byoip-ipam-ipv6-8")
- [Step 9: Advertise the CIDR](#tutorials-byoip-ipam-ipv6-9 "#tutorials-byoip-ipam-ipv6-9")
- [Step 10: Cleanup](#tutorials-byoip-ipam-ipv4-cleanup "#tutorials-byoip-ipam-ipv4-cleanup")

## Step 1: Create AWS CLI named profiles and IAM roles

To complete this tutorial as a single AWS user, you can use AWS CLI named profiles to switch
from one IAM role to another. [Named profiles](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles") are
collections of settings and credentials that you
refer to when using the `--profile` option with the AWS CLI.
For more
information about how to create IAM roles and named profiles for AWS accounts, see
[Using an IAM role in the AWS CLI](../../../cli/latest/userguide/cli-configure-role.md "../../../cli/latest/userguide/cli-configure-role.md").

Create one role and one named profile for each of the three AWS accounts you will use in this tutorial:

- A profile called `management-account` for the AWS Organizations management account.
- A profile called `ipam-account` for the AWS Organizations member account that is configured to be your IPAM administrator.
- A profile called `member-account` for the AWS Organizations member account in your organization which will allocate CIDRs from an IPAM pool.

After you have created the IAM roles and named profiles, return to this page and go to the next step. You will notice throughout the rest of this tutorial that the sample AWS CLI commands use the `--profile` option with one of the named profiles to indicate which account must run the command.

## Step 2: Create an IPAM

This step is optional. If you already have an IPAM created with operating Regions of
`us-east-1` and `us-west-2` created, you can skip this step.
Create an IPAM and specify an operating region of `us-east-1` and
`us-west-2` . You must select an operating region so that you can use the
locale option when you create your IPAM pool. The IPAM integration with BYOIP requires
that the locale is set on whichever pool will be used for the BYOIP CIDR.

This step must be done by the IPAM account.

Run the following command:

```
aws ec2 create-ipam --description `my-ipam` --region `us-east-1` --operating-regions `RegionName=us-west-2` --profile `ipam-account`
```

In the output, you'll see the IPAM you've created. Note the value for `PublicDefaultScopeId`. You will need your public scope ID in the next step.

```
{
 "Ipam": {
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
}

```

## Step 3: Create an IPAM pool

Since you are going to create a top-level IPAM pool with a Regional pool within it,
and we’re going to allocate space to a resource (a VPC) from the
Regional pool, you will set the locale on the Regional pool and not the top-level
pool. You’ll add the locale to the Regional pool when you create the Regional pool
in a later step. The IPAM integration with BYOIP requires that the locale is set on
whichever pool will be used for the BYOIP CIDR.

This step must be done by the IPAM account.

Choose if you want this IPAM pool CIDR to be advertisable by AWS over the public internet (`--publicly-advertisable` or `--no-publicly-advertisable`).

###### Note

Note that the scope ID must be the ID for the public scope and the address family must be `ipv6`.

###### To create an IPv6 address pool for all of your AWS resources using the

AWS CLI

1. Run the following command to create an IPAM pool. Use the ID of the public
   scope of the IPAM that you created in the previous step.

```
aws ec2 create-ipam-pool --region `us-east-1` --ipam-scope-id `ipam-scope-0087d83896280b594` --description `"top-level-IPv6-pool"` --address-family `ipv6` `--publicly-advertisable` --profile `ipam-account`
```

In the output, you'll see `create-in-progress`, which indicates that pool creation is in progress.

```
{
    "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-07f2466c7158b50c4",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-07f2466c7158b50c4",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "Locale": "None",
        "PoolDepth": 1,
        "State": "create-in-progress",
        "Description": "top-level-Ipv6-pool",
        "AutoImport": false,
        "Advertisable": true,
        "AddressFamily": "ipv6",
        "Tags": []
    }
}
```

2. Run the following command until you see a state of
   `create-complete` in the output.

```
aws ec2 describe-ipam-pools --region `us-east-1` --profile `ipam-account`

```

The following example output shows the state of the pool.

```
{
    "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-07f2466c7158b50c4",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-07f2466c7158b50c4",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "Locale": "None",
        "PoolDepth": 1,
        "State": "create-complete",
        "Description": "top-level-Ipv6-pool",
        "AutoImport": false,
        "Advertisable": true,
        "AddressFamily": "ipv6",
        "Tags": []
    }
}
```

## Step 4: Provision a CIDR to the top-level pool

Provision a CIDR block to the top-level pool. Note that when provisioning an IPv6 CIDR
to a pool within the top-level pool, the most specific IPv6 address range that you can
bring is /48 for CIDRs that are publicly advertisable and /60 for CIDRs that are not
publicly advertisable.

###### Note

- If you [verified
  your domain control with an X.509 certificate](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert"), you must include the
  CIDR and the BYOIP message and certificate signature that you created in that step so we can
  verify that you control the public space.
- If you [verified your domain control with a DNS TXT record](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt"), you must
  include the CIDR and IPAM verification token that you created in that step so we can verify
  that you control the public space.

You only need to verify domain control when you provision the BYOIP CIDR to the
top-level pool. For the Regional pool within the top-level pool, you can omit the domain
ownership option.

This step must be done by the IPAM account.

###### To provision a CIDR block to the pool using the AWS CLI

1. To provision the CIDR with certificate information, use the following command
   example. In addition to replacing the values as
   needed in the example, ensure that you replace `Message` and
   `Signature` values with the `text_message` and
   `signed_message` values that you got in [Verify your domain with an X.509 certificate](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert").

```
aws ec2 provision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-07f2466c7158b50c4` --cidr `2605:9cc0:409::/48` --verification-method remarks-x509 --cidr-authorization-context Message="`1|aws|470889052444|2605:9cc0:409::/48|20250101|SHA256|RSAPSS`",Signature="`FU26~vRG~NUGXa~akxd6dvdcCfvL88g8d~YAuai-CR7HqMwzcgdS9RlpBGtfIdsRGyr77LmWyWqU9Xp1g2R1kSkfD00NiLKLcv9F63k6wdEkyFxNp7RAJDvF1mBwxmSgH~Crt-Vp6LON3yOOXMp4JENB9uM7sMlu6oeoutGyyhXFeYPzlGSRdcdfKNKaimvPCqVsxGN5AwSilKQ8byNqoa~G3dvs8ueSaDcT~tW4CnILura70nyK4f2XzgPKKevAD1g8bpKmOFMbHS30CxduYknnDl75lvEJs1J91u3-wispI~r69fq515UR19TA~fmmxBDh1huQ8DkM1rqcwveWow__`" --profile `ipam-account`
```

To provision the CIDR with verification token information, use the following
command example. In addition to replacing the values
as needed in the example, ensure that you replace
`ipam-ext-res-ver-token-0309ce7f67a768cf0` with the
`IpamExternalResourceVerificationTokenId` token ID that you got
in [Verify your domain with a DNS TXT record](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt").

```
aws ec2 provision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-07f2466c7158b50c4` --cidr `2605:9cc0:409::/48` --verification-method dns-token --ipam-external-resource-verification-token-id `ipam-ext-res-ver-token-0309ce7f67a768cf0` --profile `ipam-account`
```

In the output, you'll see the CIDR pending provision.

```
{
    "IpamPoolCidr": {
        "Cidr": "2605:9cc0:409::/48",
        "State": "pending-provision"
    }
}
```

2. Ensure that this CIDR has been provisioned before you continue.

###### Important

While most provisioning will be completed within two hours, it may take up
to one week to complete the provisioning process for publicly advertisable
ranges.

Run the following
command until you see a state of `provisioned` in the output.

```
aws ec2 get-ipam-pool-cidrs --region `us-east-1` --ipam-pool-id `ipam-pool-07f2466c7158b50c4` --profile `ipam-account`
```

The following example output shows the state.

```
{
    "IpamPoolCidrs": [
        {
            "Cidr": "2605:9cc0:409::/48",
            "State": "provisioned"
        }
    ]
}
```

## Step 5: Create a Regional pool within the

top-level pool

Create a Regional pool within the top-level pool. `--locale` is required on
the pool and it must be one of the operating Regions you configured when you created the
IPAM.

This step must be done by the IPAM account.

###### Important

When you create the pool, you must include `--aws-service ec2`. The service you select determines the AWS service where the CIDR will be advertisable. Currently, the only option is `ec2`, which means that the CIDRs allocated from this pool will be advertisable for the Amazon EC2 service and the Amazon VPC service (for CIDRs associated with VPCs).

###### To create a Regional pool using the

AWS CLI

1. Run the following command to create the pool.

```
aws ec2 create-ipam-pool --description `"Regional-IPv6-pool"` --region `us-east-1` --ipam-scope-id `ipam-scope-0087d83896280b594` --source-ipam-pool-id `ipam-pool-07f2466c7158b50c4` --locale `us-west-2` --address-family `ipv6` --aws-service ec2 --profile `ipam-account`
```

In the output, you'll see IPAM creating the pool.

```
{
    "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-0053b7d2b4fc3f730",
        "SourceIpamPoolId": "ipam-pool-07f2466c7158b50c4",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0053b7d2b4fc3f730",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "Locale": "us-west-2",
        "PoolDepth": 2,
        "State": "create-in-progress",
        "Description": "reg-ipv6-pool",
        "AutoImport": false,
        "Advertisable": true,
        "AddressFamily": "ipv6",
        "Tags": [],
        "ServiceType": "ec2"
    }
}
```

2. Run the following command until you see a state of
   `create-complete` in the output.

```
aws ec2 describe-ipam-pools --region `us-east-1` --profile `ipam-account`
```

In the output, you see the pools that you have in your IPAM. In this tutorial,
we created a top-level and a Regional pool, so you'll see them both.

## Step 6: Provision a CIDR to the Regional pool

Provision a CIDR block to the Regional pool. Note that when provisioning the CIDR to a
pool within the top-level pool, the most specific IPv6 address range that you can bring
is /48 for CIDRs that are publicly advertisable and /60 for CIDRs that are not publicly
advertisable.

This step must be done by the IPAM account.

###### To assign a CIDR block to the Regional pool using the AWS CLI

1. Run the following command to provision the CIDR.

```
aws ec2 provision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --cidr `2605:9cc0:409::/48` --profile `ipam-account`
```

In the output, you'll see the CIDR pending provision.

```
{
    "IpamPoolCidr": {
        "Cidr": "2605:9cc0:409::/48",
        "State": "pending-provision"
    }
}
```

2. Run the following command until you see the state of `provisioned`
   in the output.

```
aws ec2 get-ipam-pool-cidrs --region `us-east-1` --ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --profile `ipam-account`
```

The following example output shows the correct state.

```
{
    "IpamPoolCidrs": [
        {
            "Cidr": "2605:9cc0:409::/48",
            "State": "provisioned"
        }
    ]
}
```

## Step 7. Share the Regional pool

Follow the steps in this section to share the IPAM pool using AWS Resource Access Manager (RAM).

### Enable resource sharing in

AWS RAM

After you create your IPAM, you’ll want to share the regional pool with other
accounts in your organization. Before you share an IPAM pool, complete the steps in
this section to enable resource sharing with AWS RAM. If you are using the AWS CLI to
enable resource sharing, use the `--profile
 `management-account`` option.

###### To enable resource sharing

1. Using the AWS Organizations management account, open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/ "https://console.aws.amazon.com/ram/").
2. In the left navigation pane, choose **Settings**,
   choose **Enable sharing with AWS Organizations**, and then choose **Save settings**.

You can now share an IPAM pool with other members of the organization.

### Share an IPAM pool using AWS RAM

In this section you’ll share the regional pool with another AWS Organizations member
account. For complete instructions on sharing IPAM pools, including information on
the required IAM permissions, see [Share an IPAM pool using AWS RAM](share-pool-ipam.md "share-pool-ipam.md"). If you are using the AWS CLI to enable resource sharing, use the `--profile `ipam-account`` option.

###### To share an IPAM pool using AWS RAM

1. Using the IPAM admin account, open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. Choose the private scope, choose the IPAM pool, and choose
   **Actions** > **View
   details**.
4. Under **Resource sharing**, choose **Create resource share**. The AWS RAM console opens.
   You share the pool using AWS RAM.
5. Choose **Create a resource share**.
6. In the AWS RAM console, choose **Create a resource share**
   again.
7. Add a **Name** for the shared pool.
8. Under **Select resource type**, choose **IPAM pools,** and then choose the ARN of the pool you want to share.
9. Choose **Next**.
10. Choose the **AWSRAMPermissionIpamPoolByoipCidrImport**
    permission. The details of the permission options are out of scope for this
    tutorial, but you can find out more about these options in [Share an IPAM pool using AWS RAM](share-pool-ipam.md "share-pool-ipam.md").
11. Choose **Next**.
12. Under **Principals** > **Select principal
    type**, choose **AWS account** and enter the
    account ID of the account that will be bringing an IP address range to IPAM and choose **Add** .
13. Choose **Next**.
14. Review the resource share options and the principals that you’ll be
    sharing with, and then choose **Create**.
15. To allow the `member-account` account to allocate IP
    address CIDRS from the IPAM pool, create a second resource share with
    `AWSRAMDefaultPermissionsIpamPool`. The value for `--resource-arns` is the ARN of the
    IPAM pool that you created in the previous section. The value for
    `--principals` is the account ID of the `member-account`. The value for `--permission-arns` is the ARN of the
    `AWSRAMDefaultPermissionsIpamPool` permission.

## Step 8: Create a VPC using the IPv6 CIDR

Create a VPC using the IPAM pool ID. You must associate an IPv4 CIDR block to the VPC
as well using the `--cidr-block` option or the request will fail. When you
run the command in this section, the value for `--region` must match the
`--locale` option you entered when you created the pool that will be used
for the BYOIP CIDR.

This step must be done by the member account.

###### To create a VPC with the IPv6 CIDR using the AWS CLI

1. Run the following command to provision the CIDR.

```
aws ec2 create-vpc --region `us-west-2` --ipv6-ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --cidr-block `10.0.0.0/16` --ipv6-netmask-length `56` --profile `member-account`
```

In the output, you'll see the VPC being created.

```
{
    "Vpc": {
        "CidrBlock": "10.0.0.0/16",
        "DhcpOptionsId": "dopt-2afccf50",
        "State": "pending",
        "VpcId": "vpc-00b5573ffc3b31a29",
        "OwnerId": "123456789012",
        "InstanceTenancy": "default",
        "Ipv6CidrBlockAssociationSet": [
            {
                "AssociationId": "vpc-cidr-assoc-01b5703d6cc695b5b",
                "Ipv6CidrBlock": "2605:9cc0:409::/56",
                "Ipv6CidrBlockState": {
                    "State": "associating"
                },
                "NetworkBorderGroup": "us-east-1",
                "Ipv6Pool": "ipam-pool-0053b7d2b4fc3f730"
            }
        ],
        "CidrBlockAssociationSet": [
            {
                "AssociationId": "vpc-cidr-assoc-09cccb07d4e9a0e0e",
                "CidrBlock": "10.0.0.0/16",
                "CidrBlockState": {
                    "State": "associated"
                }
            }
        ],
        "IsDefault": false
    }
}
```

2. View the VPC allocation in IPAM.

```
aws ec2 get-ipam-pool-allocations --region `us-west-2` --ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --profile `ipam-account`

```

In the output, you'll see allocation in IPAM.

```
{
    "IpamPoolAllocations": [
        {
            "Cidr": "2605:9cc0:409::/56",
            "IpamPoolAllocationId": "ipam-pool-alloc-5f8db726fb9e4ff0a33836e649283a52",
            "ResourceId": "vpc-00b5573ffc3b31a29",
            "ResourceType": "vpc",
            "ResourceOwner": "123456789012"
        }
    ]
}
```

## Step 9: Advertise the CIDR

Once you create the VPC with CIDR allocated in IPAM, you can then start advertising
the CIDR you brought to AWS that is in pool that has `--aws-service ec2`
defined. In this tutorial, that's your Regional pool. By default the CIDR is not
advertised, which means it's not publicly accessible over the internet. When you run the
command in this section, the value for `--region` must match the
`--locale` option you entered when you created the Regional pool that
will be used for the BYOIP CIDR.

This step must be done by the IPAM account.

###### Start advertising the CIDR using the AWS CLI

- Run the following command to advertise the CIDR.

```
aws ec2 advertise-byoip-cidr --region `us-west-2` --cidr `2605:9cc0:409::/48` --profile `ipam-account`
```

In the output, you'll see the CIDR is advertised.

```
{
    "ByoipCidr": {
        "Cidr": "2605:9cc0:409::/48",
        "State": "advertised"
    }
}
```

## Step 10: Cleanup

Follow the steps in this section to clean up the resources you've provisioned and
created in this tutorial. When you run the commands in this section, the value for
`--region` must match the `--locale` option you entered when
you created the Regional pool that will be used for the BYOIP CIDR.

###### Clean up using the AWS CLI

1. Run the following command to view the VPC allocation managed in IPAM.

This step must be done by the IPAM account.

```
aws ec2 get-ipam-pool-allocations --region `us-west-2` --ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --profile `ipam-account`

```

The output shows the allocation in IPAM.

```
{
    "IpamPoolAllocations": [
        {
            "Cidr": "2605:9cc0:409::/56",
            "IpamPoolAllocationId": "ipam-pool-alloc-5f8db726fb9e4ff0a33836e649283a52",
            "ResourceId": "vpc-00b5573ffc3b31a29",
            "ResourceType": "vpc",
            "ResourceOwner": "123456789012"
        }
    ]
}
```

2. Run the following command to stop advertising the CIDR. When you run the
   command in this step, the value for `--region` must match the
   `--locale` option you entered when you created the Regional pool
   that will be used for the BYOIP CIDR.

This step must be done by the IPAM account.

```
aws ec2 withdraw-byoip-cidr --region `us-west-2` --cidr `2605:9cc0:409::/48` --profile `ipam-account`
```

In the output, you'll see the CIDR State has changed from **advertised** to **provisioned**.

```
{
    "ByoipCidr": {
        "Cidr": "2605:9cc0:409::/48",
        "State": "provisioned"
    }
}
```

3. Run the following command to delete the VPC. When you run the command in
   this section, the value for `--region` must match the
   `--locale` option you entered when you created the Regional pool
   that will be used for the BYOIP CIDR.

This step must be done by the member account.

```
aws ec2 delete-vpc --region `us-west-2` --vpc-id `vpc-00b5573ffc3b31a29` --profile `member-account`
```

You will not see any output when you run this command. 4. Run the following command to view the VPC allocation in IPAM. It can take
some time for IPAM to discover that the VPC has been deleted and remove this
allocation. When you run the commands in this section, the value for
`--region` must match the `--locale` option you
entered when you created the Regional pool that will be used for the BYOIP
CIDR.

This step must be done by the IPAM account.

```
aws ec2 get-ipam-pool-allocations --region `us-west-2` --ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --profile `ipam-account`
```

The output shows the allocation in IPAM.

```
{
   "IpamPoolAllocations": [
        {
            "Cidr": "2605:9cc0:409::/56",
            "IpamPoolAllocationId": "ipam-pool-alloc-5f8db726fb9e4ff0a33836e649283a52",
            "ResourceId": "vpc-00b5573ffc3b31a29",
            "ResourceType": "vpc",
            "ResourceOwner": "123456789012"
        }
    ]
}
```

Rerun the command and look for the allocation to be removed. You cannot continue to clean up and deprovision the IPAM pool CIDR
until you see that the allocation has been removed from IPAM.

```
aws ec2 get-ipam-pool-allocations --region `us-west-2` --ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --profile `ipam-account`
```

The output shows the allocation removed from IPAM.

```
{
    "IpamPoolAllocations": []
}
```

5. Delete the RAM shares and disable RAM integration with AWS
   Organizations. Complete the steps in [Deleting a resource
   share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-delete.md "../../../ram/latest/userguide/working-with-sharing-delete.md") and [Disabling
   resource sharing with AWS Organizations](../../../ram/latest/userguide/security-disable-sharing-with-orgs.md "../../../ram/latest/userguide/security-disable-sharing-with-orgs.md") in the _AWS RAM User Guide_, in that order, to delete the
   RAM shares and disable RAM integration with AWS Organizations.

This step must be done by the IPAM account and management account
respectively. If you are using the AWS CLI to delete the RAM shares and disable
RAM integration, use the `--profile
 `ipam-account`` and  `--profile
 `management-account`` options. 6. Run the following command to deprovision the Regional pool CIDR.

This step must be done by the IPAM account.

```
aws ec2 deprovision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --cidr `2605:9cc0:409::/48` --profile `ipam-account`

```

In the output, you'll see the CIDR pending deprovision.

```
{
    "IpamPoolCidr": {
        "Cidr": "2605:9cc0:409::/48",
        "State": "pending-deprovision"
    }
}
```

Deprovisioning takes time to complete. Continue to run the command until you see the CIDR state **deprovisioned**.

```
aws ec2 get-ipam-pool-cidrs --region `us-east-1` --ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --cidr `2605:9cc0:409::/48` --profile `ipam-account`

```

In the output, you'll see the CIDR pending deprovision.

```
{
    "IpamPoolCidr": {
        "Cidr": "2605:9cc0:409::/48",
        "State": "deprovisioned"
    }
}
```

7. Run the following command to delete the Regional pool.

This step must be done by the IPAM account.

```
aws ec2 delete-ipam-pool --region `us-east-1` --ipam-pool-id `ipam-pool-0053b7d2b4fc3f730` --profile `ipam-account`

```

In the output, you can see the delete state.

```
{
    "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-0053b7d2b4fc3f730",
        "SourceIpamPoolId": "ipam-pool-07f2466c7158b50c4",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0053b7d2b4fc3f730",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "Locale": "us-east-1",
        "PoolDepth": 2,
        "State": "delete-in-progress",
        "Description": "reg-ipv6-pool",
        "AutoImport": false,
        "Advertisable": true,
        "AddressFamily": "ipv6"
    }
}
```

8. Run the following command to deprovision the top-level pool CIDR.

This step must be done by the IPAM account.

```
aws ec2 deprovision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-07f2466c7158b50c4` --cidr `2605:9cc0:409::/48` --profile `ipam-account`

```

In the output, you'll see the CIDR pending deprovision.

```
{
    "IpamPoolCidr": {
        "Cidr": "2605:9cc0:409::/48",
        "State": "pending-deprovision"
    }
}
```

Deprovisioning takes time to complete. Run the following command to check the status of deprovisioning.

```
aws ec2 get-ipam-pool-cidrs --region `us-east-1` --ipam-pool-id `ipam-pool-07f2466c7158b50c4` --profile `ipam-account`
```

Wait until you see **deprovisioned** before you continue to the next step.

```
{
    "IpamPoolCidr": {
        "Cidr": "2605:9cc0:409::/48",
        "State": "deprovisioned"
    }
}
```

9. Run the following command to delete the top-level pool.

This step must be done by the IPAM account.

```
aws ec2 delete-ipam-pool --region `us-east-1` --ipam-pool-id `ipam-pool-07f2466c7158b50c4` --profile `ipam-account`
```

In the output, you can see the delete state.

```
{
    "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-0053b7d2b4fc3f730",
        "SourceIpamPoolId": "ipam-pool-07f2466c7158b50c4",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0053b7d2b4fc3f730",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "Locale": "us-east-1",
        "PoolDepth": 2,
        "State": "delete-in-progress",
        "Description": "reg-ipv6-pool",
        "AutoImport": false,
        "Advertisable": true,
        "AddressFamily": "ipv6"
    }
}
```

10. Run the following command to delete the IPAM.

This step must be done by the IPAM account.

```
aws ec2 delete-ipam --region `us-east-1` --ipam-id `ipam-090e48e75758de279` --profile `ipam-account`
```

In the output, you'll see the IPAM response. This means that the IPAM was deleted.

```
{
    "Ipam": {
        "OwnerId": "123456789012",
        "IpamId": "ipam-090e48e75758de279",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "PublicDefaultScopeId": "ipam-scope-0087d83896280b594",
        "PrivateDefaultScopeId": "ipam-scope-08b70b04fbd524f8d",
        "ScopeCount": 2,
        "OperatingRegions": [
            {
                "RegionName": "us-east-1"
            },
            {
                "RegionName": "us-west-2"
            }
        ]
    }
}
```
