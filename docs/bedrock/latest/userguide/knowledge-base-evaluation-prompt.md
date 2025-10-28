# Create a prompt dataset for a RAG

evaluation in Amazon Bedrock

To evaluate retrieval and generation for an Amazon Bedrock Knowledge Base or for your own Retrieval Augmented Generation (RAG) system, you provide a prompt dataset.
When you provide response data from your own RAG system, Amazon Bedrock skips
the Knowledge Base invoke step and performs the evaluation job directly on your data.

Prompt datasets must be stored in Amazon S3 and use the JSON line format and
`.jsonl` file extension. Each line must be a valid JSON object. There can be
up to 1000 prompts in your dataset per evaluation job. For retrieve-and-generate evaluation jobs, the maximum number of turns for each
conversation is 5. For retrieve-only evaluations, you can specify only a single turn.

For jobs created using the console you must update the Cross Origin Resource Sharing (CORS)
configuration on the S3 bucket. To learn more about the required CORS permissions, see [Required Cross Origin Resource Sharing
(CORS) permissions on S3 buckets](model-evaluation-security-cors.md "model-evaluation-security-cors.md").

See the following topics to learn more about key value pairs that are required based on the
type of evaluation job you select.

###### Topics

- [Create a prompt dataset
  for retrieve-only RAG evaluation jobs](knowledge-base-evaluation-prompt-retrieve.md "knowledge-base-evaluation-prompt-retrieve.md")
- [Creating a prompt
  dataset for retrieve-and-generate RAG evaluation jobs](knowledge-base-evaluation-prompt-retrieve-generate.md "knowledge-base-evaluation-prompt-retrieve-generate.md")
