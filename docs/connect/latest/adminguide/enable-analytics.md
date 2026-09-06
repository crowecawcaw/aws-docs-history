

# Enable conversational analytics in Connect Customer conversational analytics
<a name="enable-analytics"></a>

You can enable conversational analytics in a few steps:

1. Enable conversational analytics on your Connect Customer instance.

1. Add a [Set recording and analytics behavior](set-recording-behavior.md) block to a flow, and configure it to enable conversational analytics for voice, chat, email, or a combination of channels.

The following image shows a block that's configured for call recording and speech analytics. The **Call recording** option is set to **Agent and customer**. In the **Analytics** section, the options are selected for automated interactions and agent interactions.

![The properties page for a set recording and analytics behavior block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-recording-and-analytics-behavior.png)


The procedures in this topic describe the steps to enable conversational analytics for calls, chats, or emails.

**Note**  
For new flows, the [Set recording, analytics and processing behavior](set-recording-analytics-processing-behavior.md) block replaces the [Set recording and analytics behavior](set-recording-behavior.md) block. The new block reorganizes the analytics options. The following procedures and images describe the earlier block, which remains supported in existing flows. The steps to enable conversational analytics are equivalent in both blocks.

**Topics**
+ [Important things to know](#important-set-behaviorblock)
+ [Enable conversational analytics for your Connect Customer instance](#enable-cl)
+ [Enable call recording and speech analytics](#enable-callrecording-speechanalytics)
+ [Enable chat analytics](#enable-chatanalytics)
+ [Enable email analytics](#enable-emailanalytics)
+ [Enable redaction](#enable-redaction)
+ [Review redaction for accuracy](#review-sensitive-data-redaction)
+ [Disable sentiment analysis](#disable-sentiment-analysis-voice-and-chat)
+ [Dynamically enable redaction based on the customer's language](#dynamically-enable-analytics-contact-flow)
+ [Design a flow for key highlights](#call-summarization-agent)
+ [What if the flow block fails to enable conversational analytics?](#troubleshoot-contactlens-enablement)
+ [Multi-party calls](#multiparty-calls-contactlens)

## Important things to know
<a name="important-set-behaviorblock"></a>
+ **Collect data after transferring a contact**: If you want to continue using conversational analytics to collect data after transferring a contact to another agent or queue, you need to add another [Set recording and analytics behavior](set-recording-behavior.md) block with **Enable analytics** enabled for the flow. This is because a transfer generates a second contact ID and contact record. Conversational analytics needs to run on that contact record as well.
**Note**  
For [queue-to-queue transfers](queue-to-queue-transfer.md) the configuration information for conversational analytics is copied to the transferred contact.
+ When you choose a language that is supported by sentiment analysis, AND select **Enable conversational analytics speech analytics**, **Enable chat analytics**, or **Enable email analytics** in the [Set recording and analytics behavior](set-recording-behavior.md) block, sentiment analysis is enabled by default. You can choose to [disable sentiment analysis](#disable-sentiment-analysis-voice-and-chat). 
+ Where you place the [Set recording and analytics behavior](set-recording-behavior.md) block in a flow affects the agent's experience with key highlights. For more information, see [Design a flow for key highlights](#call-summarization-agent).

## Enable conversational analytics for your Connect Customer instance
<a name="enable-cl"></a>

Before you can enable conversational analytics, you first need to enable conversational analytics for your instance. 

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance alias. The instance alias is also your **instance name**, which appears in your Connect Customer URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box around the instance alias.  
![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. In the Connect Customer console, in the navigation pane, choose **Analytics tools**, and then choose **Enable conversational analytics**.

1. Choose **Save**.

## Enable call recording and speech analytics
<a name="enable-callrecording-speechanalytics"></a>

After conversational analytics is enabled for your instance, you can add [Set recording and analytics behavior](set-recording-behavior.md) blocks to your flows. You then enable conversational analytics when you configure the **Set recording and analytics behavior** block.

1. In the flow designer add a [Set recording and analytics behavior](set-recording-behavior.md) block to your flow. 

   For information about which flow types you can use with this block and other tips, see [Set recording and analytics behavior](set-recording-behavior.md).

1. Open the **Set recording and analytics behavior** properties page. Under **Call recording**, choose **On**, **Agent and Customer**.

   Both agent and customer call recordings are required to use conversational analytics for voice contacts.

1. Under **Analytics**, choose **Enable conversational analytics**, **Enable speech analytics**. 

   If you don't see this option, Connect Customer conversational analytics hasn't been enabled for your instance. For instructions to enable it, see [Enable conversational analytics for your Connect Customer instance](#enable-cl).

1. Choose one of the following:

   1. **Post-call analytics**: conversational analytics analyzes the call recording after the conversation and After Contact Work (ACW) is complete. This option provides the best transcription accuracy.

   1. **Real-time analytics**: conversational analytics provides both real-time insights during the call, and post-call analytics after the conversation has ended and After Contact Work (ACW) is complete.

      If you choose this option, we recommend setting up alerts based on keywords and phrases that the customer might utter during the call. conversational analytics analyzes the conversation real-time to detect the specified keywords or phrases, and alerts supervisors. From there, supervisors can listen in on the live call and provide guidance to the agent to help them resolve the issue faster.

      For information about setting up alerts, see [Alert supervisors in real-time for calls](add-rules-for-alerts.md).

      If your instance was created before October 2018, additional configuration is needed to access real-time call analytics. For more information, see [Service-linked role permissions](connect-slr.md#slr-permissions).

1. Choose from the [list of available languages](supported-languages.md#supported-languages-contact-lens).

   For instructions about specifying the language dynamically, see [Dynamically enable redaction based on the customer's language](#dynamically-enable-analytics-contact-flow).

1. Optionally, enable redaction of sensitive data. For more information, see the next section, [Enable redaction](#enable-redaction).

1. Choose **Save**.

1. If the contact is going to be transferred to another agent or queue, repeat these steps to add another [Set recording and analytics behavior](set-recording-behavior.md) block with **Enable conversational analytics for conversational analytics** enabled. 

## Enable chat analytics
<a name="enable-chatanalytics"></a>

1. In the [Set recording and analytics behavior](set-recording-behavior.md) block, under **Analytics**, choose **Enable conversational analytics**, and **Enable chat analytics**.
**Note**  
By choosing this option you will receive both real-time and post-chat analytics.

   If you don't see this option, Connect Customer conversational analytics hasn't been enabled for your instance. For instructions to enable it, see [Enable conversational analytics for your Connect Customer instance](#enable-cl).

1. Choose from the [list of available languages](supported-languages.md#supported-languages-contact-lens).

   For instructions on choosing the language and redaction dynamically, see [Dynamically enable redaction based on the customer's language](#dynamically-enable-analytics-contact-flow).

1. Optionally, enable redaction of sensitive data. For more information, see the next section, [Enable redaction](#enable-redaction).

1. Choose **Save**.

1. If the contact is going to be transferred to another agent or queue, repeat these steps to add another [Set recording and analytics behavior](set-recording-behavior.md) block with **Enable conversational analytics for conversational analytics** enabled. 

## Enable email analytics
<a name="enable-emailanalytics"></a>

You can enable conversational analytics for email contacts to automatically categorize emails, redact sensitive data, and generate contact summaries.

1. In the flow designer, add a [Set recording, analytics and processing behavior](set-recording-analytics-processing-behavior.md) block to your inbound email flow. Place the block before the email contact is routed to a queue or agent.

1. Open the block properties. For **Action**, choose **Set recording and analytics behavior**.

1. For **Channel**, choose **Email**.

1. Under **Analytics**, choose **Enable conversational analytics**, and **Enable email analytics**.

   If you don't see this option, Connect Customer conversational analytics hasn't been enabled for your instance. For instructions to enable it, see [Enable conversational analytics for your Connect Customer instance](#enable-cl).

1. Choose from the [list of available languages](supported-languages.md#supported-languages-contact-lens).

1. Optionally, enable redaction of sensitive data. For more information, see [Enable redaction](#enable-redaction).

1. Optionally, under **Generative AI capabilities**, enable **Contact summary** to generate summaries for email contacts.

1. Choose **Save**.

1. If the email contact is going to be transferred to another agent or queue, repeat these steps to add another [Set recording, analytics and processing behavior](set-recording-analytics-processing-behavior.md) block with **Enable conversational analytics for conversational analytics** enabled.

## Enable redaction of sensitive data
<a name="enable-redaction"></a>

When you configure the [Set recording and analytics behavior](set-recording-behavior.md) block for conversational analytics, you also have the option to enable redaction of sensitive data in a flow. When redaction is enabled you can choose from the following options:
+ Redact all personally identifiable information (PII) data (all PII entities supported).
+ Choose which PII entities to redact from the list of supported entities.

If you accept the default settings, conversational analytics redacts all personally identifiable information (PII) it identifies, and replaces it with **[PII]** in the transcript. The default settings are shown in the following image because the following options are selected: **Redact sensitive data**, **Redact All PII data**, and **Replace with placeholder PII**.

![The default settings for sensitive data redaction.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-enable-redaction-default.png)


### Select PII entities to redact
<a name="select-pii-entities-redact"></a>

Under the **Data redaction** section, you can select specific PII entities to redact. The following image shows that **Credit/Debit Card Number** is going to be redacted.

![The data redaction section, a list of entities you can redact.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-select-entities-to-redact.png)


### Choose data redaction replacement
<a name="mask-pii"></a>

Under the **Data redaction replacement** section, you can choose the mask to be used as data redaction replacement. For example, in the following image, the **Replace with placeholder PII** option indicates that **PII** will replace the data.

![The option to replace data with PII.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-dataredactionreplacement.png)


For more information about using redaction, see [Use sensitive data redaction](sensitive-data-redaction.md).

## Review sensitive data redaction for accuracy
<a name="review-sensitive-data-redaction"></a>

The redaction feature is designed to identify and remove sensitive data. However, due to the predictive nature of machine learning, it may not identify and remove all instances of sensitive data in a transcript generated by conversational analytics. We recommend you review any redacted output to ensure it meets your needs.

**Important**  
The redaction feature does not meet the requirements for de-identification under medical privacy laws like the U.S. Health Insurance Portability and Accountability Act of 1996 (HIPAA), so we recommend you continue to treat it as protected health information after redaction.

For the location of redacted files and examples, see [Output file locations](example-contact-lens-output-locations.md).

## Disable sentiment analysis
<a name="disable-sentiment-analysis-voice-and-chat"></a>

When you choose a language that is supported by sentiment analysis, AND choose **Enable speech analytics** or **Enable chat analytics**, sentiment analysis is enabled by default for all agents and customers. For a list of languages supported by sentiment analysis, see [AI features](supported-languages.md#supported-languages-contact-lens). 

The following image shows the sentiment analysis option is enabled on the **Set recording and analytics behavior** block. 

![The Sentiment analysis option when it is enabled.](http://docs.aws.amazon.com/connect/latest/adminguide/images/sentiment-analysis-enabled.png)


The following image shows a language that is not supported by sentiment analysis. We recommend opening the **Sentiment** section to verify whether it is enabled or disabled. 

![The Sentiment analysis option when it is disable because the language is not supported.](http://docs.aws.amazon.com/connect/latest/adminguide/images/sentiment-analysis-verify.png)


To disable sentiment analysis for all agents and customers, deselect the **Enable Sentiment Analysis** option, as shown in the following image.

![The sentiment analysis option when it is disabled.](http://docs.aws.amazon.com/connect/latest/adminguide/images/sentiment-analysis-disabled.png)


## Dynamically enable redaction based on the customer's language
<a name="dynamically-enable-analytics-contact-flow"></a>

You can dynamically enable the redaction of the output files based on the language of the customer. For example, for customers using en-US, you might want only a redacted file whereas for those using en-GB, you might want both the original and redacted output files.
+ Redaction: choose one of the following (they are case sensitive)
  + None
  + RedactedOnly
  + RedactedAndOriginal
+ Language: Choose from the [list of available languages](supported-languages.md#supported-languages-contact-lens).

You can set these attributes in the following ways:
+ User defined: use a **Set contact attributes** block. For general instructions about using this block, see [How to reference contact attributes](how-to-reference-attributes.md). Define the **Destination key** and **Value** for redaction and language as needed. 

  The following image shows an example of how you can configure the **Set contact attributes** block to use contact attributes for redaction. Choose the **Use text** option, set **Destination key** to **redaction\_option**, and set **Value** to **RedactedAndOriginal**. 
**Note**  
 **Value** is case sensitive.   
![The set contact attributes block, the use text option, the value is case sensitive.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-contact-attributes-enable-redaction1.png)

  The following image show how to use contact attributes for language. Choose the Use text option, set Destination key to language, set **Value** to **en-US**.  
![The set contact attributes block, the use text option, the value is case sensitive.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-contact-attributes-enable-redaction2.png)
+ [Use a Lambda function](attribs-with-lambda.md). This is similar to how you set up user-defined contact attributes. An AWS Lambda function can return the result as a key-value pair, depending on the language of the Lambda response. The following example shows a Lambda response in JSON: 

  ```
  {
     'redaction_option': 'RedactedOnly',
     'language': 'en-US'
  }
  ```

## Design a flow for key highlights
<a name="call-summarization-agent"></a>

Transcripts are visible to agents using the Contact Control Panel (CCP) depending on whether conversational analytics is enabled in the [Set recording and analytics behavior](set-recording-behavior.md) in the inbound flow, or a transfer flow.

This section provides three use cases for enabling conversational analytics in the [Set recording and analytics behavior](set-recording-behavior.md) block, and describes how they affect the agent's experience with key highlights.

### Use case 1: Conversational analytics is enabled in an inbound flow only
<a name="call-summarization-inbound-notransfer"></a>
+ A contact enters the inbound flow, and there are no call transfers. Following is the agent experience:

  The agent receives the full transcript during After Contact Work (ACW). The transcript includes everything said by the agent and the customer, from the moment the agent accepts the initial call, until the call has ended, as shown in the following image.  
![The contact control panel, the transcript of the conversation.](http://docs.aws.amazon.com/connect/latest/adminguide/images/call-summarization-use1.png)
+ A contact enters the inbound flow, and there is a call transfer. Following is the agent experience:
  + Agent 1 receives a call transcript after they leave the conference/warm transfer, during ACW.

    The transcript includes everything said by agent 1 and the customer, from the moment the agent accepts the initial call, until the agent 1 leaves the conference/warm transfer portion of the call. The transcript includes the flow (transfer/queue flow) prompt messages, as shown in the following image.   
![The flow transfer prompt in the transcript.](http://docs.aws.amazon.com/connect/latest/adminguide/images/call-summarization-use2.png)
  + Agent 2 receives a call transcript at the time of accepting the conference/warm transfer call from agent 1.

    The transcript includes everything said by agent 1 and the customer, from the moment agent 1 accepts the initial call until the agent 1 leaves the conference/warm transfer portion of the call. The transcript includes the flow (transfer/queue flow) prompt messages, and the warm transfer conversation, as shown in the following image.   
![The transcript, the flow transfer prompt and the warm transfer between two agents.](http://docs.aws.amazon.com/connect/latest/adminguide/images/call-summarization-use2b.png)

    Because conversational analytics is not enabled in the transfer flow, agent 2 doesn't see the remainder of the transcript when the call has ended and they enter ACW. The following image of ACW for agent 2 shows the transcript is empty.   
![An empty transcript.](http://docs.aws.amazon.com/connect/latest/adminguide/images/call-summarization-use2c.png)

### Use case 2: Conversational analytics is enabled in an inbound flow and a transfer flow (quick connect)
<a name="call-summarization-inbound-transfer2"></a>
+ A contact enters the inbound flow, and there are no call transfers. Following is the agent experience:
  + Agent 1 receives a full call transcript (unredacted) during ACW. 

    The transcript includes everything said by agent 1 and the customer from the moment the agent accepts the call, until the call has ended. This is shown in the following image of the CCP for agent 1.  
![The CCP for agent 1, a full call transcript.](http://docs.aws.amazon.com/connect/latest/adminguide/images/call-summarization-use3.png)
+ A contact enters the inbound flow, and there is a call transfer. Following is the agent experience:
  + Agent 1 receives a call transcript after they leave the conference/warm transfer, during ACW.

    The transcript includes everything said by agent 1 and the customer from the moment agent 1 accepts the call, until agent 1 leaves the conference/warm transfer portion of the call. The transcript includes flow (transfer/queue flow) prompt messages.

    The full call transcript until warm transfer is shown in the following image.  
![A full call transcript until agent 1 leaves the conference.](http://docs.aws.amazon.com/connect/latest/adminguide/images/call-summarization-use2b.png)
  + Agent 2 receives a call transcript at the time of accepting the conference/warm transfer call from agent 1.

    The transcript includes everything said by agent 1 and the customer, from the moment agent 1 accepts the call, until agent 1 leaves the conference/warm transfer portion of the call. The transcript includes the flow (transfer/queue flow) prompt messages. 
  + Because conversational analytics is enabled in the transfer flow, agent 2 receives a call transcript after the call is completed, during ACW. 

    The transcript includes only the remaining portion of the call between agent 2 and customer, after agent 1 has left the call. The transcript includes everything said by agent 2 and the customer, from the moment they are conferenced/warm transferred in, until the call has ended. An example transcript is shown in the following image.  
![A transcript of the call between agent 2 and the customer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/call-summarization-use3b.png)

## What if the flow block fails to enable conversational analytics?
<a name="troubleshoot-contactlens-enablement"></a>

It's possible that the [Set recording and analytics behavior](set-recording-behavior.md) block can fail to enable conversational analytics on a contact. If conversational analytics isn't enabled for a contact, [check the flow logs](search-contact-flow-logs.md) for the error.

## Multi-party calls and conversational analytics
<a name="multiparty-calls-contactlens"></a>

Conversational analytics supports calls with up to 2 participants. For example, if there are more than two parties (agent and customer) on a call, or a call is getting transferred to a third party, the quality of the transcription and analytics, such as sentiment, redaction, categories among others, can get degraded. We recommend you disable conversational analytics for multi-party or third-party calls if there are more than two parties (agent and customer). To do this, add another [Set recording and analytics behavior](set-recording-behavior.md) block to the flow and disable conversational analytics. For more information about the behavior of the flow block, see [Configuration tips](set-recording-behavior.md#set-recording-behavior-tips). 