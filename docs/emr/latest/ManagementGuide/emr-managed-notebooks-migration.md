# Amazon EMR Notebooks are available as

Amazon EMR Studio Workspaces in the console

## Making the transition from

EMR Notebooks to Workspaces

In the [new Amazon EMR
console](whats-new-in-console.md "whats-new-in-console.md"), we've merged EMR Notebooks with Amazon EMR Studio Workspaces
into a single experience. When you use an EMR Studio, you can create and
configure different Workspaces to organize and run notebooks. If you had
Amazon EMR notebooks in the old console, they're available as EMR Studio
Workspaces in the console.

Amazon EMR created these new EMR Studio Workspaces for you. The number of
Studios that we created corresponds to the number of distinct VPCs that you use from
EMR Notebooks. For example, if you connect to EMR clusters in two different VPCs
from EMR Notebooks, then we created two new EMR Studios. Your notebooks are
distributed among the new Studios.

###### Important

We turned off the option to create new notebooks in the old Amazon EMR console.
Instead, use **Create Workspace** in the new Amazon EMR
console.

For more information on Amazon EMR Studio Workspaces, see [Learn EMR Studio workspaces](emr-studio-configure-workspace.md "emr-studio-configure-workspace.md"). For a conceptual overview of
EMR Studio, see [Workspaces](how-emr-studio-works.md#emr-studio-workspaces "how-emr-studio-works.md#emr-studio-workspaces") on the [How Amazon EMR Studio works](how-emr-studio-works.md "how-emr-studio-works.md")
page.

## What do you need to do?

While you can still use your existing notebooks in the old console, we recommend
that you instead use Amazon EMR Studio Workspaces in the console. You must
configure additional role permissions to turn on the [capabilities in EMR Studio
that aren’t available in EMR Notebooks](#emr-notebooks-workspaces-enhancements "#emr-notebooks-workspaces-enhancements").

###### Note

At a minimum, to view existing EMR Notebooks as EMR Studio
Workspaces and to create new Workspaces, users must have
`elasticmapreduce:ListStudios` and
`elasticmapreduce:CreateStudioPresignedUrl` permissions on their
roles. To access all of the EMR Studio features, see [Enabling EMR Studio features
for EMR Notebooks users](#emr-notebooks-workspaces-enable "#emr-notebooks-workspaces-enable") for the complete list of
added permissions that EMR Notebooks users will need.

## Enhanced capabilities in

EMR Studio beyond EMR Notebooks

With Amazon EMR Studio, you can set up and use the following capabilities that aren't
available with EMR Notebooks:

- [Browse and attach to
  EMR clusters from within Jupyterlab](emr-studio-create-use-clusters.md "emr-studio-create-use-clusters.md")
- [Browse and attach to
  EMR Notebooks virtual clusters from within Jupyterlab](emr-studio-create-use-clusters.md "emr-studio-create-use-clusters.md")
- [Connect to Git repos from within
  Jupyterlab](emr-studio-git-repo.md "emr-studio-git-repo.md")
- [Collaborate with other
  members of your team to write and run notebook code](emr-studio-workspace-collaboration.md "emr-studio-workspace-collaboration.md")
- [Browse data with SQL
  Explorer](emr-studio-sql-explorer.md "emr-studio-sql-explorer.md")
- [Provision EMR clusters with
  Service Catalog](emr-studio-cluster-templates.md "emr-studio-cluster-templates.md")

For a complete list of capabilities with Amazon EMR Studio, see [Key features of EMR Studio](emr-studio.md#emr-studio-key-features "emr-studio.md#emr-studio-key-features").

## Enabling EMR Studio features

for EMR Notebooks users

The new EMR Studios that we will create as part of this merge use the existing
`EMR_Notebooks_DefaultRole` IAM role as the EMR Studio service
role.

Users who transition to EMR Studio from EMR Notebooks and want to use the
additional capabilities of EMR Studio require several new role permissions. Add
the following permissions to the roles of your EMR Notebooks users who plan to use
EMR Studio.

###### Note

At a minimum, to view existing EMR Notebooks as EMR Studio
Workspaces and to create new Workspaces, users must have
`elasticmapreduce:ListStudios` and
`elasticmapreduce:CreateStudioPresignedUrl` permissions on their
roles. To use all of the EMR Studio features, add all of the permissions
listed below. Admin users also need permission to create and manage an
EMR Studio. For more information, see [Administrator permissions to create and manage
an EMR Studio](emr-studio-admin-permissions.md "emr-studio-admin-permissions.md").

```
"elasticmapreduce:DescribeStudio",
"elasticmapreduce:ListStudios",
"elasticmapreduce:CreateStudioPresignedUrl",
"elasticmapreduce:UpdateEditor",
"elasticmapreduce:PutWorkspaceAccess",
"elasticmapreduce:DeleteWorkspaceAccess",
"elasticmapreduce:ListWorkspaceAccessIdentities",
"emr-containers:ListVirtualClusters",
"emr-containers:DescribeVirtualCluster",
"emr-containers:ListManagedEndpoints",
"emr-containers:DescribeManagedEndpoint",
"emr-containers:CreateAccessTokenForManagedEndpoint",
"emr-containers:ListJobRuns",
"emr-containers:DescribeJobRun",
"servicecatalog:SearchProducts",
"servicecatalog:DescribeProduct",
"servicecatalog:DescribeProductView",
"servicecatalog:DescribeProvisioningParameters",
"servicecatalog:ProvisionProduct",
"servicecatalog:UpdateProvisionedProduct",
"servicecatalog:ListProvisioningArtifacts",
"servicecatalog:DescribeRecord",
"servicecatalog:ListLaunchPaths",
"cloudformation:DescribeStackResources"
```

The following permissions are also required to use the collaboration capabilities
in EMR Studio, but weren't required with EMR Notebooks.

```
"sso-directory:SearchUsers",
"iam:GetUser",
"iam:GetRole",
"iam:ListUsers",
"iam:ListRoles",
"sso:GetManagedApplicationInstance"
```
