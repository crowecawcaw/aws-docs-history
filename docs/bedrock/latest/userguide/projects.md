# Projects (OpenAI-compatible)

Amazon Bedrock Projects API provides application-level isolation for your generative AI workloads using [OpenAI-compatible APIs](bedrock-mantle.md "bedrock-mantle.md"). Projects enable you to organize and manage your AI applications with improved access control, cost tracking, and observability across your organization.

###### Note

Projects can only be used with models that use the OpenAI-compatible APIs against the [bedrock-mantle endpoint](bedrock-mantle.md "bedrock-mantle.md"). If you are using the bedrock-runtime endpoint, please use Inference Profiles instead of tagging and observability.

## What is a Project?

A Project is a logical boundary used to isolate workloads such as applications, environments, or experiments within Amazon Bedrock. Projects provide:

- **Access isolation**: Control who can access specific project resources using [IAM policies for Amazon Bedrock Projects](security-iam-projects.md "security-iam-projects.md")
- **Cost monitoring**: Track spending at the project level using [AWS tags](whitepapers/latest/tagging-best-practices/what-are-tags.md "whitepapers/latest/tagging-best-practices/what-are-tags.md") and [AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md")

Projects allow you to manage multiple generative AI workloads in production without creating separate AWS accounts or organizations, reducing operational complexity while maintaining security and governance.

Each AWS account has a default project where all inference requests are associated with. You can create more projects in your account using the Projects API.

## When to Use Projects

You should use the Projects API when you need to:

- **Organize by business structure**: Manage Bedrock usage based on your organizational taxonomy such as business units, teams, applications, or cost centers
- **Track costs accurately**: Monitor and allocate AI spending to specific teams, projects, or environments
- **Enforce access policies**: Apply granular IAM permissions to control who can access specific AI workloads
- **Scale production workloads**: Run multiple production applications with clear operational boundaries and monitoring

## Projects vs. Inference Profiles

Both Projects API and [Inference Profiles](inference-profiles-create.md "inference-profiles-create.md") provide isolation, tagging, and access control capabilities in Amazon Bedrock, but they differ based on the API you use. If you're using OpenAI-compatible APIs with the [bedrock-mantle](endpoints.md "endpoints.md") endpoint, which uses the Mantle inference engine, use the Projects API. If you're using Invoke or Converse APIs with the [bedrock-runtime](endpoints.md "endpoints.md") endpoint, use Inference Profiles. While you can use Chat Completions API with either bedrock-mantle or bedrock-runtime endpoints, we recommend you use the Mantle endpoint.

| Feature        | Projects API                                         | Inference Profiles                                                               |
| -------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------- |
| Supported APIs | OpenAI-compatible APIs (Responses, Chat Completions) | Native Bedrock APIs (Invoke, Converse), OpenAI-compatible API (Chat Completions) |
| Endpoint       | `bedrock-mantle.{region}.api.aws`                    | `bedrock-runtime.{region}.amazonaws.com`                                         |
| Use Case       | Applications using OpenAI-compatible endpoints       | Applications using native Bedrock APIs                                           |
| Access Control | Project as a resource in IAM policies                | IAM policies on inference profile ARN                                            |
| Cost Tracking  | AWS tags on projects                                 | AWS tags on inference profiles                                                   |

## Projects vs. AWS Accounts

[AWS Accounts](../../../accounts/latest/reference/accounts-welcome.md "../../../accounts/latest/reference/accounts-welcome.md") and [AWS Organizations](../../../controltower/latest/userguide/organizations.md "../../../controltower/latest/userguide/organizations.md") represent billing and ownership boundaries at the infrastructure level. Projects represent workload and application boundaries within a single account.

Using Projects instead of separate AWS accounts provides:

- **Faster setup**: Create projects in seconds via API calls
- **Reduced complexity**: Manage multiple workloads without account sprawl
- **Simplified operations**: Centralized management within a single account
- **Lower overhead**: No need for cross-account IAM roles or resource sharing

## Getting started with Projects

This page walks you through creating your first project, associating it with inference requests, and managing project resources.

### Prerequisites

Before you begin, ensure you have:

- An AWS account with Amazon Bedrock access
- IAM permissions to create and manage Bedrock projects
- Python 3.7 or later installed
- The OpenAI Python SDK installed: `pip install openai boto3`
- An [API key](api-keys.md "api-keys.md") for Amazon Bedrock authentication

### Step 1: Set Up Your Environment

Configure your environment variables with your Amazon Bedrock credentials:

```
export OPENAI_API_KEY="<your-bedrock-key>"
export OPENAI_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/v1"
```

Replace `<your-region>` with your AWS region (e.g., us-east-1, us-west-2).

###### Note

Amazon Bedrock offers [two types of keys](bedrock/latest/userguide/api-keys-how.md "bedrock/latest/userguide/api-keys-how.md"): short-term and long-term. While you can use long-term API keys for exploration of Amazon Bedrock, we recommend short-term keys for applications with greater security requirements. If you use long-term keys with Projects, note that the default policy attached to long term keys only allows you to get and list projects, but not create/update/archive them. If you would like your long-term key to manage projects, then you will have to assign additional IAM policies to your keys to enable these operations.

### Step 2: Discover Available Models

Use the `list()` API to retrieve a list of models compatible with the Projects API:

```
curl -X GET $OPENAI_BASE_URL/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

### Step 3: Create Your First Project

Create a project using the Create Project API with tags for cost monitoring and observability. Note that at this time only cURL is supported in the SDK.

```
curl -X POST $OPENAI_BASE_URL/organization/projects \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Project ABC",
    "tags": {
      "Project": "CustomerChatbot",
      "Environment": "Production",
      "Owner": "TeamAlpha",
      "CostCenter": "21524"
    }
  }' -v
