# ElastiCache API permissions: Actions, resources, and conditions reference

When you set up [access
control](IAM.md "IAM.md") and write permissions policies to attach to an IAM policy (either identity-based or resource-based), use the following table as a reference. The table lists each
Amazon ElastiCache API operation and the corresponding actions for which you can grant
permissions to perform the action. You specify the actions in the policy's
`Action` field, and you specify a resource
value in the policy's `Resource` field. Unless indicated otherwise, the resource is required. Some fields include both a required resource and optional resources. When there is no resource ARN, the resource in the policy is a wildcard (\*).

You can use condition keys in your ElastiCache policies to express conditions. To see a list of ElastiCache-specific condition keys, along with the actions and resource types to which they apply, see [Using condition keys](IAM.md "IAM.md"). For a
complete list of AWS-wide keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

###### Note

To specify an action, use the `elasticache:` prefix followed by the API
operation name (for example, `elasticache:DescribeCacheClusters`).

To see a list of ElastiCache actions, see [Actions Defined by Amazon ElastiCache](../../../service-authorization/latest/reference/list_amazonelasticache.md#amazonelasticache-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonelasticache.md#amazonelasticache-actions-as-permissions") in the
_Service Authorization Reference_.
