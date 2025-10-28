# Promote the permission and resource

share

If you use customized (customer managed) permissions, you need to promote the
permission and the associated resource share in order for the model package
group to be discoverable. Complete the following steps to promote the permission
and resource share.

1. To promote your customized permission to be accessible by AWS RAM, use
   the following command:

```
aws ram promote-permission-created-from-policy —permission-arn `<permission-arn>`
```

2. Promote the resource share using the following command:

```
aws ram promote-resource-share-created-from-policy --resource-share-arn `<resource-share-arn>`
```

If you see the `OperationNotPermittedException` error while
performing the previous steps, the entity is not discoverable but is accessible.
For example, if the resource owner attaches a resource policy with an assume
role principal such as `“Principal”: {“AWS”:
 “arn:aws:iam::3333333333:role/Role-1”}`, or if the resource policy
allows `“Action”: “*”` , the associated model package group is not
promotable nor discoverable.
