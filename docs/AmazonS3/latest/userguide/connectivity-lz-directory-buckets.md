# Private connectivity from your

VPC

You can use a gateway endpoint to access directory buckets in AWS Local Zones (Local Zones) from
your virtual private cloud (VPC), without requiring an internet gateway or NAT device for your VPC, and at
no additional cost. The following topic describes configuring gateway VPC endpoints
between your VPC and directory buckets in Local Zones.

###### To configure a gateway VPC endpoint

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. Create a name for your endpoint.
5. For **Service category**, choose
   **AWS services**.
6. For **Services**, add the filter
   **Type=Gateway** and then choose the option button next to
   **com.amazonaws.`region`.s3express**.
7. For **VPC**, choose the VPC in which to create the
   endpoint.
8. For **Route tables**, select the route table on your Local Zone to be
   used by the endpoint. After the endpoint is created, a route record will be added to
   the route table that you select in this step.
9. For **Policy**, choose **Full access** to allow
   all operations by all principals on all resources over the VPC endpoint.
   Otherwise, choose **Custom** to attach a VPC endpoint policy that
   controls the principals' permissions to perform actions on resources over the VPC endpoint.
10. (Optional) To add a tag, choose **Add new tag**, and enter the
    tag key and the tag value.
11. Choose **Create endpoint**.
    To learn more about gateway VPC endpoints, see [Gateway endpoints](../../../vpc/latest/privatelink/gateway-endpoints.md "../../../vpc/latest/privatelink/gateway-endpoints.md") in the _AWS PrivateLink Guide_.
    For the data
    residency use cases, we recommend enabling access to your buckets only from your VPC using
    gateway VPC endpoints. When access is restricted to a VPC or a VPC endpoint, you can access the objects through the AWS Management Console, the REST
    API, AWS CLI, and AWS SDKs.

###### Note

To restrict access to a VPC or a VPC endpoint using the AWS Management Console, you must use the AWS Management Console Private Access. For more information, see [AWS Management Console Private Access](../../../awsconsolehelpdocs/latest/gsg/console-private-access.md "../../../awsconsolehelpdocs/latest/gsg/console-private-access.md") in the _AWS Management Console guide_.
