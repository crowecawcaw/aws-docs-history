# Knowledge bases

Knowledge bases are reusable libraries of trusted content that your agentic CX
designer applications can use to answer user questions.

Use a knowledge base when you want your conversational AI application to provide
grounded answers without creating a dedicated flow for every possible question.
Knowledge bases are useful for FAQs, policies, product information,
troubleshooting guidance, support instructions, and other content users may ask
about during a conversation.

To access knowledge bases, select **Resources** from your workspace menu, then
choose **Knowledge bases**.

A knowledge base is an on-demand content source that helps your application
answer questions using approved information.

When a user asks a question, agentic CX designer can search the knowledge base
for relevant content and return an answer based on the best match. This helps the
application respond to common questions while keeping answers grounded in the
content your team provides.

Knowledge bases can be used in:

|                         |                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| **Knowledge base node** | Retrieves an answer at a specific point in a deterministic flow.                              |
| **Agent tool**          | Lets an agent use the knowledge base as a tool when answering questions or completing a task. |

Agentic CX designer supports these knowledge base content types:

|               |                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Q&A**       | Stores question-and-answer pairs entered manually or uploaded through a supported file format.                                                  |
| **Documents** | Ingests uploaded files, such as PDFs, images, or text files, so the application can<br>retrieve relevant information from the document content. |

## Knowledge base settings

Knowledge base settings control how content is matched and returned.

|                          |                                                                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Confidence threshold** | Determines how confident the match must be before the knowledge base returns an answer.                                                                       |
| **Summarization**        | Allows the application to rephrase retrieved content into a more natural response.                                                                            |
| **Temperature**          | Controls how much flexibility the model has when summarizing or rephrasing an answer. Lower values are more conservative; higher values allow more variation. |
| **Top P**                | Controls how many word choices are considered when generating a summarized response. Lower values generally produce more conventional responses.              |

Use conservative settings when accuracy and consistency are more important than
dynamic creative phrasing.

## Q&A knowledge bases

A Q&A knowledge base stores structured question-and-answer pairs.

Use Q&A when your content is already organized as clear questions and approved
answers, such as FAQs, policy responses, support scripts, or short troubleshooting
guidance.

###### To create a Q&A knowledge base

1. Open **Resources** from the workspace menu.
2. Select **Knowledge bases**.
3. Select **Create knowledge base**.
4. Enter a name.
5. Choose **Q&A** as the content type.
6. Create the knowledge base.
7. Add content manually or upload supported Q&A content.
8. Save your changes.

You can add Q&A content by manually creating articles or uploading supported structured content.

Each Q&A entry should include:

- A user-facing question or phrase
- One or more approved responses
- Optional payload or metadata, if supported

Example JSON format:

```
[
  {
    "question": {
      "text": "What are your business hours?"
    },
    "responses": [
      {
        "type": "text",
        "body": "We are open Monday through Friday from 9 AM to 6 PM."
      }
    ]
  }
]
```

Metadata can be used to filter which Q&A content should be searched during retrieval, when supported.

Use metadata when a Q&A knowledge base contains a large amount of content and
you only want to search a specific subset.

For example, an insurance support application may include policy questions for
multiple states. Metadata can help filter answers by state, coverage type, or
document type so the user receives a more relevant response.

Example metadata schema:

```
{
  "documentId": "",
  "policyholderId": "",
  "documentType": "",
  "coverageType": "",
  "language": "",
  "state": "",
  "sensitive": true
}
```

###### To configure metadata

1. Open the Q&A knowledge base.
2. Select the **Metadata** tab.
3. Add or generate the metadata schema.
4. Save the schema.
5. Open the **Content** tab.
6. Expand the relevant Q&A article.
7. Add metadata values.
8. Save your changes.
9. Publish a new version of the knowledge base.

After metadata is configured, you can apply metadata filters when the knowledge
base is called from a flow, if supported by the node configuration.

After creating or updating Q&A content, publish the knowledge base so the
changes become available.

###### To publish

1. Open the Q&A knowledge base.
2. Select the **Deployments** tab.
3. Enter an optional deployment description.
4. Select **Publish**.

Publishing creates a new version of the Q&A knowledge base content. After the
initial application deployment, publishing Q&A updates can make content changes
available without requiring a new application deployment.

If needed, you can roll back a Q&A knowledge base to a previous published version.

###### To roll back

1. Open the Q&A knowledge base.
2. Select the **Deployments** tab.
3. Locate the previous version.
4. Select **Roll back** for the version you want to restore.

Use rollback when a recent content update introduced incorrect or unintended answers.

## Documents knowledge bases

A Documents knowledge base lets you upload files and use their content for retrieval.

Use Documents when your source material exists as policies, manuals, PDFs,
guides, articles, or other documentation that would be difficult to convert into
individual Q&A pairs.

Document ingestion processes your uploaded files so the application can search
and retrieve relevant content when a user asks a question.

###### To create a Documents knowledge base

1. Open **Resources** from the workspace menu.
2. Select **Knowledge bases**.
3. Select **Create knowledge base**.
4. Enter a name.
5. Choose **Documents** as the content type.
6. Create the knowledge base.
7. Select **Upload**.
8. Upload files from your computer (pdf, txt, jpg, png, doc, docx).
9. Save your changes.
10. Wait for the files to finish processing.

When processing is complete, the document status should show that the content
has been ingested.

## How retrieval works

Knowledge bases use semantic retrieval to find relevant content.

At a high level:

1. A user asks a question.
2. Agentic CX designer compares the user's question against knowledge base content.
3. The most relevant matching content is retrieved.
4. The application returns or summarizes an answer based on the retrieved content.
5. If no confident match is found, the flow can follow a no-match, fallback, or escalation path.

This helps the application answer questions based on approved content rather than
relying only on a prompt.

## Using a knowledge base in a flow

###### To use a knowledge base in a deterministic flow

1. Open a flow.
2. Add a Knowledge base node.
3. Select the knowledge base to query.
4. Choose the user question or variable that should be sent to the knowledge base
   (default is {System.utterance}).
5. Configure the output variable that will store the answer.
6. Connect the match path to the next message or action where the output variable is referenced.
7. Connect the no-match path to a recovery, fallback, or escalation experience.
8. Save and test the flow.

For example, an Unknown flow might send the user's latest utterance to a
knowledge base. If a match is found, the application returns the answer. If no match
is found, the application can ask a clarifying question, link to a different knowledge
base node, or route to escalation.

## Using a knowledge base as an agent tool

A knowledge base can also be attached as a tool to an agent node.

Use this when the AI agent should decide when to search the knowledge base as
part of a broader task.

For example, an AI agent may use a knowledge base to answer policy questions
while also collecting user details and calling Data requests.

When attaching a knowledge base as a tool, provide clear instructions so the agent
understands:

- Identify the tool as a knowledge base and when to use
- What to do if no answer is found
- Whether it should summarize or quote content
