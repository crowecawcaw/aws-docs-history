Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Monitoring CodeGuru Reviewer with Amazon CloudWatch

You can use Amazon CloudWatch to monitor the number of recommendations created for your source code
in an associated repository over time.

The recommendations are available for three _dimensions_:

- `ProviderType` – View the number of recommendations for a provider type. You
  can view the count of recommendations in all repositories in AWS CodeCommit, your Bitbucket account, your GitHub account, or
  your GitHub Enterprise Server account, over a period of time.
- `CodeReviewType` – View the number of recommendations for a code review type. The one available
  code review type is `PullRequest`. Use it to view the count of recommendations in one pull request.
- `RepositoryName` – View the count of recommendations for one repository over a period of time.
  You can set a CloudWatch alarm that notifies you when the number of recommendations exceeds a
  threshold you set.

For more information about creating and using CloudWatch alarms and metrics, see [Using
Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").

You can track the following metric for each dimension over a period of time.

| Metric                          | Description                                                                                                                                                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RecommendationsPublishedCount` | The number of recommendations over a period of time per `ProviderType`, `CodeReviewType`, or `RepositoryName` for completed code reviews. Units: Count Valid CloudWatch statistic: Count Valid CloudWatch period: 1 hour | ###### Topics <br>• [Monitoring recommendations with CloudWatch metrics](cloudwatch-metric.md "cloudwatch-metric.md") <br>• [Monitoring CodeGuru Reviewer recommendations with CloudWatch alarms](cloudwatch-alarm.md "cloudwatch-alarm.md") |
