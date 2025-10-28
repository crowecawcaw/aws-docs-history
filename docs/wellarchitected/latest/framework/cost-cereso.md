# Cost-effective resources

Using the appropriate instances and resources for your workload is
key to cost savings. For example, a reporting process might take
five hours to run on a smaller server but one hour to run on a
larger server that is twice as expensive. Both servers give you
the same outcome, but the smaller server incurs more cost over
time.

A well-architected workload uses the most cost-effective
resources, which can have a significant and positive economic
impact. You also have the opportunity to use managed services to
reduce costs. For example, rather than maintaining servers to
deliver email, you can use a service that charges on a per-message
basis.

AWS offers a variety of flexible and cost-effective pricing
options to acquire instances from Amazon EC2 and other services in
a way that more effectively fits your needs. _On-Demand_
_Instances_ permit you to pay for compute
capacity by the hour, with no minimum commitments required.
_Savings Plans and Reserved Instances_ offer
savings of up to 75% oﬀ On-Demand pricing. With Spot Instances,
you can leverage unused Amazon EC2 capacity and offer savings of
up to 90% oﬀ On-Demand pricing. _Spot
Instances_ are appropriate where the system can tolerate
using a fleet of servers where individual servers can come and go
dynamically, such as stateless web servers, batch processing, or
when using HPC and big data.

Appropriate service selection can also reduce usage and costs;
such as CloudFront to minimize data transfer, or decrease costs, such as utilizing Amazon Aurora on Amazon RDS to
remove expensive database licensing costs.

The following questions focus on these considerations for cost
optimization.

| COST 5:  How do you evaluate cost when you select services?                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon EC2, Amazon EBS, and Amazon S3 are building-block AWS services. Managed services, such as Amazon RDS and Amazon DynamoDB, are higher level, or application level, AWS services. By selecting the appropriate building blocks and managed services, you can optimize this workload for cost. For example, using managed services, you can reduce or remove much of your administrative and operational overhead, freeing you to work on applications and business-related activities. |
| COST 6:  How do you meet cost targets when you select resource type, size and number?                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Verify that you choose the appropriate resource size and number of resources for the task at hand. You minimize waste by selecting the most cost effective type, size, and number.                                                                                                                                                                                                                                                                                                          |
| COST 7:  How do you use pricing models to reduce cost?                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Use the pricing model that is most appropriate for your resources to minimize expense.                                                                                                                                                                                                                                                                                                                                                                                                      |
| COST 8:  How do you plan for data transfer charges?                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Verify that you plan and monitor data transfer charges so that you can make architectural decisions to minimize costs. A small yet effective architectural change can drastically reduce your operational costs over time.                                                                                                                                                                                                                                                                  | By factoring in cost during service selection, and using tools such as Cost Explorer and AWS Trusted Advisor to regularly review your AWS usage, you can actively monitor your utilization and adjust your deployments accordingly. |
