#

Accessing Neptune Analytics graph from Neptune Analytics interface endpoints

You can use the AWS CLI or AWS SDKs to access Neptune Analytics graph API operations through Neptune Analytics interface endpoints.

## AWS CLI examples

To access Neptune Analytics API operations through Neptune Analytics interface endpoints in AWS CLI
commands, use the `--region` parameter.

**Example: Create a VPC endpoint**

```
aws ec2 create-vpc-endpoint \
--region us-east-1 \
--service-name neptune-graph-service-name (for control APIs)/ neptune-graph-data-service-name (for data APIs) \
--vpc-id client-vpc-id \
--subnet-ids client-subnet-id \
--vpc-endpoint-type Interface \
--security-group-ids client-sg-id
```

**Example: Modify a VPC endpoint**

Neptune Analytics VPC endpoint service uses private hosted zone to route requests to your Neptune Analytics graph. Ensure that
you have enabled private dns on your VPC interface endpoint.

```
aws ec2 modify-vpc-endpoint \
--region us-east-1 \
--vpc-endpoint-id client-vpc-endpoint-id \
--private-dns-enabled
```

###### Note

Ensure that the private dns is always enabled on your VPC interface endpoint otherwise you might
see errors in routing requests to your Neptune Analytics graph.

**Example: List graphs using the region parameter**

```
aws neptune-graph list-graphs --region us-east-1
```

**Example: Execute a query using the region parameter**

```
aws neptune-graph execute-query \
--graph-identifier g-0123456789 \
--region us-east-1 \
--query-string "MATCH (n) RETURN n LIMIT 1" \
--language open_cypher \
out.txt
```

## AWS SDK examples

To access Neptune Analytics API operations through Neptune Analytics interface endpoints when using the AWS SDKs, update your
SDKs to the latest version. Then, configure your clients to use the AWS region for accessing a
Neptune Analytics API operation through Neptune Analytics interface endpoints.

**SDK for Python (Boto3)**

In this example, you will use an endpoint URL to access a Neptune Analytics graph.

```
neptune_graph_client = session.client(
service_name='neptune-graph',
region_name='us-east-1'
)
```

**SDK for Java 2.x**

In this example, you will use an endpoint URL to access a Neptune Analytics graph.

```
//client build with endpoint config
final NeptuneGraphClient NeptuneGraphClient.builder()
        .region(software.amazon.awssdk.regions.Region.US_EAST_1)
        .credentialsProvider(credentialsProvider)
        .build();
```
