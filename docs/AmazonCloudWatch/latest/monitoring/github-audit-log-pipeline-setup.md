# CloudWatch pipelines configuration for GitHub Audit Log

###### Note

Important: GitHub Enterprise accounts are required to use this connector. GitHub Personal or Organization accounts are not supported.

Collects audit log data from GitHub organizations or enterprises using
personal access tokens or GitHub App authentication.

Configure the GitHub Audit Log source with the following parameters:

```
source:
  github_auditlog:
    scope: "ORGANIZATION"
    organization: "<example-org-name>"
    authentication:
      personal_access_token: "${{aws_secrets:<secret-name>:token}}"
```

###### Parameters

`scope` (required)

Scope of audit logs to collect. Must be "ORGANIZATION" or
"ENTERPRISE".

`organization` (required when scope is ORGANIZATION)

GitHub organization name.

`enterprise` (required when scope is ENTERPRISE)

GitHub enterprise name.

`authentication.personal_access_token` (required for PAT
auth)

Personal access token for GitHub API authentication.
