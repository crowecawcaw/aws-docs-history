# Bring your own IPv6 CIDR to IPAM using the AWS

Management Console

Follow the steps in this tutorial to bring an IPv6 CIDR to IPAM and allocate a VPC
with the CIDR using both the AWS Management Console and the AWS CLI.

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

- [Step 1: Create a top-level IPAM pool](#tutorials-byoip-ipam-ipv6-console-1 "#tutorials-byoip-ipam-ipv6-console-1")
- [Step 2. Create a Regional pool within the
  top-level pool](#tutorials-byoip-ipam-ipv6-console-2 "#tutorials-byoip-ipam-ipv6-console-2")
- [Step 3. Share the Regional pool](#tutorials-byoip-ipam-ipv4-console-4-deux "#tutorials-byoip-ipam-ipv4-console-4-deux")
- [Step 4: Create a VPC](#tutorials-byoip-ipam-ipv6-console-4 "#tutorials-byoip-ipam-ipv6-console-4")
- [Step 5: Advertise the CIDR](#tutorials-byoip-ipam-ipv6-console-5 "#tutorials-byoip-ipam-ipv6-console-5")
- [Step 6: Cleanup](#tutorials-byoip-ipam-ipv6-console-cleanup "#tutorials-byoip-ipam-ipv6-console-cleanup")

## Step 1: Create a top-level IPAM pool

Since you are going to create a top-level IPAM pool with a Regional pool within it,
and we’re going to allocate space to a resource from the
Regional pool, you will set the locale on the Regional pool and not the top-level
pool. You’ll add the locale to the Regional pool when you create the Regional pool
in a later step. The IPAM integration with BYOIP requires that the locale is set on
whichever pool will be used for the BYOIP CIDR.

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
7. Under **Address family**, choose **IPv6**.
8. Under **Resource planning**, leave **Plan IP space
   within the scope** selected. For more information about using this
   option to plan for subnet IP space within a VPC, see [Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md "tutorials-subnet-planning.md").
9. Under **Locale**, choose **None**. You will
   set the locale on the Regional pool.

The locale is the AWS Region where you want this IPAM pool to be available for allocations. For example, you can only allocate a CIDR for a VPC from an IPAM pool that shares a locale with the VPC’s Region. Note that when you have chosen a locale for a pool, you cannot modify it. If the home Region of the IPAM is unavailable due to an outage and the pool has a locale different than the home Region of the IPAM, the pool can still be used to allocate IP addresses.

###### Note

If you are creating a single pool only and not a top-level pool with Regional pools within it,
you would want to choose a Locale for this pool so that the pool is
available for allocations. 10. Under **Public IP source**, **BYOIP** is
selected by default. 11. Under **CIDRs to provision**, do one of the following:

    * If you [verified
     your domain control with an X.509 certificate](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-cert"), you must include the
     CIDR and the BYOIP message and certificate signature that you created in that step so we can
     verify that you control the public space.
    * If you [verified your domain control with a DNS TXT record](tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt "tutorials-byoip-ipam-domain-verification-methods.md#tutorials-byoip-ipam-domain-verification-dns-txt"), you must
     include the CIDR and IPAM verification token that you created in that step so we can verify
     that you control the public space.

Note that when provisioning an IPv6 CIDR to a pool within the top-level pool,
the most specific IPv6 address range that you can bring is /48 for CIDRs that
are publicly advertisable and /60 for CIDRs that are not publicly advertisable.

###### Important

While most provisioning will be completed within two hours, it may take up
to one week to complete the provisioning process for publicly advertisable
ranges. 12. Leave **Configure this pool's allocation rule settings**
unselected. 13. (Optional) Choose **Tags** for the pool. 14. Choose **Create pool**.

Ensure that this CIDR has been provisioned before you continue. You can see the state
of provisioning in the **CIDRs** tab in the pool details page.

## Step 2. Create a Regional pool within the

top-level pool

Create a Regional pool within the top-level pool. A Locale is required on
the pool and it must be one of the operating Regions you configured when you created the
IPAM.

This step must be done by the IPAM account.

###### To create a Regional pool within a top-level pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, when you create a pool, the default private scope is selected. If you don’t want to use the default
   private scope, from the dropdown menu at the top of the content pane, choose the scope you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. Choose **Create pool**.
5. (Optional) Add a **Name tag** for the pool and a description for the pool.
6. Under **Source**, choose the top-level pool that you created
   in the previous section.
7. Under **Resource planning**, leave **Plan IP
   space within the scope** selected. For more information
   about using this option to plan for subnet IP space within a VPC, see
   [Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md "tutorials-subnet-planning.md").
8. Choose the locale for the pool. Choosing a locale ensures there are no
   cross-region dependencies between your pool and the resources allocating from
   it. The available options come from the operating Regions that you chose when
   you created your IPAM. In this tutorial, we'll use `us-east-2` as the
   locale for the Regional pool.

The locale is the AWS Region where you want this IPAM pool to be available for allocations. For example, you can only allocate a CIDR for a VPC from an IPAM pool that shares a locale with the VPC’s Region. Note that when you have chosen a locale for a pool, you cannot modify it. If the home Region of the IPAM is unavailable due to an outage and the pool has a locale different than the home Region of the IPAM, the pool can still be used to allocate IP addresses. 9. Under **Service**, choose **EC2 (EIP/VPC)**.
The service you select determines the AWS service where the CIDR will be
advertisable. Currently, the only option is **EC2 (EIP/VPC)**,
which means that the CIDRs allocated from this pool will be advertisable for the
Amazon EC2 service and the Amazon VPC service (for
CIDRs associated with VPCs). 10. Under **CIDRs to provision**, choose a CIDR to provision for
the pool. Note that when provisioning an IPv6 CIDR to a pool within the
top-level pool, the most specific IPv6 address range that you can bring is /48
for CIDRs that are publicly advertisable and /60 for CIDRs that are not publicly
advertisable. 11. Enable **Configure this pool's allocation rule settings** and choose optional
allocation rules for this pool:

    * **Automatically import discovered resources**: This option is not available if the **Locale** is set to **None**. If selected, IPAM will continuously look for resources within the CIDR range of this pool
     and automatically import them as allocations into your IPAM. Note the following:




    	+ The CIDRs that will be allocated for
    	 these resources must not already be allocated to other resources in order for the import to succeed.
    	+ IPAM will import
    	 a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently
    	 marked as noncompliant.
    	+ If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only.
    	+ If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only.
    * **Minimum netmask length**: The minimum netmask length required for
     CIDR allocations in this IPAM pool to be compliant and the largest size CIDR block that can be allocated from the pool. The minimum netmask length must be less than the maximum
     netmask length. Possible netmask lengths for IPv4 addresses are `0` - `32`. Possible netmask lengths for IPv6 addresses
     are `0` - `128`.
    * **Default netmask length**: A default netmask length for
     allocations added to this pool.
    * **Maximum netmask length**: The maximum netmask length that will
     be required for CIDR allocations in this pool. This value dictates the
     smallest size CIDR block that can be allocated from the pool. Ensure
     that this value is minimum `/48`.
    * **Tagging requirements**: The tags that are required for
     resources to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the
     allocation tagging rules are changed on the pool, the resource may be marked as noncompliant.
    * **Locale**: The locale that will be required for
     resources that use CIDRs from this pool. Automatically imported resources
     that do not have this locale will be marked noncompliant. Resources that are not
     automatically imported into the pool will not be allowed to allocate space from
     the pool unless they are in this locale.

12. (Optional) Choose **Tags** for the pool.
13. When you’ve finished configuring your pool, choose **Create
    pool**.

Ensure that this CIDR has been provisioned before you continue. You can see the state of provisioning in the **CIDRs** tab in the pool details page.

## Step 3. Share the Regional pool

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

## Step 4: Create a VPC

Complete the steps in [Create a VPC](../userguide/create-vpc.md "../userguide/create-vpc.md") in the _Amazon VPC User Guide_.

This step must be done by the member account.

###### Note

- When you open VPC in the AWS Management console, the AWS Region you create the VPC
  in must match the `Locale` option you chose when you created the pool that
  will be used for the BYOIP CIDR.
- When you reach the step to choose a CIDR for the VPC, you will have an option to use a
  CIDR from an IPAM pool. Choose the Regional pool you created in this tutorial.

When you create the VPC, AWS allocates a CIDR in the IPAM pool to the VPC. You can
view the allocation in IPAM by choosing a pool in the content pane of the IPAM console
and viewing the **Allocations** tab for the pool.

## Step 5: Advertise the CIDR

The steps in this section must be done by the IPAM account. Once you create the VPC,
you can then start advertising the CIDR you brought to AWS that is in the pool that has the **Service EC2 (EIP/VPC)** configured. In this tutorial, that's your Regional pool. By default the CIDR is
not advertised, which means it's not publicly accessible over the internet.

This step must be done by the IPAM account.

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

## Step 6: Cleanup

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

###### Step 2: Delete the VPC

This step must be done by the member account.

- Complete the steps in [Delete
  a VPC](../userguide/delete-vpc.md "../userguide/delete-vpc.md") in the _Amazon VPC User Guide_ to delete the VPC.
  When you open VPC in the AWS Management console, the AWS Region delete the VPC from must match the `Locale` option you chose when you created the pool
  that will be used for the BYOIP CIDR. In this tutorial, that pool is the Regional
  pool.

When you delete the VPC, it takes time for IPAM to discover that the resource has been deleted and to deallocate the CIDR allocated to the VPC.
You cannot continue to the next step in the cleanup until you see that IPAM has removed the allocation from the pool in the pool details **Allocations** tab.

###### Step 3: Delete the RAM shares and disable RAM integration with AWS Organizations

This step must be done by the IPAM account and management account respectively.

- Complete the steps in [Deleting a resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-delete.md "../../../ram/latest/userguide/working-with-sharing-delete.md")
  and [Disabling resource sharing with AWS Organizations](../../../ram/latest/userguide/security-disable-sharing-with-orgs.md "../../../ram/latest/userguide/security-disable-sharing-with-orgs.md") in
  the _AWS RAM User Guide_, in that order, to delete the RAM shares and disable RAM integration with AWS Organizations.

###### Step 4: Deprovision the CIDRs from the Regional pool and top-level pool

This step must be done by the IPAM account.

- Complete the steps in [Deprovision CIDRs from a pool](depro-pool-cidr-ipam.md "depro-pool-cidr-ipam.md") to deprovision the CIDRs from the Regional pool and then the top-level pool, in that order.

###### Step 5: Delete the Regional pool and top-level pool

This step must be done by the IPAM account.

- Complete the steps in [Delete a pool](delete-pool-ipam.md "delete-pool-ipam.md") to delete the Regional pool and then the top-level pool, in that order.
