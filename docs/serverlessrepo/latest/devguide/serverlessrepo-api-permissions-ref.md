# AWS Serverless Application Repository API Permissions: Actions and Resources Reference

When you set up [access control](security-iam.md#security_iam_access-manage "security-iam.md#security_iam_access-manage") and write permissions
policies that you can attach to an IAM identity (identity-based policies), you can use the
following table as a reference. The table includes each
AWS Serverless Application Repository API operation, the corresponding actions that you can grant permissions to perform
the action, and the AWS resource that you can grant the permissions. You specify the actions
in the policy's `Action` field, and you specify the resource value in the
policy's `Resource` field.

To specify an action, use the `serverlessrepo:` prefix followed by the API
operation name (for example, `serverlessrepo:ListApplications`).

| Operation                                                                                                                     | URI                                                        | Method | AWS Resources (ARNs)                                                         |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------ | ---------------------------------------------------------------------------- |
| **Operation:_<br>• ListApplications<br>**Required Permissions:_<br>• serverlessrepo:ListApplications                          | /applications                                              | GET    | \*                                                                           |
| **Operation:_<br>• CreateApplication<br>**Required Permissions:_<br>• serverlessrepo:CreateApplication                        | /applications                                              | POST   | \*                                                                           |
| **Operation:_<br>• GetApplication<br>**Required Permissions:_<br>• serverlessrepo:GetApplication                              | /applications/`application-id`                             | GET    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:_<br>• DeleteApplication<br>**Required Permissions:_<br>• serverlessrepo:DeleteApplication                        | /applications/`application-id`                             | DELETE | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:_<br>• UpdateApplication<br>**Required Permissions:_<br>• serverlessrepo:UpdateApplication                        | /applications/`application-id`                             | PATCH  | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>CreateCloudFormationChangeSet<br>**Required Permissions:*<br>• serverlessrepo:CreateCloudFormationChangeSet | /applications/`application-id`/changesets                  | POST   | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>GetApplicationPolicy<br>**Required Permissions:*<br>• serverlessrepo:GetApplicationPolicy                   | /applications/`application-id`/policy                      | GET    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>PutApplicationPolicy<br>**Required Permissions:*<br>• serverlessrepo:PutApplicationPolicy                   | /applications/`application-id`/policy                      | PUT    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>ListApplicationVersions<br>**Required Permissions:*<br>• serverlessrepo:ListApplicationVersions             | /applications/`application-id`/versions                    | GET    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>CreateApplicationVersion<br>**Required Permissions:*<br>• serverlessrepo:CreateApplicationVersion           | /applications/`application-id`/versions/`semantic-version` | PUT    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:**<br>ListApplicationDependencies<br>**Required Permissions:*<br>• serverlessrepo:ListApplicationDependencies     | /applications/`application-id`/dependencies                | GET    | arn:aws:serverlessrepo:`region`:`account-id`:applications/`application-name` |
| **Operation:_<br>• SearchApplications<br>**Required Permissions:_<br>• serverlessrepo:SearchApplications                      | n/a                                                        | n/a    | \*                                                                           |
