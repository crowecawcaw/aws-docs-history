# Private connectivity from your

VPC

To reduce the amount of time your packets spend on the network, configure your virtual private cloud (VPC) with a gateway endpoint to access directory buckets in Availability Zones while keeping traffic within the AWS network, and at no additional cost.

###### To configure a gateway VPC endpoint

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
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
8. For **Route tables**, choose the route table in your VPC to be used by the endpoint. After the endpoint is created, a route record will be added to the route table that you select in this step.
9. For **Policy**, choose **Full access** to allow
   all operations by all principals on all resources over the VPC endpoint.
   Otherwise, choose **Custom** to attach a VPC endpoint policy that
   controls the principals' permissions to perform actions on resources over the VPC endpoint.
10. For **IP address type**, choose from the following options:
    - **IPv4** – Assign IPv4 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have IPv4 address ranges and the service accepts IPv4 requests.
    - **IPv6** – Assign IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets are IPv6 only subnets and the service accepts IPv6 requests.
    - **Dualstack** – Assign both IPv4 and IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges and the service accepts both IPv4 and IPv6 requests.

11. (Optional) To add a tag, choose **Add new tag**, and enter the
    tag key and the tag value.
12. Choose **Create endpoint**.
    To learn more about gateway VPC endpoints, see [Gateway endpoints](../../../vpc/latest/privatelink/gateway-endpoints.md "../../../vpc/latest/privatelink/gateway-endpoints.md") in the _AWS PrivateLink Guide_.
    For the data
    residency use cases, we recommend enabling access to your buckets only from your VPC using
    gateway VPC endpoints. When access is restricted to a VPC or a VPC endpoint, you can access the objects through the AWS Management Console, the REST
    API, AWS CLI, and AWS SDKs.

###### Note

To restrict access to a VPC or a VPC endpoint using the AWS Management Console, you must use the AWS Management Console Private Access. For more information, see [AWS Management Console Private Access](../../../awsconsolehelpdocs/latest/gsg/console-private-access.md "../../../awsconsolehelpdocs/latest/gsg/console-private-access.md") in the _AWS Management Console guide_.
