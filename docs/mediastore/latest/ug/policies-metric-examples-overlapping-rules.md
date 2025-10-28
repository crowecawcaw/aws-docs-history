End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example metric policy: Path-level metrics with overlapping rules

This example policy indicates that AWS Elemental MediaStore should send metrics to Amazon CloudWatch at the container level. In addition, MediaStore should
send metrics for two folders: `sports/football/saturday` and `sports/football`.

The metrics for MediaStore requests to the `sports/football/saturday` folder have a CloudWatch dimension of
`ObjectGroupName=footballGroup1`. Because objects that are stored in the `sports/football` folder match both rules,
CloudWatch displays two data points for these objects: one with a dimension of `ObjectGroupName=footballGroup1` and the second with a
dimension of `ObjectGroupName=footballGroup2`.

```
{
   "ContainerLevelMetrics": "`ENABLED`",
   "MetricPolicyRules": [
     {
       "ObjectGroup": "`sports/football/saturday`",
       "ObjectGroupName": "`footballGroup1`"
     },
     {
       "ObjectGroup": "`sports/football`",
       "ObjectGroupName": "`footballGroup2`"
     }
   ]
 }
```
