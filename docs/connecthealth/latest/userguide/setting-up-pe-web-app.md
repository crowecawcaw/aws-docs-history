

# Set up agents in the patient engagement web app

You use the patient engagement web app to set up the agentic capabilities for patient access. In the app, you create an agent, turn capabilities on or off, configure each capability, and publish your changes.

In this guide, the object that you create and publish is called an *agent*.

![Home page of the patient engagement web app](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-home.png)


## Prerequisites
<a name="pe-setup-prerequisites"></a>

Before you set up an agent, complete the following:
+ Set up a patient engagement domain.
+ Connect an Epic electronic health record (EHR) integration and confirm that its status is `ACTIVE`. You cannot create an agent until an EHR integration exists.
+ To use the insurance check in appointment management, set up a real-time eligibility (RTE) integration in the AWS Management Console.
+ To use information assistance or knowledge base answers, set up a knowledge base (KB) integration in the AWS Management Console.
+ To use pharmacy refills in prescription management, add a pharmacy SOAP endpoint to your EHR integration.

## How drafts, publishing, and discarding work
<a name="pe-setup-changes"></a>

Your changes are saved as a draft until you publish them. Callers keep getting the current published setup until you publish. There is no version history, difference view, or rollback. The app tracks only your current draft and the published version.

To publish changes, choose **Publish** on the agent page. A confirmation message tells you that callers get the changes as soon as you publish. Publishing applies the agent’s draft and the drafts of every capability that is turned on.

You cannot publish when either of the following is true:
+ A decision tree is uploaded, but AWS hasn’t published it yet.
+ A capability that requires patient verification is turned on, but patient verification is turned off.

To undo changes, choose **Discard changes**. You can discard the whole agent or one section. A capability that was never published stays unpublished.

## Create, rename, and delete an agent
<a name="pe-setup-agent"></a>

![Agents page listing two agents with their status and capabilities](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-agents-list.png)


When you create an agent, the app adds every capability, turns each one on, and applies its default settings. If your domain has no `ACTIVE` RTE integration, the insurance check stays off.

### To create an agent
<a name="pe-setup-to-create-an-agent"></a>

1. Open the patient engagement web app.

1. In the navigation pane, choose **Agents**.

1. Choose **Create agent**.

1. For **Name**, enter a name for the agent.

1. Choose **Create**.

An agent name is required and must use printable ASCII characters. A name cannot contain the characters `< > = ( ) " ' % & ;`, and it can be up to 1,028 characters long.

You can rename or delete an agent from the row actions in the list, or from the **Actions** menu on the agent page. Renaming an agent does not require publishing. Deleting an agent is permanent, and callers stop reaching that agent.

## Turn capabilities on or off
<a name="pe-setup-capabilities"></a>

![Agent page showing the five capabilities and their status](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-agent-page.png)


Each capability has a card on the agent page. Choose a card to open the capability page, where you turn the capability on or off and set its options. Changes stay in your draft until you publish.

Patient verification is a dependency for the other capabilities. If you turn patient verification off, the app also turns off every capability except information assistance. The app asks you to confirm before it does this.

## Configure patient verification
<a name="pe-setup-verification"></a>

Patient verification confirms the patient’s identity against your EHR. The patient always provides all three factors. For the first and third factors, you choose which values the patient can use. The second factor is always date of birth. The patient’s medical record number (MRN) is one of the values that you can allow for the first factor.

![Patient verification capability page showing the three verification factor groups](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-patient-verification.png)



| Factor | Values | Default | 
| --- | --- | --- | 
| First factor | Phone number; MRN; Phone number or MRN | Phone number or MRN | 
| Second factor | Date of birth (fixed) | Date of birth | 
| Third factor | ZIP code; Last 4 SSN; ZIP code or last 4 SSN | Last 4 SSN | 

## Configure appointment management
<a name="pe-setup-appointment"></a>

![Appointment management capability page showing sub-capabilities and visit types](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-appointment-management.png)


Appointment management has four sub-capabilities, each with its own toggle: **Scheduling**, **Rescheduling**, **Cancellation**, and **Lookup**. All four are on by default.

### Open scheduling
<a name="pe-setup-open-scheduling"></a>

When **Scheduling** is on, you can turn on **Open scheduling**. Open scheduling is off by default.

### Insurance check
<a name="pe-setup-insurance-check"></a>

 **Insurance check** adds a real-time eligibility (RTE) check during scheduling. It is off by default. The toggle is unavailable until you have an `ACTIVE` RTE integration. To connect one, choose **Link RTE integration**.

### Visit types for cancellation and rescheduling
<a name="pe-setup-visit-types-for-cancellation-and-rescheduling"></a>

You can limit which visit types a patient can cancel or reschedule. Add each visit type as an ID and display name, or choose **Add from CSV** and enter one `ID,Name` pair per line. You can add up to 100 visit types. If you leave the list empty, patients can cancel or reschedule all visit types.

### Decision tree
<a name="pe-setup-decision-tree"></a>

