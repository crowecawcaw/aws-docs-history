

# Connector for SCEP VPC endpoints (AWS PrivateLink)
<a name="c4scep-vpc-endpoints"></a>

You can create a private connection between your VPC and Connector for SCEP by configuring an interface VPC endpoint. Interface endpoints are powered by [AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.html), a technology for privately accessing Connector for SCEP API operations. AWS PrivateLink routes all network traffic between your VPC and Connector for SCEP through the Amazon network, avoiding exposure on the open internet. Each VPC endpoint is represented by one or more [elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) with private IP addresses in your VPC subnets.

The interface VPC endpoint connects your VPC directly to Connector for SCEP without an internet gateway, NAT device, VPN connection, or Direct Connect connection. The instances in your VPC don't need public IP addresses to communicate with the Connector for SCEP API.

To use Connector for SCEP through your VPC, you must connect from an instance that is inside the VPC. Alternatively, you can connect your private network to your VPC by using an AWS Virtual Private Network (Site-to-Site VPN) or Direct Connect. For information about Site-to-Site VPN, see [VPN Connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html) in the *Amazon VPC User Guide*. For information about Direct Connect, see [Creating a Connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dedicated_connection.html#create-connection) in the *Direct Connect User Guide*.

Connector for SCEP does not require the use of AWS PrivateLink, but we recommend it as an additional layer of security. For more information about AWS PrivateLink and VPC endpoints, see [Accessing Services Through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/userguide/privatelink-access-aws-services.html).

## Considerations for Connector for SCEP VPC endpoints
<a name="c4scep-vpc-endpoint-considerations"></a>

Before you set up interface VPC endpoints for Connector for SCEP, be aware of the following considerations:
+ Connector for SCEP might not support VPC endpoints in some Availability Zones. When you create a VPC endpoint, first check support in the management console. Unsupported Availability Zones are marked "Service not supported in this Availability Zone."
+ VPC endpoints do not support cross-Region requests. Ensure that you create your endpoint in the same Region where you create your connector.
+ VPC endpoints only support Amazon provided DNS through Amazon Route 53. If you want to use your own DNS, you can use conditional DNS forwarding. For more information, see [DHCP Options Sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.
+ The security group attached to the VPC endpoint must allow incoming connections on port 443 from the private subnet of the VPC.

## Creating the VPC endpoint for Connector for SCEP
<a name="c4scep-vpc-endpoint-create"></a>

You can create a VPC endpoint for the Connector for SCEP service using either the VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/) or the AWS Command Line Interface. For more information, see the [Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) procedure in the *Amazon VPC User Guide*. Connector for SCEP supports making calls to all of its API operations inside your VPC.

When creating the endpoint, specify `com.amazonaws.{{region}}.pca-connector-scep` as the service name.

If you have enabled private DNS host names for the endpoint, then the default Connector for SCEP endpoint now resolves to your VPC endpoint. For a comprehensive list of default service endpoints, see [Service Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html).

If you have not enabled private DNS host names, Amazon VPC provides a DNS endpoint name that you can use in the following format:

```
{{vpc-endpoint-id}}.pca-connector-scep.{{region}}.vpce.amazonaws.com
```

For more information, see [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) in the *Amazon VPC User Guide*.

## Create a VPC endpoint policy for Connector for SCEP
<a name="c4scep-vpc-endpoint-policy"></a>

You can create a policy for Amazon VPC endpoints for Connector for SCEP to specify the following:
+ The principal that can perform actions
+ The actions that can be performed
+ The resources on which actions can be performed

For more information, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC Guide*.

**Example – VPC endpoint policy for Connector for SCEP actions**  
When attached to an endpoint, the following policy grants access for all principals to the listed Connector for SCEP actions on the specified connector resource.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "pca-connector-scep:GetConnector",
            "pca-connector-scep:ListConnectors"
         ],
         "Resource": "arn:aws:pca-connector-scep:{{region}}:{{account}}:connector/{{connector-id}}"
      }
   ]
}
```

## Creating a VPC endpoint for Connector for SCEP enrollment operations
<a name="c4scep-vpc-endpoint-enrollment"></a>

Connector for SCEP provides a separate VPC endpoint service for enrollment operations such as `GetCACaps` and `PKIOperation`.

When creating the enrollment endpoint, specify `com.amazonaws.{{region}}.pca-connector-scep.enroll` as the service name.

When creating a connector, you can optionally specify a `VpcEndpointId` to restrict the connector to only be accessible through that specific VPC endpoint.

If you have not enabled private DNS host names, Amazon VPC provides a DNS endpoint name that you can use in the following format:

```
{{vpc-endpoint-id}}.enroll.pca-connector-scep.{{region}}.vpce.amazonaws.com
```

**Note**  
To reach your connector, you must use the endpoint URL included in the connector details, not the VPC endpoint DNS name directly. However, you can replace the DNS name portion of the connector endpoint URL with any valid VPC endpoint DNS name, such as an AZ-specific DNS name.  
 For instance, to use an AZ specific DNS name, you may replace   

```
https://{{vpc-endpoint-id}}.enroll.pca-connector-scep.{{region}}.vpce.amazonaws.com/{{account-id}}-{{connector-id}}/{{UUID}}
```
 with   

```
https://{{vpc-endpoint-id}}-{{availability-zone}}.enroll.pca-connector-scep.{{region}}.vpce.amazonaws.com/{{account-id}}-{{connector-id}}/{{UUID}}
```

**Example – VPC endpoint policy for Connector for SCEP enrollment operations**  
You can attach a VPC endpoint policy to control access to enrollment operations. When attached to an endpoint, the following policy grants access for all principals to the `GetCACaps` and `PKIOperation` operations. The resource in the stanza is a connector.

Connector for SCEP enrollment operations aren't authenticated with SigV4. Due to this, they aren't associated with an IAM principal and instead are considered anonymous by VPC endpoint policies. As such, your VPC endpoint policy must allow all principals for these actions.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "pca-connector-scep:GetCACaps",
            "pca-connector-scep:GetCACert",
            "pca-connector-scep:PKIOperation"
         ],
         "Resource": [
            arn:{{aws}}:pca-connector-scep:{{us-east-1}}:{{111122223333}}:connector/{{11223344-1234-1122-2233-112233445566}}
         ]
      }
   ]
}
```