# Create a network interface endpoint for Verified Access

Use the following procedure to create a network interface endpoint.

###### Requirements

- Only IPv4 traffic is supported.
- The network interface must belong to the same virtual private cloud (VPC) as the security
  groups.
- We use the private IP on the network interface to forward the traffic.
- Before you create a Verified Access endpoint, you must create a Verified Access group. For more information,
  see [Create a Verified Access group](create-verified-access-group.md#create-group "create-verified-access-group.md#create-group").
- You must provide a domain name for your application. This is the public DNS name your
  users will use to access your application. You will also need to provide a public SSL
  certificate with a CN that matches this domain name. You can create or import the certificate
  using AWS Certificate Manager.

###### To create a network interface endpoint using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access endpoints**.
3. Choose **Create Verified Access endpoint**.
4. (Optional) For **Name tag** and **Description**, enter
   a name and description for the endpoint.
5. For **Verified Access group**, choose a Verified Access group.
6. For **Endpoint details**, do the following:
   1. For **Protocol**, choose a protocol.
   2. For **Attachment type**, choose **VPC**.
   3. For **Endpoint type**, choose **Network interface**.
   4. (HTTP/HTTPS) For **Port**, enter the port number. (TCP) For
      **Port ranges**, enter a port range and choose **Add port**.
   5. For **Network interface**, choose a network interface.
   6. For **Security groups**, choose the security groups for the endpoint.
      These security groups control the inbound and outbound traffic for the Verified Access endpoint.
   7. For **Endpoint domain prefix**, enter a custom identifier to prepend
      to the DNS name that Verified Access generates for the endpoint.

7. (HTTP/HTTPS) For **Application details**, do the following:
   1. For **Application domain**, enter a DNS name for your application.
   2. Under **Domain certificate ARN**, choose a public TLS certificate.

8. (Optional) For **Policy definition**, enter a Verified Access policy for the
   endpoint.
9. (Optional) To add a tag, choose **Add new tag** and enter the
   tag key and the tag value.
10. Choose **Create Verified Access endpoint**.

###### To create a Verified Access endpoint using the AWS CLI

Use the [create-verified-access-endpoint](../../../cli/latest/reference/ec2/create-verified-access-endpoint.md "../../../cli/latest/reference/ec2/create-verified-access-endpoint.md") command.
