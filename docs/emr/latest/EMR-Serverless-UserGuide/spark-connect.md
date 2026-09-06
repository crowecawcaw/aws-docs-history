

# Run interactive sessions with Amazon EMR Serverless through Spark Connect
<a name="spark-connect"></a>

With Amazon EMR release `emr-7.13.0` and later, you can connect to an Amazon EMR Serverless application from self-managed PySpark clients such as VS Code, PyCharm, and Jupyter notebooks using the EMR Serverless session APIs with Apache Spark Connect. Spark Connect uses a client-server architecture that decouples your application code from the Spark driver process. You develop and debug PySpark code in your local IDE while Spark operations run on EMR Serverless compute. Spark Connect offers the following benefits:
+ Connect to EMR Serverless from any PySpark client, including VS Code, PyCharm, and Jupyter notebooks.
+ Set breakpoints and step through PySpark code in your IDE while DataFrames run on production-scale data remotely.

A Spark Connect session is a managed connection between your local PySpark client and a Spark driver running on Amazon EMR Serverless. When you start a session, EMR Serverless provisions a Spark driver and executors on your behalf. Your local client sends DataFrame and SQL operations to the driver, and the driver runs them remotely. The session persists until you terminate it or it reaches the idle timeout, so you can run multiple queries interactively without restarting Spark. Each session has its own endpoint URL and authentication token that you use to connect.

## Required permissions
<a name="spark-connect-permissions"></a>

In addition to the required permissions to access Amazon EMR Serverless, also add the following permissions to your IAM role to access a Spark Connect endpoint and manage Spark Connect sessions:

`emr-serverless:StartSession`  
Grants permission to create a Spark Connect session on the application that you specify as `Resource`.

`emr-serverless:GetSessionEndpoint`  
Grants permission to retrieve the Spark Connect endpoint URL and authentication token for a session.

`emr-serverless:GetSession`  
Grants permission to get the status of a session.

`emr-serverless:ListSessions`  
Grants permission to list sessions on an application.

`emr-serverless:TerminateSession`  
Grants permission to terminate a session.

`iam:PassRole`  
Grants permission to access the IAM execution role when creating the Spark Connect session. Amazon EMR Serverless uses this role to run your workloads.

`emr-serverless:GetResourceDashboard`  
Grants permission to generate the Spark UI URL and provides access to the logs for the session.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EMRServerlessApplicationLevelAccess",
            "Effect": "Allow",
            "Action": [
                "emr-serverless:StartSession",
                "emr-serverless:ListSessions"
            ],
            "Resource": [
                "arn:aws:emr-serverless:{{region}}:{{account-id}}:/applications/{{application-id}}"
            ]
        },
        {
            "Sid": "EMRServerlessSessionLevelAccess",
            "Effect": "Allow",
            "Action": [
                "emr-serverless:GetSession",
                "emr-serverless:GetSessionEndpoint",
                "emr-serverless:TerminateSession",
                "emr-serverless:GetResourceDashboard"
            ],
            "Resource": [
                "arn:aws:emr-serverless:{{region}}:{{account-id}}:/applications/{{application-id}}/sessions/*"
            ]
        },
        {
            "Sid": "EMRServerlessRuntimeRoleAccess",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::{{account-id}}:role/{{EMRServerlessExecutionRole}}"
            ],
            "Condition": {
                "StringLike": {
                    "iam:PassedToService": "emr-serverless.amazonaws.com"
                }
            }
        }
    ]
}
```

## Working with interactive sessions
<a name="spark-connect-working"></a>

To create a Spark Connect-enabled application and connect to it, follow these steps.

**To start a Spark Connect session**

1. Create an application with Spark Connect sessions.

   ```
   aws emr-serverless create-application \
     --type "SPARK" \
     --name "spark-connect-app" \
     --release-label emr-7.13.0 \
     --interactive-configuration '{"sessionEnabled": true}'
   ```

1. After Amazon EMR Serverless creates your application, start the application if you have not enabled auto-start to accept Spark Connect sessions.

   ```
   aws emr-serverless start-application \
     --application-id {{APPLICATION_ID}}
   ```

1. Use the following command to check the status of your application. After the status becomes `STARTED`, start a session.

   ```
   aws emr-serverless get-application \
     --application-id {{APPLICATION_ID}}
   ```

1. Start a session with an IAM execution role that grants access to your data.

   ```
   aws emr-serverless start-session \
     --application-id {{APPLICATION_ID}} \
     --execution-role-arn arn:aws:iam::{{account-id}}:role/{{EMRServerlessExecutionRole}}
   ```

1. Monitor the session state using the `get-session` API and wait for the session to be in `STARTED` or `IDLE` state.

   ```
   aws emr-serverless get-session \
     --application-id {{APPLICATION_ID}} \
     --session-id {{SESSION_ID}}
   ```

1. Retrieve the Spark Connect endpoint and authentication token. The endpoint URL returned by `GetSessionEndpoint` does not include a port number. When constructing the `sc://` connection URL, you must append `:443` — for example, `sc://`{{hostname}}`:443/;use_ssl=true;x-aws-proxy-auth=`{{token}}. Without it, the PySpark client defaults to port 15002, which is not reachable on EMR Serverless.

   ```
   aws emr-serverless get-session-endpoint \
     --application-id {{APPLICATION_ID}} \
     --session-id {{SESSION_ID}}
   ```

   The response includes the endpoint URL and an authentication token:

   ```
   {
     "endpoint": "{{ENDPOINT_URL}}",
     "authToken": "{{AUTH_TOKEN}}",
     "authTokenExpiresAt": "{{AUTH_TOKEN_EXPIRY_TIME}}"
   }
   ```

