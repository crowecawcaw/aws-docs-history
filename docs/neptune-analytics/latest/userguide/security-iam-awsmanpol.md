

# AWS managed policies for Neptune Analytics
<a name="security-iam-awsmanpol"></a>

AWS provides the following managed IAM policies for Neptune Analytics:
+ **NeptuneGraphReadOnlyAccess** — Grants read-only access to Neptune Analytics graph resources, including actions such as `neptune-graph:Get*`, `neptune-graph:List*`, and `neptune-graph:Read*`. Use this policy for users who need to view Neptune Analytics graph configurations without making changes.
+ **AWSServiceRoleForNeptuneGraphPolicy** — Used by the Neptune Analytics service-linked role to publish CloudWatch metrics and logs on behalf of your graphs. You do not attach this policy to users directly.