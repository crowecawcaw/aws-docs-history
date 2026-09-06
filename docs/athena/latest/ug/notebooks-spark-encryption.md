

# Enable Apache Spark encryption
<a name="notebooks-spark-encryption"></a>

You can enable Apache Spark encryption on Athena. Doing so encrypts data in transit between Spark nodes and also encrypts data at rest stored locally by Spark. To enhance security for this data, Athena uses the following encryption configuration:

```
spark.io.encryption.keySizeBits="256" 
spark.io.encryption.keygen.algorithm="HmacSHA384"
```

To enable Spark encryption, you can use the Athena console, the AWS CLI, or the Athena API.

## Use the Athena console to enable Spark encryption in a new notebook
<a name="notebooks-spark-encryption-athena-console-new-notebook"></a>

**To create a new notebook that has Spark encryption enabled**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. If the console navigation pane is not visible, choose the expansion menu on the left.

1. Do one of the following:
   + In **Notebook explorer**, choose **Create notebook**.
   + In **Notebook editor**, choose **Create notebook**, or choose the plus icon (**\+**) to add a notebook.

1. For **Notebook name**, enter a name for the notebook.

1. Expand the **Spark properties** option.

1. Select **Turn on Spark encryption**.

1. Choose **Create**.

The notebook session that you create is encrypted. Use the new notebook as you normally would. When you later launch new sessions that use the notebook, the new sessions will also be encrypted.

## Use the Athena console to enable Spark encryption for an existing notebook
<a name="notebooks-spark-encryption-athena-console-existing-notebook"></a>

You can also use the Athena console to enable Spark encryption for an existing notebook.

**To enable encryption for an existing notebook**

1. [Open a new session](notebooks-spark-managing.md#opening-a-previously-created-notebook) for a previously created notebook.

1. In the notebook editor, from the **Session** menu on the upper right, choose **Edit session**.

1. In the **Edit session details** dialog box, expand **Spark properties**.

1. Select **Turn on Spark encryption**.

1. Choose **Save**.

The console launches a new session that has encryption enabled. Later sessions that you create for this notebook will also have encryption enabled.

## Use the AWS CLI to enable Spark encryption
<a name="notebooks-spark-encryption-cli"></a>

You can use the AWS CLI to enable encryption when you launch a session by specifying the appropriate Spark properties.

**To use the AWS CLI to enable Spark encryption**

1. Use a command like the following to create an engine configuration JSON object that specifies Spark encryption properties.

   ```
   ENGINE_CONFIGURATION_JSON=$( 
     cat <<EOF 
   { 
       "CoordinatorDpuSize": 1, 
       "MaxConcurrentDpus": 20, 
       "DefaultExecutorDpuSize": 1, 
       "SparkProperties": { 
         "spark.authenticate": "true", 
         "spark.io.encryption.enabled": "true", 
         "spark.network.crypto.enabled": "true" 
       } 
   } 
   EOF 
   )
   ```

1. In the AWS CLI, use the `athena start-session` command and pass in the JSON object that you created to the `--engine-configuration` argument, as in the following example:

   ```
   aws athena start-session \ 
      --region "{{region}}" \ 
      --work-group "{{your-work-group}}" \ 
      --engine-configuration "$ENGINE_CONFIGURATION_JSON"
   ```

For Apache Spark version 3.5 sessions, you enable encryption by specifying the same encryption properties in the `Classifications` element of the engine configuration instead of in the `SparkProperties` element. The encryption behavior is identical to earlier versions: Athena encrypts data in transit between Spark nodes and data at rest stored locally by Spark, using AES 256-bit encryption with the `HmacSHA384` algorithm. Use a command like the following, in which the classification `Name` must be `spark-defaults`.

```
aws athena start-session \ 
   --region "{{region}}" \ 
   --work-group "{{your-work-group}}" \ 
   --engine-configuration '{ 
       "Classifications": [{ 
           "Name": "spark-defaults", 
           "Properties": { 
               "spark.authenticate": "true", 
               "spark.io.encryption.enabled": "true", 
               "spark.network.crypto.enabled": "true" 
           } 
       }] 
   }'
```

You can also enable Spark encryption when you create a work group. Specify the same encryption properties in the `Classifications` element of the `EngineConfiguration` in the work group configuration, as in the following example. Sessions that you later start in this work group inherit the encryption configuration.

```
aws athena create-work-group \ 
   --region "{{region}}" \ 
   --name "{{your-work-group}}" \ 
   --configuration '{ 
       "EngineVersion": { 
           "SelectedEngineVersion": "Apache Spark version 3.5" 
       }, 
       "ExecutionRole": "{{execution-role}}", 
       "EngineConfiguration": { 
           "Classifications": [{ 
               "Name": "spark-defaults", 
               "Properties": { 
                   "spark.authenticate": "true", 
                   "spark.io.encryption.enabled": "true", 
                   "spark.network.crypto.enabled": "true" 
               } 
           }] 
       } 
   }'
```

## Use the Athena API to enable Spark encryption
<a name="notebooks-spark-encryption-api"></a>

To enable Spark encryption with the Athena API, use the [StartSession](https://docs.aws.amazon.com/athena/latest/APIReference/API_StartSession.html) action and its [EngineConfiguration](https://docs.aws.amazon.com/athena/latest/APIReference/API_EngineConfiguration.html) `SparkProperties` parameter to specify the encryption configuration in your `StartSession` request.

For Apache Spark version 3.5 sessions, use the `StartSession` action with the `EngineConfiguration` `Classifications` parameter, instead of `SparkProperties`, to specify the encryption properties. The classification name must be `spark-defaults`.