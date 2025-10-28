# Bring your own IPv4 CIDR to IPAM using both the AWS

Management Console and the AWS CLI

Follow these steps to bring an IPv4 CIDR to IPAM and allocate an Elastic IP address (EIP) using both the AWS
Management Console and the AWS CLI.

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
- [Step 2: Create a top-level IPAM pool](#tutorials-byoip-ipam-ipv4-console-create-top "#tutorials-byoip-ipam-ipv4-console-create-top")
- [Step 3. Create a Regional pool within the top-level pool](#tutorials-byoip-ipam-ipv4-console-create-reg "#tutorials-byoip-ipam-ipv4-console-create-reg")
- [Step 4: Advertise the CIDR](#tutorials-byoip-ipam-ipv4-console-adv "#tutorials-byoip-ipam-ipv4-console-adv")
- [Step 5. Share the Regional
  pool](#tutorials-byoip-ipam-ipv4-console-share-reg "#tutorials-byoip-ipam-ipv4-console-share-reg")
- [Step 6: Allocate an Elastic IP address
  from the pool](#tutorials-byoip-ipam-ipv4-console-all-eip "#tutorials-byoip-ipam-ipv4-console-all-eip")
- [Step 7: Associate the Elastic IP address with
  an EC2 instance](#tutorials-byoip-ipam-ipv4-console-assoc-eip "#tutorials-byoip-ipam-ipv4-console-assoc-eip")
- [Step 8: Cleanup](#tutorials-byoip-ipam-ipv4-console-cleanup "#tutorials-byoip-ipam-ipv4-console-cleanup")
- [Alternative to Step 6](#tutorials-byoip-ipam-ipv4-alt "#tutorials-byoip-ipam-ipv4-alt")

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

## Step 2: Create a top-level IPAM pool

Complete the steps in this section to create a top-level IPAM pool.

This step must be done by the IPAM account.

###### To create a pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, when you create a pool, the default private scope is selected.
   Choose the public scope. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. Choose **Create pool**.
5. (Optional) Add a **Name tag** for the pool and a **Description** for the pool.
6. Under **Source**, choose **IPAM
   scope**.
7. Under **Address family**, choose **IPv4**.
8. Under **Resource planning**, leave **Plan IP
   space within the scope** selected. For more information
   about using this option to plan for subnet IP space within a VPC, see
   [Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md "tutorials-subnet-planning.md").
9. Under **Locale**, choose **None**.

The IPAM integration with BYOIP requires that the locale is set on
whichever pool will be used for the BYOIP CIDR. Since we are going to create a top-level IPAM pool with a Regional pool within it,
and we’re going to allocate space to an Elastic IP address from the
Regional pool, you will set the locale on the Regional pool and not the top-level
pool. You’ll add the locale to the Regional pool when you create the Regional pool
in a later step.

###### Note

If you are creating a single pool only and not a top-level pool with Regional pools within it,
you would want to choose a Locale for this pool so that the pool is
available for allocations. 10. Under **Public IP source**, choose
**BYOIP**. 11. Under **CIDRs to provision**, do one of the following:

    * If you [verified
     your domain control with an X.509 certificate](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert"), you must include the
     CIDR and the BYOIP message and certificate signature that you created in that step so we can
     verify that you control the public space.
    * If you [verified your domain control with a DNS TXT record](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt"), you must
     include the CIDR and IPAM verification token that you created in that step so we can verify
     that you control the public space.

Note that when provisioning an IPv4 CIDR to a pool within the
top-level pool, the minimum IPv4 CIDR you can provision is
`/24`; more specific CIDRs (such as `/25`) are
not permitted.

###### Important

While most provisioning will be completed within two hours, it may take up
to one week to complete the provisioning process for publicly advertisable
ranges. 12. Leave **Configure this pool's allocation rule settings**
unselected. 13. (Optional) Choose **Tags** for the pool. 14. Choose **Create pool**.

Ensure that this CIDR has been provisioned before you continue. You can see the state of provisioning in the **CIDRs** tab in the pool details page.

## Step 3. Create a Regional pool within the top-level pool

Create a Regional pool within the top-level pool. The IPAM integration with BYOIP
requires that the locale is set on whichever pool will be used for the BYOIP CIDR.
You’ll add the locale to the Regional pool when you create the Regional pool in this
section. The `Locale` must be part of one of the operating Regions you
configured when you created the IPAM. For example, a locale of _us-east-1_ means that _us-east-1_ must
be an operating Region for the IPAM. A locale of _us-east-1-scl-1_ (a network border group used for Local Zones) means that
the IPAM must have an operating Region of _us-east-1_.

This step must be done by the IPAM account.

###### To create a Regional pool within a top-level pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, when you create a pool, the default private scope is selected. If you don’t want to use the default
   private scope, from the dropdown menu at the top of the content pane, choose the scope you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. Choose **Create pool**.
5. (Optional) Add a **Name tag** for the pool and a **Description** for the pool.
6. Under **Source**, choose the top-level pool that you created
   in the previous section.
7. Under **Resource planning**, leave **Plan IP
   space within the scope** selected. For more information
   about using this option to plan for subnet IP space within a VPC, see
   [Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md "tutorials-subnet-planning.md").
8. Under **Locale**, choose the locale for the pool. In this
   tutorial, we'll use `us-east-2` as the locale for the Regional pool. The available options come from
   the operating Regions that you chose when you created your IPAM.

The locale for the pool should be one of the following:

    * An AWS Region where you want this IPAM pool to be available for allocations.
    * The network border group for an AWS Local Zone where you want this IPAM pool to be available for allocations ([supported Local Zones](../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-zone-avail "../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-zone-avail")). This option is only available for IPAM IPv4 pools in the public scope.
    * An [AWS Dedicated Local Zone](https://aws.amazon.com/dedicatedlocalzones/ "https://aws.amazon.com/dedicatedlocalzones/"). To create a pool within an AWS Dedicated Local Zone, enter the AWS Dedicated Local Zone in the selector input.

For example, you can only allocate a CIDR for a VPC from an IPAM pool that shares a locale with the VPC’s Region. Note that when you have chosen a locale for a pool, you cannot modify it. If the home Region of the IPAM is unavailable due to an outage and the pool has a locale different than the home Region of the IPAM, the pool can still be used to allocate IP addresses.

Choosing a locale ensures there are no cross-region dependencies between your
pool and the resources allocating from it. 9. Under **Service**, choose **EC2 (EIP/VPC)**. The service you select determines the AWS service where the CIDR will be advertisable. Currently, the only option is **EC2 (EIP/VPC)**, which means that the CIDRs allocated from this pool will be advertisable for the Amazon EC2 service (for Elastic IP addresses) and the Amazon VPC service (for CIDRs associated with VPCs). 10. Under **CIDRs to provision**, choose a CIDR to provision for
the pool.

###### Note

When provisioning a CIDR to a Regional pool within the top-level pool, the
most specific IPv4 CIDR you can provision is `/24`; more specific
CIDRs (such as `/25`) are not permitted. After you create the
Regional pool, you can create smaller pools (such as `/25`)
within the same Regional pool. Note that if you share the Regional pool or
pools within it, these pools can only be used in the locale set on the same
Regional pool. 11. Enable **Configure this pool's allocation rule settings**.
You have the same allocation rule options here as you did when you created the
top-level pool. See [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md") for an explanation of the options that are
available when you create pools. The allocation rules for the Regional pool are
not inherited from the top-level pool. If you do not apply any rules here, there
will be no allocation rules set for the pool. 12. (Optional) Choose **Tags** for the pool. 13. When you’ve finished configuring your pool, choose **Create
pool**.

Ensure that this CIDR has been provisioned before you continue. You can see the state of provisioning in the **CIDRs** tab in the pool details page.

## Step 4: Advertise the CIDR

The steps in this section must be done by the IPAM account. Once you associate the
Elastic IP address (EIP) with an instance or Elastic Load Balancer, you can then start
advertising the CIDR you brought to AWS that is in pool that has the **Service EC2 (EIP/VPC)** configured. In this tutorial, that's your Regional
pool. By default the CIDR is not advertised, which means it's not publicly accessible
over the internet.

This step must be done by the IPAM account.

###### Note

The advertisement status doesn't not restrict your ability to allocate Elastic IP addresses. Even if your
BYOIPv4 CIDR is not advertised, you can still can create EIPs from the IPAM pool.

###### To advertise the CIDR

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, when you create a pool, the default private scope is selected.
   Choose the public scope. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. Choose the Regional pool you created in this tutorial.
5. Choose the **CIDRs** tab.
6. Select the BYOIP CIDR and choose **Actions** >
   **Advertise**.
7. Choose **Advertise CIDR**.

As a result, the BYOIP CIDR is advertised and the value in the
**Advertising** column changes from **Withdrawn**
to **Advertised**.

## Step 5. Share the Regional

pool

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

## Step 6: Allocate an Elastic IP address

from the pool

Complete the steps in this section to allocate an Elastic IP address from the pool. Note that if
you are using public IPv4 pools to allocate Elastic IP addresses, you can use the
alternative steps in [Alternative to Step 6](#tutorials-byoip-ipam-ipv4-alt "#tutorials-byoip-ipam-ipv4-alt") rather than the steps
in this section.

###### Important

If you see an error related to not having permissions to call ec2:AllocateAddress, the managed
permission currently assigned to the IPAM pool that was shared with you needs to be
updated. Contact the person who created the resource share and ask them to update
the managed permission `AWSRAMPermissionIpamResourceDiscovery` to the
default version. For more information, see [Update a resource
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

## Step 7: Associate the Elastic IP address with

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

## Step 8: Cleanup

Follow the steps in this section to clean up the resources you've provisioned and
created in this tutorial.

###### Step 1: Withdraw the CIDR from advertising

This step must be done by the IPAM account.

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, when you create a pool, the default private scope is selected.
   Choose the public scope.
4. Choose the Regional pool you created in this tutorial.
5. Choose the **CIDRs** tab.
6. Select the BYOIP CIDR and choose **Actions** >
   **Withdraw from advertising**.
7. Choose **Withdraw CIDR**.

As a result, the BYOIP CIDR is no longer advertised and the value in the
**Advertising** column changes from **Advertised**
to **Withdrawn**.

###### Step 2: Disassociate the Elastic IP address

This step must be done by the member account. If you are using the AWS CLI, use the `--profile `member-account`` option.

- Complete the steps in [Disassociate an Elastic IP address](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-associating-different "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-associating-different") in
  the _Amazon EC2 User Guide_ to disassociate the EIP.
  When you open EC2 in the AWS Management console, the AWS Region you disassociate the
  EIP in must match the `Locale` option you chose when you created the pool
  that will be used for the BYOIP CIDR. In this tutorial, that pool is the Regional
  pool.

###### Step 3: Release the Elastic IP address

This step must be done by the member account. If you are using the AWS CLI, use the `--profile `member-account`` option.

- Complete the steps in [Release an Elastic IP address](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-releasing "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-releasing") in the
  _Amazon EC2 User Guide_ to release an Elastic IP address (EIP)
  from the public IPv4 pool. When you open EC2 in the AWS Management console,
  the AWS Region you allocate the EIP in must match the `Locale`
  option you chose when you created the pool that will be used for the BYOIP
  CIDR.

###### Step 4: Delete any RAM shares and disable RAM integration with AWS

Organizations

This step must be done by the IPAM account and management account
respectively. If you are using the AWS CLI to delete the RAM shares and disable RAM
integration, use the `--profile `ipam-account`` and
  `--profile `management-account``
options.

- Complete the steps in [Deleting a resource
  share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-delete.md "../../../ram/latest/userguide/working-with-sharing-delete.md") and [Disabling
  resource sharing with AWS Organizations](../../../ram/latest/userguide/security-disable-sharing-with-orgs.md "../../../ram/latest/userguide/security-disable-sharing-with-orgs.md") in the _AWS RAM User Guide_, in that order, to delete the
  RAM shares and disable RAM integration with AWS Organizations.

###### Step 5: Deprovision the CIDRs from the Regional pool and top-level

pool

This step must be done by the IPAM account. If you are using the AWS CLI to share the pool, use the `--profile `ipam-account`` option.

- Complete the steps in [Deprovision CIDRs from a pool](depro-pool-cidr-ipam.md "depro-pool-cidr-ipam.md") to deprovision the CIDRs from the Regional pool and then the top-level pool, in that order.

###### Step 6: Delete the Regional pool and top-level pool

This step must be done by the IPAM account. If you are using the AWS CLI to share the pool, use the `--profile `ipam-account`` option.

- Complete the steps in [Delete a pool](delete-pool-ipam.md "delete-pool-ipam.md") to delete the Regional pool and then the top-level pool, in that order.

## Alternative to Step 6

If you are using public IPv4 pools to allocate Elastic IP addresses, you can use the
steps in this section rather than the steps in [Step 6: Allocate an Elastic IP address
from the pool](#tutorials-byoip-ipam-ipv4-console-all-eip "#tutorials-byoip-ipam-ipv4-console-all-eip").

###### Contents

- [Step 1: Create a public IPv4 pool](#tutorials-byoip-ipam-ipv4-console-alt-pool "#tutorials-byoip-ipam-ipv4-console-alt-pool")
- [Step 2: Provision the public IPv4 CIDR to your public IPv4 pool](#tutorials-byoip-ipam-ipv4-console-alt-cidr "#tutorials-byoip-ipam-ipv4-console-alt-cidr")
- [Step 3: Allocate an Elastic IP address from
  the public IPv4 pool](#tutorials-byoip-ipam-ipv4-console-alt-eip "#tutorials-byoip-ipam-ipv4-console-alt-eip")
- [Alternative to Step 6
  cleanup](#tutorials-byoip-ipam-ipv4-console-alt-cleanup "#tutorials-byoip-ipam-ipv4-console-alt-cleanup")

### Step 1: Create a public IPv4 pool

This step should be done by the member account that will provision an Elastic IP address.

###### Note

- This step must be done by the member account using the AWS CLI.
- Public IPv4 pools and IPAM pools are managed by distinct resources in AWS. Public IPv4 pools are single account resources
  that enable you to convert your publicly-owned CIDRs to Elastic IP addresses. IPAM pools can be used to allocate your public space
  to public IPv4 pools.

###### To create a public IPv4 pool using the AWS CLI

- Run the following command to provision the CIDR. When you run the
  command in this section, the value for `--region` must match the
  `Locale` option you chose when you created the pool that will be
  used for the BYOIP CIDR.

```
aws ec2 create-public-ipv4-pool --region `us-east-2` --profile `member-account`
```

In the output, you'll see the public IPv4 pool ID. You will need this
ID in the next step.

```
{
    "PoolId": "ipv4pool-ec2-09037ce61cf068f9a"
}
```

### Step 2: Provision the public IPv4 CIDR to your public IPv4 pool

Provision the public IPv4 CIDR to your public IPv4 pool. The value for
`--region` must match the `Locale` value you chose when you
created the pool that will be used for the BYOIP CIDR. The `--netmask-length`
is the amount of space out of the IPAM pool that you want to bring to your public pool.
The value cannot be larger than the netmask length of the IPAM pool. The least specific
`--netmask-length` you can define is `24`.

###### Note

- If you are bringing a `/24` CIDR range to IPAM to share across an AWS
  Organization, you can provision smaller prefixes to multiple IPAM pools, say
  `/27` (using `-- netmask-length 27`), rather than
  provisioning the entire `/24` CIDR (using `-- netmask-length
24`) as is shown in this tutorial.
- This step must be done by the member account using the AWS CLI.

###### To create a public IPv4 pool using the AWS CLI

1. Run the following command to provision the CIDR.

```
aws ec2 provision-public-ipv4-pool-cidr --region `us-east-2` --ipam-pool-id `ipam-pool-04d8e2d9670eeab21` --pool-id `ipv4pool-ec2-09037ce61cf068f9a` --netmask-length `24` --profile `member-account`
```

In the output, you'll see the provisioned CIDR.

```
{
    "PoolId": "ipv4pool-ec2-09037ce61cf068f9a",
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
aws ec2 describe-public-ipv4-pools --region `us-east-2` --max-results `10` --profile `member-account`
```

In the output, you'll see the provisioned CIDR. By default the CIDR is
not advertised, which means it's not publicly accessible over the internet.
You will have the chance to set this CIDR to advertised in the last step of
this tutorial.

```
{
    "PublicIpv4Pools": [
        {
            "PoolId": "ipv4pool-ec2-09037ce61cf068f9a",
            "Description": "",
            "PoolAddressRanges": [
                {
                    "FirstAddress": "130.137.245.0",
                    "LastAddress": "130.137.245.255",
                    "AddressCount": 256,
                    "AvailableAddressCount": 255
                }
            ],
            "TotalAddressCount": 256,
            "TotalAvailableAddressCount": 255,
            "NetworkBorderGroup": "us-east-2",
            "Tags": []
        }
    ]
}
```

Once you create the public IPv4 pool, to view the public IPv4 pool allocated in the
IPAM Regional pool, open the IPAM console and view the allocation in the Regional pool
under **Allocations** or **Resources**.

### Step 3: Allocate an Elastic IP address from

the public IPv4 pool

Complete the steps in [Allocate an Elastic IP address](../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-allocating "../../../AWSEC2/latest/UserGuide/working-with-eips.md#using-instance-addressing-eips-allocating") in the _Amazon EC2 User Guide_
to allocate an EIP from the public IPv4 pool. When you open EC2 in
the AWS Management console, the AWS Region you allocate the EIP in must match the
`Locale` option you chose when you created the pool that will be used for
the BYOIP CIDR.

This step must be done by the member account. If you are using the AWS CLI, use the `--profile `member-account`` option.

Once you've completed these three steps, return to [Step 7: Associate the Elastic IP address with
an EC2 instance](#tutorials-byoip-ipam-ipv4-console-assoc-eip "#tutorials-byoip-ipam-ipv4-console-assoc-eip") and continue until you complete the tutorial.

### Alternative to Step 6

cleanup

Complete these steps to clean up public IPv4 pools created with the alternative to Step 9. You should complete these steps after you release the Elastic IP address during the standard cleanup process in [Step 8: Cleanup](#tutorials-byoip-ipam-ipv4-console-cleanup "#tutorials-byoip-ipam-ipv4-console-cleanup").

###### Step 1: Deprovision the public IPv4 CIDR from your public IPv4 pool

###### Important

This step must be done by the member account using the AWS CLI.

1. View your BYOIP CIDRs.

```
aws ec2 describe-public-ipv4-pools --region `us-east-2` --profile `member-account`
```

In the output, you'll see the IP addresses in your BYOIP CIDR.

```
{
    "PublicIpv4Pools": [
        {
            "PoolId": "ipv4pool-ec2-09037ce61cf068f9a",
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
            "NetworkBorderGroup": "us-east-2",
            "Tags": []
        }
    ]
}
```

2. Run the following command to release the CIDR from the public IPv4 pool.

```
aws ec2 deprovision-public-ipv4-pool-cidr --region `us-east-2` --pool-id `ipv4pool-ec2-09037ce61cf068f9a` --cidr `130.137.245.0/24` --profile `member-account`
```

3. View your BYOIP CIDRs again and ensure there are no more provisioned
   addresses. When you run the command in this section, the value for
   `--region` must match the Region of your IPAM.

```
aws ec2 describe-public-ipv4-pools --region `us-east-2` --profile `member-account`
```

In the output, you'll see the IP addresses count in your public IPv4 pool.

```
{
    "PublicIpv4Pools": [
        {
            "PoolId": "ipv4pool-ec2-09037ce61cf068f9a",
            "Description": "",
            "PoolAddressRanges": [],
            "TotalAddressCount": 0,
            "TotalAvailableAddressCount": 0,
            "NetworkBorderGroup": "us-east-2",
            "Tags": []
        }
    ]
}
```

###### Note

It can take some time for IPAM to discover that public IPv4 pool allocations have
been removed. You cannot continue to clean up and deprovision the IPAM pool CIDR
until you see that the allocation has been removed from IPAM.

###### Step 2: Delete the public IPv4 pool

This step must be done by the member account.

- Run the following command to delete the public IPv4 pool the CIDR.
  When you run the command in this section, the value for `--region`
  must match the `Locale` option you chose when you created the pool
  that will be used for the BYOIP CIDR. In this tutorial, that pool is the
  Regional pool. This step must be done using the AWS CLI.

```
aws ec2 delete-public-ipv4-pool --region `us-east-2` --pool-id `ipv4pool-ec2-09037ce61cf068f9a` --profile `member-account`
```

In the output, you'll see the return value **true**.

```
{
"ReturnValue": true
}
```

Once you delete the pool, to view the allocation unmanaged by IPAM, open the IPAM
console and view the details of the Regional pool under
**Allocations**.
