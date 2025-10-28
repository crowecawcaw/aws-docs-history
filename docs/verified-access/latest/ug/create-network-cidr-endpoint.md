# Create a network CIDR endpoint for Verified Access

Use the following procedure to create a network CIDR endpoint. For example, you can use a network CIDR
endpoint to enable access to EC2 instances in a specific subnet over port 22 (SSH).

###### Requirements

- Only the TCP protocol is supported.
- Verified Access provides a DNS record for each IP address in the CIDR range that is used by a resource.
  If you delete a resource, it's IP address is no longer in use and Verified Access deletes the corresponding
  DNS record.
- If you specify a custom subdomain, Verified Access provides a DNS record for each IP address in the
  endpoint subnets that is in the specified CIDR range and used in the subdomain, and provides
  you with the IP addresses of its DNS servers. You can configure a forwarding rule for your
  subdomain to point to the Verified Access DNS servers. Any request made to a record in the domain is
  resolved by the Verified Access DNS servers to the IP address of the requested resource.
- Before you create a Verified Access endpoint, you must create a Verified Access group. For more information,
  see [Create a Verified Access group](create-verified-access-group.md#create-group "create-verified-access-group.md#create-group").
- Create the endpoint and then connect to the application using the [Connectivity Client](connectivity-client.md "connectivity-client.md").

###### To create a network CIDR endpoint using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access endpoints**.
3. Choose **Create Verified Access endpoint**.
4. (Optional) For **Name tag** and **Description**, enter
   a name and description for the endpoint.
5. For **Verified Access group**, choose a Verified Access group for the endpoint.
6. For **Endpoint details**, do the following:
   1. For **Protocol**, choose **TCP**.
   2. For **Attachment type**, choose **VPC**.
   3. For **Endpoint type**, choose **Network CIDR**.
   4. For **Port ranges**, enter a port range and choose **Add port**.
   5. For **Subnet**, choose the subnets.
   6. For **Security groups**, choose the security groups for the endpoint.
      These security groups control the inbound and outbound traffic for the Verified Access endpoint.
   7. (Optional) For **Endpoint domain prefix**, enter a custom identifier to prepend
      to the DNS name that Verified Access generates for the endpoint.

7. (Optional) For **Policy definition**, enter a Verified Access policy for the
   endpoint.
8. (Optional) To add a tag, choose **Add new tag** and enter the
   tag key and the tag value.
9. Choose **Create Verified Access endpoint**.

###### To create a Verified Access endpoint using the AWS CLI

Use the [create-verified-access-endpoint](../../../cli/latest/reference/ec2/create-verified-access-endpoint.md "../../../cli/latest/reference/ec2/create-verified-access-endpoint.md") command.
