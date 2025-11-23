# Allocate sequential Elastic IP addresses from an IPAM pool

IPAM enables you to provision Amazon-owned public IPv4 blocks to IPAM pools and allocate
sequential [Elastic IP addresses](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md") from those
pools to AWS resources.

Contiguously-allocated Elastic IP addresses are public IPv4 addresses that are allocated sequentially.
For example, if Amazon provides you a public IPv4 CIDR block of `192.0.2.0/30` and
you allocate the four available public IPv4 addresses from that CIDR block, an example of
four sequential Elastic IP addresses is `192.0.2.0`, `192.0.2.1`,
`192.0.2.2`, and `192.0.2.3`.

Contiguously-allocated Elastic IP addresses enable you to simplify your security and networking rules in
the following ways:

- **Security administration**: Using sequential IPv4 addresses
  reduces your firewall management overhead. You can add an entire prefix with a
  single rule and associate IPs from the same prefix as you scale, saving time and
  effort.
- **Enterprise access**: You can simplify the address space shared
  with your clients by using an entire CIDR block instead of a long list of individual
  public IPv4 addresses. This avoids the need to constantly communicate IP changes as
  your application scales on AWS.
- **Simplified IP management**: Using sequential IPv4 addresses
  simplifies public IP management for your central networking team, as it reduces the
  need to track individual public IPs and instead allows them to focus on a limited
  number of IP prefixes.
  In this tutorial, you'll go through the steps required to allocate sequential Elastic IP addresses from
  an IPAM pool. You'll create an IPAM pool with an Amazon-provided contiguous public IPv4
  CIDR block, allocate Elastic IP addresses from the pool, and learn how to monitor IPAM pool
  allocations.

###### Note

- There are charges associated with provisioning Amazon-owned public IPv4 CIDR
  blocks. For more information, see the **Amazon-provided contiguous IPv4 block** tab on the [Amazon VPC pricing page](https://aws.amazon.com//vpc/pricing/ "https://aws.amazon.com//vpc/pricing/").
- This tutorial assumes you want to create an IPAM [using IPAM with a single account](enable-single-user-ipam.md "enable-single-user-ipam.md").
  If you want to share Amazon-owned contiguous public IPv4 blocks across accounts,
  first [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md "enable-integ-ipam.md") and
  then [Share an IPAM pool using AWS RAM](share-pool-ipam.md "share-pool-ipam.md"). If you
  integrate with AWS Organizations, you have the option to create a [service
  control policy](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") to prevent deprovisioning of the contig IPv4 blocks
  assigned to the pool.
- You cannot [transfer](../userguide/WorkWithEIPs.md#transfer-EIPs-intro "../userguide/WorkWithEIPs.md#transfer-EIPs-intro") sequential Elastic IP addresses allocated from an IPAM pool to other
  AWS accounts. Instead, IPAM allows you to share IPAM pools across AWS
  accounts by integrating IPAM with AWS Organizations (as mentioned
  above).
- There are limits on the number of Amazon-owned public IPv4 CIDR blocks you can
  provision and their size. For more information, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").

###### Contents

- [Step 1: Create an IPAM](#tutorials-eip-pool-1 "#tutorials-eip-pool-1")
- [Step 2: Create an IPAM pool and provision a
  CIDR](#tutorials-eip-pool-2 "#tutorials-eip-pool-2")
- [Step 3: Allocate an Elastic IP address from the pool](#tutorials-eip-pool-3 "#tutorials-eip-pool-3")
- [Step 4: Associate the Elastic IP address with an EC2
  instance](#tutorials-eip-pool-4 "#tutorials-eip-pool-4")
- [Step 5: Track and monitor pool usage](#track-monitor-eips-ipam "#track-monitor-eips-ipam")
- [Cleanup](#tutorials-eip-pool-cleanup "#tutorials-eip-pool-cleanup")

## Step 1: Create an IPAM

Complete the steps in this section to create an IPAM.

AWS Management Console

###### To create an IPAM

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the AWS Management Console, choose the AWS Region in
   which you want to create the IPAM. Create the IPAM in your main
   Region of operations.
3. On the service home page, choose **Create
   IPAM**.
4. Select **Allow Amazon VPC IP Address
   Manager to replicate data from source account(s) into the
   IPAM delegate account**. If you do not select this
   option, you cannot create an IPAM.
5. Choose an **IPAM tier**. For more information
   about the features available in each tier and the costs
   associated with the tiers, see the IPAM tab on the [Amazon VPC pricing
   page](https://aws.amazon.com//vpc/pricing/ "https://aws.amazon.com//vpc/pricing/").
6. Under **Operating regions**, select the AWS
   Regions in which this IPAM can manage and discover resources.
   The AWS Region in which you are creating your IPAM is selected
   as one of the operating Regions by default. For example, if
   you’re creating this IPAM in AWS Region `us-east-1`
   but you want to create Regional IPAM pools later that provide
   CIDRs to VPCs in `us-west-2`, select
   `us-west-2` here. If you forget an operating
   Region, you can return at a later time and edit your IPAM
   settings.

###### Note

If you are creating an IPAM in the Free Tier, you can
select multiple operating Regions for your IPAM, but the
only IPAM feature that will be available across operating
Regions is [Public IP
insights](view-public-ip-insights.md "view-public-ip-insights.md"). You cannot use other features in the
Free Tier, like BYOIP, across the IPAM's operating Regions.
You can only use them in the IPAM's home Region. To use all
IPAM features across operating Regions, [create an IPAM in the Advanced
Tier](mod-ipam-tier.md "mod-ipam-tier.md"). 7. Choose **Create IPAM**.

Command line
The commands in this section link to the AWS CLI Reference
documentation. The documentation provides detailed descriptions of the
options that you can use when you run the commands.

Create the IPAM with the [create-ipam](../../../cli/latest/reference/ec2/create-ipam.md "../../../cli/latest/reference/ec2/create-ipam.md")
command:

```
aws ec2 create-ipam --region `us-east-1`
```

Example response:

```
{
    "Ipam": {
        "OwnerId": "320805250157",
        "IpamId": "ipam-0755477df834ea06b",
        "IpamArn": "arn:aws:ec2::320805250157:ipam/ipam-0755477df834ea06b",
        "IpamRegion": "us-east-1",
        "PublicDefaultScopeId": "ipam-scope-01bc7290e4a9202f9",
        "PrivateDefaultScopeId": "ipam-scope-0a50983b97a7a583a",
        "ScopeCount": 2,
        "OperatingRegions": [
            {
                "RegionName": "us-east-1"
            }
        ],
        "State": "create-in-progress",
        "Tags": [],
        "DefaultResourceDiscoveryId": "ipam-res-disco-02cc5b34cc3f04f09",
        "DefaultResourceDiscoveryAssociationId": "ipam-res-disco-assoc-06b3a4dccfc81f7c1",
        "ResourceDiscoveryAssociationCount": 1,
        "Tier": "advanced"
    }
}

```

You'll need the PublicDefaultScopeId in the next step. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").

## Step 2: Create an IPAM pool and provision a

CIDR

Complete the steps in this section to create an IPAM pool from which you'll allocate
the Elastic IP addresses.

AWS Management Console

###### To create a pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. Choose the public scope. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. Choose **Create pool**.
5. (Optional) Add a **Name tag** for the pool and a
   **Description** for the pool.
6. Under **Source**, choose **IPAM
   scope**.
7. Under **Address family**, choose
   **IPv4**.
8. Under **Resource planning**, leave **Plan IP space
   within the scope** selected.
9. Under **Locale**, choose the locale for the pool. The locale
   is the AWS Region where you want this IPAM pool to be available for
   allocations. The available options come from the operating Regions that you
   chose when you created your IPAM.
10. Under **Service**, choose **EC2 (EIP/VPC)**.
    The service you select determines the AWS service where the CIDR will
    advertised. Currently, the only option is **EC2 (EIP/VPC)**,
    which means that the CIDRs allocated from this pool will be advertised for the
    Amazon EC2 service (for Elastic IP addresses).
11. Under **Public IP source**, choose
    **Amazon-owned**.
12. Under **CIDR to provision**, choose **Add
    Amazon-owned public CIDR**. Choose a **Netmask**
    length between `/29` (8 IP addresses) and `/30` (4 IP
    addresses). You can add up to 2 CIDRs by default. For information about
    increasing the limits on Amazon-provided contiguous public IPv4 CIDRs, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").
13. Leave **Configure this pool's allocation rule settings**
    unselected.
14. (Optional) Choose **Tags** for the pool.
15. Choose **Create pool**.

Ensure that this CIDR has been provisioned before you continue. You can see the state
of provisioning in the **CIDRs** tab in the pool details page.

Command line

###### To create a pool

1. Create an IPAM pool with the [create-ipam-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam-pool.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam-pool.html") command. The locale is the AWS
   Region where you want this IPAM pool to be available for
   allocations. The available options come from the operating Regions
   that you chose when you created your IPAM.

```
aws ec2 create-ipam-pool --region `us-east-1` --ipam-scope-id `ipam-scope-01bc7290e4a9202f9` --address-family ipv4 --locale `us-east-1` --aws-service ec2 --public-ip-source amazon
```

Example response with state
`create-in-progress`:

```
{
    "IpamPool": {
        "OwnerId": "320805250157",
        "IpamPoolId": "ipam-pool-07ccc86aa41bef7ce",
        "IpamPoolArn": "arn:aws:ec2::320805250157:ipam-pool/ipam-pool-07ccc86aa41bef7ce",
        "IpamScopeArn": "arn:aws:ec2::320805250157:ipam-scope/ipam-scope-01bc7290e4a9202f9",
        "IpamScopeType": "public",
        "IpamArn": "arn:aws:ec2::320805250157:ipam/ipam-0755477df834ea06b",
        "IpamRegion": "us-east-1",
        "Locale": "us-east-1",
        "PoolDepth": 1,
        "State": "create-in-progress",
        "AutoImport": false,
        "AddressFamily": "ipv4",
        "Tags": [],
        "AwsService": "ec2",
        "PublicIpSource": "amazon"
    }
}
```

2. Check that the pool was created successfully with the [describe-ipam-pools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-pools.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-pools.html") command.

```
aws ec2 describe-ipam-pools --region `us-east-1` --ipam-pool-ids `ipam-pool-07ccc86aa41bef7ce`
```

Example response with state `create-complete`:

```
{
    "IpamPools": [
        {
            "OwnerId": "320805250157",
            "IpamPoolId": "ipam-pool-07ccc86aa41bef7ce",
            "IpamPoolArn": "arn:aws:ec2::320805250157:ipam-pool/ipam-pool-07ccc86aa41bef7ce",
            "IpamScopeArn": "arn:aws:ec2::320805250157:ipam-scope/ipam-scope-01bc7290e4a9202f9",
            "IpamScopeType": "public",
            "IpamArn": "arn:aws:ec2::320805250157:ipam/ipam-0755477df834ea06b",
            "IpamRegion": "us-east-1",
            "Locale": "us-east-1",
            "PoolDepth": 1,
            "State": "create-complete",
            "AutoImport": false,
            "AddressFamily": "ipv4",
            "Tags": [],
            "AwsService": "ec2",
            "PublicIpSource": "amazon"
        }
    ]
}
```

3. Provision a CIDR to the pool with the [provision-ipam-pool-cidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/provision-ipam-pool-cidr.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/provision-ipam-pool-cidr.html") command. Choose a
   `--netmask-length` between
   `/29` (8 IP addresses) and `/30` (4 IP
   addresses). You can add up to 2 CIDRs by default. For information
   about increasing the limits on Amazon-provided contiguous public
   IPv4 CIDRs, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").

```
aws ec2 provision-ipam-pool-cidr --region `us-east-1` --ipam-pool-id `ipam-pool-07ccc86aa41bef7ce` --netmask-length `29`
```

Example response with state `pending-provision`:

```
{
    "IpamPoolCidr": {
        "State": "pending-provision",
        "IpamPoolCidrId": "ipam-pool-cidr-01856e43994df4913b7bc6aac47adf983",
        "NetmaskLength": 29
    }
}
```

4. Ensure that this CIDR has been provisioned before you continue. You can view the state
   of provisioning using the [get-ipam-pool-cidrs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ipam-pool-cidrs.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ipam-pool-cidrs.html") command.

```
aws ec2 get-ipam-pool-cidrs --region `us-east-1` --ipam-pool-id `ipam-pool-07ccc86aa41bef7ce`
```

Example response with state `provisioned`:

```
{
    "IpamPoolCidrs": [
        {
            "Cidr": "18.97.0.40/29",
            "State": "provisioned",
            "IpamPoolCidrId": "ipam-pool-cidr-01856e43994df4913b7bc6aac47adf983",
            "NetmaskLength": 29
        }
    ]
}
```

## Step 3: Allocate an Elastic IP address from the pool

Complete the steps in this section to allocate an Elastic IP address from the pool.

AWS Management Console
Follow the steps in [Allocate an Elastic IP address](../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-allocating "../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-allocating") in the _Amazon EC2 User Guide_
to allocate the address, but note the following:

- Ensure that the AWS Region you are in in the EC2 console matches the Locale option you chose
  when you created the pool in Step 2.
- When you choose the address pool, choose the option to **Allocate using an IPv4 IPAM
  pool** and choose the pool you created in Step

1.

Command line
Allocate an address from the pool with the [allocate-address](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html") command. The `--region` you use
must match the `-locale` option you chose when you created the
pool in Step 2. Include the ID of the IPAM pool you created in Step 2 in
`--ipam-pool-id`.

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

Optionally, you can also choose a specific `/32` in your IPAM pool by using the `--address` option.

```
aws ec2 allocate-address --region `us-east-1` --ipam-pool-id `ipam-pool-07ccc86aa41bef7ce` --address `18.97.0.41`
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

## Step 4: Associate the Elastic IP address with an EC2

instance

Complete the steps in this section to associate the Elastic IP address with an EC2
instance.

AWS Management Console
Follow the steps in [Associate an Elastic IP address](../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-associating "../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-associating") in the
_Amazon EC2 User Guide_ to allocate an Elastic IP address from the
IPAM pool, but note the following: When you use AWS Management Console
option, the AWS Region you associate the Elastic IP address in must match the
Locale option you chose when you created the pool in Step 2.

Command line
Associate the Elastic IP address with an instance with the [associate-address](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html") command. The `--region` you associate the
Elastic IP address in must match the `--locale` option you chose when you
created the pool in Step 2.

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

## Step 5: Track and monitor pool usage

Once you've allocated Elastic IP addresses from the IPAM pool, you can track and monitor IPAM pool
allocations.

AWS Management Console

- View the IPAM pool details **Allocations** tab in the IPAM
  console. Any Elastic IP addresses allocated from the IPAM pool have a **Resource
  Type** of **EIP**.
- Use [Public IP insights](view-public-ip-insights.md "view-public-ip-insights.md"):
  - Under **Public IP types**, filter by
    **Amazon-owned EIPs**. This shows the total number
    of public IPv4 addresses allocated to Amazon-owned Elastic IP addresses. If you filter
    by this measure and scroll to **Public IP addresses**
    at the bottom of the page, you'll see the Elastic IP addresses you've
    allocated.
  - Under **EIP usage**, filter by **Associated
    Amazon-owned EIPs** or **Unassociated Amazon-owned
    EIPs**. This shows the total number of Elastic IP addresses that you have
    allocated in your AWS account and that you have or have not associated
    with an EC2 instance, network interface, or AWS resource. If you
    filter by this measure and scroll to **Public IP
    addresses** at the bottom of the page, you'll see details
    about the filtered resources.
  - Under **Amazon-owned IPv4 contiguous IPs usage**,
    monitor sequential public IPv4 address usage over time and related
    Amazon-owned IPv4 IPAM pools.

- Use Amazon CloudWatch to track and monitor metrics related to Amazon-provided
  contiguous public IPv4 blocks that have been provisioned to IPAM pools. For the
  available metrics specific to contiguous IPv4 blocks, see **Public IP Metrics** under [IPAM metrics](cloudwatch-ipam-ip-address-usage.md "cloudwatch-ipam-ip-address-usage.md"). In addition to viewing
  metrics, you can create alarms in Amazon CloudWatch to notify you when thresholds are
  reached. Creating alarms and setting up notifications with Amazon CloudWatch is outside
  the scope of this tutorial. For more information, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in
  the _Amazon CloudWatch User Guide_.

Command line

- View the IPAM pool allocations with the [get-ipam-pool-allocations](../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md "../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md") command. Any Elastic IP addresses allocated
  from the IPAM pool have a **Resource Type** of
  **eip**.

```
aws ec2 get-ipam-pool-allocations --region `us-east-1` --ipam-pool-id `ipam-pool-07ccc86aa41bef7ce`
```

Example response:

```
{
     "IpamPoolAllocations": [
        {
            "Cidr": "18.97.0.40/32",
            "IpamPoolAllocationId": "ipam-pool-alloc-0bd07df786e8148aba2763e2b6c1c44bd",
            "ResourceId": "eipalloc-0c9decaa541d89aa9",
            "ResourceType": "eip",
            "ResourceRegion": "us-east-1",
            "ResourceOwner": "320805250157"
        }
    ]
}
```

- Use Amazon CloudWatch to track and monitor metrics related to
  Amazon-provided contiguous public IPv4 blocks that have been
  provisioned to IPAM pools. For the available metrics specific to
  contiguous IPv4 blocks, see **Public IP
  Metrics** under [IPAM metrics](cloudwatch-ipam-ip-address-usage.md "cloudwatch-ipam-ip-address-usage.md"). In addition
  to viewing metrics, you can create alarms in Amazon CloudWatch to notify you
  when thresholds are reached. Creating alarms and setting up
  notifications with Amazon CloudWatch is outside the scope of this tutorial.
  For more information, see [Using Amazon CloudWatch
  alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User
  Guide_.

The tutorial is now complete. You've created an IPAM pool with an Amazon-provided contiguous public IPv4
CIDR block, allocated Elastic IP addresses from the pool, and learned how to monitor IPAM pool
allocations. Continue to the next section to delete the resources you've created in this tutorial.

## Cleanup

Follow the steps in this section to clean up the resources you've created in this
tutorial.

**Step 1: Disassociate the Elastic IP address**

Complete the steps in [Disassociate an Elastic IP address](../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-associating-different "../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-associating-different") in the _Amazon EC2 User Guide_ to
disassociate the Elastic IP address.

**Step 2: Release the Elastic IP address**

Complete the steps in [Release an
Elastic IP address](../../../AWSEC2/latest/UserGuide/using-instance-addressing-eips-releasing.md "../../../AWSEC2/latest/UserGuide/using-instance-addressing-eips-releasing.md") in the _Amazon EC2 User Guide_ to release an Elastic IP address from
the public IPv4 pool.

**Step 3: Deprovision the CIDR from the IPAM
pool**

Complete the steps in [Deprovision CIDRs from a pool](depro-pool-cidr-ipam.md "depro-pool-cidr-ipam.md") to deprovision the Amazon-owned public CIDR
from the IPAM pool. This step is required for pool deletion. You will be billed for the
Amazon-provided contiguous IPv4 block until this step is complete.

**Step 4: Delete the IPAM pool**

Complete the steps in [Delete a pool](delete-pool-ipam.md "delete-pool-ipam.md") to delete the IPAM pool.

**Step 5: Delete the IPAM**

Complete the steps in [Delete an IPAM](delete-ipam.md "delete-ipam.md") to delete the IPAM.

The tutorial cleanup is complete.
