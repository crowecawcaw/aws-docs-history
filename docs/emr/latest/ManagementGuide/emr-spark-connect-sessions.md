

# Interactive sessions
<a name="emr-spark-connect-sessions"></a>

With Amazon EMR release `emr-spark-8.0.0` and later, you can connect to an Amazon EMR cluster from self-managed PySpark clients such as VS Code, PyCharm, and Jupyter notebooks using the Amazon EMR session APIs with Apache Spark Connect. Spark Connect uses a client-server architecture that decouples your application code from the Spark driver process. You develop and debug PySpark code in your local IDE while Spark operations run on your Amazon EMR cluster. Spark Connect offers the following benefits:
+ Connect to Amazon EMR clusters from any PySpark client, including VS Code, PyCharm, and Jupyter notebooks.
+ Set breakpoints and step through PySpark code in your IDE while DataFrames run on production-scale data on your cluster.
+ Run multiple interactive queries without restarting Spark. Sessions persist until you terminate them or they reach the idle timeout.

A Spark Connect session is a managed connection between your local PySpark client and a Spark Connect Server running on your Amazon EMR cluster. When you start a session, Amazon EMR launches a Spark Connect Server as a YARN application on your cluster. Your local client sends DataFrame and SQL operations to the server through a managed authentication proxy, and the server runs them on the cluster. Each session has its own endpoint URL and authentication token that you use to connect.

## Prerequisites
<a name="emr-spark-connect-prereqs"></a>
+ An Amazon EMR cluster running release `emr-spark-8.0.0` or later with `SessionEnabled` set to `true`.
+ The Spark application installed on the cluster.
+ Python 3.9 or later with `pyspark[connect]` installed locally. The PySpark version must match the Spark version on your cluster.
+ For clusters in private subnets, the Amazon EMR service role must include the `AmazonEMRServicePolicyForSessions` managed policy, which grants permissions to create Network Load Balancers and VPC endpoint services in your account.

## Required permissions
<a name="emr-spark-connect-permissions"></a>

To use Spark Connect sessions, you need two sets of permissions:

### User permissions
<a name="emr-spark-connect-user-permissions"></a>

Add the following permissions to your IAM user or role to manage Spark Connect sessions:

`elasticmapreduce:StartSession`  
Grants permission to create a Spark Connect session on the cluster that you specify.

`elasticmapreduce:GetSession`  
Grants permission to get the status of a session.

`elasticmapreduce:GetSessionEndpoint`  
Grants permission to retrieve the Spark Connect endpoint URL and authentication token for a session.

`elasticmapreduce:ListSessions`  
Grants permission to list sessions on a cluster.

`elasticmapreduce:TerminateSession`  
Grants permission to terminate a session.

`iam:PassRole`  
(Required only for runtime role sessions) Grants permission to pass an execution role to the session.

