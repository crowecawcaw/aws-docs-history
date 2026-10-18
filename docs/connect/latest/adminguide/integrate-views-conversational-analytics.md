

# Prefill guides for after contact work using conversational analytics
<a name="integrate-views-conversational-analytics"></a>

You can fill in fields in a guide for after contact work (ACW) with outputs from conversational analytics:
+ The contact summary.
+ Extracted information, such as a booking ID or claim number.

When an agent enters ACW, the guide opens with those fields filled. The agent reviews the values, edits them if needed, and submits the guide.

**Note**  
The conversational analytics integration works only in views shown during after contact work, and only for voice and chat contacts. Email and task contacts aren't supported.

## Prerequisites
<a name="integrate-views-conversational-analytics-prerequisites"></a>
+ A guide for ACW that includes a custom view. The contact flow uses a **Set event flow** block to set `DisconnectAgentUI` to a flow that shows your view for ACW. For more information, see [Enable smart default guides for after contact work](enable-smart-default-guides-acw.md). You can't use the AWS managed **After Contact Work** view, because prefilling requires editing the properties of its components.
+ Add the following security profile permissions for your administrators (the users who create the guide) and your agents (the users who complete the guide):


<table>
<thead>
  <tr><th>Section</th><th>Permission</th><th>Needed for</th><th>Admins</th><th>Agents</th></tr>
</thead>
<tbody>
  <tr><td><b>Analytics and Optimization</b></td><td><b>Contact Lens - conversational analytics</b></td><td>Contact summary</td><td>View</td><td>View</td></tr>
  <tr><td><b>Analytics and Optimization</b></td><td><b>Contact Lens - post-contact summary</b></td><td>Contact summary</td><td>View</td><td>View</td></tr>
  <tr><td><b>Analytics and Optimization</b></td><td><b>Information extraction - definitions</b></td><td>Extracted information</td><td>All</td><td>Not needed</td></tr>
  <tr><td><b>Analytics and Optimization</b></td><td><b>Information extraction - results</b></td><td>Extracted information</td><td>View</td><td>View</td></tr>
  <tr><td><b>Analytics and Optimization</b></td><td><b>Rules</b></td><td>Extracted information</td><td>All</td><td>Not needed</td></tr>
  <tr><td><b>Analytics and Optimization</b></td><td><b>Rules - Generative AI</b></td><td>Extracted information</td><td>All</td><td>Not needed</td></tr>
  <tr><td><b>Contact Control Panel (CCP)</b></td><td><b>Contact Lens data</b></td><td>Contact summary and extracted information</td><td>Not needed</td><td>Access</td></tr>
  <tr><td><b>Recordings and Transcripts</b></td><td><b>Call recordings (redacted)</b> or <b>Call recordings (unredacted)</b></td><td>Voice contacts</td><td>Access</td><td>Access</td></tr>
  <tr><td><b>Recordings and Transcripts</b></td><td><b>Contact transcripts (redacted)</b> or <b>Contact transcripts (unredacted)</b></td><td>Chat contacts</td><td>Access</td><td>Access</td></tr>
</tbody>
</table>


  For recordings and transcripts, choose the permission that matches the redaction setting in your contact flow. If you turn on redaction in [Step 4](#integrate-views-conversational-analytics-step4), choose the redacted permission. Otherwise, choose the unredacted permission.

## Step 1: Create an information extraction rule for after contact work
<a name="integrate-views-conversational-analytics-step1"></a>

Skip this step if you prefill only the contact summary.

1. Create the information extraction definitions you want to prefill. For more information, see [Step 1: Create information extraction definition](information-extraction-configure.md#information-extraction-step1).

1. Create a rule with those definitions. For more information, see [Step 2: Create a rule with the Extract Information action](information-extraction-configure.md#information-extraction-step2). For the event source, choose one of the following:
   + Voice: **After-call work analysis is available**
   + Chat: **After chat analysis is available**

**Note**  
Rules with a post-contact analysis event source don't prefill the guide.

## Step 2: Add a conversational analytics integration to the view
<a name="integrate-views-conversational-analytics-step2"></a>

1. Open your view for ACW in the UI builder.

1. Choose an empty area of the canvas, so that no component is selected.

1. In the **Customize** panel, choose the **Integrations** tab, then **Configure**.

1. For **Integration Name**, enter a name. You use this name to reference the integration's data in components.

1. For **Integration Type**, choose **Conversational Analytics**.

1. To see the data you can reference, choose **Reference**.

## Step 3: Reference the data in a component
<a name="integrate-views-conversational-analytics-step3"></a>

1. On the canvas of the UI builder, choose the component you want to prefill. You can prefill any component that accepts text. We recommend the **Text Area** component.

1. On the **Properties** tab, enter a reference in `DefaultValue`:


<table>
<thead>
  <tr><th>To prefill</th><th>Reference</th></tr>
</thead>
<tbody>
  <tr><td>The contact summary</td><td><code>$.#IntegrationName.ContactSummary</code></td></tr>
  <tr><td>Extracted information</td><td><code>$.#IntegrationName.InformationExtraction['Definition name']</code></td></tr>
</tbody>
</table>


   Replace {{IntegrationName}} with the name from Step 2, and {{Definition name}} with the name of an information extraction definition. Keep the square brackets and single quotes. They let definition names include spaces.

   For example, if your integration is named `ConvAnalytics`, the reference `$.#ConvAnalytics.InformationExtraction['Booking ID']` prefills the field with the value of the `Booking ID` definition.

1. Save and publish the view.

## Step 4: Turn on conversational analytics in the contact flow
<a name="integrate-views-conversational-analytics-step4"></a>

1. Open the contact flow that corresponds to your agents' inbound or outbound contacts.

1. Add a **Set recording, analytics, and processing behavior** block before the **Set event flow** block that sets `DisconnectAgentUI`.

1. Configure the block:

   1. For **Select action**, choose **Set recording and analytics behavior**.

   1. For **Select channel**, choose **Voice** or **Chat**.

   1. Turn on conversational analytics for the channel:
      + Voice:

        1. Under **Enable recording**, select **Agent** and **Customer**.

        1. Under **Enable conversational analytics**, select **Enable conversational analytics** and **Enable agent and customer interaction analytics**.

        1. Choose **Real-time and post-contact analytics**. **Post-contact analytics** doesn't prefill the guide.
      + Chat: Under **Enable conversational analytics**, select **Enable conversational analytics**.

   1. Under **AI analytics**, select **Agent interaction summary**. You need this setting even if you prefill only extracted information.

   1. (Optional) Under **Redaction**, turn on conversational analytics redaction to remove sensitive data from the contact summary.

1. Save and publish the flow.

## What agents see
<a name="integrate-views-conversational-analytics-agents"></a>

When an agent enters ACW, the components you configured will show a loading indicator before filling with the contact summary or extracted information. An error banner will appear if the contact summary or extracted information aren't available.