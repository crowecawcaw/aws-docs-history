# Best Practice 17.6 – Evaluate cost

benefits and impact of shared services and solutions

Where the same function is required by multiple SAP systems, it can be a
cost-effective option to centralize the management and costs by using existing solutions,
sharing components, or both. Monitoring, backups, and connectivity are common functions
that can be managed either within an AWS account boundary or in a dedicated account.
Standardization, reducing duplication, and reducing complexity reduces cost.

Find appropriate ways to share resources for cost reduction while still maintaining
appropriate isolation and without introducing dependencies that might impact
operations.

**Suggestion 17.6.1 – Evaluate the cost benefit of a 1-to-1 versus a
1-to-many setup for each shared service**

A standard pattern for SAP landscapes is to isolate non-production and production
workloads in separate accounts as part of a multi-account strategy. This can be a logical
boundary for some services. Consider complexity and operational costs for each scenario
including management boundaries which enforce segmentation, and any data transfer cost
impact across Regions, AZs, VPCs, or accounts.

In a multi-account design, some AWS services can be hosted centrally and accessed
by several applications and accounts in a hub and spoke design to save cost. Such services
include:

- Dedicated VPC with NAT gateway for all outbound traffic from spoke VPCs
- Centralized model for load balancers and Web Dispatchers
- Shared Amazon EFS or Amazon FSx for transports and other file sharing needs

**Suggestion 17.6.2 – Evaluate where reuse of existing services can
reduce costs**

This suggestion applies across a number of levels:

- Where AWS provides services, these often minimize overhead and work with
  consumption-based pricing. Some examples include Amazon EFS, AWS Backint Agent for SAP
  HANA, and AWS Backup.
- Your business might have an enterprise-wide standard for some functions (for
  example, enterprise backup) which should be used for operational consistency and
  economies of scale.
- AWS Partner solutions might be available through the AWS Marketplace or BYOL (bring your own
  license) based on your specific business requirements.
- License-included AWS Marketplace machine images might help reduce upfront costs. Licensing
  restrictions should be considered in this scenario as they could impact solution
  flexibility by restricting portability to different instance types.

**Suggestion 17.6.3 – Understand the impacts of using build vs. buy
vs. open source approaches**

Whether this is AWS or APN partner solution, there are varying degrees of build it
yourself vs. open source vs. off the shelf product. Examples include backup solutions,
high availability (HA) solutions, and shared storage solutions.

When considering a build-it-yourself approach or the use of an open source solution,
you should consider the following:

- Service level agreements
- Required skills to build and maintain
- Business impact of a service outage
  You should also evaluate the available commercial models for any solutions you intend
  to buy based on your specific business requirements and functionality each solution
  provides. Consider the terms of any commercial model, for example, the right to use vs.
  pay per use charges and how any such charges are calculated.
