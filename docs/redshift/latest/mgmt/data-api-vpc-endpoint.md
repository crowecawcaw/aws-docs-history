Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating an Amazon VPC endpoint (AWS PrivateLink)

for the Data API

Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources, such as Amazon Redshift clusters and
applications, into a virtual private cloud (VPC). AWS PrivateLink provides private
connectivity between virtual private clouds (VPCs) and AWS services securely on
the Amazon network. Using AWS PrivateLink, you can create VPC endpoints, which you can
use connect to services across different accounts and VPCs based on Amazon VPC. For more
information about AWS PrivateLink, see [VPC Endpoint Services
(AWS PrivateLink)](../../../vpc/latest/userguide/endpoint-service.md "../../../vpc/latest/userguide/endpoint-service.md") in the _Amazon Virtual Private Cloud User Guide_.

You can call the Data API with Amazon VPC endpoints. Using an Amazon VPC endpoint keeps
traffic between applications in your Amazon VPC and the Data API in the AWS
network, without using public IP addresses. Amazon VPC endpoints can help you meet
compliance and regulatory requirements related to limiting public internet
connectivity. For example, if you use an Amazon VPC endpoint, you can keep traffic
between an application running on an Amazon EC2 instance and the Data API in the
VPCs that contain them.

After you create the Amazon VPC endpoint, you can start using it without making any
code or configuration changes in your application.

###### To create an Amazon VPC endpoint for the Data API

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Choose **Endpoints**, and then choose **Create
   Endpoint**.
3. On the **Create Endpoint** page, for **Service
   category**, choose **AWS services**. For
   **Service Name**, choose
   **redshift-data**
   (`com.amazonaws.`region`.redshift-data`).
4. For **VPC**, choose the VPC to create the endpoint
   in.

Choose the VPC that contains the application that makes Data API
calls. 5. For **Subnets**, choose the subnet for each Availability
Zone (AZ) used by the AWS service that is running your application.

To create an Amazon VPC endpoint, specify the private IP address range in which
the endpoint is accessible. To do this, choose the subnet for each
Availability Zone. Doing so restricts the VPC endpoint to the private IP
address range specific to each Availability Zone and also creates an Amazon VPC
endpoint in each Availability Zone. 6. For **Enable DNS name**, select **Enable for this
endpoint**.

Private DNS resolves the standard Data API DNS hostname
(`https://redshift-data.`region`.amazonaws.com`)
to the private IP addresses associated with the DNS hostname specific to
your Amazon VPC endpoint. As a result, you can access the Data API VPC
endpoint using the AWS CLI or AWS SDKs without making any code or
configuration changes to update the Data API endpoint URL. 7. For **Security group**, choose a security group to
associate with the Amazon VPC endpoint.

Choose the security group that allows access to the AWS service that is
running your application. For example, if an Amazon EC2 instance is running your
application, choose the security group that allows access to the Amazon EC2
instance. The security group enables you to control the traffic to the Amazon VPC
endpoint from resources in your VPC. 8. Choose **Create endpoint**.
After the endpoint is created, choose the link in the AWS Management Console to view the
endpoint details.

The endpoint **Details** tab shows the DNS hostnames that were
generated while creating the Amazon VPC endpoint.

You can use the standard endpoint
(`redshift-data.`region`.amazonaws.com`)
or one of the VPC-specific endpoints to call the Data API within the Amazon VPC. The
standard Data API endpoint automatically routes to the Amazon VPC endpoint. This routing
occurs because the Private DNS hostname was enabled when the Amazon VPC endpoint was
created.

When you use an Amazon VPC endpoint in a Data API call, all traffic between your
application and the Data API remains in the Amazon VPCs that contain them. You can
use an Amazon VPC endpoint for any type of Data API call. For information about
calling the Data API, see [Considerations when calling the
Amazon Redshift Data API](data-api.md#data-api-calling-considerations "data-api.md#data-api-calling-considerations").
