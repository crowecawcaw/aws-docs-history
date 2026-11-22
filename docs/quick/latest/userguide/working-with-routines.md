

# Routines

Routines run your agents and assets automatically, so work happens without you starting it by hand. There are three types of routine, each defined by what starts a run. A schedule runs at recurring times. An inbound email routine runs when an email arrives at a designated address. A Quick event routine runs when a specific event occurs in Quick, such as a file upload. For each routine, you define what runs, what starts it, the capabilities it can use, and how it responds.

Routines run in the cloud, so they run at their configured time even when your computer is off. The exception is a run that needs a local tool, such as reading a file on your machine, browser automation, or local code execution. For those steps, your computer must be on with the desktop app running and connected. Otherwise, Quick skips the run, and the run shows as skipped in [Monitor and manage agents and flows with Mission Control](mission-control.md). A routine can use only the capabilities listed in its **Uses** field, and your administrator's, connector owner's, and your own access controls still apply. When a run reaches an action that requires your approval, the run waits until you approve or deny the action.

## Schedules
<a name="routines-schedules"></a>

A schedule runs an agent or a published flow automatically at times you set, such as every weekday morning, every 30 minutes, or once next Friday. Quick posts each run's result to your **Feed** or sends it to a connected app such as Slack or email.

**To create a schedule from chat**

1. In Quick, open **Chat**.

1. In the chat box, describe what you want the schedule to do. Include the following details.
   + When it runs, for example "every morning at 8", "weekdays at 5 PM", "every 30 minutes", or "once, tomorrow at 9 AM". Quick uses the time zone in your Settings unless you name another.
   + What to do each time.
   + Where the result goes, such as your **Feed**, a Slack channel, or email. The default is your **Feed**.
   + Optionally, which agent runs it. The default is the agent you are chatting with. To use another agent, name it or @mention it. The agent must be published.
   + Optionally, a flow to run. Name the published flow and its inputs.
   + Optionally, when to skip a run, so it runs only when something is new.

1. Answer any follow-up questions that Quick asks.

1. Check the confirmation message to verify the schedule.

1. Optionally, ask Quick to run a test. A test is a full run that can take a few minutes and carries out allowed actions.

The following are example prompts for a schedule.
+ "Every weekday at 8 AM, summarize my unread Slack messages, new email, and today's calendar, and post it to my Feed."
+ "Every 30 minutes, check my inbox for new email and flag anything urgent. Only run when there's new email."
+ "Every day at 5 PM, check \#project-atlas for updates and email me a summary."
+ "Every Monday at 9 AM, search the web for news about Example Corp and write a short report."
+ "Remind me tomorrow at 3 PM to send the quarterly numbers to finance."

### Run settings
<a name="w2aac49b7c11"></a>

The run settings control how the agent carries out each run. You can configure the following settings:
+ Mode – Choose Fast, Balanced, or Smart.
+ Thinking effort – Have the agent apply additional reasoning before responding.
+ Memory – Allow the agent to use profile and search tools.
+ Sub-tasks – Let the agent break work into parallel sub-tasks.

### Managing schedules
<a name="w2aac49b7c13"></a>

To manage your schedules, you can ask Quick in chat, for example "change my morning brief to 7:30", "turn off the inbox triage schedule", or "show me my schedules". You can also open **Routines** to view and edit them. Built-in routines include the feed agent that populates your proactive feed. For more information, see [Stay on top of your work with your proactive feed](working-with-feed.md).

### Notes
<a name="w2aac49b7c15"></a>

Runs in the cloud  
Schedules run in the cloud, so they run at their configured time even when your computer is off. Steps that need a local tool require the desktop app running and connected.

Published versions  
A schedule runs the published version of an agent or flow.

How often  
A schedule can run as often as every 15 minutes. You can schedule it for certain days of the week, but not a specific day of the month.

Actions need limits  
When a run reaches an action that requires approval, it waits until you approve or deny it. Set limits on the actions a routine can take.

## Inbound email
<a name="routines-inbound-email"></a>

An inbound email routine runs your agent or flow when an email is sent to a designated trigger address. You can use dynamic variables from the email to populate input values.

You create an inbound email routine from **Routines**.

**To create an inbound email routine**

1. Open **Routines**.

1. Choose **Create**.

1. Describe what you want the routine to do. Include the following details.
   + The address you want.
   + What to do with each email.
   + Where the result goes.
   + Optionally, who can send to the address. The default is only you. To let anyone at your company send to it, allow your email domain, for example @example.com.
   + Optionally, which emails count.
   + Optionally, a flow to run.

1. Answer any follow-up questions that Quick asks.

1. Check the confirmation message. The address has the format `alias@region.mail.quick.aws.com`.

1. Send or forward emails to that address.

The following are example prompts for an inbound email routine.
+ "When an email arrives at my support address, summarize it and post the summary to my Feed."
+ "When an email arrives, create a task from it and reply to the sender with a confirmation."

### Use details from the email
<a name="w2aac49b9c13"></a>

To use a detail from the email, describe the part you want. The following dynamic variables are available.


| Variable | Description | 
| --- | --- | 
| @From | The sender's email address. | 
| @Subject | The subject line of the email. | 
| @To | The recipient address. | 
| @Body | The body text of the email. | 
| @Attachments | The files attached to the email. | 

### Notes
<a name="w2aac49b9c15"></a>

Unique addresses  
Each inbound email routine has its own unique trigger address.

Specific senders  
You can limit the routine to specific senders, or let anyone at your company send to the address.

Forwarded email  
You can forward email to the trigger address to start a run.

Manage routines  
To view and edit your inbound email routines, open **Routines**.

## Quick events
<a name="routines-quick-events"></a>

A Quick event routine runs an agent or a published flow when something happens in Quick. Quick supports the following events.


| Event | Filter | 
| --- | --- | 
| File uploaded to a space | Filter by file name, type, or size. | 
| Flow execution completed | Filter by how the flow was run: manually, by a routine, or either. | 

**To create a Quick event routine**

1. In Quick, open **Chat**.

1. Describe what you want the routine to do. Include the following details.
   + The event to watch.
   + What to do.
   + Where the result goes.
   + Optionally, which events count.
   + Optionally, a flow to run, which enables flow chaining.

1. Answer any follow-up questions that Quick asks.

1. Check the confirmation message to verify the routine.

The following are example prompts for a Quick event routine.
+ "When a file is uploaded to the Example Corp space, extract the key points and post them to my Feed."
+ "When a flow execution completes, email me the output as a PDF."

### Use details from the event
<a name="w2aac49c11c13"></a>

To use a detail from the event, describe the part you want. The variables available depend on the event.

For a File uploaded to a space event, the following variables are available.


| Variable | Description | 
| --- | --- | 
| @File | The uploaded file. | 
| @FileName | The name of the file. | 
| @Extension | The file type, such as PDF, DOCX, XLSX, or CSV. | 
| @SizeInMb | The size of the file in megabytes. | 

For a Flow execution completed event, the following variables are available.


| Variable | Description | 
| --- | --- | 
| @FlowName | The name of the flow. | 
| @RunType | How the flow was run, either triggered or manual. | 
| @OutputPDF | The flow output as a PDF. | 

### Notes
<a name="w2aac49c11c15"></a>

Published flows only  
A Quick event routine can run a published flow only.

Access  
A routine runs within your access, and your administrator's, connector owner's, and your own access controls still apply.

Runs in the cloud  
Quick event routines run in the cloud. Steps that need a local tool require the desktop app running and connected.

Manage routines  
To view and edit your Quick event routines, open **Routines**.