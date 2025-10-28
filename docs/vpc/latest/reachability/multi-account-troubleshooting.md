# Troubleshoot cross-account analyses in

Reachability Analyzer

The following information can help you troubleshoot common issues with running
cross-account analyses in Reachability Analyzer.

###### Issues

- ["StackSet is not empty" or "StackSet already exists"](#stackset-not-empty "#stackset-not-empty")
- ["Error fetching resources"](#error-fetching-resources "#error-fetching-resources")
- ["Organizational unit not found in StackSet"](#organizational-unit-not-found "#organizational-unit-not-found")

## "StackSet is not empty" or "StackSet already exists"

If you receive one of these errors while enabling trusted access, do the following
to resolve the issue.

###### To resolve the issue

1. Choose **Turn off trusted access**.
2. Wait until you see a banner at the top of the screen indicating that the operation
   was successful.
3. Choose **Turn on trusted access**.

## "Error fetching resources"

If you receive this error while attempting to access resources from another
account in the organization, it usually indicates that your account doesn't
have all permissions required.

- Verify that you have permission to call the `AssumeRole` and
  `SetSourceIdentity` API actions. For example, the following policy
  grants permission to call these actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole",
 "sts:SetSourceIdentity"
 ],
 "Resource": "*"
 }
 ]
}`

```

- Verify that you have permission to call AWS CloudFormation API actions. For example, the
  [AWSCloudFormationFullAccess](../../../aws-managed-policy/latest/reference/AWSCloudFormationFullAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudFormationFullAccess.md") and [AWSCloudFormationReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSCloudFormationReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudFormationReadOnlyAccess.md") policies grant permissions to
  call these actions.
- Verify that you have permission to call AWS Organizations API actions. For example, the
  [AWSOrganizationsFullAccess](../../../aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.md "../../../aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.md") and [AWSOrganizationsReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSOrganizationsReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSOrganizationsReadOnlyAccess.md") policies grant permissions to
  call these actions.

## "Organizational unit not found in StackSet"

If you receive this error while disabling trusted access, do the following to
resolve the issue.

###### To resolve the issue

1. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. In the navigation pane, choose **StackSets**.
3. Select `ReachabilityAnalyzerCrossAccountResourceAccessStackSet`
   and then choose **Actions**, **Delete StackSet**.
4. Return to the Reachability Analyzer settings page and refresh the page.
5. Choose **Turn off trusted access**.
