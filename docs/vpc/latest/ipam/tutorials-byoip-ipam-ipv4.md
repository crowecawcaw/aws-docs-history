# Bring your own public IPv4 CIDR to IPAM using only the AWS CLI

Follow these steps to bring an IPv4 CIDR to IPAM and allocate an Elastic IP address (EIP) with the CIDR using only the AWS CLI.

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
- [Step 2: Create an IPAM](#tutorials-byoip-ipam-ipv4-2 "#tutorials-byoip-ipam-ipv4-2")
- [Step 3: Create a top-level IPAM pool](#tutorials-byoip-ipam-ipv4-3 "#tutorials-byoip-ipam-ipv4-3")
- [Step 4: Provision a CIDR to the top-level pool](#tutorials-byoip-ipam-ipv4-4 "#tutorials-byoip-ipam-ipv4-4")
- [Step 5: Create a Regional pool within the
  top-level pool](#tutorials-byoip-ipam-ipv4-5 "#tutorials-byoip-ipam-ipv4-5")
- [Step 6: Provision a CIDR to the Regional pool](#tutorials-byoip-ipam-ipv4-6 "#tutorials-byoip-ipam-ipv4-6")
- [Step 7: Advertise the CIDR](#tutorials-byoip-ipam-ipv4-11 "#tutorials-byoip-ipam-ipv4-11")
- [Step 8: Share the Regional pool](#tutorials-byoip-ipam-ipv4-console-4-deux "#tutorials-byoip-ipam-ipv4-console-4-deux")
- [Step 9: Allocate an Elastic IP address
  from the pool](#tutorials-byoip-ipam-ipv4-console-cli-all-eip "#tutorials-byoip-ipam-ipv4-console-cli-all-eip")
- [Step 10: Associate the Elastic IP address with
  an EC2 instance](#tutorials-byoip-ipam-ipv4-console-cli-assoc-eip "#tutorials-byoip-ipam-ipv4-console-cli-assoc-eip")
- [Step 11: Cleanup](#tutorials-byoip-ipam-ipv4-cli-cleanup "#tutorials-byoip-ipam-ipv4-cli-cleanup")
- [Alternative to Step 9](#tutorials-byoip-ipam-ipv4-cli-alt "#tutorials-byoip-ipam-ipv4-cli-alt")

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

In the output, you'll see the IPAM you've created. Note the value for
`PublicDefaultScopeId`. You will need your public scope ID in the next
step. You are using the public scope because BYOIP CIDRs are public IP addresses, which
is what the public scope is meant for.

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

## Step 3: Create a top-level IPAM pool

Complete the steps in this section to create a top-level IPAM pool.

This step must be done by the IPAM account.

###### To create an IPv4 address pool for all of your AWS resources using the

AWS CLI

1. Run the following command to create an IPAM pool. Use the ID of the public
   scope of the IPAM that you created in the previous step.

This step must be done by the IPAM account.

```
aws ec2 create-ipam-pool --region `us-east-1` --ipam-scope-id `ipam-scope-0087d83896280b594` --description `"top-level-IPv4-pool"` --address-family `ipv4` --profile `ipam-account`
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
        "Locale": "None",
        "PoolDepth": 1,
        "State": "create-in-progress",
        "Description": "top-level-pool",
        "AutoImport": false,
        "AddressFamily": "ipv4",
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
    "IpamPools": [
        {
            "OwnerId": "123456789012",
            "IpamPoolId": "ipam-pool-0a03d430ca3f5c035",
            "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0a03d430ca3f5c035",
            "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
            "IpamScopeType": "public",
            "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
            "Locale": "None",
            "PoolDepth": 1,
            "State": "create-complete",
            "Description": "top-level-IPV4-pool",
            "AutoImport": false,
            "AddressFamily": "ipv4",
            "Tags": []
        }
    ]
}
```

## Step 4: Provision a CIDR to the top-level pool

Provision a CIDR block to the top-level pool. Note that when provisioning an IPv4 CIDR
to a pool within the top-level pool, the minimum IPv4 CIDR you can provision is
`/24`; more specific CIDRs (such as `/25`) are not
permitted.

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
ownership verification option.

This step must be done by the IPAM account.

###### Important

You only need to verify domain control when you provision the BYOIP CIDR to the
top-level pool. For the Regional pool within the top-level pool, you can omit the
domain control option. Once you onboard your BYOIP to IPAM, you are not required to
perform ownership validation when you divide the BYOIP across Regions and
accounts.

###### To provision a CIDR block to the pool using the AWS CLI

1. To provision the CIDR with certificate information, use the following command
   example. In addition to replacing the values as needed in the example, ensure
   that you replace `Message` and `Signature` values with the
   `text_message` and `signed_message` values that you
   got in [Verify your domain with an X.509 certificate](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert").

```
aws ec2 provision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-0a03d430ca3f5c035` --cidr `130.137.245.0/24` --verification-method remarks-x509 --cidr-authorization-context Message="`1|aws|470889052444|130.137.245.0/24|20250101|SHA256|RSAPSS`",Signature="`W3gdQ9PZHLjPmrnGM~cvGx~KCIsMaU0P7ENO7VRnfSuf9NuJU5RUveQzus~QmF~Nx42j3z7d65uyZZiDRX7KMdW4KadaLiClyRXN6ps9ArwiUWSp9yHM~U-hApR89Kt6GxRYOdRaNx8yt-uoZWzxct2yIhWngy-du9pnEHBOX6WhoGYjWszPw0iV4cmaAX9DuMs8ASR83K127VvcBcRXElT5URr3gWEB1CQe3rmuyQk~gAdbXiDN-94-oS9AZlafBbrFxRjFWRCTJhc7Cg3ASbRO-VWNci-C~bWAPczbX3wPQSjtWGV3k1bGuD26ohUc02o8oJZQyYXRpgqcWGVJdQ__`" --profile `ipam-account`
```

To provision the CIDR with verification token information, use the following
command example. In addition to replacing the values as needed in the example,
ensure that you replace `ipam-ext-res-ver-token-0309ce7f67a768cf0`
with the `IpamExternalResourceVerificationTokenId` token ID that you
got in [Verify your domain with a DNS TXT record](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt").

```
aws ec2 provision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-0a03d430ca3f5c035` --cidr `130.137.245.0/24` --verification-method dns-token --ipam-external-resource-verification-token-id `ipam-ext-res-ver-token-0309ce7f67a768cf0` --profile `ipam-account`
```

In the output, you'll see the CIDR pending provision.

```
{
    "IpamPoolCidr": {
        "Cidr": "130.137.245.0/24",
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
aws ec2 get-ipam-pool-cidrs --region `us-east-1` --ipam-pool-id `ipam-pool-0a03d430ca3f5c035` --profile `ipam-account`
```

The following example output shows the state.

```
{
    "IpamPoolCidrs": [
        {
            "Cidr": "130.137.245.0/24",
            "State": "provisioned"
        }
    ]
}
```

## Step 5: Create a Regional pool within the

top-level pool

Create a Regional pool within the top-level pool.

The locale for the pool should be one of the following:

- An AWS Region where you want this IPAM pool to be available for allocations.
- The network border group for an AWS Local Zone where you want this IPAM pool to be available for allocations ([supported Local Zones](../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-zone-avail "../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-zone-avail")). This option is only available for IPAM IPv4 pools in the public scope.
- An [AWS Dedicated Local Zone](https://aws.amazon.com/dedicatedlocalzones/ "https://aws.amazon.com/dedicatedlocalzones/"). To create a pool within an AWS Dedicated Local Zone, enter the AWS Dedicated Local Zone in the selector input.
- `Global` when you want to use IP addresses globally across all AWS Regions, such as CloudFront locations. The `Global` locale is only available for public IPv4 pools.

For example, you can only allocate a CIDR for a VPC from an IPAM pool that shares a locale with the VPC’s Region. Note that when you have chosen a locale for a pool, you cannot modify it. If the home Region of the IPAM is unavailable due to an outage and the pool has a locale different than the home Region of the IPAM, the pool can still be used to allocate IP addresses.

When you run the commands in this section, the value for `--region` must
include the `--locale` option you entered when you created the pool that will
be used for the BYOIP CIDR. For example, if you created the BYOIP pool with a locale of
_us-east-1_, the `--region` should be
_us-east-1_. If you created the BYOIP pool with a
locale of _us-east-1-scl-1_ (a network border group
used for Local Zones), the `--region` should be _us-east-1_ because that Region manages the locale _us-east-1-scl-1_.

This step must be done by the IPAM account.

Choosing a locale ensures there are no
cross-region dependencies between your pool and the resources allocating from
it. The available options come from the operating Regions that you chose when
you created your IPAM. In this tutorial, we'll use `us-west-2` as the
locale for the Regional pool.

###### Important

When you create the pool, you must include `--aws-service ec2`. The service you select determines the AWS service where the CIDR will be advertisable. Currently, the only option is `ec2`, which means that the CIDRs allocated from this pool will be advertisable for the Amazon EC2 service (for Elastic IP addresses) and the Amazon VPC service (for CIDRs associated with VPCs).

###### To create a Regional pool using the

AWS CLI

1. Run the following command to create the pool.

```
aws ec2 create-ipam-pool --description `"Regional-IPv4-pool"` --region `us-east-1` --ipam-scope-id `ipam-scope-0087d83896280b594` --source-ipam-pool-id `ipam-pool-0a03d430ca3f5c035` --locale `us-west-2` --address-family `ipv4` --aws-service ec2 --profile `ipam-account`

```

In the output, you'll see IPAM creating the pool.

```
{
     "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-0d8f3646b61ca5987",
        "SourceIpamPoolId": "ipam-pool-0a03d430ca3f5c035",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0d8f3646b61ca5987",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "Locale": "us-west-2",
        "PoolDepth": 2,
        "State": "create-in-progress",
        "Description": "Regional--pool",
        "AutoImport": false,
        "AddressFamily": "ipv4",
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

Provision a CIDR block to the Regional pool.

###### Note

When provisioning a CIDR to a Regional pool within the top-level pool, the
most specific IPv4 CIDR you can provision is `/24`; more specific
CIDRs (such as `/25`) are not permitted. After you create the
Regional pool, you can create smaller pools (such as `/25`)
within the same Regional pool. Note that if you share the Regional pool or
pools within it, these pools can only be used in the locale set on the same
Regional pool.

This step must be done by the IPAM account.

###### To assign a CIDR block to the Regional pool using the AWS CLI

1. Run the following command to provision the CIDR.

```
aws ec2 provision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987` --cidr `130.137.245.0/24` --profile `ipam-account`
```

In the output, you'll see the CIDR pending provision.

```
{
    "IpamPoolCidr": {
        "Cidr": "130.137.245.0/24",
        "State": "pending-provision"
    }
}
```

2. Run the following command until you see the state of `provisioned`
   in the output.

```
aws ec2 get-ipam-pool-cidrs --region `us-east-1` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987` --profile `ipam-account`
```

The following example output shows the correct state.

```
{
    "IpamPoolCidrs": [
        {
            "Cidr": "130.137.245.0/24",
            "State": "provisioned"
        }
    ]
}
```

## Step 7: Advertise the CIDR

The steps in this section must be done by the IPAM account. Once you associate the
Elastic IP address (EIP) with an instance or Elastic Load Balancer, you can then start
advertising the CIDR you brought to AWS that is in pool that has `--aws-service
 ec2` defined. In this tutorial, that's your Regional pool. By default the CIDR
is not advertised, which means it's not publicly accessible over the internet. When you
run the command in this section, the value for `--region` must match the
`--locale` option you entered when you created the pool that will be used
for the BYOIP CIDR.

This step must be done by the IPAM account.

###### Note

The advertisement status doesn't not restrict your ability to allocate Elastic IP addresses. Even if your
BYOIPv4 CIDR is not advertised, you can still can create EIPs from the IPAM pool.

###### Start advertising the CIDR using the AWS CLI

- Run the following command to advertise the CIDR.

```
aws ec2 advertise-byoip-cidr --region `us-west-2` --cidr `130.137.245.0/24` --profile `ipam-account`

```

In the output, you'll see the CIDR is advertised.

```
{
    "ByoipCidr": {
        "Cidr": "130.137.245.0/24",
        "State": "advertised"
    }
}
```

## Step 8: Share the Regional pool

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

## Step 9: Allocate an Elastic IP address

from the pool

Complete the steps in this section to allocate an Elastic IP address from the pool. Note that if
you are using public IPv4 pools to allocate Elastic IP addresses, you can use the
alternative steps in [Alternative to Step 9](#tutorials-byoip-ipam-ipv4-cli-alt "#tutorials-byoip-ipam-ipv4-cli-alt") rather than the steps
in this section.

###### Important

If you see an error related to not having permissions to call ec2:AllocateAddress,
the managed permission currently assigned to the IPAM pool that was shared with you
needs to be updated. Contact the person who created the resource share and ask them
to update the managed permission `AWSRAMPermissionIpamResourceDiscovery`
to the default version. For more information, see [Update a resource
share](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the _AWS RAM User Guide_ .

AWS Management Console
Follow the steps in [Allocate an Elastic IP address](../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-allocating "../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-allocating") in the _Amazon EC2 User Guide_
to allocate the address, but note the following:

- This step must be done by the member account.
- Ensure that the AWS Region you are in in the EC2 console matches the Locale option you chose
  when you created the Regional pool.
- When you choose the address pool, choose the option to **Allocate using an IPv4 IPAM
  pool** and choose the Regional pool you created.

Command line
Allocate an address from the pool with the [allocate-address](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html") command. The `--region` you use
must match the `-locale` option you chose when you created the
pool in Step 2. Include the ID of the IPAM pool you created in Step 2 in
`--ipam-pool-id`. Optionally, you can also choose a specific
`/32` in your IPAM pool by using the `--address`
option.

```
aws ec2 allocate-address --region `us-east-1` --ipam-pool-id `ipam-pool-07ccc86aa41bef7ce`
```

Example response:

```
{
    "PublicIp": "18.97.0.41",
    "AllocationId": "eipalloc-056cdd6019c0f4b46",
    "PublicIpv4Pool": "ipam-pool-07ccc86aa41bef7ce",
    "NetworkBorderGroup": "us-east-1",
    "Domain": "vpc"
}
```

For more information, see [Allocate an Elastic IP address](../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-allocating "../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-allocating") in the
_Amazon EC2 User Guide_.

## Step 10: Associate the Elastic IP address with

an EC2 instance

Complete the steps in this section to associate the Elastic IP address with an EC2
instance.

AWS Management Console
Follow the steps in [Associate an Elastic IP address](../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-associating "../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-associating") in the _Amazon EC2 User Guide_
to allocate an Elastic IP address from the IPAM pool, but note the following: When you
use AWS Management Console option, the AWS Region you associate the
Elastic IP address in must match the Locale option you chose when you created the
Regional pool.

This step must be done by the member account.

Command line
This step must be done by the member account. Use the `--profile `member-account`` option.

Associate the Elastic IP address with an instance with the [associate-address](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html") command. The `--region` you
associate the Elastic IP address in must match the `--locale` option you chose
when you created the Regional pool.

```
aws ec2 associate-address --region `us-east-1` --instance-id `i-07459a6fca5b35823` --public-ip `18.97.0.41`
```

Example response:

```
{
    "AssociationId": "eipassoc-06aa85073d3936e0e"
}
```

For more information, see [Associate an Elastic IP address with an instance or network interface](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-associating "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-associating") in the
_Amazon EC2 User Guide_.

## Step 11: Cleanup

Follow the steps in this section to clean up the resources you've provisioned and
created in this tutorial. When you run the commands in this section, the value for
`--region` must include the `--locale` option you entered when
you created the pool that will be used for the BYOIP CIDR.

###### Clean up using the AWS CLI

1. View the EIP allocation managed in IPAM.

This step must be done by the IPAM account.

```
aws ec2 get-ipam-pool-allocations --region `us-west-2` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987` --profile `ipam-account`
```

The output shows the allocation in IPAM.

```
{
    "IpamPoolAllocations": [
        {
            "Cidr": "130.137.245.0/24",
            "IpamPoolAllocationId": "ipam-pool-alloc-5dedc8e7937c4261b56dc3e3eb53dc45",
            "ResourceId": "ipv4pool-ec2-0019eed22a684e0b2",
            "ResourceType": "ec2-public-ipv4-pool",
            "ResourceOwner": "123456789012"
        }
    ]
}
```

2. Stop advertising the IPv4 CIDR.

This step must be done by the IPAM account.

```
aws ec2 withdraw-byoip-cidr --region `us-west-2` --cidr `130.137.245.0/24` --profile `ipam-account`
```

In the output, you'll see the CIDR State has changed from **advertised** to **provisioned**.

```
{
    "ByoipCidr": {
        "Cidr": "130.137.245.0/24",
        "State": "provisioned"
    }
}
```

3. Release the Elastic IP address.

This step must be done by the member account.

```
aws ec2 release-address --region `us-west-2` --allocation-id `eipalloc-0db3405026756dbf6` --profile `member-account`
```

You will not see any output when you run this command. 4. View the EIP allocation is no longer managed in IPAM. It can take some
time for IPAM to discover that the Elastic IP address has been removed. You
cannot continue to clean up and deprovision the IPAM pool CIDR until you see
that the allocation has been removed from IPAM. When you run the command in this
section, the value for `--region` must include the `--locale` option
you entered when you created the pool that will be used for the BYOIP
CIDR.

This step must be done by the IPAM account.

```
aws ec2 get-ipam-pool-allocations --region `us-west-2` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987` --profile `ipam-account`

```

The output shows the allocation in IPAM.

```
{
    "IpamPoolAllocations": []
}
```

5. Deprovision the Regional pool CIDR. When you
   run the commands in this step, the value for `--region` must match
   the Region of your IPAM.

This step must be done by the IPAM account.

```
aws ec2 deprovision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987` --cidr `130.137.245.0/24` --profile `ipam-account`
```

In the output, you'll see the CIDR pending deprovision.

```
{
    "IpamPoolCidr": {
        "Cidr": "130.137.245.0/24",
        "State": "pending-deprovision"
    }
}
```

Deprovisioning takes time to complete. Check the status of deprovisioning.

```
aws ec2 get-ipam-pool-cidrs --region `us-east-1` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987` --profile `ipam-account`

```

Wait until you see **deprovisioned** before you continue to the next step.

```
{
    "IpamPoolCidr": {
        "Cidr": "130.137.245.0/24",
        "State": "deprovisioned"
    }
}
```

6. Delete the RAM shares and disable RAM integration with AWS
   Organizations. Complete the steps in [Deleting a resource
   share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-delete.md "../../../ram/latest/userguide/working-with-sharing-delete.md") and [Disabling
   resource sharing with AWS Organizations](../../../ram/latest/userguide/security-disable-sharing-with-orgs.md "../../../ram/latest/userguide/security-disable-sharing-with-orgs.md") in the _AWS RAM User Guide_, in that order, to delete the
   RAM shares and disable RAM integration with AWS Organizations.

This step must be done by the IPAM account and management account
respectively. If you are using the AWS CLI to delete the RAM shares and disable
RAM integration, use the `--profile
 `ipam-account`` and  `--profile
 `management-account`` options. 7. Delete the Regional pool. When you run the
command in this step, the value for `--region` must match the Region
of your IPAM.

This step must be done by the IPAM account.

```
aws ec2 delete-ipam-pool --region `us-east-1` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987` --profile `ipam-account`

```

In the output, you can see the delete state.

```
{
   "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-0d8f3646b61ca5987",
        "SourceIpamPoolId": "ipam-pool-0a03d430ca3f5c035",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0d8f3646b61ca5987",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0087d83896280b594",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-090e48e75758de279",
        "Locale": "us-east-1",
        "PoolDepth": 2,
        "State": "delete-in-progress",
        "Description": "reg-ipv4-pool",
        "AutoImport": false,
        "Advertisable": true,
        "AddressFamily": "ipv4"
    }
}
```

8. Deprovision the top-level pool CIDR. When you
   run the commands in this step, the value for `--region` must match
   the Region of your IPAM.

This step must be done by the IPAM account.

```
aws ec2 deprovision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-0a03d430ca3f5c035` --cidr `130.137.245.0/24` --profile `ipam-account`
```

In the output, you'll see the CIDR pending deprovision.

```
{
    "IpamPoolCidr": {
        "Cidr": "130.137.245.0/24",
        "State": "pending-deprovision"
    }
}
```

Deprovisioning takes time to complete. Run the following command to check the status of deprovisioning.

```
aws ec2 get-ipam-pool-cidrs --region `us-east-1` --ipam-pool-id `ipam-pool-0a03d430ca3f5c035` --profile `ipam-account`

```

Wait until you see **deprovisioned** before you continue to the next step.

```
{
    "IpamPoolCidr": {
        "Cidr": "130.137.245.0/24",
        "State": "deprovisioned"
    }
}
```

9. Delete the top-level pool. When you run the
   command in this step, the value for `--region` must match the Region
   of your IPAM.

This step must be done by the IPAM account.

```
aws ec2 delete-ipam-pool --region `us-east-1` --ipam-pool-id `ipam-pool-0a03d430ca3f5c035` --profile `ipam-account`

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
        "AddressFamily": "ipv4"
    }
}
```

10. Delete the IPAM. When you run the command in
    this step, the value for `--region` must match the Region of your
    IPAM.

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
        ],
    }
}
```

## Alternative to Step 9

If you are using public IPv4 pools to allocate Elastic IP addresses, you can use the
steps in this section rather than the steps in [Step 9: Allocate an Elastic IP address
from the pool](#tutorials-byoip-ipam-ipv4-console-cli-all-eip "#tutorials-byoip-ipam-ipv4-console-cli-all-eip").

###### Contents

- [Step 1: Create a public IPv4 pool](#tutorials-byoip-ipam-ipv4-9 "#tutorials-byoip-ipam-ipv4-9")
- [Step 2: Provision the public IPv4 CIDR to your public IPv4 pool](#tutorials-byoip-ipam-ipv4-9 "#tutorials-byoip-ipam-ipv4-9")
- [Step 3: Create an Elastic IP address from the public
  IPv4 pool](#tutorials-byoip-ipam-ipv4-10 "#tutorials-byoip-ipam-ipv4-10")
- [Alternative to Step 9 cleanup](#tutorials-byoip-ipam-ipv4-cli-alt-cleanup "#tutorials-byoip-ipam-ipv4-cli-alt-cleanup")

### Step 1: Create a public IPv4 pool

This step would typically be done by a different AWS account which wants to
provision an Elastic IP address, such as the member account.

###### Important

Public IPv4 pools and IPAM pools are managed by distinct resources in AWS. Public IPv4 pools are single account resources
that enable you to convert your publicly-owned CIDRs to Elastic IP addresses. IPAM pools can be used to allocate your public space
to public IPv4 pools.

###### To create a public IPv4 pool using the AWS CLI

- Run the following command to provision the CIDR. When you run the
  command in this section, the value for `--region` must match the
  `--locale` option you entered when you created the pool that will
  be used for the BYOIP CIDR.

```
aws ec2 create-public-ipv4-pool --region `us-west-2` --profile `member-account`
```

In the output, you'll see the public IPv4 pool ID. You will need this
ID in the next step.

```
{
    "PoolId": "ipv4pool-ec2-0019eed22a684e0b2"
}
```

### Step 2: Provision the public IPv4 CIDR to your public IPv4 pool

Provision the public IPv4 CIDR to your public IPv4 pool. The value for
`--region` must match the `--locale` value you entered when
you created the pool that will be used for the BYOIP CIDR. The least specific
`--netmask-length` you can define is `24`.

This step must be done by the member account.

###### To create a public IPv4 pool using the AWS CLI

1. Run the following command to provision the CIDR.

```
aws ec2 provision-public-ipv4-pool-cidr --region `us-west-2` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987` --pool-id `ipv4pool-ec2-0019eed22a684e0b2` --netmask-length `24` --profile `member-account`
```

In the output, you'll see the provisioned CIDR.

```
{
    "PoolId": "ipv4pool-ec2-0019eed22a684e0b2",
    "PoolAddressRange": {
        "FirstAddress": "130.137.245.0",
        "LastAddress": "130.137.245.255",
        "AddressCount": 256,
        "AvailableAddressCount": 256
    }
}
```

2. Run the following command to view the CIDR provisioned in the public IPv4 pool.

```
aws ec2 describe-byoip-cidrs --region `us-west-2` --max-results `10` --profile `member-account`
```

In the output, you'll see the provisioned CIDR. By default the CIDR is
not advertised, which means it's not publicly accessible over the internet.
You will have the chance to set this CIDR to advertised in the last step of
this tutorial.

```
{
    "ByoipCidrs": [
        {
            "Cidr": "130.137.245.0/24",
            "StatusMessage": "Cidr successfully provisioned",
            "State": "provisioned"
        }
    ]
}
```

### Step 3: Create an Elastic IP address from the public

IPv4 pool

Create an Elastic IP address (EIP) from the public IPv4 pool. When you run the
commands in this section, the value for `--region` must match the
`--locale` option you entered when you created the pool that will be used
for the BYOIP CIDR.

This step must be done by the member account.

###### To create an EIP from the public IPv4 pool using the AWS CLI

1. Run the following command to create the EIP.

```
aws ec2 allocate-address  --region `us-west-2` --public-ipv4-pool `ipv4pool-ec2-0019eed22a684e0b2` --profile `member-account`
```

In the output, you'll see the allocation.

```
{
    "PublicIp": "130.137.245.100",
    "AllocationId": "eipalloc-0db3405026756dbf6",
    "PublicIpv4Pool": "ipv4pool-ec2-0019eed22a684e0b2",
    "NetworkBorderGroup": "us-east-1",
    "Domain": "vpc"
}
```

2. Run the following command to view the EIP allocation managed in IPAM.

This step must be done by the IPAM account.

```
aws ec2 get-ipam-pool-allocations --region `us-west-2` --ipam-pool-id `ipam-pool-0d8f3646b61ca5987` --profile `ipam-account`
```

The output shows the allocation in IPAM.

```
{
    "IpamPoolAllocations": [
        {
            "Cidr": "130.137.245.0/24",
            "IpamPoolAllocationId": "ipam-pool-alloc-5dedc8e7937c4261b56dc3e3eb53dc45",
            "ResourceId": "ipv4pool-ec2-0019eed22a684e0b2",
            "ResourceType": "ec2-public-ipv4-pool",
            "ResourceOwner": "123456789012"
        }
    ]
}
```

### Alternative to Step 9 cleanup

Complete these steps to clean up public IPv4 pools created with the alternative to Step 9. You should complete these steps after you release the Elastic IP address during the standard cleanup process in [Step 10: Cleanup](tutorials-byoip-ipam-ipv6.md#tutorials-byoip-ipam-ipv4-cleanup "tutorials-byoip-ipam-ipv6.md#tutorials-byoip-ipam-ipv4-cleanup").

1. View your BYOIP CIDRs.

This step must be done by the member account.

```
aws ec2 describe-public-ipv4-pools --region `us-west-2` --profile `member-account`
```

In the output, you'll see the IP addresses in your BYOIP CIDR.

```
{
    "PublicIpv4Pools": [
        {
            "PoolId": "ipv4pool-ec2-0019eed22a684e0b2",
            "Description": "",
            "PoolAddressRanges": [
                {
                    "FirstAddress": "130.137.245.0",
                    "LastAddress": "130.137.245.255",
                    "AddressCount": 256,
                    "AvailableAddressCount": 256
                }
            ],
            "TotalAddressCount": 256,
            "TotalAvailableAddressCount": 256,
            "NetworkBorderGroup": "us-east-1",
            "Tags": []
        }
    ]
}
```

2. Release the CIDR from the public IPv4 pool. When you run the command in
   this section, the value for `--region` must match the Region of
   your IPAM.

This step must be done by the member account.

```
aws ec2 deprovision-public-ipv4-pool-cidr --region `us-east-1` --pool-id `ipv4pool-ec2-0019eed22a684e0b2` --cidr `130.137.245.0/24` --profile `member-account`
```

3. View your BYOIP CIDRs again and ensure there are no more provisioned
   addresses. When you run the command in this section, the value for
   `--region` must match the Region of your IPAM.

This step must be done by the member account.

```
aws ec2 describe-public-ipv4-pools --region `us-east-1` --profile `member-account`
```

In the output, you'll see the IP addresses count in your public IPv4 pool.

```
{
    "PublicIpv4Pools": [
        {
            "PoolId": "ipv4pool-ec2-0019eed22a684e0b2",
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
