# Get started with AWS Global Networks for Transit Gateways

The following tasks help you become familiar with AWS Global Networks for Transit Gateways. For more information about
how AWS Global Networks for Transit Gateways works, see [How AWS Global Networks for Transit Gateways works](how-gnw-works.md "how-gnw-works.md").

In this example, you create a global network and register your transit gateway with the global
network. You can also define and associate your on-premises network resources with the
global network.

###### Tasks

- [Prerequisites](#network-manager-prerequisites "#network-manager-prerequisites")
- [Step 1: Create a global
  network](#getting-started-create-global-network "#getting-started-create-global-network")
- [Step 2: Register your transit
  gateway](#getting-started-register-tgw "#getting-started-register-tgw")
- [Step 3: (Optional) Define and associate your
  on-premises network resources](#getting-started-define-wan "#getting-started-define-wan")
- [Step 4: (Optional) Enable multi-account
  access](#getting-started-multi-account "#getting-started-multi-account")
- [Step 5: View and monitor your global
  network](#getting-started-view-global-network "#getting-started-view-global-network")

## Prerequisites

Before you begin, ensure that you have a transit gateway with attachments in your account or in
any account within your organization. For more information, see [Getting Started with Transit
Gateways](../../../vpc/latest/tgw/tgw-getting-started.md "../../../vpc/latest/tgw/tgw-getting-started.md").

The transit gateway can be in the same AWS account as the global network or in a different
AWS account within the organization.

## Step 1: Create a global

network

Create a global network as a container for your transit gateway.

###### To create a global network

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose
   **Global Networks**.
3. Choose **Create global network**.
4. Enter a name and description for the global network, and choose
   **Create global network**.

## Step 2: Register your transit

gateway

Register a transit gateway in your global network.

###### To register the transit gateway

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit gateways**, and then
   choose **Register transit gateway**.
5. From the **Select account** dropdown list, choose the account
   that you want to register the transit gateway from.

A list of transit gateways from that account appear in the **Select transit
gateway to register** section. 6. Select one or more transit gateways from the list, and then choose **Register
transit gateway**.

## Step 3: (Optional) Define and associate your

on-premises network resources

You can define your on-premises network by creating sites, links, and devices to
represent objects in your network. For more information, see the following
procedures:

- [Create a site using AWS Network Manager](creating-a-site.md "creating-a-site.md")
- [Adding a link](nm-site-link-add.md "nm-site-link-add.md")
- [Add a device using AWS Network Manager](nm-devices-add.md "nm-devices-add.md")

You associate the device with a specific site, and with one or more links. For
more information, see [Associate or disassociate a device
link using AWS Network Manager](nm-device-link-associate.md "nm-device-link-associate.md").

On your transit gateway you can

- Create a Site-to-Site VPN connection attachment. For more information, see [Customer gateway associations](gw-association.md#cgw-associations "gw-association.md#cgw-associations").
- Create a transit gateway Connect attachment, and then associate the Connect
  peer with the device. For more information, see [Add a Connect peer association using AWS Network Manager](connect-peer-association.md "connect-peer-association.md").

You can also work with one of our Partners in the AWS Partner Network (APN) to
provision and connect your on-premises network. For more information, see
[AWS Network Manager](https://aws.amazon.com/transit-gateway/network-manager "https://aws.amazon.com/transit-gateway/network-manager").

## Step 4: (Optional) Enable multi-account

access

Enable multi-account access to register transit gateways from multiple accounts, allowing you to
view and manage transit gateways and associated resources from those registered accounts in your
global network. Onboarding to AWS Organizations is a prerequisite for enabling multi-account
access for Network Manager.

1. Create your organization using AWS Organizations.

If you've already done this skip this step. For more information on creating
an organization using AWS Organizations, see [Creating and
managing an organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the
_AWS Organizations User Guide_. 2. Enable multi-account on the Network Manager console.

This enables trusted access for Network Manager and allows for registering delegated
administrators. For more information enabling trusted access and registering
delegated administrators, see [Multi-account in AWS Global Networks for Transit Gateways](nm-multi-account.md "nm-multi-account.md"). 3. Create your global network.

For more information on creating a global network, see [Create a global network using AWS Network Manager](global-networks-creating.md "global-networks-creating.md"). 4. Register transit gateways.

With multi-account enabled, you can register transit gateways from multiple accounts to
your global network. For more information about registering transit gateways, see [Transit gateway registrations in AWS Global Networks for Transit Gateways](tgw-registrations.md "tgw-registrations.md").

## Step 5: View and monitor your global

network

The Network Manager console provides a dashboard for you to view and monitor both your transit gateway
network objects in your global network.

###### To access the dashboard for your global network

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. The **Overview** page provides an inventory of the objects in
   your global network for your transit gateway network. For more information about the pages
   in the dashboard, see [Access transit gateway network dashboards using AWS Network Manager](nm-monitoring-console.md "nm-monitoring-console.md").
