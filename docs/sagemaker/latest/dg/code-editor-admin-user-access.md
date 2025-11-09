# Give your users access to private

spaces

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

This section provides a policy that grants user access to private spaces. You can also
use the policy to restrict private spaces and applications that are associated with them to
the owner associated with the user profile.

You must provide your users with permissions to the following:

- Private spaces
- The user profile required for access to the private spaces
  To provide permissions, attach the following policy to the IAM roles of your
  users.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {

 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateApp",
 "sagemaker:DeleteApp"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:app/*",
 "Condition": {
 "Null": {
 "sagemaker:OwnerUserProfileArn": "true"
 }
 }
 },
 {
 "Sid": "SMStudioCreatePresignedDomainUrlForUserProfile",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreatePresignedDomainUrl"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:user-profile/`domain-id`/`user-profile-name`"
 },
 {
 "Sid": "SMStudioAppPermissionsListAndDescribe",
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListApps",
 "sagemaker:ListDomains",
 "sagemaker:ListUserProfiles",
 "sagemaker:ListSpaces",
 "sagemaker:DescribeApp",
 "sagemaker:DescribeDomain",
 "sagemaker:DescribeUserProfile",
 "sagemaker:DescribeSpace"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SMStudioAppPermissionsTagOnCreate",
 "Effect": "Allow",
 "Action": [
 "sagemaker:AddTags"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:*/*",
 "Condition": {
 "Null": {
 "sagemaker:TaggingAction": "false"
 }
 }
 },
 {
 "Sid": "SMStudioRestrictSharedSpacesWithoutOwners",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateSpace",
 "sagemaker:UpdateSpace",
 "sagemaker:DeleteSpace"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:space/`domain-id`/*",
 "Condition": {
 "Null": {
 "sagemaker:OwnerUserProfileArn": "true"
 }
 }
 },
 {
 "Sid": "SMStudioRestrictSpacesToOwnerUserProfile",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateSpace",
 "sagemaker:UpdateSpace",
 "sagemaker:DeleteSpace"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:space/`domain-id`/*",
 "Condition": {
 "ArnLike": {
 "sagemaker:OwnerUserProfileArn": "arn:aws:sagemaker:`us-east-1`:`111122223333`:user-profile/`domain-id`/`user-profile-name`"
 },
 "StringEquals": {
 "sagemaker:SpaceSharingType": [
 "Private",
 "Shared"
 ]
 }
 }
 },
 {
 "Sid": "SMStudioRestrictCreatePrivateSpaceAppsToOwnerUserProfile",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateApp",
 "sagemaker:DeleteApp"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:app/`domain-id`/*",
 "Condition": {
 "ArnLike": {
 "sagemaker:OwnerUserProfileArn": "arn:aws:sagemaker:`us-east-1`:`111122223333`:user-profile/`domain-id`/`user-profile-name`"
 },
 "StringEquals": {
 "sagemaker:SpaceSharingType": [
 "Private"
 ]
 }
 }
 }
 ]
}`

```
