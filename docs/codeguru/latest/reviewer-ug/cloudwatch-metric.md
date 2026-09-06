

As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

# Monitoring recommendations with CloudWatch metrics
<a name="cloudwatch-metric"></a>

You can view Amazon CodeGuru Reviewer metrics in the Amazon CloudWatch console.<a name="cloudswatch-console-procedure"></a>

**To access recommendation metrics**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**. 

1. On the **All metrics** tab, choose **AWS/CodeGuruReviewer**. 

1. Choose the dimension you want metrics for: **ProviderType**, **CodeReviewType**, or **RepositoryName**. The graph on the page displays metrics for recommendations for all selected items that are available for the selected dimension. 