# Setting up a Slurm cluster in

Studio

The following instructions describe how to set up a HyperPod Slurm cluster in
Studio.

1. Create a domain or have one ready. For information on creating a domain, see
   [Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md").
2. (Optional) Create and attach a custom FSx for Lustre volume to your domain.
   1. Ensure that your FSx Lustre file system exists in the same VPC as your intended
      domain, and is in one of the subnets present in the domain.
   2. You can follow the instructions in [Adding a custom file system to a domain](domain-custom-file-system.md "domain-custom-file-system.md").

3. (Optional) We recommend that you add tags to your clusters to ensure a more smooth
   workflow. For information on how to add tags, see [Edit a
   SageMaker HyperPod cluster](sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-edit-clusters "sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-edit-clusters") to update your cluster
   using the SageMaker AI console.
   1. Tag your FSx for Lustre file system to your Studio domain. This will help you
      identify the file system while launching your Studio spaces. To do so, add the
      following tag to your cluster to identify it with the FSx filesystem ID, `fs-id`.

   Tag Key = “`hyperpod-cluster-filesystem`”, Tag Value =
   “`fs-id`”. 2. Tag your [Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md")
   workspace to your Studio domain. This will be used to quickly link to your Grafana
   workspace directly from your cluster in Studio. To do so, add the following tag to your
   cluster to identify it with your Grafana workspace ID, `ws-id`.

   Tag Key = “`grafana-workspace`”, Tag Value = “`ws-id`”.

4. Add the following permission to your execution role.

For information on SageMaker AI execution roles and how to edit them, see [Understanding domain space permissions and
execution roles](execution-roles-and-spaces.md "execution-roles-and-spaces.md").

To learn how to attach policies to an IAM user or group, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:TerminateSession"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateCluster",
 "sagemaker:ListClusters"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData",
 "cloudwatch:GetMetricData"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeCluster",
 "sagemaker:DescribeClusterNode",
 "sagemaker:ListClusterNodes",
 "sagemaker:UpdateCluster",
 "sagemaker:UpdateClusterSoftware"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:cluster/*"
 }
 ]
}`

```

5. Add a tag to this IAM role, with Tag Key = “`SSMSessionRunAs`” and Tag Value
   = “`os user`”. The `os user` here is the same user that you setup for
   the Slurm cluster. Manage access to SageMaker HyperPod clusters at an IAM role or user level by
   using the Run As feature in [AWS Systems Manager Agent (SSM Agent)](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md").
   With this feature, you can start each SSM session using the operating system (OS) user
   associated to the IAM role or user.

For information on how to add tags to your execution role, see [Tag IAM
roles](../../../IAM/latest/UserGuide/id_tags_roles.md "../../../IAM/latest/UserGuide/id_tags_roles.md"). 6. [Turn on Run As support
for Linux and macOS managed nodes](../../../systems-manager/latest/userguide/session-preferences-run-as.md "../../../systems-manager/latest/userguide/session-preferences-run-as.md"). The Run As settings are account wide and is
required for all SSM sessions to start successfully. 7. (Optional) [Restrict task view
in Studio for Slurm clusters](#sagemaker-hyperpod-studio-setup-slurm-restrict-tasks-view "#sagemaker-hyperpod-studio-setup-slurm-restrict-tasks-view"). For information
on viewable tasks in Studio, see [Tasks](sagemaker-hyperpod-studio-tabs.md#sagemaker-hyperpod-studio-tabs-tasks "sagemaker-hyperpod-studio-tabs.md#sagemaker-hyperpod-studio-tabs-tasks").
In Amazon SageMaker Studio you can navigate to view your clusters in HyperPod clusters
(under Compute).

## Restrict task view

in Studio for Slurm clusters

You can restrict users to view Slurm tasks that are authorized to view, without requiring
manual input of namespaces or additional permissions checks. The restriction is applied based
on the users’ IAM role, providing a streamlined and secure user experience. The following
section provides information on how to restrict task view in Studio for Slurm clusters.
For information on viewable tasks in Studio, see [Tasks](sagemaker-hyperpod-studio-tabs.md#sagemaker-hyperpod-studio-tabs-tasks "sagemaker-hyperpod-studio-tabs.md#sagemaker-hyperpod-studio-tabs-tasks").

All Studio users can view, manage, and interact with all Slurm cluster tasks by
default. To restrict this, you can manage access to SageMaker HyperPod clusters at an IAM role or
user level by using the **Run As** feature in [AWS Systems Manager Agent
(SSM Agent)](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md").

You can do this by tagging IAM roles with specific identifiers, such as their username
or group. When a user accesses Studio, the Session Manager uses the Run As feature to execute
commands as a specific Slurm user account that matches their IAM role tags. The Slurm
configuration can be set up to limit task visibility based on the user account. The Studio
UI will automatically filter tasks visible to that specific user account when commands are
executed through the Run As feature. Once set up, each user assuming the role with the
specified identifiers will have those Slurm tasks filtered based on the Slurm configuration.
For information on how to add tags to your execution role, see [Tag IAM roles](../../../IAM/latest/UserGuide/id_tags_roles.md "../../../IAM/latest/UserGuide/id_tags_roles.md").
