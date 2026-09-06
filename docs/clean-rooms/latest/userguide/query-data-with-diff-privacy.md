

# Viewing the impact of differential privacy
<a name="query-data-with-diff-privacy"></a>

In general, writing and running queries doesn't change when differential privacy is turned on. However, you can't run a query if there isn't enough privacy budget remaining. As you run queries and consume the privacy budget, you can see approximately how many aggregations you can run and how that might impact future queries.

**To view the impact of differential privacy in a collaboration**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration that has **Your member details** status of **Run queries**.

1. On the **Analysis** tab, under **Tables**, view the remaining privacy budget. This is displayed as the estimated number of **aggregation functions remaining** and the **Utility used** (rendered as a percentage).
**Note**  
The estimated number of **aggregate functions remaining** and the percentage of the **Utility used** only display for the member who can query.

1. Choose **View impact** to view how much noise is injected into the results and approximately how many aggregation functions you can run.