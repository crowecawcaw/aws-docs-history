# Start SAP application

You can perform a start operation on a single node or HA (high availability) SAP HANA application or on a single node or distributed setup of an SAP ABAP application which is registered with AWS Systems Manager for SAP.

When starting an SAP HANA application, the Amazon EC2 instance(s) on which the SAP HANA application will run is started first (if it is not already running), before the application is started. When starting a single node setup of an SAP ABAP application, the HANA database and/or the Amazon EC2 instance on which the SAP ABAP application will run is started first (if it is not already running).

Before you initiate a start operation, complete the setup prerequisites described in [Get started with AWS Systems Manager for SAP](get-started.md "get-started.md") and register your SAP application, if you have not already done so.

You can start Systems Manager for SAP application using AWS CLI or AWS Management Console. The following procedure is for starting an SAP application using AWS CLI.

###### Topics

- [Step 1: Register SAP Application](#step1-start-application "#step1-start-application")
- [Step 2: Start SAP Application](#step2-start-application "#step2-start-application")
- [Step 3: Check Start Operation status](#step3-start-application "#step3-start-application")
- [Step 4: Monitor and verify Start operation](#step4-start-application "#step4-start-application")

## Step 1: Register SAP Application

Register your SAP application, if you have not already done so. For more information, see [Register SAP HANA database](register-database.md "register-database.md") or [Register SAP ABAP application](register-abap.md "register-abap.md").

In your records, note the `ApplicationId` of your registration.

## Step 2: Start SAP Application

You can use the following AWS CLI command to start your SAP application:

```
aws ssm-sap start-application \
--application-id <APPLICATION_ID> \
--region <REGION_ID>
```

The parameter `application-id` is required. As the value, use the ApplicationID generated from registration in Step 1.

**Command template**

```
aws ssm-sap start-application --application-id <APPLICATION_ID> --region <REGION_ID>
```

**Command example**

```
aws ssm-sap start-application \
--application-id myHanaApplication \
--region us-east-1
```

**Return example**

```
{
    "OperationId": "a7h4j3k6-8463-836h-018h-7sh377h6hhd6" //(Note)
}
```

**Note** the OperationId for use in the next step

## Step 3: Check Start Operation status

The start operation can take up to five minutes to complete. During that time, you can use the following command to check the status of the operation. Use the `OperationId` that was generated in Step 2.

**Command template**

```
aws ssm-sap get-operation --operation-id <OPERATION_ID> --region <REGION_ID>
```

## Step 4: Monitor and verify Start operation

Verify the start operation on the application through the event using the [ListOperationEvents](../../../ssmsap/latest/APIReference/API_ListOperationEvents.md "../../../ssmsap/latest/APIReference/API_ListOperationEvents.md") API.

**Command template**

```
aws ssm-sap list-operation-events --operation-id <OPERATION_ID> --region <REGION_ID>
```

**Command example**

```
aws ssm-sap list-operation-events \
--operation-id b2bc3266-9369-4163-b935-6a586c80e76b \
--region us-east-1
```

**Json output**

```
{
    "OperationEvents": [
        {
            "Description": "Start the SAP component ECD-ABAP",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-ABAP",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:53:59.846000+00:00"
        },
        {
            "Description": "Start the SAP component ECD-D12-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-D12-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:52:59.846000+00:00"
        },
        {
            "Description": "Start the SAP component ECD-D12-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-D12-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:51:59.846000+00:00"
        },
        {
            "Description": "Start the SAP component ECD-ASCS10-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-ASCS10-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:50:59.846000+00:00"
        },
        {
            "Description": "Start the SAP component ECD-ASCS10-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-ASCS10-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:49:59.846000+00:00"
        },
        {
            "Description": "Start the SAP component ECD-ABAP",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-ABAP",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:48:59.846000+00:00"
        },
        {
            "Description": "Start the SAP component HDB-HDB00",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:HANA/hanaStartStop/COMPONENT/HDB-HDB00",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:47:59.856000+00:00"
        },
        {
            "Description": "Start the SAP component HDB-HDB00-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:HANA/hanaStartStop/COMPONENT/HDB-HDB00-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:47:59.846000+00:00"
        },
        {
            "Description": "Start the SAP component HDB-HDB00-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:HANA/hanaStartStop/COMPONENT/HDB-HDB00-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:46:59.846000+00:00"
        },
        {
            "Description": "Start the SAP component HDB-HDB00",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:HANA/hanaStartStop/COMPONENT/HDB-HDB00",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:46:59.836000+00:00"
        },
        {
            "Description": "Start the EC2 instance i-abcdefgh987654321",
            "Resource": {
                "ResourceArn": "arn:aws:ec2:us-east-1:111111111111:instance/i-abcdefgh987654321",
                "ResourceType": "AWS::EC2::Instance"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:45:59.846000+00:00"
        },
        {
            "Description": "Start the EC2 instance i-abcdefgh987654321",
            "Resource": {
                "ResourceArn": "arn:aws:ec2:us-east-1:111111111111:instance/i-abcdefgh987654321",
                "ResourceType": "AWS::EC2::Instance"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:44:59.846000+00:00"
        }
    ]
}
```
