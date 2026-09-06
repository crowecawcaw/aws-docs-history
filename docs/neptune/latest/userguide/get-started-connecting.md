

# Connecting to an Amazon Neptune cluster
<a name="get-started-connecting"></a>

After creating a Neptune cluster, you must set up network access so that your applications can reach the cluster endpoint. The following sections describe the network connectivity options. For more information about querying your data after you connect, see [Accessing graph data](get-started-access-graph.md).

## Network connectivity options
<a name="get-started-connect-ways"></a>

An Amazon Neptune DB cluster can *only* be created in an Amazon Virtual Private Cloud (Amazon VPC). Its endpoints are accessible only within that VPC unless you enable and set up [Neptune public endpoints](neptune-public-endpoints.md) for the DB cluster.

You can set up network access to your Neptune DB cluster in its VPC in several ways:
+ [Connecting from an Amazon EC2 instance in the same VPC](get-started-connect-ec2-same-vpc.md)
+ [Connecting from an Amazon EC2 instance in another VPC](get-started-connect-ec2-other-vpc.md)
+ [Connecting from a private network](get-started-connect-private-net.md)
+ [Connecting from a public endpoint](neptune-public-endpoints.md)

## Verify your connection
<a name="get-started-verify-connection"></a>

After you set up network access, you can verify that your connection works by calling the instance status endpoint. A successful response confirms that your client can reach the Neptune cluster.

------
#### [ AWS CLI ]

Run the following command:

```
aws neptunedata get-engine-status \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --region {{us-east-1}}
```

For more information, see [get-engine-status](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-engine-status.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=10, retries={'total_max_attempts': 1})
)

response = client.get_engine_status()

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/status \
  --region {{us-east-1}} \
  --service neptune-db
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

For more information about using **awscurl** with IAM authentication, see [Using `awscurl` with temporary credentials to securely connect to a DB cluster with IAM authentication enabled](iam-auth-connect-command-line.md#iam-auth-connect-awscurl).

------
#### [ curl ]

Run the following command:

```
curl -G https://{{your-neptune-endpoint}}:{{port}}/status
```

**Note**  
This command works only when IAM authentication is not enabled on your cluster. If IAM authentication is enabled, use **awscurl** or the AWS CLI instead.

------

A healthy cluster returns a JSON response that includes `"status": "healthy"`. For example:

```
{
    "status": "healthy",
    "startTime": "Thu Aug 24 21:07:13 UTC 2023",
    "dbEngineVersion": "{{1.3.1.0.R1}}",
    "role": "writer",
    "dfeQueryEngine": "viaQueryHint",
    "gremlin": { "version": "tinkerpop-{{3.7.2}}" },
    "sparql": { "version": "sparql-1.1" },
    "opencypher": { "version": "Neptune-9.0.20190305-1.0" },
    "labMode": { ... },
    "features": { ... },
    "settings": { ... }
}
```

If you cannot reach the endpoint, verify that your network configuration allows traffic on port 8182 (or your configured port) and that your security group rules permit inbound connections from your client. For more information, see [Securing access to Neptune](get-started-security.md). For help setting up the AWS CLI, SDKs, or `curl`, see [Using command-line tools](get-started-cli-tools.md).