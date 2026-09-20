

# Create a Notebook in EMR Studio
<a name="emr-managed-notebooks-create"></a>

**Note**  
EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-migration.html) and [Amazon EMR console](https://docs.aws.amazon.com/emr/latest/ManagementGuide/whats-new-in-console.html).

You create an EMR notebook using the old Amazon EMR console. Creating notebooks using the AWS CLI or the Amazon EMR API is not supported.

**To create an EMR notebook**

1. Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/](https://console.aws.amazon.com/elasticmapreduce/).

1. Choose **Notebooks**, **Create notebook**.

1. Enter a **Notebook name** and an optional **Notebook description**.

1. If you have an active cluster to which you want to attach the notebook, leave the default **Choose an existing cluster** selected, click **Choose**, select a cluster from the list, and then click **Choose cluster**. For information about cluster requirements for EMR Notebooks, see [Requirements, differences in release versions, and security for EMR Notebooks](emr-managed-notebooks-considerations.md).

   **—or—**

   Choose **Create a cluster**, enter a **Cluster name** and choose options according to the following guidelines. The cluster is created in the default VPC for the account using On-Demand instances.


<table>
<thead>
  <tr><th>Setting</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Cluster name</b></td><td>The friendly name used to identify the cluster.</td></tr>
  <tr><td><b>Release</b></td><td>Cannot be modified. Defaults to the latest Amazon EMR release version (5.36.2).</td></tr>
  <tr><td><b>Applications</b></td><td>Cannot be modified. Lists the applications that are installed on the cluster.</td></tr>
  <tr><td><b>Instance</b></td><td>Enter the number of instances and select the EC2 Instance type. One instance is used for the primary node. The rest are used for core nodes. The instance type determines the number of notebooks that can attach to the cluster simultaneously. For more information, see <a href="emr-managed-notebooks-considerations.md#emr-managed-notebooks-cluster-limits">Limits for concurrently attached EMR Notebooks</a>.</td></tr>
  <tr><td><b>EMR role</b></td><td>Leave the default or choose the link to specify a custom service role for Amazon EMR. For more information, see <a href="emr-iam-role.md">Service role for Amazon EMR (EMR role)</a>.</td></tr>
  <tr><td><b>EC2 instance profile</b></td><td>Leave the default or choose the link to specify a custom service role for EC2 instances. For more information, see <a href="emr-iam-role-for-ec2.md">Service role for cluster EC2 instances (EC2 instance profile)</a>.</td></tr>
  <tr><td><b>EC2 key pair</b></td><td>Choose an EC2 key pair to be able to connect to cluster instances. For more information, see <a href="emr-connect-master-node-ssh.md">Connect to the Amazon EMR cluster primary node using SSH</a>.</td></tr>
  <tr><td><b>Auto-termination</b></td><td>Auto-termination is supported for Amazon EMR versions 5.30.0 and 6.1.0 and later.Select the checkbox to enable auto-termination, then specify the amount of idle time after which the cluster should automatically shut down. For more information, see <a href="emr-auto-termination-policy.md">Using an auto-termination policy for Amazon EMR cluster cleanup</a>.</td></tr>
</tbody>
</table>


1. For **Security groups**, choose **Use default security groups**. Alternatively, choose **Choose security groups** and select custom security groups that are available in the VPC of the cluster. You select one for the primary instance and another for the notebook client instance. For more information, see [Specifying EC2 security groups for EMR Notebooks](emr-managed-notebooks-security-groups.md).

1. For **AWS Service Role**, leave the default or choose a custom role from the list. The client instance for the notebook uses this role. For more information, see [Service role for EMR Notebooks](emr-managed-notebooks-service-role.md).

1. For **Notebook location** choose the location in Amazon S3 where the notebook file is saved, or specify your own location. If the bucket and folder don't exist, Amazon EMR creates it.

   Amazon EMR creates a folder with the **Notebook ID** as folder name, and saves the notebook to a file named `{{NotebookName}}.ipynb`. For example, if you specify the Amazon S3 location `s3://amzn-s3-demo-bucket/MyNotebooks` for a notebook named `MyFirstEMRManagedNotebook`, the notebook file is saved to `s3://amzn-s3-demo-bucket/MyNotebooks/{{NotebookID}}/MyFirstEMRManagedNotebook.ipynb`.

   If you specify an encrypted location in Amazon S3, you must set up the [Service role for EMR Notebooks](emr-managed-notebooks-service-role.md) as a key user. The default service role is `EMR_Notebooks_DefaultRole`. If you are using an AWS KMS key for encryption, see [Using key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-users-crypto) in the AWS Key Management Service Developer Guide and the [support article for adding key users](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-access-default-encryption/).

1. Optionally, if you have added a Git-based repository to Amazon EMR that you want to associate with this notebook, choose **Git repository**, select **Choose repository** and then select a repository from the list. For more information, see [Associating Git-based repositories with EMR Notebooks](emr-git-repo.md).

1. Optionally, choose **Tags**, and then add any additional key-value tags for the notebook.
**Important**  
A default tag with the **Key** string set to `creatorUserID` and the value set to your IAM user ID is applied for access purposes. We recommend that you do not change or remove this tag because it can be used to control access. For more information, see [Use cluster and Notebook tags with IAM policies for access control](security_iam_service-with-iam.md#emr-tag-based-access).

1. Choose **Create Notebook**.