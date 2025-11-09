# Visualize AWS IoT FleetWise vehicle data

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

The Edge Agent for AWS IoT FleetWise software sends selected vehicle data to an MQTT topic, or transfers it to Amazon Timestream
or Amazon Simple Storage Service (Amazon S3). After your data arrives in the data destination, you can use other AWS services
to process, re-route, visualize, and share it.

###### Note

Amazon Timestream is not available in the Asia Pacific (Mumbai) Region.

## Processing vehicle data sent to an MQTT topic

Vehicle data sent by MQTT messaging is delivered in near real-time and allows
you to use Rules to take action, or route data to other destinations. For more
information about using MQTT, see [Device communication protocols](../../../iot/latest/developerguide/protocols.md "../../../iot/latest/developerguide/protocols.md") and [Rules for AWS IoT](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") in the
_AWS IoT Core Developer Guide_.

The default schema of data that is sent in an MQTT message contains the following
fields.

| Field name               | Data type | Description                                                                    |
| ------------------------ | --------- | ------------------------------------------------------------------------------ |
| `eventId`                | varchar   | The ID of the data collection event.                                           |
| `vehicleName`            | varchar   | The ID of the vehicle from which the data was collected.                       |
| `name`                   | varchar   | The name of the campaign that the Edge Agent software uses to collect<br>data. |
| `time`                   | timestamp | The timestamp of the data point.                                               |
| `measure_name`           | varchar   | The name of the signal.                                                        |
| `measure_value::bigint`  | bigint    | Signal values of type Integer.                                                 |
| `measure_value::double`  | double    | Signal values of type Double.                                                  |
| `measure_value::boolean` | boolean   | Signal values of type Boolean.                                                 |
| `measure_value::varchar` | varchar   | Signal values of type varchar.                                                 |

## Process vehicle data in Timestream

Timestream is a fully managed time series database that can store and analyze trillions of
time series data points per day. Your data is stored in a customer managed Timestream table.
You can use Timestream to query vehicle data so that you can gain insights about your
vehicles. For more information, see [What is
Amazon Timestream?](../../../timestream/latest/developerguide/what-is-timestream.md "../../../timestream/latest/developerguide/what-is-timestream.md")

The default schema of data that is transferred to Timestream contains the following
fields.

| Field name               | Data type | Description                                                                    |
| ------------------------ | --------- | ------------------------------------------------------------------------------ |
| `eventId`                | varchar   | The ID of the data collection event.                                           |
| `vehicleName`            | varchar   | The ID of the vehicle from which the data was collected.                       |
| `name`                   | varchar   | The name of the campaign that the Edge Agent software uses to collect<br>data. |
| `time`                   | timestamp | The timestamp of the data point.                                               |
| `measure_name`           | varchar   | The name of the signal.                                                        |
| `measure_value::bigint`  | bigint    | Signal values of type Integer.                                                 |
| `measure_value::double`  | double    | Signal values of type Double.                                                  |
| `measure_value::boolean` | boolean   | Signal values of type Boolean.                                                 |
| `measure_value::varchar` | varchar   | Signal values of type varchar.                                                 |

## Visualize vehicle data stored in Timestream

After your vehicle data is transferred to Timestream, you can use the following AWS
services to visualize, monitor, analyze, and share your data.

- Visualize and monitor data in dashboards by using [Grafana or Amazon Managed Grafana](../../../timestream/latest/developerguide/Grafana.md "../../../timestream/latest/developerguide/Grafana.md"). You can
  visualize data from multiple AWS sources (such as Amazon CloudWatch and Timestream) and
  other data sources with a single Grafana dashboard.
- Analyze and visualize data in dashboards by using [Quick Suite](../../../timestream/latest/developerguide/Quicksight.md "../../../timestream/latest/developerguide/Quicksight.md").

## Process vehicle data in Amazon S3

Amazon S3 is an object storage service that stores and protects any amount of data. You can
use S3 for a variety of use cases, such as data lakes,
backup and restore, archive, enterprise applications, AWS IoT devices, and big data
analytics. Your data is stored in S3 as objects in buckets. For more information, see
[What is
Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")

The default schema of data that is transferred to Amazon S3 contains the following
fields.

| Field name              | Data type | Description                                                                    |
| ----------------------- | --------- | ------------------------------------------------------------------------------ |
| `eventId`               | varchar   | The ID of the data collection event.                                           |
| `vehicleName`           | varchar   | The ID of the vehicle from which the data was collected.                       |
| `name`                  | varchar   | The name of the campaign that the Edge Agent software uses to collect<br>data. |
| `time`                  | timestamp | The timestamp of the data point.                                               |
| `measure_name`          | varchar   | The name of the signal.                                                        |
| `measure_value_BIGINT`  | bigint    | Signal values of type Integer.                                                 |
| `measure_value_DOUBLE`  | double    | Signal values of type Double.                                                  |
| `measure_value_BOOLEAN` | boolean   | Signal values of type Boolean.                                                 |
| `measure_value_STRUCT`  | struct    | Signal values of type Struct.                                                  |
| `measure_value_VARCHAR` | varchar   | Signal values of type varchar.                                                 |

## Amazon S3 object format

AWS IoT FleetWise transfers vehicle data to S3 where it's saved as an object. You can use the
object URI that uniquely identifies the data to find data from the campaign. The S3
object URI format depends on if the collected data is unstructured or processed
data.

Unstructured data is stored in S3 in a not pre-defined manner. It can be in various formats, such as images or videos.

Vehicle messages passed to AWS IoT FleetWise with signal data from Amazon Ion files are decoded and transferred to S3 as objects. The S3 objects represent each signal and are binary encoded.

The unstructured data S3 object URI uses the following format:

```
s3://`bucket-name`/`prefix`/unstructured-data/`random-ID-yyyy-MM-dd-HH-mm-ss-SSS-vehicleName-signalName-fieldName`
```

Processed data is stored in S3 and undergoes processing steps that validate, enrich, and transform messages. Object lists and velocity are examples of processed data.

Data transferred to S3 are stored as objects that represent records that were buffered
for a period of about 10 minutes. By default, AWS IoT FleetWise adds a UTC time prefix in the
format `year=YYYY/month=MM/date=DD/hour=HH` before writing objects to S3.
This prefix creates a logical hierarchy in the bucket where each forward slash
(`/`) creates a level in the hierarchy. The processed data also contains the S3 object URI to unstructured data.

The processed data S3 object URI uses the following format:

```
s3://`bucket-name`/`prefix`/processed-data/year=`YYYY`/month=`MM`/day=`DD`/hour=`HH`/part-0000-`random-ID`.gz.parquet
```

Raw data, also known as primary data, are data collected from Amazon Ion files. You can use raw data to troubleshoot any issues or to root cause errors.

The raw data S3 object URI uses the following format:

```
s3://`bucket-name`/`prefix`/raw-data/`vehicle-name/eventID-timestamp`.10n
```

## Analyze vehicle data stored in Amazon S3

After your vehicle data is transferred to S3, you can use the following AWS
services to monitor, analyze, and share your data.

Extract and analyze data using Amazon SageMaker AI for downstream labeling and machine learning (ML) workflows.

For more information, see the following topics in the _Amazon SageMaker AI Developer Guide_:

- [Process data](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md")
- [Train machine learning models](../../../sagemaker/latest/dg/train-model.md "../../../sagemaker/latest/dg/train-model.md")
- [Label Images](../../../sagemaker/latest/dg/sms-label-images.md "../../../sagemaker/latest/dg/sms-label-images.md")

Catalog your data using AWS Glue crawler and analyze it in Amazon Athena. By default, objects
written to S3 have Apache Hive style time partitions, with data paths that contain
key-value pairs connected by equal signs.

For more information, see the following topics in the _Amazon Athena User
Guide_:

- [Partitioning data in Athena](../../../athena/latest/ug/partitions.md "../../../athena/latest/ug/partitions.md")
- [Using AWS Glue to connect to data sources in Amazon S3](../../../athena/latest/ug/data-sources-glue.md "../../../athena/latest/ug/data-sources-glue.md")
- [Best practices when using Athena with AWS Glue](../../../athena/latest/ug/glue-best-practices.md "../../../athena/latest/ug/glue-best-practices.md")

Visualize data using Quick Suite by either reading your Athena table or S3 bucket directly.

###### Tip

If you're reading from S3 directly, confirm that your vehicle data is in JSON
format because Quick Suite doesn't support Apache Parquet format.

For more information, see the following topics in the _Amazon Quick Suite User
Guide_:

- [Supported data
  sources](../../../quicksight/latest/user/supported-data-sources.md "../../../quicksight/latest/user/supported-data-sources.md")
- [Creating a data
  source](../../../quicksight/latest/user/create-a-data-source.md "../../../quicksight/latest/user/create-a-data-source.md")
