

# Creating the Amazon S3 VPC Endpoint
<a name="bulk-load-tutorial-vpc"></a>

The Neptune loader requires a VPC endpoint of type Gateway for Amazon S3.

**To set up access for Amazon S3**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create Endpoint**.

1. Choose the **Service Name** `com.amazonaws.{{region}}.s3` for the Gateway type endpoint.
**Note**  
If the Region here is incorrect, make sure that the console Region is correct.

1. Choose the VPC that contains your Neptune DB instance (it is listed for your DB instance in the Neptune console).

1. Select the check box next to the route tables that are associated with the subnets related to your cluster. If you only have one route table, you must select that box.

1. Choose **Create Endpoint**.

For information about creating the endpoint, see [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html#create-vpc-endpoint) in the *Amazon VPC User Guide*. For information about the limitations of VPC endpoints, [VPC Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html).

**Next Steps**  
Now that you have granted access to the Amazon S3 bucket, you can prepare to load data. For information about supported formats, see [Load Data Formats](bulk-load-tutorial-format.md).