A decision tree guides the questions that the agent asks to determine which visit to book, and the scheduling rules to apply.

![Decision tree section with the option to upload a PDF](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-decision-tree-upload.png)


To add a decision tree, do the following:

1. On the appointment management capability page, go to **Decision tree**.

1. Choose **Upload**.

1. Select a PDF file that is no larger than 4 MB.

To change or remove the tree, choose **Replace** or **Remove**.

After you upload a decision tree, AWS reviews it. The decision tree shows one of these statuses: `Extraction in progress`, `Ready`, `Needs reconciliation`, or `Extraction failed`. When the status is `Ready`, you can test the draft decision tree. You can publish the agent after AWS publishes the decision tree.

![Shared settings showing a decision tree with Ready status](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-decision-tree-ready.png)


## Configure prescription management
<a name="pe-setup-medication"></a>

![Prescription management capability page showing refill request and refill status](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-prescription-management.png)


Prescription management takes refill requests and reports refill status for health system pharmacies on Epic Willow. It has two toggles, **Refill request** and **Refill status**, and at least one must stay on.

Pharmacy refills need a Simple Object Access Protocol (SOAP) endpoint on your EHR integration. If the endpoint is missing, the capability page shows a message and a **Go to EHR integration** link.

## Configure MyChart password reset
<a name="pe-setup-password"></a>

![Password reset capability page showing the reset method options](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-password-reset.png)


For **Reset method**, choose how the agent sends the reset link:
+  **Email only** – The agent sends the link by email.
+  **Text message only** – The agent sends the link by text message.
+  **Let the caller choose** – The patient chooses email or text message during the call.

The default is **Let the caller choose**.

## Configure information assistance
<a name="pe-setup-information"></a>

![Information assistance capability page showing knowledge base documents](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-information-assistance.png)


Information assistance has no settings beyond the knowledge base. It answers general, non-clinical questions from the knowledge base documents that you add. For more information, see [Add knowledge base documents](#add-kb-documents).

## Set escalation thresholds
<a name="pe-setup-escalation"></a>

On the agent page, open **Advanced configuration** to set when the agent escalates to a person. Two settings control this:
+  **Retries before escalation** – How many times the agent retries before it escalates.
+  **Off-topic redirects before escalation** – How many times the agent redirects an off-topic conversation before it escalates.

Each setting accepts a value from 1 to 10.

The default for each is 2. You set these values on the agent, and every capability uses them.

## Add knowledge base documents
<a name="add-kb-documents"></a>

Information assistance and MyChart password reset answer questions from the knowledge base documents that you add. Open scheduling uses the open scheduling configuration file that you add to the knowledge base. This file maps visit types to providers and departments. Set up a knowledge base (KB) integration in the AWS Management Console before you add documents.

![Dialog box for adding a document to the knowledge base](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-kb-upload.png)


### To add a knowledge base document
<a name="pe-setup-to-add-a-knowledge-base-document"></a>

1. In the navigation pane, choose **Knowledge**.

1. Choose **Upload document**.

1. For **Files**, select one or more files.

1. For **Agent**, choose one agent or **All agents**.

1. For **Scope**, choose **All capabilities** or a single capability.

1. (Optional) For **Description**, enter a description.

1. Choose **Upload**.

You can add PDF, DOCX, TXT, MD, HTML, and CSV files.

Each file can be up to 50 MB.

The scope options are information assistance, appointment management (open scheduling), and MyChart password reset. The default scope is the first of these capabilities that the agent serves, not all capabilities.

Before you upload a document, send it to your AWS account team for review. AWS analyzes the document and returns an updated version. Upload the updated document, test it, and then publish it.

To publish a document, select it and choose **Submit for review**.

You can replace a file only while it is unpublished. You can also edit a document’s description or delete a document. Deleting a document re-indexes the knowledge base. You cannot upload a document while the knowledge base is indexing.

## Use the Connect Health Assistant
<a name="pe-setup-assistant"></a>

The Connect Health Assistant is a chat panel for administrators. To open it, choose **Show assistant**. The assistant helps you understand and test your setup. It does not change your configuration, and it is not a patient channel.

![Connect Health Assistant panel open next to the Appointment management page](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/pe-web-app-assistant-panel.png)


The assistant can do the following:
+ List your agents and capabilities and their status.
+ Explain a capability or how a patient call is handled.
+ Run a simulated call in chat against your unpublished draft.
+ Search your knowledge base.

To run a simulated call, choose **Test in chat**. **Test in chat** is available on the agent page and on each capability page.

## Test agents by phone
<a name="pe-setup-test"></a>

Before you make a test call, sync your EHR integration on the **Home** page. Until you sync it, patient details don’t appear in the handoff view that staff see.

On the **Home** page, the **Make a test call** card shows a test phone number after your EHR integration is `ACTIVE`. Call that number to test your published setup.

To change the contact flow, phone numbers, or other call settings, choose **Customize call flow**. This opens the Amazon Connect Customer console. The patient engagement web app does not include contact flow or phone number settings.