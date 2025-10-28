# Examples of using Amazon Rekognition identity-based

policy examples

By default, users and roles don't have permission to create or modify
Amazon Rekognition resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the users or groups that require
those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Example Amazon Rekognition Custom Labels policies](#security_iam_id-based-policy-examples-custom-labels "#security_iam_id-based-policy-examples-custom-labels")
- [Example 1: Allow a user read-only access to resources](#security_iam_id-based-policy-examples-read-only "#security_iam_id-based-policy-examples-read-only")
- [Example 2: Allow a user full access to resources](#security_iam_id-based-policy-examples-full-acess "#security_iam_id-based-policy-examples-full-acess")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")

## Example Amazon Rekognition Custom Labels policies

You can create identity-based policies for Amazon Rekognition Custom Labels. For more information, see
[Security](../customlabels-dg/sc-introduction.md "../customlabels-dg/sc-introduction.md").

## Example 1: Allow a user read-only access to resources

The following example grants read-only access to Amazon Rekognition resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rekognition:CompareFaces",
 "rekognition:DetectFaces",
 "rekognition:DetectLabels",
 "rekognition:ListCollections",
 "rekognition:ListFaces",
 "rekognition:SearchFaces",
 "rekognition:SearchFacesByImage",
 "rekognition:DetectText",
 "rekognition:GetCelebrityInfo",
 "rekognition:RecognizeCelebrities",
 "rekognition:DetectModerationLabels",
 "rekognition:GetLabelDetection",
 "rekognition:GetFaceDetection",
 "rekognition:GetContentModeration",
 "rekognition:GetPersonTracking",
 "rekognition:GetCelebrityRecognition",
 "rekognition:GetFaceSearch",
 "rekognition:GetTextDetection",
 "rekognition:GetSegmentDetection",
 "rekognition:DescribeStreamProcessor",
 "rekognition:ListStreamProcessors",
 "rekognition:DescribeProjects",
 "rekognition:DescribeProjectVersions",
 "rekognition:DetectCustomLabels",
 "rekognition:DetectProtectiveEquipment",
 "rekognition:ListTagsForResource",
 "rekognition:ListDatasetEntries",
 "rekognition:ListDatasetLabels",
 "rekognition:DescribeDataset"

 ],
 "Resource": "*"
 }
 ]
}`

```

## Example 2: Allow a user full access to resources

The following example grants full access to Amazon Rekognition resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rekognition:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users

to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```
