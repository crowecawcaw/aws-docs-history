

# Source configuration for GitLab
<a name="gitlab-source-config"></a>

## Integrating with GitLab
<a name="gitlab-integration"></a>

CloudWatch Pipeline uses the GitLab REST API and GraphQL API to retrieve audit events, project activity, merge request data, group membership information, and vulnerability findings from your GitLab environment. The REST API exposes endpoints for fetching time-filtered event data for security monitoring and compliance analysis, while the GraphQL API is used to retrieve project vulnerability data.

To integrate CloudWatch Pipelines with GitLab, complete the following high-level steps:
+ Generate a Personal Access Token (PAT) in the GitLab Console.
+ Store the credentials in AWS Secrets Manager.
+ Create a CloudWatch pipeline with GitLab as the data source.
+ Verify that data is flowing into the pipeline.

## Prerequisites
<a name="gitlab-prerequisites"></a>

Before you begin, make sure you have the following:
+ An active GitLab (SaaS) account with Owner or Admin access
+ A GitLab Personal Access Token (PAT) with the `read_api` scope
+ An AWS account with permissions to create and manage CloudWatch Pipelines
+ An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager

## Authenticating with GitLab
<a name="gitlab-authentication"></a>

GitLab uses a Personal Access Token (PAT) for authentication. The pipeline passes the token through the `PRIVATE-TOKEN` header to authenticate each API request.

## Configure Authentication for GitLab
<a name="gitlab-configure-auth"></a>

To configure authentication credentials for the pipeline:

1. In the upper-right corner of GitLab, select your avatar.

1. Select **Edit profile**.

1. In the left sidebar, select **Access** > **Personal access tokens**.

1. From the **Generate token** dropdown, select **Legacy token**.

1. Enter a token name.

1. (Optional) Enter a token description.

1. Set an expiration date for the token.

1. Select `read_api` as the scope.

1. Select **Generate token**.

1. Save the token value.

1. Store the `pat_token` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline
<a name="gitlab-pipeline-config"></a>

To configure the pipeline, choose GitLab as the data source. Provide the Personal Access Token. After you create and activate the pipeline, audit and activity data from GitLab will begin flowing into the selected CloudWatch Logs log group.

The following optional parameters are available:
+ **Polling intervals** – `members_polling_interval` (default `P1D`), `vulnerabilities_polling_interval` (default `P1D`)
+ **Backfill durations** – `projects_backfill` (default `P180D`), `merge_requests_backfill` (default `P180D`), `group_audit_events_backfill` (default `P180D`), `project_audit_events_backfill` (default `P180D`)

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="gitlab-ocsf-support"></a>

This integration supports the following OCSF event classes:
+ **Vulnerability Finding [2002]** – Vulnerability Finding Activity
+ **Group Management [3006]** – Group Audit Event Activity
+ **User Inventory Info [5003]** – Member Activity
+ **Software Inventory Info [5020]** – Project Activity
+ **Web Resources Activity [6001]** – Merge Request Activity