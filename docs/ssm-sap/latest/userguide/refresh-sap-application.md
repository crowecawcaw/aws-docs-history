# Refresh SAP application

The following steps will guide you through a refresh of your SAP HANA application or of your single node setup of SAP ABAP application. This refresh updates the application metadata in the AWS Systems Manager for SAP.

Before you refresh an application, complete the setup prerequisites described in [Get started with AWS Systems Manager for SAP](get-started.md "get-started.md") and register your SAP application if you have not already done so.

## Step 1: Register SAP Application

Register your SAP application, if you have not already done so. For more information, see [Register SAP HANA database](register-database.md "register-database.md") or [Register SAP ABAP application](register-abap.md "register-abap.md").

In your records, note the `ApplicationId` of your registration.

## Step 2: Refresh SAP Application

You can use the following AWS CLI command to refresh your SAP application:

```
 aws ssm-sap start-application-refresh \
--application-id <APPLICATION_ID> \
--region <REGION_ID>
```

The parameter `application-id` is required. As the value, use the ApplicationID generated from registration in Step 1.

## Step 3: Check Refresh Operation status

The refresh operation can take up to five minutes to complete. During that time, you can use the following command to check the status of the operation. Use the `OperationId` generated in Step 2.

**Command template**

```
 aws ssm-sap get-operation \
--operation-id <OPERATION_ID> \
--region <REGION_ID>
```

## Step 4: Verify application status

Use the command [get-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/get-application.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/get-application.html") ([GetApplication](../../../ssmsap/latest/APIReference/API_GetApplication.md "../../../ssmsap/latest/APIReference/API_GetApplication.md") API) to verify the application status. You can also view the details of registered databases with `ListDatabases` and `GetDatabase` API.

**Command template**

```
 aws ssm-sap get-application --application-id <APPLICATION_ID> --region <REGION_ID>
```

**Example to get the summary of an application**

```
 aws ssm-sap get-application \
--application-id mySAPABAPApplication \
--region us-east-1
```

**Response example**

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
    ],
    "LastUpdated": "2023-10-04T22:16:59.106000-07:00"
  },
  "Tags": {}
}
```
