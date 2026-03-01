# Configuring Oracle Rest Data Services (ORDS)

The following topic lists the configuration options for ORDS 21 and 22:

###### Topics

- [Installing and configuring ORDS 21 and lower](#Appendix.Oracle.Options.APEX.ORDS "#Appendix.Oracle.Options.APEX.ORDS")
- [Installing and configuring ORDS 22 and higher](#Appendix.Oracle.Options.APEX.ORDS22 "#Appendix.Oracle.Options.APEX.ORDS22")

## Installing and configuring ORDS 21 and lower

You are now ready to install and configure Oracle Rest Data Services (ORDS)
for use with Oracle APEX. For Oracle APEX version 5.0 and later, use ORDS versions
19.1 to 21. To learn how to install ORDS 22 and higher, see [Installing and configuring ORDS 22 and higher](#Appendix.Oracle.Options.APEX.ORDS22 "#Appendix.Oracle.Options.APEX.ORDS22").

Install the listener on a separate host such as an Amazon EC2 instance, an on-premises
server at your company, or your desktop computer. For the examples in this section, we
assume that the name of your host is `myapexhost.example.com`, and that your
host is running Linux.

###### To install and configure ORDS 21 and lower for use with Oracle APEX

1. Go to [Oracle REST data services](https://www.oracle.com/database/technologies/appdev/rest-data-services-downloads-212.html "https://www.oracle.com/database/technologies/appdev/rest-data-services-downloads-212.html"), and examine the Readme. Make sure that
   you have the required version of Java installed.
2. Create a new directory for your ORDS installation.

```
mkdir /home/apexuser/ORDS
cd /home/apexuser/ORDS
```

3. Download the file
   `ords.`version.number`.zip` from
   [Oracle REST data services](https://www.oracle.com/database/technologies/appdev/rest-data-services-downloads-212.html "https://www.oracle.com/database/technologies/appdev/rest-data-services-downloads-212.html").
4. Unzip the file into the `/home/apexuser/ORDS`
   directory.
5. If you're installing ORDS in a multitenant database, add the following line to
   the file
   `/home/apexuser/ORDS/params/ords_params.properties`:

```
pdb.disable.lockdown=false
```

6. Grant the master user the required privileges to install ORDS.

After the options for Oracle APEX are installed, give the master user
the required privileges to install the ORDS schema. You can do this by
connecting to the database and running the following commands. Replace
`MASTER_USER` with the
uppercase name of your master user.

###### Important

When you enter the user name, use uppercase unless you created the user
with a case-sensitive identifier. For example, if you run `CREATE USER
 myuser` or `CREATE USER MYUSER`, the data dictionary
stores `MYUSER`. However, if you use double quotes in
`CREATE USER "MyUser"`, the data dictionary stores
`MyUser`. For more information, see [Granting SELECT or EXECUTE privileges to SYS objects](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").

```
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_OBJECTS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_ROLE_PRIVS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_TAB_COLUMNS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_CONS_COLUMNS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_CONSTRAINTS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_OBJECTS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_PROCEDURES', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_TAB_COLUMNS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_TABLES', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_VIEWS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('WPIUTL', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_SESSION', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_UTILITY', '`MASTER_USER`', 'EXECUTE', true);
```

###### Note

These commands apply to ORDS version 19.1 and later. 7. Install the ORDS schema using the downloaded ords.war file.

```
java -jar ords.war install advanced
```

The program prompts you for the following information. The default values are
in brackets. For more information, see [Introduction to Oracle REST data services](https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/20.2/aelig/installing-REST-data-services.html#GUID-6F7B4E61-B730-4E73-80B8-F53299123730 "https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/20.2/aelig/installing-REST-data-services.html#GUID-6F7B4E61-B730-4E73-80B8-F53299123730") in the Oracle
documentation.

    * Enter the location to store configuration data:


    Enter `/home/apexuser/ORDS`. This is the
     location of the ORDS configuration files.
    * Specify the database connection type to use. Enter number for [1]
     Basic [2] TNS [3] Custom URL [1]:


    Choose the desired connection type.
    * Enter the name of the database server [localhost]:
     `DB_instance_endpoint`


    Choose the default or enter the correct value.
    * Enter the database listener port [1521]:
     `DB_instance_port`


    Choose the default or enter the correct value.
    * Enter 1 to specify the database service name, or 2 to specify the
     database SID [1]:


    Choose `2` to specify the database SID.
    * Database SID [xe]


    Choose the default or enter the correct value.
    * Enter 1 if you want to verify/install Oracle REST Data Services schema
     or 2 to skip this step [1]:


    Choose `1`. This step creates the Oracle REST Data Services
     proxy user named ORDS\_PUBLIC\_USER.
    * Enter the database password for ORDS\_PUBLIC\_USER:


    Enter the password, and then confirm it.
    * Requires to login with administrator privileges to verify Oracle REST
     Data Services schema.


    Enter the administrator user name:
     `master_user`


    Enter the database password for
     `master_user`:
     `master_user_password`


    Confirm the password:
     `master_user_password`


    ###### Note

    Specify a password other than the prompt shown here as a security
     best practice.
    * Enter the default tablespace for ORDS\_METADATA [SYSAUX].


    Enter the temporary tablespace for ORDS\_METADATA [TEMP].


    Enter the default tablespace for ORDS\_PUBLIC\_USER [USERS].


    Enter the temporary tablespace for ORDS\_PUBLIC\_USER [TEMP].
    * Enter 1 if you want to use PL/SQL Gateway or 2 to skip this step. If
     you're using Oracle Application Express or migrating from mod\_plsql, you
     must enter 1 [1].


    Choose the default.
    * Enter the PL/SQL Gateway database user name [APEX\_PUBLIC\_USER]


    Choose the default.
    * Enter the database password for APEX\_PUBLIC\_USER:


    Enter the password, and then confirm it.
    * Enter 1 to specify passwords for Application Express RESTful Services
     database users (APEX\_LISTENER, APEX\_REST\_PUBLIC\_USER) or 2 to skip this
     step [1]:


    Choose `2` for APEX 4.1.1.V1; choose `1` for all
     other APEX versions.
    * [Not needed for APEX 4.1.1.v1] Database password for
     APEX\_LISTENER


    Enter the password (if required), and then confirm it.
    * [Not needed for APEX 4.1.1.v1] Database password for
     APEX\_REST\_PUBLIC\_USER


    Enter the password (if required), and then confirm it.
    * Enter a number to select a feature to enable:


    Enter `1` to enable all features: SQL Developer Web, REST
     Enabled SQL, and Database API.
    * Enter 1 if you wish to start in standalone mode or 2 to exit
     [1]:


    Enter `1`.
    * Enter the APEX static resources location:


    If you unzipped APEX installation files into
     `/home/apexuser`, enter
     `/home/apexuser/apex/images`. Otherwise, enter
     ``unzip_path`/apex/images`,
     where `unzip_path` is the directory where you
     unzipped the file.
    * Enter 1 if using HTTP or 2 if using HTTPS [1]:


    If you enter `1`, specify the HTTP port. If you enter
     `2`, specify the HTTPS port and the SSL host name. The
     HTTPS option prompts you to specify how you will provide the
     certificate:




    	+ Enter `1` to use the self-signed
    	 certificate.
    	+ Enter `2` to provide your own certificate. If you
    	 enter `2`, specify the path for the SSL certificate
    	 and the path for the SSL certificate private key.

8. Set a password for the APEX `admin` user. To do this, use SQL\*Plus
   to connect to your DB instance as the master user, and then run the following
   commands.

```
EXEC rdsadmin.rdsadmin_util.grant_apex_admin_role;
grant APEX_ADMINISTRATOR_ROLE to `master`;
@/home/apexuser/apex/apxchpwd.sql
```

Replace `master` with your master user
name. When the `apxchpwd.sql` script prompts you, enter a new
`admin` password. 9. Start the ORDS listener. Run the following code.

```
java -jar ords.war
```

The first time you start ORDS, you are prompted to provide the
location of the APEX Static resources. This images folder is located in the
`/apex/images` directory in the installation directory for
APEX. 10. Return to the Oracle APEX administration window in your browser and
choose **Administration**. Next, choose
**Application Express Internal Administration**. When
you are prompted for credentials, enter the following information:

    * User name – `admin`
    * Password – the password you set
     using the `apxchpwd.sql` script

Choose **Login**, and then set a new password for the
`admin` user.

Your listener is now ready for use.

## Installing and configuring ORDS 22 and higher

You are now ready to install and configure Oracle Rest Data Services (ORDS) for use
with Oracle APEX. For the examples in this section, we assume that the name of your
separate host is `myapexhost.example.com`, and that your host is running
Linux. The instructions for ORDS 22 differ from the instructions for previous
releases.

###### To install and configure ORDS 22 and higher for use with Oracle APEX

1. Go to [Oracle REST data services](http://www.oracle.com/technetwork/developer-tools/rest-data-services/downloads/index.html "http://www.oracle.com/technetwork/developer-tools/rest-data-services/downloads/index.html"), and examine the Readme for the ORDS
   version that you plan to download. Make sure that you have the required version
   of Java installed.
2. Create a new directory for your ORDS installation.

```
mkdir /home/apexuser/ORDS
cd /home/apexuser/ORDS
```

3. Download the file
   `ords.`version.number`.zip` or
   `ords-latest.zip` from [Oracle REST data services](http://www.oracle.com/technetwork/developer-tools/rest-data-services/downloads/index.html "http://www.oracle.com/technetwork/developer-tools/rest-data-services/downloads/index.html").
4. Unzip the file into the `/home/apexuser/ORDS`
   directory.
5. Grant the master user the required privileges to install ORDS.

After the `APEX` option is installed, give the master user
the required privileges to install the ORDS schema. You can do this by
logging in to the database and running the following commands. Replace
`MASTER_USER` with the
uppercase name of your master user.

###### Important

When you enter the user name, use uppercase unless you created the user
with a case-sensitive identifier. For example, if you run `CREATE USER
 myuser` or `CREATE USER MYUSER`, the data dictionary
stores `MYUSER`. However, if you use double quotes in
`CREATE USER "MyUser"`, the data dictionary stores
`MyUser`. For more information, see [Granting SELECT or EXECUTE privileges to SYS objects](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").

```
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_OBJECTS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_ROLE_PRIVS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_TAB_COLUMNS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_CONS_COLUMNS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_CONSTRAINTS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_OBJECTS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_PROCEDURES', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_TAB_COLUMNS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_TABLES', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('USER_VIEWS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('WPIUTL', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_SESSION', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_UTILITY', '`MASTER_USER`', 'EXECUTE', true);

exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_LOB', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_ASSERT', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_OUTPUT', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_SCHEDULER', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('HTP', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('OWA', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('WPG_DOCLOAD', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_CRYPTO', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_METADATA', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_SQL', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('UTL_SMTP', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_NETWORK_ACL_ADMIN', '`MASTER_USER`', 'EXECUTE', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('SESSION_PRIVS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_USERS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_NETWORK_ACL_PRIVILEGES', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_NETWORK_ACLS', '`MASTER_USER`', 'SELECT', true);
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_REGISTRY', '`MASTER_USER`', 'SELECT', true);
```

###### Note

The preceding commands apply to ORDS 22 and later. 6. Install the ORDS schema using the downloaded `ords` script. Specify
directories to contain configuration files and log files. Oracle Corporation
recommends not placing these directories inside the directory that contains the
ORDS product software.

```
mkdir -p /home/apexuser/ords_config /home/apexuser/ords_logs

/home/apexuser/ORDS/bin/ords \
  --config /home/apexuser/ords_config \
  install --interactive --log-folder /home/apexuser/ords_logs
```

For DB instances running the container database (CDB) architecture, use ORDS 23.3
or higher and pass the `--pdb-skip-disable-lockdown` argument when
installing ORDS.

```
/home/apexuser/ORDS/bin/ords \
  --config /home/apexuser/ords_config \
  install --interactive --log-folder /home/apexuser/ords_logs --pdb-skip-disable-lockdown
```

The program prompts you for the following information. The default values are
in brackets. For more information, see [Introduction to Oracle REST data services](https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/20.2/aelig/installing-REST-data-services.html#GUID-6F7B4E61-B730-4E73-80B8-F53299123730 "https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/20.2/aelig/installing-REST-data-services.html#GUID-6F7B4E61-B730-4E73-80B8-F53299123730") in the Oracle
documentation.

    * `Choose the type of installation:`


    Choose `2` to install ORDS schemas in the
     database and create a database connection pool in the local ORDS
     configuration files.
    * `Specify the database connection type to use. Enter number for
     [1] Basic [2] TNS [3] Custom URL:`


    Choose the desired connection type. This example assumes that you
     choose `1`.
    * `Enter the name of the database server [localhost]:`
    ``DB_instance_endpoint``


    Choose the default or enter the correct value.
    * `Enter the database listener port [1521]:`
    ``DB_instance_port``


    Choose the default `1521` or enter the correct
     value.
    * `Enter the database service name [orcl]:`


    Enter the database name used by your RDS for Oracle DB instance.
    * `Provide database user name with administrator
     privileges`


     Enter the master user name for your RDS for Oracle DB instance.
    * `Enter the database password for [username]:`


    Enter the master user password for your RDS for Oracle DB instance.
    * `Enter the default tablespace for ORDS_METADATA and
     ORDS_PUBLIC_USER [SYSAUX]:`
    * `Enter the temporary tablespace for ORDS_METADATA [TEMP]. Enter
     the default tablespace for ORDS_PUBLIC_USER [USERS]. Enter the
     temporary tablespace for ORDS_PUBLIC_USER [TEMP].`
    * `Enter a number to select additional feature(s) to enable
     [1]:`
    * `Enter a number to configure and start ORDS in standalone mode
     [1]:`


     Choose `2` to skip starting ORDS immediately in
     standalone mode.
    * `Enter a number to select the protocol [1] HTTP`
    * `Enter the HTTP port [8080]:`
    * `Enter the APEX static resources location:`


    Enter the path to the Oracle APEX installation files
     (`/home/apexuser/apex/images`).

7. Set a password for the Oracle APEX `admin` user. To do
   this, use SQL\*Plus to connect to your DB instance as the master user, and then run
   the following commands.

```
EXEC rdsadmin.rdsadmin_util.grant_apex_admin_role;
grant APEX_ADMINISTRATOR_ROLE to `master`;
@/home/apexuser/apex/apxchpwd.sql
```

Replace `master` with your master user
name. When the `apxchpwd.sql` script prompts you, enter a new
`admin` password. 8. Run ORDS in standalone mode using the `ords` script with the
`serve` command. For production deployments, consider using
supported Java EE application servers such as Apache Tomcat or Oracle WebLogic
Server. For more information, see [Deploying and Monitoring Oracle REST Data Services](https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/23.1/ordig/deploying-and-monitoring-oracle-rest-data-services.html#GUID-6791F5DF-AC67-4885-BFFA-B80964C17EC9 "https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/23.1/ordig/deploying-and-monitoring-oracle-rest-data-services.html#GUID-6791F5DF-AC67-4885-BFFA-B80964C17EC9") in the Oracle
Database documentation.

```
/home/apexuser/ORDS/bin/ords \
  --config /home/apexuser/ords_config serve \
  --port 8193 \
  --apex-images /home/apexuser/apex/images
```

If ORDS is running but unable to access the Oracle APEX installation,
you might see the following error, particularly on non-CDB instances.

```
The procedure named apex_admin could not be accessed, it may not be declared, or the user executing this request may not have been granted execute privilege on the procedure, or a function specified by security.requestValidationFunction configuration property has prevented access.
```

To fix this error, change the request validation function used by ORDS by
running the `ords` script with the `config` command. By
default, ORDS uses the `ords_util.authorize_plsql_gateway` procedure,
which is only supported on CDB instances. For non-CDB instances, you can change
this procedure to the `wwv_flow_epg_include_modules.authorize`
package. See the Oracle Database documentation and Oracle Support for best
practices on configuring the proper request validation function for your use
case. 9. Return to the Oracle APEX administration window in your browser and
choose **Administration**. Next, choose
**Application Express Internal Administration**. When
you are prompted for credentials, enter the following information:

    * User name – `admin`
    * Password – the password you set
     using the `apxchpwd.sql` script

Choose **Login**, and then set a new password for the
`admin` user.

Your listener is now ready for use.
