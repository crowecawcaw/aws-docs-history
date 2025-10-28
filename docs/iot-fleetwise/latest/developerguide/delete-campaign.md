# Delete an AWS IoT FleetWise campaign

You can use the AWS IoT FleetWise console or API to delete campaigns.

## Delete a campaign (console)

To delete a campaign, use the AWS IoT FleetWise console.

###### To delete a campaign

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
2. On the navigation pane, choose **Campaigns**.
3. On the **Campaigns** page, choose the target
   campaign.
4. Choose **Delete**.
5. In **Delete `campaign-name`?**, enter the
   name of the campaign to delete, and then choose **Confirm**.

## Delete a campaign (AWS CLI)

You can use the [DeleteCampaign](../APIReference/API_DeleteCampaign.md "../APIReference/API_DeleteCampaign.md") API operation to delete a campaign. The following
example uses AWS CLI.

To delete a campaign, run the following command.

Replace `campaign-name` with the name of the vehicle that
you're deleting.

```
aws iotfleetwise delete-campaign --name `campaign-name`
```

###### Deleted data partitions are not recoverable

Deleting a campaign removes all data from devices and the data in a partition
won't upload to the cloud.

## Verify campaign deletion

You can use the [ListCampaigns](../APIReference/API_ListCampaigns.md "../APIReference/API_ListCampaigns.md")
API operation to verify if a campaign has been deleted. The following example uses the
AWS CLI.

To retrieve a paginated list of summaries for all campaigns, run the following
command.

```
aws iotfleetwise list-campaigns
```
