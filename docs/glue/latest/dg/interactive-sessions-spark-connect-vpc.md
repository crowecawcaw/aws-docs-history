

# Connecting to Spark Connect within a VPC
<a name="interactive-sessions-spark-connect-vpc"></a>

You can use AWS PrivateLink to connect to a Spark Connect session from within your VPC. When you use an interface VPC endpoint, communication between your VPC and the AWS Glue Spark Connect endpoint stays entirely within the AWS network.

## Prerequisites
<a name="spark-connect-vpc-prerequisites"></a>
+ A VPC with at least one subnet
+ A security group that allows inbound HTTPS (port 443) from your VPC CIDR
+ IAM permissions for `ec2:CreateVpcEndpoint` and `glue:*`

## Step 1: Create VPC endpoints
<a name="spark-connect-vpc-create-endpoints"></a>

You need two VPC endpoints:
+ **Spark Connect sessions** (`com.amazonaws.{{region}}.glue.sessions`) – For the gRPC data path.
+ **AWS Glue API** (`com.amazonaws.{{region}}.glue`) – For calling `CreateSession`, `GetSessionEndpoint`, and other control plane APIs.

The following AWS Cloud Development Kit (AWS CDK) (AWS CDK) example creates both VPC endpoints with a security group that allows HTTPS from within the VPC:

```
import { Stack, StackProps, Aws } from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import { Construct } from 'constructs';

export interface SparkConnectVpcStackProps extends StackProps {
  /** Existing VPC ID to use. If not provided, creates a new VPC. */
  readonly vpcId?: string;
}

export class SparkConnectVpcStack extends Stack {
  readonly vpc: ec2.IVpc;

  constructor(scope: Construct, id: string, props?: SparkConnectVpcStackProps) {
    super(scope, id, props);

    // Use existing VPC or create a new one
    if (props?.vpcId) {
      this.vpc = ec2.Vpc.fromLookup(this, 'Vpc', { vpcId: props.vpcId });
    } else {
      this.vpc = new ec2.Vpc(this, 'SparkConnectVpc', {
        maxAzs: 2,
        natGateways: 0,
        subnetConfiguration: [
          {
            name: 'Private',
            subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
          },
        ],
      });
    }

    // Security group allowing HTTPS from within the VPC
    const endpointSg = new ec2.SecurityGroup(this, 'EndpointSg', {
      vpc: this.vpc,
      description: 'Allow HTTPS for Glue Spark Connect VPC endpoints',
      allowAllOutbound: false,
    });
    endpointSg.addIngressRule(
      ec2.Peer.ipv4(this.vpc.vpcCidrBlock),
      ec2.Port.tcp(443),
      'HTTPS from VPC'
    );

    // 1. Spark Connect sessions endpoint
    this.vpc.addInterfaceEndpoint('GlueSessionsEndpoint', {
      service: new ec2.InterfaceVpcEndpointService(
        `com.amazonaws.${Aws.REGION}.glue.sessions`
      ),
      securityGroups: [endpointSg],
      privateDnsEnabled: true,
    });

    // 2. Glue API endpoint (for CreateSession, GetSessionEndpoint, etc.)
    this.vpc.addInterfaceEndpoint('GlueApiEndpoint', {
      service: ec2.InterfaceVpcEndpointAwsService.GLUE,
      securityGroups: [endpointSg],
      privateDnsEnabled: true,
    });
  }
}
```

## Step 2: Connect from inside the VPC
<a name="spark-connect-vpc-connect"></a>

After creating the endpoints with private DNS enabled, the `sc://` session URL resolves to your VPC endpoint automatically. Use the standard Spark Connect flow from any resource in the VPC (Amazon EC2, Lambda, Amazon ECS, and others) with no code changes:

```
import boto3
from urllib.parse import quote
from pyspark.sql import SparkSession

glue = boto3.client("glue", region_name="{{us-east-1}}")

# Create a Spark Connect session
glue.create_session(
    Id="{{my-session}}",
    Role="arn:aws:iam::{{123456789012}}:role/{{GlueRole}}",
    Command={"Name": "glueetl"},
    GlueVersion="5.1",
    SessionType="SPARK_CONNECT",
)

# Wait for READY state, then get endpoint
resp = glue.get_session_endpoint(SessionId="{{my-session}}")
endpoint = resp["SparkConnect"]
token = quote(endpoint["AuthToken"], safe="")
url = f"{endpoint['Url']}:443/;use_ssl=true;x-aws-proxy-auth={token}"

# Connect — resolves via PrivateLink automatically
spark = SparkSession.builder.remote(url).getOrCreate()

spark.version
```

## Connecting within a VPC using Spark utilities
<a name="spark-connect-vpc-spark-utils"></a>

If you use the `sagemaker-studio` library, the Spark utilities module works within a VPC with no additional configuration. After creating the VPC endpoints, initialize the session as usual:

```
from sagemaker_studio import sparkutils

spark = sparkutils.init(connection_name="{{my-glue-spark-connection}}")

df = spark.read.table("{{my_database}}.{{my_table}}")
df.show()
```

The Spark utilities module resolves the endpoint through PrivateLink automatically when the VPC endpoints are configured with private DNS enabled.

## Considerations
<a name="spark-connect-vpc-notes"></a>
+ **Private DNS** – When enabled, the `sc://s-{{id}}.sessions.glue.{{region}}.amazonaws.com` hostname resolves to the VPC endpoint's private IP. No URL changes are needed.
+ **Token encoding** – The auth token must be URL-encoded (`urllib.parse.quote(token, safe="")`) because it contains special characters.