

# REL01-BP01 Aware of service quotas and constraints

 Cloud services set quotas on how many resources you can provision and how fast you can call operations. Some quotas you can raise on request. Others are fixed by the resource itself and cannot change. To plan capacity, track which quotas apply to your workload and how close your usage runs to each quota. 

 **Desired outcome:** 
+  You have an inventory of the adjustable quotas and fixed constraints that apply to every service your workload uses, recorded per account and per Region. 
+  Your usage is tracked against each quota, and alerts reach the right team before consumption approaches the quota. 
+  You have a documented process for requesting quota increases, including the typical lead time for each request. 
+  Your teams distinguish an adjustable quota from a fixed constraint and make design decisions accordingly. 

 **Common anti-patterns:** 
+  Teams deploy a workload without knowing the adjustable quotas or fixed constraints of the services it uses. 
+  Teams assume that quotas increase automatically, or that an increase is granted the moment it is requested. 
+  Teams treat the default quota as identical across every service, Region, and account. 
+  Teams assume a fixed constraint can be exceeded and the service will scale past it. 
+  Teams skip testing at peak traffic, so service quotas first surface in production. 
+  Teams overprovision by selecting resource types far larger than actual demand or expected peaks. 

 **Benefits of establishing this best practice:** 
+  Tracking quota usage across accounts and Regions surfaces exhaustion risk before it degrades the workload. 
+  Identifying fixed constraints early prevents design choices that cannot scale later. 
+  A known request process and lead time let you raise quotas ahead of demand as part of routine capacity planning. 
+  Sizing resources against real requirements avoids the cost and operational overhead of overprovisioning. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Two kinds of quotas govern how much of a service you can consume. A *service quota* is a value AWS assigns to your account, such as the number of instances you can run in a Region. A *service constraint* is a quota built into a resource type, such as the maximum size of a message or the maximum runtime of a function. You manage quotas through requests and monitoring and accommodate constraints through architecture. 

 An *adjustable* (soft) quota can be raised by submitting a request, subject to review and approval. A *fixed* (hard) quota cannot be changed under any circumstances, including emergency events. The [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) console marks each quota as adjustable or not. A design that treats a fixed quota as adjustable has no path forward when usage hits the limit. 

 Most quotas are specific to a Region, and the same named quota can hold a different value in each Region. A quota set to a high value where you run production traffic today may sit at its low default in the Region you plan to fail over to. A smaller set of quotas are global. Because quotas are tracked per account, a workload that spans several accounts carries a separate set of quota values in each one. 

 Quotas act as guardrails that stop a misconfiguration or a runaway process from provisioning more capacity than you intended, and they cap request rates to protect shared services from abuse. Quotas can also block legitimate growth. A quota that was generous at launch becomes a bottleneck during a scaling event, and an Auto Scaling group that tries to add instances past the quota may fail to grow when you need it. 

 AWS enforces quotas across roughly 250 services, with thousands of quota names in a single Region, which makes manual tracking impossible. [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) gives you one place to look up values and request increases across services. [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) reports usage against quotas for a subset of services and flags those approaching their limit. To discover which services and resources your workload uses, [AWS Config](https://aws.amazon.com/config/) and AWS CloudFormation stack data can enumerate deployed resources, and you can use the AWS CLI and SDKs to read quota values programmatically. Some limits exist outside Service Quotas entirely, such as rate limits configured in an API usage plan or storage and throughput limits set on individual volumes, so a complete inventory has to look in more than one place. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Review the quota landscape:** Read the [AWS service quotas reference](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) to understand how quotas are structured, scoped, and requested. Note which quotas apply per Region and which are global. 

1.  **Inventory the services your workload uses:** Enumerate deployed resources with [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html) and [AWS CloudFormation stack resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.html), and cross-check against your deployment code. Do this for every account and Region the workload runs in. 

1.  **Identify the applicable quotas and constraints:** For each service, record its adjustable quotas and fixed constraints. Read values programmatically from [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) and [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), and check service documentation for quotas that are not exposed in the Service Quotas console. 

1.  **Establish monitoring and alerting:** Configure automated checks that alert you when usage approaches a quota or a resource constraint. Set thresholds that are meaningful for each resource so alerts arrive with time to act. 

1.  **Detect quota values that differ across Regions:** Add an automated check that compares each quota across the Regions and accounts your workload uses, and reports differences for reconciliation. 

1.  **Scan logs and metrics for constraint indicators:** Automate the review of application logs and metrics for quota or constraint errors, and route any matches to your monitoring system as alerts. 

1.  **Build a request and approval workflow:** Define how your organization calculates a required quota change and submits it, including an exception path for a denied or partial approval. Account for the lead time an increase request can take. 

1.  **Review quotas before adopting new services:** Before you use a new service in production, evaluate its quotas and constraints in a test or load-testing account to minimize potential impact in production. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL01-BP03 Accommodate fixed service quotas and constraints through architecture](rel01-bp03.md) 
+  [REL01-BP02 Manage service quotas across accounts and regions](rel01-bp02.md) 
+  [REL01-BP04 Monitor and manage quotas](rel01-bp04.md) 
+  [REL01-BP06 Verify that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel01-bp06.md) 

 **Related documents:** 
+  [Availability and recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-availability-and-recovery-objectives.html) 
+  [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) 
+  [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) 
+  [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) 
+  [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) 
+  [Amazon EC2 service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) 
+  [Service limits](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html) 
+  [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) 
+  [Availability with redundancy](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-redundancy.html) 
+  [Managing and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/) 
+  [View AWS Trusted Advisor recommendations at scale with AWS Organizations](https://aws.amazon.com/blogs/mt/organizational-view-for-trusted-advisor/) 
+  [Automating Service Limit Increases and Enterprise Support with AWS Control Tower](https://aws.amazon.com/blogs/mt/automating-service-limit-increases-enterprise-support-aws-control-tower/) 

 **Related videos:** 
+  [How do I manage my service quotas for my AWS services?](https://www.youtube.com/watch?v=Ddf5WG5I0Qo) 

 **Related tools:** 
+  [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/quota-monitor/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Cloud Development Kit (AWS CDK) (AWS CDK)](https://aws.amazon.com/cdk/) 