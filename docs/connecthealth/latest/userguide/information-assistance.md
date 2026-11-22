

# Information assistance

Information assistance is part of the agentic capabilities for patient access. It answers general, non-clinical questions, such as facility hours, directions, parking, departments, and help with navigating the patient portal. It answers from a knowledge base (KB) that you provide. Callers reach it by phone. It supports English only.

To make information assistance available to callers, turn it on in the web app. For instructions on setting up agents, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md). A caller does not need to be verified for information assistance to answer general questions.

## How it works
<a name="ia-how-it-works"></a>

Information assistance answers questions from your knowledge base and hands off when it cannot help. It works as follows:
+ It answers general, non-clinical questions from your knowledge base.
+ When a question is unclear, it asks the caller to narrow it down. For example, it can ask which location or department the caller means.
+ During another task, it can answer a general question and then continue the task.
+ It transfers the caller to a person when it cannot answer the question, or when there are signs that the caller is in distress.

## What information assistance does not do
<a name="ia-limitations"></a>

Information assistance does not do the following:
+ Give medical or clinical advice, even if a knowledge base document includes clinical content
+ Give medication information
+ Support languages other than English

## Prepare your knowledge base
<a name="ia-knowledge-base"></a>

Information assistance answers from the documents that you add to your knowledge base in the web app. Prepare your documents before you add them.

You add documents in the web app, scoped to this capability. For instructions on setting up agents, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).

Keep the following in mind when you add documents:
+  **Supported formats**: You can add documents in PDF, DOCX, TXT, MD, HTML, and CSV formats.
+  **File size**: Each file can be up to 50 MB.
+  **Scope**: You add documents for a specific agent and capability. Information assistance uses only the documents that are scoped to it.
+  **Review**: Before you upload a document, send it to your AWS account team for review. AWS analyzes the document and returns an updated version. Upload the updated document, test it, and then publish it.

### Best practices for knowledge base documents
<a name="ia-kb-best-practices"></a>

To help information assistance give accurate answers, follow these practices when you write your documents:
+ Write content for patients. Use patient-facing wording only.
+ Remove staff scripts and internal-only instructions.
+ Remove content that contradicts other documents.
+ Avoid image-heavy documents and screenshots.
+ Use clear section headings.
+ Don’t password-protect documents.