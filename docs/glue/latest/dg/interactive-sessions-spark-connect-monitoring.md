

# Monitoring Spark Connect sessions
<a name="interactive-sessions-spark-connect-monitoring"></a>

 Apache Spark provides a suite of web user interfaces (UIs) that you can use to monitor your Spark cluster. The Spark Live UI is supported for Spark Connect sessions in AWS Glue, providing real-time visibility into job execution, stages, and performance metrics. The Spark UI is available while the session is in `READY` state. 

## Monitoring in Notebooks in SageMaker Unified Studio
<a name="spark-connect-sagemaker-notebooks"></a>

 In Notebooks in SageMaker Unified Studio, Spark UI links are available in the kernel footer at the bottom of the notebook. 
+ Choose the **Spark UI** link to open the dashboard in a separate tab.
+ Choose **Spark Driver Logs** to view driver logs directly from the kernel footer.

## Enabling the Spark Live UI using API
<a name="spark-connect-enable-live-ui"></a>

 To enable the Spark Live UI, add the `--enable-spark-live-ui` parameter when you create the session. 

 The following example creates a Spark Connect session with the Spark Live UI enabled: 

```
import boto3

glue = boto3.client("glue", region_name="{{us-east-1}}")

glue.create_session(
    Id="{{my-session}}",
    Role="arn:aws:iam::{{123456789012}}:role/{{GlueRole}}",
    Command={"Name": "glueetl"},
    GlueVersion="5.1",
    SessionType="SPARK_CONNECT",
    IdleTimeout=60,
    Timeout=60,
    DefaultArguments={
        "--language": "python",
        "--enable-spark-live-ui": "true",
    },
)
```

## Accessing the Spark UI dashboard
<a name="spark-connect-access-dashboard"></a>

 You can access the Spark UI dashboard by using the `GetDashboardUrl` API or from the AWS Glue console. The dashboard opens in a new browser tab. Authentication is handled automatically through the dashboard URL token. 

```
response = glue.get_dashboard_url(
    ResourceId="{{my-session}}",
    ResourceType="SESSION",
)
dashboard_url = response["Url"]
print(dashboard_url)
```

**Note**  
The dashboard URL token is single-use. It is exchanged for a session cookie on the first request. Open it once in a browser to access the Spark UI.

## Spark UI tabs for Spark Connect sessions
<a name="spark-connect-ui-tabs"></a>

 The Spark UI provides the following tabs for monitoring your Spark Connect session. For more information about the Spark UI, see [Web UI](https://spark.apache.org/docs/latest/web-ui.html) in the Apache Spark documentation. 

## Enabling executor logs
<a name="spark-connect-executor-logs"></a>

 To enable executor logs for your Spark Connect session, specify the S3 paths for Spark event logs and Spark logs in the `DefaultArguments` parameter when you create the session. 

```
glue.create_session(
    Id="{{my-session}}",
    Role="arn:aws:iam::{{123456789012}}:role/{{GlueRole}}",
    Command={"Name": "glueetl"},
    GlueVersion="5.1",
    SessionType="SPARK_CONNECT",
    DefaultArguments={
        "--language": "python",
        "--enable-auto-scaling": "true",
        "--enable-spark-live-ui": "true",
        "--spark-event-logs-path": "s3://{{my-bucket}}/events/",
        "--spark-logs-s3-uri": "s3://{{my-bucket}}/logs/",
        "--enable-spark-ui": "true"
    },
)
```

 After the session runs, executor logs are available at the S3 paths you specified. You can also access them from the **Executors** tab in the Spark UI. 