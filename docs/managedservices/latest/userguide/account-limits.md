# AMS account limits

There are three distinct types of limits to consider within AMS multi-account landing zone: AMS API limits, AMS
resource limits, and AWS limits.

There are two distinct types of limits to consider within AMS single-account landing zone: AMS API limits, and
AWS limits.

## AMS account API limits

This section describes the account level limits after which AWS Managed Services (AMS) throttles the AMS SKMS API service. This means,
if you call any of the listed APIs more than 10 times in a second,
one of the calls is "throttled" (you receive a `ThrottleException`). Under rare situations, an external or downstream dependency
might throttle the AMS API and then AMS may throttle your API calls at a possibly lower rate.

###### Note

For information on the AMS SKMS API, download the reference through the **Reports** tab of the AWS Artifact console.

For each AMS SKMS API listed, the operation is throttled after 10 TPS (transactions per second):

- `GetStack`
- `GetSubnet`
- `GetVpc`
- `ListAmis`
- `ListStackSummaries`
- `ListSubnetSummaries`
- `ListVpcSummaries`

## AMS multi-account landing zone account resource limits

Account resource limits relate to AMS multi-account landing zone application accounts and VPCs and subnets.

### Application account resource limits

There is a soft limit of 50 application accounts per organization. If you have a use case for more than 50 application accounts, contact your cloud
service delivery manager (CSDM) to relay your requirements.

### VPCs and subnets resource limits

There is a soft limit of 10 VPCs per application account within the pre-defined AWS Region for the organization.

Each VPC may have 1 to 10 private subnet tiers spanned across 2 to 3 availability zones. Additionally,
each VPC may have 0 to 5 public subnet tiers spanned across 2 to 3 availability zones.
If you have requirements beyond these limits, inform your CSDM or Cloud Architect to review your use case.

### AMS multi-account landing zone application to account ratio

One account per application is supported in AMS multi-account landing zone; however, each Application account has a small cost, and you are charged for the
number of connections to the Transit Gateway per hour, and the amount of traffic that flows through AWS Transit Gateway.
So, the more segregated applications are into accounts or VPCs, the higher the costs.

To reduce costs and still ensure an appropriate segregation of duties, AMS recommends that you

1.  group applications by teams with tightly coupled business processes, and
2.  do not mix applications that are in different stages (prod vs. non-prod) or managed by different teams.
    In this way, you will have fewer accounts, access management and the segregation of duties will be easier, and traffic cost could be mitigated.

For example: An enterprise has in production a Trading application and a Portfolio Management application, both applications are managed by
the Investments IT team and exchange a lot of traffic with each other. In this scenario the company can benefit from grouping both applications
in the same account and same the VPC, because the Investments IT team won’t have to request access to multiple Application accounts and the
company will save on traffic costs. In this case, the company should create another account for the same applications in development stage and provide access to
the development team.

In another scenario, the enterprise has in production a Payroll application and an Accounting
application, managed by the Human Resources IT and Accounting IT teams respectively. Although
the Payroll application has to exchange information with the Accounting application, we recommend
segregating both applications in different accounts, one per team, and establishing a connection
between both application’s VPCs using the Networking account. In this way, the company will
prevent HR IT team request changes affecting the accounting application infrastructure,
of which they would have no knowledge.

Tips on how to group accounts into organizational units (OUs). An OU is logical grouping mechanism that
enables you to categorize (group) accounts and apply policies and configurations to based on those groups.
The recommended approach for creating OUs is to base them on policies that need to be applied to
a specific group of accounts, not on the internal hierarchy of teams within your reporting structure.
An OU is not equivalent to an Active Directory’s OU, and attempting to replicate the AD OU structure
in AWS Organizations is discouraged and results in a difficult to maintain and/or operate structure.

## AWS account limits

AWS account limits apply to your AWS Managed Services (AMS) accounts. The easiest method to determine default and current limits for AWS services is by leveraging
[AWS Service Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").
AMS recommends right-sizing individual service limits to the appropriate size to run the service(s) in the account.
Limits act like guard-rails to protect your accounts for security and cost runaways. If you would like to
raise a specific limit, submit a service request with AMS, and AMS Operations will raise the limit on
your behalf. For example, the default limit (or quota) for RDS instances is 40; if your workload requires 50
RDS instances, raise a service request for AMS Operations to raise the limit to your needed value.
