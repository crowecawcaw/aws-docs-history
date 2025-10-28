# Backfill domain tags

You can improve resource filtering by adding domain tags to untagged resources. If you
have resources that are not tagged, you can backfill them.

If you have created resources in a domain before 11/30/2022, those resources are not
automatically tagged with the domain Amazon Resource Name (ARN) tag.

To accurately attribute resources to their respective domain, you must add the
domain tag to existing resources using the AWS CLI, as follows.

1. Map all existing SageMaker AI resources and their respective ARNs to the domains that
   exist in your account.
2. Run the following command from your local machine to tag the resource with the ARN of
   the resource's respective domain. This must be repeated for every SageMaker AI resource in
   your account.

```
aws resourcegroupstaggingapi tag-resources \
    --resource-arn-list arn:aws:sagemaker:`region`:`account-id`:space/`domain-id`/`space-name` \
    --tags sagemaker:domain-arn=arn:aws:sagemaker:`region`:`account-id`:domain/`domain-id`
```
