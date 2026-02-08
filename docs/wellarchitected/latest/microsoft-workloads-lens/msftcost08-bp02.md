# MSFTCOST08-BP02 Consider serverless architecture for your

Microsoft .NET applications

AWS Lambda enables .NET developers to build serverless applications
without managing servers, paying only for actual usage. Using modern
.NET versions, developers can create scalable functions in C# or F#
that run on-demand in the cloud, reducing costs and development
time.

**Desired outcome:** By adopting
serverless architecture with AWS Lambda for .NET applications,
organizations may achieve improved scalability and cost efficiency,
paying only for resources used while eliminating server management
overhead. Using AWS tools like Microservice Extractor may further
simplify the modernization of existing applications.

**Common anti-patterns:**

- Maintaining continuously operational and over-sized servers for
  .NET applications instead of leveraging serverless architecture,
  resulting in unnecessary costs and underutilized resources.
- Keeping large and monolithic .NET applications intact rather
  than breaking them down into microservices or serverless
  functions, leading to reduced flexibility and scalability.

**Benefits of establishing this best
practice:**

- Organizations only pay for actual compute resources consumed
  during function execution, eliminating costs associated with
  idle server capacity and infrastructure management.
- Development teams can focus on code rather than server
  maintenance, reducing operational overhead and accelerating
  deployment cycles.
- Applications automatically scale based on demand without manual
  intervention, ensuring optimal performance during peak loads
  while maintaining cost efficiency during low-usage periods.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin by identifying suitable .NET applications or components that
can benefit from serverless architecture. Start small by migrating
discrete functions to AWS Lambda using modern .NET versions (Core
or later). Utilize AWS Microservice Extractor for .NET to analyze
and decompose existing monolithic applications into smaller,
manageable services. Implement proper monitoring and logging from
the outset using AWS CloudWatch, and establish clear deployment
pipelines using AWS CI/CD tools. Gradually, expand the serverless
footprint as the team gains experience and confidence with the
architecture.

### Implementation steps

1. Install and configure AWS Microservice Extractor for .NET to
   analyze existing monolithic applications and identify
   potential microservice candidates
2. Assess existing .NET applications and identify functions
   suitable for serverless migration, prioritizing stateless
   operations and event-driven processes
3. Set up the AWS Lambda development environment with .NET SDK
   and necessary AWS tools (AWS Toolkit for Visual Studio and
   AWS CLI)
4. Create and test initial Lambda functions using modern .NET
   versions, implementing proper error handling and logging
5. Configure automated deployment pipelines using AWS CI/CD
   services (CodePipeline and CodeBuild) for consistent
   function updates
6. Monitor function performance and costs using AWS CloudWatch,
   and optimize resource allocation based on actual usage
   patterns

## Resources

**Related documents:**

- [Consider
  serverless .NET](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-serverless.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-serverless.md")

**Related tools:**

\*[What
Is AWS Microservice Extractor for .NET?](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")
