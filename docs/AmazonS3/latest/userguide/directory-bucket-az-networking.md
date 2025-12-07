# Networking for directory buckets in an Availability Zone

To reduce the amount of time your packets spend on the network, configure your virtual private cloud (VPC) with a gateway endpoint to access directory buckets in Availability Zones while keeping traffic within the AWS network, and at no additional cost.

###### Topics

- [Endpoints for directory buckets in Availability Zones](#s3-express-endpoints-az "#s3-express-endpoints-az")
- [Configuring VPC gateway
  endpoints](#s3-express-networking-vpc-gateway "#s3-express-networking-vpc-gateway")

## Endpoints for directory buckets in Availability Zones

The following table shows the Regional and Zonal API endpoints that are available for
each Region and Availability Zone.

| Region name           | Region           | Availability Zone IDs                  | Regional endpoint                                                                                              | Zonal endpoint                                                                                                                                                                                                                                                                                                                   |
| --------------------- | ---------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia) | `us-east-1`      | `use1-az4`<br>`use1-az5`<br>`use1-az6` | `s3express-control.us-east-1.amazonaws.com`<br>`s3express-control-dualstack.us-east-1.amazonaws.com`           | `s3express-use1-az4.us-east-1.amazonaws.com`<br>`s3express-use1-az4.dualstack.us-east-1.amazonaws.com`<br>`s3express-use1-az5.us-east-1.amazonaws.com`<br>`s3express-use1-az5.dualstack.us-east-1.amazonaws.com`<br>`s3express-use1-az6.us-east-1.amazonaws.com`<br>`s3express-use1-az6.dualstack.us-east-1.amazonaws.com`       |
| US East (Ohio)        | `us-east-2`      | `use2-az1`<br>`use2-az2`               | `s3express-control.us-east-2.amazonaws.com`<br>`s3express-control-dualstack.us-east-2.amazonaws.com`           | `s3express-use2-az1.us-east-2.amazonaws.com`<br>`s3express-use2-az1.dualstack.us-east-2.amazonaws.com`<br>`s3express-use2-az2.us-east-2.amazonaws.com`<br>`s3express-use2-az2.dualstack.us-east-2.amazonaws.com`                                                                                                                 |
| US West (Oregon)      | `us-west-2`      | `usw2-az1`<br>`usw2-az3`<br>`usw2-az4` | `s3express-control.us-west-2.amazonaws.com`<br>`s3express-control-dualstack.us-west-2.amazonaws.com`           | `s3express-usw2-az1.us-west-2.amazonaws.com`<br>`s3express-usw2-az1.dualstack.us-west-2.amazonaws.com`<br>`s3express-usw2-az3.us-west-2.amazonaws.com`<br>`s3express-usw2-az3.dualstack.us-west-2.amazonaws.com`<br>`s3express-usw2-az4.us-west-2.amazonaws.com`<br>`s3express-usw2-az4.dualstack.us-west-2.amazonaws.com`       |
| Asia Pacific (Mumbai) | `ap-south-1`     | `aps1-az1`<br>`aps1-az3`               | `s3express-control.ap-south-1.amazonaws.com`<br>`s3express-control-dualstack.ap-south-1.amazonaws.com`         | `s3express-aps1-az1.ap-south-1.amazonaws.com`<br>`s3express-aps1-az1.dualstack.ap-south-1.amazonaws.com`<br>`s3express-aps1-az3.ap-south-1.amazonaws.com`<br>`s3express-aps1-az3.dualstack.ap-south-1.amazonaws.com`                                                                                                             |
| Asia Pacific (Tokyo)  | `ap-northeast-1` | `apne1-az1`<br>`apne1-az4`             | `s3express-control.ap-northeast-1.amazonaws.com`<br>`s3express-control-dualstack.ap-northeast-1.amazonaws.com` | `s3express-apne1-az1.ap-northeast-1.amazonaws.com`<br>`s3express-apne1-az1.dualstack.ap-northeast-1.amazonaws.com`<br>`s3express-apne1-az4.ap-northeast-1.amazonaws.com`<br>`s3express-apne1-az4.dualstack.ap-northeast-1.amazonaws.com`                                                                                         |
| Europe (Ireland)      | `eu-west-1`      | `euw1-az1`<br>`euw1-az3`               | `s3express-control.eu-west-1.amazonaws.com`<br>`s3express-control-dualstack.eu-west-1.amazonaws.com`           | `s3express-euw1-az1.eu-west-1.amazonaws.com`<br>`s3express-euw1-az1.dualstack.eu-west-1.amazonaws.com`<br>`s3express-euw1-az3.eu-west-1.amazonaws.com`<br>`s3express-euw1-az3.dualstack.eu-west-1.amazonaws.com`                                                                                                                 |
| Europe (Stockholm)    | `eu-north-1`     | `eun1-az1`<br>`eun1-az2`<br>`eun1-az3` | `s3express-control.eu-north-1.amazonaws.com`<br>`s3express-control-dualstack.eu-north-1.amazonaws.com`         | `s3express-eun1-az1.eu-north-1.amazonaws.com`<br>`s3express-eun1-az1.dualstack.eu-north-1.amazonaws.com`<br>`s3express-eun1-az2.eu-north-1.amazonaws.com`<br>`s3express-eun1-az2.dualstack.eu-north-1.amazonaws.com`<br>`s3express-eun1-az3.eu-north-1.amazonaws.com`<br>`s3express-eun1-az3.dualstack.eu-north-1.amazonaws.com` |

## Configuring VPC gateway

endpoints

Use the following procedure to create a gateway endpoint that connects to
Amazon S3 Express One Zone storage class objects and directory buckets.

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
9. For **Policy**, choose **Full access** to
   allow all operations by all principals on all resources over the VPC endpoint.
   Otherwise, choose **Custom** to attach a VPC endpoint policy
   that controls the principals' permissions to perform actions on
   resources over the VPC endpoint.
10. For **IP address type**, choose from the following options:
    - **IPv4** – Assign IPv4 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have IPv4 address ranges and the service accepts IPv4 requests.
    - **IPv6** – Assign IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets are IPv6 only subnets and the service accepts IPv6 requests.
    - **Dualstack** – Assign both IPv4 and IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges and the service accepts both IPv4 and IPv6 requests.

11. (Optional) To add a tag, choose **Add new tag**, and enter
    the tag key and the tag value.
12. Choose **Create endpoint**.

After creating a gateway endpoint, you can use Regional API endpoints and Zonal API
endpoints to access Amazon S3 Express One Zone storage class objects and directory buckets.

To learn more about gateway VPC endpoints, see [Gateway endpoints](../../../vpc/latest/privatelink/gateway-endpoints.md "../../../vpc/latest/privatelink/gateway-endpoints.md") in the _AWS PrivateLink Guide_. For the data residency use cases, we recommend enabling access to your buckets only from your VPC using gateway VPC endpoints. When access is restricted to a VPC or a VPC endpoint, you can access the objects through the AWS Management Console, the REST API, AWS CLI, and AWS SDKs.

###### Note

To restrict access to a VPC or a VPC endpoint using the AWS Management Console, you must use the AWS Management Console Private Access. For more information, see [AWS Management Console Private Access](../../../awsconsolehelpdocs/latest/gsg/console-private-access.md "../../../awsconsolehelpdocs/latest/gsg/console-private-access.md") in the *AWS Management Console guide*AWS Management Console guide.
