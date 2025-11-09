As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Monitoring recommendations with CloudWatch metrics

You can view Amazon CodeGuru Reviewer metrics in the Amazon CloudWatch console.

###### To access recommendation metrics

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. On the **All metrics** tab, choose
   **AWS/CodeGuruReviewer**.
4. Choose the dimension you want metrics for:
   **ProviderType**,
   **CodeReviewType**, or
   **RepositoryName**. The graph on the page displays
   metrics for recommendations for all selected items that are available for the selected
   dimension.
