# Use Spark properties to specify custom configuration

When you create or edit a session in Amazon Athena for Apache Spark, you can use [Spark
properties](https://spark.apache.org/docs/latest/configuration.html#spark-properties "https://spark.apache.org/docs/latest/configuration.html#spark-properties") to specify `.jar` files, packages, or another
custom configuration for the session. To specify your Spark properties, you can use the
Athena console, the AWS CLI, or the Athena API.

## Use the Athena console to specify Spark properties

In the Athena console, you can specify your Spark properties when you [create a
notebook](notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook "notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook") or [edit a
current session](notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details "notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details").

###### To add properties in the **Create notebook** or **Edit session details** dialog box

1. Expand **Spark properties**.
2. To add your properties, use the **Edit in table** or
   **Edit in JSON** option.
   - For the **Edit in table** option, choose
     **Add property** to add a property, or choose
     **Remove** to remove a property. Use the
     **Key** and **Value** boxes to
     enter property names and their values.
     - To add a custom `.jar` file, use the
       `spark.jars` property.
     - To specify a package file, use the
       `spark.jars.packages` property.

   - To enter and edit your configuration directly, choose the
     **Edit in JSON** option. In the JSON text editor,
     you can perform the following tasks:
     - Choose **Copy** to copy the JSON text to the
       clipboard.
     - Choose **Clear** to remove all text from the
       JSON editor.
     - Choose the settings (gear) icon to configure line wrapping or
       choose a color theme for the JSON editor.

### Notes

- You can set properties in Athena for Spark, which is the same as setting
  [Spark properties](https://spark.apache.org/docs/latest/configuration.html#spark-properties "https://spark.apache.org/docs/latest/configuration.html#spark-properties") directly on a [SparkConf](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.html "https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.html") object.
- Start all Spark properties with the `spark.` prefix. Properties
  with other prefixes are ignored.
- Not all Spark properties are available for custom configuration on Athena.
  If you submit a `StartSession` request that has a restricted
  configuration, the session fails to start.
  - You cannot use the `spark.athena.` prefix because it is
    reserved.

## Use the AWS CLI or Athena API to provide custom configuration

To use the AWS CLI or Athena API to provide your session configuration, use the [StartSession](../APIReference/API_StartSession.md "../APIReference/API_StartSession.md") API action or the
[start-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-session.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-session.html") CLI command. In your `StartSession` request, use
the `SparkProperties` field of [EngineConfiguration](../APIReference/API_EngineConfiguration.md "../APIReference/API_EngineConfiguration.md") object
to pass your configuration information in JSON format. This starts a session with your
specified configuration.

To specify custom Spark properties from the AWS CLI, use `engine-configuration` configuration when you start an interactive session.

```
aws athena start-session \
--region "REGION"
--work-group "WORKGROUP" \
--engine-configuration '{
    "Classifications": [{
      "Name": "spark-defaults",
      "Properties": {
        "spark.dynamicAllocation.minExecutors": "1",
        "spark.dynamicAllocation.initialExecutors": "2",
        "spark.dynamicAllocation.maxExecutors": "10",
        "spark.dynamicAllocation.executorIdleTimeout": "300"
      }
    }]
  }'
```

You can also specify configuration defaults at the Workgroup level using the `CreateWorkgroup` API action or the `UpdateWorkgroup` API action. Configuration defaults defined at the workgroup applies to all Sessions started for that workgroup.

To specify default Spark properties from the AWS CLI for a workgroup, use the `engine-configuration` configuration when creating a new Workgroup:

```
aws athena create-work-group \
  --region "REGION" \
  --name "WORKGROUP_NAME" \
  --configuration '{
    "EngineVersion": {
      "SelectedEngineVersion": "Apache Spark version 3.5"
    },
    "ExecutionRole": "EXECUTION_ROLE",
    "EngineConfiguration": {
      "Classifications": [
        {
          "Name": "spark-defaults",
          "Properties": {
            "spark.dynamicAllocation.minExecutors": "1",
            "spark.dynamicAllocation.initialExecutors": "2",
            "spark.dynamicAllocation.maxExecutors": "10",
            "spark.dynamicAllocation.executorIdleTimeout": "300"
          }
        }
      ]
    }
  }'
```

To modify defaults Spark properties from the AWS CLI for a workgroup, use the `engine-configuration` configuration when updating a Workgroup. The changes apply to new interactive sessions going forward.

```
aws athena update-work-group \
  --region "REGION" \
  --work-group "WORKGROUP_NAME" \
  --configuration-updates '{
    "EngineVersion": {
      "SelectedEngineVersion": "Apache Spark version 3.5"
    },
    "ExecutionRole": "EXECUTION_ROLE",
    "EngineConfiguration": {
      "Classifications": [
        {
          "Name": "spark-defaults",
          "Properties": {
            "spark.dynamicAllocation.minExecutors": "1",
            "spark.dynamicAllocation.initialExecutors": "2",
            "spark.dynamicAllocation.maxExecutors": "12",
            "spark.dynamicAllocation.executorIdleTimeout": "300"
          }
        }
      ]
    }
  }'
```
