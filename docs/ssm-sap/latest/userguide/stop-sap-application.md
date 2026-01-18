# Stop SAP application

You can perform a stop operation on a single node or HA (high availability) SAP HANA application or on a single node or distrubuted setup of SAP ABAP application that has been registered with AWS Systems Manager for SAP.

While performing the stop operation on an SAP HANA application, you can optionally also stop the Amazon EC2 instance(s) on which the SAP HANA application is running. While performing a stop operation on a single node setup of SAP ABAP application, you can optionally also stop the HANA database application and the Amazon EC2 instance on which the SAP ABAP application is running.

Before you initiate a stop operation, complete the setup prerequisites described in [Get started with AWS Systems Manager for SAP](get-started.md "get-started.md") and register your SAP application, if you have not already done so.

You can stop Systems Manager for SAP application using AWS CLI or AWS Management Console. The following procedure is for stopping an SAP application using AWS CLI.

###### Topics

- [Step 1: Register SAP Application](#step1-stop-application "#step1-stop-application")
- [Step 2: Stop SAP Application](#step2-stop-application "#step2-stop-application")
- [Step 3: Check Stop Operation status](#step3-stop-application "#step3-stop-application")
- [Step 4: Monitor and verify stop operation](#step4-stop-application "#step4-stop-application")

## Step 1: Register SAP Application

Register your SAP application, if you have not already done so. For more information, see [Register SAP HANA database](register-database.md "register-database.md") or [Register SAP ABAP application](register-abap.md "register-abap.md").

## Step 2: Stop SAP Application

You can use the following AWS CLI command to stop your SAP application:

```
 aws ssm-sap stop-application \
--application-id <APPLICATION_ID> \
--stop-connected-entity <ENTITY> \
--include-ec2-instance-shutdown \
--region <REGION_ID>
```

The parameter `application-id` is required. As the value, use the ApplicationID generated from registration in Step 1.

The following parameters are optional:

- Use the `stop-connected-entity` parameter with a value of `DBMS` (Database Management System) to also stop the corresponding database application when you stop a single node setup of an SAP ABAP application.
- Use the Boolean parameter `include-ec2-instance-shutdown` to shut down the Amazon EC2 instance on which the SAP HANA or single node set up of an SAP ABAP application is running

The following are examples of the stop operation on a single node SAP ABAP setup and an SAP HANA setup with AWS Systems Manager for SAP:

SAP ABAP

**Command template**

```
 aws ssm-sap stop-application --application-id <APPLICATION_ID> --stop-connected-entity <ENTITY> --include-ec2-instance-shutdown --region <REGION_ID>
```

**Command example**

```
 aws ssm-sap stop-application \
--application-id myABAPApplication \
--stop-connected-entity DBMS \
--include-ec2-instance-shutdown \
--region us-east-1
```

**Return example**

```
 {
    "OperationId": "a7h4j3k6-8463-836h-018h-7sh377h6hhd6"
}
```

SAP HANA

**Command template**

```
 aws ssm-sap stop-application --application-id <APPLICATION_ID> --include-ec2-instance-shutdown --region <REGION_ID>
```

**Command example**

```
 aws ssm-sap stop-application \
--application-id myABAPApplication \
--include-ec2-instance-shutdown \
--region us-east-1
```

**Return Example**

```
 {
    "OperationId": "j3h5j4k5-8323-192j-102n-18h7hhh27h27"
}
```

## Step 3: Check Stop Operation status

The stop operation can take up to five minutes to complete. During that time, you can use the following command to check the status of the operation. Use the `OperationId` that was generated in Step 2.

**Command template**

```
 aws ssm-sap get-operation --operation-id <OPERATION_ID> --region <REGION_ID>
```

**Command example**

```
 aws ssm-sap get-operation \
--operation-id b2bc3266-9369-4163-b935-6a586c80e76b \
--region us-east-1
```

## Step 4: Monitor and verify stop operation

Verify the stop operation on the application through the event using the [ListOperationEvents](../../../ssmsap/latest/APIReference/API_ListOperationEvents.md "../../../ssmsap/latest/APIReference/API_ListOperationEvents.md") API.

**Command template**

```
 aws ssm-sap list-operation-events --operation-id <OPERATION_ID> --region <REGION_ID>
```

**Command example**

```
 aws ssm-sap list-operation-events \
--operation-id a1bc2345-6789-0123-d456-7e890f12g34h
```

**Return example**

```
 {
    "OperationEvents": [
        {
            "Description": "Stop the EC2 instance i-abcdefgh987654321",
            "Resource": {
                "ResourceArn": "arn:aws:ec2:us-east-1:111111111111:instance/i-abcdefgh987654321",
                "ResourceType": "AWS::EC2::Instance"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:55:59.846000+00:00"
        },
        {
            "Description": "Stop the EC2 instance i-abcdefgh987654321",
            "Resource": {
                "ResourceArn": "arn:aws:ec2:us-east-1:111111111111:instance/i-abcdefgh987654321",
                "ResourceType": "AWS::EC2::Instance"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:54:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component HDB-HDB00",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:HANA/hanaStartStop/COMPONENT/HDB-HDB00",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:53:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component HDB-HDB00-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:HANA/hanaStartStop/COMPONENT/HDB-HDB00-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:52:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component HDB-HDB00-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:HANA/hanaStartStop/COMPONENT/HDB-HDB00-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:51:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component HDB-HDB00",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:HANA/hanaStartStop/COMPONENT/HDB-HDB00",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:50:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component ECD-ABAP",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-ABAP",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:49:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component ECD-ASCS10-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-ASCS10-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:48:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component ECD-ASCS10-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-ASCS10-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:47:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component ECD-D12-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-D12-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "COMPLETED",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:46:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component ECD-D12-sapci",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-D12-sapci",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:45:59.846000+00:00"
        },
        {
            "Description": "Stop the SAP component ECD-ABAP",
            "Resource": {
                "ResourceArn": "arn:aws:ssm-sap:us-east-1:111111111111:SAP_ABAP/nwStartStop/COMPONENT/ECD-ABAP",
                "ResourceType": "AWS::SystemsManagerSAP::Component"
            },
            "Status": "IN_PROGRESS",
            "StatusMessage": "",
            "Timestamp": "2024-01-03T04:44:59.846000+00:00"
        }
    ]
}
```
