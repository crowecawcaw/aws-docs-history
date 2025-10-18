# PutDashboard

Creates a dashboard if it does not already exist, or updates an existing dashboard.
 If you update a dashboard, the entire contents are replaced with what you specify
 here.

All dashboards in your account are global, not region-specific.

A simple way to create a dashboard using `PutDashboard` is to copy an
 existing dashboard. To copy an existing dashboard using the console, you can load the
 dashboard and then use the View/edit source command in the Actions menu to display the
 JSON block for that dashboard. Another way to copy a dashboard is to use
 `GetDashboard`, and then use the data returned within
 `DashboardBody` as the template for the new dashboard when you call
 `PutDashboard`.

When you create a dashboard with `PutDashboard`, a good practice is to
 add a text widget at the top of the dashboard with a message that the dashboard was
 created by script and should not be changed in the console. This message could also
 point console users to the location of the `DashboardBody` script or the
 CloudFormation template used to create the dashboard.


## Request Parameters





**DashboardBody** 


The detailed information about the dashboard in JSON format, including the widgets
 to include and their location on the dashboard. This parameter is required.


For more information about the syntax, see [Dashboard Body Structure and Syntax](CloudWatch-Dashboard-Body-Structure.md "CloudWatch-Dashboard-Body-Structure.md").


Type: String


Required: Yes




**DashboardName** 


The name of the dashboard. If a dashboard with this name already exists, this call
 modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is
 created. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, "-", and
 "\_". This parameter is required.


Type: String


Required: Yes




## Response Elements


The following element is returned by the service.





**DashboardValidationMessages** 


If the input for `PutDashboard` was correct and the dashboard was
 successfully created or modified, this result is empty.


If this result includes only warning messages, then the input was valid enough for
 the dashboard to be created or modified, but some elements of the dashboard might not
 render.


If this result includes error messages, the input was not valid and the operation
 failed.


