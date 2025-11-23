# Disable health check logs for your Application Load Balancer

You can disable health check logs for your load balancer at any time. After you
disable health check logs, your health check logs remain in your S3 bucket until you delete
them. For more information, see [Creating, configuring, and working with buckets](../../../AmazonS3/latest/userguide/creating-buckets-s3.md "../../../AmazonS3/latest/userguide/creating-buckets-s3.md") in the
_Amazon S3 User Guide_.

Console

###### To disable health check logs

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the name of your load balancer to open its details page.
4. On the **Attributes** tab, choose
   **Edit**.
5. For **Monitoring**, turn off **Health check
   logs**.
6. Choose **Save changes**.

AWS CLI

###### To disable health check logs

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes Key=health_check_logs.s3.enabled,Value=false
```
