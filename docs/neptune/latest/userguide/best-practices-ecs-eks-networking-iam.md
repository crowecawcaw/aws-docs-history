

# Configure networking, security groups, and IAM authentication
<a name="best-practices-ecs-eks-networking-iam"></a>

Containerized deployments on Amazon ECS or Amazon EKS require correct network configuration and IAM credential management to connect to Neptune.

**Security groups checklist**
+ The Neptune cluster security group must allow inbound TCP on port 8182 (or the custom port configured for your Neptune cluster) from the Amazon EKS node or pod CIDR range.
+ If you use the Amazon VPC CNI plugin with custom networking, verify that the pod subnet has a route to the Neptune subnet.
+ Neptune must be in the same Amazon VPC as your Amazon ECS or Amazon EKS cluster, or connected through Amazon VPC peering or Transit Gateway.

**Verify connectivity from inside the container**

Before debugging application-level issues, confirm the network path by running one of the following commands from inside the container:

------
#### [ AWS CLI ]

```
aws neptunedata get-engine-status \
  --endpoint-url https://{{your-neptune-endpoint}}:8182
```

For more information, see [get-engine-status](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-engine-status.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    region_name='{{us-east-1}}',
    endpoint_url='https://{{your-neptune-endpoint}}:8182',
    config=Config(read_timeout=10)
)

response = client.get_engine_status()
print(response['status'])
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:8182/status \
  --region {{us-east-1}} \
  --service neptune-db
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -k https://{{your-neptune-endpoint}}:8182/status
```

**Note**  
The `-k` flag skips certificate verification. Use this only for connectivity testing, not in production code.

------

A successful response confirms that security groups, routing, and DNS resolution are all working. A timeout indicates a network-level issue.

**IAM credential refresh**

If you use [IAM authentication](iam-auth.md) with Neptune, your pods must refresh credentials before they expire. We recommend [Amazon EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) for new deployments. IAM Roles for Service Accounts (IRSA) is also supported and widely used.

With either approach, retrieve credentials *inside* the authentication generator function, not once at startup. IRSA and Pod Identity tokens expire after 1 hour. If you cache credentials at initialization, requests will fail with `AccessDeniedException: security token expired` after the token expires.
+ For gremlin-go: call `cfg.Credentials.Retrieve(ctx)` inside the `gen` function passed to `NewDynamicAuth`.
+ For Java: use `NeptuneGremlinClient` with a `HandshakeInterceptor` that refreshes SigV4 signing on each new connection.

**Cross-account access**

Neptune doesn't support direct cross-account IAM authentication. If your Amazon EKS cluster is in a different AWS account than your Neptune cluster, the pod must first assume a role in the Neptune account before authenticating.

**Ingress configuration for Graph Explorer**

If you run [Graph Explorer](https://github.com/aws/graph-explorer) in a containerized environment, ensure that all paths are accessible to the proxy—not only `/explorer`. On Amazon EKS, configure your ingress controller rules to allow all paths. On Amazon ECS, configure your Application Load Balancer target group and listener rules to forward all paths to the Graph Explorer container. Graph Explorer's proxy makes calls to `/summary`, `/gremlin`, `/openCypher`, and `/sparql`. Path-restricted routing rules break the proxy silently.