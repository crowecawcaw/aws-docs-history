# Use `DeleteVpcEndpoints` with an AWS SDK or CLI

The following code examples show how to use `DeleteVpcEndpoints`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Create a VPC with private subnets and NAT gateways](example_vpc_GettingStartedPrivate_section.md "example_vpc_GettingStartedPrivate_section.md")

CLI

**AWS CLI**

**To delete an endpoint**

This example deletes endpoints vpce-aa22bb33 and vpce-1a2b3c4d. If the command is partially successful or unsuccessful, a list of unsuccessful items is returned. If the command succeeds, the returned list is empty.

Command:

```
`aws ec2 delete-vpc-endpoints --vpc-endpoint-ids `vpce-aa22bb33` `vpce-1a2b3c4d``

```

Output:

```
{
  "Unsuccessful": []
}
```

- For API details, see
  [DeleteVpcEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoints.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoints.html")
  in _AWS CLI Command Reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/ec2#code-examples").

```

    /**
     * @param string $vpcEndpointId
     * @return void
     */
    public function deleteVpcEndpoint(string $vpcEndpointId)
    {
        try {
            $this->ec2Client->deleteVpcEndpoints([
                "VpcEndpointIds" => [$vpcEndpointId],
            ]);
        }catch (Ec2Exception $caught){
            echo "There was a problem deleting the VPC Endpoint: {$caught->getAwsErrorMessage()}\n";
            throw $caught;
        }
    }



```

- For API details, see
  [DeleteVpcEndpoints](../../../goto/SdkForPHPV3/ec2-2016-11-15/DeleteVpcEndpoints.md "../../../goto/SdkForPHPV3/ec2-2016-11-15/DeleteVpcEndpoints.md")
  in _AWS SDK for PHP API Reference_.

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


    def delete_vpc_endpoints(self, vpc_endpoint_ids: list[str]) -> None:
        """
        Deletes the specified VPC endpoints.

        :param vpc_endpoint_ids: A list of IDs of the VPC endpoints to delete.
        """
        try:
            self.ec2_client.delete_vpc_endpoints(VpcEndpointIds=vpc_endpoint_ids)
        except ClientError as err:
            logger.error(
                "Couldn't delete VPC endpoints %s. Here's why: %s: %s",
                vpc_endpoint_ids,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [DeleteVpcEndpoints](../../../goto/boto3/ec2-2016-11-15/DeleteVpcEndpoints.md "../../../goto/boto3/ec2-2016-11-15/DeleteVpcEndpoints.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ec2#code-examples").

```
    TRY.
        lo_ec2->deletevpcendpoints( it_vpcendpointids = it_vpc_endpoint_ids ).
        MESSAGE 'Deleted VPC endpoint(s).' TYPE 'I'.
      CATCH /aws1/cx_rt_service_generic INTO DATA(lo_exception).
        DATA(lv_error) = |"{ lo_exception->av_err_code }" - { lo_exception->av_err_msg }|.
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [DeleteVpcEndpoints](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
