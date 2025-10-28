End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example metric policy: Container-level metrics

This example policy indicates that AWS Elemental MediaStore should send metrics to Amazon CloudWatch at the container level. For example, this includes the
`RequestCount` metric that counts the number of `Put` requests made to the container. Alternatively, you can set this
to `DISABLED`.

Because there are no rules in this policy, MediaStore does not send metrics at the path level. For example, you can't see how many
`Put` requests were made to a particular folder within this container.

```
{
   "ContainerLevelMetrics": "`ENABLED`"
}
```
