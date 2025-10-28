# Upload files to a chat in Amazon Q Business

Users using the Amazon Q Business web experience can upload documents and use
the uploaded documents to ask questions and summarize or analyze data based on the
content of the uploaded documents. Amazon Q provides a list of recent
documents, enabling users to find and reuse recently attached files in new conversations
without re-uploading. Users can upload new files from their computer, select from recent
files, or drag and drop files directly into any conversation.

Users can upload up to 20 files during a conversation. The maximum upload size for
each file is 50 MB and 3.75 MB for images. The total parsed content for all files
combined has to be under 665,000 characters. Documents uploaded through the chat
interface are deleted with the associated conversation after 30 days of inactivity. Once
files are attached to a conversation, they cannot be deleted individually. Users must
delete the entire conversation to remove attached files.

Using the Amazon Q Business web experience, you can upload documents and use
them to ask questions and summarize or analyze data based on their content. When you
start a new conversation, you can upload new files, choose from a saved list of recent
documents, or drag and drop files directly into the conversation.

To use this feature, enable **Allow end users to send queries directly to the
LLM** in **Admin controls and guardrails**. For more
information, see the [Response settings](guardrails-global-controls.md#guardrails-global-response "guardrails-global-controls.md#guardrails-global-response") topic in [Admin controls and guardrails](guardrails-global-controls.md#guardrails-global-response "guardrails-global-controls.md#guardrails-global-response").

Amazon Q Business supports specific document types for upload. To learn more
about the document types that can be uploaded, see [Supported document formats in Amazon Q Business](doc-types.md "doc-types.md").

If you plan to upload comma separated value (CSV) or Microsoft Excel (XLS, XLSX)
files, we recommend using tables that have no more than 4 columns and 10 rows for best
results.

###### Important

Audio formats such as MP3, MP4, FLAC, WAV and Video formats such as MP4 and MOV
are not supported for chat upload.
