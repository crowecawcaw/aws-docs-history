# Best Practice 17.3 – Understand

business requirements to make cost-optimized design decisions per environment

Optimize the cost of each system or environment individually based on its differing
characteristics. Consider capacity, performance, reliability and operating hours to match
business requirements. For environments or applications that are less critical for the
experience of end users or business processes, minimize storage, compute, and operating
hours to reduce cost. Balance the cost savings of a reduced configuration with operational
requirements for testing or support.

**Suggestion 17.3.1 – Evaluate if non-production environments need a
full copy of production data**

Having full copies of production data in non-production will greatly impact your
storage and compute costs. Consider minimizing the number of copies of production data
while still meeting your testing requirements. Options to minimize costs of non-production
environment data storage include:

- Using less storage capacity for development and test systems.
- Using data slicing tools to carve out a smaller subset of test data in
  non-production systems.
- Consider the use of temporary production copies. These copies can be created
  on-demand and then quickly decommissioned, or archived, after the business need or
  test has passed.
- Evaluate if the SAP recommendation for SAP HANA databases of 50% working memory is
  required in non-production systems.

**Suggestion 17.3.2 – Evaluate if non-production environments always
need to have the same performance as production**

Non-production systems and some support systems are likely to have a smaller set of
users, handle significantly lower transaction volumes, or have flexible response time
requirements. Consider the following:

- Reducing the SAP Application Performance Standard (SAPS) for your workload by
  using smaller EC2 instance types.
- Using fewer application servers.
- Using lower cost Amazon EBS storage types, for example, `gp3` instead
  of `io2` .
- Using reduced performance characteristics for non-production systems volumes, for
  example, 3,000 IOPS instead of 10,000 IOPS.
- The elasticity of the cloud means that you can scale up your non-production
  testing resources that require production-like performance, such as load or scaling
  tests.

**Suggestion 17.3.3 – Evaluate if non-production environments need the
same operating hours as production**

Non-production environments like test, training, and sandbox systems, might have
reduced operating hours compared with production. Consider time zones and the working
hours of your support teams to determine whether all systems are required 24 x 7. Use this
information to select the lowest pricing model.

For example, running your SAP training system for 40 hours a week with an on-demand
pricing model (~23% uptime) will be cheaper than running it always on at 100% with a 3-year
Reserved Instance or Savings Plan.

**Suggestion 17.3.4 – Evaluate if non-production environments
consistently need the same reliability as production**

Choose the most cost-effective architecture to match each system’s individual
reliability requirements. See [Reliability]: [Best
Practice 10.1 - Agree on SAP workload availability goals that align with your business
requirements](best-practice-10-1.md "best-practice-10-1.md"). Further guidance can be found in the [Reliability Pillar](../reliability-pillar/welcome.md "../reliability-pillar/welcome.md") of the AWS Well-Architected Framework.

Where a production-like architecture exists solely for testing purposes, consider how
often it needs to mirror production. If database high availability is needed in a
non-production environment for reliability or performance testing, you can choose to shut
down or scale down the secondary instance outside of these testing windows to save
cost.

Cost benefits can be realized through the use of automation and by using on-demand
pricing for environments that don’t need production-like performance at all times.

**Suggestion 17.3.5 – Evaluate the business requirements for non-core
systems including support and legacy systems**

If environments exist for reference purposes only, or have a less critical business
role, evaluate the uptime, performance, and reliability requirements needed compared to
your core production systems.

For example, a legacy ERP system might require being kept for reference purposes from
a prior application conversion or business restructure. Costs for this system can be
optimized by running the EC2 instances only when required, thus only paying for Amazon EBS
storage. A more cost-effective solution could be archiving the system via backup to Amazon
S3 and Amazon S3 Glacier.
