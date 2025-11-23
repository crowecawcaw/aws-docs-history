# Gateway endpoints for Amazon S3

You can access Amazon S3 from your VPC using gateway VPC endpoints. After you create the
gateway endpoint, you can add it as a target in your route table for traffic
destined from your VPC to Amazon S3.

There is no additional charge for using gateway endpoints.

Amazon S3 supports both gateway endpoints and interface endpoints. With a gateway endpoint,
you can access Amazon S3 from your VPC, without requiring an internet gateway or NAT device for
your VPC, and with no additional cost. However, gateway endpoints do not allow access from
on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway.
For those scenarios, you must use an interface endpoint, which is available for an additional
cost. For more information, see [Types of VPC endpoints for Amazon S3](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md#types-of-vpc-endpoints-for-s3 "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md#types-of-vpc-endpoints-for-s3") in the _Amazon S3 User Guide_.

###### Contents

- [Considerations](#gateway-endpoint-considerations-s3 "#gateway-endpoint-considerations-s3")
- [Private DNS](#private-dns-s3 "#private-dns-s3")
- [Create a gateway endpoint](#create-gateway-endpoint-s3 "#create-gateway-endpoint-s3")
- [Control access using bucket policies](#bucket-policies-s3 "#bucket-policies-s3")
- [Associate route tables](#associate-route-tables-s3 "#associate-route-tables-s3")
- [Edit the VPC endpoint policy](#edit-vpc-endpoint-policy-s3 "#edit-vpc-endpoint-policy-s3")
- [Delete a gateway endpoint](#delete-gateway-endpoint-s3 "#delete-gateway-endpoint-s3")

## Considerations

- A gateway endpoint is available only in the Region where you created it. Be sure
  to create your gateway endpoint in the same Region as your S3 buckets.
- If you're using the Amazon DNS servers, you must enable both [DNS hostnames and DNS resolution](../userguide/vpc-dns.md#vpc-dns-updating "../userguide/vpc-dns.md#vpc-dns-updating")
  for your VPC. If you're using your own DNS server, ensure that requests to Amazon S3
  resolve correctly to the IP addresses maintained by AWS.
- The rules for the security groups for your instances that access Amazon S3 through a
  gateway endpoint must allow traffic to and from Amazon S3. You can reference the ID of the
  [prefix list](../userguide/working-with-aws-managed-prefix-lists.md "../userguide/working-with-aws-managed-prefix-lists.md")
  for Amazon S3 in security group rules.
- The network ACL for the subnet for your instances that access Amazon S3 through a gateway
  endpoint must allow traffic to and from Amazon S3. You can't reference prefix lists in
  network ACL rules, but you can get the IP address range for Amazon S3 from the [prefix list](../userguide/working-with-aws-managed-prefix-lists.md "../userguide/working-with-aws-managed-prefix-lists.md") for
  Amazon S3.
- Check whether you are using an AWS service that requires access to an S3 bucket.
  For example, a service might require access to buckets that contain log files, or might
  require you to download drivers or agents to your EC2 instances. If so, ensure that your
  endpoint policy allows the AWS service or resource to access these buckets using the
  `s3:GetObject` action.
- You can't use the `aws:SourceIp` condition in an identity policy or
  a bucket policy for requests to Amazon S3 that traverse a VPC endpoint. Instead, use the
  `aws:VpcSourceIp` condition. Alternatively, you can use route tables to
  control which EC2 instances can access Amazon S3 through the VPC endpoint.
- The source IPv4 or IPv6 addresses from instances in your affected subnets as received by
  Amazon S3 change from public addresses to the private addresses in your VPC. An
  endpoint switches network routes, and disconnects open TCP connections. The previous
  connections that used public addresses are not resumed. We recommend that you
  do not have any critical tasks running when you create or modify an endpoint; or
  that you test to ensure that your software can automatically reconnect to Amazon S3 after
  the connection break.
- Endpoint connections cannot be extended out of a VPC. Resources on the other side of a
  VPN connection, VPC peering connection, transit gateway, or Direct Connect connection in your
  VPC cannot use a gateway endpoint to communicate with Amazon S3.
- Your account has a default quota of 20 gateway endpoints per Region, which is adjustable.
  There is also a limit of 255 gateway endpoints per VPC.

## Private DNS

You can configure private DNS to optimize costs when you create both a gateway endpoint
and an interface endpoint for Amazon S3.

###### Route 53 Resolver

Amazon provides a DNS server, called the [Route 53 Resolver](../../../Route53/latest/DeveloperGuide/resolver.md "../../../Route53/latest/DeveloperGuide/resolver.md"), for your VPC. The
Route 53 Resolver automatically resolves local VPC domain names and records in private hosted zones.
However, you can't use the Route 53 Resolver from outside your VPC. Route 53 provides Resolver endpoints
and Resolver rules so that you can use the Route 53 Resolver from outside your VPC. An
_inbound Resolver endpoint_ forwards DNS queries from the on-premises
network to Route 53 Resolver. An _outbound Resolver endpoint_ forwards DNS queries
from the Route 53 Resolver to the on-premises network.

When you configure your interface endpoint for Amazon S3 to use private DNS only for the
inbound Resolver endpoint, we create an inbound Resolver endpoint. The inbound Resolver
endpoint resolves DNS queries to Amazon S3 from on-premises to the private IP addresses of the
interface endpoint. We also add ALIAS records for the Route 53 Resolver to the public hosted zone for
Amazon S3, so that DNS queries from your VPC resolve to the Amazon S3 public IP addresses, which
routes traffic to the gateway endpoint.

###### Private DNS

If you configure private DNS for your interface endpoint for Amazon S3 but do not configure
private DNS only for the inbound Resolver endpoint, requests from both your on-premises
network and your VPC use the interface endpoint to access Amazon S3. Therefore, you pay to use
the interface endpoint for traffic from the VPC, instead of using the gateway endpoint for
no additional charge.

![Amazon S3 request routing with both endpoint types.](images/s3-private-dns-default.png)

###### Private DNS only for the inbound Resolver endpoint

If you configure private DNS only for the inbound Resolver endpoint, requests from
your on-premises network use the interface endpoint to access Amazon S3, and requests from your
VPC use the gateway endpoint to access Amazon S3. Therefore, you optimize your costs, because
you pay to use the interface endpoint only for traffic that can't use the gateway
endpoint.

In order to configure this, the DNS record IP type of the gateway endpoint must match the interface endpoint
or be `service-defined`. AWS PrivateLink doesn't support any other combination.
For more information, see [DNS record IP type](gateway-endpoints.md#gateway-endpoint-dns-record-ip-type "gateway-endpoints.md#gateway-endpoint-dns-record-ip-type").

![Amazon S3 request routing with private DNS and an inbound Resolver endpoint.](images/s3-private-dns-inbound-endpoint.png)

###### Configure private DNS

You can configure private DNS for an interface endpoint for Amazon S3 when you create
it or after you create it. For more information, see [Create a VPC endpoint](create-interface-endpoint.md#create-interface-endpoint-aws "create-interface-endpoint.md#create-interface-endpoint-aws") (configure during creation) or [Enable private DNS names](interface-endpoints.md#enable-private-dns-names "interface-endpoints.md#enable-private-dns-names") (configure after creation).

## Create a gateway endpoint

Use the following procedure to create a gateway endpoint that connects to Amazon S3.

###### To create a gateway endpoint using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. For **Service category**, choose **AWS services**.
5. For **Services**, add the filter **Type = Gateway**.

If your Amazon S3 data is stored in general purpose buckets, select **com.amazonaws.**`region`**.s3**.

If your Amazon S3 data is stored in directory buckets, select **com.amazonaws.**`region`**.s3express**. 6. For **VPC**, select the VPC in which to create the
endpoint. 7. For **IP address type**, choose from the following options:

    * **IPv4** – Assign IPv4 addresses to the endpoint network
     interfaces. This option is supported only if all selected subnets have IPv4 address
     ranges and the service accepts IPv4 requests.
    * **IPv6** – Assign IPv6 addresses to the endpoint network
     interfaces. This option is supported only if all selected subnets are IPv6 only
     subnets and the service accepts IPv6 requests.
    * **Dualstack** – Assign both IPv4 and IPv6 addresses to
     the endpoint network interfaces. This option is supported only if all selected
     subnets have both IPv4 and IPv6 address ranges and the service accepts both IPv4 and
     IPv6 requests.

8. For **Route tables**, select the route tables to be used
   by the endpoint. We automatically add a route that points traffic destined for
   the service to the endpoint network interface.
9. For **Policy**, select **Full access** to allow
   all operations by all principals on all resources over the VPC endpoint. Otherwise, select
   **Custom** to attach a VPC endpoint policy that controls the permissions
   that principals have to perform actions on resources over the VPC endpoint.
10. (Optional) To add a tag, choose **Add new tag** and enter the tag
    key and the tag value.
11. Choose **Create endpoint**.

###### To create a gateway endpoint using the command line

- [create-vpc-endpoint](../../../cli/latest/reference/ec2/create-vpc-endpoint.md "../../../cli/latest/reference/ec2/create-vpc-endpoint.md") (AWS CLI)
- [New-EC2VpcEndpoint](../../../powershell/latest/reference/items/New-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/New-EC2VpcEndpoint.md") (Tools for Windows PowerShell)

## Control access using bucket policies

You can use bucket policies to control access to buckets from specific endpoints, VPCs,
IP address ranges, and AWS accounts. These examples assume that there are also policy
statements that allow the access required for your use cases.

###### Example: Restrict access to a specific endpoint

You can create a bucket policy that restricts access to a specific endpoint by using
the [aws:sourceVpce](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpce "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpce") condition key. The following policy denies access to the
specified bucket using the specified actions unless the specified gateway endpoint
is used. Note that this policy blocks access to the specified bucket using the
specified actions through the AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow-access-to-specific-VPCE",
 "Effect": "Deny",
 "Principal": "*",
 "Action": ["s3:PutObject", "s3:GetObject", "s3:DeleteObject"],
 "Resource": ["arn:aws:s3:::`bucket_name`",
 "arn:aws:s3:::`bucket_name`/*"],
 "Condition": {
 "StringNotEquals": {
 "aws:sourceVpce": "`vpce-1a2b3c4d`"
 }
 }
 }
 ]
}`

```

###### Example: Restrict access to a specific VPC

You can create a bucket policy that restricts access to specific VPCs by using the
[aws:sourceVpc](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc") condition key. This is useful if you have multiple endpoints
configured in the same VPC. The following policy denies access to the specified bucket
using the specified actions unless the request comes from the specified VPC. Note that
this policy blocks access to the specified bucket using the specified actions through
the AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow-access-to-specific-VPC",
 "Effect": "Deny",
 "Principal": "*",
 "Action": ["s3:PutObject", "s3:GetObject", "s3:DeleteObject"],
 "Resource": ["arn:aws:s3:::`example_bucket`",
 "arn:aws:s3:::`example_bucket`/*"],
 "Condition": {
 "StringNotEquals": {
 "aws:sourceVpc": "`vpc-111bbb22`"
 }
 }
 }
 ]
}`

```

###### Example: Restrict access to a specific IP address range

You can create a policy that restricts access to specific IP address ranges by using
the [aws:VpcSourceIp](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-vpcsourceip "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-vpcsourceip") condition key. The following policy denies access to the
specified bucket using the specified actions unless the request comes from the specified
IP address. Note that this policy blocks access to the specified bucket using the specified
actions through the AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow-access-to-specific-VPC-CIDR",
 "Effect": "Deny",
 "Principal": "*",
 "Action": ["s3:PutObject", "s3:GetObject", "s3:DeleteObject"],
 "Resource": ["arn:aws:s3:::`bucket_name`",
 "arn:aws:s3:::`bucket_name`/*"],
 "Condition": {
 "NotIpAddress": {
 "aws:VpcSourceIp": "`172.31.0.0/16`"
 }
 }
 }
 ]
}`

```

###### Example: Restrict access to buckets in a specific AWS account

You can create a policy that restricts access to the S3 buckets in a specific
AWS account by using the `s3:ResourceAccount` condition key. The
following policy denies access to S3 buckets using the specified actions unless
they are owned by the specified AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow-access-to-bucket-in-specific-account",
 "Effect": "Deny",
 "Principal": "*",
 "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
 "Resource": "arn:aws:s3:::*",
 "Condition": {
 "StringNotEquals": {
 "s3:ResourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

## Associate route tables

You can change the route tables that are associated with the gateway endpoint.
When you associate a route table, we automatically add a route that points traffic
destined for the service to the endpoint network interface. When you disassociate
a route table, we automatically remove the endpoint route from the route table.

###### To associate route tables using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Select the gateway endpoint.
4. Choose **Actions**, **Manage route tables**.
5. Select or deselect route tables as needed.
6. Choose **Modify route tables**.

###### To associate route tables using the command line

- [modify-vpc-endpoint](../../../cli/latest/reference/ec2/modify-vpc-endpoint.md "../../../cli/latest/reference/ec2/modify-vpc-endpoint.md") (AWS CLI)
- [Edit-EC2VpcEndpoint](../../../powershell/latest/reference/items/Edit-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/Edit-EC2VpcEndpoint.md") (Tools for Windows PowerShell)

## Edit the VPC endpoint policy

You can edit the endpoint policy for a gateway endpoint, which controls access to Amazon S3
from the VPC through the endpoint. After you update an endpoint policy, it can take a few
minutes for the changes to take effect. The default policy allows full access. For more
information, see [Endpoint policies](vpc-endpoints-access.md "vpc-endpoints-access.md").

###### To change the endpoint policy using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Select the gateway endpoint.
4. Choose **Actions**, **Manage policy**.
5. Choose **Full Access** to allow full access to the service, or
   choose **Custom** and attach a custom policy.
6. Choose **Save**.

The following are example endpoint policies for accessing Amazon S3.

###### Example: Restrict access to a specific bucket

You can create a policy that restricts access to specific S3 buckets only. This is
useful if you have other AWS services in your VPC that use S3 buckets.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow-access-to-specific-bucket",
 "Effect": "Allow",
 "Principal": "*",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket_name`",
 "arn:aws:s3:::`bucket_name`/*"
 ]
 }
 ]
}`

```

###### Example: Restrict access to a specific IAM role

You can create a policy that restricts access to a specific IAM role. You must use
`aws:PrincipalArn` to grant access to a principal.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow-access-to-specific-IAM-role",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "ArnEquals": {
 "aws:PrincipalArn": "arn:aws:iam::`111122223333`:role/`role_name`"
 }
 }
 }
 ]
}`

```

###### Example: Restrict access to users in a specific account

You can create a policy that restricts access to a specific account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow-callers-from-specific-account",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

## Delete a gateway endpoint

When you are finished with a gateway endpoint, you can delete it. When you delete a
gateway endpoint, we remove the endpoint route from the subnet route tables.

You can't delete a gateway endpoint if private DNS is enabled.

###### To delete a gateway endpoint using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Select the gateway endpoint.
4. Choose **Actions**, **Delete VPC endpoints**.
5. When prompted for confirmation, enter `delete`.
6. Choose **Delete**.

###### To delete a gateway endpoint using the command line

- [delete-vpc-endpoints](../../../cli/latest/reference/ec2/delete-vpc-endpoints.md "../../../cli/latest/reference/ec2/delete-vpc-endpoints.md") (AWS CLI)
- [Remove-EC2VpcEndpoint](../../../powershell/latest/reference/items/Remove-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/Remove-EC2VpcEndpoint.md") (Tools for Windows PowerShell)
