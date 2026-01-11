Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Adding VPC connections for a space

You can add VPC connections in the Amazon CodeCatalyst console.

You must have the **Space administrator** role or **Power user** role to
manage VPC connections at the space level.

###### To add VPC connections

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space.

###### Tip

If you belong to more than one space, choose a space in the top
navigation bar. 3. Choose **Settings**, and then choose
**VPC connections**.

The page lists all VPC connections in your space. You can view the
**VPC connection name** name, the **VPC ID**, and
the associated **AWS account connection**. 4. Choose **Add VPC connection**. 5. In **AWS account connection**, do the following:

    * For **AWS account connection**, choose a connection from the drop-down
     menu.


    For more information about connections, see [Adding an AWS account to a space](../userguide/ipa-connect-account-create.md "../userguide/ipa-connect-account-create.md")  in the *CodeCatalyst User Guide*.


    ###### Note

    If you associate your VPC connection with a project-restricted AWS account connection, your VPC
     connection will only have access to specific projects and cannot be set as default.
     For more information, see [Enabling or disabling project-restricted account
     connections](managing-accounts-restriction.md "managing-accounts-restriction.md").
    * For **VPC role**, choose a role from the drop-down menu and then
     choose **Next**.




    	+ We recommend that the `ArnLike` field for your trust policy contains the following:



    	```
    	{
    	  "aws:SourceArn": [
    	    "arn:aws:codecatalyst:::space/`<space-id>`",
    	    "arn:aws:codecatalyst:::space/`<space-id>`/project/*"
    	  ]
    	}
    	```

    	Adding this `SourceArn` condition in your trust policy ensures that the VPC role is only used for the specified space.


    	###### Note

    	Understand that VPC connections are a space level resource, meaning that your VPC can be accessed by different projects.
    	 You can restrict access by configuring your VPC role trust policy with a specific `projectId` instead of instead of `*`.
    	+ The `Action` field for your permission policy must contain the following:



    	```
    	[
    	  "ec2:CreateNetworkInterface",
    	  "ec2:DescribeDhcpOptions",
    	  "ec2:DescribeNetworkInterfaces",
    	  "ec2:DeleteNetworkInterface",
    	  "ec2:DescribeSubnets",
    	  "ec2:DescribeSecurityGroups",
    	  "ec2:DescribeVpcs"
    	]
    	```
    This **VPC role** will be used to populate the **VPC**,
     **Subnets**, and **Security groups** drop-down menus and establish
     VPC connectivity with CodeCatalyst actions.


    For more information about roles, see [Managing IAM roles for connected accounts](../userguide/spaces-manage-roles.md "../userguide/spaces-manage-roles.md")  in the *CodeCatalyst User Guide*.

6. In **VPC connection details**, do the following:
   - For **VPC**, choose a VPC from the drop-down menu.

   For more information, see
   [Create a VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md")
   in the _Amazon VPC User Guide_.
   - In **Subnets**, choose _private_ subnets to connect to in each availability
     zone from the drop-down menus. Do not choose public subnets.

   For more information, see
   [Create a subnet](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md")
   in the _Amazon VPC User Guide_.
   - In **Security groups**, select the groups from the drop-down menu. You can select up to five security groups.

   For more information, see
   [Security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md")
   in the _Amazon VPC User Guide_.
   - In **VPC connection name**, enter the reference name for your VPC connection
     then choose **Next**.

   ###### Note

   Each VPC connection name must be unique per space.

7. After you've reviewed your selections, choose **Add VPC connection**.
8. You can now associate this VPC connection with an environment to use with your workflow actions or create
   a Dev Environment associated to your VPC connection. For instructions, see [Associating a VPC connection with an environment](../userguide/deploy-environments-managing-environment.md#deploy-environments-associate-vpc "../userguide/deploy-environments-managing-environment.md#deploy-environments-associate-vpc") or [Using Dev Environments with a VPC connection](../userguide/devenvironment-using-vpc.md "../userguide/devenvironment-using-vpc.md") in the _CodeCatalyst User Guide_.
