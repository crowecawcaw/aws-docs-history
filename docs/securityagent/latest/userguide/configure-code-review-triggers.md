

# Configure pull request code review triggers
<a name="configure-code-review-triggers"></a>

Configure when AWS Security Agent reviews pull requests and merge requests in connected repositories. By default, AWS Security Agent reviews a pull request when it’s ready for review and doesn’t review draft pull requests. Use trigger filters to limit reviews by target branch or label, to review draft pull requests, or to start a review when a label is added.

Trigger filters apply only to repositories where you turn on **Code review comments**. AWS Security Agent checks each filter group on its own. A pull request starts a review if it meets every condition in at least one group.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, make sure that you have:
+ An Agent Space. For more information, see [Create an Agent Space](create-agent-space.md).
+ A connected repository. For more information, see [Connect integrations](admin-integrations.md).
+ Code review enabled for the repository. For more information, see [Enable code review](enable-code-review-scan.md).
+ Permission to edit the repository’s connected integration settings in AWS Security Agent.

## Configure trigger filters
<a name="_configure_trigger_filters"></a>

1. In the AWS Security Agent console, select your Agent Space. Then select the **Code review** tab, and choose **Edit configuration**.

1. In **Connected integrations**, edit the repositories that you want to configure.

1. On the **Manage capabilities** step, turn on **Code review comments** for each repository that you want AWS Security Agent to review.

1. Expand **Code review comments trigger filters**. In the section for the repository, choose **Add filter group**.

1. Configure the group. Each group needs trigger events, conditions, or both.
   + For **Trigger events (optional)**, choose the events that start a review.
   + For **Conditions (optional)**, choose **Add condition**, and then choose **Target branches** or **Labels**. Choose **Include matches** or **Exclude matches**. Then enter a name or RE2 regular expression, and choose **Add**. Repeat to add more patterns.

1. (Optional) To also review pull requests that meet other criteria, add another filter group. You can add up to five groups for each repository.

1. Choose **Save**.

A group without trigger events applies when a pull request is opened, updated, or marked ready for review, including draft pull requests. A group without conditions applies to all branches and labels. A pull request must meet every condition in a group. **Include matches** is met when any pattern matches, and **Exclude matches** is met when no pattern matches.

**Filter groups replace the default trigger**  
When a repository has filter groups, AWS Security Agent reviews a pull request only if it matches one of them. A group without trigger events also reviews draft pull requests. To limit reviews by branch without reviewing drafts, choose **Pull request ready for review** for **Trigger events (optional)**.

You can also configure trigger filters with the `triggerFilterGroups` capability in the [UpdateIntegratedResources](https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateIntegratedResources.html) API operation.

## Filter patterns
<a name="_filter_patterns"></a>

Patterns are RE2 regular expressions, not wildcards, and each pattern must match the complete branch or label name. You can add up to 20 patterns to a condition, and the conditions in all of a repository’s groups can contain up to 100 patterns in total. Each pattern can contain up to 256 characters. RE2 doesn’t support lookarounds or backreferences.

The following table shows example patterns.


| Pattern | Matches | 
| --- | --- | 
|  `main`  | Only `main`  | 
|  `release/.*`  | Branches that start with `release/`, such as `release/1.0`  | 
|  `main\|develop`  |  `main` and `develop`  | 
|  `release/*`  | Only `release` and `release/`, because `*` repeats the preceding `/`  | 
|  `security-.*`  | Labels that start with `security-`, such as `security-review`  | 

## Review pull requests based on labels
<a name="_review_pull_requests_based_on_labels"></a>

For GitHub and GitLab, a **Labels** condition matches the labels currently on the pull request. A group that reviews new pull requests also reviews one that is opened with a matching label. A **Labels** condition with **Exclude matches**, such as one for `skip-review`, prevents reviews while that label is on the pull request.

To start a review when someone adds a label, create a filter group that has only the **Pull request label added** event, or **Merge request label added** for GitLab. Then add a **Labels** condition with **Include matches**. A review starts only when the label that was added matches that condition. Adding an unrelated label to a pull request that already has a matching label doesn’t start another review.

 **Labels** conditions aren’t available for Bitbucket Cloud or Azure DevOps.

## If a pull request isn’t reviewed
<a name="_if_a_pull_request_isnt_reviewed"></a>

AWS Security Agent doesn’t comment on pull requests that don’t match a filter group. If a pull request isn’t reviewed, check the following:
+  **Code review comments** is turned on for the repository.
+ The pull request is open. Draft pull requests are reviewed only by a group without trigger events or a group that includes the **Pull request drafted** event.
+ The pull request meets every condition in at least one filter group.
+ Each pattern matches the complete branch or label name.

## Related topics
<a name="_related_topics"></a>
+  [Review code security findings in pull requests](review-code-findings-github.md) – what AWS Security Agent posts when a review runs.
+  [Service Quotas](quotas.md) – each review counts toward the monthly quota for pull request code reviews. Reviewing draft pull requests or every update uses more of the quota.
+  [Enable code review](enable-code-review-scan.md) – remediation commands, such as `@AWS-Security-Agent fix all findings`, follow the **Code remediation** setting, not trigger filters.