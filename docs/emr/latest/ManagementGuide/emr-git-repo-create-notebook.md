# Create a new Notebook with an

associated Git repository in EMR Studio

###### Note

EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").

###### To create a notebook and associate it with Git repositories in the old Amazon EMR

console

1. Follow the instructions at [Create a Notebook in EMR Studio](emr-managed-notebooks-create.md "emr-managed-notebooks-create.md").
2. For **Security group**, choose **Use your own
   security group**.

###### Note

The security groups for your notebook must include an outbound rule to
allow the notebook to route traffic to the internet via the cluster. We
recommend that you create your own security groups. For more
information, see [Specifying EC2 security groups for EMR Notebooks](emr-managed-notebooks-security-groups.md "emr-managed-notebooks-security-groups.md"). 3. For **Git repositories**, **Choose
repository** to associate with the notebook.

    1. Choose a repository that is stored as a resource in your account,
     and then choose **Save**.
    2. To add a new repository as a resource in your account, choose
     **add a new repository**. Complete the
     **Add repository** workflow in a new window.
