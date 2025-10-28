# Disable access logs for your Classic Load Balancer

You can disable access logs for your load balancer at any time. After you disable
access logs, your access logs remain in your Amazon S3 until you delete the them. For more
information, see [Working with S3 buckets](../../../AmazonS3/latest/userguide/creating-buckets-s3.md "../../../AmazonS3/latest/userguide/creating-buckets-s3.md")
in the _Amazon S3 User Guide_.

###### To disable access logs for your load balancer using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select the name of your load balancer to open its details page.
4. On the **Attributes** tab, choose **Edit**.
5. On the **Edit load balancer attributes** page, in the **Monitoring** section, disable **Access logs**.

###### To disable access logs using the AWS CLI

Use the following [modify-load-balancer-attributes](../../../cli/latest/reference/elb/modify-load-balancer-attributes.md "../../../cli/latest/reference/elb/modify-load-balancer-attributes.md")
command to disable access logs:

```
`aws elb modify-load-balancer-attributes --load-balancer-name `my-loadbalancer` --load-balancer-attributes "{\"AccessLog\":{\"Enabled\":false}}"`
```

The following is an example response:

```
{
    "LoadBalancerName": "my-loadbalancer",
    "LoadBalancerAttributes": {
        "AccessLog": {
            "S3BucketName": "amzn-s3-demo-loadbalancer-logs",
            "EmitInterval": 60,
            "Enabled": false,
            "S3BucketPrefix": "my-app"
        }
    }
}
```