The following is an example IAM policy for managing sessions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EMRSessionClusterAccess",
            "Effect": "Allow",
            "Action": [
                "elasticmapreduce:StartSession",
                "elasticmapreduce:ListSessions"
            ],
            "Resource": "arn:aws:elasticmapreduce:{{region}}:{{account-id}}:cluster/*"
        },
        {
            "Sid": "EMRSessionAccess",
            "Effect": "Allow",
            "Action": [
                "elasticmapreduce:GetSession",
                "elasticmapreduce:GetSessionEndpoint",
                "elasticmapreduce:TerminateSession"
            ],
            "Resource": "arn:aws:elasticmapreduce:{{region}}:{{account-id}}:cluster/*/session/*"
        },
        {
            "Sid": "PassExecutionRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/{{execution-role-name}}",
            "Condition": {
                "StringLike": {
                    "iam:PassedToService": "elasticmapreduce.amazonaws.com"
                }
            }
        }
    ]
}
```

### Service role permissions for private subnet clusters
<a name="emr-spark-connect-service-role"></a>

For clusters launched in private subnets, Amazon EMR creates a Network Load Balancer (NLB) and VPC endpoint service in your account to enable connectivity between the managed authentication proxy and your cluster. Attach the `AmazonEMRServicePolicyForSessions` managed policy to your Amazon EMR service role to grant these permissions.

Public subnet clusters do not require this policy because connectivity is established directly through the cluster's public IP address.

**Note**  
For the `AmazonEMRServicePolicyForSessions` policy to function correctly, your VPC and subnet must be tagged with `for-use-with-amazon-emr-managed-policies=true`.

## Working with interactive sessions
<a name="emr-spark-connect-working"></a>

To create a session-enabled cluster and connect to it, follow these steps.

**To start a Spark Connect session**

1. Create a cluster with Spark Connect sessions enabled:

   ```
   aws emr create-cluster \
     --name "spark-connect-cluster" \
     --release-label emr-spark-8.0.0 \
     --applications Name=Spark \
     --service-role arn:aws:iam::{{account-id}}:role/EMR_DefaultRole \
     --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,SubnetId={{subnet-id}} \
     --instance-groups '[
       {"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"m5.xlarge"},
       {"InstanceCount":2,"InstanceGroupType":"CORE","InstanceType":"m5.xlarge"}
     ]' \
     --session-enabled \
     --tags Key=for-use-with-amazon-emr-managed-policies,Value=true
   ```

1. After the cluster reaches the `WAITING` state, start a session. The `--name` parameter is required and must be a non-empty value.

   ```
   aws emr start-session \
     --cluster-id {{j-XXXXXXXXXXXXX}} \
     --name "my-session"
   ```

   For runtime role sessions, add the `--execution-role-arn` parameter:

   ```
   aws emr start-session \
     --cluster-id {{j-XXXXXXXXXXXXX}} \
     --name "my-session" \
     --execution-role-arn arn:aws:iam::{{account-id}}:role/{{execution-role}}
   ```

1. Monitor the session state. Wait for the session to reach `IDLE` state:

   ```
   aws emr get-session \
     --cluster-id {{j-XXXXXXXXXXXXX}} \
     --session-id {{is-XXXXXXXXXXXXX}}
   ```

1. Retrieve the Spark Connect endpoint and authentication token:

   ```
   aws emr get-session-endpoint \
     --cluster-id {{j-XXXXXXXXXXXXX}} \
     --session-id {{is-XXXXXXXXXXXXX}}
   ```

   The response includes the endpoint URL and an authentication token:

   ```
   {
       "Endpoint": "https://{{session-id}}.emr-spark-connect.{{region}}.amazonaws.com",
       "AuthToken": "{{v2.local.xxx...}}",
       "AuthTokenExpirationTime": "2026-01-01T01:00:00Z"
   }
   ```

1. Install the PySpark client that matches the Spark version on your cluster:

   ```
   pip install 'pyspark[connect]==4.0.1' boto3
   ```

1. Connect from your PySpark client using the endpoint and token:

   ```
   from pyspark.sql import SparkSession
   
   session_id = "{{is-XXXXXXXXXXXXX}}"
   auth_token = "{{token from get-session-endpoint}}"
   endpoint_url = "{{Endpoint from get-session-endpoint}}"
   
   # Build the sc:// URL from the returned Endpoint value rather than hardcoding the host.
   # GetSessionEndpoint returns an https:// URL with no port; convert it to sc:// and
   # append :443 (without the port, the PySpark client defaults to 15002, which is not reachable).
   host = endpoint_url.replace("https://", "")
   url = f"sc://{host}:443/;use_ssl=true;x-aws-proxy-auth={auth_token};authorization={session_id}"
   
   spark = SparkSession.builder.remote(url).getOrCreate()
   spark.sql("SELECT 1 + 1 AS result").show()
   spark.stop()
   ```

1. When you are done, terminate the session to release resources:

   ```
   aws emr terminate-session \
     --cluster-id {{j-XXXXXXXXXXXXX}} \
     --session-id {{is-XXXXXXXXXXXXX}}
   ```
**Important**  
`spark.stop()` only closes the local client connection. The remote session continues running and consuming cluster resources until you explicitly terminate it or it reaches the idle timeout.

## Complete Python example
<a name="emr-spark-connect-example"></a>

The following script demonstrates the full lifecycle: create a session, connect, run queries, and clean up.

```
import boto3
import time
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

REGION = "{{us-east-1}}"
CLUSTER_ID = "{{j-XXXXXXXXXXXXX}}"

client = boto3.client("emr", region_name=REGION)

# Start a session
response = client.start_session(ClusterId=CLUSTER_ID, Name="demo-session")
session_id = response["Id"]
print(f"Session {session_id} starting...")

