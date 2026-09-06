

# Tutorial: Creating a MySQL DB cluster with a custom parameter group
<a name="tutorial-creating-custom-OPG"></a>

In this tutorial, you create a MySQL DB cluster with a custom parameter group. For more information about parameter groups, see [DB cluster parameter groups for Amazon Aurora DB clusters](USER_WorkingWithDBClusterParamGroups.md).

**Important**  
There's no charge for creating an AWS account. However, by completing this tutorial, you might incur costs for the AWS resources you use. You can delete these resources after you complete the tutorial if they are no longer needed.

To create a DB cluster with custom configurations and settings, you can use custom parameter groups. Custom parameter groups are particularly helpful if you work with multiple databases and want to uniformly configure settings for them.

By completing these steps, you learn:
+ How to use Amazon Aurora to create a MySQL DB cluster with a custom parameter group.
+ How to use specific parameters for MySQL DB clusters. 

To complete this tutorial, perform the following tasks:

1. Create a DB cluster parameter group with the MySQL parameter `default_password_lifetime`. 

1. Create a MySQL DB cluster with the custom DB cluster parameter group that you created.

**Topics**
+ [Prerequisites](#tutorial-creating-custom-OPG.Prerequisites)
+ [Create an Amazon Aurora DB cluster parameter group](#tutorial-creating-custom-OPG.create-parameter-group)
+ [Modify parameter value in your custom parameter group](#tutorial-creating-custom-OPG.add-parameters)
+ [Create MySQL DB cluster with a DB cluster parameter group](#tutorial-creating-custom-OPG.create-OPG)

## Prerequisites
<a name="tutorial-creating-custom-OPG.Prerequisites"></a>

This tutorial requires you to have an AWS account and a user with administrative access. If you don't already have those set up, complete the steps in the following sections:
+ [Sign up for an AWS account](CHAP_SettingUp_Aurora.md#sign-up-for-aws)

## Create an Amazon Aurora DB cluster parameter group
<a name="tutorial-creating-custom-OPG.create-parameter-group"></a>

In this tutorial, you learn how to create a custom parameter group with [ default\_password\_lifetime](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_password_lifetime) for a MySQL DB cluster in the console. The `default_password_lifetime` parameter controls the number of days before the client password automatically expires. For more information on other parameters available for MySQL DB clusters, see [Aurora MySQL configuration parameters](AuroraMySQL.Reference.ParameterGroups.md) . 

**To create a parameter group**

1. Open the Amazon RDS console and choose **Parameter groups**. 

1. For **Custom parameter groups**, choose **Create parameter group**. 

1. Set the parameter group details.

   1. Enter a name for the parameter group.

   1. Enter a description of the parameter group.

   1. For **Engine type**, choose **Aurora MySQL.** 

   1. For **Parameter group family**, choose **aurora-mysql8.0.** 

   1. For **Type**, choose **DB cluster parameter group.**

1. Choose **Create**. 

The new DB cluster parameter group appears on the **Parameter groups** page in the Amazon RDS console. The following steps illustrate how to modify parameter values to customize your parameter group. 

## Modify parameter value in your custom parameter group
<a name="tutorial-creating-custom-OPG.add-parameters"></a>

Use the following steps to modify the parameter value in the parameter group that you created in [Create an Amazon Aurora DB cluster parameter group](#tutorial-creating-custom-OPG.create-parameter-group). 

**To modify parameter values in your parameter group**

1. Open the Amazon RDS console and choose **Parameter groups**. 

1. For **Custom parameter groups**, choose the name of the DB cluster parameter group you created.

1. Choose **Edit**. 

1. In the **Filter parameters** search box, search for the custom parameter `default_password_lifetime`. 

1. Select the check box next to the parameter and enter a value the number of days to set for this password lifetime parameter. 

1. Select **Save Changes**.

The custom parameter group is now available to associate with Amazon Aurora for MySQL 8.0 DB cluster. 

## Create MySQL DB cluster with a DB cluster parameter group
<a name="tutorial-creating-custom-OPG.create-OPG"></a>

Finally, create a MySQL DB cluster with the custom parameter group that you made in the previous steps. The following steps show how to create the MySQL DB cluster with your custom parameter group.

**To create a DB cluster with a custom parameter and new option group**

1. Open the Amazon RDS console and choose **Databases**. 

1. Choose **Create database**.

1. For **Choose a database creation method**, choose **Standard Create**.

1. For **Engine options**, choose **Aurora (MySQL Compatible)**.

1. Select **Additional Configuration**.
   + For **Initial database name**, choose a name for your DB cluster.
   + Under the **DB cluster parameter group** dropdown, select the name of the DB cluster parameter group you created previously.

1. For this tutorial, you can leave the default settings for any other DB settings or modify them as required. 

1. Choose **Create database**.

RDS creates a new MySQL DB cluster with a custom parameter group group. To see more information on this database, see the **Databases** page of the Amazon RDS console.

In this tutorial, you configured a MySQL DB cluster with tailored settings using a custom parameter group. This newly created MySQL DB cluster manages the user password lifetime by using the parameter `default_password_lifetime`. To optimize your database, you can apply additional setting in your custom parameter group and add options. 

 After you have finished creating your customized DB cluster, you should delete your resources to avoid incurring unwanted costs. To delete a DB cluster, follow the instructions in  [Deleting Aurora DB clusters and DB instances](USER_DeleteCluster.md). 