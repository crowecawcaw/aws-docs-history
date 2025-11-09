# AWS Serverless Application Repository API Permissions: Actions and

Resources Reference

When you set up [access control](security-iam.md#security_iam_access-manage "security-iam.md#security_iam_access-manage") and write permissions
policies that you can attach to an IAM identity (identity-based policies), you can use the
following table as a reference. The table includes each
AWS Serverless Application Repository API operation, the corresponding actions that you can grant permissions to perform
the action, and the AWS resource that you can grant the permissions. You specify the actions
in the policy's `Action` field, and you specify the resource value in the
policy's `Resource` field.

To specify an action, use the `serverlessrepo:` prefix followed by the API
operation name (for example, `serverlessrepo:ListApplications`).

| Operation                                                                                                                      | URI                                                        | Method | AWS Resources (ARNs)                                                         |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- | ------ | ---------------------------------------------------------------------------- |
| **Operation:\*<br>• ListApplications<br>**Required Permissions:\*<br>• serverlessrepo:ListApplications                         | /applications                                              | GET    | \*                                                                           |
| **Operation:\*<br>• CreateApplication<br>**Required Permissions:\*<br>• serverlessrepo:CreateApplication                       | /applications                                              | POST   | \*                                                                           |
| **Operation:\*<br>• GetApplication<br>**Required Permissions:\*<br>• serverlessrepo:GetApplication                             | /applications/`application-id`                             | GET    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:\*<br>• DeleteApplication<br>**Required Permissions:\*<br>• serverlessrepo:DeleteApplication                       | /applications/`application-id`                             | DELETE | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:\*<br>• UpdateApplication<br>**Required Permissions:\*<br>• serverlessrepo:UpdateApplication                       | /applications/`application-id`                             | PATCH  | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>CreateCloudFormationChangeSet<br>\*_Required Permissions:_<br>• serverlessrepo:CreateCloudFormationChangeSet | /applications/`application-id`/changesets                  | POST   | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>GetApplicationPolicy<br>\*_Required Permissions:_<br>• serverlessrepo:GetApplicationPolicy                   | /applications/`application-id`/policy                      | GET    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>PutApplicationPolicy<br>\*_Required Permissions:_<br>• serverlessrepo:PutApplicationPolicy                   | /applications/`application-id`/policy                      | PUT    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>ListApplicationVersions<br>\*_Required Permissions:_<br>• serverlessrepo:ListApplicationVersions             | /applications/`application-id`/versions                    | GET    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>CreateApplicationVersion<br>\*_Required Permissions:_<br>• serverlessrepo:CreateApplicationVersion           | /applications/`application-id`/versions/`semantic-version` | PUT    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>ListApplicationDependencies<br>\*_Required Permissions:_<br>• serverlessrepo:ListApplicationDependencies     | /applications/`application-id`/dependencies                | GET    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:\*<br>• SearchApplications<br>**Required Permissions:\*<br>• serverlessrepo:SearchApplications                     | n/a                                                        | n/a    | \*                                                                           |
