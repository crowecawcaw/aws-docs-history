As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Monitoring CodeGuru Reviewer recommendations with CloudWatch alarms

You can create an Amazon CloudWatch alarm for your CodeGuru Reviewer recommendations to monitor their count
over time.

An alarm watches the number of recommendations for one of three CodeGuru Reviewer CloudWatch dimensions
that you specify:

- `ProviderType` – View the number of recommendations for a provider type. You
  can view the count of recommendations in all repositories in AWS CodeCommit, your Bitbucket account, your GitHub account, or
  your GitHub Enterprise Server account, over a period of time.
- `CodeReviewType` – View the number of recommendations for a code review type. The one available
  code review type is `PullRequest`. Use it to view the count of recommendations in one pull request.
- `RepositoryName` – View the count of recommendations for one repository over a period of time.
  You set one or more actions that happen when the number of recommendations for a
  dimension exceeds a count over a number of time periods you choose. For example, you can
  specify that an Amazon SNS notification is sent when more than 25 recommendations are generated for
  a branch in a repository within an hour.

A user or role must have CloudWatch `PutMetricAlarm` permissions to create an alarm.
For more information, see [Using
identity-based policies for CodeGuru Reviewer](auth-and-access-control-iam-identity-based-access-control.md "auth-and-access-control-iam-identity-based-access-control.md") and [Amazon CloudWatch permissions reference](../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md "../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md") in the _Amazon CloudWatch User Guide_.

###### To create a CloudWatch alarm for CodeGuru Reviewer

recommendations

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**.
5. Choose **AWS/CodeGuruReviewer**.
6. Choose the dimension to monitor:
   **ProviderType**,
   **CodeReviewType**, or
   **RepositoryName**. Then choose a metric to create
   an alarm for.
7. Continue through the process to create your alarm.

For more information about setting up CloudWatch alarms in the CloudWatch console, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.
