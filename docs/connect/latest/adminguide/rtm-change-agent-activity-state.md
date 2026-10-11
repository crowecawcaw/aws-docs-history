

# Change the "Agent activity" status in a metrics report in the Contact Control Panel (CCP)
<a name="rtm-change-agent-activity-state"></a>

Agents manually set their status in the Contact Control Panel (CCP). However, on the real-time metrics report and analytics dashboard, managers can manually change the **Agent Activity** status of an agent. This overrides what the agent has set in the CCP.

 The value that's displayed in the **Agent Activity** column can be either: 
+ The agent's availability status, such as **Offline**, **Available**, or **Break**.
+ The contact state, such as **Incoming** or **On contact**.

When you choose the **Agent Activity** column, you can select and change an agent's *availability status*, such as **Offline**, **Available**, or **Break**. The following image shows an example where the **Available** and **Offline** statuses, along with some custom statuses, are in the dropdown list of the **Activity** column. After the new status is selected, it will be reflected within the **Activity** column itself after the update has finished.

![The dropdown list of availability statuses for the Agent activity column.](https://docs.aws.amazon.com/connect/latest/adminguide/images/rtm-change-agent-activity-state.png)


This change also appears in the agent event stream.

When a *contact state* is displayed in the **Agent Activity** column, such as **Incoming** or **On contact**, you can change it to any other availability status and this will be displayed in the **Next activity** column after the update has finished.

![The dropdown list of availability statuses when an agent is on contact.](https://docs.aws.amazon.com/connect/latest/adminguide/images/rtm-change-agent-activity-state-incoming.png)


![The Next activity column update after another activity was selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/rtm-change-agent-activity-state-next-activity.png)


When a manager changes an agent's activity status from **Missed** contact state to an availability status in the analytics pages, the system behavior differs for single or multiple contact states:
+ **Single-contact state scenario:** If the agent has only **Missed** contact states across all channels, the system clears the **Missed** status and immediately applies the new availability status.
+ **Multi-contact state scenario:** If the agent is currently **On Contact/Incoming** on any channel while having **Missed** contacts on other channels, the system populates the **Next activity** column when the manager selects any status except **Available**.

**Note**  
The real-time metrics report and analytics dashboards do not display who changed the agent's status. You can find this information in AWS CloudTrail by looking at the `PutUserStatus` API events. For more information, see [Find who changed an agent's activity status](#rtm-change-agent-activity-state-find-who).

## Required permissions to change an agent's activity status
<a name="rtm-change-agent-activity-state-permissions"></a>

For someone such as a manager to be able to change an agent's activity status on the analytics pages, they need to be assigned a security profile that has the following permission: 
+ View - Agent Status

The **Agent status - View** permission is shown in the following image of the **Users and permissions** section of the security profile page.

![The Agent status - View permission.](https://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_agent_status_view.png)


## Find who changed an agent's activity status
<a name="rtm-change-agent-activity-state-find-who"></a>

A manager can change an agent's status on the real-time metrics page and analytics dashboards. When this happens, Connect Customer calls the `PutUserStatus` API on the manager's behalf by using the service-linked role. CloudTrail records this API call, so you can identify who made the change. For more information about how Connect Customer works with CloudTrail, see [Log Connect Customer API calls with AWS CloudTrail](logging-using-cloudtrail.md).

1. Open the CloudTrail console in the same AWS Region as your Connect Customer instance, and then choose **Event history**.

1. For **Lookup attributes**, choose **Event name**, and then enter `PutUserStatus`. The event source is `connect.amazonaws.com`.

1. Choose the event to open its record, and then review the following fields.

`requestParameters.UserId`  
The user ID of the agent whose status was changed.

`requestParameters.AgentStatusId`  
The ID of the new agent status.

`userIdentity.arn`  
An Amazon Resource Name (ARN) of the form `arn:aws:sts::{{account-id}}:assumed-role/AWSServiceRoleForAmazonConnect_{{suffix}}/{{session-name}}`. The session name (which is also the portion after the colon in `userIdentity.principalId`) is the user ID of the manager who made the change.

`eventTime`  
The date and time when the status was changed.

To map these IDs to names, use the following:
+ For the user IDs of the agent and the manager, use the [DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) API, or find the user on the **Users** page in the Connect Customer admin website.
+ For the agent status ID, use the [DescribeAgentStatus](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeAgentStatus.html) API.