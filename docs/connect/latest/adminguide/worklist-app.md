

# Access the Worklist app in the agent workspace
<a name="worklist-app"></a>

The Worklist app enables agents with the required permissions and routing profile settings to manually prioritize and assign queued work to themselves. The following steps explain how to provide your agents access to the Worklist app in the agent workspace.

**Note**  
An agent can access the Worklist app in the agent workspace only if they have a security profile with the permissions described in the following steps.

1. Update your agents' security profiles by choosing one of these permissions:
   + **Allow 'Assign to me' for any contact**: Agents can view contacts under any of these conditions:
     + The current agent is the only preferred agent on the contact.
     + The current agent is one of the preferred agents on the contact.
     + Any agent or set of agents are preferred agents on the contact.
     + The contact has no preferred agents.
   + **Allow 'Assign to me' for my contact**: Agents can view contacts under these conditions:
     + The current agent is the only preferred agent on the contact.
     + The current agent is one of the preferred agents on the contact.  
![Contact actions for the Worklist app.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-app-1.png)

   After you assign these permissions, they appear on the **Security profiles** page.  
![Security profile permissions for the Worklist app.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-security-profile.png)  
![Security profile with permissions to access the Worklist app.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-security-profile-2.png)

1. Update the routing profile settings to specify the queues and channels available for manual assignment.  
![Routing profile settings for the Worklist app.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-routing-profile.png)

1. After you update the security profile and routing profile settings, the agent sees the Worklist app in the agent workspace.  
![Worklist app in the agent workspace.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-workspace-view.png)

## Available filter options
<a name="worklist-filter-options"></a>

The filter options depend on the agent's permissions:
+ An agent with **Allow 'Assign to me' for any contact** can view these filter options:  
![Filter options for agents with Assign to me for any contact permission.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-filter-any-contact.png)
+ An agent with **Allow 'Assign to me' for my contact** can view these filter options:  
![Filter options for agents with Assign to me for my contact permission.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-filter-my-contact.png)

## Time range filter for contact history
<a name="worklist-time-range-filter"></a>

By default, the Worklist app shows contacts created in the last 2 weeks. To see older contacts, use the **Time range** filter to choose a date range. You can choose any date range within the past 90 days.

![The Worklist app showing the Time range filter for choosing contact history date ranges.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-time-range-filter.png)