```

Response:

```
{
  "arn": "arn:aws:bedrock-mantle:ap-northeast-1:673693429514:project/proj_5d5ykleja6cwpirysbb7",
  "created_at": 1772135628,
  "id": "proj_5d5ykleja6cwpirysbb7",
  "name": "Project ABC",
  "object": "organization.project",
  "status": "active",
  "tags": {
    "Owner": "TeamAlpha",
    "Project": "CustomerChatbot",
    "Environment": "Production",
    "CostCenter": "21524"
  }
}
```

**Important Notes:**

- The geography parameter in the OpenAI API specification is ignored by Amazon Bedrock.
- The region is determined by your endpoint configuration.
- The arn field is specific to Amazon Bedrock and provides the ARN for IAM policy attachment.
- Tags can be specified during project creation and are returned in all project responses.

### Step 4: Associate Inference Requests with Your Project

To associate your project for inference requests, provide the project ID when creating the client:

cURL

```
curl -X POST $OPENAI_BASE_URL/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "OpenAI-Project: proj_5d5ykleja6cwpirysbb7" \
  -d '{
    "model": "openai.gpt-oss-120b",
    "input": "Explain the benefits of using projects in Amazon Bedrock"
  }'
```

Python

```
from openai import OpenAI
client = OpenAI(project="proj_5d5ykleja6cwpirysbb7")
```

All inference requests made with this client will be associated with the specified project, ensuring proper isolation, cost tracking, and access control.

### Step 5: Verify Your Project Setup

List all projects to verify your project was created successfully:

```
curl -X GET $OPENAI_BASE_URL/organization/projects \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

Response:

```
{
  "data": [
    {
      "arn": "arn:aws:bedrock-mantle:ap-northeast-1:673693429514:project/default",
      "created_at": 1764460800,
      "id": "default",
      "name": "default",
      "object": "organization.project",
      "status": "active",
      "tags": {}
    },
    {
      "arn": "arn:aws:bedrock-mantle:ap-northeast-1:673693429514:project/proj_2z766pfxmkij5vwubv75",
      "created_at": 1771823259,
      "id": "proj_2z766pfxmkij5vwubv75",
      "name": "Project ABC",
      "object": "organization.project",
      "status": "active",
      "tags": {}
    }
  ],
  "first_id": "default",
  "has_more": false,
  "last_id": "proj_znaruqn723npmjqnxqfd",
  "object": "list"
}
```

