# Clean up an AWS PCS cluster in AWS CloudFormation

If you used AWS CloudFormation to create your AWS PCS cluster, you can open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation") and delete the stack to delete the cluster
and all its associated resources.

###### Important

For the sample cluster, if you created additional compute node groups or queues
in your cluster (beyond the `login` and `compute-1` groups
that the sample CloudFormation template created), you must use the
[AWS PCS console](https://console.aws.amazon.com/pcs "https://console.aws.amazon.com/pcs") or AWS CLI to delete
those resources before you delete the CloudFormation stack. For more information,
see [Deleting a cluster in AWS PCS](working-with_clusters_delete.md "working-with_clusters_delete.md").
