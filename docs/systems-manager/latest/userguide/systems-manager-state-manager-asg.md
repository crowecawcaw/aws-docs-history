AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Running Auto Scaling groups with

associations

The best practice when using associations to run Auto Scaling groups is to use tag
targets. Not using tags might cause you to reach the association limit.

If all nodes are tagged with the same key and value, you only need one association
to run your Auto Scaling group. The following procedure describes how to create such an
association.

###### To create an association that runs Auto Scaling groups

1. Ensure all nodes in the Auto Scaling group are tagged with the same key and value.
   For more instructions on tagging nodes, see [Tagging Auto
   Scaling groups and instances](../../../autoscaling/ec2/userguide/autoscaling-tagging.md "../../../autoscaling/ec2/userguide/autoscaling-tagging.md") in the
   _AWS Auto Scaling User Guide_.
2. Create an association by using the procedure in [Working with associations in Systems Manager](state-manager-associations.md "state-manager-associations.md").

If you're working in the console, choose **Specify instance
tags** in the **Targets** field. For
**Instance tags**, enter the **Tag**
key and value for your Auto Scaling group.

If you're using the AWS Command Line Interface (AWS CLI), specify `--targets
 Key=tag:`tag-key`,Values=`tag-value``
where the key and value match what you tagged your nodes with.
