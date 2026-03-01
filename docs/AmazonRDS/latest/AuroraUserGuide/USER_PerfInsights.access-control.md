# Using tag-based access control for Performance Insights

You can control access to Performance Insights metrics using tags inherited from the parent DB instance.
To control access to Performance Insights operations, use IAM policies. These policies can check the tags on your DB instance to determine permissions.

## How tags work with Performance Insights

Performance Insights automatically applies your DB instance tags to authorize Performance Insights metrics.
When you add tags to your DB instance, you can immediately use those tags to control access to Performance Insights data.

- To add or update tags for Performance Insights metrics, modify the tags on your DB instance.
- To view tags for Performance Insights metrics, call `ListTagsForResource` on the Performance Insights metric resource.
  It will return the tags from the DB instance associated with the metric.

###### Note

The `TagResource` and `UntagResource` operations return an error if you try to use them directly on Performance Insights metrics.

## Creating tag-based IAM policies

To control access to Performance Insights operations, use the `aws:ResourceTag` condition key in your IAM policies.
These policies check the tags on yourDB instance.

###### Example

This policy prevents access to Performance Insights metrics for production databases. The policy denies the `pi:GetResourceMetrics` operation in Performance Insights
for any database resource tagged with `env:prod`.

```
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "pi:GetResourceMetrics",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/env": "prod"
                }
            }
        }
    ]
}

```
