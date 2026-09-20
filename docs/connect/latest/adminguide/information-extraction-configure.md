

# Configure voice and chat information extraction
<a name="information-extraction-configure"></a>

Configuring information extraction requires two steps:
+ **Create information extraction definitions** – Define what information to extract from contacts
+ **Create a rule with the Extract Information action** – Define when to trigger extraction for matching contacts

## Step 1: Create information extraction definition
<a name="information-extraction-step1"></a>

Extraction definitions are instance-level resources that define what to extract from a contact. However, they only take effect when you add them to a rule (Step 2).

**To create an extraction definition**

1. In the Connect Customer navigation pane, choose **Rules**.

1. On the **Rules** page, choose the **Information extraction** tab.

1. Choose **Create information extraction definition**.

1. Configure the information extraction criteria:


<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Name</b></td><td>The name of the information to extract. The name is included as input to the extraction process and appears as the label for the extracted information (unless you specify a display label). For example: <code>Reservation ID</code> or <code>Next steps promised</code>.</td></tr>
  <tr><td><b>Display Label</b> (optional)</td><td>The label for the extracted information. The display label is not used as input to the extraction process.</td></tr>
  <tr><td><b>Prompt Hint</b></td><td>Provide contextual cues or guidelines to identify the specific information you want to extract. Example: <code>A reservation identifier should be six characters long and only include letters A-Z and digits 0-9.</code></td></tr>
  <tr><td><b>If information is not found</b></td><td>What to display when the information is not found in the contact. <b>Omit</b> hides the field entirely. <b>Replace with alternate word</b> to specify a fixed value (for example, "Not provided").</td></tr>
</tbody>
</table>

**Tip**  
Do not over-engineer the **Prompt Hint** — prompt engineering is already handled by conversational analytics. Keep hints brief and descriptive.

1. Choose **Save**.

You can edit extraction definitions at any time. Changes apply to contacts processed after the edit.

Repeat this process for each piece of information you want to extract. You can create multiple extraction definitions and selectively use them in different rules.

**Examples of verbatim information extraction criteria:**


| Name | Prompt hint | 
| --- | --- | 
| Preferred name | The name the customer used when introducing themself to the agent. | 
| Invoice number | The unique identifier assigned to a specific invoice which starts with "I-", then a four-digit year, then "-", and then eight digits. | 
| Reservation ID | The unique identifier assigned to a specific reservation and is comprised of six characters and only includes letters A-Z and digits 0-9. | 

**Examples of derived information extraction criteria:**


| Name | Prompt hint | 
| --- | --- | 
| Reason for contact | The primary reason or issue that led the customer to contact the agent as stated by the customer at the start of the conversation. | 
| Resolution provided | What actions did the agent take during the contact to address the customer's concerns or issues. | 
| Next steps promised | What next steps, if any, that the agent told the customer would happen after the conversation. | 

## Step 2: Create a rule with the Extract Information action
<a name="information-extraction-step2"></a>

Rules are used to trigger the information extraction process. Add information extraction definitions to a rule to activate extraction for matching contacts.

**To create a rule with information extraction**

1. In the Connect Customer navigation pane, choose **Rules**.

1. Choose **Create a rule**, then select **Conversational analytics**.

1. For **When** (event source), choose one of the following:


<table>
<thead>
  <tr><th>Event source</th><th>When processed</th><th>Where results appear</th></tr>
</thead>
<tbody>
  <tr><td>After-call work analysis is available</td><td>During after-contact work.</td><td>CCP (Extracted Information widget), Contact details page</td></tr>
  <tr><td>After chat analysis is available</td><td>During after-contact work.</td><td>Contact details page</td></tr>
  <tr><td>Post-call analysis is available</td><td>After the contact is closed and after-contact work is complete.</td><td>Contact search, Contact details page</td></tr>
  <tr><td>Post-chat analysis is available</td><td>After the contact is closed and after-contact work is complete.</td><td>Contact search, Contact details page</td></tr>
</tbody>
</table>

**Note**  
If a post-contact analysis rule triggers an information extraction that was already completed by an after-call work analysis rule, the extraction is skipped and does not process a second time.
**Note**  
Information extraction is not available for real-time call analysis or real-time chat analysis event sources.

1. Define your rule conditions. Choose **Next**.
**Tip**  
If you want information extraction to occur on most contacts, set the condition to match on **Agents** or **Queues** rather than specific keywords. This provides broad coverage while still providing the flexibility to limit extraction to relevant contact types.

1. Under **Actions**, choose **Extract Information**.

1. Select the information extraction definitions to include in this rule. You can select multiple definitions.

1. (Optional) Add additional actions. Extracted information is available as injectable variables in the following actions:
   + **Send email** — Insert extracted information into the email subject or body.
   + **Create task** — Include extracted information in the task name or description.
   + **Create case** — Map extracted information to case fields.
   + **Send notification** — Include extracted information in notification messages.

   To insert extracted information, use the variable picker (or type `@`) and select from the available information names.

1. Choose **Save**.