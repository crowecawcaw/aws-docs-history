# CreateDashboard


Creates a custom dashboard or the Highlights dashboard.



* **Custom dashboards** - Custom dashboards allow you to query 
 events in any event data store type. You can add up to 10 widgets to a custom dashboard. You can manually refresh a custom dashboard, or you can set a refresh schedule.
* **Highlights dashboard** - You can create
 the Highlights dashboard to see a summary of key user activities and API usage across all your event data stores. 
 CloudTrail Lake manages the Highlights dashboard and refreshes the dashboard every 6 hours. To create the Highlights dashboard, you must set and enable a refresh schedule.

 CloudTrail runs queries to populate the dashboard's widgets during a manual or scheduled refresh. CloudTrail must be granted permissions to run the `StartQuery` operation on your behalf. To provide permissions, run the `PutResourcePolicy` operation to attach a resource-based policy to each event data store. For more information, 
 see [Example: Allow CloudTrail to run queries to populate a dashboard](../userguide/security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard "../userguide/security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard") in the *AWS CloudTrail User Guide*.
 


 To set a refresh schedule, CloudTrail must be granted permissions to run the `StartDashboardRefresh` operation to refresh the dashboard on your behalf. To provide permissions, run the `PutResourcePolicy` operation to attach a resource-based policy to the dashboard. For more information, 
 see [Resource-based policy example for a dashboard](../userguide/security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards "../userguide/security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards") in the *AWS CloudTrail User Guide*.
 

For more information about dashboards, see [CloudTrail Lake dashboards](../userguide/lake-dashboard.md "../userguide/lake-dashboard.md") in the *AWS CloudTrail User Guide*.


## Request Syntax



