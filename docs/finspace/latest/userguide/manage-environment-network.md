After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Managing environment network

settings

For each Managed kdb Insights environment, you can configure a network connection to
allow the Managed kdb clusters running in your environment infrastructure account to
access resources in your internal network. You can create a connection by connecting
your infrastructure account to an existing transit gateway in your organization.

After you add a network, you can also specify details for the DNS servers that your
Managed kdb clusters will use to resolve resources outside of your Managed kdb
environment. After your Managed kdb environment is connected to your network, you can
optionally configure your network to allow outbound traffic from your environment to the
internet. This connectivity is managed by your network infrastructure. Managed kdb
doesn't support direct internet access (inbound or outbound).

## Prerequisites

Before you proceed, complete the following prerequisites:

- Make sure that a kdb environment has been created. For more information, see
  [Creating a kdb environment](using-kdb-environment.md#create-kdb-environment "using-kdb-environment.md#create-kdb-environment").
- Make sure that a transit gateway has been created in AWS Transit Gateway. For more
  information, see [Create the
  transit gateway](../../../vpc/latest/tgw/tgw-getting-started.md#step-create-tgw "../../../vpc/latest/tgw/tgw-getting-started.md#step-create-tgw") in the _AWS Transit Gateway User
  Guide_.
- Make sure that you have a _/26 (64)_ IP
  address range from the _100.64.0.0/10_ range
  that you can allocate to the subnets that connect to your transit
  gateway.

## Creating a network connection

You can configure a network connection to allow the Managed kdb clusters running
in your environment infrastructure account to access resources in your internal
network.

Optionally, you can also define how you manage the outbound traffic from kdb
network to your internal network. You do this by configuring the attachment network
access control lists (ACLs).

A network ACL allows or denies specific outbound traffic at the subnet level. You
can use the default network ACL for your VPC. Alternatively, to add an additional
layer of security to your VPC, you can create a custom network ACL for your VPC with
rules that are similar to the rules for your security groups. For more information,
see the [Network ACL
rules](../../../vpc/latest/userguide/vpc-network-acls.md#nacl-rules "../../../vpc/latest/userguide/vpc-network-acls.md#nacl-rules") in the _Amazon VPC User Guide_.

###### Note

- You can only configure one network connection per Managed kdb
  environment.
- You cannot delete a network connection. To remove the existing network
  and the network ACL attachments, delete the Managed kdb environment.

###### To create a network connection

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, under **Network** tab, choose **Add
   network configuration**.
5. On **Add network configuration** page, enter a transit gateway ID and the CIDR range that will be used for the subnets connecting to your internal network. For more information, see the [_Amazon VPC Transit Gateways User Guide_.](../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw "../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw")

###### Note

When you add a transit gateway without creating a network ACL, all outbound traffic is allowed by default. 6. (Optional) Add rules to define how you want to manage the outbound traffic from kdb network to
your internal network. Choose **Add new rule** to allow or
deny outbound traffic for each port range and destination.

###### Note

    * When you create a network ACL rule, by default all the other traffic are
     denied.
    * We process the ACL rules according to the rule numbers, in ascending order.

7. Choose **Save**. The connection creation process begins and the environment
   details page opens from where you can check the status under the
   **Network** tab.

## Editing a network

###### Note

- You can't edit the transit gateway ID and CIDR routable space for your
  network.
- You only edit the network ACL configurations for your network.

###### To edit a network connection

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, under **Network** tab,
   choose **Edit network**.
5. On **Edit network** page, add or modify the network ACL
   rules as required.
6. Choose **Save changes**. The updates are available on the
   environment details page.

## Adding DNS details

You can set the DNS resolver that the Managed kdb Insights compute nodes will use
for resolving IP addresses. This is useful if you want to connect from your Managed
kdb compute clusters to resources like on-premises kdb ticker plants or other
resources. We recommend you add DNS details only after you have successfully
configured a network in your Managed kdb environment.

###### Note

You can only add one DNS server and IP address per Managed kdb
environment.

###### To add DNS details

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. Under **DNS details**, choose **Add details**.
5. On **Add DNS details** page, enter the DNS server name and IP address that the clusters running in the Managed kdb environment will use.
6. Choose **Add DNS details**. The **environment
   details** page opens and the DNS details are added in the **DNS details** section, from where you can edit the
   DNS details.
