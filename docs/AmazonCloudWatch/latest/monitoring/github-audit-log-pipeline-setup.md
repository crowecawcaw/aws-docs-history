

# CloudWatch pipelines configuration for GitHub Audit Log
<a name="github-audit-log-pipeline-setup"></a>

**Note**  
 Important: GitHub Enterprise accounts are required to use this connector. GitHub Personal or Organization accounts are not supported. 

Collects audit log data from GitHub organizations or enterprises using personal access tokens or GitHub App authentication.

Configure the GitHub Audit Log source with the following parameters:

```
source:
  github_auditlog:
    scope: "ORGANIZATION"
    organization: "<example-org-name>"
    range: "P7D"
    authentication:
      personal_access_token: "${{aws_secrets:<secret-name>:token}}"
```Parameters

`scope` (required)  
Scope of audit logs to collect. Must be "ORGANIZATION" or "ENTERPRISE".

`organization` (required when scope is ORGANIZATION)  
GitHub organization name.

`enterprise` (required when scope is ENTERPRISE)  
GitHub enterprise name.

`authentication.personal_access_token` (required for PAT auth)  
Personal access token for GitHub API authentication.

`range` (optional)  
The time range for log collection. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for 21 hours). Default is 0 hours, and the maximum is 90 days.