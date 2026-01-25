# Use `CreateVpcEndpoint` with an AWS SDK or CLI

The following code examples show how to use `CreateVpcEndpoint`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Create a VPC with private subnets and NAT gateways](example_vpc_GettingStartedPrivate_section.md "example_vpc_GettingStartedPrivate_section.md")

CLI

**AWS CLI**

**Example 1: To create a gateway endpoint**

The following `create-vpc-endpoint` example creates a gateway VPC endpoint between VPC `vpc-1a2b3c4d` and Amazon S3 in the `us-east-1` region, and associates route table `rtb-11aa22bb` with the endpoint.

```
`aws ec2 create-vpc-endpoint \
 --vpc-id `vpc-1a2b3c4d` \
 --service-name `com.amazonaws.us-east-1.s3` \
 --route-table-ids `rtb-11aa22bb``

```

Output:

```
{
    "VpcEndpoint": {
        "PolicyDocument": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Sid\":\"\",\"Effect\":\"Allow\",\"Principal\":\"\*\",\"Action\":\"\*\",\"Resource\":\"\*\"}]}",
        "VpcId": "vpc-1a2b3c4d",
        "State": "available",
        "ServiceName": "com.amazonaws.us-east-1.s3",
        "RouteTableIds": [
            "rtb-11aa22bb"
        ],
        "VpcEndpointId": "vpc-1a2b3c4d",
        "CreationTimestamp": "2015-05-15T09:40:50Z"
    }
}
```