1. After the endpoint is ready, connect from a PySpark client. Install the PySpark client that matches the Spark version on your EMR Serverless application, and the AWS SDK for Python.

   ```
   # Match the PySpark version to your EMR Serverless release version (3.5.6 for emr-7.13.0)
   pip install pyspark[connect]==3.5.6
   pip install boto3
   ```

The following is a sample Python script to start a session and send requests directly to the session endpoint:

```
import boto3
import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

client = boto3.client('emr-serverless', region_name='{{REGION}}')

APPLICATION_ID = '{{APPLICATION_ID}}'
EXECUTION_ROLE = 'arn:aws:iam::{{account-id}}:role/{{EMRServerlessExecutionRole}}'

# Start the session
response = client.start_session(
    applicationId=APPLICATION_ID,
    executionRoleArn=EXECUTION_ROLE
)
session_id = response['sessionId']
print(f"Session {session_id} starting...")

# Wait for the session to be ready
while True:
    response = client.get_session(
        applicationId=APPLICATION_ID,
        sessionId=session_id
    )
    state = response['session']['state']
    print(f"Session state: {state}")
    if state in ('STARTED', 'IDLE'):
        break
    if state in ('FAILED', 'TERMINATED'):
        raise Exception(f"Session failed: {response['session'].get('stateDetails', 'Unknown error')}")
    time.sleep(5)

# Retrieve the Spark Connect endpoint and authentication token
response = client.get_session_endpoint(
    applicationId=APPLICATION_ID,
    sessionId=session_id
)

# Construct the authenticated remote URL
auth_token = response['authToken']
endpoint_url = response['endpoint']
connect_url = endpoint_url.replace("https://", "sc://", 1) + ":443/;use_ssl=true;"
connect_url += f"x-aws-proxy-auth={auth_token}"

# Start the Spark session
spark = SparkSession.builder.remote(connect_url).getOrCreate()
print(f"Connected. Spark version: {spark.version}")

# Run SQL
spark.sql("SELECT 1+1 AS result").show()

# Run DataFrame operations
df = spark.range(100).withColumn("squared", col("id") * col("id"))
df.show(10)
print(f"Count: {df.count()}")

# Stop the Spark session (disconnects the client only)
spark.stop()

# Terminate the EMR Serverless session to stop billing.
# spark.stop() only closes the local client connection. The remote session
# continues running and incurring charges until you explicitly terminate it
# or it reaches the idle timeout.
client.terminate_session(
    applicationId=APPLICATION_ID,
    sessionId=session_id
)
print(f"Session {session_id} terminated.")
```

To access the live Spark UI or Spark History Server for a session, use the `GetResourceDashboard` API.

```
response = client.get_resource_dashboard(
    applicationId=APPLICATION_ID,
    resourceId=session_id,
    resourceType='SESSION'
)
response['url']
```

While a session is active, the URL opens the live Apache Spark UI for real-time monitoring of queries, stages, and executors. After a session ends, the Spark History Server remains available for post-session analysis through the Amazon EMR Serverless console.

## Considerations and limitations
<a name="spark-connect-considerations"></a>

Consider the following when running interactive workloads through Spark Connect.
+ Spark Connect is supported with Amazon EMR Serverless release `emr-7.13.0` and later.
+ Spark Connect is supported only for the Apache Spark engine.
+ Spark Connect supports DataFrame and SQL APIs in PySpark. RDD-based APIs are not supported.
+ Authentication tokens are time-limited to 1 hour. When a token expires, gRPC calls fail with an authentication error. Call `GetSessionEndpoint` to obtain a new token and create a new `SparkSession` with the updated token.
+ Sessions end after a configurable idle timeout. Default timeout is set to 1 hour.
+ Each session has a hard limit of 24 hours by default, after which it auto-terminates even if it is actively running a task.
+ Each EMR Serverless application supports up to 25 concurrent sessions by default. To request a limit increase, contact AWS Support.
+ By default, `autoStopConfig` is on for applications. The application stops automatically after 15 minutes with no active sessions or job runs. You can change this configuration as part of your `create-application` or `update-application` request.
+ For the best startup experience, configure pre-initialized capacity for drivers and executors.
+ You should enable AutoStart or manually start your application before starting an EMR Serverless session.
+ The PySpark version installed locally must match the Apache Spark version on your Amazon EMR Serverless application (3.5.6 for `emr-7.13.0`). A version mismatch causes `ImportError` or unexpected behavior.
+ Fine-grained access control through Lake Formation is not supported for Spark Connect sessions.
+ Trusted Identity Propagation is not supported for interactive sessions with Spark Connect.
+ Serverless storage on EMR Serverless is not supported for interactive sessions with Spark Connect.
+ There is no additional charge for using Spark Connect. You pay only for EMR Serverless compute resources (vCPU, memory, and storage) consumed during your session.
+ The Spark configuration `spark.connect.grpc.binding.address` is reserved by EMR Serverless and cannot be overridden by users.
+ The PySpark package you install locally must match the Spark version on your EMR Serverless application. A version mismatch causes connection errors. Python UDFs (`@udf`, `spark.udf.register`) also require the local Python minor version to match the worker, or they fail with `PYTHON_VERSION_MISMATCH`. Built-in SQL functions and DataFrame operations do not require a Python version match.
+ To pass Spark configurations with `start-session`, set them under `runtimeConfiguration` in the `--configuration-overrides` parameter. The `start-job-run` API uses `applicationConfiguration` instead.