# Wait for IDLE state
while True:
    response = client.get_session(ClusterId=CLUSTER_ID, SessionId=session_id)
    state = response["Session"]["State"]
    print(f"  State: {state}")
    if state == "IDLE":
        break
    if state in ("FAILED", "TERMINATED"):
        raise Exception(f"Session failed: {state}")
    time.sleep(5)

# Get endpoint and token
response = client.get_session_endpoint(ClusterId=CLUSTER_ID, SessionId=session_id)
auth_token = response["AuthToken"]
host = response["Endpoint"].replace("https://", "")

# Connect via Spark Connect
url = f"sc://{host}:443/;use_ssl=true;x-aws-proxy-auth={auth_token};authorization={session_id}"
spark = SparkSession.builder.remote(url).getOrCreate()
print(f"Connected. Spark version: {spark.version}")

# Run queries
spark.sql("SELECT 'Hello from EMR!' AS message").show()
df = spark.range(100).withColumn("squared", F.col("id") * F.col("id"))
df.show(5)

# Disconnect client
spark.stop()

# Terminate session
client.terminate_session(ClusterId=CLUSTER_ID, SessionId=session_id)
print(f"Session {session_id} terminated.")
```

## Session engine configuration
<a name="emr-spark-connect-engine-config"></a>

You can pass Spark configuration overrides when starting a session. These configurations are applied to the Spark Connect Server for that session only, without affecting other sessions or the cluster defaults.

```
aws emr start-session \
  --cluster-id {{j-XXXXXXXXXXXXX}} \
  --name "configured-session" \
  --engine-configuration '{
    "Classification": "spark-defaults",
    "Properties": {
      "spark.executor.memory": "4g",
      "spark.executor.cores": "2",
      "spark.dynamicAllocation.enabled": "true"
    }
  }'
```

## Considerations and limitations
<a name="emr-spark-connect-considerations"></a>

Consider the following when using Spark Connect sessions on Amazon EMR:
+ Spark Connect is supported with Amazon EMR release `emr-spark-8.0.0` and later.
+ Spark Connect supports DataFrame and SQL APIs in PySpark. RDD-based APIs are not supported.
+ The PySpark version installed locally must match the Apache Spark version on your Amazon EMR cluster. A version mismatch causes connection errors or unexpected behavior. Python UDFs (`@udf`, `spark.udf.register`) additionally require the local Python minor version to match the Python version on the cluster workers, or they fail with `PYTHON_VERSION_MISMATCH`. Built-in SQL functions and DataFrame operations do not require a Python version match.
+ Authentication tokens expire after 1 hour. When a token expires, gRPC calls fail with an authentication error. Call `GetSessionEndpoint` to obtain a new token and create a new `SparkSession` with the updated URL.
+ Sessions end after a configurable idle timeout. The default timeout is 60 minutes, with a maximum of 24 hours.
+ Amazon EMR enforces a limit of 1000 concurrent active sessions per cluster. If a cluster reaches this limit, Amazon EMR rejects new session requests until existing sessions end. The practical maximum can be lower. It depends on your cluster's instance types and the resources each session consumes.
+ For clusters in private subnets, Amazon EMR creates a Network Load Balancer (NLB) in your account. Ensure your account has sufficient Elastic Load Balancing quota. Each NLB supports up to 50 clusters.
+ For private subnet clusters, the VPC and subnet must be tagged with `for-use-with-amazon-emr-managed-policies=true`.
+ The authentication proxy enforces a rate limit of 5,000 requests per 5-minute window per source IP address. High-throughput workloads from a single client may reach this limit. Internal Spark Connect protocol messages (such as `ReleaseExecute`) count toward this limit.
+ There is no additional charge for using Spark Connect. You pay only for the Amazon EC2 instances in your Amazon EMR cluster.
+ `spark.stop()` only closes the local client connection. The session continues running on the cluster until you call `TerminateSession` or the idle timeout expires.
+ High Availability (HA) clusters with multiple primary nodes are not supported for Spark Connect sessions.
+ Python UDFs may fail with a `No module named 'pyspark'` error because the Python worker process spawned by the executor JVM starts without `pyspark` on its `PYTHONPATH`. To work around this, set the executor `PYTHONPATH` to include `pyspark` when you start the session, for example by passing `spark.executorEnv.PYTHONPATH` in the session engine configuration.
+ Trusted Identity Propagation (TIP) is not supported for Spark Connect sessions.
+ Fine-grained access control (FGAC) through Lake Formation is not supported for Spark Connect sessions in this release.