```
{
   "Name": "`string`",
   "RefreshSchedule": { 
      "Frequency": { 
         "Unit": "`string`",
         "Value": `number`
      },
      "Status": "`string`",
      "TimeOfDay": "`string`"
   },
   "TagsList": [ 
      { 
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "TerminationProtectionEnabled": `boolean`,
   "Widgets": [ 
      { 
         "QueryParameters": [ "`string`" ],
         "QueryStatement": "`string`",
         "ViewProperties": { 
            "`string`" : "`string`" 
         }
      }
   ]
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[Name](#API_CreateDashboard_RequestSyntax "#API_CreateDashboard_RequestSyntax")**



 The name of the dashboard. The name must be unique to your account.



To create the Highlights dashboard, the name must be `AWSCloudTrail-Highlights`.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 128.


Pattern: `^[a-zA-Z0-9_\-]+$`



Required: Yes




**[RefreshSchedule](#API_CreateDashboard_RequestSyntax "#API_CreateDashboard_RequestSyntax")**



 The refresh schedule configuration for the dashboard.



To create the Highlights dashboard, you must set a refresh schedule and set the `Status` to `ENABLED`. The `Unit` for the refresh schedule must be `HOURS` 
 and the `Value` must be `6`.


Type: [RefreshSchedule](API_RefreshSchedule.md "API_RefreshSchedule.md") object


Required: No




**[TagsList](#API_CreateDashboard_RequestSyntax "#API_CreateDashboard_RequestSyntax")**


A list of tags.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Maximum number of 200 items.


Required: No




**[TerminationProtectionEnabled](#API_CreateDashboard_RequestSyntax "#API_CreateDashboard_RequestSyntax")**



 Specifies whether termination protection is enabled for the dashboard. If termination protection is enabled, you cannot delete the dashboard until termination protection is disabled.



Type: Boolean


Required: No




**[Widgets](#API_CreateDashboard_RequestSyntax "#API_CreateDashboard_RequestSyntax")**



An array of widgets for a custom dashboard. A custom dashboard can have a maximum of ten widgets.



You do not need to specify widgets for the Highlights dashboard.


Type: Array of [RequestWidget](API_RequestWidget.md "API_RequestWidget.md") objects


Required: No




## Response Syntax



```
{
   "DashboardArn": "***string***",
   "Name": "***string***",
   "RefreshSchedule": { 
      "Frequency": { 
         "Unit": "***string***",
         "Value": ***number***
      },
      "Status": "***string***",
      "TimeOfDay": "***string***"
   },
   "TagsList": [ 
      { 
         "Key": "***string***",
         "Value": "***string***"
      }
   ],
   "TerminationProtectionEnabled": ***boolean***,
   "Type": "***string***",
   "Widgets": [ 
      { 
         "QueryAlias": "***string***",
         "QueryParameters": [ "***string***" ],
         "QueryStatement": "***string***",
         "ViewProperties": { 
            "***string***" : "***string***" 
         }
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[DashboardArn](#API_CreateDashboard_ResponseSyntax "#API_CreateDashboard_ResponseSyntax")**



The ARN for the dashboard.



Type: String


Pattern: `^[a-zA-Z0-9._/\-:]+$`





**[Name](#API_CreateDashboard_ResponseSyntax "#API_CreateDashboard_ResponseSyntax")**



The name of the dashboard.



Type: String


Length Constraints: Minimum length of 3. Maximum length of 128.


Pattern: `^[a-zA-Z0-9_\-]+$`





**[RefreshSchedule](#API_CreateDashboard_ResponseSyntax "#API_CreateDashboard_ResponseSyntax")**



The refresh schedule for the dashboard, if configured.



Type: [RefreshSchedule](API_RefreshSchedule.md "API_RefreshSchedule.md") object




**[TagsList](#API_CreateDashboard_ResponseSyntax "#API_CreateDashboard_ResponseSyntax")**


A list of tags.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Maximum number of 200 items.




**[TerminationProtectionEnabled](#API_CreateDashboard_ResponseSyntax "#API_CreateDashboard_ResponseSyntax")**



 Indicates whether termination protection is enabled for the dashboard.



Type: Boolean




**[Type](#API_CreateDashboard_ResponseSyntax "#API_CreateDashboard_ResponseSyntax")**



The dashboard type.



Type: String


Valid Values: `MANAGED | CUSTOM`





**[Widgets](#API_CreateDashboard_ResponseSyntax "#API_CreateDashboard_ResponseSyntax")**



An array of widgets for the dashboard.



Type: Array of [Widget](API_Widget.md "API_Widget.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ConflictException** 


This exception is thrown when the specified resource is not ready for an operation. This
 can occur when you try to run an operation on a resource before CloudTrail has time
 to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the
 operation again.


HTTP Status Code: 400




**EventDataStoreNotFoundException** 


The specified event data store was not found.


HTTP Status Code: 400




**InactiveEventDataStoreException** 


The event data store is inactive.


HTTP Status Code: 400




**InsufficientEncryptionPolicyException** 


For the `CreateTrail`
`PutInsightSelectors`, `UpdateTrail`, `StartQuery`, and `StartImport` operations, this exception is thrown 
 when the policy on the S3 bucket or AWS KMS key does
 not have sufficient permissions for the operation.


For all other operations, this exception is thrown when the policy for the AWS KMS key does
 not have sufficient permissions for the operation.


HTTP Status Code: 400




**InvalidQueryStatementException** 


The query that was submitted has validation errors, or uses incorrect syntax or
 unsupported keywords. For more information about writing a query, see [Create or edit a query](../userguide/query-create-edit-query.md "../userguide/query-create-edit-query.md") in the *AWS CloudTrail User
 Guide*.


HTTP Status Code: 400




**InvalidTagParameterException** 


This exception is thrown when the specified tag key or values are not valid. It can also
 occur if there are duplicate tags or too many tags on the resource.


HTTP Status Code: 400




**ServiceQuotaExceededException** 



 This exception is thrown when the quota is exceeded. For information about CloudTrail quotas, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail "https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail") 
 in the *AWS General Reference*.



HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## Examples


### Example


The following example creates a custom dashboard named `AccountActivityDashboard` with 
 four widgets and a refresh schedule of every 12 hours. This example enables termination protection to prevent the dashboard from being accidentally deleted.



```
{
  "Name": "AccountActivityDashboard",
  "RefreshSchedule": {
    "Frequency": {
      "Unit": "HOURS",
      "Value": 12
    },
    "Status": "ENABLED",
    "TimeOfDay": "00:00"
  },
  "TerminationProtectionEnabled": true,
  "Widgets": [
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "TopErrors",
        "View": "Table"
      },
      "QueryStatement": "SELECT errorCode, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' AND (errorCode is not null) GROUP BY errorCode ORDER BY eventCount DESC LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    },
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "MostActiveRegions",
        "View": "PieChart",
        "LabelColumn": "awsRegion",
        "ValueColumn": "eventCount",
        "FilterColumn": "awsRegion"
      },
      "QueryStatement": "SELECT awsRegion, COUNT(*) AS eventCount FROM eds where eventTime > '?' and eventTime < '?' GROUP BY awsRegion ORDER BY eventCount LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    },
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "AccountActivity",
        "View": "LineChart",
        "YAxisColumn": "eventCount",
        "XAxisColumn": "eventDate",
        "FilterColumn": "readOnly"
      },
      "QueryStatement": "SELECT DATE_TRUNC('?', eventTime) AS eventDate, IF(readOnly, 'read', 'write') AS readOnly, COUNT(*) as eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY DATE_TRUNC('?', eventTime), readOnly ORDER BY DATE_TRUNC('?', eventTime), readOnly",
      "QueryParameters": ["$Period$", "$StartTime$", "$EndTime$", "$Period$", "$Period$"]
    },
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "TopServices",
        "View": "BarChart",
        "LabelColumn": "service",
        "ValueColumn": "eventCount",
        "FilterColumn": "service",
        "Orientation": "Horizontal"
      },
      "QueryStatement": "SELECT REPLACE(eventSource, '.amazonaws.com') AS service, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY eventSource ORDER BY eventCount DESC LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    }
  ]
}
```

### Example


The following example creates the Highlights dashboard. The Highlights dashboard requires that you set and enable a refresh schedule for every 6 hours.



```
{
  "Name": "AWSCloudTrail-Highlights",
  "RefreshSchedule": {
    "Frequency": {
      "Unit": "HOURS",
      "Value": 6
    },
    "Status": "ENABLED"
  },
  "TerminationProtectionEnabled": true
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/CreateDashboard")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/CreateDashboard")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/CreateDashboard")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/CreateDashboard")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/CreateDashboard")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/CreateDashboard")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/CreateDashboard")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/CreateDashboard")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/CreateDashboard")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/CreateDashboard "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/CreateDashboard")
