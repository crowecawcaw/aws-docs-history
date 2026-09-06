

# Connect to Athena Spark sessions using an interface VPC endpoint
<a name="athena-spark-vpc-endpoint"></a>

For workgroups using [Apache Spark version 3.5](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-release-versions.html#notebooks-spark-release-versions-spark-35), you can connect directly to Athena Spark sessions using an interface VPC endpoint (AWS PrivateLink) in your Virtual Private Cloud (VPC) instead of connecting over the internet. When you use an interface VPC endpoint, communication between your VPC and Athena Spark session endpoints is conducted entirely within the AWS network.

Each VPC endpoint is represented by one or more Elastic Network Interfaces (ENIs) with private IP addresses in your VPC subnets. The ENIs in your VPC don't need public IP addresses to communicate with Athena Spark session endpoints.

To use Athena Spark session endpoints through your VPC, you must connect from an instance that is inside the VPC or connect your private network to your VPC using (Site-to-Site VPN) or AWS Direct Connect.

## Supported endpoints
<a name="athena-spark-vpc-endpoint-supported"></a>

The following Athena Spark session endpoints support private access via AWS PrivateLink:



| Endpoint | Description | Service name | 
| --- | --- | --- | 
| Spark Connect | gRPC endpoint for remote Spark workload execution | com.amazonaws.{{region}}.athena.sessions | 
| Live UI | Browser-based real-time Spark task monitoring | com.amazonaws.{{region}}.athena.dashboard | 
| Persistent UI | Spark History Server for completed sessions | com.amazonaws.{{region}}.athena.persistent-dashboard | 

## Considerations
<a name="athena-spark-vpc-endpoint-considerations"></a>
+ To ensure that session endpoint URLs are only accessible from within your VPC, you must call `GetSessionEndpoint` (Spark Connect) or `GetResourceDashboard` (Live UI and Persistent UI) through the Athena API VPC endpoint. Athena embeds the originating VPC in the access token and enforces that the endpoint is accessed from the same VPC.
+ A session endpoint URL generated from within a VPC can be accessed from that same VPC or from the public internet, but not from a different VPC. This supports common workflows where a token is generated programmatically from within a VPC and the resulting dashboard URL is opened in a local browser.
+ A session endpoint URL generated from the public internet is not accessible from within a VPC.
+ VPC endpoint policies are not supported on Athena Spark Connect, Live UI, or Persistent UI endpoints.
+ VPC endpoint policies are supported on Athena API endpoints. To control which IAM principals can invoke Athena API endpoints, apply a VPC endpoint policy to your Athena API VPC endpoint (`com.amazonaws.{{region}}.athena`).

## Create a VPC endpoint for Athena Spark session endpoints
<a name="athena-spark-vpc-endpoint-create"></a>

You can create an interface VPC endpoint using the AWS Management Console or the AWS CLI.

To create an endpoint using the AWS CLI:

```
aws ec2 create-vpc-endpoint \
  --vpc-id <your-vpc-id> \
  --service-name com.amazonaws.<region>.athena.sessions \
  --vpc-endpoint-type Interface \
  --subnet-ids <subnet-id> \
  --security-group-ids <security-group-id> \
  --private-dns-enabled
```

After you create the endpoint and enable private DNS, the Spark Connect session URL resolves automatically to your VPC endpoint — no changes are needed in your SparkConnect client configuration. For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink documentation*.

## Create a VPC endpoint policy for Athena Spark session endpoints
<a name="athena-spark-vpc-endpoint-policy"></a>

VPC endpoint policies are not supported on Athena Spark Connect, Live UI, or Persistent UI endpoints.

To control access, attach a VPC endpoint policy to your Athena API endpoint (`com.amazonaws.{{region}}.athena`). Because session endpoint URLs are bound to the VPC from which they were generated, controlling who can call `GetSessionEndpoint` or `GetResourceDashboard` through the API endpoint effectively controls access to the corresponding session endpoints.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html).

The following example allows only a specific IAM role to generate session endpoint URLs:

```
{
  "Statement": [
    {
      "Action": [
        "athena:GetSessionEndpoint",
        "athena:GetResourceDashboard"
      ],
      "Effect": "Allow",
      "Resource": "*",
      "Principal": {
        "AWS": "arn:aws:iam::<account-id>:role/<role-name>"
      }
    }
  ]
}
```