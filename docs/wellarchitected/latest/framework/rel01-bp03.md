

# REL01-BP03 Accommodate fixed service quotas and constraints through architecture

 When a design assumes it can grow past a fixed quota or physical resource constraint, it fails at scale with no remediation path. Design around fixed quotas from the start so the workload performs under both normal and peak conditions. 

 **Desired outcome:** 
+  Your architecture operates within the fixed quotas and resource constraints of every service it uses. 
+  Your workload performs as expected under normal load and at projected peak load. 
+  You have identified, during design, the fixed quotas that could constrain the workload as it grows. 
+  Your observability alerts on usage that approaches a fixed quota before it constrains the workload. 

 **Common anti-patterns:** 
+  Teams choose a resource without realizing a fixed constraint will cause the design to fail as it scales. 
+  Teams benchmark against unrealistic conditions, such as sustaining a burst rate that is only allowed briefly. 
+  Teams select a design that cannot be modified when a fixed quota, such as a maximum message size, is reached. 
+  Teams build no observability for fixed quotas, so a workload nearing one gives no warning. 

 **Benefits of establishing this best practice:** 
+  The workload runs under all projected load levels without hitting a fixed quota. 
+  Design-time analysis catches unworkable choices while they are still cheap to change. 
+  Alerting on fixed quotas gives operators time to shift load or redesign before usage reaches the quota. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 An adjustable quota is a starting value you can raise through a request. A fixed quota is a boundary of the service, and no request, escalation, or severity level will move it. The [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) console marks a quota as fixed when its adjustable column reads no. Some fixed quotas are not listed there at all and appear only in a service's own documentation, so a design review that consults only one source will miss them. 

 Because you cannot negotiate a fixed quota, it is an architectural input, not an operational setting. Consider a function with a maximum runtime. If any code path might exceed that maximum, no amount of tuning changes the outcome. Restructure the work, split it, or move it to a service without that quota. Explore this input during design. Finding it after production deployment forces re-architecture, which is far more expensive than choosing a different pattern early. 

 A design with a fixed-quota risk can look healthy for a long time. For example, a message-queue payload quota, a burst rate permitted only for short intervals, or a cap on concurrent database connections may never come up in light testing. The workload crosses the quota only under real peak load or during a failover that concentrates traffic, so the failure appears in production. Evaluate fixed quotas with the same scrutiny as functional requirements. 

 Multi-Region patterns such as active/active and the active/passive variants concentrate usage during a failure, pushing a location toward quotas it never approached in steady state. To calculate the quota gap needed during failover, see [REL01-BP06 Verify that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel01-bp06.md). Reproduce that failover load with stress testing, load testing, and fault injection testing to reveal fixed-quota breaches in a controlled environment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **List the services in the candidate design:** During the design phase, enumerate every service the workload will use so each one can be checked for quotas before you commit to it. 

1.  **Record adjustable and fixed quotas for each service:** Capture both the adjustable quotas and the fixed constraints per service. Read fixed values from the [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) console and, where quotas are not exposed there, from the service documentation such as the [AWS Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) page. 

1.  **Let business and technology drivers shape the choice:** Weigh business outcomes, use case, dependent systems, availability targets, and disaster recovery objectives against the fixed quotas you recorded. Choose the design that meets these drivers without depending on a quota you cannot raise. 

1.  **Analyze usage across accounts and Regions:** Determine whether each fixed quota is scoped per Region or per account, and map projected usage against it in every location the workload runs. 

1.  **Model resilience scenarios against fixed quotas:** For zonal and Regional failure cases in active/active and active/passive designs, calculate the concentrated usage a failover creates and confirm no fixed quota is breached under that load. 

1.  **Validate with stress, load, and fault injection testing:** In a test environment, drive the workload toward its fixed quotas with stress, load, and resilience testing so any breach appears under controlled conditions rather than in production. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL01-BP01 Aware of service quotas and constraints](rel01-bp01.md) 
+  [REL01-BP06 Verify that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel01-bp06.md) 
+  [REL01-BP04 Monitor and manage quotas](rel01-bp04.md) 
+  [REL12-BP04 Test resilience using chaos engineering](rel12-bp04.md) 

 **Related documents:** 
+  [Availability and recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-availability-and-recovery-objectives.html) 
+  [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) 
+  [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) 
+  [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) 
+  [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) 
+  [Amazon EC2 service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) 
+  [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/) 
+  [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) 
+  [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) 
+  [Availability with redundancy](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-redundancy.html) 
+  [Managing and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/) 

 **Related videos:** 
+  [How do I manage my service quotas for my AWS services?](https://www.youtube.com/watch?v=Ddf5WG5I0Qo) 

 **Related tools:** 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Cloud Development Kit (AWS CDK) (AWS CDK)](https://aws.amazon.com/cdk/) 