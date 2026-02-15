# Register your SAP HANA databases with Systems Manager for SAP

You can register a single node or a high availability setup with multiple nodes for SAP HANA database with Systems Manager for SAP. Ensure that you have completed the setup perquisites described in [Get started with Systems Manager for SAP](get-started.md "get-started.md"). Follow along these steps to register your database.

###### Topics

- [Step 1: Create a JSON for credentials](#step1 "#step1")
- [Step 2: Register database](#step2 "#step2")
- [Step 3: Check registration status](#step3 "#step3")
- [Step 4: Verify registration](#step4 "#step4")
- [Step 5: View component summary](#step5 "#step5")
- [Backup your database – optional](#optional-step "#optional-step")

## Step 1: Create a JSON for credentials

Create a JSON file to store the credentials you created in [Register SAP HANA database credentials in AWS Secrets Manager](get-started.md#register-secrets "get-started.md#register-secrets").

```
[
    {
        "DatabaseName": "<YOUR_SID>/<YOUR_DATABASE_NAME>",
        "CredentialType": "ADMIN",
        "SecretId": "<YOUR_SECRET_NAME>"
    },
    {
        "DatabaseName": "<YOUR_SID>/<ANOTHER_ONE_OF_YOUR_DATABASE_NAME>",
        "CredentialType": "ADMIN",
        "SecretId": "<YOUR_SECRET_NAME>"
    }
]
```

- Enter a unique name for the JSON file. For example, `SsmForSapRegistrationCredentials.json`.
- For `DatabaseName`, ensure that you enter both, the system ID and the database name.
- For `SecretId`, use the Secret name created in Step 4 of [Register SAP HANA database credentials in AWS Secrets Manager](get-started.md#register-secrets "get-started.md#register-secrets").

The following is an example JSON file.

```
[
    {
        "DatabaseName": "HDB/SYSTEMDB",
        "CredentialType": "ADMIN",
        "SecretId": "HANABackup"
    },
    {
        "DatabaseName": "HDB/HDB",
        "CredentialType": "ADMIN",
        "SecretId": "HANABackup"
    }
]
```

## Step 2: Register database

Register your SAP HANA databases using the following command.

Make sure to use the correct SAP HANA database instance number and SAP HANA database name (SID). These are different than the SAP instance number and SAP System Identifier.

**Command Template**

```
aws ssm-sap register-application --application-id <APPLICATION_ID> --application-type HANA --instances <YOUR_EC2_INSTANCE_ID> --sap-instance-number <YOUR_HANA_DATABASE_SYSTEM_NUMBER> --sid <YOUR_HANA_DATABASE_SID> --region <REGION> --credentials file://<PATH_TO_YOUR_CREDENTIALS_JSON_FILE>
```

**Example command with sample values**

```
aws ssm-sap register-application \
--application-id myHanaApplication \
--application-type HANA \
--instances i-0123456789abcdefg \
--sap-instance-number 00 \
--sid HDB \
--region us-east-1 \
--credentials file://SsmForSapRegistrationCredentials.json
```

**Example JSON response**

```
{
    "Application": {
        "Id": "myHanaApplication",
        "Type": "HANA",
        "Arn": "<APPLICATION_ARN>",
        "Status": "REGISTERING",
        "Components": [],
        "LastUpdated": "2022-08-19T10:58:48.521000-07:00"
    },
    "OperationId": "6bd44104-d63c-449d-8007-6c1b471e3e5e" //(1)
}
```

1. Take note of this operation ID. You’ll need it in the next step.

In the preceding example, the instance number is 00 and SID is HDB. This can be verified with `/usr/sap/<SID>/HDB<instance number>`. For example, the path will be `/usr/sap/HDB/HDB00`.

###### Note

To register a high availability SAP HANA database, you can input either the primary or the secondary instance ID with the `--instances` parameter. For example, for a high availability SAP HANA database residing on primary node `i-0123456789abcdefg` and secondary node `i-9876543210abcdefg`, you can specify database registration in any one of the following ways.

- `--instances i-0123456789abcdefg`
- `--instances i-9876543210abcdefg`

## Step 3: Check registration status

The registration may take a few minutes to complete. Use the following command to check the status of the registration. Replace `<YOUR_OPERATION_ID>` with the `OperationID` from the previous step.

```
aws ssm-sap get-operation --operation-id <YOUR_OPERATION_ID> --region <REGION>
```

## Step 4: Verify registration

Verify the registration with [GetApplication](../../../ssmsap/latest/APIReference/API_GetApplication.md "../../../ssmsap/latest/APIReference/API_GetApplication.md") API. You can also view the details of registered databases with [ListDatabases](../../../ssmsap/latest/APIReference/API_ListDatabases.md "../../../ssmsap/latest/APIReference/API_ListDatabases.md") and [GetDatabase](../../../ssmsap/latest/APIReference/API_GetDatabase.md "../../../ssmsap/latest/APIReference/API_GetDatabase.md") API.

**Command template**

```
aws ssm-sap get-application --application-id <APPLICATON_ID> --region <REGION>
```

**Example to get the summary of an application**

```
aws ssm-sap get-application \
--application-id myHanaApplication \
--region us-east-1
```

**Example output**

```
{
    "Application": {
        "Id": "myHanaApplication",
        "Type": "HANA",
        "Arn": "arn:aws:ssm-sap:us-east-1:123456789123:HANA/myHanaApplication",
        "Status": "ACTIVATED",
        "DiscoveryStatus": "SUCCESS",
        "Components": [
            "HDB-HDB00" //(1)
        ],
        "LastUpdated": "2023-07-06T13:25:35.702000-07:00"
    },
    "Tags": {}
}
```

1. Take note of this component ID. You’ll need it in the next step.

## Step 5: View component summary

Get the component summary with [GetComponent](../../../ssmsap/latest/APIReference/API_GetComponent.md "../../../ssmsap/latest/APIReference/API_GetComponent.md") API.

```
aws ssm-sap get-component --application-id <APPLICATION_ID> --component-id <YOUR_COMPONENT_ID_FROM_LAST_STEP> --region <REGION>
```

Systems Manager for SAP provides two types of components for an SAP HANA application – parent and child.

- `HANA` – there is only one parent component representing the logical database.
- `HANA_NODE` – there are multiple child components representing database host entities.

See the following table for examples of single node and high availability SAP HANA database setup with Systems Manager for SAP.

###### Example

Single node

**GetComponent API output for parent component**

```
{
    "Component": {
        "ComponentId": "HDB-HDB00",
        "ChildComponents": [
            "HDB-HDB00-sapci"
        ],
        "ApplicationId": "myHanaApplication",
        "ComponentType": "HANA",
        "Status": "RUNNING",
        "Databases": [
            "SYSTEMDB",
            "HDB"
        ],
        "Hosts": [
            {
                "HostName": "sapci",
                "HostIp": "172.31.31.70",
                "EC2InstanceId": "i-0123456789abcdefg",
                "InstanceId": "i-0123456789abcdefg",
                "HostRole": "LEADER",
                "OsVersion": "SUSE Linux Enterprise Server 15 SP4"
            }
        ],
        "PrimaryHost": "i-0123456789abcdefg",
        "LastUpdated": "2023-07-19T11:06:36.114000-07:00",
        "Arn": "arn:aws:ssm-sap:us-east-1:123456789123:HANA/myHanaApplication/COMPONENT/HDB-HDB00"
    },
    "Tags": {}
}
```

**GetComponent API output for child component**

```
{
    "Component": {
        "ComponentId": "HDB-HDB00-sapci",
        "ParentComponent": "HDB-HDB00",
        "ApplicationId": "myHanaApplication",
        "ComponentType": "HANA_NODE",
        "Status": "RUNNING",
        "SapHostname": "sapci.local",
        "SapKernelVersion": "753, patch 1010, changelist 2124070",
        "HdbVersion": "",
        "Resilience": {
            "HsrTier": "",
            "HsrReplicationMode": "NONE",
            "HsrOperationMode": "NONE"
        },
        "AssociatedHost": {
            "Hostname": "sapci",
            "Ec2InstanceId": "i-04823df91c0934025",
            "OsVersion": "SUSE Linux Enterprise Server 15 SP4"
        },
        "LastUpdated": "2023-07-19T11:06:36.101000-07:00",
        "Arn": "arn:aws:ssm-sap:us-east-1:123456789101:HANA/myHanaApplication/COMPONENT/HDB-HDB00-sapci"
    },
    "Tags": {}
}
```

High availability

**GetComponent API output for parent component**

```
{
    "Component": {
        "ComponentId": "HDB-HDB00",
        "ChildComponents": [
            "HDB-HDB00-sapsecdb",
            "HDB-HDB00-sappridb"
        ],
        "ApplicationId": "myHanaApplication",
        "ComponentType": "HANA",
        "Status": "RUNNING",
        "Databases": [
            "SYSTEMDB",
            "HDB"
        ],
        "LastUpdated": "2023-06-28T22:57:24.053000-07:00",
        "Arn": "arn:aws:ssm-sap:us-east-1:123456789123:HANA/myHanaApplication/COMPONENT/HDB-HDB00"
    },
    "Tags": {}
}
```

**GetComponent API output for child component (primary)**

```
{
    "Component": {
        "ComponentId": "HDB-HDB00-sappridb",
        "ParentComponent": "HDB-HDB00",
        "ApplicationId": "myHanaApplication",
        "ComponentType": "HANA_NODE",
        "Status": "RUNNING",
        "SapHostname": "sappridb.local",
        "SapKernelVersion": "753, patch 1010, changelist 2124070",
        "HdbVersion": "2.00.065.00.1665753120",
        "Resilience": {
            "HsrTier": "1",
            "HsrReplicationMode": "PRIMARY",
            "HsrOperationMode": "PRIMARY",
            "ClusterStatus": "ONLINE"
        },
        "AssociatedHost": {
            "Hostname": "sappridb",
            "Ec2InstanceId": "i-0123456789abcdefg",
            "OsVersion": "SUSE Linux Enterprise Server 15 SP4"
        },
        "LastUpdated": "2023-07-19T10:20:26.888000-07:00",
        "Arn": "arn:aws:ssm-sap:us-east-1:123456789123:HANA/myHanaApplication/COMPONENT/HDB-HDB00-sappridb"
    },
    "Tags": {}
}
```

**GetComponent API output for child component (secondary)**

```
{
    "Component": {
        "ComponentId": "HDB-HDB00-sapsecdb",
        "ParentComponent": "HDB-HDB00",
        "ApplicationId": "myHanaApplication",
        "ComponentType": "HANA_NODE",
        "Status": "RUNNING",
        "SapHostname": "sapsecdb.local",
        "SapKernelVersion": "753, patch 1010, changelist 2124070",
        "HdbVersion": "2.00.065.00.1665753120",
        "Resilience": {
            "HsrTier": "2",
            "HsrReplicationMode": "SYNC",
            "HsrOperationMode": "LOGREPLAY",
            "ClusterStatus": "ONLINE"
        },
        "AssociatedHost": {
            "Hostname": "sapsecdb",
            "Ec2InstanceId": "i-0123456789abcdefg",
            "OsVersion": "SUSE Linux Enterprise Server 15 SP4"
        },
        "LastUpdated": "2023-07-19T10:20:26.639000-07:00",
        "Arn": "arn:aws:ssm-sap:us-east-1:123456789123:HANA/myHanaApplication/COMPONENT/HDB-HDB00-sapsecdb"
    },
    "Tags": {}
}
```

## Backup your database – _optional_

Now the registration is complete, and you can begin data protection operations, including backup and restore of your SAP HANA databases. For more details, see [AWS Backup documentation](../../../aws-backup/latest/devguide/backup-saphana.md#w142aac17c15c33b5 "../../../aws-backup/latest/devguide/backup-saphana.md#w142aac17c15c33b5").
