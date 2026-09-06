

# Cleaning up security agent resources
<a name="clean-up-guardduty-agent-resources-process"></a>

This section explains how you can clean up the AWS resources associated with the security agent. As listed in [Disabling, uninstalling, and resource cleanup](runtime-monitoring-agent-resource-clean-up.md), GuardDuty will not delete or remove all the security agent resources. The following section provides instructions on how you can delete the security agent resources.

**To delete Amazon VPC endpoint**  
When you manage the security agent manually, you may have created an Amazon VPC endpoint manually. After uninstalling the security agent for all the monitored resources in your account, you can choose to delete this VPC endpoint.  
The following list provides scenarios when using a shared VPC compared to not using a shared VPC.  
+ Without a shared VPC – When you no longer want to monitor a resource in an account, consider deleting the Amazon VPC endpoint.
+ With a shared VPC – When a shared VPC owner account deletes the shared VPC resource that was still being used, the Runtime Monitoring (and when applicable, EKS Runtime Monitoring) coverage status for the resources in your shared VPC owner account and the participating account might become unhealthy. For information about coverage status, see [Reviewing runtime coverage statistics and troubleshooting issues](runtime-monitoring-assessing-coverage.md).
For deleting the VPC endpoint, see [Delete an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/delete-interface-endpoint.html) in the *AWS PrivateLink Guide*.

**To delete the security group**  
+ Without a shared VPC – When you no longer want to monitor a resource type in an account, consider deleting the security group associated with the Amazon VPC.
+ With a shared VPC – When the shared VPC owner account deletes the security group, any participant account that is currently using the security group associated with the shared VPC, the Runtime Monitoring coverage status for the resources in your shared VPC owner account and the participating account might become unhealthy. For more information, see [Reviewing runtime coverage statistics and troubleshooting issues](runtime-monitoring-assessing-coverage.md).
For information about steps, see [Delete an Amazon EC2 security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deleting-security-group.html) in the *Amazon EC2 User Guide*.

**To remove GuardDuty security agent from an EKS cluster**  
To remove the security agent from your EKS cluster that you no longer want to monitor, see [Removing an Amazon EKS add-on from a cluster](https://docs.aws.amazon.com/eks/latest/userguide/removing-an-add-on.html) in the *Amazon EKS User Guide*.  
Removing the EKS add-on agent doesn't remove the `amazon-guardduty` namespace from the EKS cluster. To delete the `amazon-guardduty` namespace, see [Deleting a namespace](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/#deleting-a-namespace).

**To delete the `amazon-guardduty` namespace (EKS cluster)**   
Disabling Automated agent configuration doesn't automatically remove the `amazon-guardduty` namespace from your EKS cluster. To delete the `amazon-guardduty` namespace, see [Deleting a namespace](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/#deleting-a-namespace).