# Register your SAP ABAP application with AWS Systems Manager for SAP

You can register a single node or multi node (distributed or high availability) setup for SAP ABAP application with Systems Manager for SAP. Ensure that you have completed the setup perquisites described in [Get started with Systems Manager for SAP](get-started.md "get-started.md"). Follow along these steps to register your SAP ABAP application.

###### Topics

- [Step 1: Register database](#step1-abap "#step1-abap")
- [Step 2: Register application](#step2-abap "#step2-abap")
- [Step 3: Check registration status](#step3-abap "#step3-abap")
- [Step 4: Verify registration](#step4-abap "#step4-abap")
- [Step 5: View component summary](#step5-abap "#step5-abap")

## Step 1: Register database

Register your SAP HANA database before registering your SAP ABAP application. For more information, see [Register your SAP HANA databases with Systems Manager for SAP](register-database.md "register-database.md").

Note the `ApplicationId` of your registration.

## Step 2: Register application

1. Use the `ApplicationId` noted in the previous step in the next command.
2. Use the following command to find the Amazon Resource Name (ARN) of the database.

```
aws ssm-sap list-databases --application-id <APPLICATION_ID>
```

```
{
    "Databases": [
        {
            "ApplicationId": "SAP_HANA_APPLICATION",
            "ComponentId": "HDB-HDB00",
            "DatabaseId": "SYSTEMDB",
            "DatabaseType": "SYSTEM",
            "Arn": "arn:aws:ssm-sap:us-east-1:123456789101:HANA/SAP_HANA_APPLICATION/DB/SYSTEMDB",
            "Tags": {}
        },
        {
            "ApplicationId": "SAP_HANA_APPLICATION",
            "ComponentId": "HDB-HDB00",
            "DatabaseId": "HDB",
            "DatabaseType": "TENANT",
            "Arn": "arn:aws:ssm-sap:us-east-1:123456789101:HANA/SAP_HANA_APPLICATION/DB/HDB", //(Note)
            "Tags": {}
        }
    ]
}
```

**Note** the `database-arn` for use in the next step. 3. Register your SAP ABAP application with the following command.

**Command template**

```
aws ssm-sap register-application \
--application-id <APPLICATION_ID> \
--application-type SAP_ABAP \
--instances <YOUR_EC2_INSTANCE_ID> \
--sid <YOUR_HANA_SID> \
--region <REGION>
--database-arn <SAP HANA DATABASE ARN FROM REGISTERED APPLICATION>
--component-info '[
    {
      "ComponentType": "WD",
      "Sid": "<YOUR_WEB_DISPATCHER_SID>",
      "Ec2InstanceId": "<YOUR_YOUR_WEB_DISPATCHER_EC2_INSTANCE_ID>"
    }
  ]'
```

**Example command with sample values**

```
aws ssm-sap register-application
    --application-id "mySAPABAPApplication" \
    --application-type SAP_ABAP \
    --instances i-0307b3e5fbdc4bda1 \
    --sid ECD \
    --region us-east-1 \
    --database-arn "arn:aws:ssm-sap:us-east-1:123456789101:HANA/SAP_HANA_APPLICATION/DB/HDB"
    --component-info '[{"ComponentType": "WD", "Sid":"WD1", "Ec2InstanceId":"i-07837dbacc572b5f2"}]'
```

**Example JSON response**

```
{
    "Application": {
        "Id": "mySAPABAPApplication",
        "Type": "SAP_ABAP",
        "Arn": "<APPLICATION_ARN>",
        "Status": "REGISTERING",
        "Components": [],
        "LastUpdated": "2022-08-19T10:58:48.521000-07:00"
    },
    "OperationId": "6bd44104-d63c-449d-8007-6c1b471e3e5e" //(Note)
}
```

**Note** Take note of this operation ID. You’ll need it in the next step.

## Step 3: Check registration status

The registration may take a few minutes to complete. Use the following command to check the status of your registration. Use the `OperationId` generated when registering your SAP ABAP application in the preceding step.

```
aws ssm-sap get-operation --operation-id <YOUR_OPERATION_ID> --region <REGION>
```

## Step 4: Verify registration

Verify the registration with [GetApplication](../../../ssmsap/latest/APIReference/API_GetApplication.md "../../../ssmsap/latest/APIReference/API_GetApplication.md") API. You can also view the details of registered databases with [ListDatabases](../../../ssmsap/latest/APIReference/API_ListDatabases.md "../../../ssmsap/latest/APIReference/API_ListDatabases.md") and [GetDatabase](../../../ssmsap/latest/APIReference/API_GetDatabase.md "../../../ssmsap/latest/APIReference/API_GetDatabase.md") API.

1. Run Commands to Verify Registration

**Command template**

```
aws ssm-sap get-application --application-id <APPLICATION_ID> --region <REGION>
```

**Example to get the summary of an application**

```
aws ssm-sap get-application --application-id mySAPABAPApplication --region us-east-1
```

**Example JSON Response**

```
{
  "Application": {
    "Id": "mySAPABAPApplication",
    "Type": "SAP_ABAP",
    "Arn": "arn:aws:ssm-sap:us-east-1:123456789101:SAP_ABAP/mySAPABAPApplication",
    "Status": "ACTIVATED",
    "DiscoveryStatus": "SUCCESS",
    "Components": [
        "ECD-ABAP"
        "WD1-WD14"  //(Note)
    ]
    "LastUpdated": "2023-10-04T22:16:59.106000-07:00"
  },
  "Tags": {}
}
```

**Note** Take note of this component ID. You’ll need it in the next step.

## Step 5: View component summary

Get the component summary with [GetComponent](../../../ssmsap/latest/APIReference/API_GetComponent.md "../../../ssmsap/latest/APIReference/API_GetComponent.md") API.

1. Command template

```
aws ssm-sap get-component --application-id <APPLICATION_ID> --component-id <YOUR_COMPONENT_ID_FROM_LAST_STEP> --region <REGION>
```

2. GetComponent API output for parent component ECD-ABAP

```
aws ssm-sap get-component \
   --application-id mySAPABAPApplication \
   --component-id ECD-ABAP \
   --region us-east-1
```

**Sample JSON Output**

```
{
    "Component": {
        "ComponentId": "ECD-ABAP",
        "Sid": "ECD",
        "ChildComponents": [
            "ECD-ASCS10-sapci",
            "ECD-D12-sapci"
            "ECD-D00-sapappser1",
            "ECD-D00-sapappser2"
        ],
        "ApplicationId": "mySAPABAPApplication",
        "ComponentType": "ABAP",
        "Status": "RUNNING",
        "DatabaseConnection": {
            "DatabaseConnectionMethod": "DIRECT",
            "DatabaseArn": "arn:aws:ssm-sap:us-east-1:123456789101:HANA/SAP_HANA_APPLICATION/DB/HDB",
            "ConnectionIp": "172.31.19.240"
        },
        "LastUpdated": "2023-10-04T22:16:59.089000-07:00",
        "Arn": "arn:aws:ssm-sap:us-east-1:123456789101:SAP_ABAP/mySAPABAPApplication/COMPONENT/ECD-ABAP"
    },
    "Tags": {}
}
```

3. GetComponent API output for parent component WD1-W14

```
aws ssm-sap get-component --component-id WD1-W14\
    --application-id mySAPABAPApplication \
    --region us-east-1
```

**Sample JSON Output**

```
{
    "Component": {
        "ComponentId": "WD1-W14",
        "Sid": "WD1",
        "ChildComponents": [
            "WD1-W14-sapwd"
        ],
        "ApplicationId": "mySAPABAPApplication",
        "ComponentType": "WEBDISP",
        "Status": "RUNNING",
        "LastUpdated": "2024-10-04T22:16:59.089000-07:00",

        "Arn": "arn:aws:ssm-sap:us-east-1:123456789101:SAP_ABAP/mySAPABAPApplication/COMPONENT/WD1-W14"
    },
    "Tags": {}
}
```

4. GetComponent API output for child component ECD-ASCS10-sapci

```
aws ssm-sap get-component \
    --component-id ECD-ASCS10-sapci --application-id mySAPABAPApplication \
    --region us-east-1
```

**Sample Output**

```
{
    "Component": {
        "ComponentId": "ECD-ASCS10-sapci",
        "Sid": "ECD",
        "SystemNumber": "10",
        "ParentComponent": "ECD-ABAP",
        "ApplicationId": "mySAPABAPApplication",
        "ComponentType": "ASCS",
        "Status": "RUNNING",
        "SapFeature": "MESSAGESERVER|ENQUE",
        "SapHostname": "sapci",
        "SapKernelVersion": "785, patch 200, changelist 2150416",
        "Resilience": {
            "EnqueueReplication": false
        },
        "AssociatedHost": {
            "Hostname": "sapci",
            "Ec2InstanceId": "i-0307b3e5fbdc4bda1",
            "IpAddresses": [
                {
                    "IpAddress": "172.31.19.240",
                    "Primary": true,
                    "AllocationType": "VPC_SUBNET"
                }
            ],
            "OsVersion": "SUSE Linux Enterprise Server 15 SP4"
        },
        "LastUpdated": "2023-10-04T22:16:58.915000-07:00",
        "Arn": "arn:aws:ssm-sap:us-east-1:123456789101:SAP_ABAP/mySAPABAPApplication/COMPONENT/ECD-ASCS10-sapci"
    },
    "Tags": {}
}
```

5. GetComponent API for Child Component WD1-W14-sapwd

```
aws ssm-sap get-component \
   --component-id WD1-W14-sapwd --application-id mySAPABAPApplication \
   --region us-east-1
```

**Sample Output**

```
{
    "Component": {
        "ComponentId": "WD1-W14-sapwd",
        "Sid": "WD1",
        "SystemNumber": "14",
        "ParentComponent": "WD1-W14",
        "ApplicationId": "mySAPABAPApplication",
        "ComponentType": "WD",
        "Status": "RUNNING",
        "SapFeature": "WEBDISP",
        "SapHostname": "sapci",
        "SapKernelVersion": "785, patch 200, changelist 2150416",
        "Resilience": {
            "EnqueueReplication": false
        },
        "AssociatedHost": {
            "Hostname": "sapwd",
            "Ec2InstanceId": "i-12345abcde678f9g0",
            "IpAddresses": [
                {
                    "IpAddress": "172.31.32.187",
                    "Primary": true,
                    "AllocationType": "VPC_SUBNET"
                }
            ],
            "OsVersion": "SUSE Linux Enterprise Server 15 SP4"
        },
        "LastUpdated": "2023-10-04T22:16:58.915000-07:00",
        "Arn": "arn:aws:ssm-sap:us-east-1:123456789101:SAP_ABAP/mySAPABAPApplication/COMPONENT/WD1-W14-sapwd"
    },
    "Tags": {}
}
```
