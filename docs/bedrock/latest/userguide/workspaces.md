# Workspaces (Anthropic-compatible)

Amazon Bedrock Workspaces provide application-level isolation for your generative AI workloads using the Anthropic-compatible Messages API on the `bedrock-mantle` endpoint. Workspaces enable you to segment your AI applications for cost tracking, observability, and access control.

###### Tip

For new applications, we recommend the `bedrock-runtime` endpoint. If you don't need Workspaces, use the [Converse](conversation-inference.md "conversation-inference.md") or [Invoke](inference-invoke.md "inference-invoke.md") APIs with [Inference Profiles](inference-profiles-create.md "inference-profiles-create.md") for isolation, tagging, and cost tracking on `bedrock-runtime`.

###### Note

Workspaces can only be used with models that support the Messages API on the `bedrock-mantle` endpoint. To see which models support the Messages API, see [APIs supported by Amazon Bedrock](apis.md "apis.md").

If you are using the OpenAI-compatible APIs (Responses API, Chat Completions), use [Projects (OpenAI-compatible)](projects.md "projects.md") instead.

## What is a Workspace?

A Workspace is a logical boundary used to isolate workloads such as applications, environments, or experiments within Amazon Bedrock when using the Anthropic Messages API. Workspaces are the same underlying resource as [Projects (OpenAI-compatible)](projects.md "projects.md") — they are managed using the Projects API and provide the same capabilities:

