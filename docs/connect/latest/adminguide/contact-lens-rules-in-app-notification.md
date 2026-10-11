

# Create rules that send in-app notifications
<a name="contact-lens-rules-in-app-notification"></a>

You can create rules to automatically notify people in your organization through in-app notifications within Connect Customer's admin and agent workspaces. Example use cases include:
+ Notifying an agent when they receive a performance evaluation.
+ Notifying a supervisor when an SLA is breached on a case.
+ Notifying the agent handling a case when the case is updated.
+ Notifying a centralized compliance team when an agent exhibits non-compliant behaviors on a contact.
+ Notifying agents or supervisors on updates to agent schedules or time-off requests.

In-app notifications are also available as a standalone Connect Customer API, for use cases unrelated to rules, such as system notifications or custom messages sent directly from your own applications. For more information about how recipients see and interact with in-app notifications, and how to create them outside of rules, see [Notifications in the workspace header](amazon-connect-notifications.md).

**To create a rule that sends an in-app notification**

1. Log in to Connect Customer with a user account that has the [required permissions](permissions-for-rules.md) to create rules.

1. Navigate to **Analytics and optimization**, **Rules**.

1. On the **Rules** page, choose **Create a rule**, and then from the dropdown list, choose the rule type for the trigger you want. **Send in-app notification** is available for conversational analytics, evaluation forms, cases, cases SLA breach, and scheduling rule types.  
![The Rules page, with the Create a rule dropdown list open and Cases highlighted among the available rule types.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-in-app-notification-create-rule.png)

1. On the **New rule** page, define the conditions for the rule.

1. When you define actions for the rule, choose **Send in-app notification** for the action.  
![The Define actions step, the Add action dropdown list, with an arrow pointing to the Send in-app notification action.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-in-app-notification-action.png)

1. In the **Send in-app notification** section, under **To**, choose who is going to receive the notification by using one of these options: 
   + **Select recipients by login, first, or last name**: Routes the notification to the agents you select.
   + **Select recipients by tags**: Routes the notification dynamically based on the agent's tag values.
   + **Select the agent who handled the contact** (or the case-assignment equivalent): Routes the notification to the agent associated with the contact or case. This option is available only for supported trigger types.
   + **Select supervisors of the agents impacted by the scheduling change**: Routes the notification to the supervisors of every agent affected by the change. This option is available only for scheduling rules.

1. Under **Content**, add the notification message: 
   + Choose a **Locale** for each message. Choose **Add language** to add a message in another locale; each locale can be used only once per notification. Add a message for every locale your recipients use, so that each person sees the notification in their own console locale.
   + In **Message**, enter the notification text. Use **@ to add dynamic variables** that are populated when the rule runs, the same way you would for an email notification's variables.

1. Under **Priority**, choose **High** or **Low**. High priority notifications are displayed above low priority notifications in the recipient's notification panel, and are shown with increased visual emphasis. Reserve **High** for messages that need immediate attention, such as an SLA breach or a critical system event—using it for routine updates reduces its effectiveness over time.

   The following image shows the **Send in-app notification** section with recipients, content, and priority defined.  
![The Send in-app notification section, showing the To, Content, and Priority fields with a sample message and a Low priority selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-in-app-notification-panel.png)

1. Choose **Next**. Review your selections, and then choose **Save**.  
![The Review and save page, showing the When, If, and Then summary for a rule with the Assign Contact Category and Send in-app notification actions, and the Save as draft and Save and publish buttons.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-in-app-notification-review.png)

1. After you add rules, they are applied to new contacts that occur after the rule was added. Rules are applied when Connect Customer conversational analytics analyzes conversations.

   You cannot apply rules to past, stored conversations. 

## Inserting variables and links in notification content
<a name="in-app-notification-insert-variables-links"></a>

The **Message** field in the **Content** section supports dynamic variables and clickable links, so recipients can jump straight to the relevant contact, case, or evaluation.
+ Type `@` in the message, or choose **Insert variable** on the toolbar, to open the list of variables available for the rule's trigger type (for example, **Agent ID**, **Agent name**, **Contact ID**, **Instance URL**, **Queue ID**, **Queue name**, and **Rule name**). Choose a variable to insert it at the cursor position.  
![The Message field with the Insert variable list open, showing the available variables including Agent ID, Agent name, Contact ID, Instance URL, Queue ID, Queue name, and Rule name.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-in-app-notification-insert-variable.png)
+ To edit or add a clickable hyperlink, select the text you want to turn into a link, and then choose the link icon on the toolbar. Enter or insert variables for the link text and the URL (for example, combine the **Instance URL** and **Contact ID** variables to link directly to a contact's details page), and then choose **Edit**, **Copy**, or **Unlink** to manage the link.  
![The Message field with the link insertion popup open, showing a link built from the Instance URL and Contact ID variables, and the Edit, Copy, and Unlink options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-in-app-notification-insert-link.png)

## In-app notification limits
<a name="in-app-notification-limits"></a>
+ The notification message is limited to 500 visible characters per locale, after variable values are resolved. Markdown link URLs don't count against this limit.
+ You can add one message per supported locale per notification.
+ Notifications have a default visibility period of one week. After that, they're automatically removed for the recipient.
+ **Select the agent who handled the contact** (or the case-assignment equivalent) is available only for the trigger types that support it.
+ **Select supervisors of the agents impacted by the scheduling change** is available only for scheduling rules.