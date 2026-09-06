

# Oracle Management Agent for Enterprise Manager Cloud Control
<a name="Oracle.Options.OEMAgent"></a>

Oracle Enterprise Manager (OEM) Management Agent is a software component that monitors targets running on hosts and communicates that information to the middle-tier Oracle Management Service (OMS). Amazon RDS supports Management Agent through the use of the `OEM_AGENT` option. 

For more information, see [Overview of Oracle Enterprise Manager Cloud Control](https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emcon/overview-oracle-enterprise-manager-cloud-control.html) in the Oracle documentation.

**Topics**
+ [Requirements for Management Agent](#Oracle.Options.OEMAgent.PreReqs)
+ [OMS host communication prerequisites](#Oracle.Options.OEMAgent.PreReqs.host)
+ [Limitations for Management Agent](#Oracle.Options.OEMAgent.limitations)
+ [Option settings for Management Agent](#Oracle.Options.OEMAgent.Options)
+ [Enabling the Management Agent option for your DB instance](#Oracle.Options.OEMAgent.Enable)
+ [Removing the Management Agent option](#Oracle.Options.OEMAgent.Remove)
+ [Performing database tasks with the Management Agent](#Oracle.Options.OEMAgent.DBTasks)

## Requirements for Management Agent
<a name="Oracle.Options.OEMAgent.PreReqs"></a>

Following are general requirements for using Management Agent: 
+ You can use either the CDB or non-CDB architecture.
+ You must use an Oracle Management Service (OMS) that is configured to connect to your DB instance. Note the following OMS requirements:
  + Management Agent version 24.1.0.0.v1 requires OMS version 24.1.
  + Management Agent versions 13.5.0.0.v2 and 13.5.0.0.v3 require OMS version 13.5.0.23 or 24.1.
  + Management Agent version 13.5.0.0.v1 requires OMS version 13.5.0.0 or 24.1.
  + Management Agent versions 13.4.0.9.v1 and 13.4.0.9.v2 require OMS version 13.4.0.9 or later and patch 32198287.
+ In most cases, you must configure your VPC to allow connections from OMS to your DB instance. If you aren't familiar with Amazon Virtual Private Cloud (Amazon VPC), we recommend that you complete the steps in [Tutorial: Create a VPC for use with a DB instance (IPv4 only)](CHAP_Tutorials.WebServerDB.CreateVPC.md) before continuing. 
+ You can use Management Agent with Oracle Enterprise Manager Cloud Control for 12c and 13c. Ensure that you have sufficient storage space for your OEM release:
  + At least 8.5 GiB for OEM 24.1 Release 1
  + At least 8.5 GiB for OEM 13c Release 5
  + At least 8.5 GiB for OEM 13c Release 4
  + At least 8.5 GiB for OEM 13c Release 3
  + At least 5.5 GiB for OEM 13c Release 2
  + At least 4.5 GiB for OEM 13c Release 1
  + At least 2.5 GiB for OEM 12c
+ If you're using Management Agent versions `OEM_AGENT 13.2.0.0.v3` and `13.3.0.0.v2`, and if you want to use TCPS connectivity, follow the instructions in [Configuring third party CA certificates for communication with target databases](https://docs.oracle.com/cd/E73210_01/EMSEC/GUID-8337AD48-1A32-4CD5-84F3-256FAE93D043.htm#EMSEC15996) in the Oracle documentation. Also, update the JDK on your OMS by following the instructions in the Oracle document with the Oracle Doc ID 2241358.1. This step ensures that OMS supports all the cipher suites that the database supports.
**Note**  
TCPS connectivity between the Management Agent and the DB instance is supported for Management Agent `OEM_AGENT 13.2.0.0.v3`, `13.3.0.0.v2`, `13.4.0.9.v1`, and higher versions.

## OMS host communication prerequisites
<a name="Oracle.Options.OEMAgent.PreReqs.host"></a>

Make sure that your OMS host and your Amazon RDS DB instance can communicate. Do the following: 
+ To connect from the Management Agent to your OMS host when your OMS host is behind a firewall, add the IP addresses of your DB instances to the firewall. Make sure the firewall for the OMS allows the following network traffic:  
From the OMS host to your DB instance  
Configure a one-way firewall rule that allows traffic from the OMS host to the database listener port (default 1521) and the OEM Agent port (default 3872).  
From your DB instance to the OMS host  
Configure a one-way firewall rule that allows traffic from the DB instance to the OMS HTTP port (default 4903).
+ To connect from your OMS to the Management Agent, if your OMS has a publicly resolvable host name, add the OMS address to a security group. Your security group must have inbound rules that allow access to the DB listener port and the Management Agent port. For an example of creating a security and adding inbound rules, see [Tutorial: Create a VPC for use with a DB instance (IPv4 only)](CHAP_Tutorials.WebServerDB.CreateVPC.md). 
+ To connect from your OMS to the Management Agent, if your OMS doesn't have a publicly resolvable host name, use one of the following: 
  + If your OMS is hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance in a private VPC, you can set up VPC peering to connect from OMS to Management Agent. For more information, see [A DB instance in a VPC accessed by an EC2 instance in a different VPC](USER_VPC.Scenarios.md#USER_VPC.Scenario3). 
  + If your OMS is hosted on-premises, you can set up a VPN connection to allow access from OMS to Management Agent. For more information, see [A DB instance in a VPC accessed by a client application through the internet](USER_VPC.Scenarios.md#USER_VPC.Scenario4) or [VPN connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html). 
+ To connect OEM Management Agent version 13.5.0.0 (v1-v3) or 24.1.0.0.v1 to a 24.1 OMS host, set `MINIMUM_TLS_VERSION` to use the TLS 1.2 protocol `TLSv1.2` in your configuration options.

## Limitations for Management Agent
<a name="Oracle.Options.OEMAgent.limitations"></a>

Following are some limitations to using Management Agent: 
+ You can't provide custom Oracle Management Agent images.
+ Administrative tasks such as job execution and database patching, that require host credentials, aren't supported. 
+ Host metrics and the process list aren't guaranteed to reflect the actual system state. Thus, you shouldn't use OEM to monitor the root file system or mount point file system. For more information about monitoring the operating system, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.OS.md).
+ Autodiscovery isn't supported. You must manually add database targets. 
+ OMS module availability depends on your database edition. For example, the database performance diagnosis and tuning module is only available for Oracle Database Enterprise Edition. 
+ Management Agent consumes additional memory and computing resources. If you experience performance problems after enabling the `OEM_AGENT` option, we recommend that you scale up to a larger DB instance class. For more information, see [DB instance classes](Concepts.DBInstanceClass.md) and [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md). 
+ The user running the `OEM_AGENT` on the Amazon RDS host doesn't have operating system access to the alert log. Thus, you can't collect metrics for `DB Alert Log` and `DB Alert Log Error Status` in OEM.

## Option settings for Management Agent
<a name="Oracle.Options.OEMAgent.Options"></a>

Amazon RDS supports the following settings for the Management Agent option.

**Note**  
For Oracle Database 26ai, the Management Agent option has the following requirements:  
The only supported Management Agent version is `24.1.0.0.v1`.
Only the following TLS cipher suites are supported:  
TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256
TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384
TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384
TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384


| Option setting | Required | Valid values | Description | 
| --- | --- | --- | --- | 
| **Version** (`AGENT_VERSION`) | Yes | `24.1.0.0.v1`<br />`13.5.0.0.v3`<br />`13.5.0.0.v2`<br />`13.5.0.0.v1`<br />`13.4.0.9.v2`<br />`13.4.0.9.v1`<br />`13.3.0.0.v2`<br />`13.3.0.0.v1`<br />`13.2.0.0.v3`<br />`13.2.0.0.v2`<br />`13.2.0.0.v1`<br />`13.1.0.0.v1` | The version of the Management Agent software. The minimum supported version is `13.1.0.0.v1`.<br />The AWS CLI option name is `OptionVersion`. In the AWS GovCloud (US) Regions, 13.1 versions aren't available.  For Oracle Database 26ai, the only supported agent version is `24.1.0.0.v1`.  | 
| **Port** (`AGENT_PORT`) | Yes | An integer value | The port on the DB instance that listens for the OMS host. The default is 3872. Your OMS host must belong to a security group that has access to this port. <br />The AWS CLI option name is `Port`. | 
| **Security Groups** | Yes | Existing security groups | A security group that has access to **Port**. Your OMS host must belong to this security group. <br />The AWS CLI option name is `VpcSecurityGroupMemberships` or `DBSecurityGroupMemberships`. | 
| **OMS\_HOST** | Yes | A string value, for example {{my.example.oms}}  | The publicly accessible host name or IP address of the OMS. <br />The AWS CLI option name is `OMS_HOST`. | 
| **OMS\_PORT** | Yes | An integer value | The HTTPS upload port on the OMS Host that listens for the Management Agent. <br />To determine the HTTPS upload port, connect to the OMS host, and run the following command (which requires the `SYSMAN` password):emctl status oms -details <br />The AWS CLI option name is `OMS_PORT`. | 
| **AGENT\_REGISTRATION\_PASSWORD** | Yes | A string value | The password that the Management Agent uses to authenticate itself with the OMS. We recommend that you create a persistent password in your OMS before enabling the `OEM_AGENT` option. With a persistent password you can share a single Management Agent option group among multiple Amazon RDS databases. <br />The AWS CLI option name is `AGENT_REGISTRATION_PASSWORD`. | 
| **ALLOW\_TLS\_ONLY** | No | `true`, `false` (default) | A value that configures the OEM Agent to support only the `TLSv1` protocol while the agent listens as a server. This setting is no longer supported. Management Agent versions 13.1.0.0.v1 and higher support Transport Layer Security (TLS) by default.  | 
| **MINIMUM\_TLS\_VERSION** | No | `TLSv1` (default), `TLSv1.2` | A value that specifies the minimum TLS version supported by the OEM Agent while the agent listens as a server. Desupported agent versions only support the `TLSv1` setting.<br />To connect 13.5.0.0 (v1-v3) or 24.1.0.0.v1 to a 24.1 OMS host, set this to `TLSv1.2`. | 
| **TLS\_CIPHER\_SUITE** | No | See [Option settings for Management Agent](#Oracle.Options.OEMAgent.Options). | A value that specifies the TLS cipher suite used by the OEM Agent while the agent listens as a server.  | 

The following table lists the TLS cipher suites that the Management Agent option supports.


| Cipher suite | Agent version supported | FedRAMP compliant | Supported Oracle versions | 
| --- | --- | --- | --- | 
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA | All | No | 19c, 21c | 
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | 13.1.0.0.v1 and higher | No | 19c, 21c | 
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA | 13.2.0.0.v3 and higher | No | 19c, 21c | 
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256 | 13.2.0.0.v3 and higher | No | 19c, 21c, 26ai | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA | 13.2.0.0.v3 and higher | Yes | 19c, 21c | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA | 13.2.0.0.v3 and higher | Yes | 19c, 21c | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | 13.2.0.0.v3 and higher | Yes | 19c, 21c | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 | 13.2.0.0.v3 and higher | Yes | 19c, 21c, 26ai | 
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 | 13.4.0.9.v1 and higher | Yes | 19c, 21c, 26ai | 
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 | 13.4.0.9.v1 and higher | Yes | 19c, 21c, 26ai | 

### Certificate compatibility with cipher suites
<a name="Oracle.Options.OEMAgent.CertificateCompatibility"></a>

RDS for Oracle supports both RSA and Elliptic Curve Digital Signature Algorithm (ECDSA) certificates. When you configure the OEM Agent option for your DB instance, you must ensure that the cipher suites you specify in the `TLS_CIPHER_SUITE` option setting are compatible with the certificate type used by your DB instance.

The following table shows the compatibility between certificate types and cipher suites:


| Certificate type | Compatible cipher suites | Incompatible cipher suites | 
| --- | --- | --- | 
| RSA certificates (rds-ca-2019, rds-ca-rsa2048-g1, rds-ca-rsa4096-g1) | TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA<br />TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256<br />TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA<br />TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 | TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384<br />TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 | 
| ECDSA certificates (rds-ca-ecc384-g1) | TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384<br />TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 | TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA<br />TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256<br />TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA<br />TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 | 

When you specify a cipher suite in the `TLS_CIPHER_SUITE` option setting, make sure it is compatible with the certificate type used by your DB instance. If you attempt to associate an option group with an OEM Agent option that contains a cipher suite incompatible with the certificate type of a DB instance, the operation will fail with an error message indicating the incompatibility.

## Enabling the Management Agent option for your DB instance
<a name="Oracle.Options.OEMAgent.Enable"></a>

To enable the Management Agent option, use the following steps:

**Topics**
+ [Step 1: Adding the Management Agent option to your DB instance](#Oracle.Options.OEMAgent.Add)
+ [Step 2: Unlocking the DBSNMP user account](#Oracle.Options.OEMAgent.DBSNMP)
+ [Step 3: Adding your targets to the Management Agent console](#Oracle.Options.OEMAgent.Using)

### Step 1: Adding the Management Agent option to your DB instance
<a name="Oracle.Options.OEMAgent.Add"></a>

To add the Management Agent option to your DB instance, do the following:

1. Create a new option group, or copy or modify an existing option group.

1. Add the option to the option group.

1. Associate the option group with the DB instance.

If you encounter errors, check [My Oracle Support](https://support.oracle.com/) documents for information about resolving specific problems.

After you add the Management Agent option, you don't need to restart your DB instance. As soon as the option group is active, the OEM Agent is active. 

If your OMS host is using an untrusted third-party certificate, Amazon RDS returns the following error.

```
You successfully installed the OEM_AGENT option. Your OMS host is using an untrusted third party certificate. 
Configure your OMS host with the trusted certificates from your third party.
```

If this error is returned, the Management Agent option isn't enabled until the problem is corrected. For information about correcting the problem, see the My Oracle Support document [2202569.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=2202569.1).

#### Console
<a name="Oracle.Options.OEMAgent.Add.Console"></a>

**To add the Management Agent option to your DB instance**

1. Determine the option group you want to use. You can create a new option group or use an existing option group. If you want to use an existing option group, skip to the next step. Otherwise, create a custom DB option group with the following settings: 

   1. For **Engine** choose the oracle edition for your DB instance. 

   1. For **Major engine version** choose the version of your DB instance. 

   For more information, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create). 

1. Add the **OEM\_AGENT** option to the option group, and configure the option settings. For more information about adding options, see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption). For more information about each setting, see [Option settings for Management Agent](#Oracle.Options.OEMAgent.Options). 

1. Apply the option group to a new or existing DB instance: 
   + For a new DB instance, you apply the option group when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md). 
   + For an existing DB instance, you apply the option group by modifying the instance and attaching the new option group. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md). 

#### AWS CLI
<a name="Oracle.Options.OEMAgent.Add.CLI"></a>

The following example uses the AWS CLI [add-option-to-option-group](https://docs.aws.amazon.com/cli/latest/reference/rds/add-option-to-option-group.html) command to add the `OEM_AGENT` option to an option group called `myoptiongroup`. 

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name "myoptiongroup" \
    --options OptionName=OEM_AGENT,OptionVersion={{13.1.0.0.v1}},Port={{3872}},VpcSecurityGroupMemberships={{sg-1234567890}},OptionSettings=[{Name=OMS_HOST,Value={{my.example.oms}}},{Name=OMS_PORT,Value={{4903}}},{Name=AGENT_REGISTRATION_PASSWORD,Value={{password}}}] \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name "myoptiongroup" ^
    --options OptionName=OEM_AGENT,OptionVersion={{13.1.0.0.v1}},Port={{3872}},VpcSecurityGroupMemberships={{sg-1234567890}},OptionSettings=[{Name=OMS_HOST,Value={{my.example.oms}}},{Name=OMS_PORT,Value={{4903}}},{Name=AGENT_REGISTRATION_PASSWORD,Value={{password}}}] ^
    --apply-immediately
```

### Step 2: Unlocking the DBSNMP user account
<a name="Oracle.Options.OEMAgent.DBSNMP"></a>

The Management Agent uses the `DBSNMP` user account to connect to the database and report issues to Oracle Enterprise Manager. In a CDB, `DBSNMP` is a common user. This user account is necessary for both the Management Agent and OEM Database Express. By default, this account is locked. The procedure for unlocking this account differs depending on whether your database uses the non-CDB or CDB architecture.

**To unlock the DBSNMP user account**

1. In SQL\*Plus or another Oracle SQL application, log in to your DB instance as your master user.

1. Do either of the following actions, depending on the database architecture:  
**Your database is a non-CDB.**  
Run the following SQL statement:  

   ```
   1. ALTER USER dbsnmp IDENTIFIED BY {{new_password}} ACCOUNT UNLOCK;
   ```  
**Your database is a CDB.**  
Run the following stored procedure to unlock the `DBSNMP` account:  

   ```
   1. EXEC rdsadmin.rdsadmin_util.reset_oem_agent_password('{{new_password}}');
   ```
If you receive an error stating that the procedure doesn't exist, reboot your CDB instance to install it automatically. For more information, see [Rebooting a DB instance](USER_RebootInstance.md).

### Step 3: Adding your targets to the Management Agent console
<a name="Oracle.Options.OEMAgent.Using"></a>

To add a DB instance as a target, make sure you know the endpoint and port. For information about finding the endpoint for your Amazon RDS DB instance, see [Finding the endpoint of your RDS for Oracle DB instance](USER_Endpoint.md). If your database uses the CDB architecture, then add the `CDB$ROOT` container separately as a target.

**To add targets to the Management Agent console**

1. In your OMS console, choose **Setup**, **Add Target**, **Add Targets Manually**. 

1. Choose **Add Targets Declaratively by Specifying Target Monitoring Properties**.

1. For **Target Type**, choose **Database Instance**.

1. For **Monitoring Agent**, choose the agent with the identifier that is the same as your RDS DB instance identifier. 

1. Choose **Add Manually**.

1. Enter the endpoint for your Amazon RDS DB instance, or choose it from the host name list. Make sure that the specified host name matches the endpoint of the Amazon RDS DB instance.

1. Specify the following database properties:
   + For **Target name**, enter a name. 
   + For **Database system name**, enter a name.
   + For **Monitor username**, enter **dbsnmp**. 
   + For **Monitor password**, enter the password from [Step 2: Unlocking the DBSNMP user account](#Oracle.Options.OEMAgent.DBSNMP). 
   + For **Role**, enter **normal**. 
   + For **Oracle home path**, enter **/oracle**. 
   + For **Listener Machine name**, the agent identifier already appears. 
   + For **Port**, enter the database port. The RDS default port is 1521. 
   + For **Database name**, enter the name of your database. If your database is a CDB, this name is `RDSCDB`. 

1. Choose **Test Connection**. 

1. Choose **Next**. The target database appears in your list of monitored resources. 

## Removing the Management Agent option
<a name="Oracle.Options.OEMAgent.Remove"></a>

You can remove the OEM Agent from a DB instance. After you remove the OEM Agent, you don't need to restart your DB instance. 

To remove the OEM Agent from a DB instance, do one of the following: 
+ Remove the OEM Agent option from the option group it belongs to. This change affects all DB instances that use the option group. For more information, see [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption). 
+ Modify the DB instance and specify a different option group that doesn't include the OEM Agent option. This change affects a single DB instance. You can specify the default (empty) option group, or a different custom option group. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md). 

## Performing database tasks with the Management Agent
<a name="Oracle.Options.OEMAgent.DBTasks"></a>

You can use Amazon RDS procedures to run certain EMCTL commands on the Management Agent. By running these procedures, you can do the tasks listed following.

**Note**  
Tasks are executed asynchronously.

**Topics**
+ [Securing the Management Agent](#Oracle.Options.OEMAgent.DBTasks.SecureAgent)
+ [Getting the status of the Management Agent](#Oracle.Options.OEMAgent.DBTasks.GetAgentStatus)
+ [Restarting the Management Agent](#Oracle.Options.OEMAgent.DBTasks.RestartAgent)
+ [Listing the targets monitored by the Management Agent](#Oracle.Options.OEMAgent.DBTasks.ListTargets)
+ [Listing the collection threads monitored by the Management Agent](#Oracle.Options.OEMAgent.DBTasks.ListCollectionThreads)
+ [Clearing the Management Agent state](#Oracle.Options.OEMAgent.DBTasks.ClearState)
+ [Making the Management Agent upload its OMS](#Oracle.Options.OEMAgent.DBTasks.ForceUploadOMS)
+ [Pinging the OMS](#Oracle.Options.OEMAgent.DBTasks.PingOMS)
+ [Viewing the status of an ongoing task](#Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus)

### Securing the Management Agent
<a name="Oracle.Options.OEMAgent.DBTasks.SecureAgent"></a>

To secure the Management Agent, run the Amazon RDS procedure `rdsadmin.rdsadmin_oem_agent_tasks.secure_oem_agent`. This procedure is equivalent to running the `emctl secure agent` command.

The following procedure creates a task to secure the Management Agent and returns the ID of the task:

```
SELECT rdsadmin.rdsadmin_oem_agent_tasks.secure_oem_agent as TASK_ID from DUAL;
```

To display the output file for the task and view the result, see [Viewing the status of an ongoing task](#Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus).

### Getting the status of the Management Agent
<a name="Oracle.Options.OEMAgent.DBTasks.GetAgentStatus"></a>

To get the status of the Management Agent, run the Amazon RDS procedure `rdsadmin.rdsadmin_oem_agent_tasks.get_status_oem_agent`. This procedure is equivalent to the `emctl status agent` command.

The following procedure creates a task to get the Management Agent's status and returns the ID of the task.

```
SELECT rdsadmin.rdsadmin_oem_agent_tasks.get_status_oem_agent() as TASK_ID from DUAL;
```

To display the output file for the task and view the result, see [Viewing the status of an ongoing task](#Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus).

### Restarting the Management Agent
<a name="Oracle.Options.OEMAgent.DBTasks.RestartAgent"></a>

To restart the Management Agent, run the Amazon RDS procedure `rdsadmin.rdsadmin_oem_agent_tasks.restart_oem_agent`. This procedure is equivalent to running the `emctl stop agent` and `emctl start agent` commands.

The following procedure creates a task to restart the Management Agent and returns the ID of the task.

```
SELECT rdsadmin.rdsadmin_oem_agent_tasks.restart_oem_agent as TASK_ID from DUAL;    
```

To display the output file for the task and view the result, see [Viewing the status of an ongoing task](#Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus).

### Listing the targets monitored by the Management Agent
<a name="Oracle.Options.OEMAgent.DBTasks.ListTargets"></a>

To list the targets monitored by the Management Agent, run the Amazon RDS procedure `rdsadmin.rdsadmin_oem_agent_tasks.list_targets_oem_agent`. This procedure is equivalent to running the `emctl config agent listtargets` command.

The following procedure creates a task to list the targets monitored by the Management Agent and returns the ID of the task.

```
SELECT rdsadmin.rdsadmin_oem_agent_tasks.list_targets_oem_agent as TASK_ID from DUAL;
```

To display the output file for the task and view the result, see [Viewing the status of an ongoing task](#Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus).

### Listing the collection threads monitored by the Management Agent
<a name="Oracle.Options.OEMAgent.DBTasks.ListCollectionThreads"></a>

To list of all the running, ready, and scheduled collection threads monitored by the Management Agent, run the Amazon RDS procedure `rdsadmin.rdsadmin_oem_agent_tasks.list_clxn_threads_oem_agent`. This procedure is equivalent to the `emctl status agent scheduler` command.

The following procedure creates a task to list the collection threads and returns the ID of the task.

```
SELECT rdsadmin.rdsadmin_oem_agent_tasks.list_clxn_threads_oem_agent() as TASK_ID from DUAL;          
```

To display the output file for the task and view the result, see [Viewing the status of an ongoing task](#Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus).

### Clearing the Management Agent state
<a name="Oracle.Options.OEMAgent.DBTasks.ClearState"></a>

To clear the Management Agent's state, run the Amazon RDS procedure `rdsadmin.rdsadmin_oem_agent_tasks.clearstate_oem_agent`. This procedure is equivalent to running the `emctl clearstate agent` command.

The following procedure creates a task that clears the Management Agent's state and returns the ID of the task.

```
SELECT rdsadmin.rdsadmin_oem_agent_tasks.clearstate_oem_agent() as TASK_ID from DUAL;
```

To display the output file for the task and view the result, see [Viewing the status of an ongoing task](#Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus).

### Making the Management Agent upload its OMS
<a name="Oracle.Options.OEMAgent.DBTasks.ForceUploadOMS"></a>

To make the Management Agent upload the Oracle Management Server (OMS) associated with it, run the Amazon RDS procedure `rdsadmin.rdsadmin_oem_agent_tasks.upload_oem_agent`. This procedure is equivalent to running the `emctl upload agent` command.

The following procedure creates a task that makes the Management Agent upload its associated OMS and return the ID of the task.

```
SELECT rdsadmin.rdsadmin_oem_agent_tasks.upload_oem_agent() as TASK_ID from DUAL;
```

To display the output file for the task and view the result, see [Viewing the status of an ongoing task](#Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus).

### Pinging the OMS
<a name="Oracle.Options.OEMAgent.DBTasks.PingOMS"></a>

To ping the Management Agent's OMS, run the Amazon RDS procedure `rdsadmin.rdsadmin_oem_agent_tasks.ping_oms_oem_agent`. This procedure is equivalent to running the `emctl pingOMS` command.

The following procedure creates a task that pings the Management Agent's OMS and returns the ID of the task.

```
SELECT rdsadmin.rdsadmin_oem_agent_tasks.ping_oms_oem_agent() as TASK_ID from DUAL;
```

To display the output file for the task and view the result, see [Viewing the status of an ongoing task](#Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus).

### Viewing the status of an ongoing task
<a name="Oracle.Options.OEMAgent.DBTasks.ViewTaskStatus"></a>

You can view the status of an ongoing task in a bdump file. The bdump files are located in the `/rdsdbdata/log/trace` directory. Each bdump file name is in the following format.

```
dbtask-{{task-id}}.log 
```

When you want to monitor a task, replace `{{task-id}}` with the ID of the task that you want to monitor.

To view the contents of bdump files, run the Amazon RDS procedure `rdsadmin.rds_file_util.read_text_file`. The following query returns the contents of the `dbtask-1546988886389-2444.log` bdump file. 

```
SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','dbtask-1546988886389-2444.log'));
```

For more information about the Amazon RDS procedure `rdsadmin.rds_file_util.read_text_file`, see [Reading files in a DB instance directory](Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.ReadingFiles).