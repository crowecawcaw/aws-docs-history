# Tutorial: Creating a MySQL DB instance with a custom parameterand new option group

In this tutorial, you create a MySQL DB instance
with a custom
parameter and new option group.
For more information about
custom parameter
and option groups, see
[Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md") and
[Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md").

###### Important

There's no charge for creating an AWS account. However, by completing this tutorial, you might incur
costs for the AWS resources you use. You can delete these resources after you complete the tutorial
if they are no longer needed.

To create a DB instance
with custom configurations and settings, you can use custom
parameter and new option groups.
Custom parameter and new option groups are particularly helpful if you work with multiple
databases and want to uniformly configure settings for them.

By completing these steps, you learn:

- How to use Amazon RDS to
  create a MySQL DB instance with
  a custom parameter and new option group.
- How to use specific
  parameters and options for MySQL
  DB instances.
  To complete this tutorial, perform the following tasks:

1. Create a custom
   parameter group with the MySQL parameters
   `default_password_lifetime`and `disconnect_on_expired_password`.
2. Create a new option group with MySQL option feature
   `MariaDB Audit Plugin`. For steps to create an option group, see
   [Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md").
3. Create a MySQL DB instance
   with the custom parameter group
   and new option group that you created.

###### Topics

- [Prerequisites](#tutorial-creating-custom-OPG.Prerequisites "#tutorial-creating-custom-OPG.Prerequisites")
- [Create an Amazon RDS parameter group](#tutorial-creating-custom-OPG.create-parameter-group "#tutorial-creating-custom-OPG.create-parameter-group")
- [Modify parameter values in your custom parameter group](#tutorial-creating-custom-OPG.add-parameters "#tutorial-creating-custom-OPG.add-parameters")
- [Create a new Amazon RDS option group](#tutorial-creating-custom-OPG.create-option-group "#tutorial-creating-custom-OPG.create-option-group")
- [Add a option to your new option group](#tutorial-creating-custom-OPG.add-options "#tutorial-creating-custom-OPG.add-options")
- [Create MySQL DB instance with a custom parameter and a new option group](#tutorial-creating-custom-OPG.create-OPG "#tutorial-creating-custom-OPG.create-OPG")

## Prerequisites

This tutorial requires you to have an AWS account and a user with administrative access.
If you don't already have those set up, complete the steps in the following sections:

- [Sign up for an AWS account](CHAP_SettingUp.md#sign-up-for-aws "CHAP_SettingUp.md#sign-up-for-aws")
- [Create a user with administrative access](CHAP_SettingUp.md#create-an-admin "CHAP_SettingUp.md#create-an-admin")

## Create an Amazon RDS parameter group

In this tutorial, you learn how to create a custom parameter group with
[default_password_lifetime](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_password_lifetime "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_password_lifetime") and
[disconnect_on_expired_password](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_disconnect_on_expired_password "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_disconnect_on_expired_password")
for a MySQL DB instance in the console.

The `default_password_lifetime` parameter controls the number of days before the client password automatically expires. The `disconnect_on_expired_password`
parameter controls whether the MySQL DB instance disconnects the client when the password expires.
For more information on other parameters available for MySQL DB instances, see
[Parameters for MySQL](Appendix.MySQL.md "Appendix.MySQL.md")

.

###### To create a parameter group

1. Open the Amazon RDS console and choose
   **Parameter groups**.
2. For **Custom parameter groups**, choose
   **Create parameter group**.
3. Set the parameter group details.
   1. Enter a name for the parameter group.
   2. Enter a description of the parameter group.
   3. For **Engine type**, choose
      **MySQL Community.**
   4. For **Parameter group family**, choose
      **MySQL 8.0.**

4. Choose
   **Create**.

The new parameter group appears on the
**Parameter groups** page in the Amazon RDS console. The following steps illustrate how to modify parameter values
to customize your parameter group.

## Modify parameter values in your custom parameter group

Use the following steps to modify the parameter values
in the parameter group that you created in
[Create an Amazon RDS parameter group](#tutorial-creating-custom-OPG.create-parameter-group "#tutorial-creating-custom-OPG.create-parameter-group").

###### To modify parameter values in your parameter group

1. Open the Amazon RDS console and choose
   **Parameter groups**.
2. For **Custom parameter groups**, choose the name of the parameter group you created.
3. Choose
   **Edit**.
4. In the **Filter parameters** search box, search for the
   custom parameter
   `default_password_lifetime`.
5. Select the check box next to the parameter and enter a value the number of days to set for this password lifetime parameter.
6. Select **Save Changes**.
7. Repeat the same steps for the parameter
   `disconnect_on_expired_password`. When you choose this parameter, you are prompted to select a value of 0 or 1 from the dropdown menu.
   Select 1 to disconnect on expired password.

The custom parameter group
is now available to associate with Amazon RDS for
MySQL 8.0 DB instance.
Next, create a new option group for your DB instance.

## Create a new Amazon RDS option group

Create a new option group with the option
[MariaDB Audit Plugin](Appendix.MySQL.Options.md "Appendix.MySQL.Options.md").
This plugin logs server activity for security and compliance. For more information on other custom options available for MySQL DB instances, see
[Options for MySQL DB instances](Appendix.MySQL.md "Appendix.MySQL.md").

###### To create an option group

1. Open the Amazon RDS console and choose
   **Option groups**.
2. For **Option Groups**, choose
   **Create group**.
3. Set the option group details.
   - Enter a name for the option group.
   - Enter a description of the option group.
   - For **Engine**, select
     **mysql**.
   - For **Major engine version**, select
     **8.0**.

4. Choose
   **Create**.

The new option group appears on the
**Option groups** page in the Amazon RDS console. The following steps show how to add options to the option group.

## Add a option to your new option group

Use the following steps to add a option to the new option group that you created in
[Create a new Amazon RDS option group](#tutorial-creating-custom-OPG.create-option-group "#tutorial-creating-custom-OPG.create-option-group").

###### To add an option to your option group

1. Open the Amazon RDS console and choose
   **Option groups**.
2. For **Option groups**, select the name of the option group that you created.
3. Under **Options**, choose
   **Add option**.
4. Set the option group details.
   - For **Option name**, choose the option MariaDB Audit Plugin,
     **MARIADB_AUDIT_PLUGIN**.
   - For **Option settings**, leave all the default options selected.
   - For **Apply immediately**, choose
     **Yes**.

5. Choose
   **Create option**.

The new option group should now be available for all associated DB instances. Next, create a MySQL DB instance with the custom parameter and new option group.

## Create MySQL DB instance with a custom parameter and a new option group

Finally, create a MySQL DB instance with the
custom parameter
and new option group that you made in the previous steps. The following steps show
how to create the MySQL DB instance with your
custom parameter and new option group.

###### To create a DB instance with a custom parameter and new option group

1. Open the Amazon RDS console and choose **Databases**.
2. Choose **Create database**.
3. For **Choose a database creation method**, choose **Standard Create**.
4. For **Engine options**, choose
   **MySQL**
   .
5. For **Availability and durability**, choose **Single DB instance.** This step is necessary to support a custom parameter or new option group.
6. Select **Additional Configuration**.
   - For **Initial database name**, choose a name for your DB instance.
   - Under the **DB parameter group** dropdown, select the name of the
     custom parameter group you created previously.
   - Under **Option group** dropdown, select the name of new option group you created previously.

7. For this tutorial, you can leave the default settings for any other DB settings or modify them as required.
8. Choose **Create database**.

RDS creates a new MySQL DB instance with a
custom parameter groupand new option group. To see more information on this database,
see the **Databases** page of the Amazon RDS console.

In this tutorial, you configured a MySQL DB instance
with tailored settings using a custom parameter and a new option group.
This newly created MySQL DB instance
manages the user password lifetime by using the parameter `default_password_lifetime`.
This DB instance
also disconnects users that connect with an expired password by using the parameter `disconnect_on_expired_password`.
You also use the option `MariaDB Audit Plugin` to keep track of server activity.
To optimize your database, you can apply additional setting in your custom parameter group and add options.

After you have finished creating your customized DB instance,
you should delete your resources to avoid incurring unwanted costs. To delete a DB instance,
follow the instructions in [Deleting a DB instance](USER_DeleteInstance.md "USER_DeleteInstance.md").
