

# How agents view their schedule in the Connect Customer agent workspace
<a name="scheduling-view-schedule-agents"></a>

There are two ways agents can access their schedules:
+ If your organization uses the Connect Customer agent workspace, agents access their schedule by entering **https://{{instance name}}/connect/agent-app-v2/** into their browser and then choosing the calendar icon.
+ If your organization uses the Salesforce CTI, or a custom-built agent desktop, agents access their schedule by entering **https://{{instance name}}/connect/agent-app-v2/scheduling** into their browser, logging into Connect Customer, and then choosing the calendar icon.

Following are steps agents use to view their schedule in the agent application.

1. Log on to the agent workspace using the URL that your admin gives you. 

1. Choose the **Calendar** icon on the application navigation bar to launch the staff schedule manager viewer, shown in the following image. Otherwise, the staff schedule manager viewer launches automatically.  
![The agent workspace, the Calendar icon.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-scheduling-calendaricon.png)

   The following image shows a sample schedule in the agent workspace.  
![A sample schedule in the agent workspace.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-scheduling-agent-view.png)

The Agent Calendar displays times according to the following prioritized timezone logic:
+ Agent-specific timezone — If the administrator has explicitly configured a timezone in the agent's staff rules or profile settings, this timezone is used.
+ Fallback: Agent's local device timezone — If no agent-specific timezone has been configured, the calendar uses the timezone detected from the agent's computer or browser settings.