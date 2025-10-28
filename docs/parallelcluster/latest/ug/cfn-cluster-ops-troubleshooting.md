# Troubleshooting stacks that include the AWS ParallelCluster custom resource

With an AWS ParallelCluster custom resource, CloudFormation deploys a cluster from a new, separate stack. You can monitor
cluster creation by taking the following steps:

1. Navigate to CloudFormation in the AWS Management Console and choose **Stacks** in the navigation pane.
2. Choose the stack with the name that you defined for the cluster name.
3. If the stack state is `ROLLBACK_COMPLETE`, an error occurred during cluster creation.
4. Choose **Stack details**, and choose the **Events** tab.
5. Search **Events** on **Logical ID** for the name that you defined for the cluster name. It has a
   `Status reason` that gives a reason for an issue.
6. You can also choose the **Stacks** drop down menu, and then **Deleted** to see the list of deleted
   stacks. Select the stack with the cluster name and view **Events** for more details.
7. To view the output from the custom resource provider that manages the cluster, select the stack with the
   **Description** "AWS ParallelCluster Cluster Custom Resource." Choose the **Resources** tab, find the resource
   with **Logical ID**
   `PclusterCfnFunctionLogGroup`, and follow the given link. View the log streams that show the Lambda debug output.
8. To troubleshoot the cluster, see [AWS ParallelCluster troubleshooting](troubleshooting-v3.md "troubleshooting-v3.md").
