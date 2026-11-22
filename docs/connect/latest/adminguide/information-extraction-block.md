

# Flow block in Connect Customer: Information Extraction

Use the **Information Extraction** block to extract structured data from an email contact and its attachments, and then branch or route on the result within the flow.

**Note**  
The **Information Extraction** block is only available in [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/enable-nextgeneration-amazonconnect.html) instances, and only in certain Regions. For the list of Regions, see [Conversational analytics availability by Region](regions.md#contactlens_region).

This block extends [Information extraction](information-extraction.md) (voice and chat) to the email channel, and uses the same extraction definitions.

## Description
<a name="information-extraction-block-description"></a>
+ Extracts structured data, such as customer name, invoice number, or reason for contact, from the body and attachments of an email contact.
+ Starts an extraction job that runs asynchronously. To read the result, add a second **Information Extraction** block set to **Load extraction result** after a wait period.
+ Stores the result in the `$.ExtractedInformation` namespace.
+ Available in Connect Customer Customer at no additional cost.

## Supported channels
<a name="information-extraction-block-channels"></a>

The following table lists how this block routes a contact who is using the specified channel.


| Channel | Supported? | 
| --- | --- | 
| Voice | No | 
| Chat | No | 
| Task | No | 
| Email | Yes | 

## Flow types
<a name="information-extraction-block-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ Inbound flow
+ Flow modules

## Prerequisites and dependencies
<a name="information-extraction-block-prerequisites"></a>

Before you use this block, verify the following:
+ You created at least one [information extraction definition](https://docs.aws.amazon.com/connect/latest/adminguide/information-extraction-configure.html) that specifies the fields to extract, for example **Customer Name** or **Invoice Number**.
+ The contact is an email contact. The block extracts information from the email body and supported attachments.

## Properties
<a name="information-extraction-block-properties"></a>

The block supports the following actions. Select an action using **Select an action**.

### Invoke information extraction
<a name="information-extraction-block-invoke"></a>

The following image shows the **Invoke information extraction** action in the block properties, including the **Select entities** list where you choose the fields to extract.

![The Information Extraction block with the Invoke information extraction action and the Select entities list.](https://docs.aws.amazon.com/connect/latest/adminguide/images/information-extraction-invoke.png)

+ **Select entities** (required): The fields to extract, from an extraction definition associated with your instance. You can set this manually or dynamically.
+ The block starts the extraction job and routes the contact to the next block immediately. The job runs asynchronously and can take up to a minute to finish.
+ Branches: **Success** and **Error**.
  + **Success**: The block started the extraction job. Use `$.ExtractedInformation.InvocationId` to reference the job.
  + **Error**: The block could not start the job. This can happen when the extraction definition is invalid, the block cannot fetch the email content, or a service error occurs. Check that the extraction definition is valid and the email content is accessible, then retry the extraction.

### Load extraction result
<a name="information-extraction-block-load"></a>

The following image shows the **Load extraction result** action in the block properties, with **Namespace** set to **Extracted information** and **Key** set to **Invocation ID**.

![The Information Extraction block set to the Load extraction result action, with Namespace set to Extracted information and Key set to Invocation ID.](https://docs.aws.amazon.com/connect/latest/adminguide/images/information-extraction-load.png)

+ **Invocation ID** (required): The invocation ID of a job started by a previous **Invoke information extraction** action. `$.ExtractedInformation.InvocationId` contains the invocation ID of the most recent extraction.
+ For the **Load extraction result** action, set **Namespace** = `ExtractedInformation` and **Key** = **Invocation ID**.
+ Branches: **Success**, **In progress**, and **Error**.
  + **Success**: The extraction completed. The result is available in `$.ExtractedInformation.ResultData`.
  + **In progress**: The extraction is still running. Add a [Wait](wait.md) block before this block to allow time for the extraction to complete, or loop back to check again.
  + **Error**: The extraction failed. The block routes the contact down this branch.

## Namespace
<a name="information-extraction-block-namespace"></a>

The **Information Extraction** block writes results to the following namespace paths:
+ `$.ExtractedInformation.InvocationId` – the current extraction job ID.
+ `$.ExtractedInformation.ResultData` – the extraction result, a JSON object that contains the fields from the extraction definition.
+ `$.ExtractedInformation.ResultData.fieldName` – a specific extracted field. Each field is a list, so use an index. For example, `$.ExtractedInformation.ResultData.customerName[0]`.

Each new invocation overwrites the previous `$.ExtractedInformation` result. To keep a result, copy it to a contact attribute (`$.Attributes.*`) using the [Set contact attributes](set-contact-attributes.md) block before you start another extraction.

The following image shows a **Set contact attributes** block that copies `customerName` and `applicationId` from `$.ExtractedInformation.ResultData` into user-defined attributes.

![A Set contact attributes block that copies extracted fields from the ExtractedInformation namespace into user-defined attributes.](https://docs.aws.amazon.com/connect/latest/adminguide/images/information-extraction-set-attributes.png)


## Supported attachment types
<a name="information-extraction-block-attachments"></a>

The block processes the email body and the following attachment types.


| Attachment type | File extensions | How the block processes it | 
| --- | --- | --- | 
| Portable Document Format (PDF) documents | `.pdf` | Sent to the AI model as a native document content block. | 
| JPEG images | `.jpg`, `.jpeg` | Sent to the AI model as a native image content block. | 
| PNG images | `.png` | Sent to the AI model as a native image content block. | 
| Plain text files | `.txt` | Included inline with the email body text. | 

The block skips unsupported attachment types, such as `.docx`, `.xlsx`, and `.zip`. The extraction job still succeeds using the email body and any supported attachments.
+ Maximum attachment size: 4.5 MB per attachment.
+ Maximum PDF length: 100 pages. The block rejects a PDF that exceeds 100 pages.

## Configuration tips
<a name="information-extraction-block-tips"></a>
+ Add a [Wait](wait.md) block with a 60-second timeout between the **Invoke information extraction** and **Load extraction result** blocks. This gives the AI model time to process the email.
+ Copy results to contact attributes. Each extraction overwrites the previous `$.ExtractedInformation` namespace. Use a [Set contact attributes](set-contact-attributes.md) block to persist the data before you start another extraction.
+ Extraction definitions are reusable. You can use the same definition for voice and chat rules-based extraction and for this block.
+ Handle the **Error** branch. The block routes the contact down the **Error** branch when the email body is empty, attachments are corrupted, or the AI model returns an error. Route the branch to a queue, or set a default attribute value.

## Example
<a name="information-extraction-block-example"></a>

When a financial services company receives a loan application by email with a PDF attachment, an inbound email flow can use the **Information Extraction** block to extract the applicant name and application ID from the email body and the PDF. After a [Wait](wait.md) block, a second **Information Extraction** block loads the result. The flow then copies the fields to contact attributes with a [Set contact attributes](set-contact-attributes.md) block and routes the contact to the right loan processing team, or to a default queue if the extraction fails.

## Configured
<a name="information-extraction-block-configured"></a>

After you configure the block, it shows the **Success** and **Error** branches for the **Invoke information extraction** action. For the **Load extraction result** action, it also shows the **In progress** branch.

The following image shows a sample inbound email flow that uses these branches.

![A sample inbound email flow with Invoke and Load Information Extraction blocks, a Wait block, and a Set contact attributes block.](https://docs.aws.amazon.com/connect/latest/adminguide/images/information-extraction-example-flow.png)


The following image shows the extracted `customerName` and `applicationId` values as user-defined attributes in the agent workspace.

![The agent workspace showing extracted customerName and applicationId values as user-defined attributes for an email contact.](https://docs.aws.amazon.com/connect/latest/adminguide/images/information-extraction-result.png)
