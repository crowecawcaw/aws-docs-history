# Adding tags to an Amazon EC2 container instance for

Amazon ECS

You can associate tags with your Amazon EC2 container instances for Amazon ECS using one of the following
methods:

- Method 1 – When creating the container instance using the Amazon EC2 API,
  CLI, or console, specify tags by passing user data to the instance using the
  container agent configuration parameter
  `ECS_CONTAINER_INSTANCE_TAGS`. This creates tags that are associated
  with the container instance in Amazon ECS only, they cannot be listed using the Amazon EC2
  API. For more information, see [Bootstrapping Amazon ECS Linux container instances to pass data](bootstrap_container_instance.md "bootstrap_container_instance.md").

###### Important

If you launch your container instances using an Amazon EC2 Auto Scaling group,
then you should use the ECS_CONTAINER_INSTANCE_TAGS agent configuration
parameter to add tags. This is due to the way in which tags are added to
Amazon EC2 instances that are launched using Auto Scaling groups.

The following is an example of a user data script that associates tags with
your container instance:

```
#!/bin/bash
cat <<'EOF' >> /etc/ecs/ecs.config
ECS_CLUSTER=`MyCluster`
ECS_CONTAINER_INSTANCE_TAGS={"`tag_key`": "`tag_value`"}
EOF
```

- Method 2 – When you create your container instance using the Amazon EC2 API,
  CLI, or console, first specify tags using the `TagSpecification.N`
  parameter. Then, pass user data to the instance by using the container agent
  configuration parameter `ECS_CONTAINER_INSTANCE_PROPAGATE_TAGS_FROM`.
  Doing so propagates them from Amazon EC2 to Amazon ECS.

The following is an example of a user data script that propagates the tags
that are associated with an Amazon EC2 instance, and registers the instance with a
cluster that's named `MyCluster`.

```
#!/bin/bash
cat <<'EOF' >> /etc/ecs/ecs.config
ECS_CLUSTER=`MyCluster`
ECS_CONTAINER_INSTANCE_PROPAGATE_TAGS_FROM=ec2_instance
EOF
```

To provide access to allow container instance tags to propagate from Amazon EC2 to
Amazon ECS, manually add the following permissions as an inline policy to the Amazon ECS
container instance IAM role. For more information, see [Adding and
Removing IAM Policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

    + `ec2:DescribeTags`

The following is an example policy that's used to add these
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeTags"
 ],
 "Resource": "*"
 }
 ]
}`

```
