# Create an AWS IoT FleetWise campaign

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can use the AWS IoT FleetWise console or API to create campaigns to collect vehicle
data.

###### Important

For your campaign to work, you must have the following:

- The Edge Agent software is running in your vehicle. For more information about how
  to develop, install, and work with the Edge Agent software, do the following:
  1.  Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
  2.  On the service home page, in the **Get started with AWS IoT FleetWise**
      section, choose **Explore Edge Agent**.

- You've set up AWS IoT Core to provision your vehicle. For more information,
  see [Provision AWS IoT FleetWise vehicles](provision-vehicles.md "provision-vehicles.md").

###### Topics

- [Create a campaign (console)](#create-campaign-console "#create-campaign-console")
- [Create a campaign (AWS CLI)](#create-campaign-cli "#create-campaign-cli")
- [Logical expressions for AWS IoT FleetWise
  campaigns](logical-expression.md "logical-expression.md")

## Create a campaign (console)

Use the AWS IoT FleetWise console to create a campaign to select, collect, and transfer
vehicle data to the cloud.

###### To create a campaign

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
2. On the navigation pane, choose **Campaigns**.
3. On the **Campaigns** page, choose **Create
   campaign**, and then complete the steps in the following
   topics.

###### Topics

- [Step 1: Configure campaign](#configure-campaign-console "#configure-campaign-console")
- [Step 2: Specify storage and upload conditions](#specify-storage-upload-conditions "#specify-storage-upload-conditions")
- [Step 3: Configure data destination](#configure-data-collection-scheme-console "#configure-data-collection-scheme-console")
- [Step 4: Add vehicles](#add-attributes-console "#add-attributes-console")
- [Step 5: Review and
  create](#review-and-create-campaign-console "#review-and-create-campaign-console")
- [Step 6: Deploy a campaign](#update-campaign-console "#update-campaign-console")

###### Important

- You must have a signal catalog and a vehicle before you create a
  campaign. For more information, see [Manage AWS IoT FleetWise signal catalogs](signal-catalogs.md "signal-catalogs.md") and [Manage AWS IoT FleetWise vehicles](vehicles.md "vehicles.md").
- After a campaign is created, you must approve the campaign. For more
  information, see [Update an AWS IoT FleetWise campaign](update-campaign-cli.md "update-campaign-cli.md").

### Step 1: Configure campaign

In **General information**, do the following:

1. Enter a name for the campaign.
2. (Optional) Enter a description.

Configure the campaign's data collection scheme. A data collection scheme
gives the Edge Agent software instructions on what data to collect or when to collect it.
In the AWS IoT FleetWise console, you can configure a data collection scheme in the
following ways:

- Manually define the data collection scheme.
- Upload a file to automatically define the data collection
  scheme.

In **Configuration option**, choose one of the
following:

- To manually specify the type of data collection scheme and define
  options to customize the scheme, choose **Define data collection
  scheme**.

Manually specify the type of data collection scheme and
define options to customize the scheme.

    1. In the **Data collection scheme
     details** section, choose the type of
     data collection scheme you want this campaign to
     use. To use a logical expression to recognize what
     vehicle data to collect, choose
     **Condition-based**. To use a
     specific time period to decide how often to collect
     vehicle data, choose
     **Time-based**.
    2. Define the duration of time the campaign collects
     data.


    ###### Note

    By default, an approved campaign is activated
     immediately and doesn't have a set end time. To
     avoid extra charges, you must specify a time
     range.
    3. If you specified a condition-based data collection
     scheme, you must define a logical expression to
     recognize what data to collect. AWS IoT FleetWise uses a
     logical expression to recognize what data to collect
     for a condition-based scheme. The expression must
     specify a signal's fully qualified name as a
     variable, a comparison operator, and a comparison
     value.


    For example, if you specify the
     `$variable.`myVehicle.InVehicleTemperature`
     > 50.0` expression, AWS IoT FleetWise collects
     temperature values that are greater than 50.0. For
     instructions about how to write expressions, see
     [Logical expressions for AWS IoT FleetWise
     campaigns](logical-expression.md "logical-expression.md").


    Enter the logical expression used to recognize
     what data to collect.
    4. (Optional) Specify the language version of the
     conditional expression. The default value is
     1.
    5. (Optional) Specify the minimum trigger interval,
     which is the smallest duration of time between two
     data collection events. For example, if a signal
     changes often, you might want to collect data at a
     slower rate.
    6. Specify the **Trigger mode**
     condition for the Edge Agent software to collect data. By
     default, the Edge Agent for AWS IoT FleetWise software
     **Always** collects data whenever
     the condition is met. Or, it can collect data only
     when the condition is met for the first time,
     **On first trigger**.
    7. If you specified a time-based data collection
     scheme, you must specify a time
     **Period**, in milliseconds, from
     10,000 ‐ 60,000 milliseconds. The Edge Agent software
     uses the time period to decide how often to collect
     data.
    8. (Optional) Edit the scheme’s **Advanced
     scheme options**.


    	1. To save wireless bandwidth and reduce
    	 network traffic by compressing data, choose
    	 **Snappy**.
    	2. (Optional) To define how long, in
    	 milliseconds, to continue collecting data after a
    	 data collection event, you can specify the
    	 **Post trigger collection
    	 duration**.
    	3. (Optional) To indicate the priority level of
    	 the campaign, specify the campaign
    	 **Priority**. Campaigns with a
    	 smaller number for priority are deployed first and
    	 are considered to have a higher priority.
    	4. The Edge Agent software can temporarily store data
    	 locally when a vehicle isn't connected to the
    	 cloud. After the connection is reestablished, the
    	 data stored locally is automatically transferred
    	 to the cloud. Specify if you want the Edge Agent
    	 to **Store data locally** during
    	 a lost connection.
    	5. (Optional) To provide additional information
    	 for a signal, add up to five attributes as
    	 **Extra data dimensions**.

- To upload a file to define the data collection scheme, select
  **Upload a .json file from your local device**.
  AWS IoT FleetWise automatically defines which options that you can define in the
  file. You can review and update the selected options.

Upload a .json file with details about the data collection
scheme.

    1. To import information about the data collection
     scheme, choose **Choose files**.
     For more information about the required file format,
     see the [CreateCampaign](../APIReference/API_CreateCampaign.md#API_CreateCampaign "../APIReference/API_CreateCampaign.md#API_CreateCampaign") API documentation.


    ###### Note

    AWS IoT FleetWise currently supports the .json file
     format extension.
    2. AWS IoT FleetWise automatically defines the data collection
     scheme based on the information in your file. Review
     the options that AWS IoT FleetWise selected for you. You can
     update the options, if needed.

### Step 2: Specify storage and upload conditions

To choose if the Edge Agent software will temporarily store data locally when a vehicle isn't connected to the cloud, specify the spooling mode.

- In **Data spooling mode**, choose one of the following:
  - **Not stored** – The Edge Agent software collects but doesn't temporarily store data locally when a vehicle is offline. The Edge Agent software transfers data to the cloud when the vehicle reconnects.
  - **Stored to disk** – The Edge Agent software collects and temporarily stores data locally when a vehicle is offline. Collected data is temporarily stored at a location defined by the Edge Agent config file “persistency” section. The Edge Agent transfers data to the cloud when the vehicle reconnects.
  - **Stored to disk with partitions** – The vehicle always temporarily stores data on the Edge in your specified data partition. You can choose when you want to forward your stored data to the cloud.
    1. (Optional) Enter a partition ID to designate a particular set of data.
    2. Enter a folder name as the location where data will be stored. The absolute path of the storage location is `{persistency_path} / {vehicle_name} / {campaign_name} / {storage_location}`.
    3. Enter the maximum storage size of the data stored in the partition. Newer data overwrites older data when the partition reaches the maximum size.
    4. Enter the minimum amount of time that data in this partition will be kept on the disk.
    5. (Optional) Enter upload conditions for the partition.

#### Specify signals

You can specify the signals to collect data from during the campaign.

###### To specify the signals to collect data from

1. Select the **Signal name**.
2. (Optional) For **Max sample count**, enter the
   maximum number of data samples that the Edge Agent software collects and
   transfers to the cloud during the campaign.
3. (Optional) For **Min sampling interval**, enter
   the minimum duration of time between two data sample collection
   events, in milliseconds. If a signal changes often, you can use this
   parameter to collect data at a slower rate.
4. To add another signal, choose **Add more
   signals**. You can add up to 999 signals.
5. Choose **Next**.

### Step 3: Configure data destination

###### Note

If the campaign contains vision system data signals, you can only store the vehicle data in Amazon S3. You can't store it in Timestream or send it to an MQTT topic.

Vision system data is in preview release and is subject to change.

Amazon Timestream is not available in the Asia Pacific (Mumbai) Region.

Choose the destination where you want to send or store data collected by the campaign.
You can send vehicle data to an MQTT topic, or
store it in Amazon S3 or Amazon Timestream.

In **Destination settings**, do the following:

- Choose Amazon S3, Amazon Timestream, or MQTT topic from the dropdown list.

###### Important

You can only transfer data to S3 if AWS IoT FleetWise has permissions to write
into the S3 bucket. For more information about granting access, see
[Controlling
access with AWS IoT FleetWise](controlling-access.md "controlling-access.md").

To store vehicle data in an S3 bucket, choose **Amazon S3**. S3 is an
object storage service that stores data as objects within buckets. For more information,
see [Creating, configuring, and working with Amazon S3 buckets](../../../AmazonS3/latest/userguide/creating-buckets-s3.md "../../../AmazonS3/latest/userguide/creating-buckets-s3.md") in the _Amazon Simple Storage Service
User Guide_.

S3 optimizes the cost of data storage and provides additional mechanisms to
use vehicle data, such as data lakes, centralized data storage, data processing
pipelines, and analytics. You can use S3 to store data for batch processing and
analysis. For example, you can create reports of hard-braking events for your
machine learning (ML) model. Incoming vehicle data is buffered for 10 minutes
before delivery.

In **S3 destination settings**, do the following:

1. For **S3 bucket**, choose a bucket that AWS IoT FleetWise
   has permissions to.
2. (Optional) Enter a custom prefix that you can use to organize data
   stored in the S3 bucket.
3. Choose the output format, which is the format files that are
   saved as in the S3 bucket.
4. Choose if you want to compress data stored in the S3 bucket as
   a .gzip file. We recommend compressing data because it minimizes
   storage costs.
5. The options you select in **S3 destination
   settings** change the **Example S3 object
   URI**. This is an example of what files are saved
   as in S3.

###### Important

You can only transfer data to a table if AWS IoT FleetWise has permissions to
write data into Timestream. For more information about granting access,
see [Controlling access with AWS IoT FleetWise](controlling-access.md "controlling-access.md").

Amazon Timestream is not available in the Asia Pacific (Mumbai) Region.

To store vehicle data in a Timestream table, choose **Amazon Timestream**.
You can use Timestream to query vehicle data so that you can identify trends and patterns.
For example, you can use Timestream to create an alarm for vehicle fuel level. Incoming
vehicle data is transferred to Timestream in near real time. For more information, see
[What is Amazon Timestream?](../../../timestream/latest/developerguide/what-is-timestream.md "../../../timestream/latest/developerguide/what-is-timestream.md") in the _Amazon Timestream Developer Guide_.

In **Timestream table settings**, do the following:

1. For **Timestream database name**, choose the name of
   your Timestream database from the dropdown list.
2. For **Timestream table name**, choose the name of your
   Timestream table from the dropdown list.
   In **Service access for Timestream**, do the following:

- Choose an IAM role from the dropdown list.

###### Important

You can only route data to an MQTT topic if AWS IoT FleetWise has permissions to AWS IoT topics. For more information about granting access, see
[Controlling
access with AWS IoT FleetWise](controlling-access.md "controlling-access.md").

To send vehicle data to an MQTT topic, choose **MQTT topic**.

Vehicle data sent by MQTT messaging is delivered in near real-time and allows
you to use rules to take action, or route data to other destinations. For more
information about using MQTT, see [Device communication protocols](../../../iot/latest/developerguide/protocols.md "../../../iot/latest/developerguide/protocols.md") and [Rules for AWS IoT](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") in the
_AWS IoT Core Developer Guide_.

1. Under **MQTT topic**, enter the **Topic
   name**.
2. Under **Service access for MQTT topic**, choose
   whether you want to let AWS IoT FleetWise **Create and use a new service
   role** for you. If you want to **Use an existing service
   role**, select the role in the dropdown list under
   **Select role**.

- Choose **Next**.

### Step 4: Add vehicles

To choose which vehicles to deploy your campaign to, select them in the vehicles
list. Filter vehicles by searching for the attributes and their values that you added
when creating the vehicles, or by vehicle name.

In **Filter vehicles**, do the following:

1. In the search box, find the attribute or vehicle name and choose it
   from the list.

###### Note

Each attribute can be used only once. 2. Enter the value of the attribute or the vehicle name that you want to
deploy the campaign to. For example, if the fully qualified name of the
attribute is `fuelType`, enter `gasoline` as its
value. 3. To search for another vehicle attribute, repeat the preceding steps.
You can search for up to five vehicle attributes and an unlimited number
of vehicle names. 4. Vehicles that match your search are listed under **Vehicle
name**. Choose the vehicles that you want the campaign to
deploy to.

###### Note

Up to 100 vehicles are displayed in search results. Choose
**Select all** to add all vehicles to the
campaign. 5. Choose **Next**.

### Step 5: Review and

create

Verify the configurations for the campaign, and then choose **Create
campaign**.

###### Note

After a campaign is created, you or your team must deploy the campaign to
vehicles.

### Step 6: Deploy a campaign

After you create a campaign, you or your team must deploy the campaign to
vehicles.

###### To deploy a campaign

1. On the **Campaign summary** page, choose
   **Deploy**.
2. Review and confirm that you want to start the deployment and begin
   collecting data from vehicles connected to the campaign.
3. Choose **Deploy**.

If you want to pause collecting data from vehicles connected to the campaign,
on the **Campaign summary** page, choose
**Suspend**. To resume collecting data from vehicles
connected to the campaign, choose **Resume**.

## Create a campaign (AWS CLI)

You can use the [CreateCampaign](../APIReference/API_CreateCampaign.md "../APIReference/API_CreateCampaign.md")
API operation to create a campaign. The following example uses the AWS CLI.

When you create a campaign, data collected from vehicles can be sent to an MQTT
topic or stored in either Amazon S3 (S3) or Amazon Timestream. Choose Timestream for a fast, scalable,
and server-less time series database, such as to store data that requires near real time
processing. Choose S3 for object storage with industry-leading scalability, data availability,
security, and performance. Choose MQTT to deliver data in near real-time and to use
[Rules
for AWS IoT](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") to perform actions you define or route the data to other destinations.

###### Important

You can only transfer vehicle data to an MQTT topic, Amazon S3, or Amazon Timestream if AWS IoT FleetWise has
permissions to send MQTT messages on your behalf, or to write data into S3 or Timestream.
For more information about granting access, see [Controlling access with
AWS IoT FleetWise](controlling-access.md "controlling-access.md").

Amazon Timestream is not available in the Asia Pacific (Mumbai) Region.

### Create campaign

###### Important

- You must have a signal catalog and a vehicle or fleet before you
  create a campaign. For more information, see [Manage AWS IoT FleetWise signal catalogs](signal-catalogs.md "signal-catalogs.md"), [Manage AWS IoT FleetWise vehicles](vehicles.md "vehicles.md"), and [Manage fleets in AWS IoT FleetWise](fleets.md "fleets.md").
- After a campaign is created, you must use the
  `UpdateCampaign` API operation to approve the campaign.
  For more information, see [Update an AWS IoT FleetWise campaign](update-campaign-cli.md "update-campaign-cli.md")

To create a campaign, run the following command.

Replace `file-name` with the name of the .json file that
contains the campaign configuration.

```
aws iotfleetwise create-campaign --cli-input-json file://`file-name`.json
```

- Replace `campaign-name` with the name
  of the campaign that you're creating.
- Replace `signal-catalog-arn` with the
  Amazon Resource Name (ARN) of the signal catalog.
- Replace `target-arn` with the ARN of
  a fleet or vehicle that you created.
- Replace `bucket-arn` with the ARN of
  the S3 bucket.

```
{
    "name": "`campaign-name`",
    "targetArn": "`target-arn`",
    "signalCatalogArn": "`signal-catalog-arn`",
    "collectionScheme": {
        "conditionBasedCollectionScheme": {
            "conditionLanguageVersion": 1,
            "expression": "$variable.`Vehicle.DemoBrakePedalPressure` > 7000",
            "minimumTriggerIntervalMs": 1000,
            "triggerMode": "ALWAYS"
        }
    },
    "compression": "SNAPPY",
    "diagnosticsMode": "OFF",
    "postTriggerCollectionDuration": 1000,
    "priority": 0,
    "signalsToCollect": [
        {
         "maxSampleCount": 100,
         "minimumSamplingIntervalMs": 0,
         "name": "Vehicle.DemoEngineTorque"
        },
        {
         "maxSampleCount": 100,
         "minimumSamplingIntervalMs": 0,
         "name": "Vehicle.DemoBrakePedalPressure"
        }
    ],
    "spoolingMode": "TO_DISK",
    "dataDestinationConfigs": [
        {
         "s3Config": {
             "bucketArn": "`bucket-arn`",
             "dataFormat": "PARQUET",
             "prefix": "`campaign-name`",
              "storageCompressionFormat": "GZIP"
      }
    }
  ],
     "dataPartitions": [
      { ...  }
  ]
}
```

###### Note

Amazon Timestream is not available in the Asia Pacific (Mumbai) Region.

- Replace `campaign-name` with the
  name of the campaign that you're creating.
- Replace `signal-catalog-arn` with the ARN of the signal catalog.
- Replace `target-arn` with the ARN
  of a fleet or vehicle that you created.
- Replace `role-arn` with the ARN of the
  task execution role that grants AWS IoT FleetWise permission to deliver data
  to the Timestream table.
- Replace `table-arn` with the ARN
  of the Timestream table.

```
{
  "name": "campaign-name",
  "targetArn": "target-arn",
  "signalCatalogArn": "signal-catalog-arn",
  "collectionScheme": {
    "conditionBasedCollectionScheme": {
      "conditionLanguageVersion": 1,
      "expression": "$variable.`Vehicle.DemoBrakePedalPressure` > 7000",
      "minimumTriggerIntervalMs": 1000,
      "triggerMode": "ALWAYS"
    }
  },
  "compression": "SNAPPY",
  "diagnosticsMode": "OFF",
  "postTriggerCollectionDuration": 1000,
  "priority": 0,
  "signalsToCollect": [
    {
      "maxSampleCount": 100,
      "minimumSamplingIntervalMs": 0,
      "name": "Vehicle.DemoEngineTorque"
    },
    {
      "maxSampleCount": 100,
      "minimumSamplingIntervalMs": 0,
      "name": "Vehicle.DemoBrakePedalPressure"
    }
  ],
  "spoolingMode": "TO_DISK",
  "dataDestinationConfigs": [
    {
      "timestreamConfig": {
        "executionRoleArn": "role-arn",
        "timestreamTableArn": "table-arn"
      }
    }
  ],
   "dataPartitions": [
      { ...  }
  ]
}
```

- Replace `campaign-name` with the name
  of the campaign that you're creating.
- Replace `signal-catalog-arn` with the
  Amazon Resource Name (ARN) of the signal catalog.
- Replace `target-arn` with the ARN of
  a fleet or vehicle that you created.
- Replace `topic-arn` with the ARN of
  the [MQTT topic](../../../iot/latest/developerguide/topics.md "../../../iot/latest/developerguide/topics.md") that you specified as the
  destination for messages containing vehicle data.
- Replace `role-arn` with the ARN of the
  task execution role that grants AWS IoT FleetWise permission to send, receive,
  and take action on messages for the MQTT topic you specified.

```
{
  "name": "`campaign-name`",
  "targetArn": "`target-arn`",
  "signalCatalogArn": "`signal-catalog-arn`",
  "collectionScheme": {
    "conditionBasedCollectionScheme": {
      "conditionLanguageVersion": 1,
      "expression": "$variable.`Vehicle.DemoBrakePedalPressure` > 7000",
      "minimumTriggerIntervalMs": 1000,
      "triggerMode": "ALWAYS"
    }
  },
  "compression": "SNAPPY",
  "diagnosticsMode": "OFF",
  "postTriggerCollectionDuration": 1000,
  "priority": 0,
  "signalsToCollect": [
    {
      "maxSampleCount": 100,
      "minimumSamplingIntervalMs": 0,
      "name": "Vehicle.DemoEngineTorque"
    },
    {
      "maxSampleCount": 100,
      "minimumSamplingIntervalMs": 0,
      "name": "Vehicle.DemoBrakePedalPressure"
    }
  ],
  "spoolingMode": "TO_DISK",
  "dataDestinationConfigs": [
      {
          "mqttTopicConfig": {
              "mqttTopicArn": "`topic-arn`",
              "executionRoleArn": "`role-arn`"
          }
      }
  ]
}
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `CreateCampaign` API operation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS_KEY_ID`"
 ]
 }
 ]
}`

```
