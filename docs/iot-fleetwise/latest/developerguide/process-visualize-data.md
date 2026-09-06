

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Visualize AWS IoT FleetWise vehicle data
<a name="process-visualize-data"></a>

**Important**  
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

The Edge Agent for AWS IoT FleetWise software sends selected vehicle data to an MQTT topic, or transfers it to Amazon Timestream or Amazon Simple Storage Service (Amazon S3). After your data arrives in the data destination, you can use other AWS services to process, re-route, visualize, and share it.

**Note**  
Amazon Timestream is not available in the Asia Pacific (Mumbai) Region.

## Processing vehicle data sent to an MQTT topic
<a name="process-mqtt-data"></a>

Vehicle data sent by MQTT messaging is delivered in near real-time and allows you to use Rules to take action, or route data to other destinations. For more information about using MQTT, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) and [Rules for AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) in the *AWS IoT Core Developer Guide*.

The default schema of data that is sent in an MQTT message contains the following fields.


| Field name | Data type | Description | 
| --- | --- | --- | 
| `eventId` | varchar | The ID of the data collection event. | 
| `vehicleName` | varchar | The ID of the vehicle from which the data was collected. | 
| `name` | varchar | The name of the campaign that the Edge Agent software uses to collect data. | 
| `time` | timestamp | The timestamp of the data point. | 
| `measure_name` | varchar | The name of the signal. | 
| `measure_value::bigint` | bigint | Signal values of type Integer. | 
| `measure_value::double` | double | Signal values of type Double. | 
| `measure_value::boolean` | boolean | Signal values of type Boolean. | 
| `measure_value::varchar` | varchar | Signal values of type varchar. | 

## Process vehicle data in Timestream
<a name="process-vehicle-data"></a>

Timestream is a fully managed time series database that can store and analyze trillions of time series data points per day. Your data is stored in a customer managed Timestream table. You can use Timestream to query vehicle data so that you can gain insights about your vehicles. For more information, see [What is Amazon Timestream?](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html)

The default schema of data that is transferred to Timestream contains the following fields.


| Field name | Data type | Description | 
| --- | --- | --- | 
| `eventId` | varchar | The ID of the data collection event. | 
| `vehicleName` | varchar | The ID of the vehicle from which the data was collected. | 
| `name` | varchar | The name of the campaign that the Edge Agent software uses to collect data. | 
| `time` | timestamp | The timestamp of the data point. | 
| `measure_name` | varchar | The name of the signal. | 
| `measure_value::bigint` | bigint | Signal values of type Integer. | 
| `measure_value::double` | double | Signal values of type Double. | 
| `measure_value::boolean` | boolean | Signal values of type Boolean. | 
| `measure_value::varchar` | varchar | Signal values of type varchar. | 

## Visualize vehicle data stored in Timestream
<a name="visualize-vehicle-data"></a>

