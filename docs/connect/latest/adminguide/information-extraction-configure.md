# Configure voice and chat information extraction

Configuring information extraction requires two steps:

- **Create information extraction definitions**
  – Define what information to extract from contacts
- **Create a rule with the Extract Information
  action** – Define when to trigger extraction for matching
  contacts

## Step 1: Create information extraction definition

Extraction definitions are instance-level resources that define what to extract
from a contact. However, they only take effect when you add them to a rule
(Step 2).

###### To create an extraction definition

1. In the Connect Customer navigation pane, choose **Rules**.
2. On the **Rules** page, choose the **Information
   extraction** tab.
3. Choose **Create information extraction definition**.
4. Configure the information extraction criteria:

| Field                              | Description                                                                                                                                                                                                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                           | The name of the information to extract. The name is<br>included as input to the extraction process and appears<br>as the label for the extracted information (unless you<br>specify a display label). For example:<br>`Reservation ID` or `Next steps<br>promised`. |
| **Display Label**<br>(optional)    | The label for the extracted information. The display<br>label is not used as input to the extraction<br>process.                                                                                                                                                    |
| **Prompt Hint**                    | Provide contextual cues or guidelines to identify the<br>specific information you want to extract. Example:<br>`A reservation identifier should be six<br>characters long and only include letters A-Z and<br>digits 0-9.`                                          |
| **If information is not<br>found** | What to display when the information is not found in<br>the contact. *_Omit_<br>• hides the field<br>entirely. *_Replace with alternate<br>word_<br>• to specify a fixed value (for<br>example, "Not provided").                                                    |

###### Tip

Do not over-engineer the **Prompt Hint** — prompt
engineering is already handled by conversational analytics. Keep hints
brief and descriptive. 5. Choose **Save**.

You can edit extraction definitions at any time. Changes apply to contacts
processed after the edit.

Repeat this process for each piece of information you want to extract. You can
create multiple extraction definitions and selectively use them in different
rules.

**Examples of verbatim information extraction
criteria:**

| Name           | Prompt hint                                                                                                                                     |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Preferred name | The name the customer used when introducing themself to the<br>agent.                                                                           |
| Invoice number | The unique identifier assigned to a specific invoice which<br>starts with "I-", then a four-digit year, then "-", and then<br>eight digits.     |
| Reservation ID | The unique identifier assigned to a specific reservation and<br>is comprised of six characters and only includes letters A-Z and<br>digits 0-9. |

**Examples of derived information extraction
criteria:**

| Name                | Prompt hint                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Reason for contact  | The primary reason or issue that led the customer to contact<br>the agent as stated by the customer at the start of the<br>conversation. |
| Resolution provided | What actions did the agent take during the contact to address<br>the customer's concerns or issues.                                      |
| Next steps promised | What next steps, if any, that the agent told the customer<br>would happen after the conversation.                                        |

## Step 2: Create a rule with the Extract Information action

Rules are used to trigger the information extraction process. Add information
extraction definitions to a rule to activate extraction for matching
contacts.

###### To create a rule with information extraction

1. In the Connect Customer navigation pane, choose
   **Rules**.
2. Choose **Create a rule**, then select
   **Conversational analytics**.
3. For **When** (event source), choose one of the
   following:

| Event source                          | When processed                                                     | Where results appear                                        |
| ------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------- |
| After-call work analysis is available | During after-contact work.                                         | CCP (Extracted Information widget), Contact details<br>page |
| After chat analysis is available      | During after-contact work.                                         | Contact details page                                        |
| Post-call analysis is available       | After the contact is closed and after-contact work is<br>complete. | Contact search, Contact details page                        |
| Post-chat analysis is available       | After the contact is closed and after-contact work is<br>complete. | Contact search, Contact details page                        |

###### Note

If a post-contact analysis rule triggers an information extraction
that was already completed by an after-call work analysis rule, the
extraction is skipped and does not process a second time.

###### Note

Information extraction is not available for real-time call analysis or
real-time chat analysis event sources. 4. Define your rule conditions. Choose **Next**.

###### Tip

If you want information extraction to occur on most contacts, set the
condition to match on **Agents** or
**Queues** rather than specific keywords. This
provides broad coverage while still providing the flexibility to limit
extraction to relevant contact types. 5. Under **Actions**, choose **Extract
Information**. 6. Select the information extraction definitions to include in this rule. You
can select multiple definitions. 7. (Optional) Add additional actions. Extracted information is available as
injectable variables in the following actions:

    * **Send email** — Insert extracted information
     into the email subject or body.
    * **Create task** — Include extracted information
     in the task name or description.
    * **Create case** — Map extracted information to
     case fields.
    * **Send notification** — Include extracted
     information in notification messages.

To insert extracted information, use the variable picker (or type
`@`) and select from the available information
names. 8. Choose **Save**.
