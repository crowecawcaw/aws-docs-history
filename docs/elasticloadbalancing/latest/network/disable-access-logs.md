# Disable access logs for your Network Load Balancer

You can disable access logging for your load balancer at any time. After you
disable access logging, your access logs remain in your S3 bucket until you delete
the them. For more information, see [Creating, configuring, and working with S3 buckets](../../../AmazonS3/latest/userguide/creating-buckets-s3.md "../../../AmazonS3/latest/userguide/creating-buckets-s3.md") in the _Amazon S3 User Guide_.

Console

###### To disable access logs

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the name of your load balancer to open its details page.
4. On the **Attributes** tab, choose
   **Edit**.
5. For **Monitoring**, turn off **Access
   logs**.
6. Choose **Save changes**.

AWS CLI

###### To disable access logs

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes Key=access_logs.s3.enabled,Value=false
```
