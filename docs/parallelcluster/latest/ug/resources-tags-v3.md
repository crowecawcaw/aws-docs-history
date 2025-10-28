# AWS ParallelCluster resources and tagging

With AWS ParallelCluster you can create tags to track and manage your AWS ParallelCluster resources. You define the tags that you want AWS CloudFormation to
create and propagate to all cluster resources in the [Tags section](Tags-v3.md "Tags-v3.md") of the cluster configuration
file. You can also use tags that AWS ParallelCluster automatically generates to track and manage your resources.

When you create a cluster, the cluster and its resources are tagged with the AWS ParallelCluster and AWS systems tags defined in this
section.

AWS ParallelCluster applies tags to the cluster instances, volumes, and resources. To identify the cluster stack, AWS CloudFormation applies AWS system
tags to the cluster instances. To identify the cluster Amazon EC2 launch templates, Amazon EC2 applies system tags to the instances. You can use these tags to view and manage
your AWS ParallelCluster resources.

###### Warning

All AWS ParallelCluster tags are essential and must not be modified in order to avoid impacts to system functionality. Because of this, you can't modify AWS system tags.

The following is an example of an AWS system tag for an AWS ParallelCluster resource.

```
`"aws:cloudformation:stack-name"=`"clustername"``
```

The following is an example of an AWS ParallelCluster tag applied to a resource.

```
`"parallelcluster:cluster-name"=`"clustername"``
```

You can view these tags in the Amazon EC2 section of the AWS Management Console.
