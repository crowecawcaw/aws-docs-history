# Use packs to collect and process data in

SiteWise Edge

###### Note

The data processing pack (DPP) feature is no longer availabke to new customers. Existing customers can continue to use the service as normal. For more information, see
[Data processing pack availability change](../appguide/iotsitewise-dpp-availability-change.md "../appguide/iotsitewise-dpp-availability-change.md").

AWS IoT SiteWise Edge gateways use different packs to determine how to collect and process
your data.

Currently, the following packs are available:

- **Data collection pack** – Use this
  pack to collect your industrial data and route it to AWS Cloud
  destinations. By default, this pack is enabled automatically for your
  SiteWise Edge gateway.
- **Data processing pack** – Use this
  pack to enable SiteWise Edge gateway communication with edge-configured asset
  models and assets. You can use edge configuration to control what asset data
  to compute and process on-site. You can then send your data to AWS IoT SiteWise or
  other AWS services. For more information about the data processing pack,
  see [Configure edge data processing for AWS IoT SiteWise models
  and assets](edge-processing.md "edge-processing.md").

## Upgrading packs

###### Important

Upgrading data processing pack versions from before (and including) 2.0.x
to version 2.1.x will result in data loss of locally stored
measurements.

SiteWise Edge gateways use different packs to determine how to collect and process
your data. You can use the AWS IoT SiteWise console to upgrade packs.

###### To upgrade packs (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation, choose **Edge gateways** in the **Edge** section.
3. In the **Gateways** list, choose the SiteWise Edge gateway
   with the packs you want to upgrade.
4. In the **Gateway configuration** section, choose
   **Software updates available**.
5. On the Edit software versions page, choose
   **Updates**.

###### Note

You can only upgrade packs that are enabled. To find the list of
packs that are enabled for this SiteWise Edge gateway, choose
**Overview**, and then see the **Edge
capabilities** section. 6. On the edit software versions page, in the **Gateway component
updates** section, do the following:

    * To update the **OPC UA collector**, choose a
     version, and then choose **Deploy**.
    * To update the **Publisher**, choose a
     version, and then choose **Deploy**.
    * To update the **Data processing pack**,
     choose a version, and then choose
     **Deploy**.

7. When you're done deploying new versions, choose
   **Done**.

If you're experiencing problems upgrading the packs, see [Unable to deploy packs to SiteWise Edge gateways](troubleshooting-gateway.md#gateway-issue-ggv2-packs "troubleshooting-gateway.md#gateway-issue-ggv2-packs").
