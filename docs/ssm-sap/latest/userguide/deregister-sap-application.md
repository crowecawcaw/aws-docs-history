# Deregister SAP application

The following steps will guide you through deregistration your SAP HANA application or of your single node setup of SAP ABAP application registered with Systems Manager for SAP.

If a database has not been previously registered with AWS Systems Manager, the deregistration process will result in a `ValidationException`.

## Step 1: Get ApplicationId of your SAP application

**Command template**

```
 aws ssm-sap list-applications --region <REGION_ID>
```

Note the `ApplicationId` of your registration.

## Step 2: Deregister SAP application

You can use the AWS CLI command [deregister-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/deregister-application.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/deregister-application.html") (API [DeregisterApplication](../../../ssmsap/latest/APIReference/API_DeregisterApplication.md "../../../ssmsap/latest/APIReference/API_DeregisterApplication.md")) to deregister your SAP application.

**Command template**

```
 aws ssm-sap deregister-application --application-id <APPLICATION_ID> --region <REGION>
```

The parameter `application-id` is required. As the value, use the ApplicationID retrieved in Step 1.

## Step 3: Verify deregistration

Run the command [list-applications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/list-applications.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/list-applications.html") ([ListApplications](../../../ssmsap/latest/APIReference/API_ListApplications.md "../../../ssmsap/latest/APIReference/API_ListApplications.md") API) to verify your application is not present.
