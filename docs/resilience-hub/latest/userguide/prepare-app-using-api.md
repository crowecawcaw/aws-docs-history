

# Preparing the application
<a name="prepare-app-using-api"></a>

For preparing an application, you must first create an application, assign a resiliency policy, and then import the application resources from your input sources. For more information about the AWS Resilience Hub APIs that are used to prepare an application, see the following topics:
+ [Creating an application](#create-app-using-api)
+ [Creating resiliency policy](#create-res-policy-using-api)
+ [Importing resources from an input source and monitoring the import status](#import-app-resource-using-api)
+ [Publishing the draft version of your application and assigning a resiliency policy](#publish-application-using-api)

## Creating an application
<a name="create-app-using-api"></a>

To create a new application in AWS Resilience Hub, you must call the `CreateApp` API and provide a unique application name. For more information about this API, see [https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateApp.html](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateApp.html).

The following example shows how to create a new application `newApp` in AWS Resilience Hub using `CreateApp` API. 

### Request
<a name="create-app-using-api-req"></a>

```
aws resiliencehub create-app --name newApp
```

### Response
<a name="create-app-using-api-res"></a>

```
{
    "app": {
        "appArn": "<App_ARN>",
        "name": "newApp",
        "creationTime": "2022-10-26T19:48:00.434000+03:00",
        "status": "Active",
        "complianceStatus": "NotAssessed",
        "resiliencyScore": 0.0,
        "tags": {},
        "assessmentSchedule": "Disabled"
    }
}
```

## Creating resiliency policy
<a name="create-res-policy-using-api"></a>

After creating the application, you must create a resiliency policy that enables you to understand your application’s resiliency posture using `CreateResiliencyPolicy` API. For more information about this API, see [https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateResiliencyPolicy.html](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateResiliencyPolicy.html).

The following example shows how to create `newPolicy` for your application in AWS Resilience Hub using `CreateResiliencyPolicy` API.

### Request
<a name="create-res-policy-using-api-req"></a>

```
aws resiliencehub create-resiliency-policy \
--policy-name newPolicy --tier NonCritical \
--policy '{"AZ": {"rtoInSecs": 172800,"rpoInSecs": 86400}, \
"Hardware": {"rtoInSecs": 172800,"rpoInSecs": 86400}, \
"Software": {"rtoInSecs": 172800,"rpoInSecs": 86400}}'
```

### Response
<a name="create-res-policy-using-api-res"></a>

```
{
    "policy": {
        "policyArn": "<Policy_ARN>",
        "policyName": "newPolicy",
        "policyDescription": "",
        "dataLocationConstraint": "AnyLocation",
        "tier": "NonCritical",
        "estimatedCostTier": "L1",
        "policy": {
            "AZ": {
                "rtoInSecs": 172800,
                "rpoInSecs": 86400
            },
            "Hardware": {
                "rtoInSecs": 172800,
                "rpoInSecs": 86400
            },
            "Software": {
                "rtoInSecs": 172800,
                "rpoInSecs": 86400
            }
        },
        "creationTime": "2022-10-26T20:48:05.946000+03:00",
        "tags": {}
    }
}
```

## Importing resources from an input source and monitoring the import status
<a name="import-app-resource-using-api"></a>

AWS Resilience Hub provides the following APIs to import resources to your application:
+ `ImportResourcesToDraftAppVersion` – This API allows you to import resources to the draft version of your application from different input sources. For more information about this API, see [https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ImportResourcesToDraftAppVersion.html](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ImportResourcesToDraftAppVersion.html).
+ `PublishAppVersion` – This API publishes a new version of the application along with the updated AppComponents. For more information about this API, see [https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PublishAppVersion.html](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PublishAppVersion.html).
+ `DescribeDraftAppVersionResourcesImportStatus` – This API allows you to monitor the import status of your resources to an application version. For more information about this API, see [https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeDraftAppVersionResourcesImportStatus.html](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeDraftAppVersionResourcesImportStatus.html).

The following example shows how to import resources to your application in AWS Resilience Hub using `ImportResourcesToDraftAppVersion` API.

### Request
<a name="w2aab5c14b9c11b9"></a>

```
aws resiliencehub import-resources-to-draft-app-version \
--app-arn <App_ARN> \
--terraform-sources '[{"s3StateFileUrl": <S3_URI>}]'
```

### Response
<a name="w2aab5c14b9c11c13"></a>

```
{
    "appArn": "<App_ARN>",
    "appVersion": "draft",
    "sourceArns": [],
    "status": "Pending",
    "terraformSources": [
        {
            "s3StateFileUrl": <S3_URI>
        }
    ]
}
```

The following example shows how to manually add resources to your application in AWS Resilience Hub using `CreateAppVersionResource` API.

### Request
<a name="create-res-policy-using-api-req"></a>

```
aws resiliencehub create-app-version-resource \
--app-arn <App_ARN> \
--resource-name "backup-efs" \
--logical-resource-id '{"identifier": "backup-efs"}' \
--physical-resource-id '<Physical_resource_id_ARN>' \
--resource-type AWS::EFS::FileSystem \
--app-components '["new-app-component"]'
```

### Response
<a name="create-res-policy-using-api-res"></a>

```
{
    "appArn": "<App_ARN>",
    "appVersion": "draft",
    "physicalResource": {
        "resourceName": "backup-efs",
        "logicalResourceId": {
            "identifier": "backup-efs"
        },
        "physicalResourceId": {
            "identifier": "<Physical_resource_id_ARN>",
            "type": "Arn"
        },
        "resourceType": "AWS::EFS::FileSystem",
        "appComponents": [
            {
                "name": "new-app-component",
                "type": "AWS::ResilienceHub::StorageAppComponent",
                "id": "new-app-component"
            }
        ]
    }
}
```

The following example shows how to monitor the import status of your resources in AWS Resilience Hub using `DescribeDraftAppVersionResourcesImportStatus` API.

### Request
<a name="describe-draft-app-policy-req"></a>

```
aws resiliencehub describe-draft-app-version-resources-import-status \
--app-arn <App_ARN>
```

### Response
<a name="describe-draft-app-policy-res"></a>

```
{
    "appArn": "<App_ARN>",
    "appVersion": "draft",
    "status": "Success",
    "statusChangeTime": "2022-10-26T19:55:18.471000+03:00"
}
```

## Publishing the draft version of your application and assigning a resiliency policy
<a name="publish-application-using-api"></a>

Before running an assessment, you must first publish the draft version of your application and assign a resiliency policy to the released version of your application. 

**To publish the draft version of your application and assign a resiliency policy**

1. To publish the draft version of your application, use `PublishAppVersion` API. For more information about this API, see [https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PublishAppVersion.html](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PublishAppVersion.html).

   The following example shows how to publish the draft version of the application in AWS Resilience Hub using `PublishAppVersion` API.

   

**Request**  


   ```
   aws resiliencehub publish-app-version \
    --app-arn <App_ARN>
   ```

**Response**  


   ```
   {
       "appArn": "<App_ARN>",
       "appVersion": "release"
   }
   ```

1. Apply a resiliency policy to the released version of your application using `UpdateApp` API. For more information about this API, see [https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateApp.html](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateApp.html).

   The following example shows how to apply a resiliency policy to the released version of an application in AWS Resilience Hub using `UpdateApp` API.

**Request**  


   ```
   aws resiliencehub update-app \
   --app-arn <App_ARN> \
   --policy-arn <Policy_ARN>
   ```

**Response**  


   ```
   {
       "app": {
           "appArn": "<App_ARN>",
           "name": "newApp",
           "policyArn": "<Policy_ARN>",
           "creationTime": "2022-10-26T19:48:00.434000+03:00",
           "status": "Active",
           "complianceStatus": "NotAssessed",
           "resiliencyScore": 0.0,
           "tags": {
               "resourceArn": "<App_ARN>"
           },
           "assessmentSchedule": "Disabled"
       }
   }
   ```