

# Run interactive sessions with Amazon EMR on EKS through Spark Connect
<a name="emr-eks-spark-connect"></a>

With Amazon EMR on EKS release `emr-7.14.0` and later (or `emr-spark-8.1.0` and later), you can connect to a managed Spark Connect endpoint from self-managed PySpark clients such as VS Code, PyCharm, and Jupyter notebooks. Spark Connect uses a client-server architecture that decouples your application code from the Spark driver process. You develop and debug PySpark code in your local IDE while Spark operations run on your EKS cluster through Amazon EMR on EKS. Spark Connect offers the following benefits:
+ Connect to Amazon EMR on EKS from any PySpark client, including VS Code, PyCharm, and Jupyter notebooks
+ Set breakpoints and step through PySpark code in your IDE while DataFrames run on production-scale data remotely
+ Run on your own EKS cluster with full control over compute, networking, and security configuration

A Spark Connect endpoint is a managed endpoint on your virtual cluster that hosts a Spark Connect server. When you create a Spark Connect endpoint, Amazon EMR on EKS provisions a Spark driver with a gRPC server on your EKS cluster. Your local PySpark client sends DataFrame and SQL operations to the driver through the gRPC endpoint. To interact with the endpoint, you obtain session credentials using the `GetManagedEndpointSessionCredentials` API. Each endpoint supports multiple concurrent sessions.

## Prerequisites
<a name="emr-eks-spark-connect-prerequisites"></a>

Before you create a Spark Connect endpoint, make sure you have the following.

The following requirements are specific to Spark Connect endpoints:
+ An EKS cluster with at least one *private subnet*. To route gRPC traffic to the endpoint, Spark Connect provisions an internal Network Load Balancer (NLB), which requires a private subnet in your VPC. The NLB is internal and isn't exposed to the public internet.
+ The AWS Load Balancer Controller installed on your EKS cluster, so that Amazon EMR on EKS can provision the internal NLB. For instructions, see [Installing the AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html).

You also need the following standard Amazon EMR on EKS resources. If you already run jobs on Amazon EMR on EKS, you likely have these in place:
+ An IAM job execution role with permissions to access your data sources, such as Amazon S3 buckets and the Data Catalog. For instructions, see [Creating a job execution role](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/creating-job-execution-role.html).
+ If your EKS cluster uses Cluster Access Management, the required access entries for Amazon EMR on EKS. For instructions, see [Setting up cluster access for Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-cluster-access.html).

## Required permissions
<a name="emr-eks-spark-connect-permissions"></a>

Add the following permissions to your IAM role to create and interact with a Spark Connect endpoint:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EMRContainersEndpointAccess",
            "Effect": "Allow",
            "Action": [
                "emr-containers:CreateManagedEndpoint",
                "emr-containers:DescribeManagedEndpoint",
                "emr-containers:DeleteManagedEndpoint",
                "emr-containers:ListManagedEndpoints",
                "emr-containers:GetManagedEndpointSessionCredentials"
            ],
            "Resource": [
                "arn:aws:emr-containers:{{region}}:{{account-id}}:/virtualclusters/{{virtual-cluster-id}}",
                "arn:aws:emr-containers:{{region}}:{{account-id}}:/virtualclusters/{{virtual-cluster-id}}/endpoints/*"
            ]
        },
        {
            "Sid": "PassRoleToEMRContainers",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/{{ExecutionRole}}",
            "Condition": {
                "StringLike": {
                    "iam:PassedToService": "emr-containers.amazonaws.com"
                }
            }
        }
    ]
}
```

## Create a security configuration
<a name="emr-eks-spark-connect-security-config"></a>

Spark Connect endpoints require a security configuration associated with your virtual cluster. The security configuration defines the authentication and authorization settings for the endpoint, and specifies the system namespace where Spark Connect infrastructure runs.

**Note**  
Each security configuration has a one-to-one relationship with a virtual cluster. You cannot reuse the same security configuration across multiple virtual clusters.

Create a security configuration with a system namespace:

```
aws emr-containers create-security-configuration \
  --name "{{security-config-name}}" \
  --security-configuration '{
    "authenticationConfiguration": {
      "identityCenterConfiguration": {
        "enableIdentityCenter": false
      }
    }
  }' \
  --container-provider '{
    "type": "EKS",
    "id": "{{eks-cluster-name}}",
    "info": {
      "eksInfo": {
        "namespace": "{{system-namespace}}"
      }
    }
  }'
```

The `namespace` in the security configuration is the *system namespace* where Spark Connect infrastructure components run. This is separate from the user namespace specified when creating the virtual cluster.

## Create a virtual cluster with Spark Connect enabled
<a name="emr-eks-spark-connect-create-vc"></a>

Create a virtual cluster associated with the security configuration. You must set `sessionEnabled` to `true` and provide the `securityConfigurationId` from the previous step.

```
aws emr-containers create-virtual-cluster \
  --name "{{virtual-cluster-name}}" \
  --container-provider '{
    "type": "EKS",
    "id": "{{eks-cluster-name}}",
    "info": {
      "eksInfo": {
        "namespace": "{{user-namespace}}"
      }
    }
  }' \
  --security-configuration-id {{SECURITY_CONFIGURATION_ID}} \
  --session-enabled true
