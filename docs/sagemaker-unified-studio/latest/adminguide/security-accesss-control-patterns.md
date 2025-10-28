# Access control patterns Amazon SageMaker Unified Studio

Effective data management and governance are crucial to deriving value from data assets
while maintaining compliance and security. In Amazon SageMaker Unified Studio, you can use projects to simplify
development and collaboration. Projects contain one or more IAM roles, and there is at least
one project role for each account in which the project has resources. You have access to all
the tools, compute, data, and AIML assets this role has access to. When you access a project
from Amazon SageMaker Unified Studio, it is equivalent to logging into an account in a specific region and
assuming one of the project’s roles. There are two ways to manage what these roles have
access to. First, you can simply add the IAM permissions directly to the project’s IAM role.
Second, you can publish data and AI/ML assets to the Amazon SageMaker catalog and enable
project members to subscribe to those assets. Both of these approaches are covered in this
section.

###### Topics

- [Using IAM to configure access in
  Amazon SageMaker Unified Studio](#security-accesss-control-patterns-iam "#security-accesss-control-patterns-iam")
- [Data access and
  subscription workflows using Amazon SageMaker catalog](#security-accesss-control-patterns-datazone "#security-accesss-control-patterns-datazone")

## Using IAM to configure access in

Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, a domain is the fundamental organizational unit that enables you to
manage multiple AWS Regions, accounts, and workloads through a single interface. Each
domain has its own unique URL and provides centralized management of studio settings,
accounts, users, and network configurations.

Within domains, projects streamline and enable collaboration. Projects can be located
in different regions or in different accounts within a given region. Project metadata
contains information about the project's git repository, members, and their permissions.
There is at least one project role for each account in which the project has resources.
The project IAM role defines what tools, compute resources, data, and AI/ML assets
project members can access. You can think of entering a project in Amazon SageMaker Unified Studio as logging
into a regional account where you take on a designated role. To manage access to data,
you can simply modify the IAM permissions to the project’s IAM role.

It is important that you understand the different IAM roles used in Amazon SageMaker Unified Studio and
their functions in detail. This section covers those details. When you modify an IAM
role to manage data access, you must factor in the region, account, and role you need to
give permissions to. For more information on simplifying configuring permissions and
customizing role assignments, see the [AWS IAM Roles section](../userguide/bring-resources-scripts.md#resource-scripts-iam "../userguide/bring-resources-scripts.md#resource-scripts-iam") in "Bringing existing resources into Amazon
SageMaker Unified Studio".

**Domain execution role** - the
AmazonSageMakerDomainExecution role is an IAM role that enables Amazon SageMaker Unified Studio to execute API
calls on behalf of authorized users. It provides access to all APIs that are required
for Amazon SageMaker Unified Studio to use, as well as RAM permissions to support usage of associated accounts
in an Amazon SageMaker unified domain. It also provides access to services used outside
of a project scope, including AWS CodeConnections, Amazon Q, AWS Systems Manager,
and Amazon Bedrock.

**Service role** - the AmazonSageMakerDomainService role
is a specialized service role that enables domain-level actions in Amazon SageMaker Unified Studio. It is
responsible for managing critical operations within the domain, particularly the
handling of blueprint parameters in Systems Manager (SSM). These parameters are
essential for executing privileged calls, ensuring secure and controlled access to
domain-level functionalities.

**Provisioning Role** - Amazon SageMaker Unified Studio employs an IAM policy
to manage and provision resources across various AWS services within an AWS account.
This policy, associated with the AmazonSageMakerProvisioning role, grants access to
essential services such as Amazon SageMaker, AWS Glue, Amazon S3, AWS Lake
Formation, Amazon Redshift, Amazon Athena, Amazon Q, Amazon EMR, AWS CodeCommit, Amazon Bedrock,
and AWS IAM. The policy enables management of SageMaker Domains and
Spaces, AWS Glue components, S3 objects, Lake Formation grants, Redshift workgroups,
Athena workgroups and catalogs, EMR clusters, KMS keys, CodeCommit repositories, Secrets
Manager secrets, IAM roles, and Amazon Bedrock in SageMaker Unified Studio resources.
This access allows Amazon SageMaker Unified Studio to effectively orchestrate and manage the lifecycle of
projects and resources across the AWS ecosystem, providing users with a seamless and
integrated experience for data science and machine learning tasks.

**Manage Access Role** - the AmazonSageMakerManageAccess
role is designed to manage access and permissions across various data services. This
role enables Amazon SageMaker Unified Studio to publish, grant, and revoke access to data within Amazon
SageMaker Lakehouse, AWS Glue Data Catalog, and Amazon Redshift. Additionally, it
facilitates the management of subscriptions for data and AI assets in the Amazon
SageMaker catalog. To achieve these functionalities, the role incorporates three Amazon
DataZone managed policies: AmazonDataZoneGlueManageAccessRolePolicy,
AmazonDataZoneRedshiftManageAccessRolePolicy, and AmazonDataZoneSageMakerAccess. These
policies collectively provide the necessary permissions for seamless data management and
access control, ensuring efficient collaboration and resource utilization across
different AWS services.

**Project role** - Amazon SageMaker Unified Studio creates IAM roles that
enable project users to perform data analytics, AI, and machine learning tasks. There
are two IAM policies governing these permissions: SageMakerStudioProjectUserRolePolicy
and SageMakerStudioProjectRoleMachineLearningPolicy. This role grants users read and
write access to relevant AWS services including Amazon SageMaker, AWS Glue, Amazon
S3, AWS Lake Formation, Amazon Redshift, Amazon Athena, Amazon Q, and Amazon EMR.
Additionally, it provides necessary permissions for infrastructure resources such as
network interfaces, AWS KMS keys, AWS CodeCommit, and AWS Secrets Manager.
Administrators maintain granular control over these permissions through role tagging -
for example, they can disable Glue Spark workload permissions by applying the tag
'EnableGlueSparkWorkloads=false', or restrict Generative AI Studio access using the tag
'EnableGenAIStudio=false'.

###### Note

You can't create new projects with AWS CodeCommit. Existing projects that were
created using CodeCommit will continue to work.

**Amazon Bedrock service role** - in each Generative AI
app development project, Amazon SageMaker Unified Studio creates an IAM role that allows the Amazon Bedrock
service to access generative AI application resources in the project. This role governs
the access and permissions for various Amazon Bedrock components within Amazon SageMaker Unified Studio. It
encompasses four main service roles: Amazon Bedrock Agent, Amazon Bedrock Knowledge
Base, Amazon Bedrock Flows, and Amazon Bedrock Evaluation. Each role is designed to
grant specific permissions to Amazon Bedrock services, allowing them to interact with
relevant resources such as Amazon Bedrock models, AWS Lambda functions, Amazon S3
buckets, AWS KMS keys, and OpenSearch Serverless collections. The policies ensure that
Amazon Bedrock Agents, Knowledge Bases, Flows, and Evaluations can access necessary
resources while maintaining security through project-specific tag restrictions. These
roles enable seamless integration of Amazon Bedrock capabilities with Amazon SageMaker Unified Studio,
facilitating tasks like model invocation, data access, encryption, and resource
management within the confines of each project's scope. This structured approach ensures
efficient operation of Amazon Bedrock services while maintaining appropriate access
controls and resource isolation. This role is attached with the following AWS managed
policies:

- [AWS policy: SageMakerStudioBedrockAgentServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockAgentServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockAgentServiceRolePolicy.md")
- [AWS policy:
  SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy.md")
- [AWS policy: SageMakerStudioBedrockFlowServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockFlowServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockFlowServiceRolePolicy.md")
- [AWS policy:
  SageMakerStudioBedrockEvaluationJobServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockEvaluationJobServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockEvaluationJobServiceRolePolicy.md")

**Amazon Bedrock Lambda execution role** - in each
Generative AI app development project, Amazon SageMaker Unified Studio creates an IAM role that allows the
AWS Lambda service to access generative AI application resources in the project. This
role encompasses two key roles within Amazon SageMaker Unified Studio: the Amazon Bedrock Knowledge Base
custom resource service role and the Amazon Bedrock function execution role. The
knowledge base custom resource role enables configuration of vector stores and Amazon
Bedrock knowledge bases, granting AWS Lambda-backed CloudFormation custom resources
access to Amazon Bedrock knowledge bases and OpenSearch Serverless collections. It
allows for starting and querying knowledge base ingestion jobs and preparing OpenSearch
collections. It permits AWS Lambda to access Amazon Bedrock function component
configurations, including Secrets Manager secrets and KMS keys, which are necessary for
handling API requests. Additionally, this role provides write permissions to CloudWatch
Logs for monitoring and logging purposes. This facilitates the seamless integration and
management of Amazon Bedrock components within the Amazon SageMaker Unified Studio while maintaining
appropriate access controls. This role is attached with the following AWS managed
policies:

- [AWSLambdaBasicExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaBasicExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaBasicExecutionRole.md")
- [AWS policy:
  SageMakerStudioBedrockFunctionExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockFunctionExecutionRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockFunctionExecutionRolePolicy.md")
- [AWS policy:
  SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy](security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy.md")

**Amazon Bedrock chat agent user role** - in each Amazon
Bedrock chat agent, Amazon SageMaker Unified Studio creates an IAM role that allows the Amazon DataZone
service to provide shared users access to an Amazon Bedrock chat agent app's
configuration and Amazon Bedrock chat agent. As part of the AmazonBedrockChatAgent
blueprint, it defines the main policy for the Amazon Bedrock chat agent user role. It
grants users the ability to interact with shared Amazon Bedrock chat agent apps,
including invoking Amazon Bedrock chat agents, retrieving configurations from Amazon S3,
and utilizing AWS KMS keys for encryption. It provides necessary permissions for users
to read and invoke Amazon Bedrock chat agents, access specific S3 objects within the
project's bucket, and use KMS keys for encrypted data access. The role is designed to
allow access only to individually shared Amazon Bedrock chat agent apps, maintaining
security by restricting domain and project users from modifying user role tags. It
ensures that users can effectively utilize Amazon Bedrock chat agent applications while
adhering to appropriate access controls and data protection measures. This role is
attached with the following AWS managed policies:

**Amazon Bedrock prompt user role** - in each Amazon
Bedrock prompt, Amazon SageMaker Unified Studio creates an IAM role that allows the Amazon DataZone service to
provide shared users access to an Amazon Bedrock prompt and its configuration. It
defines the access permissions for users of Amazon Bedrock prompts within Amazon SageMaker Unified Studio. As
part of the AmazonBedrockPrompt blueprint, it serves as the main policy for the Amazon
Bedrock prompt user role. It grants users access to shared Amazon Bedrock prompts,
including the ability to read Amazon Bedrock prompts, access their configurations stored
in Amazon S3, and use AWS KMS keys for encryption. It provides necessary permissions
for users to interact with Amazon Bedrock prompts, retrieve specific objects from the
project's S3 bucket, and utilize KMS keys for encrypted data access. It is designed to
allow access only to individually shared Amazon Bedrock prompts, maintaining security by
restricting domain and project users from modifying user role tags. This ensures that
users can effectively work with Amazon Bedrock prompts while adhering to appropriate
access controls and data protection measures within Amazon SageMaker Unified Studio.

**Query execution role for federated connection** - this
role is used when executing a query using Amazon Athena. AWS LakeFormation assumes
this role to vend credentials needed by Amazon Athena during query execution. The
SageMakerQueryExecutionRole has the AWS policy:
SageMakerStudioQueryExecutionRolePolicy attached.

**EMR Service role** - this role defines the necessary
permissions for Amazon EMR instances running on EC2, ensuring secure and controlled
access to EC2 networking, IAM roles, and AWS KMS for encryption. It grants permissions
to create network interfaces and launch instances, restricting these actions to VPCs
that match the principal’s VPC ID tag. To support secure data handling, it provides
AWS KMS encryption and decryption permissions for a specified KMS key, allowing EMR
instances to manage encrypted data and EBS volumes. It also enables EMR to manage KMS
grants, including listing, revoking, and describing keys, specifically for EC2 services
within the same AWS account. Furthermore, the policy permits EMR to list KMS key
aliases, ensuring seamless access to encryption keys. This policy ensures that EMR
instances operate within a well-defined network, securely handle encrypted data, and
adhere to account-specific security constraints.

**EMR Instance Profile role** - this role grants
permissions necessary for Amazon EMR instances operating within Amazon SageMaker Unified Studio, ensuring
secure access to S3, IAM, and KMS resources. It allows EMR instances to retrieve SSL
certificates from an S3 bucket, ensuring secure communication, and access patching RPMs
stored in a predefined S3 location. Additionally, it permits retrieval of bootstrap
action scripts from S3, enabling customized EMR cluster configurations, and allows the
uploading of EMR cluster logs to a designated S3 location for monitoring and debugging
purposes. The role also enables EMR instances to assume runtime roles with specific
session tags, ensuring authorized access to Lake Formation resources. Furthermore, it
grants permissions for AWS KMS operations, including encryption, decryption, and key
generation, allowing secure handling of sensitive data and EBS volume encryption. By
enforcing conditions based on resource ownership, principal tags, and account
constraints, this IAM role ensures that EMR clusters operate securely within a
well-defined Amazon DataZone framework, maintaining compliance and access control best
practices.

**Partner Apps IAM role** - this role enables Amazon
SageMaker partner app users to access applications, list available applications, launch
application web UIs, and connect via the application SDK. Access is restricted to
partner apps owned by the same AWS account as the requesting principal (enforced by
the aws:ResourceAccount condition). This ensures that the user can only interact with
partner apps within their own AWS account, preventing cross-account access.

## Data access and

subscription workflows using Amazon SageMaker catalog

You get a comprehensive framework for data discovery, subscription, and consumption
through the Amazon SageMaker catalog. It enables seamless collaboration between data
publishers and subscribers, facilitating controlled access to valuable data assets
across an organization. By implementing a structured process for asset discovery,
subscription requests, and approval workflows, Amazon SageMaker Unified Studio ensures that data access is
granted based on justified needs and adheres to organizational policies.

Once an asset is published to a domain, subscribers can discover and request a
subscription to this asset. The subscription process begins with a subscriber searching
for and browsing the catalog to discover an asset they want. From Amazon SageMaker Unified Studio, they choose
to subscribe to the asset by submitting a subscription request that includes
justification and the reason for the request. The subscription approver then reviews the
access request. They can either approve or reject the request. After a subscription is
granted, a fulfillment process starts to facilitate access to the asset for the
subscriber. For more information, see [Request subscription to assets in Amazon DataZone](../../../datazone/latest/userguide/subscribe-to-data-assets-managed-by-datazone.md "../../../datazone/latest/userguide/subscribe-to-data-assets-managed-by-datazone.md").

In Amazon SageMaker catalog, subscription requests to assets are managed by
subscription approvers. A subscription approver for an asset is determined by the
publishing agreement with which this asset was published into the Amazon SageMaker
catalog. For some assets, Amazon SageMaker catalog can manage access grants and
auto-approve subscription requests. These assets are called managed assets and include
Lake Formation-managed AWS Glue Data Catalog tables and Amazon Redshift tables and
views. Alternatively, for manual approvals, Amazon SageMaker catalog kicks of a workflow
via an EventBridge integration so the subscription approver can review and
approve/reject the request. After a subscription is granted, Amazon SageMaker catalog
starts a fulfillment process starts to facilitate access to the asset for the subscriber
and takes care of managing and orchestrating the permissions setup across regions and
accounts. To learn more about how Amazon SageMaker catalog facilitates asset discovery,
subscription requests, approval processes, and access controls, see [Amazon DataZone data discovery, subscription, and consumption](../../../datazone/latest/userguide/discover-subscribe-consume-data.md "../../../datazone/latest/userguide/discover-subscribe-consume-data.md").
