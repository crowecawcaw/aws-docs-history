# Modifying your

application

AWS Resilience Hub allows you to modify your application resources by editing a draft version
of your application and publishing the changes to a new (published) version. AWS Resilience Hub
uses the published version of your application, which includes the updated resources, for
running resiliency assessments.

For more information, see the following topics:

- [Manually adding resources to your
  application](#manually-add-resource-using-api "#manually-add-resource-using-api")
- [Grouping resources into a single
  Application Component](#group-resource-using-api "#group-resource-using-api")
- [Excluding a resource from an
  AppComponent](#exclude-resource-using-api "#exclude-resource-using-api")

## Manually adding resources to your

application

If the resource is not deployed as part of an input source, AWS Resilience Hub allows you
to manually add the resource to your application using
`CreateAppVersionResource` API. For more information about this API,
see [https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateAppVersionResource.html](../APIReference/API_CreateAppVersionResource.md "../APIReference/API_CreateAppVersionResource.md").

You must provide the following parameters to this API:

- Amazon Resource Name (ARN) of the application
- Logical ID of the resource
- Physical ID of the resource
- AWS CloudFormation type

The following example shows how to manually add resources to your application in
AWS Resilience Hub using `CreateAppVersionResource` API.

### Request

```
aws resiliencehub create-app-version-resource \
--app-arn `<App_ARN>` \
--resource-name "backup-efs" \
--logical-resource-id '{"identifier": "backup-efs"}' \
--physical-resource-id '`<Physical_resource_id_ARN>`' \
--resource-type AWS::EFS::FileSystem \
--app-components '["new-app-component"]'
```

### Response

```
{
    "appArn": "`<App_ARN>`",
    "appVersion": "draft",
    "physicalResource": {
        "resourceName": "backup-efs",
        "logicalResourceId": {
            "identifier": "backup-efs"
        },
        "physicalResourceId": {
            "identifier": "`<Physical_resource_id_ARN>`",
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

## Grouping resources into a single

Application Component

An Application Component (AppComponent) is a group of related AWS resources that
work and fail as a single unit. For example, when you have cross-Region workloads
that are used as standby deployments. AWS Resilience Hub has rules governing which AWS
resources can belong to which type of AppComponent. AWS Resilience Hub allows you to group
resources into a single AppComponent using the following resource management
APIs.

- `UpdateAppVersionResource` – This API updates the
  resource details of an application. For more information about this API, see
  [UpdateAppVersionResource](../APIReference/API_UpdateAppVersionResource.md "../APIReference/API_UpdateAppVersionResource.md").
- `DeleteAppVersionAppComponent` – This API deletes the
  AppComponent from the application. For more information about this API, see
  [DeleteAppVersionAppComponent](../APIReference/API_DeleteAppVersionAppComponent.md "../APIReference/API_DeleteAppVersionAppComponent.md").

The following example shows how to update the resource details of your application
in AWS Resilience Hub using `DeleteAppVersionAppComponent` API.

### Request

```
aws resiliencehub delete-app-version-app-component \
--app-arn `<App_ARN>` \
--id new-app-component
```

### Response

```
{
    "appArn": "`<App_ARN>`",
    "appVersion": "draft",
    "appComponent": {
        "name": "new-app-component",
        "type": "AWS::ResilienceHub::StorageAppComponent",
        "id": "new-app-component"
    }
}
```

The following example shows how to delete the empty AppComponent that was created
in the previous examples in AWS Resilience Hub using `UpdateAppVersionResource`
API.

### Request

```
aws resiliencehub delete-app-version-app-component \
--app-arn `<App_ARN>` \
--id new-app-component
```

### Response

```
{
    "appArn": "`<App_ARN>`",
    "appVersion": "draft",
    "appComponent": {
        "name": "new-app-component",
        "type": "AWS::ResilienceHub::StorageAppComponent",
        "id": "new-app-component"
    }
}
```

## Excluding a resource from an

AppComponent

AWS Resilience Hub allows you to exclude resources from assessments using
`UpdateAppVersionResource` API. These resources will not be
considered while computing the resiliency of your application. For more information
about this API, see [https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateAppVersionResource.html](../APIReference/API_UpdateAppVersionResource.md "../APIReference/API_UpdateAppVersionResource.md").

###### Note

You can exclude only those resources that were imported from an input
source.

The following example shows how to exclude a resource of your application in
AWS Resilience Hub using `UpdateAppVersionResource` API.

### Request

```
aws resiliencehub update-app-version-resource \
--app-arn `<App_ARN>` \
--resource-name "ec2instance-nvz" \
--excluded
```

### Response

```
{
    "appArn": "`<App_ARN>`",
    "appVersion": "draft",
    "physicalResource": {
        "resourceName": "ec2instance-nvz",
        "logicalResourceId": {
            "identifier": "ec2",
            "terraformSourceName": "test.state.file"
        },
        "physicalResourceId": {
            "identifier": "i-0b58265a694e5ffc1",
            "type": "Native",
            "awsRegion": "us-west-2",
            "awsAccountId": "123456789101"
        },
        "resourceType": "AWS::EC2::Instance",
        "appComponents": [
            {
                "name": "computeappcomponent-nrz",
                "type": "AWS::ResilienceHub::ComputeAppComponent"
            }
        ]
    }
}
```
