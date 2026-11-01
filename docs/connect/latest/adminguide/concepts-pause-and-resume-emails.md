

# Pause and resume emails in Connect Customer
<a name="concepts-pause-and-resume-emails"></a>

Amazon Connect Customer lets agents pause emails while waiting for information or approvals, freeing them to handle higher-priority contacts and resume their work later. For example, an agent waiting for a supervisor to approve a refund can pause the email and take an incoming call. Paused time is tracked separately from active handling time, giving supervisors a more accurate view of the time agents spend working on emails.

Agents can pause and resume emails directly from the Agent workspace or Contact Control Panel (CCP) and see how long each email has been paused. Supervisors can monitor paused emails and pause duration in real time, and use flows to automatically resume or transfer emails that remain paused beyond a configured threshold.

**Topics**
+ [How agents pause and resume emails](#pause-emails-agent-experience)
+ [Resuming a paused email](#when-resume-emails)
+ [Programmatically pause and resume emails](#programmatically-pause-and-resume-emails)
+ [Configure a flow to pause and resume emails](#configure-flow-pause-resume-emails)
+ [Considerations](#pause-emails-considerations)

## How agents pause and resume emails
<a name="pause-emails-agent-experience"></a>

Agents pause and resume an email from their Contact Control Panel (CCP) or agent workspace. The following steps describe how an agent pauses an email and later resumes it.

To pause an email, the agent chooses the **Pause** button at the top of the email contact. The following image shows a connected email that has a draft reply in progress, with the **Pause** button at the top of the email contact.

![A connected email in the agent workspace, with the Pause button highlighted at the top of the email contact.](https://docs.aws.amazon.com/connect/latest/adminguide/images/PauseAnEmail.png)


When the agent pauses the email, the agent handling timer for that email stops. The message body and the reply composer are hidden behind a **Paused** banner, and **Send** is blocked until the agent resumes the email. Any draft reply that the agent started is preserved. To continue working on the email, the agent chooses **Resume**.

A pause indicator and the email subject remain visible in the contact list so that the agent can identify the paused email among their open contacts. The following image shows the contact list with two email contacts, where the paused email is marked **Paused**.

![The agent's contact list with two email contacts; the paused email is marked Paused in the list.](https://docs.aws.amazon.com/connect/latest/adminguide/images/ViewWhenMultipleEmailContacts.png)


## Resuming a paused email
<a name="when-resume-emails"></a>

A paused email can be resumed at any time by the agent who is handling it. There is no time limit for how long an email can remain paused.

To resume the email, the agent chooses the **Resume** button at the top of the paused email contact. When the agent resumes the email, the message body and the reply composer are restored, the draft reply that the agent started is preserved, and **Send** is enabled again so that the agent can continue the reply. The following image shows a paused email with the **Resume** button highlighted at the top of the email contact.

![A paused email in the agent workspace showing the 'This email has been paused' banner, with the Resume button highlighted at the top of the email contact.](https://docs.aws.amazon.com/connect/latest/adminguide/images/ResumeAnEmail.png)


## Programmatically pause and resume emails
<a name="programmatically-pause-and-resume-emails"></a>

You can pause and resume emails programmatically by using the [PauseContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_PauseContact.html) and [ResumeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_ResumeContact.html) APIs, which let you pause or resume a contact without agent interaction. To pause or resume an email, specify the contact ID of the inbound email contact. When you pause an inbound email that has an agent reply (a draft reply) in progress, Connect Customer also pauses the associated agent-reply contact, and resuming the inbound email resumes it as well. You can't pause or resume an agent-reply contact directly; pause and resume always operate on the inbound email contact.

When pausing and resuming an email, you can configure a corresponding flow to run at the pause and resume events. For more information, see [Flow block in Connect Customer: Resume contact](resume-contact.md).

## Configure a flow to pause and resume emails
<a name="configure-flow-pause-resume-emails"></a>

You can configure a flow to run automatically when an email contact is paused. In the flow designer, add a **Set event flow** block and choose the **Flow at contact pause** event hook to specify the flow that runs when an agent pauses an email. For example, you can use this flow to resume or transfer an email that has remained paused. For more information about the flow block used to resume a contact, see [Flow block in Connect Customer: Resume contact](resume-contact.md).

![The Set event flow block configuration with the event hook set to Flow at contact pause and a flow selected to run when an email contact is paused.](https://docs.aws.amazon.com/connect/latest/adminguide/images/FlowToTriggerWhenAnEmailContactIsPaused.png)


## Considerations
<a name="pause-emails-considerations"></a>
+ An agent can pause an email a maximum of 10 times. After an email reaches this limit, Connect Customer rejects additional pause requests for that email.
+ A paused email continues to count toward the active email contact limit for the instance, the same as an email that an agent is actively handling.
+ You pause and resume an email by using the contact ID of the inbound email contact. Pausing the inbound email also pauses its in-progress agent reply, and you can't pause or resume an agent-reply contact on its own.
+ Email pause and resume is available in supported AWS Regions. It is not available in the AWS GovCloud (US) Regions or the China Regions.