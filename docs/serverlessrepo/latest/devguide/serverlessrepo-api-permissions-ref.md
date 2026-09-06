

# AWS Serverless Application Repository API Permissions: Actions and Resources Reference
<a name="serverlessrepo-api-permissions-ref"></a>

When you set up [access control](security-iam.md#security_iam_access-manage) and write permissions policies that you can attach to an IAM identity (identity-based policies), you can use the following table as a reference. The table includes each AWS Serverless Application Repository API operation, the corresponding actions that you can grant permissions to perform the action, and the AWS resource that you can grant the permissions. You specify the actions in the policy's `Action` field, and you specify the resource value in the policy's `Resource` field. 

To specify an action, use the `serverlessrepo:` prefix followed by the API operation name (for example, `serverlessrepo:ListApplications`).


| Operation | URI | Method | AWS Resources (ARNs) | 
| --- | --- | --- | --- | 
| **Operation:** ListApplications<br />**Required Permissions: **serverlessrepo:ListApplications | /applications | GET | \* | 
| **Operation:** CreateApplication<br />**Required Permissions: **serverlessrepo:CreateApplication | /applications | POST | \* | 
| **Operation:** GetApplication<br />**Required Permissions: **serverlessrepo:GetApplication | /applications/{{application-id}} | GET | arn:aws:serverlessrepo:{{region}}:{{account-id}}:applications/{{application-name}} | 
| **Operation:** DeleteApplication<br />**Required Permissions: **serverlessrepo:DeleteApplication | /applications/{{application-id}} | DELETE | arn:aws:serverlessrepo:{{region}}:{{account-id}}:applications/{{application-name}} | 
| **Operation:** UpdateApplication<br />**Required Permissions: **serverlessrepo:UpdateApplication | /applications/{{application-id}} | PATCH | arn:aws:serverlessrepo:{{region}}:{{account-id}}:applications/{{application-name}} | 
| **Operation:** CreateCloudFormationChangeSet<br />**Required Permissions: **serverlessrepo:CreateCloudFormationChangeSet | /applications/{{application-id}}/changesets | POST | arn:aws:serverlessrepo:{{region}}:{{account-id}}:applications/{{application-name}} | 
| **Operation:** GetApplicationPolicy<br />**Required Permissions: **serverlessrepo:GetApplicationPolicy | /applications/{{application-id}}/policy | GET | arn:aws:serverlessrepo:{{region}}:{{account-id}}:applications/{{application-name}} | 
| **Operation:** PutApplicationPolicy<br />**Required Permissions: **serverlessrepo:PutApplicationPolicy | /applications/{{application-id}}/policy | PUT | arn:aws:serverlessrepo:{{region}}:{{account-id}}:applications/{{application-name}} | 
| **Operation:** ListApplicationVersions<br />**Required Permissions: **serverlessrepo:ListApplicationVersions | /applications/{{application-id}}/versions | GET | arn:aws:serverlessrepo:{{region}}:{{account-id}}:applications/{{application-name}} | 
| **Operation:** CreateApplicationVersion<br />**Required Permissions: **serverlessrepo:CreateApplicationVersion | /applications/{{application-id}}/versions/{{semantic-version}} | PUT | arn:aws:serverlessrepo:{{region}}:{{account-id}}:applications/{{application-name}} | 
| **Operation:** ListApplicationDependencies<br />**Required Permissions: **serverlessrepo:ListApplicationDependencies | /applications/{{application-id}}/dependencies | GET | arn:aws:serverlessrepo:{{region}}:{{account-id}}:applications/{{application-name}} | 
| **Operation:** SearchApplications<br />**Required Permissions: **serverlessrepo:SearchApplications | n/a | n/a | \* | 