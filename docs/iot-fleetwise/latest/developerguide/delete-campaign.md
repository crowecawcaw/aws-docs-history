

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Delete an AWS IoT FleetWise campaign
<a name="delete-campaign"></a>

You can use the AWS IoT FleetWise console or API to delete campaigns.

## Delete a campaign (console)
<a name="delete-campaign-console"></a>

To delete a campaign, use the AWS IoT FleetWise console.

**To delete a campaign**

1. <a name="fleetwise-open-console"></a>Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. <a name="choose-campaigns"></a>On the navigation pane, choose **Campaigns**.

1. On the **Campaigns** page, choose the target campaign.

1. Choose **Delete**.

1. In **Delete **campaign-name**?**, enter the name of the campaign to delete, and then choose **Confirm**.

## Delete a campaign (AWS CLI)
<a name="delete-campaign-cli"></a>

You can use the [DeleteCampaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteCampaign.html) API operation to delete a campaign. The following example uses AWS CLI.

To delete a campaign, run the following command.

Replace {{campaign-name}} with the name of the vehicle that you're deleting.

```
aws iotfleetwise delete-campaign --name {{campaign-name}}
```

**Deleted data partitions are not recoverable**  
Deleting a campaign removes all data from devices and the data in a partition won't upload to the cloud.

## Verify campaign deletion
<a name="verify-campaign-deletion"></a>

You can use the [ListCampaigns](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListCampaigns.html) API operation to verify if a campaign has been deleted. The following example uses the AWS CLI.

To retrieve a paginated list of summaries for all campaigns, run the following command.

```
aws iotfleetwise list-campaigns
```