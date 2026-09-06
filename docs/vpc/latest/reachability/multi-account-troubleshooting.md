

# Troubleshoot cross-account analyses in Reachability Analyzer
<a name="multi-account-troubleshooting"></a>

The following information can help you troubleshoot common issues with running cross-account analyses in Reachability Analyzer.

**Topics**
+ ["StackSet is not empty" or "StackSet already exists"](#stackset-not-empty)
+ ["Error fetching resources"](#error-fetching-resources)
+ ["Organizational unit not found in StackSet"](#organizational-unit-not-found)

## "StackSet is not empty" or "StackSet already exists"
<a name="stackset-not-empty"></a>

If you receive one of these errors while enabling trusted access, do the following to resolve the issue.

**To resolve the issue**

1. Choose **Turn off trusted access**.

1. Wait until you see a banner at the top of the screen indicating that the operation was successful.

1. Choose **Turn on trusted access**.

## "Error fetching resources"
<a name="error-fetching-resources"></a>

If you receive this error while attempting to access resources from another account in the organization, it usually indicates that your account doesn't have all permissions required.
+ Verify that you have permission to call the `AssumeRole` and `SetSourceIdentity` API actions. For example, the following policy grants permission to call these actions.

------
#### [ JSON ]

****  

  ```
  {
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
  }
  ```

------
+ Verify that you have permission to call CloudFormation API actions. For example, the [AWSCloudFormationFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudFormationFullAccess.html) and [AWSCloudFormationReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudFormationReadOnlyAccess.html) policies grant permissions to call these actions.
+ Verify that you have permission to call AWS Organizations API actions. For example, the [AWSOrganizationsFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.html) and [AWSOrganizationsReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSOrganizationsReadOnlyAccess.html) policies grant permissions to call these actions.

## "Organizational unit not found in StackSet"
<a name="organizational-unit-not-found"></a>

If you receive this error while disabling trusted access, do the following to resolve the issue.

**To resolve the issue**

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. In the navigation pane, choose **StackSets**.

1. Select `ReachabilityAnalyzerCrossAccountResourceAccessStackSet` and then choose **Actions**, **Delete StackSet**.

1. Return to the Reachability Analyzer settings page and refresh the page.

1. Choose **Turn off trusted access**.