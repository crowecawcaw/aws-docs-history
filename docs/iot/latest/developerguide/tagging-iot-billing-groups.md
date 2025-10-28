# Billing groups

AWS IoT doesn't allow you to directly apply tags to individual things, but it does allow you
to place things in billing groups and to apply tags to these. For AWS IoT, allocation of cost
and usage data based on tags is limited to billing groups.

AWS IoT Core for LoRaWAN resources, such as wireless devices and gateways, can't be added to billing
groups. However, they can be associated with AWS IoT things, which can be added to billing
groups.

The following commands are available:

- [AddThingToBillingGroup](../apireference/API_AddThingToBillingGroup.md "../apireference/API_AddThingToBillingGroup.md") adds a thing to a billing group.
- [CreateBillingGroup](../apireference/API_CreateBillingGroup.md "../apireference/API_CreateBillingGroup.md") creates a billing group.
- [DeleteBillingGroup](../apireference/API_DeleteBillingGroup.md "../apireference/API_DeleteBillingGroup.md") deletes the billing group.
- [DescribeBillingGroup](../apireference/API_DescribeBillingGroup.md "../apireference/API_DescribeBillingGroup.md") returns information about a billing group.
- [ListBillingGroups](../apireference/API_ListBillingGroups.md "../apireference/API_ListBillingGroups.md") lists the billing groups you have created.
- [ListThingsInBillingGroup](../apireference/API_ListThingsInBillingGroup.md "../apireference/API_ListThingsInBillingGroup.md") lists the things you have added to the given billing
  group.
- [RemoveThingFromBillingGroup](../apireference/API_RemoveThingFromBillingGroup.md "../apireference/API_RemoveThingFromBillingGroup.md") removes the given thing from the billing
  group.
- [UpdateBillingGroup](../apireference/API_UpdateBillingGroup.md "../apireference/API_UpdateBillingGroup.md") updates information about the billing group.
- [CreateThing](../apireference/API_CreateThing.md "../apireference/API_CreateThing.md") allows you to specify a billing group for the thing when you create
  it.
- [DescribeThing](../apireference/API_DescribeThing.md "../apireference/API_DescribeThing.md") returns the description of a thing including the billing group
  the thing belongs to, if any.
  The AWS IoT Wireless API provides these actions to associate wireless devices and
  gateways with AWS IoT things.

- [AssociateWirelessDeviceWithThing](../../../iot-wireless/2020-11-22/apireference/API_AssociateWirelessDeviceWithThing.md "../../../iot-wireless/2020-11-22/apireference/API_AssociateWirelessDeviceWithThing.md")
- [AssociateWirelessGatewayWithThing](../../../iot-wireless/2020-11-22/apireference/API_AssociateWirelessGatewayWithThing.md "../../../iot-wireless/2020-11-22/apireference/API_AssociateWirelessGatewayWithThing.md")

## Viewing cost allocation and usage

data

You can use billing group tags to categorize and track your costs. When you apply tags
to billing groups (and so to the things they include), AWS generates a cost allocation
report as a comma-separated value (CSV) file with your usage and costs aggregated by your
tags. You can apply tags that represent business categories (such as cost centers,
application names, or owners) to organize your costs across multiple services. For more
information about using tags for cost allocation, see [Use Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the [AWS Billing and
Cost Management User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").

###### Note

To accurately associate usage and cost data with those things you have placed in
billing groups, each device or application must:

- Be registered as a thing in AWS IoT. For more information, see [Managing devices with AWS IoT](iot-thing-management.md "iot-thing-management.md").
- Connect to the AWS IoT message broker through MQTT using only the thing's name as
  the client ID. For more information, see [Device communication protocols](protocols.md "protocols.md"). If you client ID
  doesn't match the thing name, you can enable the exclusive thing attachment to
  establish the association. For more information, see [Associating an AWS IoT thing to an MQTT client
  connection](exclusive-thing.md "exclusive-thing.md").
- Authenticate using a client certificate associated with the thing.

The following pricing dimensions are available for billing groups (based on the activity
of things associated with the billing group):

- Connectivity (based on the thing name used as the client ID to connect).
- Messaging (based on messages inbound from, and outbound to, a thing; MQTT
  only).
- Shadow operations (based on the thing whose message triggered a shadow
  update).
- Rules triggered (based on the thing whose inbound message triggered the rule; does
  not apply to those rules triggered by MQTT lifecycle events).
- Thing index updates (based on the thing that was added to the index).
- Remote actions (based on the thing updated).
- [AWS IoT Device Defender
  detect](../../../iot-device-defender/latest/devguide/device-defender-detect.md "../../../iot-device-defender/latest/devguide/device-defender-detect.md") reports (based on the thing whose activity is reported).

Cost and usage data based on tags (and reported for a billing group) doesn't reflect the
following activities:

- Device registry operations (including updates to things, thing groups, and thing
  types). For more information, see [Managing devices with AWS IoT](iot-thing-management.md "iot-thing-management.md")).
- Thing group index updates (when adding a thing group).
- Index search queries.
- [Device provisioning](iot-provision.md "iot-provision.md").
- [AWS IoT Device Defender
  audit](../../../iot-device-defender/latest/devguide/device-defender-audit.md "../../../iot-device-defender/latest/devguide/device-defender-audit.md") reports.