```

**Important**  
`--security-configuration-id` — Associates this virtual cluster with the security configuration created in the previous step. This is required for Spark Connect endpoints.  
`--session-enabled` — Enables Spark Connect endpoint support on the virtual cluster. Without this flag, you cannot create Spark Connect endpoints on this virtual cluster.

## Create a Spark Connect endpoint
<a name="emr-eks-spark-connect-create"></a>

After creating a security configuration, create a Spark Connect managed endpoint on your virtual cluster.

**Note**  
The first Spark Connect endpoint on an EKS cluster takes longer to become `ACTIVE` than subsequent ones. For the first endpoint on the EKS cluster, Amazon EMR on EKS provisions the shared networking components used for connectivity — an internal Network Load Balancer (NLB) and a VPC interface endpoint (AWS PrivateLink) — which can take several minutes. These components are created only once per EKS cluster and are reused by all later endpoints on that cluster, so subsequent endpoints start up faster.

```
aws emr-containers create-managed-endpoint \
  --virtual-cluster-id {{VIRTUAL_CLUSTER_ID}} \
  --name "spark-connect-endpoint" \
  --type "SPARK_CONNECT" \
  --release-label "emr-7.14.0-latest" \
  --execution-role-arn "arn:aws:iam::{{account-id}}:role/{{ExecutionRole}}" \
  --security-configuration-id {{SECURITY_CONFIGURATION_ID}} \
  --session-idle-timeout-in-minutes 60
```

The following example includes Spark configuration overrides with dynamic allocation and a monitoring configuration to export Spark logs to Amazon S3:

```
aws emr-containers create-managed-endpoint \
  --virtual-cluster-id {{VIRTUAL_CLUSTER_ID}} \
  --name "spark-connect-endpoint" \
  --type "SPARK_CONNECT" \
  --release-label "emr-7.14.0-latest" \
  --execution-role-arn "arn:aws:iam::{{account-id}}:role/{{ExecutionRole}}" \
  --security-configuration-id {{SECURITY_CONFIGURATION_ID}} \
  --session-idle-timeout-in-minutes 60 \
  --configuration-overrides '{
    "applicationConfiguration": [
      {
        "classification": "spark-defaults",
        "properties": {
          "spark.driver.memory": "4g",
          "spark.executor.memory": "4g",
          "spark.executor.cores": "2",
          "spark.executor.instances": "3",
          "spark.dynamicAllocation.enabled": "true",
          "spark.dynamicAllocation.minExecutors": "3",
          "spark.dynamicAllocation.maxExecutors": "5"
        }
      }
    ],
    "monitoringConfiguration": {
      "s3MonitoringConfiguration": {
        "logUri": "s3://{{your-bucket}}/spark-connect-logs/"
      },
      "persistentAppUI": "ENABLED"
    }
  }'
```

Monitor the endpoint status:

```
aws emr-containers describe-managed-endpoint \
  --virtual-cluster-id {{VIRTUAL_CLUSTER_ID}} \
  --id {{ENDPOINT_ID}}
```

Wait until the endpoint state is `ACTIVE` before connecting.

## Connect to a Spark Connect endpoint
<a name="emr-eks-spark-connect-connect"></a>

After the endpoint is active, obtain session credentials and connect from a PySpark client.

**To connect to a Spark Connect endpoint**

1. Get the auth proxy URL from the endpoint description:

   ```
   aws emr-containers describe-managed-endpoint \
     --virtual-cluster-id {{VIRTUAL_CLUSTER_ID}} \
     --id {{ENDPOINT_ID}}
   ```

   The response includes the `authProxyUrl` field when the endpoint is `ACTIVE`.

1. Get a session token for the endpoint:

   ```
   aws emr-containers get-managed-endpoint-session-credentials \
     --virtual-cluster-id {{VIRTUAL_CLUSTER_ID}} \
     --endpoint-identifier {{ENDPOINT_ID}} \
     --execution-role-arn "arn:aws:iam::{{account-id}}:role/{{ExecutionRole}}" \
     --credential-type "TOKEN"
   ```

   The response includes a session token:

   ```
   {
       "id": "{{SESSION_ID}}",
       "credentials": {
           "token": "{{SESSION_TOKEN}}"
       },
       "endpointCredentials": {
           "token": "{{ENDPOINT_CREDENTIALS_TOKEN}}"
       },
       "expiresAt": "{{EXPIRY_TIME}}"
   }
   ```

   Use the `credentials.token` value as the `x-aws-proxy-auth` parameter when connecting to the auth proxy URL.

1. Install the PySpark client matching the Spark version on your endpoint (Spark 3.5.8 for `emr-7.14.0`, Spark 4.0.2 for `emr-spark-8.1.0`):

   ```
   # For emr-7.14.0
   pip install pyspark[connect]==3.5.8
   
   # For emr-spark-8.1.0
   pip install pyspark[connect]==4.0.2
   
   pip install boto3
   ```

1. Connect from PySpark using the auth proxy URL and session token:

   ```
   from pyspark.sql import SparkSession
   
   # Use the authProxyUrl from DescribeManagedEndpoint
   # and the credentials.token from GetManagedEndpointSessionCredentials
   connect_url = f"{auth_proxy_url}/;use_ssl=true;x-aws-proxy-auth={token}"
   
   spark = SparkSession.builder.remote(connect_url).getOrCreate()
   print(f"Connected. Spark version: {spark.version}")
   
   # Run queries
   spark.sql("SELECT 1+1 AS result").show()
   
   # When finished, disconnect the client
   spark.stop()
   ```

The following Python script obtains the auth proxy URL and session token, then connects to the Spark Connect endpoint:

```
import boto3
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