Type: Array of [DashboardValidationMessage](API_DashboardValidationMessage.md "API_DashboardValidationMessage.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ConflictException** 


This operation attempted to create a resource that already exists.


HTTP Status Code: 409




**InternalServiceError** 


Request processing has failed due to some unknown error, exception, or
 failure.





**Message** 





HTTP Status Code: 500




**InvalidParameterInput** 


Some part of the dashboard data is invalid.


HTTP Status Code: 400




## Examples


### Example


The following example creates a dashboard with just one text
 widget.



```
{
"DashboardName":"Dashboard with only one text widget",
"DashboardBody":{
   "widgets":[
      {
         "type":"text",
         "x":0,
         "y":7,
         "width":3,
         "height":3,
         "properties":{
            "markdown":"Hello world"
         }
      }
   ]
}
}
```

### Example


The following example modifies an existing dashboard to include one metric
 widget and one text widget.



```
{
    "DashboardName": "Two-Widget Dashboard",
    "DashboardBody": {
        "widgets": [
            {
                "type": "metric",
                "x": 0,
                "y": 0,
                "width": 12,
                "height": 6,
                "properties": {
                    "metrics": [
                        [
                            "AWS/EC2",
                            "CPUUtilization",
                            "InstanceId",
                            "i-012345"
                        ]
                    ],
                    "period": 300,
                    "stat": "Average",
                    "region": "us-east-1",
                    "title": "EC2 Instance CPU"
                }
            },
            {
                "type": "text",
                "x": 0,
                "y": 7,
                "width": 3,
                "height": 3,
                "properties": {
                    "markdown": "Hello world"
                }
            }
        ]
    }
}
```

### Example


The following example creates a dashboard with two metric widgets, side by
 side.



```
{
    "DashboardName": "Two-metric-widget Dashboard",
    "DashboardBody": {
        "widgets": [
            {
                "type": "metric",
                "x": 0,
                "y": 0,
                "width": 12,
                "height": 6,
                "properties": {
                    "metrics": [
                        [
                            "AWS/EC2",
                            "CPUUtilization",
                            "InstanceId",
                            "i-012345"
                        ]
                    ],
                    "period": 300,
                    "stat": "Average",
                    "region": "us-east-1",
                    "title": "EC2 Instance CPU"
                }
            },
            {
                "type": "metric",
                "x": 12,
                "y": 0,
                "width": 12,
                "height": 6,
                "properties": {
                    "metrics": [
                        [
                            "AWS/S3",
                            "BucketSizeBytes",
                            "BucketName",
                            "amzn-s3-demo-bucket"
                        ]
                    ],
                    "period": 86400,
                    "stat": "Maximum",
                    "region": "us-east-1",
                    "title": "amzn-s3-demo-bucket bytes"
                }
            }
        ]
    }
}
```

### Example


The following example creates a dashboard with one widget at the top that
 shows the `DiskReadBytes` metric for three EC2 instances on one
 graph, and a separate widget below that, with an alarm.



```
{
    "DashboardName": "Dashboard with a three-metric graph and an alarm",
    "DashboardBody": {
        "widgets": [
            {
                "type": "metric",
                "x": 0,
                "y": 0,
                "width": 12,
                "height": 6,
                "properties": {
                    "metrics": [
                        [
                            "AWS/EC2",
                            "DiskReadBytes",
                            "InstanceId",
                            "i-xyz"
                        ],
                        [
                            ".",
                            ".",
                            ".",
                            "i-abc"
                        ],
                        [
                            ".",
                            ".",
                            ".",
                            "i-123"
                        ]
                    ],
                    "period": 300,
                    "stat": "Average",
                    "region": "us-east-1",
                    "title": "EC2 Instance CPU"
                }
            },
            {
                "type": "metric",
                "x": 0,
                "y": 7,
                "width": 12,
                "height": 12,
                "properties": {
                    "annotations": {
                        "alarms": [
                            "arn:aws:cloudwatch:us-east-1:123456789012:alarm:myalarm"
                        ]
                    },
                    "period": 60,
                    "title": "MyAlarm"
                }
            }
        ]
    }
}
```

### Example


The following example creates a dashboard with one metric widget and one
 metric math widget.



```
{
   "DashboardName":" One metric math widget and One metric widget",
   "DashboardBody":{
      "widgets":[
         {
            "type":"metric",
            "x":0,
            "y":0,
            "width":6,
            "height":6,
            "properties":{
               "metrics":[
                  [
                     "AWS/EC2",
                     "CPUUtilization",
                     "InstanceId",
                     "i-012345"
                  ]
               ],
               "region":"us-east-1",
               "stat":"Average",
               "period":300,
               "title":"EC2 Instance CPU"
            }
         },
         {
            "type":"metric",
            "x":6,
            "y":0,
            "width":6,
            "height":6,
            "properties":{
               "metrics":[
                  [
                     {
                        "expression":"SUM(METRICS())",
                        "label":"Expression1",
                        "id":"e1",
                        "visible":true
                     }
                  ],
                  [
                     "AWS/EC2",
                     "CPUUtilization",
                     "InstanceId",
                     "i-xyz",
                     {
                        "id":"m1",
                        "visible":true
                     }
                  ],
                  [
                     "...",
                     "i-abc",
                     {
                        "id":"m2",
                        "visible":true
                     }
                  ],
                  [
                     "...",
                     "i-123",
                     {
                        "id":"m3",
                        "visible":true
                     }
                  ],
                  [
                     "...",
                     "i-456",
                     {
                        "id":"m4",
                        "visible":true
                     }
                  ]
               ],
               "region":"us-east-1",
               "stat":"Average",
               "period":300,
               "title":"Sum of CPUUtilization of four Instances"
            }
         }
      ]
   }
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutDashboard")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutDashboard")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutDashboard")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutDashboard")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutDashboard")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutDashboard")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutDashboard")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutDashboard")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutDashboard")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutDashboard "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutDashboard")
