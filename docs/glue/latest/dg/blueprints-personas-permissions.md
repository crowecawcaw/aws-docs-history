# Permissions for personas and roles for

AWS Glue blueprints

The following are the typical personas and suggested AWS Identity and Access Management (IAM) permissions
policies for personas and roles for AWS Glue blueprints.

###### Topics

- [Blueprint personas](#blueprints-personas "#blueprints-personas")
- [Permissions for blueprint personas](#blueprints-permssions "#blueprints-permssions")
- [Permissions for blueprint
  roles](#blueprints-role-permissions "#blueprints-role-permissions")

## Blueprint personas

The following are the personas typically involved in the lifecycle of AWS Glue
blueprints.

| Persona                | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| AWS Glue developer     | Develops, tests, and publishes blueprints.                  |
| AWS Glue administrator | Registers, maintains, and grants permissions on blueprints. |
| Data analyst           | Runs blueprints to create workflows.                        |

For more information, see [Overview of blueprints in AWS Glue](blueprints-overview.md "blueprints-overview.md").

## Permissions for blueprint personas

The following are the suggested permissions for each blueprint persona.

### AWS Glue developer permissions for

blueprints

The AWS Glue developer must have write permissions on the Amazon S3 bucket that is used to
publish the blueprint. Often, the developer registers the blueprint after
uploading it. In that case, the developer needs the permissions listed in [AWS Glue administrator permissions for
blueprints](#bp-persona-admin "#bp-persona-admin"). Additionally, if the developer wishes to test the blueprint after its registered, he or she also needs the permissions listed in [Data analyst permissions for
blueprints](#bp-persona-analyst "#bp-persona-analyst").

### AWS Glue administrator permissions for

blueprints

The following policy grants permissions to register, view, and maintain AWS Glue
blueprints.

###### Important

In the following policy, replace
`<s3-bucket-name>` and
`<prefix>` with the Amazon S3 path to uploaded
blueprint ZIP archives to register.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateBlueprint",
 "glue:UpdateBlueprint",
 "glue:DeleteBlueprint",
 "glue:GetBlueprint",
 "glue:ListBlueprints",
 "glue:BatchGetBlueprints"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`prefix`/*"
 }
 ]
}`

```

### Data analyst permissions for

blueprints

The following policy grants permissions to run blueprints and to view
the resulting workflow and workflow components. It also grants `PassRole`
on the role that AWS Glue assumes to create the workflow and workflow
components.

The policy grants permissions on any resource. If you want to configure
fine-grained access to individual blueprints, use the following format for
blueprint ARNs:

```
arn:aws:glue:`<region>`:`<account-id>`:blueprint/`<blueprint-name>`
```

###### Important

In the following policy, replace `<account-id>`
with a valid AWS account and replace `<role-name>`
with the name of the role used to run a blueprint. See [Permissions for blueprint
roles](#blueprints-role-permissions "#blueprints-role-permissions") for the permissions that this role
requires.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:ListBlueprints",
 "glue:GetBlueprint",
 "glue:StartBlueprintRun",
 "glue:GetBlueprintRun",
 "glue:GetBlueprintRuns",
 "glue:GetCrawler",
 "glue:ListTriggers",
 "glue:ListJobs",
 "glue:BatchGetCrawlers",
 "glue:GetTrigger",
 "glue:BatchGetWorkflows",
 "glue:BatchGetTriggers",
 "glue:BatchGetJobs",
 "glue:BatchGetBlueprints",
 "glue:GetWorkflowRun",
 "glue:GetWorkflowRuns",
 "glue:ListCrawlers",
 "glue:ListWorkflows",
 "glue:GetJob",
 "glue:GetWorkflow",
 "glue:StartWorkflowRun"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`role-name`"
 }
 ]
}`

```

## Permissions for blueprint

roles

The following are the suggested permissions for the IAM role used to create a
workflow from a blueprint. The role has to have a trust relationship with
`glue.amazonaws.com`.

###### Important

In the following policy, replace `<account-id>` with a
valid AWS account, and replace `<role-name>` with the
name of the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateJob",
 "glue:GetCrawler",
 "glue:GetTrigger",
 "glue:DeleteCrawler",
 "glue:CreateTrigger",
 "glue:DeleteTrigger",
 "glue:DeleteJob",
 "glue:CreateWorkflow",
 "glue:DeleteWorkflow",
 "glue:GetJob",
 "glue:GetWorkflow",
 "glue:CreateCrawler"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`role-name`"
 }
 ]
}`

```

###### Note

If the jobs and crawlers in the workflow assume a role other than this role, this
policy must include the `iam:PassRole` permission on that other role
instead of on the blueprint role.