REGION = '{{REGION}}'
VIRTUAL_CLUSTER_ID = '{{VIRTUAL_CLUSTER_ID}}'
ENDPOINT_ID = '{{ENDPOINT_ID}}'
EXECUTION_ROLE = 'arn:aws:iam::{{account-id}}:role/{{ExecutionRole}}'

client = boto3.client('emr-containers', region_name=REGION)

# Get the auth proxy URL from DescribeManagedEndpoint
endpoint_response = client.describe_managed_endpoint(
    virtualClusterId=VIRTUAL_CLUSTER_ID,
    id=ENDPOINT_ID
)
auth_proxy_url = endpoint_response['endpoint']['authProxyUrl']

# Get session token
creds_response = client.get_managed_endpoint_session_credentials(
    virtualClusterId=VIRTUAL_CLUSTER_ID,
    endpointIdentifier=ENDPOINT_ID,
    executionRoleArn=EXECUTION_ROLE,
    credentialType='TOKEN'
)
token = creds_response['credentials']['token']

# Connect via Spark Connect using auth proxy URL and credentials token
connect_url = f"{auth_proxy_url}/;use_ssl=true;x-aws-proxy-auth={token}"
spark = SparkSession.builder.remote(connect_url).getOrCreate()
print(f"Connected. Spark version: {spark.version}")

# Run DataFrame operations
df = spark.range(100).withColumn("squared", col("id") * col("id"))
df.show(10)
print(f"Count: {df.count()}")

spark.stop()
```

## Considerations and limitations
<a name="emr-eks-spark-connect-considerations"></a>

Consider the following when running interactive workloads through Spark Connect on Amazon EMR on EKS.
+ Spark Connect is supported with Amazon EMR on EKS release `emr-7.14.0` and later, or `emr-spark-8.1.0` and later.
+ Spark Connect supports DataFrame and SQL APIs in PySpark. Spark Connect doesn't support RDD-based APIs.
+ Session tokens are time-limited. When a token expires, gRPC calls fail with an authentication error. Call `GetManagedEndpointSessionCredentials` to obtain a new token and create a new `SparkSession` with the updated token.
+ Each security configuration has a one-to-one relationship with a virtual cluster. You cannot share a security configuration across multiple virtual clusters.
+ You must delete all endpoints using a security configuration before you can delete the security configuration.
+ The PySpark version installed locally must match the Apache Spark version on your endpoint (Spark 3.5.8 for `emr-7.14.0`, Spark 4.0.2 for `emr-spark-8.1.0`). A version mismatch causes connection errors or unexpected behavior.
+ The Spark Connect endpoint type is `SPARK_CONNECT`. This is different from Livy interactive endpoints (type `JUPYTER_ENTERPRISE_GATEWAY`).
+ The `sessionIdleTimeoutInMinutes` parameter controls how long an idle session persists before automatic termination. Default is 60 minutes.
+ Spark Connect endpoints don't support Trusted Identity Propagation.
+ Spark Connect endpoints don't support Lake Formation fine-grained access control (FGAC) yet. To enforce access control, use the IAM execution role associated with the endpoint.
+ Spark Connect endpoints use a Network Load Balancer (NLB) to route gRPC traffic. The NLB is created when the first Spark Connect endpoint is created and is only deleted when the last session-enabled virtual cluster is deleted. You are responsible for NLB costs while it exists, in addition to EKS compute resources consumed by the Spark driver and executors during your session.
+ Python UDFs (`@udf`, `spark.udf.register`) require the local Python minor version to match the remote worker version, or they fail with `PYTHON_VERSION_MISMATCH`. Built-in SQL functions and DataFrame operations do not require a Python version match.