# Creating the Amazon S3 VPC Endpoint

The Neptune loader requires a VPC endpoint of type Gateway for Amazon S3.

###### To set up access for Amazon S3

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create Endpoint**.
4. Choose the **Service Name**
   `com.amazonaws.`region`.s3` for the Gateway type endpoint.

###### Note

If the Region here is incorrect, make sure that the console Region is correct. 5. Choose the VPC that contains your Neptune DB instance (it is listed for your
DB instance in the Neptune console). 6. Select the check box next to the route tables that are associated with the subnets
related to your cluster. If you only have one route table, you must select that
box. 7. Choose **Create Endpoint**.
For information about creating the endpoint, see [VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md#create-vpc-endpoint "../../../vpc/latest/userguide/vpc-endpoints.md#create-vpc-endpoint") in the
_Amazon VPC User Guide_. For information about the limitations of VPC
endpoints, [VPC Endpoints for
Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md "../../../vpc/latest/userguide/vpc-endpoints-s3.md").

###### Next Steps

Now that you have granted access to the Amazon S3 bucket, you can prepare to load data. For
information about supported formats, see [Load Data Formats](bulk-load-tutorial-format.md "bulk-load-tutorial-format.md").
