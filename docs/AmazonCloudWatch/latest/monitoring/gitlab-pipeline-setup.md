

# CloudWatch pipelines configuration for GitLab
<a name="gitlab-pipeline-setup"></a>

Collects log data from GitLab using Personal Access Token authentication through the GitLab REST API and GraphQL API.

Configure the GitLab source with the following parameters:

```
source:
  gitlab:
    authentication:
      personal_access_token: "${{aws_secrets:gitlab-account-credentials:pat_token}}"
    range: "P30D"
```Parameters

`authentication.personal_access_token` (required)  
The GitLab Personal Access Token with `read_api` scope, stored in AWS Secrets Manager.

`range` (optional)  
The historical time period for backfilling data. Uses ISO 8601 duration format. Minimum is `PT1H`, maximum is `P180D`. Default is `P180D`.