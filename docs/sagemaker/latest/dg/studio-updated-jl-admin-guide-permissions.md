# Give your users access to

spaces

To give users access to private or shared spaces, you must attach a permissions policy
to their IAM roles. You can also use the permissions policy to restrict private spaces
and their associated applications to a specific user profile.

The following permissions policy grants access to private and shared spaces. This
allows users to create their own space and list other spaces within their domain. A
user with this policy can't access the private space of a different user. For
information about Studio spaces, see [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md").

The policy provides users with permissions to the following:

- Private spaces or shared spaces.
- A user profile for accessing those spaces.
  To provide permissions, you can scope down the permissions of the following policy and
  add it to the IAM roles of your users. You can also use this policy to restrict your
  spaces, and their associated applications, to a specific user profile.

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
 "Resource": "arn:aws:sagemaker:`us-east-2`:`111122223333`:app/*",
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
 "Resource": "arn:aws:sagemaker:`us-east-2`:`111122223333`:user-profile/`sagemaker:DomainId`/`sagemaker:UserProfileName`"
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
 "Resource": "arn:aws:sagemaker:`us-east-2`:`111122223333`:*/*",
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
 "Resource": "arn:aws:sagemaker:`us-east-2`:`111122223333`:space/`sagemaker:DomainId`/*",
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
 "Resource": "arn:aws:sagemaker:`us-east-2`:`111122223333`:space/`sagemaker:DomainId`/*",
 "Condition": {
 "ArnLike": {
 "sagemaker:OwnerUserProfileArn": "arn:aws:sagemaker:`us-east-2`:`111122223333`:user-profile/`sagemaker:DomainId`/`sagemaker:UserProfileName`"
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
 "Resource": "arn:aws:sagemaker:`us-east-2`:`111122223333`:app/`sagemaker:DomainId`/*",
 "Condition": {
 "ArnLike": {
 "sagemaker:OwnerUserProfileArn": "arn:aws:sagemaker:us-east-2:111122223333:user-profile/`sagemaker:DomainId`/`sagemaker:UserProfileName`"
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
