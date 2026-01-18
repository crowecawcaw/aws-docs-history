# Troubleshooting AWS Systems Manager for SAP

###### Topics

- [Database registration failure](#troubleshoot1 "#troubleshoot1")
- [InvalidInstanceIdException](#troubleshoot2 "#troubleshoot2")
- [AccessDeniedException](#troubleshoot3 "#troubleshoot3")
- [ResourceNotFoundException](#troubleshoot4 "#troubleshoot4")
- [Invalid control character](#troubleshoot5 "#troubleshoot5")
- [Expecting ',' delimiter](#troubleshoot6 "#troubleshoot6")
- [Maximum limit of resources](#troubleshoot7 "#troubleshoot7")
- [Unauthorized user](#troubleshoot8 "#troubleshoot8")
- [REFRESH_FAILED; Database connection mismatch](#troubleshoot9 "#troubleshoot9")
- [Unsupported setup](#troubleshoot10 "#troubleshoot10")
- [Input parameter errors](#troubleshoot11 "#troubleshoot11")
- [Application status: FAILED](#troubleshoot12 "#troubleshoot12")
- [StartApplication AccessDeniedException](#troubleshoot13 "#troubleshoot13")
- [StartApplication ConflictException](#troubleshoot14 "#troubleshoot14")
- [StartApplication ValidationException](#troubleshoot15 "#troubleshoot15")
- [StopApplication AccessDeniedException](#troubleshoot16 "#troubleshoot16")
- [StopApplication ConflictException](#troubleshoot17 "#troubleshoot17")
- [StopApplication ValidationException](#troubleshoot18 "#troubleshoot18")
- [Unsupported sslenforce setup](#troubleshoot-19 "#troubleshoot-19")
- [StartConfigurationChecks AccessDeniedException](#troubleshoot-20 "#troubleshoot-20")
- [Component Status ValidationException](#troubleshoot-21 "#troubleshoot-21")
- [Single Node Compatibility ValidationException](#troubleshoot-22 "#troubleshoot-22")
- [Check Type Compatibility ValidationException](#troubleshoot-23 "#troubleshoot-23")
- [Concurrent Checks ValidationException](#troubleshoot-24 "#troubleshoot-24")
- [ListConfigurationCheckOperations ResourceNotFoundException](#troubleshoot-25 "#troubleshoot-25")
- [ListSubcheckResults Operation ValidationException](#troubleshoot-26 "#troubleshoot-26")
- [ListSubcheckRuleResults SubCheck Result ValidationException](#troubleshoot-27 "#troubleshoot-27")
- [ListSubcheckRuleResults - Unknown Rules](#troubleshoot-28 "#troubleshoot-28")

## Database registration failure

**Problem** – `Registration of SAP HANA database on AWS Systems Manager for SAP fails with an error`

**Resolution** – Use the following steps to resolve this error.

1. Deregister the database with the following command.

```
 aws ssm-sap deregister-application \
--application-id <YOUR_APPLICATION_ID> \
--region us-east-1
```

`<YOUR_APPLICATION_ID>` must be the same as the one used during registration. 2. Re-register the database.

```
 aws ssm-sap register-application \
--application-id <YOUR_APPLICATION_ID> \
--region us-east-1
```

**Problem** – `Application DiscoveryStatus: REGISTRATION_FAILED; StatusMessage: The database ARN specified in registration input does not match discovered database connection.`

**Resolution** – The specified `--database-arn` does not match the database connection discovered on the SAP_ABAP instance. De-register the failed SAP ABAP application registration, and re-register with the correct `--database-arn`. For more information, see [Register your SAP ABAP application with Systems Manager for SAP.](register-abap.md#step2-abap "register-abap.md#step2-abap")

## InvalidInstanceIdException

**Problem** – `Error executing SSM document - InvalidInstanceIdException Instances [[<EC2_INSTANCE_ID>]] not in a valid state for account <ACCOUNT_ID> (Service: Ssm, Status Code: 400, Request ID: <REQUEST_ID>)`

**Resolution** – Ensure that your Amazon EC2 instance is active, and that the SSM Agent has been installed. For more information, see [Verify AWS Systems Manager (SSM Agent) is running](get-started.md#verify-ssm-agent "get-started.md#verify-ssm-agent"). After verification, deregister, and then re-register your application.

## AccessDeniedException

**Problem** – `Discovered 1 SAP instances. {HDB: Unable to decrypt credentials <SECRET_NAME>: An error occurred (AccessDeniedException) when calling the GetSecretValue operation: User: arn:aws:sts::<ACCOUNT_ID>:assumed-role/<EC2_IAM_ROLE>/<INSTANCE_ID> is not authorized to perform: secretsmanager:GetSecretValue on resource: <SECRET_NAME> because no identity-based policy allows the secretsmanager:GetSecretValue action},{HDB: Failed to discover HANA database ports. Exception type: <class 'IndexError'>}, REGISTER_APPLICATION`

**Resolution** – Ensure that your Amazon EC2 instance is setup correctly. For more information, see [Set up required permissions for Amazon EC2 instance running SAP HANA database](get-started.md#ec2-permissions "get-started.md#ec2-permissions"). The IAM role attached to your Amazon EC2 instance must have the permission to perform `secretsmanager:GetSecretValue` action. After verification, deregister, and then re-register your application.

## ResourceNotFoundException

**Problem** – `ERROR Discovered 1 SAP instances. {HDB: Unable to decrypt credentials <SECRET_NAME>: An error occurred (ResourceNotFoundException) when calling the GetSecretValue operation: Secrets Manager can’t find the specified secret.},{HDB: Failed to discover HANA database ports. Exception type: <class 'IndexError'>}, REGISTER_APPLICATION`

**Resolution** – Verify and ensure that you are using the correct `SECRET_NAME`. For more information, see [Register SAP HANA database credentials in AWS Secrets Manager](get-started.md#register-secrets "get-started.md#register-secrets"). After verification, deregister, and then re-register your application.

**Problem** – `An error occurred (ResourceNotFoundException) when calling the RegisterApplication operation: Resource cannot be found`

**Resolution** – The `--database-arn` provided in the registration input parameter does not exist. Ensure that the connected SAP HANA database has been registered as an application with Systems Manager for SAP. The database must be registered before registering the SAP ABAP application. For more information, see [Register database](register-abap.md#step1-abap "register-abap.md#step1-abap").

## Invalid control character

**Problem** – `Invalid control character at: line 2 column 32 (char 34)`

**Resolution** – Ensure that the `JSON` file that contains your SAP HANA database credentials is formatted correctly as a `JSON` file. Some characters may be pasted incorrectly after copying them from this file. Edit the file to remove line spaces, double quotes, spaces, and tabs. Add the formatted file content to your machine, terminal, and in your file editor. Save the changes to the file and retry registering your database.

## Expecting ',' delimiter

**Problem** – `Expecting ',' delimiter: line 1 column 36 (char 35)`

**Resolution**- – Ensure that the `JSON` file that contains your SAP HANA database credentials is formatted correctly as a `JSON` file. Some characters may be pasted incorrectly after copying them from this file. Edit the file to remove line spaces, double quotes, spaces, and tabs. Add the formatted file content to your machine, terminal, and in your file editor. Save the changes to the file and retry registering your database.

## Maximum limit of resources

**Problem** – `The number of registered resources under your account <ACCOUNTID> has reached max limit`

**Resolution** – With AWS Systems Manager for SAP, you can register up to 10 applications per AWS account. You can add up to 20 SAP HANA databases on each application. For more information, see [Quotas for Systems Manager for SAP](load-balancer-limits.md "load-balancer-limits.md").

## Unauthorized user

**Problem** – `Error executing SSM document - SsmException User: arn:aws:sts::<ACCOUNT_ID>:assumed-role/AWSServiceRoleForAWSSSMForSAP/ssm-sap is not authorized to perform: ssm:SendCommand on resource: arn:aws:ec2:us-east-1:<ACCOUNT_ID>:instance/<INSTANCE_ID> because no identity-based policy allows the ssm:SendCommand action (Service: Ssm, Status Code: 400, Request ID: 25ec41f5-1fa8-4a1a-80ac-6b7e85088d74)`

**Resolution** – Ensure that your Amazon EC2 instance has the `SSMForSAPManaged` tag with the value `True`. For more information, see [Set up required permissions for Amazon EC2 instance running SAP HANA database](get-started.md#ec2-permissions "get-started.md#ec2-permissions").

## REFRESH_FAILED; Database connection mismatch

**Problem** – `Application DiscoveryStatus: REFRESH_FAILED; StatusMessage: The database ARN specified in registration input does not match discovered database connection.`

**Resolution** – The specified `--database-arn` does not match the database connection discovered on the SAP_ABAP instance. Use the [UpdateApplicationSettings](../../../ssmsap/latest/APIReference/API_UpdateApplicationSettings.md "../../../ssmsap/latest/APIReference/API_UpdateApplicationSettings.md") API to provide the correct `--database-arn` of your SAP HANA database along with the `--application-id` of the SAP ABAP application.

```
 aws ssm-sap update-application-settings --application-id <ApplicationId> --database-arn <DatabaseArn>
```

## Unsupported setup

**Problem** – `SSM-SAP only supports single-node SAP_ABAP deployment.`

**Resolution** – Systems Manager for SAP currently only supports single-node SAP ABAP deployment registration. Your SAP ABAP application must be connected to a single-node SAP HANA instance that resides in the same Amazon EC2 instance. All components belonging to the SAP ABAP application (ASCS, dialog instances, etc.) must also reside on the same Amazon EC2 instance.

## Input parameter errors

**Problem** – `An error occurred (ValidationException) when calling the RegisterApplication operation: Credentials and/or instance number is not expected for SAP applications with type SAP_ABAP.`

**Resolution** – `--credentials` and `--sap-instance-number` are inapplicable parameters for registering Systems Manager application of type SAP_ABAP. Remove both the parameters from the [RegisterApplication](../../../ssmsap/latest/APIReference/API_RegisterApplication.md "../../../ssmsap/latest/APIReference/API_RegisterApplication.md") call.

**Problem** – `An error occurred (ValidationException) when calling the RegisterApplication operation: The SID and database ARN of ASCS or Application Server must be specified for SAP applications with type SAP_ABAP.`

**Resolution** – The SID and ARN of ASCS of the connected SAP HANA database are required input parameters for registering SAP ABAP application. Ensure that the connected SAP HANA database has been registered as a Systems Manager application before registering SAP ABAP with Systems Manager for SAP. For more information, see [Register your SAP ABAP application with Systems Manager for SAP](register-abap.md "register-abap.md").

## Application status: FAILED

**Problem** – `System configuration change detected. To continue using this application as a standalone, for operations like backup/restore through AWS Backup, deregister this application and register again`.

**Resolution** – Systems Manager for SAP does not support moving a highly available (2 nodes) application to a single node system. You must re-register your primary application with the same application ID to ensure that the primary database is associated with the application, and that backup continuity is maintained. Use the following steps.

1. De-register the database with the following command.

```
 aws ssm-sap deregister-application \
--application-id <YOUR_APPLICATION_ID> \
--region <REGION>
```

###### Note

Use the same _APPLICATION_ID_ as the one used during registration. 2. Use the following command to re-register the database with the same _APPLICATION_ID_.

```
 aws ssm-sap register-application \
--application-id <YOUR_APPLICATION_ID> \
--region <REGION>
```

## StartApplication AccessDeniedException

_Problem_ – `An error occurred (AccessDeniedException) when calling the StartApplication operation: User: arn:aws:sts::<account_id> :assumed-role/<role_name> is not authorized to perform: ssm-sap:StartApplication on resource: arn:aws:ssm-sap:<region>: <account_id>:HANA/<hana_application_id>`

_Possible cause_ – When the `StartApplication` operation is performed on an SAP ABAP application and the procedure includes starting its connected HANA application, you must have the necessary IAM permissions to run `ssm-sap:StartApplication` on the connected application. Without those permissions, the error message will occur.

_Resolution_ – Add the permission `ssm-sap:StartApplication` against the HANA application to the role of the user calling `StartApplication`.

## StartApplication ConflictException

_Problem_ – `Start Application can not be run on an already running application. Run ssm-sap start-application-refresh --application-id <ApplicationId> to ensure that the ssm-sap status reflects the current application state.`

_Possible cause_ – The application you attempted to start is already running.

_Resolution_ – [Refresh SAP application](refresh-sap-application.md "refresh-sap-application.md") to ensure the `ssm-sap` status reflects the current application state.

## StartApplication ValidationException

_Problem_ – `An error occurred (ValidationException) when calling the StartApplication operation: Caller lacks permissions to start Amazon EC2 instances`

_Possible cause_ – When the `StartApplication` operation includes starting the Amazon EC2 instances running the SAP application, you must have the necessary IAM permissions to run `ec2:StartInstances` on the corresponding Amazon EC2 instances. Without those permissions, the error message will occur.

_Resolution_ – Add the permission `ec2:StartInstances` permission against the Amazon EC2 hosts of the SAP application to the role of the user calling `StartApplication`.

## StopApplication AccessDeniedException

_Problem_ – `An error occurred (AccessDeniedException) when calling the StopApplication operation: User: arn:aws:sts::<account_id>:assumed-role/<role_name> is not authorized to perform: ssm-sap:StopApplication on resource:arn:aws:ssm-sap:<region>:<account_id>:HANA/<hana_application_id>`

_Possible cause_ – When the `StopApplication` operation is performed on an SAP ABAP application and the procedure includes starting its connected HANA application, you must have the necessary IAM permissions to run `ssm-sap:StopApplication` on the connected application. Without those permissions, the error message will occur.

_Resolution_ – Add the permission `ssm-sap:StopApplication` against the HANA application to the role of the user calling `StopApplication`.

## StopApplication ConflictException

_Problem_ – `An error occurred (ConflictException) when calling the StopApplication operation: The specified component is already stopped.` or `An error occurred (ConflictException) when calling the StopApplication operation: The specified component is not in a state that can be started or stopped.`

_Possible cause_ – If your application status or status of the components are stale, the StopApplication operation can result in these or similar `ConflictExceptions`.

_Resolution_ –

1. [Refresh SAP application](refresh-sap-application.md "refresh-sap-application.md").
2. Then, retry [Stop SAP application](stop-sap-application.md "stop-sap-application.md").

_Possible cause_ – If the `SSMForSAPManaged:True` tag has not been applied to the EC2 instance.

_Resolution_ – Apply the `SSMForSAPManaged:True` tag to the EC2 instance.

## StopApplication ValidationException

_Problem_ – `An error occurred (ValidationException) when calling the StopApplication operation: Caller lacks permissions to stop Amazon EC2 instances`

_Possible cause_ – When the `StopApplication` operation includes stopping the Amazon EC2 instances running the SAP application, you must have the necessary IAM permissions to run `ec2:StopInstances` on the corresponding EC2 instances. Without those permissions, the error message will occur.

_Resolution_ – Add the permission `ec2:StopInstances` permission against the Amazon EC2 hosts of the SAP application to the role of the user calling `StopApplication`.

## Unsupported `sslenforce` setup

_Problem_ – `HANA error code: 4321. HANA error message: connection failed: only secure connections are allowed`

_Resolution_ – Set `sslenforce` to flase in the `global.ini` file.

## StartConfigurationChecks AccessDeniedException

_Problem_ – `An error occurred (AccessDeniedException) when calling the StartConfigurationChecks operation: User: arn:aws:sts::<account_id>:assumed-role/<role_name> is not authorized to perform: ssm-sap:StartConfigurationChecks on resource: arn:aws:ssm-sap:<region>:<account_id>:HANA/<hana_application_id>`

_Possible cause_ – When the StartConfigurationChecks operation is performed, you must have the necessary IAM permissions to execute configuration checks on the application.

_Resolution_ – Add the permission `ssm-sap:StartConfigurationChecks` against the application to the role of the user calling `StartConfigurationChecks`.

## Component Status ValidationException

_Problem_ – `An error occurred (ValidationException): "<applicationId> has <componentIds> component(s) not RUNNING. Start all components to run Configuration Checks."`

_Possible cause_ – All components must be in RUNNING state before starting configuration checks. The checks cannot proceed if any component is stopped, failed, or still starting up.

_Resolution_ – Start all non-running components and wait for them to reach RUNNING state before retrying configuration checks.

## Single Node Compatibility ValidationException

_Problem_ – `An error occurred (ValidationException): "Application <applicationId> has 1 running HANA_NODE Component. The Configuration Check 'SAP_CHECK_03' is not applicable for Single Node HANA applications."`

_Possible cause_ – SAP_CHECK_03 is being executed on a single-node HANA deployment, but this check is only applicable for HA deployments.

_Resolution_ – Remove SAP_CHECK_03 from configuration checks for single-node deployments. Use only SAP_CHECK_01 and SAP_CHECK_02.

## Check Type Compatibility ValidationException

_Problem_ – `An error occurred (ValidationException): "The Configuration Check(s) '<checkIds>' are not applicable for the <applicationType> application <applicationId>"`

_Possible cause_ – The requested configuration checks are not compatible with the application type.

_Resolution_ – Use only supported configuration checks:

- For a list of supported configuration checks, use the ListConfigurationCheckDefinitions API
- You can use this API to get details about which checks are available for your specific deployment type

## Concurrent Checks ValidationException

_Problem_ – `An error occurred (ValidationException): "Unable to start new configuration checks for <applicationId>. The following checks are currently in progress: <checkIds>"`

_Possible cause_ – Configuration checks of the same type are already running for this application.

_Resolution_ – Wait for currently running checks to complete before starting new ones.

## ListConfigurationCheckOperations ResourceNotFoundException

_Problem_ – `An error occurred (ResourceNotFoundException): "Application <applicationId> doesn’t exist."`

_Possible cause_ – The specified application ID cannot be found in the application store for the given account ID.

_Resolution_ – Verify the application ID is correct and properly registered in your AWS account.

## ListSubcheckResults Operation ValidationException

_Problem_ – `An error occurred (ValidationException): "Operation Not Found: <operationId>"`

_Possible cause_ – The specified operation ID is invalid or no longer exists in the system.

_Resolution_ – Verify the operation ID is correct and still active.

## ListSubcheckRuleResults SubCheck Result ValidationException

_Problem_ – `An error occurred (ValidationException): "SubCheckResult Not Found: <subCheckResultId>"`

_Possible cause_ – The specified subcheck result ID cannot be found in the system.

_Resolution_ – Verify the subcheck result ID is correct and associated with the specified operation.

## ListSubcheckRuleResults - Unknown Rules

_Problem_ – Unknown rules are encountered during configuration checks.

_Possible cause_ – This occurs when there is a mismatch between your environment’s configuration and the supported rule definitions in Systems Manager for SAP.

_Resolution_ – Contact AWS Support with the operation ID, timestamp, AWS Region, and rule name. AWS Support will investigate the configuration mismatch and provide guidance for your environment.
