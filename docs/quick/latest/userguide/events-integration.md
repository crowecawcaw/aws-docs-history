

# Amazon Quick Sight events integration
<a name="events-integration"></a>

With Amazon EventBridge, you can respond automatically to events in Amazon Quick Sight such as new dashboard creation or updates. These events are delivered to EventBridge in near real time. As a developer, you can write simple rules to indicate which events are of interest, and what actions to take when an event matches a rule. By using events, you can complete use cases such as continuous backup and deployment.

**Topics**
+ [Supported events](#events-supported)
+ [Example event payload](#sample-events-payload)
+ [Creating rules to send Amazon Quick Sight events to Amazon CloudWatch](events-send-cloudwatch.md)
+ [Creating rules to send Amazon Quick Sight events to AWS Lambda](events-send-lambda.md)

## Supported events
<a name="events-supported"></a>

Amazon Quick Sight currently supports the following events.


| Asset type | Action | Event detail type | Event detail | 
| --- | --- | --- | --- | 
| Dashboard | Create | Amazon Quick Sight Dashboard Creation Successful | <pre>{<br />    "dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83",<br />    "versionNumber": 1<br />}</pre> | 
| Dashboard | Create | Amazon Quick Sight Dashboard Creation Failed | <pre>{<br />    "dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83",<br />    "versionNumber": 1,<br />    "errors": [<br />      {<br />        "Type": "PARAMETER_NOT_FOUND",<br />        "Message": "Missing property abc"<br />      },<br />      {<br />        "Type": "DATA_SET_NOT_FOUND",<br />        "Message": "Cannot find dataset with id abc"<br />      }<br />    ]<br />}</pre> | 
| Dashboard | Create | Amazon Quick Sight Dashboard Permissons Updated | <pre>{"dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83" }</pre> | 
| Dashboard | Update | Amazon Quick Sight Dashboard Update Successful | <pre>{<br />    "dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83",<br />    "versionNumber": 1<br />}</pre> | 
| Dashboard | Update | Amazon Quick Sight Dashboard Update Failed | <pre>{<br />    "dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83",<br />    "versionNumber": 1,<br />    "errors": [<br />      {<br />        "Type": "PARAMETER_NOT_FOUND",<br />        "Message": "Missing property abc"<br />      },<br />      {<br />        "Type": "DATA_SET_NOT_FOUND",<br />        "Message": "Cannot find dataset with id abc"<br />      }<br />    ]<br />}</pre> | 
| Dashboard | Update | Amazon Quick Sight Dashboard Permissons Updated | <pre>{"dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83"}</pre> | 
| Dashboard | Publish | Amazon Quick Sight Dashboard Published Version Updated | <pre>{<br />    "dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83",<br />    "versionNumber": 2<br />}</pre> | 
| Dashboard | Delete | Amazon Quick Sight Dashboard Deleted | <pre>{<br />    "dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83"<br />}</pre> | 
| Analysis | Create | Amazon Quick Sight Analysis Creation Successful | <pre>{<br />    "analysisId": "e5f37119-e24c-4874-901a-af9032b729b5"<br />}</pre> | 
| Analysis | Create | Amazon Quick Sight Analysis Creation Failed | <pre>{<br />    "analysisId": "e5f37119-e24c-4874-901a-af9032b729b5",<br />    "errors": [<br />      {<br />        "Type": "PARAMETER_NOT_FOUND",<br />        "Message": "Missing property abc"<br />      },<br />      {<br />        "Type": "DATA_SET_NOT_FOUND",<br />        "Message": "Cannot find dataset with id abc"<br />      }<br />    ]<br />}</pre> | 
| Analysis | Create | Amazon Quick Sight Analysis Permissons Updated | <pre>{"analysisId": "e5f37119-e24c-4874-901a-af9032b729b5" }</pre> | 
| Analysis | Delete | Amazon Quick Sight Analysis Deleted | <pre>{<br />    "analysisId": "e5f37119-e24c-4874-901a-af9032b729b5"<br />}</pre> | 
| Analysis | Update | Amazon Quick Sight Analysis update successful | <pre>{<br />    "analysisId": "e5f37119-e24c-4874-901a-af9032b729b5"<br />}</pre> | 
| Analysis | Update | Amazon Quick Sight Analysis update failed | <pre>{<br />    "analysisId": "e5f37119-e24c-4874-901a-af9032b729b5",    <br />    "errors": [        <br />        {            <br />            "Type": "PARAMETER_NOT_FOUND",            <br />            "Message": "Missing property abc"        <br />        },        <br />        {             <br />            "Type": "DATA_SET_NOT_FOUND",            <br />            "Message": "Cannot find dataset with id abc"        <br />        }    <br />    ]<br />}</pre> | 
| Analysis | Update | Amazon Quick Sight Analysis Permissons Updated | <pre>{"analysisId": "e5f37119-e24c-4874-901a-af9032b729b5" }</pre> | 
| VPC connection | Create | Amazon Quick Sight VPC Connection Creation Successful | <pre>{<br />    "vpcConnectionId": "53d34238-57e7-488d-b99a-a0037d275a4e",<br />    "availabilityStatus": "CREATION_SUCCESSFUL"<br />}</pre> | 
| VPC connection | Create | Amazon Quick Sight VPC Connection Creation Failed | <pre>{<br />    "vpcConnectionId": "53d34238-57e7-488d-b99a-a0037d275a4e",<br />    "availabilityStatus": "CREATION_FAILED"<br />}</pre> | 
| VPC connection | Update | Amazon Quick Sight VPC Connection Update Successful | <pre>{<br />    "vpcConnectionId": "53d34238-57e7-488d-b99a-a0037d275a4e",<br />    "availabilityStatus": "UPDATE_SUCCESSFUL"<br />}</pre> | 
| VPC connection | Update | Amazon Quick Sight VPC Connection Update Failed | <pre>{<br />    "vpcConnectionId": "53d34238-57e7-488d-b99a-a0037d275a4e",<br />    "availabilityStatus": "UPDATE_FAILED"<br />}</pre> | 
| VPC connection | Delete | Amazon Quick Sight VPC Connection Deletion Successful | <pre>{<br />    "vpcConnectionId": "53d34238-57e7-488d-b99a-a0037d275a4e",<br />    "availabilityStatus": "DELETED"<br />}</pre> | 
| VPC connection | Delete | Amazon Quick Sight VPC Connection Deletion Failed | <pre>{<br />    "vpcConnectionId": "53d34238-57e7-488d-b99a-a0037d275a4e",<br />    "availabilityStatus": "DELETION_FAILED"<br />}</pre> | 
| Folder | Create | Amazon Quick Sight Folder Created | <pre>{<br />    "folderId": "77e307e8-b41b-472a-90e8-fe3f471537be",<br />    "parentFolderArn": "arn:aws:quicksight:us-east-1:123456789012:folder/098765432134"<br />}</pre> | 
| Folder | Create | Amazon Quick Sight Folder Permissions Updated | <pre>{"folderId": "77e307e8-b41b-472a-90e8-fe3f471537be" }</pre> | 
| Folder | Update | Amazon Quick Sight Folder Updated | <pre>{<br />    "folderId": "77e307e8-b41b-472a-90e8-fe3f471537be"<br />}</pre> | 
| Folder | Update | Amazon Quick Sight Folder Permissions Updated | <pre>{"folderId": "77e307e8-b41b-472a-90e8-fe3f471537be" }</pre> | 
| Folder | Delete | Amazon Quick Sight Folder Deleted | <pre>{<br />    "folderId": "77e307e8-b41b-472a-90e8-fe3f471537be"<br />}</pre> | 
| Folder | Membership update | Amazon Quick Sight Folder Membership Updated | <pre>{<br />    "folderId": "77e307e8-b41b-472a-90e8-fe3f471537be",<br />    "membersAdded": ["arn:aws:quicksight:us-east-1:123456789012:analysis/e5f37119-e24c-4874-901a-af9032b729b5"],<br />    "membersRemoved": []<br />}</pre> | 
| Dataset | Create | Amazon Quick Sight Dataset Created | <pre>{<br />    "datasetId": "a6553a81-f97e-4ffa-a860-baea63196efa"<br />}</pre> | 
| Dataset | Create | Amazon Quick Sight Dataset Permissions Updated | <pre>{"datasetId": "a6553a81-f97e-4ffa-a860-baea63196efa" }</pre> | 
| Dataset | Update | Amazon Quick Sight Dataset Updated | <pre>{<br />    "datasetId": "a6553a81-f97e-4ffa-a860-baea63196efa"<br />}</pre> | 
| Dataset | Update | Amazon Quick Sight Dataset Permissions Updated | <pre>{"datasetId": "a6553a81-f97e-4ffa-a860-baea63196efa" }</pre> | 
| Dataset | Delete | Amazon Quick Sight Dataset Deleted | <pre>{<br />    "datasetId": "a6553a81-f97e-4ffa-a860-baea63196efa"<br />}</pre> | 
| DataSource | Create | Amazon Quick Sight DataSource Creation Successful | <pre>{<br />    "datasourceId": "230caa6e-dc87-406b-91fb-037f29c32824"<br />}</pre> | 
| DataSource | Create | Amazon Quick Sight DataSource Creation Failed | <pre>{<br />    "datasourceId": "230caa6e-dc87-406b-91fb-037f29c32824",<br />    "error": {<br />        "message": "AMAZON_ELASTICSEARCH engine version 7.4 is lower than minimum supported version 7.7",<br />        "type": "ENGINE_VERSION_NOT_SUPPORTED"<br />    }<br />}</pre> | 
| DataSource | Create | Amazon Quick Sight DataSource Permissions Updated | <pre>{"datasourceId": "230caa6e-dc87-406b-91fb-037f29c32824" }</pre> | 
| DataSource | Update | Amazon Quick Sight DataSource Update Successful | <pre>{<br />    "datasourceId": "230caa6e-dc87-406b-91fb-037f29c32824"<br />}</pre> | 
| DataSource | Update | Amazon Quick Sight DataSource Update Failed | <pre>{<br />    "datasourceId": "230caa6e-dc87-406b-91fb-037f29c32824",<br />    "error": {<br />        "message": "AMAZON_ELASTICSEARCH engine version 7.4 is lower than minimum supported version 7.7",<br />        "type": "ENGINE_VERSION_NOT_SUPPORTED"<br />    }<br />}</pre> | 
| DataSource | Update | Amazon Quick Sight DataSource Permissions Updated | <pre>{"datasourceId": "230caa6e-dc87-406b-91fb-037f29c32824" }</pre> | 
| DataSource | Delete | Amazon Quick Sight DataSource Deleted | <pre>{<br />    "datasourceId": "230caa6e-dc87-406b-91fb-037f29c32824"<br />}</pre> | 
| Theme | Create | Amazon Quick Sight Theme Creation Successful | <pre>{<br />    ""themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83", <br />    "versionNumber": 1"<br />}</pre> | 
| Theme | Create | Amazon Quick Sight Theme Creation Failed | <pre>{ <br />    "themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83", <br />    "versionNumber": 1<br />}</pre> | 
| Theme | Create | Amazon Quick Sight Theme Permissions Updated | <pre>{"themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83" }</pre> | 
| Theme | Update | Amazon Quick Sight Theme Update Successful | <pre>{<br />    "themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83",    <br />    "versionNumber": 2<br />}</pre> | 
| Theme | Update | Amazon Quick Sight Theme Update Failed | <pre>{<br />    "themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83",    <br />    "versionNumber": 2<br />}</pre> | 
| Theme | Update | Amazon Quick Sight Theme Permissions Updated | <pre>{"themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83" }</pre> | 
| Theme | Delete | Amazon Quick Sight Theme deleted | <pre>{<br />    "themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83"<br />}</pre> | 
| Theme | Alias Create | Amazon Quick Sight Theme Alias Created | <pre>{<br />    "themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83",    <br />    "aliasName": "MyThemeAlias"    <br />    "versionNumber": 2<br />}</pre> | 
| Theme | Alias Update | Amazon Quick Sight Alias Updated | <pre>{<br />    "themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83",    <br />    "aliasName": "MyThemeAlias"    <br />    "versionNumber": 4<br />}</pre> | 
| Theme | Alias Delete | Amazon Quick Sight Theme Alias Deleted | <pre>{<br />    "themeId": "6fdbc328-ebbd-457f-aa02-9780173afc83",    <br />    "aliasName": "MyThemeAlias"    <br />    "versionNumber": 2<br />}</pre> | 

## Example event payload
<a name="sample-events-payload"></a>

All events follow the standard EventBridge [object structure](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html). The detail field is a JSON object that contains more information about the event.

```
{
  "version": "0",
  "id": "3acb26c8-397c-4c89-a80a-ce672a864c55",
  "detail-type": "QuickSight Dashboard Creation Successful",
  "source": "aws.quicksight",
  "account": "123456789012",
  "time": "2023-10-30T22:06:31Z",
  "region": "us-east-1",
  "resources": ["arn:aws:quicksight:us-east-1:123456789012:dashboard/6fdbc328-ebbd-457f-aa02-9780173afc83"],
  "detail": {
    "dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83",
    "versionNumber": 1
  }
}
```