- **Access isolation**: Control who can access specific workspace resources using [IAM policies for Amazon Bedrock Projects](security-iam-projects.md "security-iam-projects.md")
- **Cost monitoring**: Track spending at the workspace level using [AWS tags](whitepapers/latest/tagging-best-practices/what-are-tags.md "whitepapers/latest/tagging-best-practices/what-are-tags.md") and [AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md")
- **Observability**: Track usage metrics and patterns per workspace for monitoring and optimization.

Workspaces allow you to manage multiple generative AI workloads in production without creating separate AWS accounts or organizations, reducing operational complexity while maintaining security and governance.

Each AWS account has a default workspace (project) where all inference requests are associated. You can create additional workspaces using the Projects API and reference them in Messages API requests using the `anthropic-workspace-id` header.

## When to use Workspaces

You should use Workspaces when you need to:

- **Organize by business structure**: Manage Amazon Bedrock usage based on your organizational taxonomy such as business units, teams, applications, or cost centers
- **Track costs accurately**: Monitor and allocate AI spending to specific teams, projects, or environments
- **Enforce access policies**: Apply granular IAM permissions to control who can access specific AI workloads
- **Scale production workloads**: Run multiple production applications with clear operational boundaries and monitoring

## Workspaces vs. Projects

Workspaces and [Projects (OpenAI-compatible)](projects.md "projects.md") are the same underlying resource — both are managed through the Projects API. The difference is how you reference them in your inference requests, depending on which API you use:

| Feature        | Workspaces                                              | Projects                                             |
| -------------- | ------------------------------------------------------- | ---------------------------------------------------- |
| Supported APIs | Anthropic Messages API                                  | OpenAI-compatible APIs (Responses, Chat Completions) |
| Endpoint       | `bedrock-mantle.{region}.api.aws/anthropic/v1/messages` | `bedrock-mantle.{region}.api.aws/v1`                 |
| Header         | `anthropic-workspace-id: {project-id}`                  | `OpenAI-Project: {project-id}`                       |
| Management API | Projects API                                            | Projects API                                         |
| Access Control | Project as a resource in IAM policies                   | Project as a resource in IAM policies                |
| Cost Tracking  | AWS tags on projects                                    | AWS tags on projects                                 |

## Getting started with Workspaces

This section walks you through creating a workspace, associating it with Messages API requests, and verifying your setup.

### Prerequisites

Before you begin, make sure you have:

- An AWS account with Amazon Bedrock access
- IAM permissions to create and manage Amazon Bedrock projects
- An [API key](api-keys.md "api-keys.md") for Amazon Bedrock authentication
- Access to Claude models (see [Request access to models](model-access.md "model-access.md"))

### Step 1: Set up your environment

Configure your environment variables with your Amazon Bedrock credentials:

```
export BEDROCK_API_KEY="<your-bedrock-key>"
export BEDROCK_REGION="us-east-1"
```

### Step 2: Create a Workspace

Workspaces are created using the Projects API. Create a workspace (project) with a name and tags for cost monitoring:

```
curl -X POST "https://bedrock-mantle.$BEDROCK_REGION.api.aws/v1/organization/projects" \
  -H "Authorization: Bearer $BEDROCK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Claude Chatbot Production",
    "tags": {
      "Application": "CustomerChatbot",
      "Environment": "Production",
      "Team": "NLPEngineering",
      "CostCenter": "41250"
    }
  }'
```

Response:

```
{
  "arn": "arn:aws:bedrock-mantle:us-east-1:123456789012:project/proj_abc123def456",
  "created_at": 1772135628,
  "id": "proj_abc123def456",
  "name": "Claude Chatbot Production",
  "object": "organization.project",
  "status": "active",
  "tags": {
    "Application": "CustomerChatbot",
    "Environment": "Production",
    "Team": "NLPEngineering",
    "CostCenter": "41250"
  }
}
```

Note the `id` field — this is the value you pass in the `anthropic-workspace-id` header.

### Step 3: Associate requests with your Workspace

To associate your Messages API requests with a workspace, include the `anthropic-workspace-id` header with the project ID:

curl

```
curl -X POST "https://bedrock-mantle.$BEDROCK_REGION.api.aws/anthropic/v1/messages" \
  -H "x-api-key: $BEDROCK_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-workspace-id: proj_abc123def456" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic.claude-sonnet-4-6-v1",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, how can you help me today?"}
    ]
  }'
```

Python (Anthropic SDK)

```
import anthropic

client = anthropic.Anthropic(
    base_url=f"https://bedrock-mantle.{region}.api.aws/anthropic",
    api_key=bedrock_api_key,
)

response = client.messages.create(
    model="anthropic.claude-sonnet-4-6-v1",
    max_tokens=1024,
    extra_headers={"anthropic-workspace-id": "proj_abc123def456"},
    messages=[
        {"role": "user", "content": "Hello, how can you help me today?"}
    ]
)

print(response.content[0].text)
```

All inference requests made with the same workspace ID are grouped together, enabling per-workspace cost tracking, access control, and observability.

### Step 4: Verify your Workspace setup

List all workspaces (projects) to verify your workspace was created successfully:

```
curl -X GET "https://bedrock-mantle.$BEDROCK_REGION.api.aws/v1/organization/projects" \
  -H "Authorization: Bearer $BEDROCK_API_KEY"
```

## Managing Workspaces

Since Workspaces are managed through the Projects API, all project management operations apply. See [Working with Projects](projects.md#projects-working-with "projects.md#projects-working-with") for detailed instructions on:

- **Listing workspaces**: Retrieve all workspaces in your account
- **Retrieving details**: Get information about a specific workspace
- **Updating workspaces**: Modify workspace name or tags
- **Managing tags**: Add or remove tags for cost allocation
- **Archiving workspaces**: Archive workspaces that are no longer in use

## Best practices

### Recommended Workspace structure

**One workspace per application**: Create separate workspaces for each distinct application or service.

```
├── Claude-Chatbot-Production
├── Claude-Chatbot-Staging
├── Claude-Chatbot-Development
├── Claude-Summarizer-Production
└── Claude-Summarizer-Development
```

- **Separate environments**: Use different workspaces for development, staging, and production environments.
- **Experiment isolation**: Create dedicated workspaces for experiments and proof-of-concepts.

### Workspace lifecycle management

- **Create workspaces early**: Set up workspaces before deploying applications
- **Use consistent naming**: Follow organizational naming conventions
- **Tag for cost allocation**: Always include cost center and team tags
- **Regular audits**: Periodically review and archive unused workspaces
- **Monitor usage**: Track workspace metrics to identify optimization opportunities
