# IAM behaviors for AWS Clean Rooms ML

## Cross-account jobs

Clean Rooms ML allows certain resources created by one AWS account to be securely accessed in their account by another AWS account. When a client in AWS account A calls `StartAudienceGenerationJob` on a `ConfiguredAudienceModel` resource owned by AWS account B, Clean Rooms ML creates two ARNs for the job. One ARN in AWS account A and another in AWS account B. The ARNs are identical except for their AWS account.

Clean Rooms ML creates two ARNs for the job to ensure that both accounts can apply their own IAM policies to the jobs. For example, both accounts can use tag-based access control and apply policies from their AWS organization. The job processes data from both accounts, so both accounts can delete the job and its associated data. Neither account can block the other account from deleting the job.

There is only one job execution and both accounts can see the job when they call
`ListAudienceGenerationJobs`. Both accounts can call the `Get`, `Delete`, and
`Export` APIs on the job using the ARN with their own AWS account ID.

Neither AWS account can access the job when using an ARN with the other AWS account ID.

The name of the job must be unique within an AWS account. The name in AWS account B is
`$accountA-$name`. The name chosen by AWS account A is prefixed with AWS account
A when the job is viewed in AWS account B.

In order for a cross-account `StartAudienceGenerationJob` to succeed, AWS account B must
allow that action on both the new job in AWS account B and the `ConfiguredAudienceModel` in
AWS account B using a resource policy similar to the following example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Clean-Rooms-CAMA-ID",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "`111122223333`"
 ]
 },
 "Action": [
 "cleanrooms-ml:StartAudienceGenerationJob"
 ],
 "Resource": [
 "arn:aws:cleanrooms-ml:`us-east-1`:`444455556666`:configured-audience-model/`id`",
 "arn:aws:cleanrooms-ml:`us-east-1`:`444455556666`:audience-generation-job/*"
 ],
 "Condition":{"StringEquals":{"cleanrooms-ml:CollaborationId":"`UUID`"}}
 }
 ]
}`

```

###### Note

This AWS Clean Rooms ML resource policy references two different AWS account IDs to
support cross-account audience generation:

- **111122223333** - This is the account that contains the principal (user, role, or service) authorized to start audience generation jobs. This
  account initiates the ML processing workflow.
- **444455556666** - This is the account that owns the AWS Clean Rooms ML
  resources (the configured audience model and audience generation jobs). This
  account hosts the ML models and manages the job execution.
  **Additional Configuration Notes:**

- **Statement ID (Sid)**: Replace `CAMA-ID` with your actual AWS Clean Rooms Audience
  Model Application (CAMA) identifier to make the policy statement easily
  identifiable.
- **Resource IDs**: Replace `id` with the actual ID of
  your configured audience model, and `UUID` with your
  specific collaboration ID.
- **Condition**: The `cleanrooms-ml:CollaborationId` condition ensures that
  audience generation jobs can only be started within the context of the specified
  AWS Clean Rooms collaboration, providing an additional security boundary.
  This cross-account configuration enables scenarios where one organization manages the ML models and infrastructure while allowing authorized partners to initiate audience generation processes within the bounds of their collaboration agreement.

If you use the [AWS Clean Rooms ML API](../../../cleanrooms-ml/latest/APIReference/Welcome.md "../../../cleanrooms-ml/latest/APIReference/Welcome.md") to create a configured lookalike model with `manageResourcePolicies`
set to true, AWS Clean Rooms creates this policy for you.

Additionally, the identity policy of the caller in AWS account A needs `StartAudienceGenerationJob` permission on `arn:aws:cleanrooms-ml:us-west-1:AccountA:audience-generation-job/*`. So there are three IAM Resources for Action `StartAudienceGenerationJob`: the AWS account A job, the AWS account B job, and the AWS account B `ConfiguredAudienceModel`.

###### Warning

The AWS account that started the job receives an AWS CloudTrail audit log event about the job. The
AWS account that owns the `ConfiguredAudienceModel` does not receive a AWS CloudTrail
audit log event.

## Tagging jobs

When you set the `childResourceTagOnCreatePolicy=FROM_PARENT_RESOURCE` parameter of
`CreateConfiguredAudienceModel`, all lookalike segment generation jobs within your account that are
created from that configured lookalike model default to having the same tags as the configured lookalike model.
The configured lookalike model is the parent and the lookalike segment generation job is the child.

If you are creating a job within your own account, the request tags of the job override the parent tags. Jobs created by other accounts never create tags in your account. If you set `childResourceTagOnCreatePolicy=FROM_PARENT_RESOURCE` and another account creates a job, there are two copies of the job. The copy in your account has the parent resource tags and the copy in the job submitter’s account has tags from the request.

## Validating collaborators

When granting permissions to other members of an AWS Clean Rooms collaboration, the resource policy should include
the condition key `cleanrooms-ml:CollaborationId`. This enforces that the
`collaborationId` parameter is included in the [StartAudienceGenerationJob](../../../cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.md "../../../cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.md")
request. When the `collaborationId` parameter is included in the request, Clean Rooms ML validates that the
collaboration exists, the job submitter is an active member of the collaboration, and the configured lookalike
model owner is an active member of the collaboration.

When AWS Clean Rooms manages your configured lookalike model resource policy (the `manageResourcePolicies` parameter is `TRUE` in [CreateConfiguredAudienceModelAssociation request](../apireference/API_CreateConfiguredAudienceModelAssociation.md "../apireference/API_CreateConfiguredAudienceModelAssociation.md")), this condition key will be set in the resource policy. Therefore, you must specify the `collaborationId` in [StartAudienceGenerationJob](../../../cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.md "../../../cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.md").

## Cross-account access

Only `StartAudienceGenerationJob` can be called across accounts. All other Clean Rooms ML APIs can only be used with resources in your own account. This ensures that your training data, lookalike model configuration, and other information stays private.

Clean Rooms ML never reveals Amazon S3 or AWS Glue locations across accounts. The training data location, configured
lookalike model output location, and lookalike segment generation job seed location are never visible across
accounts. Unless query logging is enabled in the collaboration, whether the seed data comes from an SQL query and the query itself are not visible across accounts. If you `Get` an audience generation job that another account submitted, the service does
not show the seed location.
