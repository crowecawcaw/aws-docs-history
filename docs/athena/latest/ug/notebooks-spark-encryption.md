# Enable Apache Spark encryption

You can enable Apache Spark encryption on Athena. Doing so encrypts data in transit
between Spark nodes and also encrypts data at rest stored locally by Spark. To enhance
security for this data, Athena uses the following encryption configuration:

```
spark.io.encryption.keySizeBits="256"
spark.io.encryption.keygen.algorithm="HmacSHA384"
```

To enable Spark encryption, you can use the Athena console, the AWS CLI, or the Athena
API.

###### To create a new notebook that has Spark encryption enabled

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. If the console navigation pane is not visible, choose the expansion menu
   on the left.
3. Do one of the following:
   - In **Notebook explorer**, choose **Create
     notebook**.
   - In **Notebook editor**, choose **Create
     notebook**, or choose the plus icon
     (**+**) to add a notebook.

4. For **Notebook name**, enter a name for the
   notebook.
5. Expand the **Spark properties** option.
6. Select **Turn on Spark encryption**.
7. Choose **Create**.
   The notebook session that you create is encrypted. Use the new notebook as you
   normally would. When you later launch new sessions that use the notebook, the new
   sessions will also be encrypted.

You can also use the Athena console to enable Spark encryption for an existing
notebook.

###### To enable encryption for an existing notebook

1. [Open a new session](notebooks-spark-managing.md#opening-a-previously-created-notebook "notebooks-spark-managing.md#opening-a-previously-created-notebook") for a previously
   created notebook.
2. In the notebook editor, from the **Session** menu on the
   upper right, choose **Edit session**.
3. In the **Edit session details** dialog box, expand
   **Spark properties**.
4. Select **Turn on Spark encryption**.
5. Choose **Save**.
   The console launches a new session that has encryption enabled. Later sessions
   that you create for this notebook will also have encryption enabled.

You can use the AWS CLI to enable encryption when you launch a session by specifying
the appropriate Spark properties.

###### To use the AWS CLI to enable Spark encryption

1. Use a command like the following to create an engine configuration JSON
   object that specifies Spark encryption properties.

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

2. In the AWS CLI, use the `athena start-session` command and pass
   in the JSON object that you created to the
   `--engine-configuration` argument, as in the following
   example:

```
aws athena start-session \
   --region "`region`" \
   --work-group "`your-work-group`" \
   --engine-configuration "$ENGINE_CONFIGURATION_JSON"
```

To enable Spark encryption with the Athena API, use the [StartSession](../APIReference/API_StartSession.md "../APIReference/API_StartSession.md")
action and its [EngineConfiguration](../APIReference/API_EngineConfiguration.md "../APIReference/API_EngineConfiguration.md")
`SparkProperties` parameter to specify the encryption configuration in
your `StartSession` request.
