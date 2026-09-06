

# Create a new Notebook with an associated Git repository in EMR Studio
<a name="emr-git-repo-create-notebook"></a>

**Note**  
EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-migration.html) and [Amazon EMR console](https://docs.aws.amazon.com/emr/latest/ManagementGuide/whats-new-in-console.html).

**To create a notebook and associate it with Git repositories in the old Amazon EMR console**

1. Follow the instructions at [Create a Notebook in EMR Studio](emr-managed-notebooks-create.md).

1. For **Security group**, choose **Use your own security group**.
**Note**  
The security groups for your notebook must include an outbound rule to allow the notebook to route traffic to the internet via the cluster. We recommend that you create your own security groups. For more information, see [Specifying EC2 security groups for EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html).

1. For **Git repositories**, **Choose repository** to associate with the notebook.

   1. Choose a repository that is stored as a resource in your account, and then choose **Save**.

   1. To add a new repository as a resource in your account, choose **add a new repository**. Complete the **Add repository** workflow in a new window. 