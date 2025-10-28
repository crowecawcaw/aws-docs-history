# Patch notifications

###### Important

Beginning February 1, 2025, AMS customers will no longer receive notifications for empty Patch Maintenance Windows in their managed accounts.

The subscribed email addresses (up to five) receive an email similar to the following just before the patch maintenance window start:

```
Dear Customer,
The AMS Patch Maintenance Window `THE_MAINTENANCE_WINDOW_NAME` was started at: 2020-02-21T12:02:18.196Z.
Details:
    Maintenance Window AccountId:   `YOUR_ACCOUNT_ID`
    Maintenance Window Region:      `YOUR_ACCOUNT_REGION`
    Maintenance Window Id:          `THE_MAINTENANCE_WINDOW_ID`
    Maintenance Window Name:        `THE_MAINTENANCE_WINDOW_NAME`
    Maintenance Window Description: MaintenanceWindow for patching patch Group `PATCH_GROUP_NAME`
    Maintenance Window Patch Group: `PATCH_GROUP_NAME`
    Maintenance Window ExecutionId: `THE_EXECUTION_ID`
Targets:
    InstanceId           InstanceName        StackId
    -------------------  --------------      -----------------------
    `THE_INSTANCE_ID`      `THE_INSTANCE_NAME`   `THE_STACK_NAME`

A follow-up message with a detailed report is sent as soon as the maintenance window is over.

Please raise a service request if you have any inquires about AMS Patch Orchestrator by following this URL:
https://console.aws.amazon.com/managedservices/servicerequest/new

Kind Regards,

Amazon Web Services
Amazon Managed Services
Patch Team
```

At the end of the patch activity, the subscribed email addresses receive an email similar to the following:

```
Dear Customer,
The AMS Patch Maintenance Window `THE_MAINTENANCE_WINDOW_NAME` ended at: 2020-02-21T12:03:20.058Z, with status: SUCCESS.
Details:
    Maintenance Window AccountId:   `YOUR_ACCOUNT_ID`
    Maintenance Window Region:      `YOUR_ACCOUNT_REGION`
    Maintenance Window Id:          `THE_MAINTENANCE_WINDOW_ID`
    Maintenance Window Name:        `THE_MAINTENANCE_WINDOW_NAME`
    Maintenance Window Description: MaintenanceWindow for patching patch Group `PATCH_GROUP_NAME`
    Maintenance Window Patch Group: `PATCH_GROUP_NAME`
    Maintenance Window ExecutionId: `THE_EXECUTION_ID`
Targets:
    RfcId                        InstanceId        InstanceName          StackId              Status
    -----------------------  -------------------  --------------    -----------------------  --------
    `THE_RFC_ID`        `THE_INSTANCE_ID`     `THE_INSTANCE_NAME THE_STACK_NAME`           `STATUS`

You can view the current Patch Compliance of your Amazon EC2 Instances by following this URL:
https://console.aws.amazon.com/systems-manager/compliance?region=YOUR_ACCOUNT_REGION

Please raise an Incident if an issue is impacting one of your production applications by following this URL:
https://console.aws.amazon.com/managedservices/incident/new

Kind Regards,

Amazon Web Services
Amazon Managed Services
Patch Team
```

Every 96 hours AMS patching system identifies all upcoming patch managed maintenance windows within that 96 hours and sends
a reminder notification to all subscribed email addresses that fall within that 96 hour window. This could be as little as one hours
before the window, or the full 96 hours. For example:

```
Dear Customer,
The AMS Patch Maintenance Window `THE_MAINTENANCE_WINDOW_NAME` will start at: 2020-05-06T16:35:36.523Z.
Details:
    Maintenance Window AccountId:   `YOUR_ACCOUNT_ID`
    Maintenance Window Region:      `YOUR_ACCOUNT_REGION`
    Maintenance Window Id:          `THE_MAINTENANCE_WINDOW_ID`
    Maintenance Window Name:        `THE_MAINTENANCE_WINDOW_NAME`
    Maintenance Window Description: MaintenanceWindow for patching patch Group `PATCH_GROUP_NAME`
    Maintenance Window Patch Group: `PATCH_GROUP_NAME`
    Maintenance Window Next Start Time: 2020-05-06T16:35:36.523Z
    Maintenance Window Schedule:        rate(24 hours)
    Maintenance Window Timezone:        `THE_TIMEZONE`
At this time, these are the instances in the "`PATCH_GROUP_NAME`" Patch Group:
    InstanceId           InstanceName    StackId                  InstanceState

-------------------------------------------------------------------------------------------------

    `THE_INSTANCE_ID`      `THE_INSTANCE_NAME`   `THE_STACK_NAME`  running/stopped
    `THE_INSTANCE_ID`      `THE_INSTANCE_NAME`   `THE_STACK_NAME`  running/stopped
    `THE_INSTANCE_ID`      `THE_INSTANCE_NAME`   `THE_STACK_NAME`  running/stopped

A notification message is sent as soon as the maintenance window starts.

You can view the current Patch Compliance of your Amazon EC2 Instances by following this URL:
https://console.aws.amazon.com/systems-manager/compliance?region=YOUR_ACCOUNT_REGION

If you would like to disable this maintenance window or you have inquires about the AMS Patch Orchestrator click on the following URL:
https://console.aws.amazon.com/managedservices/servicerequest/new

If you would like to delete this maintenance window, you can run the CT with id "ct-0q0bic0ywqk6c" against the stack id "stack-rctyznutkyj4tkkzq".

Kind Regards,

Amazon Web Services
Amazon Managed Services
Patch Team
```
