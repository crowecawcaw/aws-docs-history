

# Disable connection logs for your Application Load Balancer
<a name="disable-connection-logging"></a>

You can disable connection logs for your load balancer at any time. After you disable connection logs, your connection logs remain in your S3 bucket until you delete them. For more information, see [Creating, configuring, and working with buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon S3 User Guide*.

------
#### [ Console ]

**To disable connection logs**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Select the name of your load balancer to open its details page.

1. On the **Attributes** tab, choose **Edit**.

1. For **Monitoring**, turn off **Connection logs**.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To disable connection logs**  
Use the [modify-load-balancer-attributes](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-load-balancer-attributes.html) command.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn {{load-balancer-arn}} \
    --attributes Key=connection_logs.s3.enabled,Value=false
```

------