# AWS Graviton-based instance

recommendations

When viewing Amazon EC2 instance, EC2 Auto Scaling group, and Aurora and RDS database recommendations, you can view the price and
performance impact of running your workload on AWS Graviton-based instances.

###### To view recommendations for AWS Graviton-based instances

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **EC2 instances**, **EC2 Auto Scaling groups**, or **RDS databases** in the navigation pane.
3. On the recommendation page of the resource that you selected,
   choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown.
4. (Optional) Otherwise, choose **Current** to view
   recommendations that are based on the same CPU vendor and architecture as the current
   instance.

###### Note

The **Current price**, **Recommended price**,
**Price difference**, **Price difference (%)**, and
**Estimated monthly savings** columns are updated to provide a price
comparison between the current instance type and the instance type of the selected CPU
architecture preference. For example, if you choose **Graviton
(aws-arm64)**, prices are compared between the current instance type and the
recommended Graviton-based instance type.

## Additional resources

- [Viewing EC2 instance recommendations](view-ec2-recommendations.md "view-ec2-recommendations.md")
- [Viewing EC2 Auto Scaling group recommendations](view-asg-recommendations.md "view-asg-recommendations.md")
- [Viewing Aurora and RDS database recommendations](view-rds-recommendations.md "view-rds-recommendations.md")