### Next Steps

Now that you've created your first project, you can:

- **Configure access control**: Attach IAM policies to restrict project access
- **Set up cost tracking**: Add AWS tags for cost allocation
- **Enable monitoring**: Configure CloudWatch metrics and alarms
- **Create additional projects**: Organize workloads by team, environment, or application

## Working with Projects

This page provides detailed information about managing projects throughout their lifecycle.

### Creating Projects

#### Basic Project Creation

Create a project with a name, description, and tags:

```
curl -X POST $OPENAI_BASE_URL/organization/projects \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Development Environment",
    "tags": {
      "Project": "InternalTools",
      "Environment": "Development",
      "Owner": "TeamAlpha",
      "CostCenter": "30156"
    }
  }'
```

You can have up to 1000 projects per account.

#### Recommended Naming Conventions

Use clear, descriptive names that reflect your organizational structure:

- **By application**: CustomerChatbot-Prod, InternalSearch-Dev
- **By team**: TeamAlpha-Production, DataScience-Experiments
- **By environment**: Production-WebApp, Staging-MobileApp
- **By cost center**: CostCenter-2152-Production

### Listing Projects

#### List All Projects

Retrieve all projects in your account:

```
curl -X GET $OPENAI_BASE_URL/organization/projects \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

### Retrieving Project Details

Get detailed information about a specific project:

```
curl -X GET $OPENAI_BASE_URL/organization/projects/proj_5d5ykleja6cwpirysbb7 \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

### Updating Projects

Modify project properties such as name:

```
curl -X POST $OPENAI_BASE_URL/organization/projects/proj_5d5ykleja6cwpirysbb7 \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Production Chatbot v2"
  }'
```

### Managing Project Tags

Add new tags or update existing tag values:

```
curl -X POST $OPENAI_BASE_URL/organization/projects/proj_5d5ykleja6cwpirysbb7 \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "add_tags": {
      "Application": "WebApp",
      "Version": "2.0",
      "Team": "Engineering"
    }
  }'
```

Remove specific tags by their keys:

```
curl -X POST $OPENAI_BASE_URL/organization/projects/proj_5d5ykleja6cwpirysbb7 \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "remove_tag_keys": ["Version", "OldTagKey"]
  }'
```

###### Important Notes

- **No full replacement**: There is no operation to replace the entire tag set at once. You must explicitly specify which tags to add and which to remove.
- **Error handling**: Implement proper error handling and verification

### Archiving Projects

Archive projects that are no longer in use:

```
curl -X POST $OPENAI_BASE_URL/organization/projects/proj_abc123/archive \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json"
```

###### Important

Archived projects cannot be used for new inference requests, but historical data and metrics remain accessible for up to 30 days.

### Using Projects with Different APIs

Responses API

```
from openai import OpenAI

client = OpenAI(project="proj_abc123")

response = client.responses.create(
    model="openai.gpt-oss-120b",
    input="What are the key features of Amazon Bedrock?"
)
print(response)
```

Chat Completions API

```
from openai import OpenAI

client = OpenAI(project="proj_abc123")

response = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[
        {"role": "user", "content": "Explain how projects improve security"}
    ]
)

print(response.choices[0].message.content)
```

### Best Practices

#### Recommended Project Structure

**One project per application**: Create separate projects for each distinct application or service.

```
├── CustomerChatbot-Production
├── CustomerChatbot-Staging
├── CustomerChatbot-Development
├── InternalSearch-Production
└── InternalSearch-Development
```

- **Separate environments**: Use different projects for development, staging, and production environments.
- **Experiment isolation**: Create dedicated projects for experiments and proof-of-concepts.

#### Project Lifecycle Management

- **Create projects early**: Set up projects before deploying applications
- **Use consistent naming**: Follow organizational naming conventions
- **Document project purpose**: Include clear descriptions
- **Regular audits**: Periodically review and archive unused projects
- **Monitor usage**: Track project metrics to identify optimization opportunities
