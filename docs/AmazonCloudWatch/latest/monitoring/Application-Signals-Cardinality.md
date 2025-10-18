# Manage high-cardinality operations

Application Signals includes settings in the CloudWatch agent that you can use to manage the cardinality of your 
 operations and manage the metric exportation to optimize costs. By default, the metric limiting function becomes active 
 when the number of distinct operations for a service over time exceeds the default threshold of 500. 
 You can tune the behavior by adjusting the configuration settings. 
 


## Determine if metric limiting is activated


You can use the following methods to find if the default metric limiting is happening. If it is, 
 you should consider optimizing the cardinality control by following the steps in the next section.



* In the CloudWatch console, choose **Application Signals**, **Services**. If you see 
 an **Operation** named **AllOtherOperations** or 
 a **RemoteOperation** named **AllOtherRemoteOperations**, then metric limiting is happening.
* If any metrics collected by Application Signals have the value `AllOtherOperations` for their `Operation` 
 dimension, then metric limiting is happening.
* If any metrics collected by Application Signals have the value `AllOtherRemoteOperations` for their `RemoteOperation` 
 dimension, then metric limiting is happening.

### Optimize cardinality control


To optimize your cardinality control, you can do the following:



* Create custom rules to aggregate operations.
* Configure your metric limiting policy.

#### Create custom rules to aggregate operations


High-cardinality operations can sometimes be caused by inappropriate unique values extracted from the context. 
 For example, sending out HTTP/S requests that include user IDs or session IDs in the path can lead to hundreds of disparate 
 operations. To resolve such issues, we recommend that you configure the CloudWatch agent with customization rules to 
 rewrite these operations.


In cases where there is a surge in generating numerous different metrics through individual `RemoteOperation` calls, 
 such as `PUT /api/customer/owners/123`, `PUT /api/customer/owners/456`, and similar requests, we
 recommend that you consolidate these operations into a single `RemoteOperation`. One approach is
 to standardize all `RemoteOperation` calls that start with `PUT /api/customer/owners/` to a uniform format, 
 specifically `PUT /api/customer/owners/{ownerId}`. The following example illustrates this. For information about other customization rules, 
 see [Enable CloudWatch Application Signals](CloudWatch-Agent-Application_Signals.md "CloudWatch-Agent-Application_Signals.md").



```
{
   "logs":{
      "metrics_collected":{
         "application_signals":{
            "rules":[
               {
                  "selectors":[
                     {
                        "dimension":"RemoteOperation",
                        "match":"PUT /api/customer/owners/*"
                     }
                  ],
                  "replacements":[
                     {
                        "target_dimension":"RemoteOperation",
                        "value":"PUT /api/customer/owners/{ownerId}"
                     }
                  ],
                  "action":"replace"
               }
            ]
         }
      }
   }
}
```

In other cases, high-cardinality metrics might have been aggregated to `AllOtherRemoteOperations`, and 
 it might be unclear what specific metrics are included. The CloudWatch agent is able to log the dropped operations. 
 To identify dropped operations, use the configuration in the following example to activate logging until the problem resurfaces. 
 Then inspect the CloudWatch agent logs (accessible by container `stdout` or EC2 log files) and search for the keyword `drop metric data`.



```
{
  "agent": {
    "config": {
      "agent": {
        "debug": true
      },
      "traces": {
        "traces_collected": {
          "application_signals": {
          }
        }
      },
      "logs": {
        "metrics_collected": {
          "application_signals": {
            "limiter": {
              "log_dropped_metrics": true
            }
          }
        }
      }
    }
  }
}
```

#### Create your metric limiting policy


If the default metric limiting configuration doesn’t address the cardinality for your service, you can 
 customize the metric limiter configuration. To do this, add a `limiter` section under 
 the `logs/metrics_collected/application_signals` section in the CloudWatch Agent configuration file.


The following example lowers the threshold of metric limiting from 500 distinct metrics to 100.



```
{
  "logs": {
    "metrics_collected": {
      "application_signals": {
        "limiter": {
          "drop_threshold": 100
        }
      }
    }
  }
}
```
