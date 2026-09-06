

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Create the Amazon VPC endpoint for Amazon S3
<a name="mf-runtime-setup-vpc"></a>

In this section, you create a Amazon VPC endpoint for Amazon S3 to use. Setting up this endpoint will help you later when setting up internet access for VPC. 

1. Navigate to Amazon VPC in the AWS Management Console.

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.  
![VPC endpoints with Create Endpoint active.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-s3-endpoint_1.jpg)

1. Enter a meaningful name tag, for example: “Micro-Focus-License-S3”.

1. Choose **AWS Services** as the Service Category.  
![Endpoint Settings with sample name tag entered.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-s3-endpoint_2.png)

1. Under **Services** search for the Amazon S3 Gateway service: **com.amazonaws.[region].s3**.

   For `us-west-1` this would be: `com.amazonaws.us-west-1.s3`.

1. Choose the **Gateway** service.  
![Services with Amazon S3 Gateway service selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-s3-endpoint_3.png)

1. For VPC choose the VPC you will be using.  
![VPC with a VPC entered.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-s3-endpoint_4.png)

1. Choose all of the route tables for the VPC.  
![Route tables with all route tables selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-s3-endpoint_5.png)

1. Under **Policy** choose **Full Access**.  
![Policy with Full Access selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-s3-endpoint_6.png)
**Note**  
If you decide to create a custom policy, make sure it has access to the Amazon S3 bucket `s3://aws-supernova-marketplace-<region>-prod`.

1. Choose **Create Endpoint**.