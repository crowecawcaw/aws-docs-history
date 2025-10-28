# Managing access to the

OpenSearch UI from a VPC endpoint

You can create a private connection between your VPC and OpenSearch UI using
AWS PrivateLink. Using this connection, you can access OpenSearch UI applications as if
they were in the same VPC. This way, you don't need to configure an internet gateway,
NAT device, VPN connection, or AWS Direct Connect to establish the connection. Instances in
your VPC don't need public IP addresses to access OpenSearch UI.

To establish this private connection, you first create an interface endpoint powered
by AWS PrivateLink. An endpoint network interface is created automatically in each subnet
that you specify for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for OpenSearch UI
applications.

## Creating a private connection

between a VPC and OpenSearch UI

You can create a private connection for accessing OpenSearch UI from a VPC using
the AWS Management Console or AWS CLI.

### Creating a private

connection between a VPC and OpenSearch UI (console)

###### To create a private connection between a VPC and OpenSearch UI using

the console

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. In the left navigation, under **Serverless**, choose
   **VPC endpoints**.
3. Choose **Create VPC endpoint**.
4. For **Name**, enter a name for the endpoint.
5. For **VPC**, select the VPC that you'll access
   OpenSearch UI applications from.
6. For **Subnets**, select one subnet that you'll access
   OpenSearch UI applications from.

###### Note

An endpoint's IP address and DNS type are based on subnet
type:

    * Dual-stack: If all subnets have both IPv4 and IPv6 address
     ranges.
    * IPv6: If all subnets are IPv6 only subnets.
    * IPv4: If all subnets have IPv4 address ranges.

7. For **Security groups**, select one or more security
   group to associate with the endpoint network interfaces.

###### Note

In this step, you are limiting the ports, protocols, and sources
for inbound traffic that you’re authorizing into your endpoint.
Ensure that the security group rules allow the resources that will
use the VPC endpoint to communicate with OpenSearch UI
applications to also communicate with the endpoint network
interface. 8. 8. Choose **Create endpoint**.

### Creating a private

connection between a VPC and OpenSearch UI (AWS CLI)

###### To create a private connection between a VPC and OpenSearch UI using

the AWS CLI

Run the following command. Replace the `placeholder
 values` with your own information.

```
aws opensearchserverless create-vpc-endpoint \
    --region `region` \
    --endpoint `endpoint` \
    --name `vpc_endpoint_name` \
    --vpc-id `vpc_id` \
    --subnet-ids `subnet_ids`
```

## Updating the VPC endpoint policy

to allow access to the OpenSearch UI application

After you create the private connection, update the VPC endpoint policy to allow
access to the OpenSearch UI application in the VPC endpoint policy by specifying
the application ID.

For information about updating a VPC endpoint policy, see [Update a VPC endpoint policy](../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy "../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy") in the
_AWS PrivateLink Guide_.

Ensure that the VPC endpoint policy includes the following statement. Replace the
`placeholder value` with your own information.

```
{
    "Statement": [{
        "Action": ["opensearch:*"],
        "Effect": "Allow",
        "Principal": "*",
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "opensearch:ApplicationId": ["`opensearch-ui-application-id`"]
            }
        }
    }]
}
```

## Revoking access to OpenSearch

UI in a VPC endpoint policy

OpenSearch UI requires explicit permission in the VPC endpoint policy to allow
users to access the application from the VPC. If you no longer want users to access
OpenSearch UI from the VPC, you can remove the permission in the endpoint policy.
After this, users encounter a `403 forbidden` error message when
attempting to access OpenSearch UI.

For information about updating a VPC endpoint policy, see [Update a VPC endpoint policy](../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy "../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy") in the
_AWS PrivateLink Guide_.

The following is an example of VPC endpoint policy that denies access to the UI
applications from the VPC:

```
{
    "Statement": [{
        "Action": ["opensearch:*"],
        "Effect": "Allow",
        "Principal": "*",
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "opensearch:ApplicationId": [""]
            }
        }
    }]
}
```
