

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Upload data using AWS IoT Jobs
<a name="update-campaign-cli-data-partitions-jobs"></a>

**Important**  
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

With AWS IoT Jobs, you can configure campaigns to upload stored vehicle data to the cloud whenever you need it.

**To create a job document for your campaign**
+ Use the following example to create a job document for the campaign. A job document is a .json file that contains information about vehicles or fleets required to perform a job. For more information on creating job document, see [Create and manage jobs by using the AWS CLI](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html) in the *AWS IoT Developer Guide*.

  To request that only one vehicle uploads data, set the job target to the AWS IoT thing that's associated with the vehicle. To request that multiple vehicles (in the same campaign) upload data, create a thing group of all things corresponding with the vehicles, and then set the job target to the thing group.

  ```
  {
    "version": "1.0",
    "parameters": {
       "campaignArn": ${aws:iot:parameter:{{campaignArn}}},
       "endTime": ${aws:iot:parameter:{{endTime}}}
    }
  }
  ```

  1. Replace `CampaignArn` with the Amazon Resource Name (ARN) of a campaign in the same Region and account. The campaign ARN is required.

  1. (Optional) Replace `endTime` with the timestamp of data collected on the vehicle in ISO 8601 UTC format (without milliseconds). For example, `2024-03-05T23:00:00Z`. The timestamp is exclusive and determines the last datapoint to be uploaded. If you omit `endTime`, the Edge Agent software continues to upload until all of a campaign's stored data is uploaded. After all data is uploaded, it updates the [job execution status](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs-lifecycle.html#iot-job-execution-states) to `SUCCEEDED`. The job's [state](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs-lifecycle.html#iot-jobs-states) updates to `COMPLETED`.

**To create a job using a managed job template**

1. Choose **IoT-IoTFleetWise-CollectCampaignData** from the list of managed templates. For more information, see [Create a job from AWS managed templates](https://docs.aws.amazon.com/iot/latest/developerguide/job-template-manage-console-create.html) in the *AWS IoT Developer Guide*.

1. The managed template has the `CampaignArn` and `endTime` parameters.

   1. Replace `CampaignArn` with the Amazon Resource Name (ARN) of a campaign in the same Region and account. The campaign ARN is required.

   1. (Optional) Replace `endTime` with the timestamp of data collected on the vehicle in ISO 8601 UTC format (without milliseconds). For example, `2024-03-05T23:00:00Z`. The timestamp is exclusive and determines the last datapoint to be uploaded. If you omit `endTime`, the Edge Agent software continues to upload until all of a campaign's stored data is uploaded. After all data is uploaded, it updates the [job execution status](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs-lifecycle.html#iot-job-execution-states) to `SUCCEEDED`. The job's [state](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs-lifecycle.html#iot-jobs-states) updates to `COMPLETED`.

For related troubleshooting topics, see [Store and forward issues](troubleshooting-campaign.md).

For more information on AWS IoT Jobs, see [Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) in the *AWS IoT Developer Guide*.