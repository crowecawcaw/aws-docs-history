Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Use runtime properties in Managed Service for Apache Flink

You can use _runtime properties_ to configure your application without recompiling your application code.

###### This topic contains the following sections:

- [Manage runtime properties using the console](#how-properties-console "#how-properties-console")
- [Manage runtime properties using the CLI](#how-properties-cli "#how-properties-cli")
- [Access runtime properties in a Managed Service for Apache Flink application](#how-properties-access "#how-properties-access")

## Manage runtime properties using the console

You can add, update, or remove runtime properties from your Managed Service for Apache Flink application using the
AWS Management Console.

###### Note

If you are using an earlier supported version of Apache Flink and want to upgrade
your existing applications to Apache Flink 1.19.1, you can do so using in-place
Apache Flink version upgrades. With in-place version upgrades, you retain
application traceability against a single ARN across Apache Flink versions,
including snapshots, logs, metrics, tags, Flink configurations, and more. You can
use this feature in `RUNNING` and `READY` state. For more
information, see [Use in-place version upgrades for Apache
Flink](how-in-place-version-upgrades.md "how-in-place-version-upgrades.md").

###### Update Runtime Properties for a Managed Service for Apache Flink application

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.
2. Choose your Managed Service for Apache Flink application. Choose **Application details**.
3. On the page for your application, choose **Configure**.
4. Expand the **Properties** section.
5. Use the controls in the **Properties** section to define a property group with key-value pairs. Use
   these controls to add, update, or remove property groups and runtime properties.
6. Choose **Update**.

## Manage runtime properties using the CLI

You can add, update, or remove runtime properties using the [AWS CLI](../../../cli.md "../../../cli.md").

This section includes example requests for API actions for configuring runtime
properties for an application. For information about how to use a JSON file for input for an API
action, see [Managed Service for Apache Flink API example code](api-examples.md "api-examples.md").

###### Note

Replace the sample account ID (`012345678901`) in the examples following with
your account ID.

### Add runtime properties when creating an application

The following example request for the [`CreateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md") action adds two runtime property groups (`ProducerConfigProperties`
and `ConsumerConfigProperties`) when you
create an application:

```
{
    "ApplicationName": "MyApplication",
    "ApplicationDescription": "my java test app",
    "RuntimeEnvironment": "FLINK-1_19",
    "ServiceExecutionRole": "arn:aws:iam::012345678901:role/MF-stream-rw-role",
    "ApplicationConfiguration": {
        "ApplicationCodeConfiguration": {
            "CodeContent": {
                "S3ContentLocation": {
                    "BucketARN": "arn:aws:s3:::ka-app-code-`username`",
                    "FileKey": "java-getting-started-1.0.jar"
                }
            },
            "CodeContentType": "ZIPFILE"
        },
        "EnvironmentProperties":  {
         "PropertyGroups": [
            {
               "PropertyGroupId": "ProducerConfigProperties",
               "PropertyMap" : {
                    "flink.stream.initpos" : "LATEST",
                    "aws.region" : "us-west-2",
                    "AggregationEnabled" : "false"
               }
            },
            {
               "PropertyGroupId": "ConsumerConfigProperties",
               "PropertyMap" : {
                    "aws.region" : "us-west-2"
               }
            }
         ]
      }
    }
}
```

### Add and update runtime properties in an existing

application

The following example request for the [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") action adds or updates runtime properties for an existing application:

```
{
  "ApplicationName": "MyApplication",
  "CurrentApplicationVersionId": 2,
  "ApplicationConfigurationUpdate": {
    "EnvironmentPropertyUpdates": {
      "PropertyGroups": [
        {
          "PropertyGroupId": "ProducerConfigProperties",
          "PropertyMap" : {
            "flink.stream.initpos" : "LATEST",
            "aws.region" : "us-west-2",
            "AggregationEnabled" : "false"
          }
        },
        {
          "PropertyGroupId": "ConsumerConfigProperties",
          "PropertyMap" : {
            "aws.region" : "us-west-2"
          }
        }
      ]
    }
  }
}
```

###### Note

If you use a key that has no corresponding runtime property in a property group, Managed Service for Apache Flink adds the
key-value pair as a new property. If you use a key for an existing runtime property in a property group,
Managed Service for Apache Flink updates the property value.

### Remove runtime properties

The following example request for the [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") action removes all runtime properties and property groups
from an existing application:

```
{
  "ApplicationName": "MyApplication",
  "CurrentApplicationVersionId": 3,
  "ApplicationConfigurationUpdate": {
    "EnvironmentPropertyUpdates": {
      "PropertyGroups": []
    }
  }
}
```

###### Important

If you omit an existing property group or an existing property key in a property group, that property group or property is removed.

## Access runtime properties in a Managed Service for Apache Flink application

You retrieve runtime properties in your Java application code using the static
`KinesisAnalyticsRuntime.getApplicationProperties()` method, which returns a `Map<String, Properties>`
object.

The following Java code example retrieves runtime properties for your application:

```
 Map<String, Properties> applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties();
```

You retrieve a property group (as a `Java.Util.Properties` object) as follows:

```
Properties consumerProperties = applicationProperties.get("ConsumerConfigProperties");
```

You typically configure an Apache Flink source or sink by passing in the `Properties` object without needing to retrieve the
individual properties. The following code example demonstrates how to create an Flink source by passing in a `Properties` object
retrieved from runtime properties:

```
private static FlinkKinesisProducer<String> createSinkFromApplicationProperties() throws IOException {
  Map<String, Properties> applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties();
  FlinkKinesisProducer<String> sink = new FlinkKinesisProducer<String>(new SimpleStringSchema(),
    applicationProperties.get("ProducerConfigProperties"));

  sink.setDefaultStream(outputStreamName);
  sink.setDefaultPartition("0");
  return sink;
}
```

For code examples, see [Examples for creating and working with Managed Service for Apache Flink
applications](examples-collapsibles.md "examples-collapsibles.md").
