

# Troubleshooting for target recommendations with AWS DMS Fleet Advisor
<a name="fa-recommendations-troubleshooting"></a>

**Important**  
End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

In the following list, you can find actions to take when you encounter issues with the DMS Fleet Advisor Target Recommendations feature.

**Topics**
+ [I can't see price estimates for target recommendations](#fa-recommendations-troubleshooting-price-estimates)
+ [I can't see resource utilization charts](#fa-recommendations-troubleshooting-charts)
+ [I can't see the metrics collection status](#fa-recommendations-troubleshooting-metrics)

## I can't see price estimates for target recommendations
<a name="fa-recommendations-troubleshooting-price-estimates"></a>

If you see the **No data** for the **Estimated monthly cost** for a recommendation with a status of **Success**, then make sure that you granted your IAM user with permissions to access the AWS Price List Service API. To do so, you must create the policy that includes the `pricing:GetProducts` permission and add it to your IAM user as described in [Create IAM resources](fa-resources.md#fa-resources-iam). 

DMS Fleet Advisor doesn't calculate the estimated monthly cost for recommendations with a status of **Failed**.

## I can't see resource utilization charts
<a name="fa-recommendations-troubleshooting-charts"></a>

If you see the **Failed to load metrics** message after you expand the **Source utilization and capacity** section, then make sure that you granted your IAM user with permissions to view Amazon CloudWatch dashboards. To do so, you must add the required policy to your IAM user as described in [Create IAM resources](fa-resources.md#fa-resources-iam).

Alternatively, you can create a custom policy which includes the `cloudwatch:GetDashboard`, `cloudwatch:ListDashboards`, `cloudwatch:PutDashboard`, and `cloudwatch:DeleteDashboards` permissions. For more information, see [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the *Amazon CloudWatch User Guide*.

## I can't see the metrics collection status
<a name="fa-recommendations-troubleshooting-metrics"></a>

If you see the **No data available** for **Metrics collection** when you choose **Generate recommendations**, then make sure that you collected data. For more information, see [Collecting data for AWS DMS Fleet Advisor](fa-collecting.md).

If you have this issue after you collected data, then make sure that you granted your IAM user with the `cloudwatch:Get*` permission to access Amazon CloudWatch. DMS Fleet Advisor uses a service-linked role to publish the collected database performance metrics to CloudWatch on your behalf. Make sure to create a service-linked role to use with DMS Fleet Advisor. For more information, see [Create IAM resources](fa-resources.md#fa-resources-iam).