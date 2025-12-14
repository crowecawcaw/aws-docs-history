# Managing and connecting to Amazon Aurora DSQL

clusters using AWS PrivateLink

With AWS PrivateLink for Amazon Aurora DSQL, you can provision interface Amazon VPC endpoints (interface endpoints) in your Amazon Virtual Private Cloud. These endpoints are directly accessible from applications that are on premises over Amazon VPC and Direct Connect, or in a different AWS Region over Amazon VPC peering. Using AWS PrivateLink and interface endpoints, you can simplify private network connectivity from your applications to Aurora DSQL.

Applications within your Amazon VPC can access Aurora DSQL using Amazon VPC interface endpoints without
requiring public IP addresses.

Interface endpoints are represented by one or more elastic network interfaces (ENIs) that are assigned private IP addresses from subnets in your Amazon VPC. Requests to Aurora DSQL over interface endpoints stay on the AWS network. For more information about how to connect your Amazon VPC with your on-premises network, see the [Direct Connect User Guide](../../../directconnect/latest/UserGuide.md "../../../directconnect/latest/UserGuide.md") and the [AWS Site-to-Site VPN VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") User Guide.

For general information about interface endpoints, see [Access an AWS service using an interface Amazon VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") User Guide.

## Types of Amazon VPC endpoints for Aurora DSQL

Aurora DSQL requires two different types of AWS PrivateLink endpoints.

1. _Management endpoint_— This endpoint is used for
   administrative operations, such as `get`, `create`,
   `update`, `delete`, and `list` on Aurora DSQL
   clusters. See [Managing Aurora DSQL clusters using AWS PrivateLink](#managing-dsql-clusters-using-privatelink "#managing-dsql-clusters-using-privatelink").
2. _Connection endpoint_— This endpoint is used for
   connecting to Aurora DSQL clusters through PostgreSQL clients. See [Connecting to Aurora DSQL clusters using
   AWS PrivateLink](#privatelink-connecting-clusters "#privatelink-connecting-clusters").

## Considerations when using AWS PrivateLink for Aurora DSQL

Amazon VPC considerations apply to AWS PrivateLink for Aurora DSQL. For more information, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#vpce-interface-limitations "../../../vpc/latest/privatelink/create-interface-endpoint.md#vpce-interface-limitations") and [AWS PrivateLink quotas](../../../vpc/latest/privatelink/vpc-limits-endpoints.md "../../../vpc/latest/privatelink/vpc-limits-endpoints.md") in the AWS PrivateLink Guide.

## Managing Aurora DSQL clusters using AWS PrivateLink

You can use the AWS Command Line Interface or AWS Software Development Kits (SDKs) to manage Aurora DSQL clusters through Aurora DSQL interface endpoints.

### Creating an Amazon VPC endpoint

To create an Amazon VPC interface endpoint, see [Create an Amazon VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the AWS PrivateLink Guide.

```
aws ec2 create-vpc-endpoint \
--region `region` \
--service-name com.amazonaws.`region`.dsql \
--vpc-id `your-vpc-id` \
--subnet-ids `your-subnet-id` \
--vpc-endpoint-type Interface \
--security-group-ids `client-sg-id` \
```

To use the default Regional DNS name for Aurora DSQL API requests, do not disable private DNS when you create the Aurora DSQL interface
endpoint. When private DNS is enabled, requests to the Aurora DSQL service made from
within your Amazon VPC will automatically resolve to the private IP address of the Amazon VPC
endpoint, rather than the public DNS name. When private DNS is enabled, Aurora DSQL
requests made within your Amazon VPC will automatically resolve to your Amazon VPC
endpoint.

If private DNS is not enabled, use the `--region` and
`--endpoint-url` parameters with AWS CLI commands to manage Aurora DSQL
clusters through Aurora DSQL interface endpoints.

### Listing clusters using an endpoint

URL

In the following example, replace the AWS Region `us-east-1` and
the DNS name of the Amazon VPC endpoint ID
`vpce-1a2b3c4d-5e6f.dsql.us-east-1.vpce.amazonaws.com` with your own
information.

```
aws dsql --region `us-east-1` --endpoint-url https://`vpce-1a2b3c4d-5e6f.dsql.us-east-1.vpce.amazonaws.com` list-clusters
```

### API Operations

Refer to the [Aurora DSQL API reference](CHAP_api_reference.md "CHAP_api_reference.md") for documentation on managing resources in Aurora DSQL.

### Managing endpoint policies

By thoroughly testing and configuring the Amazon VPC endpoint policies, you can help
ensure that your Aurora DSQL cluster is secure, compliant, and aligned with your
organization's specific access control and governance requirements.

**Example: Full Aurora DSQL access policy**

The following policy grants full access to all Aurora DSQL actions and resources
through the specified Amazon VPC endpoint.

```
aws ec2 modify-vpc-endpoint \
    --vpc-endpoint-id vpce-xxxxxxxxxxxxxxxxx \
    --region region \
    --policy-document '{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": "*",
          "Action": "dsql:*",
          "Resource": "*"
        }
      ]
    }'
```

**Example: Restricted Aurora DSQL Access Policy**

The following policy only permits these Aurora DSQL actions.

- `CreateCluster`
- `GetCluster`
- `ListClusters`

All other Aurora DSQL actions are denied.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": "*",
 "Action": [
 "dsql:CreateCluster",
 "dsql:GetCluster",
 "dsql:ListClusters"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Connecting to Aurora DSQL clusters using

AWS PrivateLink

Once your AWS PrivateLink endpoint is set up and active, you can connect to your Aurora DSQL cluster using a PostgreSQL client. The connection instructions below outline the steps to construct the proper hostname for connecting through the AWS PrivateLink endpoint.

### Setting up an AWS PrivateLink

connection endpoint

**Step 1: Get the service name for
your cluster**

When creating an AWS PrivateLink endpoint for connecting to your cluster, you
first need to fetch the cluster-specific service name.

AWS CLI

```
aws dsql get-vpc-endpoint-service-name \
--region us-east-1 \
--identifier `your-cluster-id`
```

Example response

```
{
    "serviceName": "com.amazonaws.us-east-1.dsql-fnh4"
}
```

The service name includes an identifier, such as
`dsql-fnh4` in the example. This identifier is also
needed when constructing the hostname for connecting to your
cluster.

AWS SDK for Python (Boto3)

```
import boto3

dsql_client = boto3.client('dsql', region_name='us-east-1')
response = dsql_client.get_vpc_endpoint_service_name(
    identifier='your-cluster-id'
)
service_name = response['serviceName']
print(f"Service Name: {service_name}")
```

AWS SDK for Java 2.x

```
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dsql.DsqlClient;
import software.amazon.awssdk.services.dsql.model.GetVpcEndpointServiceNameRequest;
import software.amazon.awssdk.services.dsql.model.GetVpcEndpointServiceNameResponse;

String region = "us-east-1";
String clusterId = "your-cluster-id";

DsqlClient dsqlClient = DsqlClient.builder()
    .region(Region.of(region))
    .credentialsProvider(DefaultCredentialsProvider.create())
    .build();

GetVpcEndpointServiceNameResponse response = dsqlClient.getVpcEndpointServiceName(
    GetVpcEndpointServiceNameRequest.builder()
        .identifier(clusterId)
        .build()
);
String serviceName = response.serviceName();
System.out.println("Service Name: " + serviceName);
```

**Step 2: Create the Amazon VPC endpoint**

Using the service name obtained in the previous step, create an Amazon VPC
endpoint.

###### Important

The connection instructions below only work for connecting to clusters
when private is DNS enabled. Do not use the
`--no-private-dns-enabled` flag when creating the endpoint,
as this will prevent the connection instructions below from working
properly. If you disable private DNS, you will need to create your own
wildcard private DNS record that points to the created endpoint.

AWS CLI

```
aws ec2 create-vpc-endpoint \
    --region us-east-1 \
    --service-name `service-name-for-your-cluster` \
    --vpc-id `your-vpc-id` \
    --subnet-ids `subnet-id-1 subnet-id-2`  \
    --vpc-endpoint-type Interface \
    --security-group-ids `security-group-id`
```

**Example response**

```
{
    "VpcEndpoint": {
        "VpcEndpointId": "vpce-0123456789abcdef0",
        "VpcEndpointType": "Interface",
        "VpcId": "vpc-0123456789abcdef0",
        "ServiceName": "com.amazonaws.us-east-1.dsql-fnh4",
        "State": "pending",
        "RouteTableIds": [],
        "SubnetIds": [
            "subnet-0123456789abcdef0",
            "subnet-0123456789abcdef1"
        ],
        "Groups": [
            {
                "GroupId": "sg-0123456789abcdef0",
                "GroupName": "default"
            }
        ],
        "PrivateDnsEnabled": true,
        "RequesterManaged": false,
        "NetworkInterfaceIds": [
            "eni-0123456789abcdef0",
            "eni-0123456789abcdef1"
        ],
        "DnsEntries": [
            {
                "DnsName": "*.dsql-fnh4.us-east-1.vpce.amazonaws.com",
                "HostedZoneId": "Z7HUB22UULQXV"
            }
        ],
        "CreationTimestamp": "2025-01-01T00:00:00.000Z"
    }
}
```

SDK for Python

```
import boto3

ec2_client = boto3.client('ec2', region_name='us-east-1')
response = ec2_client.create_vpc_endpoint(
    VpcEndpointType='Interface',
    VpcId='your-vpc-id',
    ServiceName='com.amazonaws.us-east-1.dsql-fnh4',  # Use the service name from previous step
    SubnetIds=[
        'subnet-id-1',
        'subnet-id-2'
    ],
    SecurityGroupIds=[
        'security-group-id'
    ]
)

vpc_endpoint_id = response['VpcEndpoint']['VpcEndpointId']
print(f"VPC Endpoint created with ID: {vpc_endpoint_id}")
```

SDK for Java 2.x
Use an endpoint URL for Aurora DSQL APIs

```
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.CreateVpcEndpointRequest;
import software.amazon.awssdk.services.ec2.model.CreateVpcEndpointResponse;
import software.amazon.awssdk.services.ec2.model.VpcEndpointType;

String region = "us-east-1";
String serviceName = "com.amazonaws.us-east-1.dsql-fnh4";  // Use the service name from previous step
String vpcId = "your-vpc-id";

Ec2Client ec2Client = Ec2Client.builder()
    .region(Region.of(region))
    .credentialsProvider(DefaultCredentialsProvider.create())
    .build();

CreateVpcEndpointRequest request = CreateVpcEndpointRequest.builder()
    .vpcId(vpcId)
    .serviceName(serviceName)
    .vpcEndpointType(VpcEndpointType.INTERFACE)
    .subnetIds("subnet-id-1", "subnet-id-2")
    .securityGroupIds("security-group-id")
    .build();

CreateVpcEndpointResponse response = ec2Client.createVpcEndpoint(request);
String vpcEndpointId = response.vpcEndpoint().vpcEndpointId();
System.out.println("VPC Endpoint created with ID: " + vpcEndpointId);
```

**Additional setup when connecting
via Direct Connect or Amazon VPC peering**

Some additional setup may be needed to connect to Aurora DSQL
clusters using an AWS PrivateLink connection endpoint from
on-premise devices via Amazon VPC peering or Direct Connect. This setup
is not required if your application is running in the same
Amazon VPC as your AWS PrivateLink endpoint. The private DNS
entries created above will not resolve correctly outside the
endpoint's Amazon VPC, but you can create your own private DNS
records which resolve to your AWS PrivateLink connection endpoint.

Create a private CNAME DNS record which points to the
AWS PrivateLink endpoint's fully-qualified domain name. The
domain name of the created DNS record should be constructed
from the following components:

1. The service identifier from the service
   name. For example: `dsql-fnh4`
2. The AWS Region

Create the CNAME DNS record with a domain name in the
following format: `*.`service-identifier`.`region`.on.aws`

The format of the domain name is important for two
reasons:

1. The hostname used to connect to Aurora DSQL must
   match Aurora DSQL's server certificate when using the
   `verify-full` SSL mode. This ensures the
   highest level of connection security.
2. Aurora DSQL uses the cluster ID portion of the
   hostname used to connect to Aurora DSQL to identify the
   connecting cluster.

If creating private DNS records is not possible, you can
still connect to Aurora DSQL. See [Connecting to an
Aurora DSQL cluster using an AWS PrivateLink endpoint
without private DNS](#connecting-cluster-id-option "#connecting-cluster-id-option").

### Connecting to an Aurora DSQL cluster using an

AWS PrivateLink connection endpoint

Once your AWS PrivateLink endpoint is set up and active (check that the
`State` is `available`), you can connect to your
Aurora DSQL cluster using a PostgreSQL client. For instructions on using the AWS
SDKs, you can follow the guides in [Programming with
Aurora DSQL](programming-with.md "programming-with.md"). You must change the cluster endpoint to match the
hostname format.

#### Constructing the hostname

The hostname for connecting through AWS PrivateLink differs from the public
DNS hostname. You need to construct it using the following
components.

1. `Your-cluster-id`
2. The service identifier from the service name. For example:
   `dsql-fnh4`
3. The AWS Region. For example:
   `us-east-1`

Use the following format:
``cluster-id`.`service-identifier`.`region`.on.aws`

**Example: Connection Using
PostgreSQL**

```
# Set environment variables
export CLUSTERID=`your-cluster-id`
export REGION=us-east-1
export SERVICE_IDENTIFIER=dsql-fnh4  # This should match the identifier in your service name

# Construct the hostname
export HOSTNAME="$CLUSTERID.$SERVICE_IDENTIFIER.$REGION.on.aws"

# Generate authentication token
export PGPASSWORD=$(aws dsql --region $REGION generate-db-connect-admin-auth-token --hostname $HOSTNAME)

# Connect using psql
psql -d postgres -h $HOSTNAME -U admin
```

#### Connecting to an

Aurora DSQL cluster using an AWS PrivateLink endpoint
without private DNS

The connection instructions above rely on private DNS
records. If your application is running in the same
Amazon VPC as your AWS PrivateLink endpoint, the DNS records
are created for you. Alternatively, if you are
connecting from on-premise devices via Amazon VPC peering
or Direct Connect, then you can create your own private DNS
records. However, DNS record setup is not always
possible due to network restrictions imposed by your
security teams. If your application must connect using
Direct Connect or from a peered Amazon VPC, and DNS record setup
is not possible, you can still connect to Aurora DSQL.

Aurora DSQL uses the cluster ID portion of your hostname
to identify the connecting cluster, but if DNS record
setup is not possible, Aurora DSQL supports specifying the
target cluster using the `amzn-cluster-id`
connection option. With this option, it is possible to
use your AWS PrivateLink endpoint's fully-qualified
domain name as your hostname when connecting.

###### Important

When connecting with your AWS PrivateLink endpoint's
fully-qualified domain name or IP address, the
`verify-full` SSL mode is not supported.
For this reason, setting up private DNS is
preferred.

**Example: Specifying the cluster ID connection option using
PostgreSQL**

```
# Set environment variables
export CLUSTERID=`your-cluster-id`
export REGION=us-east-1
export HOSTNAME=vpce-04037adb76c111221-d849uc2p.dsql-fnh4.us-east-1.vpce.amazonaws.com # This should match your endpoint's fully-qualified domain name

# Construct the hostname used to generate the authentication token
export AUTH_HOSTNAME="$CLUSTERID.dsql.$REGION.on.aws"

# Generate authentication token
export PGPASSWORD=$(aws dsql --region $REGION generate-db-connect-admin-auth-token --hostname $AUTH_HOSTNAME)

# Specify the amzn-cluster-id connection option
export PGOPTIONS="-c amzn-cluster-id=$CLUSTERID"

# Connect using psql
psql -d postgres -h $HOSTNAME -U admin
```

### Troubleshooting issues with

AWS PrivateLink

#### Common Issues and Solutions

The following table lists common issues and solutions relating to
AWS PrivateLink with Aurora DSQL.

| Issue                  | Possible Cause                         | Solution                                                                                             |
| ---------------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Connection timeout     | Security group not properly configured | Use Amazon VPC Reachability Analyzer to ensure your networking<br>setup allows traffic on port 5432. |
| DNS resolution failure | Private DNS not enabled                | Verify that the Amazon VPC endpoint was created with private<br>DNS enabled.                         |
| Authentication failure | Incorrect credentials or expired token | Generate a new authentication token and verify the user<br>name.                                     |
| Service name not found | Incorrect cluster ID                   | Double-check your cluster ID and AWS Region when<br>fetching the service name.                       |

### Related Resources

For more information, see the following resources:

- [Amazon
  Aurora DSQL User Guide](../../../AmazonRDS/latest/AuroraUserGuide/aurora-dsql.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-dsql.md")
- [AWS PrivateLink
  Documentation](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md")
- [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md")
