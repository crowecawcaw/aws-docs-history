# Source configuration for GitLab

## Integrating with GitLab

CloudWatch Pipeline uses the GitLab REST API and GraphQL API to retrieve audit events, project activity, merge request data, group membership information, and vulnerability findings from your GitLab environment. The REST API exposes endpoints for fetching time-filtered event data for security monitoring and compliance analysis, while the GraphQL API is used to retrieve project vulnerability data.

To integrate CloudWatch Pipelines with GitLab, complete the following high-level steps:

- Generate a Personal Access Token (PAT) in the GitLab Console.
- Store the credentials in AWS Secrets Manager.
- Create a CloudWatch pipeline with GitLab as the data source.
- Verify that data is flowing into the pipeline.

## Prerequisites

Before you begin, make sure you have the following:

- An active GitLab (SaaS) account with Owner or Admin access
- A GitLab Personal Access Token (PAT) with the `read_api` scope
- An AWS account with permissions to create and manage CloudWatch Pipelines
- An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager

## Authenticating with GitLab

GitLab uses a Personal Access Token (PAT) for authentication. The pipeline passes the token through the `PRIVATE-TOKEN` header to authenticate each API request.

## Configure Authentication for GitLab

To configure authentication credentials for the pipeline:

1. In the upper-right corner of GitLab, select your avatar.
2. Select **Edit profile**.
3. In the left sidebar, select **Access** > **Personal access tokens**.
4. From the **Generate token** dropdown, select **Legacy token**.
5. Enter a token name.
6. (Optional) Enter a token description.
7. Set an expiration date for the token.
8. Select `read_api` as the scope.
9. Select **Generate token**.
10. Save the token value.
11. Store the `pat_token` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline

To configure the pipeline, choose GitLab as the data source. Provide the Personal Access Token. After you create and activate the pipeline, audit and activity data from GitLab will begin flowing into the selected CloudWatch Logs log group.

The following optional parameters are available:

- **Polling intervals** – `members_polling_interval` (default `P1D`), `vulnerabilities_polling_interval` (default `P1D`)
- **Backfill durations** – `projects_backfill` (default `P180D`), `merge_requests_backfill` (default `P180D`), `group_audit_events_backfill` (default `P180D`), `project_audit_events_backfill` (default `P180D`)

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports the following OCSF event classes:

- **Vulnerability Finding [2002]** – Vulnerability Finding Activity
- **Group Management [3006]** – Group Audit Event Activity
- **User Inventory Info [5003]** – Member Activity
- **Software Inventory Info [5020]** – Project Activity
- **Web Resources Activity [6001]** – Merge Request Activity
