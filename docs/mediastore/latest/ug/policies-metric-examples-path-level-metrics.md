End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example metric policy: Path-level metrics

This example policy indicates that AWS Elemental MediaStore should not send metrics to Amazon CloudWatch at the container level. In addition, MediaStore
should send metrics for objects in two specific folders: `baseball/saturday` and `football/saturday`. The metrics for
MediaStore requests are as follows:

- Requests to the `baseball/saturday` folder have a CloudWatch dimension of `ObjectGroupName=baseballGroup`.
- Requests to the `football/saturday` folder have a dimension `ObjectGroupName=footballGroup`.

```
{
   "ContainerLevelMetrics": "`DISABLED`",
   "MetricPolicyRules": [
     {
       "ObjectGroup": "`baseball/saturday`",
       "ObjectGroupName": "`baseballGroup`"
     },
     {
       "ObjectGroup": "`football/saturday`",
       "ObjectGroupName": "`footballGroup`"
     }
   ]
}
```
