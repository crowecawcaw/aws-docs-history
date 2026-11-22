

# Siemens Intelligence Center X Graph Studio on AWS

Publication date: **November 19, 2026 ([Diagram history](#sicx-diagram-history))**

This architecture shows how to deploy Siemens Intelligence Center X (ICX) Graph Studio in a single Availability Zone on AWS and how users and AI agents interact with it. The solution runs in an [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/), uses [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/) for persistent block storage, and supports deployment with [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/).

## Siemens ICX Graph Studio architecture diagram
<a name="sicx-diagram"></a>

![Users and AI agents reach Graph Studio on Amazon EC2, which queries an in-memory MPP data store on an Amazon EKS cluster.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/siemens-icx-graph-studio/images/siemens-icx-graph-studio.png)


The following steps describe the architecture:

1. Users and developers connect over HTTPS. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) resolves DNS, and [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) routes requests to the Graph Studio instance.

1. The Graph Studio environment runs on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) for management, configuration, and operations.

1. An [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) cluster hosts the graph engine workloads in a private subnet in a single Availability Zone.

1. The leader pod coordinates query execution and manages data distribution across the in-memory massively parallel processing (MPP) graph engine.

1. Follower pods process sharded graph queries in parallel and scale horizontally in the Amazon EKS cluster.

1. The MPP engine stores ontology graph data sharded by subject hash across slices for high-throughput queries.

1. [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/) provides shared storage for snapshot files and for graph exports in Turtle format.

1. [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) stores operational and analytical data sources.

1. Mendix orchestrates agentic workflows and connects to [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/) through the agent orchestration layer.

1. Foundation models in Amazon Bedrock and [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/) (Runtime and Gateway) provide large language model (LLM) inference and agent orchestration.

1. External data sources (RDBMS/OLTP, traditional BI, document repositories, cloud, and big data/Snowflake) feed into the ontology graph.

1. AI agents interact with the system over HTTPS using the Model Context Protocol (MCP) to run automated graph queries and workflows.

## Further reading
<a name="sicx-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Siemens Intelligence Center X](https://www.siemens.com/en-us/products/intelligence-center-x/)

## Diagram history
<a name="sicx-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#sicx-diagram-history) | Reference architecture diagram first published. | November 19, 2026 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.