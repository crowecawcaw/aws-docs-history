# Amazon EC2 service quotas

When you create your AWS account, we set default _quotas_ (also
referred to as limits) on your AWS resources on a per-Region basis. If you attempt to
exceed the quota for a resource, the request fails. For example, there is a maximum number
of Amazon EC2 vCPUs that you can provision for On-Demand Instances in a Region. If you attempt to launch
an instance in a Region and this request would cause your usage to exceed this quota, the
request fails. If this happens, you can reduce your resource usage or request a quota
increase.

The Service Quotas console is a central location where you can view and manage
your quotas for AWS services, and request a quota increase for many of the resources that
you use. Use the quota information that we provide
to manage your AWS infrastructure. Plan to request any quota increases in advance of the
time that you'll need them.

###### Related quota documentation

- [Amazon EC2 endpoints and quotas](../../../general/latest/gr/ec2-service.md "../../../general/latest/gr/ec2-service.md")
- [Amazon EC2 instance type quotas](../../../ec2/latest/instancetypes/ec2-instance-quotas.md "../../../ec2/latest/instancetypes/ec2-instance-quotas.md")
- [Quotas for Amazon EBS](../../../ebs/latest/userguide/ebs-resource-quotas.md "../../../ebs/latest/userguide/ebs-resource-quotas.md")
- [Amazon VPC quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md")

## View your current quotas

You can view your quotas for each Region using the Service Quotas console.

###### To view your current quotas using the Service Quotas console

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/ "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/").
2. From the navigation bar (at the top of the screen), select a Region.
3. On the **Manage quotas** pane, select a service; for example,
   **Amazon Elastic Compute Cloud (Amazon EC2)**. Choose **View
   quotas**.
4. Use the filter field to filter the list by resource name. For example, enter
   `On-Demand` to locate the quotas for On-Demand Instances.
5. To view more information, choose the quota name to open the details page for the
   quota.

## Request an increase

You can request a quota increase for each Region.

###### To request an increase using the Service Quotas console

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/ "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/").
2. From the navigation bar (at the top of the screen), select a Region.
3. Use the filter field to filter the list by resource name. For example, enter
   `On-Demand` to locate the quotas for On-Demand Instances.
4. If the quota is adjustable, choose the quota and then choose **Request
   quota increase**.
5. For **Change quota value**, enter the new quota value.
6. Choose **Request**.
7. To view any pending or recently resolved requests in the console, choose
   **Dashboard** from the navigation pane. For pending requests,
   choose the status of the request to open the request receipt. The initial status of a
   request is **Pending**. After the status changes to **Quota
   requested**, you'll see the case number with Support. Choose the case
   number to open the ticket for your request.

For more information, including how to use the AWS CLI or SDKs to
request a quota increase, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## Restriction on email sent using port 25

By default, Amazon EC2 allows outbound traffic over port 25 only to private IPv4 addresses.
Traffic over port 25 is blocked to public IPv4 addresses and IPv6 addresses.

You can request that this restriction be removed. For more information, see
[How do I remove
the restriction on port 25 from my Amazon EC2 instance or Lambda function?](https://repost.aws/knowledge-center/ec2-port-25-throttle "https://repost.aws/knowledge-center/ec2-port-25-throttle")

This restriction does not apply to outbound traffic over port 25 destined for:

- IP addresses in the primary CIDR block of the VPC in which the originating
  network interface exists.
- IP addresses in the CIDRs defined in [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918 "https://datatracker.ietf.org/doc/html/rfc1918"), [RFC 6598](https://datatracker.ietf.org/doc/html/rfc6598 "https://datatracker.ietf.org/doc/html/rfc6598"), and
  [RFC
  4193](https://datatracker.ietf.org/doc/html/rfc4193 "https://datatracker.ietf.org/doc/html/rfc4193").
