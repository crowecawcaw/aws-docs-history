# MSFTCOST04-BP03 Consider purpose-built databases

Purpose-built databases are gaining traction among businesses
adopting modern architectures like microservices, as they can
precisely accommodate specific data access patterns. These
databases, whether SQL or NoSQL, offer application teams benefits
like reduced costs, enhanced scalability, and improved resilience.
By selecting the right database for each specific use case, teams
can optimize their data management while leveraging cloud advantages
for more efficient solutions.

**Desired outcome:** By adopting
purpose-built databases tailored to specific workload requirements,
application teams will optimize data management, reduce costs, and
enhance scalability and resilience. This approach will lead to more
efficient cloud-based solutions, whether using SQL or NoSQL
databases, and minimize undifferentiated heavy lifting in database
operations.

**Common anti-patterns:**

- Using a single database technology for all applications and
  workloads, regardless of their specific data access patterns or
  requirements. This can lead to suboptimal performance,
  scalability issues, and increased costs.
- Adopting multiple specialized databases for every minor
  variation in data needs, resulting in a fragmented and overly
  complex data architecture that increases management overhead and
  potentially negates cost savings.

**Benefits of establishing this best
practice:**

- Purpose-built databases are designed to handle specific data
  access patterns, resulting in improved query performance and
  overall system efficiency tailored to each application's unique
  needs.
- By choosing databases that align closely with workload
  requirements, organizations can avoid over-provisioning
  resources and reduce unnecessary licensing costs associated with
  general-purpose database solutions.
- Purpose-built databases often come with built-in features for
  horizontal scaling and high availability, making it easier for
  applications to handle growth in data volume and user traffic
  while maintaining robust performance and reliability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin by analyzing your application's data access patterns, query
requirements, and scalability needs. Identify distinct workload
characteristics across your application portfolio and map them to
appropriate purpose-built database solutions. For new
applications, design the data architecture with these specific
requirements in mind from the start. For existing applications,
consider a phased migration approach, starting with the components
that would benefit most from purpose-built databases. Evaluate AWS
purpose-built database options such as Amazon DynamoDB for
high-performance NoSQL needs, Amazon RDS for traditional
relational workloads, or Amazon Redshift for data warehousing,
ensuring each choice aligns with both technical requirements and
cost optimization goals.

### Implementation steps

1. Analyze current data access patterns and requirements across
   your application portfolio
2. Identify suitable purpose-built database solutions for each
   distinct workload
3. Develop a migration strategy, prioritizing components that
   will benefit most from the change
4. Implement and test the new database solutions in a staging
   environment
5. Gradually migrate production workloads, monitoring
   performance and costs throughout the process

## Resources

**Related documents:**

- [Consider
  purpose-built databases](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-purpose.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-purpose.md")

**Related tools:**

- [What
  is the AWS Schema Conversion Tool?](../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md "../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md")
