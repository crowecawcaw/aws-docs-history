

# Using Slack code channels

You can move an investigation into its own Slack code channel, where your team and AWS DevOps Agent work on that investigation together. Code channels are part of Slack Code, a Slack feature for working with agents in a dedicated channel. For more information about Slack Code and code channels, see [Slack Code](https://slack.com/features/code-channels) on the Slack website.

With a code channel for an investigation, you can do the following:
+ Follow the investigation's updates in a single channel, apart from your other alerts and conversations.
+ Bring together the people working on the investigation in one private channel.
+ Review the investigation's findings and mitigation plan on the channel's **Investigation** and **Mitigation plan** tabs, which AWS DevOps Agent keeps up to date.
+ Ask AWS DevOps Agent questions about the investigation, together with your team, without mentioning the app.
+ Keep using your associated Slack channel as before, with a thread for each investigation.

## Before you begin
<a name="before-you-begin"></a>

To open a code channel for an investigation, verify that you have the following:
+ A Slack channel association with **Bidirectional mode** turned on. For more information about setting up the association, see [Connecting Slack](connecting-to-ticketing-and-chat-connecting-slack.html).
+ The code channel permissions in your Slack workspace. If you connected your Slack workspace before code channels were available, update its permissions. For more information about updating permissions, see [Updating Slack permissions for an existing workspace](connecting-to-ticketing-and-chat-connecting-slack.html#updating-slack-permissions-for-an-existing-workspace).

## Opening a code channel for an investigation
<a name="opening-a-code-channel-for-an-investigation"></a>

When AWS DevOps Agent posts an investigation card to your associated channel, the card includes **Open in code channel**.

**To open a code channel for an investigation**

1. In Slack, open the associated channel, and find the investigation card from the AWS DevOps Agent app. The card shows the investigation title, its status, a summary of the investigation, a **View investigation** link, and **Open in code channel**.

1. On the card, choose **Open in code channel**.

AWS DevOps Agent creates a private code channel named after the investigation, and posts a link to it in the investigation card's thread. You and your teammates can join the code channel for that investigation.

The following image shows an investigation card in the associated channel `#ops-alerts`. The card is a message from the AWS DevOps Agent app. It shows the investigation title, its status and start time, and a summary of the `CheckoutServiceLambda` errors that the investigation is looking into. After the summary come a **View investigation** link and **Open in code channel**.

![Investigation card showing Open in code channel below the summary.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-cc-investigation-card.png)


## Working in the code channel
<a name="working-in-the-code-channel"></a>

After you open a code channel, the investigation's updates post to the code channel instead of the card's thread. The channel's **Investigation** tab collects the updates, newest first. When AWS DevOps Agent produces a mitigation plan, a **Mitigation plan** tab appears.

The **Investigation** tab opens in a panel beside the channel. At the top, the tab shows the investigation title, its status and start time, and a short summary of the incident, the cause, and the proposed mitigation. A **View investigation** link opens the investigation in the AWS DevOps Agent web app. After the summary, each update has a heading, such as a finding or a cause, followed by its details, newest first.

The following image shows a code channel for an investigation into `CheckoutServiceLambda` errors, with the **Investigation** tab open.

![The Investigation tab in a Slack code channel.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-cc-updates.png)


To ask AWS DevOps Agent about the investigation, write your message in the code channel. You don't need to mention the app. AWS DevOps Agent answers in the channel.

For example, Mary Major asks "how long has this been going on?" without mentioning the app. AWS DevOps Agent answers that the errors started at 1:15 PM, after a deployment that lowered the payments API timeout, and that about 4,200 checkout requests failed.

## Troubleshooting code channels
<a name="troubleshooting-code-channels"></a>

If an investigation card doesn't show **Open in code channel**, verify that the card's channel association has **Bidirectional** set to **Enabled**. Then verify that your Slack workspace has the code channel permissions. For instructions on adding the permissions, see [Updating Slack permissions for an existing workspace](connecting-to-ticketing-and-chat-connecting-slack.html#updating-slack-permissions-for-an-existing-workspace).

For other Slack problems, see [Troubleshooting Slack communication](connecting-to-ticketing-and-chat-connecting-slack.html#troubleshooting-slack-communication).