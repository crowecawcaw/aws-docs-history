# Getting started with MCP

Every Data Transformation Agent API is available as an MCP tool, so you can author profiles, run test
conversions, and debug failures from an MCP-compatible AI agent without leaving your IDE.

## Prerequisites

- An MCP-compatible client (such as Kiro or Cursor).
- AWS credentials configured with the Data Transformation Agent IAM permissions from [Setting up](data-transformation-setting-up.md "data-transformation-setting-up.md").

## Step 1: Install and configure the AWS MCP server

Install the AWS MCP server in your preferred agentic tool (such as Kiro or Cursor)
and configure it with your AWS credentials and Region. For installation and
configuration instructions, see the [AWS MCP server documentation](https://github.com/awslabs/mcp "https://github.com/awslabs/mcp").

## Step 2: Verify the tools are available

After setup, the Data Transformation Agent operations appear as callable tools in your agent. The tool
names map directly to the API operations:

| Tool name                        | What it does                                        |
| -------------------------------- | --------------------------------------------------- |
| CreateDataTransformationProfile  | Creates a profile in DRAFT state                    |
| UpdateProfileWithAgent           | Sends a message to the AI agent to edit a profile   |
| PublishDataTransformationProfile | Publishes the current draft as an immutable version |
| GetDataTransformationProfile     | Retrieves profile metadata and content              |
| StartDataTransformationJob       | Starts a bulk conversion job                        |
| DescribeDataTransformationJob    | Checks job status and progress                      |
| DeleteDataTransformationProfile  | Deletes profile metadata and content                |
| ListDataTransformationProfiles   | Lists profiles in your account                      |
| ListDataTransformationJobs       | Lists transformation jobs                           |

###### Note

The sync conversion operation (TransformData) is REST-only and may not appear as
an MCP tool. Your agent can construct and execute the REST call on your behalf
: see Step 3: Test with sync conversion for the request format.

## Step 3: Use the tools in natural language

Once connected, drive the full profile lifecycle by talking to your own agent, which
interacts with Data Transformation Agent via MCP:

- “Create a C-CDA profile from the AWS Starter Profile called
  'Cardiology Profile'.” → The agent calls
  CreateDataTransformationProfile and returns the profile ID.
- “Add a mapping for the Medication section.” → The agent calls
  UpdateProfileWithAgent, shows the proposed change, and asks for confirmation.
- “Publish the profile and start a bulk job against
  s3://my-bucket/ccda-files/” → The agent calls
  PublishDataTransformationProfile then StartDataTransformationJob.
- “What's the status of my last job?” → The agent calls
  DescribeDataTransformationJob and reports progress.
- “12 records failed: what happened?” → The agent
  inspects the errors and proposes a profile fix.

Sessions maintain context across multiple turns, so the agent remembers your profile,
conversation, and prior instructions throughout the workflow.

## Troubleshooting

| Symptom                             | Fix                                                                                                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tools don't appear after setup      | Verify the AWS MCP server is running and configured for the correct Region. Restart your MCP client.                                                               |
| AccessDeniedException on tool calls | Add the healthlake:\*DataTransformation\<br>• actions to your IAM policy. See [Setting up](data-transformation-setting-up.md "data-transformation-setting-up.md"). |
| ResourceNotFoundException           | Ensure the Region in your MCP server config matches the Region where your profiles exist.                                                                          |
