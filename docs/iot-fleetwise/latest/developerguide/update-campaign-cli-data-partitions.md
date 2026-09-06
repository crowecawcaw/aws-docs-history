

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Upload campaign data
<a name="update-campaign-cli-data-partitions"></a>

**Important**  
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

There are two ways to upload campaign data on the Edge:
+ Campaigns that meet your upload conditions will automatically upload data to the cloud after they are approved. To approve a campaign, use the `updateCampaign` API operation. 
+ Through AWS IoT Jobs, you can force data to upload even when specified conditions are not met. For more information, see [Upload data using AWS IoT Jobs](update-campaign-cli-data-partitions-jobs.md).

**To upload campaign data using the `UpdateCampaign` API operation**

After you create the campaign, the campaign status displays as `WAITING_FOR_APPROVAL` until you change the `action` to `APPROVED`.
+ Use the following sample to update the campaign `action` by calling on the [UpdateCampaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateCampaign.html) API operation.

  ```
  {
     "action": "APPROVED",
     "dataExtraDimensions": [ "string" ],
     "description": "string",
     "name": "string"
  }
  ```