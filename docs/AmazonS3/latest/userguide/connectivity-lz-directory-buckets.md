

# Private connectivity from your VPC
<a name="connectivity-lz-directory-buckets"></a>

To reduce network latency, configure your virtual private cloud (VPC) with a gateway endpoint to access directory buckets in Availability Zones. This keeps traffic within the AWS network at no additional cost.

**To configure a gateway VPC endpoint**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/). 

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. Create a name for your endpoint.

1. For **Service category**, choose **AWS services**. 

1. For **Services**, add the filter **Type=Gateway** and then choose the option button next to **com.amazonaws.{{region}}.s3express**. 

1. For **VPC**, choose the VPC in which to create the endpoint.

1. For **Route tables**, choose the route table in your VPC to be used by the endpoint. After the endpoint is created, a route record will be added to the route table that you select in this step.

1. For **Policy**, choose **Full access** to allow all operations by all principals on all resources over the VPC endpoint. Otherwise, choose **Custom** to attach a VPC endpoint policy that controls the principals' permissions to perform actions on resources over the VPC endpoint. 

1. For **IP address type**, choose from the following options:
   +  **IPv4** – Assign IPv4 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have IPv4 address ranges and the service accepts IPv4 requests. 
   +  **IPv6** – Assign IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets are IPv6 only subnets and the service accepts IPv6 requests.
   +  **Dualstack** – Assign both IPv4 and IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges and the service accepts both IPv4 and IPv6 requests.

1. (Optional) To add a tag, choose **Add new tag**, and enter the tag key and the tag value.

1. Choose **Create endpoint**.

To learn more about gateway VPC endpoints, see [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html) in the *AWS PrivateLink Guide*. For data residency use cases, enable access to your buckets only from your VPC using gateway VPC endpoints. When access is restricted to a VPC or a VPC endpoint, you can access the objects through the AWS Management Console, the REST API, AWS CLI, and AWS SDKs.

**Note**  
To restrict access to a VPC or a VPC endpoint using the AWS Management Console, you must use the AWS Management Console Private Access. For more information, see [AWS Management Console Private Access](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/console-private-access.html) in the *AWS Management Console guide*.