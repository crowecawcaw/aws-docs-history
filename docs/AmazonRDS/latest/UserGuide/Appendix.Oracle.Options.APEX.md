# Setting up Oracle APEX and

Oracle Rest Data Services (ORDS)

The following topic lists the steps required to set up Oracle APEX and ORDS

###### Topics

- [Adding the APEX and APEX-DEV options
  to your DB instance](#Appendix.Oracle.Options.APEX.Add "#Appendix.Oracle.Options.APEX.Add")
- [Unlocking the public user
  account on your DB instance](#Appendix.Oracle.Options.APEX.PublicUser "#Appendix.Oracle.Options.APEX.PublicUser")
- [Configuring RESTful services for Oracle APEX](#Appendix.Oracle.Options.APEX.ConfigureRESTful "#Appendix.Oracle.Options.APEX.ConfigureRESTful")
- [Preparing to install ORDS
  on a separate host](#Appendix.Oracle.Options.APEX.ORDS.ords-setup "#Appendix.Oracle.Options.APEX.ORDS.ords-setup")
- [Setting up Oracle APEX listener](#Appendix.Oracle.Options.APEX.Listener "#Appendix.Oracle.Options.APEX.Listener")

## Adding the APEX and APEX-DEV options

to your DB instance

To add the `APEX` and `APEX-DEV` options to your RDS for Oracle DB instance,
do the following:

1. Create a new option group, or copy or modify an existing option group.
2. Add the `APEX` and `APEX-DEV` options to the option
   group.
3. Associate the option group with your DB instance.

When you add the `APEX` and `APEX-DEV` options, a brief
outage occurs while your DB instance is automatically restarted.

###### Note

`APEX_MAIL` is available when the `APEX` option is
installed. The execute privilege for the `APEX_MAIL` package is granted
to `PUBLIC` so you don't need the APEX administrative account to use
it.

###### To add the APEX and APEX-DEV options to a DB instance

1. Determine the option group that you want to use. You can create a new option
   group or use an existing option group. If you want to use an existing option
   group, skip to the next step. Otherwise, create a custom DB option group with
   the following settings:
   1. For **Engine**, choose the Oracle edition that
      you want to use. The `APEX` and `APEX-DEV`
      options are supported on all editions.
   2. For **Major engine version**, choose
      the version of your DB instance.For more information, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create").

2. Add the options to the option group. If you want to deploy only the Oracle
   APEX runtime environment, add only the `APEX` option. To deploy the
   full development environment, add both the `APEX` and
   `APEX-DEV` options.

For **Version**, choose the version of Oracle APEX that
you want to use.

###### Important

If you add the `APEX` or `APEX-DEV` options to
an existing option group that is already attached to one or more DB instances,
a brief outage occurs. During this outage, all the DB instances are
automatically restarted.

For more information about adding options, see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption"). 3. Apply the option group to a new or existing DB instance:

    * For a new DB instance, you apply the option group when you launch the
     instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
    * For an existing DB instance, you apply the option group by modifying the
     instance and attaching the new option group. When you add the
     `APEX` or `APEX-DEV` options to an
     existing DB instance, a brief outage occurs while your DB instance is
     automatically restarted. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Unlocking the public user

account on your DB instance

After you have installed the `APEX` or `APEX-DEV` options
your DB instance, make sure to do the following:

1. Change the password for the `APEX_PUBLIC_USER` account.
2. Unlock the account.

You can do this by using the Oracle SQL\*Plus command line utility. Connect to your DB instance as the master
user, and issue the following commands. Replace `new_password` with a password of your choice.

```
ALTER USER APEX_PUBLIC_USER IDENTIFIED BY `new_password`;
ALTER USER APEX_PUBLIC_USER ACCOUNT UNLOCK;
```

## Configuring RESTful services for Oracle APEX

To configure RESTful services in Oracle APEX (not needed for Oracle APEX
4.1.1.V1), use SQL\*Plus to connect to your DB instance as the master user. After you do
this, run the `rdsadmin.rdsadmin_run_apex_rest_config` stored procedure.
When you run the stored procedure, you provide passwords for the following
users:

- `APEX_LISTENER`
- `APEX_REST_PUBLIC_USER`

The stored procedure runs the `apex_rest_config.sql` script, which creates
new database accounts for these users.

###### Note

Configuration isn't required for Oracle APEX version 4.1.1.v1. For this
Oracle APEX version only, you don't need to run the stored procedure.

The following command runs the stored procedure.

```
EXEC rdsadmin.rdsadmin_run_apex_rest_config('`apex_listener_password`', '`apex_rest_public_user_password`');
```

## Preparing to install ORDS

on a separate host

Install ORDS on a separate host such as an Amazon EC2 instance, an on-premises server at
your company, or your desktop computer. The examples in this section,assume that your
host runs Linux and is named `myapexhost.example.com`.

Before you can install ORDS, you need to create a nonprivileged OS user, and then
download and unzip the Oracle APEX installation file.

###### To prepare for ORDS installation

1. Log in to `myapexhost.example.com` as `root`.
2. Create a nonprivileged OS user to own the listener installation. The following
   command creates a new user named _apexuser_.

```
useradd -d /home/apexuser `apexuser`
```

The following command assigns a password to the new user.

```
passwd apexuser;
```

3. Log in to `myapexhost.example.com` as `apexuser`,
   and download the Oracle APEX installation file from Oracle to your
   `/home/apexuser` directory:
   - [http://www.oracle.com/technetwork/developer-tools/apex/downloads/index.html](http://www.oracle.com/technetwork/developer-tools/apex/downloads/index.html "http://www.oracle.com/technetwork/developer-tools/apex/downloads/index.html")
   - [Oracle application Express prior release archives](http://www.oracle.com/technetwork/developer-tools/apex/downloads/all-archives-099381.html "http://www.oracle.com/technetwork/developer-tools/apex/downloads/all-archives-099381.html")

4. Unzip the file in the `/home/apexuser` directory.

```
unzip apex_`version`.zip
```

After you unzip the file, there is an `apex` directory in the
`/home/apexuser` directory. 5. While you are still logged into `myapexhost.example.com` as
`apexuser`, download the Oracle REST Data Services file from
Oracle to your `/home/apexuser` directory: [http://www.oracle.com/technetwork/developer-tools/apex-listener/downloads/index.html](http://www.oracle.com/technetwork/developer-tools/apex-listener/downloads/index.html "http://www.oracle.com/technetwork/developer-tools/apex-listener/downloads/index.html").

## Setting up Oracle APEX listener

###### Note

Oracle APEX Listener is deprecated.

Amazon RDS for Oracle continues to support Oracle APEX version 4.1.1 and Oracle APEX
Listener version 1.1.4. We recommend that you use the latest supported versions of
Oracle APEX and ORDS.

Install Oracle APEX Listener on a separate host such as an Amazon EC2 instance, an
on-premises server at your company, or your desktop computer. We assume that the name of
your host is `myapexhost.example.com`, and that your host is running
Linux.

### Preparing to install Oracle APEX listener

Before you can install Oracle APEX Listener, you need to create a
nonprivileged OS user, and then download and unzip the Oracle APEX installation
file.

###### To prepare for Oracle APEX listener installation

1. Log in to `myapexhost.example.com` as `root`.
2. Create a nonprivileged OS user to own the listener installation. The
   following command creates a new user named _apexuser_.

```
useradd -d /home/apexuser `apexuser`
```

The following command assigns a password to the new user.

```
passwd apexuser;
```

3. Log in to `myapexhost.example.com` as
   `apexuser`, and download the Oracle APEX installation file
   from Oracle to your `/home/apexuser` directory:
   - [http://www.oracle.com/technetwork/developer-tools/apex/downloads/index.html](http://www.oracle.com/technetwork/developer-tools/apex/downloads/index.html "http://www.oracle.com/technetwork/developer-tools/apex/downloads/index.html")
   - [Oracle application Express prior release archives](http://www.oracle.com/technetwork/developer-tools/apex/downloads/all-archives-099381.html "http://www.oracle.com/technetwork/developer-tools/apex/downloads/all-archives-099381.html")

4. Unzip the file in the `/home/apexuser` directory.

```
unzip apex_`<version>`.zip
```

After you unzip the file, there is an `apex` directory in the
`/home/apexuser` directory. 5. While you are still logged into `myapexhost.example.com` as
`apexuser`, download the Oracle APEX Listener file from
Oracle to your `/home/apexuser` directory.

#### Installing and configuring Oracle APEX listener

Before you can use Oracle APEX, you need to download the
`apex.war` file, use Java to install Oracle APEX Listener,
and then start the listener.

###### To install and configure Oracle APEX listener

1. Create a new directory based on Oracle APEX Listener and open the listener
   file.

Run the following code:

```
mkdir /home/apexuser/apexlistener
cd /home/apexuser/apexlistener
unzip ../apex_listener.`version`.zip
```

2. Run the following code.

```
java -Dapex.home=./apex -Dapex.images=/home/apexuser/apex/images -Dapex.erase -jar ./apex.war
```

3.  Enter information for the program prompts following:

        * The APEX Listener Administrator user name. The default is
         *adminlistener*.
        * A password for the APEX Listener Administrator.
        * The APEX Listener Manager user name. The default is
         *managerlistener*.
        * A password for the APEX Listener Administrator.

    The program prints a URL that you need to complete the configuration, as
    follows.

```
INFO: Please complete configuration at: http://localhost:8080/apex/listenerConfigure
Database is not yet configured
```

4. Leave Oracle APEX Listener running so that you can use Oracle Application
   Express. When you have finished this configuration procedure, you can run
   the listener in the background.
5. From your web browser, go to the URL provided by the Oracle APEX
   Listener program. The Oracle Application Express Listener
   administration window appears. Enter the following information:
   - Username –
     `APEX_PUBLIC_USER`
   - Password – the
     password for _APEX_PUBLIC_USER_. This
     password is the one that you specified earlier when you
     configured the Oracle APEX repository. For more information,
     see [Unlocking the public user
     account on your DB instance](#Appendix.Oracle.Options.APEX.PublicUser "#Appendix.Oracle.Options.APEX.PublicUser").
   - Connection type – Basic
   - Hostname – the endpoint of
     your Amazon RDS DB instance, such as
     `mydb.f9rbfa893tft.us-east-1.rds.amazonaws.com`.
   - Port – 1521
   - SID – the name of the
     database on your Amazon RDS DB instance, such as `mydb`.

6. Choose **Apply**. The Oracle APEX administration
   window appears.
7. Set a password for the Oracle APEX `admin` user. To do
   this, use SQL\*Plus to connect to your DB instance as the master user, and
   then run the following commands.

```
EXEC rdsadmin.rdsadmin_util.grant_apex_admin_role;
grant APEX_ADMINISTRATOR_ROLE to `master`;
@/home/apexuser/apex/apxchpwd.sql
```

Replace `master` with your master
user name. When the `apxchpwd.sql` script prompts you, enter a
new `admin` password. 8. Return to the Oracle APEX administration window in your browser
and choose **Administration**. Next, choose
**Application Express Internal
Administration**. When you are prompted for credentials,
enter the following information:

    * User name –
     `admin`
    * Password – the password you
     set using the `apxchpwd.sql` script

Choose **Login**, and then set a new password for the
`admin` user.

Your listener is now ready for use.
