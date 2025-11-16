# Configure edge capabilities on

AWS IoT SiteWise Edge

###### Note

The data processing pack (DPP) feature is no longer availabke to new customers. Existing customers can continue to use the service as normal. For more information, see
[Data processing pack availability change](../appguide/iotsitewise-dpp-availability-change.md "../appguide/iotsitewise-dpp-availability-change.md").

You can use AWS IoT SiteWise Edge to collect and temporarily store data so that you can
organize and process device data locally. By enabling edge processing, you can
choose to send only aggregated data to the AWS Cloud to optimize your bandwidth
usage and cloud storage costs. Using AWS IoT SiteWise components with AWS IoT Greengrass, you can collect
and process data at the edge before sending it to the AWS Cloud, or manage it
on-premises using SiteWise Edge APIs.

Data collection happens through data packs and AWS IoT SiteWise components that run on
AWS IoT Greengrass.

###### Note

- AWS IoT SiteWise retains your edge data on your SiteWise Edge gateways up to 30 days.
  The retention period of your data is dependent on the available disk
  space of your device.
- If your SiteWise Edge gateway has been disconnected from the AWS Cloud for
  30 days, the [Data Processing Pack](configure-opcua-source.md "configure-opcua-source.md")
  is automatically disabled.

###### Topics

- [Set up edge capability in SiteWise Edge](#using-sitewise-edge "#using-sitewise-edge")

## Set up edge capability in SiteWise Edge

AWS IoT SiteWise provides the following packs that your SiteWise Edge gateway can use to
determine how to collect and process your data. Select packs to enable edge
capabilities for your SiteWise Edge gateway.

- **Data collection pack** enables your SiteWise Edge gateway
  to collect data from multiple OPC UA servers, and then export the data
  from the edge to the AWS Cloud. It becomes active once you have added
  data sources to your SiteWise Edge gateway.
- **Data processing pack** enables your SiteWise Edge gateway
  to process your equipment data at the edge. For example, you can use
  asset models to compute metrics and transforms. For more information
  about asset models and assets, see [Model industrial assets](industrial-asset-models.md "industrial-asset-models.md").

###### Note

    + The data processing pack is only available on x86
     platforms.

###### To configure edge capabilities

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Edge
   gateways**.
3. Select the SiteWise Edge gateway for which you want to activate edge
   capabilities.
4. In the **Edge capabilities** section, choose
   **Edit**
5. In the **Edge capabilities** section, select
   **Enable data processing pack (incurs additional
   charges)**.
6. (Optional) In the **Edge LDAP connection** section,
   you can grant user groups in your corporate directory access to this
   SiteWise Edge gateway. The user groups can use the Lightweight Directory
   Access Protocol (LDAP) credentials to access the SiteWise Edge gateway. Then
   they can use the AWS OpsHub for AWS IoT SiteWise application, AWS IoT SiteWise API operations,
   or other tools to manage the SiteWise Edge gateway. For more information, see
   [Manage SiteWise Edge gateways](manage-gateways-ggv2.md "manage-gateways-ggv2.md").

###### Note

You can also use the Linux or Microsoft Windows
credentials to access the SiteWise Edge gateway. For more information, see
[Access your SiteWise Edge gateway using Linux
operating system credentials](manage-gateways-ggv2.md#linux-user-pool "manage-gateways-ggv2.md#linux-user-pool").

    1. Select **Activated**.
    2. For **Provider name**, enter a name for your
     LDAP provider.
    3. For **Hostname or IP address**, enter the
     hostname or IP address of your LDAP server.
    4. For **Port**, enter a port number.
    5. For **Base distinguished name (DN)**, enter a
     distinguished name (DN) for the base.


    The following attribute types are supported: commonName (CN),
     localityName (L), stateOrProvinceName (ST), organizationName
     (O), organizationalUnitName (OU), countryName (C), streetAddress
     (STREET), domainComponent (DC), and userid (UID).
    6. For **Admin group DN**, enter a DN.
    7. For **User group DN**, enter a DN.

7. Choose **Save**.

Now that you've activated edge capabilities on your SiteWise Edge gateway, you need
to configure your asset model for the edge. Your asset model edge configuration
specifies where your assets properties are computed. You can compute all
properties at the edge, or you can configure your asset model properties
separately. Asset model properties include [metrics](concept-overview.md#concept-metric "concept-overview.md#concept-metric"), [transforms](concept-overview.md#concept-transform "concept-overview.md#concept-transform"), and
[measurements](concept-overview.md#concept-measurement "concept-overview.md#concept-measurement").

For more information about asset properties, see [Define data properties](asset-properties.md "asset-properties.md").

After you create your asset model, you can then configure it for the edge.
For more information about configuring your asset model for the edge, see [Create an asset model (console)](create-asset-models.md#create-asset-model-console "create-asset-models.md#create-asset-model-console").

###### Note

Asset models and dashboards are automatically synced between the AWS
Cloud and your SiteWise Edge gateway every 10 minutes. You can also sync manually
from the local SiteWise Edge gateway application.
