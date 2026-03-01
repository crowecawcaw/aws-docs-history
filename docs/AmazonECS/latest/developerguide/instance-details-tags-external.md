# Adding tags to External container instances for Amazon ECS

You can associate tags with your external container instances for Amazon ECS by using one of the
following methods.

- Method 1 – Before running the installation script to register your
  external instance with your cluster, create or edit the Amazon ECS container
  agent configuration file at `/etc/ecs/ecs.config` and add the
  `ECS_CONTAINER_INSTANCE_TAGS` container agent configuration
  parameter. This creates tags that are associated with the external
  instance.

The following is example syntax.

```
ECS_CONTAINER_INSTANCE_TAGS={"`tag_key`": "`tag_value`"}
```

- Method 2 – After your external instance is registered to your
  cluster, you can use the AWS Management Console to add tags. For more information, see
  [Adding tags to existing resources (Amazon ECS console)](tag-resources-console.md#adding-or-deleting-tags "tag-resources-console.md#adding-or-deleting-tags").
