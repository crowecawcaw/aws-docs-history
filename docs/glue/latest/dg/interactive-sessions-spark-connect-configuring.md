

# Configuring AWS Glue interactive sessions
<a name="interactive-sessions-spark-connect-configuring"></a>

Before you connect to a AWS Glue interactive session using Spark Connect, you must configure the session with the appropriate settings.

## Prerequisites
<a name="spark-connect-config-prerequisites"></a>
+ **AWS Glue version** – You must use AWS Glue 5.1 or later.
+ **IAM permissions** – Your IAM identity must have permissions for the following actions: `glue:CreateSession`, `glue:GetSession`, and `glue:GetSessionEndpoint`.
+ **IAM role** – You must have an IAM role that AWS Glue can assume to run the session. This role must have permissions to access the data sources that your session uses.

## Creating a Spark Connect session
<a name="spark-connect-config-create-session"></a>

To create a Spark Connect session, call the `CreateSession` API with the `SessionType` parameter set to `SPARK_CONNECT`.

```
import boto3

glue_client = boto3.client("glue")

response = glue_client.create_session(
    Id="{{my-spark-connect-session}}",
    Role="arn:aws:iam::{{123456789012}}:role/{{GlueRole}}",
    Command={"Name": "glueetl"},
    GlueVersion="5.1",
    SessionType="SPARK_CONNECT"
)
```

Wait for the session to reach the `READY` state:

```
response = glue_client.get_session(
    Id="{{my-spark-connect-session}}"
)
print(response["Session"]["Status"])
```

**Important**  
The session must be in a `READY` state before you can retrieve the endpoint and connect to it.

## Configuring workers
<a name="spark-connect-config-workers"></a>

You can configure the number and type of workers for your Spark Connect session using the same parameters as other AWS Glue interactive sessions:
+ `WorkerType` – The type of workers (for example, `G.1X`, `G.2X`).
+ `NumberOfWorkers` – The number of workers to allocate.

```
response = glue_client.create_session(
    Id="{{my-spark-connect-session}}",
    Role="arn:aws:iam::{{123456789012}}:role/{{GlueRole}}",
    Command={"Name": "glueetl"},
    GlueVersion="5.1",
    SessionType="SPARK_CONNECT",
    WorkerType="G.2X",
    NumberOfWorkers=5
)
```