After your vehicle data is transferred to Timestream, you can use the following AWS services to visualize, monitor, analyze, and share your data.
+ Visualize and monitor data in dashboards by using [Grafana or Amazon Managed Grafana](https://docs.aws.amazon.com/timestream/latest/developerguide/Grafana.html). You can visualize data from multiple AWS sources (such as Amazon CloudWatch and Timestream) and other data sources with a single Grafana dashboard.
+ Analyze and visualize data in dashboards by using [Quick](https://docs.aws.amazon.com/timestream/latest/developerguide/Quicksight.html).

## Process vehicle data in Amazon S3
<a name="process-vehicle-data-s3"></a>

Amazon S3 is an object storage service that stores and protects any amount of data. You can use S3 for a variety of use cases, such as data lakes, backup and restore, archive, enterprise applications, AWS IoT devices, and big data analytics. Your data is stored in S3 as objects in buckets. For more information, see [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

The default schema of data that is transferred to Amazon S3 contains the following fields.


| Field name | Data type | Description | 
| --- | --- | --- | 
| `eventId` | varchar | The ID of the data collection event. | 
| `vehicleName` | varchar | The ID of the vehicle from which the data was collected. | 
| `name` | varchar | The name of the campaign that the Edge Agent software uses to collect data. | 
| `time` | timestamp | The timestamp of the data point. | 
| `measure_name` | varchar | The name of the signal. | 
| `measure_value_BIGINT` | bigint | Signal values of type Integer. | 
| `measure_value_DOUBLE` | double | Signal values of type Double. | 
| `measure_value_BOOLEAN` | boolean | Signal values of type Boolean. | 
| `measure_value_STRUCT` | struct | Signal values of type Struct. | 
| `measure_value_VARCHAR` | varchar | Signal values of type varchar. | 

## Amazon S3 object format
<a name="visualize-vehicle-data-s3-format"></a>

AWS IoT FleetWise transfers vehicle data to S3 where it's saved as an object. You can use the object URI that uniquely identifies the data to find data from the campaign. The S3 object URI format depends on if the collected data is unstructured or processed data.

### Unstructured data
<a name="unstructured-data"></a>

Unstructured data is stored in S3 in a not pre-defined manner. It can be in various formats, such as images or videos. 

Vehicle messages passed to AWS IoT FleetWise with signal data from Amazon Ion files are decoded and transferred to S3 as objects. The S3 objects represent each signal and are binary encoded.

The unstructured data S3 object URI uses the following format:

```
s3://{{bucket-name}}/{{prefix}}/unstructured-data/{{random-ID-yyyy-MM-dd-HH-mm-ss-SSS-vehicleName-signalName-fieldName}}
```

### Processed data
<a name="processed-data"></a>

Processed data is stored in S3 and undergoes processing steps that validate, enrich, and transform messages. Object lists and velocity are examples of processed data. 

Data transferred to S3 are stored as objects that represent records that were buffered for a period of about 10 minutes. By default, AWS IoT FleetWise adds a UTC time prefix in the format `year=YYYY/month=MM/date=DD/hour=HH` before writing objects to S3. This prefix creates a logical hierarchy in the bucket where each forward slash (`/`) creates a level in the hierarchy. The processed data also contains the S3 object URI to unstructured data.

The processed data S3 object URI uses the following format:

```
s3://{{bucket-name}}/{{prefix}}/processed-data/year={{YYYY}}/month={{MM}}/day={{DD}}/hour={{HH}}/part-0000-{{random-ID}}.gz.parquet
```

### Raw data
<a name="raw-data"></a>

Raw data, also known as primary data, are data collected from Amazon Ion files. You can use raw data to troubleshoot any issues or to root cause errors.

The raw data S3 object URI uses the following format:

```
s3://{{bucket-name}}/{{prefix}}/raw-data/{{vehicle-name/eventID-timestamp}}.10n
```

## Analyze vehicle data stored in Amazon S3
<a name="analyze-vehicle-data-s3"></a>

After your vehicle data is transferred to S3, you can use the following AWS services to monitor, analyze, and share your data.

Extract and analyze data using Amazon SageMaker AI for downstream labeling and machine learning (ML) workflows.

For more information, see the following topics in the *Amazon SageMaker AI Developer Guide*:
+ [Process data](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)
+ [Train machine learning models](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html)
+ [Label Images](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-label-images.html)

Catalog your data using AWS Glue crawler and analyze it in Amazon Athena. By default, objects written to S3 have Apache Hive style time partitions, with data paths that contain key-value pairs connected by equal signs.

For more information, see the following topics in the *Amazon Athena User Guide*:
+ [Partitioning data in Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)
+ [Using AWS Glue to connect to data sources in Amazon S3](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)
+ [Best practices when using Athena with AWS Glue](https://docs.aws.amazon.com/athena/latest/ug/glue-best-practices.html)

Visualize data using Quick by either reading your Athena table or S3 bucket directly.

**Tip**  
If you're reading from S3 directly, confirm that your vehicle data is in JSON format because Quick doesn't support Apache Parquet format.

For more information, see the following topics in the *Amazon Quick User Guide*:
+ [Supported data sources](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html)
+ [Creating a data source](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-source.html)