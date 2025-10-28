# IAM behaviors for Clean Rooms ML Custom Models

## Cross-account jobs

Clean Rooms ML allows certain resources associated with a collaboration created by one AWS account to be securely accessed in their account by another AWS account. A client in AWS account A with the member ability to run queries can call `CreateTrainedModel`, `CreateMLInputChannel`, or `StartTrainedModelInferenceJob` on a `ConfiguredModelAlgorithmAssociation` resource owned by another member in the collaboration, provided the `ConfiguredModelAlgorithmAssociation` is allowed by the custom analysis rule created with `CreateConfiguredTableAnalysisRule`.

Additionally, any active member of a collaboration can delete data associated with a trained model or ML input channel via the `DeleteTrainedModelOutput` and `DeleteMLInputChannelData` APIs.

## Cross-account access

Clean Rooms ML allows users to retrieve metadata about resources created by other accounts via the `GetCollaboration` and `ListCollaboration` APIs. Clean Rooms ML does not reveal KMS key ARNs, tags, environment variables, or hyperparameters (for the `TrainedModel` action) to other accounts.

## Membership and collaboration access

When accessing membership and collaboration resources in context of Clean Rooms ML custom models, a user’s identity policy needs permissions to the actions `cleanrooms:PassMembership`, `cleanrooms:PassCollaboration`, or both. All APIs that accept `membershipId` need the `cleanrooms:PassMembership` permission, and all APIs that accept `collaborationId` need the `cleanrooms:PassCollaboration` permission. A sample identity policy for a role that can call `createTrainedModel` in the context of a membership ID that can call `GetCollaborationTrainedModel` in the context of a collaboration ID are provided.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCleanroomsMLActions",
 "Effect": "Allow",
 "Action": [
 "cleanrooms:PassCollaboration",
 "cleanrooms:PassMembership"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowMembershipAccess",
 "Effect": "Allow",
 "Action": [
 "cleanrooms:GetMembership"
 ],
 "Resource": [
 "arn:aws:cleanrooms:`us-east-1`:`111122223333`:membership/`memberId`"
 ]
 },
 {
 "Sid": "AllowCollaborationAccess",
 "Effect": "Allow",
 "Action": [
 "cleanrooms:GetCollaboration"
 ],
 "Resource": [
 "arn:aws:cleanrooms:`us-east-1`:`111122223333`:collaboration/`collaborationId`"
 ]
 }
 ]
}`

```
