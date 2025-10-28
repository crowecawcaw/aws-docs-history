End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example metric policy: Path-level metrics using wildcards

This example policy indicates that AWS Elemental MediaStore should send metrics to Amazon CloudWatch at the container level. In addition, MediaStore should
also send metrics for objects based on their file name. A wildcard indicates that the objects can be stored anywhere in the container and they
can have any file name, as long as it ends with a `.m3u8` extension.

```
{
   "ContainerLevelMetrics": "`ENABLED`",
   "MetricPolicyRules": [
     {
       "ObjectGroup": "`*.m3u8`",
       "ObjectGroupName": "`index`"
     }
   ]
 }
```
