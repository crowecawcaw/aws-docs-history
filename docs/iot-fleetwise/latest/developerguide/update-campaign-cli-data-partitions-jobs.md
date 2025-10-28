# Upload data using AWS IoT

Jobs

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

With AWS IoT Jobs, you can configure campaigns to upload stored vehicle data
to the cloud whenever you need it.

###### To create a job document for your campaign

- Use the following example to create a job document for the campaign. A job
  document is a .json file that contains information about vehicles or fleets
  required to perform a job. For more information on creating job document,
  see [Create and manage
  jobs by using the AWS CLI](../../../iot/latest/developerguide/manage-job-cli.md "../../../iot/latest/developerguide/manage-job-cli.md") in the
  _AWS IoT Developer Guide_.

To request that only one vehicle uploads data, set the job target to the AWS IoT thing that's associated with the vehicle. To request that multiple vehicles (in the same campaign) upload data, create a thing group of all things corresponding with the vehicles, and then set the job target to the thing group.

```
{
  "version": "1.0",
  "parameters": {
     "campaignArn": ${aws:iot:parameter:`campaignArn`},
     "endTime": ${aws:iot:parameter:`endTime`}
  }
}

```

    1. Replace `CampaignArn` with the Amazon Resource Name (ARN) of a campaign in the same Region and account. The campaign ARN is required.
    2. (Optional) Replace `endTime` with the timestamp of data collected on the vehicle in ISO 8601 UTC format (without milliseconds). For example, `2024-03-05T23:00:00Z`. The timestamp is exclusive and determines the last datapoint to be uploaded. If you omit `endTime`, the Edge Agent software continues to upload until all of a campaign's stored data is uploaded. After all data is uploaded, it updates the
     [job execution status](../../../iot/latest/developerguide/iot-jobs-lifecycle.md#iot-job-execution-states "../../../iot/latest/developerguide/iot-jobs-lifecycle.md#iot-job-execution-states") to `SUCCEEDED`. The
     job's [state](../../../iot/latest/developerguide/iot-jobs-lifecycle.md#iot-jobs-states "../../../iot/latest/developerguide/iot-jobs-lifecycle.md#iot-jobs-states") updates to `COMPLETED`.

###### To create a job using a managed job template

1.  Choose **IoT-IoTFleetWise-CollectCampaignData** from the list of managed templates. For more information, see [Create a job from AWS managed templates](../../../iot/latest/developerguide/job-template-manage-console-create.md "../../../iot/latest/developerguide/job-template-manage-console-create.md") in the
    _AWS IoT Developer Guide_.
2.  The managed template has the `CampaignArn` and `endTime` parameters.

        1. Replace `CampaignArn` with the Amazon Resource Name (ARN) of a campaign in the same Region and account. The campaign ARN is required.
        2. (Optional) Replace `endTime` with the timestamp of data collected on the vehicle in ISO 8601 UTC format (without milliseconds). For example, `2024-03-05T23:00:00Z`. The timestamp is exclusive and determines the last datapoint to be uploaded. If you omit `endTime`, the Edge Agent software continues to upload until all of a campaign's stored data is uploaded. After all data is uploaded, it updates the [job execution status](../../../iot/latest/developerguide/iot-jobs-lifecycle.md#iot-job-execution-states "../../../iot/latest/developerguide/iot-jobs-lifecycle.md#iot-job-execution-states") to `SUCCEEDED`. The
         job's [state](../../../iot/latest/developerguide/iot-jobs-lifecycle.md#iot-jobs-states "../../../iot/latest/developerguide/iot-jobs-lifecycle.md#iot-jobs-states") updates to `COMPLETED`.

    For related troubleshooting topics, see [Store and forward issues](troubleshooting-campaign.md "troubleshooting-campaign.md").

For more information on AWS IoT Jobs, see [Jobs](../../../iot/latest/developerguide/iot-jobs.md "../../../iot/latest/developerguide/iot-jobs.md") in the
_AWS IoT Developer Guide_.