For more information, see [Create a gateway endpoint](../../../vpc/latest/privatelink/vpc-endpoints-s3.md#create-gateway-endpoint-s3 "../../../vpc/latest/privatelink/vpc-endpoints-s3.md#create-gateway-endpoint-s3") in the _AWS PrivateLink User Guide_.

**Example 2: To create an interface endpoint**

The following `create-vpc-endpoint` example creates an interface VPC endpoint between VPC `vpc-1a2b3c4d` and Amazon S3 in the `us-east-1` region. The command creates the endpoint in subnet `subnet-1a2b3c4d`, associates it with security group `sg-1a2b3c4d`, and adds a tag with a key of "Service" and a Value of "S3".

```
`aws ec2 create-vpc-endpoint \
 --vpc-id `vpc-1a2b3c4d` \
 --vpc-endpoint-type `Interface` \
 --service-name `com.amazonaws.us-east-1.s3` \
 --subnet-ids `subnet-7b16de0c` \
 --security-group-id `sg-1a2b3c4d` \
 --tag-specifications `ResourceType=vpc-endpoint,Tags=[{Key=service,Value=S3}]``

```

Output:

```
{
    "VpcEndpoint": {
        "VpcEndpointId": "vpce-1a2b3c4d5e6f1a2b3",
        "VpcEndpointType": "Interface",
        "VpcId": "vpc-1a2b3c4d",
        "ServiceName": "com.amazonaws.us-east-1.s3",
        "State": "pending",
        "RouteTableIds": [],
        "SubnetIds": [
            "subnet-1a2b3c4d"
        ],
        "Groups": [
            {
                "GroupId": "sg-1a2b3c4d",
                "GroupName": "default"
            }
        ],
        "PrivateDnsEnabled": false,
        "RequesterManaged": false,
        "NetworkInterfaceIds": [
            "eni-0b16f0581c8ac6877"
        ],
        "DnsEntries": [
            {
                "DnsName": "*.vpce-1a2b3c4d5e6f1a2b3-9hnenorg.s3.us-east-1.vpce.amazonaws.com",
                "HostedZoneId": "Z7HUB22UULQXV"
            },
            {
                "DnsName": "*.vpce-1a2b3c4d5e6f1a2b3-9hnenorg-us-east-1c.s3.us-east-1.vpce.amazonaws.com",
                "HostedZoneId": "Z7HUB22UULQXV"
            }
        ],
        "CreationTimestamp": "2021-03-05T14:46:16.030000+00:00",
        "Tags": [
            {
                "Key": "service",
                "Value": "S3"
            }
        ],
        "OwnerId": "123456789012"
    }
}
```

For more information, see [Create an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _AWS PrivateLink User Guide_.

**Example 3: To create a Gateway Load Balancer endpoint**

The following `create-vpc-endpoint` example creates a Gateway Load Balancer endpoint between VPC `vpc-111122223333aabbc` and and a service that is configured using a Gateway Load Balancer.

```
`aws ec2 create-vpc-endpoint \
 --service-name `com.amazonaws.vpce.us-east-1.vpce-svc-123123a1c43abc123` \
 --vpc-endpoint-type `GatewayLoadBalancer` \
 --vpc-id `vpc-111122223333aabbc` \
 --subnet-ids `subnet-0011aabbcc2233445``

```

Output:

```
{
    "VpcEndpoint": {
        "VpcEndpointId": "vpce-aabbaabbaabbaabba",
        "VpcEndpointType": "GatewayLoadBalancer",
        "VpcId": "vpc-111122223333aabbc",
        "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-123123a1c43abc123",
        "State": "pending",
        "SubnetIds": [
            "subnet-0011aabbcc2233445"
        ],
        "RequesterManaged": false,
        "NetworkInterfaceIds": [
            "eni-01010120203030405"
        ],
        "CreationTimestamp": "2020-11-11T08:06:03.522Z",
        "OwnerId": "123456789012"
    }
}
```

For more information, see [Gateway Load Balancer endpoints](../../../vpc/latest/privatelink/gateway-load-balancer-endpoints.md "../../../vpc/latest/privatelink/gateway-load-balancer-endpoints.md") in the _AWS PrivateLink User Guide_.

**Example 4: To create a resource endpoint**

The following `create-vpc-endpoint` example creates a resource endpoint.

```
`aws ec2 create-vpc-endpoint \
 --vpc-endpoint-type `Resource` \
 --vpc-id `vpc-111122223333aabbc` \
 --subnet-ids `subnet-0011aabbcc2233445` \
 --resource-configuration-arn `arn:aws:vpc-lattice-us-east-1:123456789012:resourceconfiguration/rcfg-0123abcde98765432``

```

Output:

```
{
    "VpcEndpoint": {
        "VpcEndpointId": "vpce-00939a7ed9EXAMPLE",
        "VpcEndpointType": "Resource",
        "VpcId": "vpc-111122223333aabbc",
        "State": "Pending",
        "SubnetIds": [
            "subnet-0011aabbcc2233445"
        ],
        "Groups": [
            {
                "GroupId": "sg-03e2f15fbfc09b000",
                "GroupName": "default"
            }
        ],
        "IpAddressType": "IPV4",
        "PrivateDnsEnabled": false,
        "CreationTimestamp": "2025-02-06T23:38:49.525000+00:00",
        "Tags": [],
        "OwnerId": "123456789012",
        "ResourceConfigurationArn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-0123abcde98765432"
    }
}
```

For more information, see [Resource endpoints](../../../vpc/latest/privatelink/privatelink-access-resources.md "../../../vpc/latest/privatelink/privatelink-access-resources.md") in the _AWS PrivateLink User Guide_.

**Example 5: To create a service network endpoint**

The following `create-vpc-endpoint` example creates a service network endpoint.

```
`aws ec2 create-vpc-endpoint \
 --vpc-endpoint-type `ServiceNetwork` \
 --vpc-id `vpc-111122223333aabbc` \
 --subnet-ids `subnet-0011aabbcc2233445` \
 --service-network-arn `arn:aws:vpc-lattice:us-east-1:123456789012:servicenetwork/sn-0101abcd5432abcd0` \
 --security-group-ids `sg-0123456789012abcd``

```

Output:

```
{
    "VpcEndpoint": {
        "VpcEndpointId": "vpce-0f00567fa8EXAMPLE",
        "VpcEndpointType": "ServiceNetwork",
        "VpcId": "vpc-111122223333aabbc",
        "State": "Pending",
        "SubnetIds": [
            "subnet-0011aabbcc2233445"
        ],
        "Groups": [
            {
                "GroupId": "sg-0123456789012abcd",
                "GroupName": "my-security-group"
            }
        ],
        "IpAddressType": "IPV4",
        "PrivateDnsEnabled": false,
        "CreationTimestamp": "2025-02-06T23:44:20.449000+00:00",
        "Tags": [],
        "OwnerId": "123456789012",
        "ServiceNetworkArn": "arn:aws:vpc-lattice:us-east-1:123456789012:servicenetwork/sn-0101abcd5432abcd0"
    }
}
```

For more information, see [Service network endpoints](../../../vpc/latest/privatelink/privatelink-access-service-networks.md "../../../vpc/latest/privatelink/privatelink-access-service-networks.md") in the _AWS PrivateLink User Guide_.

- For API details, see
  [CreateVpcEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html")
  in _AWS CLI Command Reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/ec2#code-examples").

```

    /**
     * @param string $serviceName
     * @param string $vpcId
     * @param array $routeTableIds
     * @return array
     */
    public function createVpcEndpoint(string $serviceName, string $vpcId, array $routeTableIds): array
    {
        try {
            $result = $this->ec2Client->createVpcEndpoint([
                'ServiceName' => $serviceName,
                'VpcId' => $vpcId,
                'RouteTableIds' => $routeTableIds,
            ]);

            return $result["VpcEndpoint"];
        } catch(Ec2Exception $caught){
            echo "There was a problem creating the VPC Endpoint: {$caught->getAwsErrorMessage()}\n";
            throw $caught;
        }
    }



```

- For API details, see
  [CreateVpcEndpoint](../../../goto/SdkForPHPV3/ec2-2016-11-15/CreateVpcEndpoint.md "../../../goto/SdkForPHPV3/ec2-2016-11-15/CreateVpcEndpoint.md")
  in _AWS SDK for PHP API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example create a new VPC Endpoint for the service com.amazonaws.eu-west-1.s3 in the VPC vpc-0fc1ff23f45b678eb**

```
New-EC2VpcEndpoint -ServiceName com.amazonaws.eu-west-1.s3 -VpcId vpc-0fc1ff23f45b678eb

```

**Output:**

```
ClientToken VpcEndpoint
----------- -----------
            Amazon.EC2.Model.VpcEndpoint
```

- For API details, see
  [CreateVpcEndpoint](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example create a new VPC Endpoint for the service com.amazonaws.eu-west-1.s3 in the VPC vpc-0fc1ff23f45b678eb**

```
New-EC2VpcEndpoint -ServiceName com.amazonaws.eu-west-1.s3 -VpcId vpc-0fc1ff23f45b678eb

```

**Output:**

```
ClientToken VpcEndpoint
----------- -----------
            Amazon.EC2.Model.VpcEndpoint
```

- For API details, see
  [CreateVpcEndpoint](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ec2#code-examples").

```
class VpcWrapper:
    """Encapsulates Amazon Elastic Compute Cloud (Amazon EC2) Amazon Virtual Private Cloud actions."""

    def __init__(self, ec2_client: boto3.client):
        """
        Initializes the VpcWrapper with an EC2 client.

        :param ec2_client: A Boto3 Amazon EC2 client. This client provides low-level
                           access to AWS EC2 services.
        """
        self.ec2_client = ec2_client

    @classmethod
    def from_client(cls) -> "VpcWrapper":
        """
        Creates a VpcWrapper instance with a default EC2 client.

        :return: An instance of VpcWrapper initialized with the default EC2 client.
        """
        ec2_client = boto3.client("ec2")
        return cls(ec2_client)


    def create_vpc_endpoint(
        self, vpc_id: str, service_name: str, route_table_ids: list[str]
    ) -> Dict[str, Any]:
        """
        Creates a new VPC endpoint for the specified service and associates it with the specified route tables.

        :param vpc_id: The ID of the VPC to create the endpoint in.
        :param service_name: The name of the service to create the endpoint for.
        :param route_table_ids: A list of IDs of the route tables to associate with the endpoint.
        :return: A dictionary representing the newly created VPC endpoint.
        """
        try:
            response = self.ec2_client.create_vpc_endpoint(
                VpcId=vpc_id,
                ServiceName=service_name,
                RouteTableIds=route_table_ids,
            )
            return response["VpcEndpoint"]
        except ClientError as err:
            logger.error(
                "Couldn't create VPC endpoint for service %s. Here's why: %s: %s",
                service_name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [CreateVpcEndpoint](../../../goto/boto3/ec2-2016-11-15/CreateVpcEndpoint.md "../../../goto/boto3/ec2-2016-11-15/CreateVpcEndpoint.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ec2#code-examples").

```
    " iv_vpc_id = 'vpc-abc123'
    " iv_service_name = 'com.amazonaws.region.service'
    TRY.
        oo_result = lo_ec2->createvpcendpoint(             " oo_result is returned for testing purposes. "
          iv_vpcid = iv_vpc_id
          iv_servicename = iv_service_name
          it_routetableids = it_route_table_ids ).
        DATA(lv_vpc_endpoint_id) = oo_result->get_vpcendpoint( )->get_vpcendpointid( ).
        MESSAGE 'Created VPC endpoint.' TYPE 'I'.
      CATCH /aws1/cx_rt_service_generic INTO DATA(lo_exception).
        DATA(lv_error) = |"{ lo_exception->av_err_code }" - { lo_exception->av_err_msg }|.
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [CreateVpcEndpoint](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
