# What is a DevOps Agent Topology?

AWS DevOps Agent's automatically discovers and visualizes the resources and relationships within your applications and uses the resulting topology to understand your infrastructure during incident investigations and when making preventative recommendations.

## How topology graphs are created

AWS DevOps Agent builds topology graphs through several automated processes:

- **Resource discovery** – The agent automatically scans your AWS accounts to identify resources like compute instances, storage services, networking components, and databases that are part of your applications.
- **Relationship detection** – The agent analyzes configuration data, CloudFormation stacks, and resource tags to determine how resources relate to one another.
- **Code and deployment mapping** – When connected to CI/CD pipelines, the agent links infrastructure resources back to their deployment processes and changed application and infrastructure code.
- **Observability behavior mapping** – Data from observability systems such as Amazon CloudWatch Application Signals and Dynatrace are used to identify observed behaviors that indicate relationships between resources.

## Key capabilities

Resource mapping provides several capabilities that enhance incident investigation and prevention:

- **Interactive visualization** – Explore your application topology through an interactive graph in the Operator Web App. You can zoom and navigate the topology to understand complex relationships between resources.
- **Contextual investigation** – During incident investigations, AWS DevOps Agent is assisted by the resource topology to identify affected components, understand blast radius, and trace the impact path through your systems.
- **Root cause analysis** – The detailed understanding of resource relationships helps pinpoint where issues originate, even in complex distributed systems with many interdependencies.
- **Impact assessment** – When analyzing incidents, the agent can better determine which downstream services might be affected by identifying dependency chains in the topology.
- **Preventative recommendations** – The agent uses topology insights to make targeted recommendations for resilience improvements, suggesting changes that will have the most significant impact on system stability.

## Topology views

The topology visualization in DevOps Center page in the Operator Web App offers multiple levels of detail:

- **System view** – Shows high-level account and region boundaries
- **Container view** – Displays deployment stacks like CloudFormation stacks that contain related resources
- **Resource view** – Shows the complete view with all resources and their relationships

## Resource discovery

Resources are discovered through two methods:

- **CloudFormation stacks** – The agent will list all of the CloudFormation stacks and their resources in the primary AWS account as well as an connected secondary accounts. This is supported for any infrastructure-as-code tooling that uses CloudFormation for deployment, including Cloud Development Kit (CDK).
- **Resource Tags** – For resources not deployed from CloudFormation, you can specify a list of AWS Tag keys and value pairs to include in the resource topology. This is useful to identify application boundaries for applications deployed through the AWS Management Console, the AWS service APIs, or other infrastructure-as-code frameworks.

###### Note

The target AWS account must have Resource Explorer enabled to discover tagged resources.

## Investigation scope beyond topology

While the application topology provides important context during investigations, AWS DevOps Agent is not limited to investigating only the resources shown in the topology. The agent may use additional data sources, such as AWS service APIs or connected observability tools, to investigate resources that are not in the application topology.

To limit the resources the agent has access to, restrict the policy for the role assigned to the agent to access cross-account resources. For more information, see [Limiting Agent Access in an AWS Account](aws-devops-agent-security-limiting-agent-access-in-an-aws-account.md "aws-devops-agent-security-limiting-agent-access-in-an-aws-account.md").
