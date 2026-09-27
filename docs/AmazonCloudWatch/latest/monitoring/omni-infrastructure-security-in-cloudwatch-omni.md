

# Infrastructure security in CloudWatch Omni
<a name="omni-infrastructure-security-in-cloudwatch-omni"></a>

As a managed service, CloudWatch Omni is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well-Architected Framework*.

You use AWS published API calls to access CloudWatch Omni through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal. Or you can use AWS Security Token Service (AWS STS) to generate temporary security credentials to sign requests. CloudWatch Omni uses Signature Version 4 with the `cloudwatch` signing name.

When CloudWatch Omni reads your telemetry to answer a query, it uses forward access session credentials, so the read is authorized as you rather than as the service. For that identity model, see [Identity and access management for CloudWatch Omni](omni-identity-and-access-management-for-cloudwatch-omni.md), and for how those credentials are protected, see [Data encryption in CloudWatch Omni](omni-data-encryption-in-cloudwatch-omni.md).

**Tenancy and data segregation**

CloudWatch Omni stores its metadata in shared, multi-tenant tables. Each item is logically isolated and scoped to the account that owns it. The underlying stores are not physically isolated for each account.

A request for a resource that another account owns is denied, and CloudWatch Omni does not reveal whether that resource exists, so resources cannot be enumerated across accounts. Resource-name uniqueness is scoped to each account.

**The local trust boundary**

Parts of CloudWatch Omni run on your own machine: the IDE extension, a local development server, and a local Model Context Protocol (MCP) server. Local mode is available in the IDE extension only and does not require an AWS connection. For what the extension does and how to set it up, see [Develop with the IDE extension](omni-develop-with-the-ide-extension.md).

You are responsible for the security of these local components and of the machine they run on:
+ **The local MCP server has no authentication or authorization.** It runs as a child process of the client that launches it, and its proxy accepts connections only from the local machine. Any process that can run on your machine can access it.
+ **The tooling can install its MCP configuration into third-party AI coding-assistant directories.** A connected assistant can then read raw local trace content, including prompts, responses, and tool inputs and outputs, without any additional authorization. Before you install the configuration, decide whether that assistant should have access to this data.
+ **Local telemetry files are plaintext.** The service does not encrypt them. See [Data encryption in CloudWatch Omni](omni-data-encryption-in-cloudwatch-omni.md).

Code-based evaluators run as AWS Lambda functions in your own account. CloudWatch Omni invokes a function whose name begins with `cloudwatchCodeEvaluator` and reads its configuration; it cannot create, modify, or delete the function. Evaluator code runs under an execution role that you control, and CloudWatch Omni does not host or execute evaluator code in its own service. Prompt-based evaluators run in Amazon Bedrock AgentCore and are scored by the model you configure. See [Evaluators and evaluations](omni-agents-evaluators.md).