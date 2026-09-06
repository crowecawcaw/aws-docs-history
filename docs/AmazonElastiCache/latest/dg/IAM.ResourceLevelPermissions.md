

# Resource-level permissions
<a name="IAM.ResourceLevelPermissions"></a>

You can restrict the scope of permissions by specifying resources in an IAM policy. Many ElastiCache API actions support a resource type that varies depending on the behavior of the action. Every IAM policy statement grants permission to an action that's performed on a resource. When the action doesn't act on a named resource, or when you grant permission to perform the action on all resources, the value of the resource in the policy is a wildcard (\*). For many API actions, you can restrict the resources that a user can modify by specifying the Amazon Resource Name (ARN) of a resource, or an ARN pattern that matches multiple resources. To restrict permissions by resource, specify the resource by ARN.

**Note**  
For resource-level permissions to be effective, the resource name in the ARN string should be lowercase.

To see a list of ElastiCache resource types and their ARNs, see [Resources Defined by Amazon ElastiCache](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticache.html#amazonelasticache-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by Amazon ElastiCache](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticache.html#amazonelasticache-actions-as-permissions).

**Topics**
+ [Example 1: Allow a user full access to specific ElastiCache resource types](#example-allow-list-current-elasticache-resources-resource)
+ [Example 2: Deny a user access to a serverless cache.](#example-allow-specific-elasticache-actions-resource)

## Example 1: Allow a user full access to specific ElastiCache resource types
<a name="example-allow-list-current-elasticache-resources-resource"></a>

The following policy explicitly allows all resources of type serverless cache.

```
{
        "Sid": "Example1",
        "Effect": "Allow",
        "Action": "elasticache:*",
        "Resource": [
             "arn:aws:elasticache:us-east-1:{{account-id}}:serverlesscache:*"
        ]
}
```

## Example 2: Deny a user access to a serverless cache.
<a name="example-allow-specific-elasticache-actions-resource"></a>

The following example explicitly denies access to a particular serverless cache.

```
{
        "Sid": "Example2",
        "Effect": "Deny",
        "Action": "elasticache:*",
        "Resource": [
            "arn:aws:elasticache:us-east-1:{{account-id}}:serverlesscache:{{name}}"
        ]
}
```