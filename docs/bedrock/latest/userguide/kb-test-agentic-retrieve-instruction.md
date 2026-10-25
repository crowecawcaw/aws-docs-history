

# Create and manage retrieval instructions
<a name="kb-test-agentic-retrieve-instruction"></a>

A retrieval instruction is a reusable resource that steers agentic retrieval. It sets how the agent searches your knowledge bases, who the assistant is, how the assistant formats answers, and when it declines to answer. You write the instruction once, Amazon Bedrock reviews it, and then you reference it from `AgenticRetrieveStream` requests.

A retrieval instruction isn't tied to a knowledge base, and it isn't a guardrail. You can apply it to requests against any of your knowledge bases in the same account and Region as the instruction. Retrieval instructions are optional. When a request doesn't reference one, agentic retrieval uses its default behavior. For more information about agentic retrieval, see [Use agentic retrieval to query a knowledge base](kb-test-agentic-retrieve.md).

## How retrieval instructions work
<a name="kb-retrieval-instruction-how-it-works"></a>

A retrieval instruction has four fields. Set at least one. Write each field as instructions addressed to the assistant, and put each kind of guidance in the field that controls it.


**Retrieval instruction fields**  

| Field | What it controls | Example | 
| --- | --- | --- | 
| retrievalGuidance | How the agent interprets and decomposes the question, and what it prioritizes when it searches. | Prefer the product manuals over the release notes. Treat model numbers such as X200 as exact-match terms. | 
| persona | Who the assistant is, including its identity, tone, and language. | You are the support assistant for Example Corp. Use a friendly, concise tone. Reply in the language of the question. | 
| answerFormat | How the answer is structured, including how it cites sources. | Start with a one-sentence answer, then list numbered steps. Cite the manual section after each step. | 
| answerPolicy | Whether and how to answer. For example, how strongly the retrieved results must support an answer, and what to do with questions that are out of scope. | Answer only from the retrieved documents. If they don't cover the question, say so and suggest contacting support. | 

The `persona`, `answerFormat`, and `answerPolicy` fields shape the generated answer. They apply only when `generateResponse` is `true` (the default). The `retrievalGuidance` field applies in both cases.

A retrieval instruction moves through the following stages:

1. **Review** – When you create or update an instruction, Amazon Bedrock stores the new content and reviews it asynchronously. The call returns before the review finishes.

1. **Activation** – When the review passes, the new content becomes the current content of the instruction, and the instruction is `ACTIVE`.

1. **Versioning** – `DRAFT` always refers to the current content, so it changes each time an update passes review. To keep the behavior of an application stable, save the current content as a numbered version, which never changes. Creating a version doesn't run a review.

1. **Application** – An `AgenticRetrieveStream` request references the instruction by its ID and, optionally, a version. When the request doesn't name a version, Amazon Bedrock applies `DRAFT`.

## Create a retrieval instruction
<a name="kb-retrieval-instruction-create"></a>

Before you start, you need a fully managed knowledge base that you query with agentic retrieval (see [Prerequisites](kb-test-agentic-retrieve.md#kb-agentic-retrieve-prereqs)), and the permissions in [Required permissions for retrieval instructions](#kb-retrieval-instruction-permissions).

1. Send a [CreateRetrievalInstruction](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateRetrievalInstruction.html) request with a `name` and an `instruction`. The following JSON example creates an instruction that sets all four fields:

   ```
   {
       "name": "{{support-assistant}}",
       "description": "Instruction for the customer support assistant",
       "instruction": {
           "retrievalGuidance": "Prefer the product manuals over the release notes. Treat model numbers such as X200 as exact-match terms.",
           "persona": "You are the support assistant for Example Corp. Use a friendly, concise tone. Reply in the language of the question.",
           "answerFormat": "Start with a one-sentence answer, then list numbered steps. Cite the manual section after each step.",
           "answerPolicy": "Answer only from the retrieved documents. If they don't cover the question, say so and suggest contacting support."
       }
   }
   ```
**Important**  
To encrypt the content with your own customer managed key, set `customerEncryptionKeyArn` in this request. You can't add or change the key later. For the key requirements and the key policy, see [Encryption of retrieval instructions](encryption-kb.md#encryption-kb-retrieval-instruction).

1. Call [GetRetrievalInstruction](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetRetrievalInstruction.html) until `lastTransitionStatus` is no longer `CREATING` or `UPDATING`.
   + `CREATE_SUCCESSFUL` – The review passed. The instruction is `ACTIVE` and ready to apply.
   + `CREATE_FAILED` – The review didn't pass. The instruction's `status` stays `INACTIVE`, and it can't be applied. `lastTransitionStatusReasons` says why. Go to the next step.

1. If the create failed, read `lastTransitionStatusReasons`. For a `CONTENT_REJECTED` reason, the entry names the field that the review rejected. Revise that field and send an [UpdateRetrievalInstruction](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateRetrievalInstruction.html) request. Send every field again, including the ones that passed, because an update replaces the whole instruction. You don't need to delete the instruction and create a new one. For the other reason codes, see `lastTransitionStatusReasons` in [GetRetrievalInstruction](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetRetrievalInstruction.html).

   Then repeat step 2. The outcome of an update is reported as `UPDATE_SUCCESSFUL` or `UPDATE_FAILED`.

## Apply a retrieval instruction to agentic retrieval
<a name="kb-retrieval-instruction-use"></a>

To apply an `ACTIVE` instruction to an `AgenticRetrieveStream` request, and to check which version a request used, see [Use retrieval instructions with agentic retrieval](kb-test-agentic-retrieve.md#kb-agentic-retrieve-instruction).

## Update a retrieval instruction
<a name="kb-retrieval-instruction-update"></a>

To change an instruction, send an [UpdateRetrievalInstruction](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateRetrievalInstruction.html) request. An update replaces the whole instruction, so send every field that you want to keep. A field that you leave out is removed. Include the `description` too, because an update without one clears it.

Amazon Bedrock reviews the new content in the same way as for a create, and the new content takes effect only after it passes review. The instruction keeps serving its previous content until the update passes review. Wait until the review finishes before you update the instruction again. A second update while a review is in progress fails with a `ConflictException`.

## Create and manage versions
<a name="kb-retrieval-instruction-versions"></a>

To create a version, send a [CreateRetrievalInstructionVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateRetrievalInstructionVersion.html) request. The version captures the current content of the instruction. Use the version number in the response in `retrievalInstructionConfiguration`. You can create a version only after the instruction is `ACTIVE`. If its first review hasn't passed, the request fails with a `ValidationException`. If an update is under review, it fails with a `ConflictException`.

To roll out a change without affecting an application that uses a pinned version:

1. Update the instruction, and call `GetRetrievalInstruction` until `lastTransitionStatus` is no longer `UPDATING`. Continue only if it is `UPDATE_SUCCESSFUL`. If it is `UPDATE_FAILED`, read `lastTransitionStatusReasons`, revise the instruction, and update it again.

1. Test the new content by sending requests that use `DRAFT`.

1. Create a version, and change the application to use the new version number.

1. To roll back, change the application back to the earlier version number. When you no longer need the earlier version, delete it.

A deleted version no longer counts toward the version quota. Amazon Bedrock never reuses a version number.

## Delete a retrieval instruction or a version
<a name="kb-retrieval-instruction-delete"></a>

To delete a version, call [DeleteRetrievalInstruction](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteRetrievalInstruction.html) with `retrievalInstructionVersion` set to the version number. Before you delete a version, move any application that pins it to another version.

To delete the instruction, first delete each of its versions and wait for any review in progress to finish, and then call `DeleteRetrievalInstruction` without `retrievalInstructionVersion`. Deleting is permanent.

## Required permissions for retrieval instructions
<a name="kb-retrieval-instruction-permissions"></a>

To manage retrieval instructions, the calling IAM identity needs permissions for the operations that it uses. The following policy allows all of them:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:CreateRetrievalInstruction",
                "bedrock:GetRetrievalInstruction",
                "bedrock:UpdateRetrievalInstruction",
                "bedrock:DeleteRetrievalInstruction",
                "bedrock:ListRetrievalInstructions",
                "bedrock:CreateRetrievalInstructionVersion",
                "bedrock:ListRetrievalInstructionVersions"
            ],
            "Resource": "arn:aws:bedrock:{{region}}:{{account-id}}:retrieval-instruction/*"
        }
    ]
}
```

To add tags when you create an instruction, the identity also needs `bedrock:TagResource`. To manage tags later, see [Tagging Amazon Bedrock resources](tagging.md). To apply an instruction in `AgenticRetrieveStream`, see [Required permissions for agentic retrieval](kb-test-agentic-retrieve.md#kb-agentic-retrieve-permissions).

If the instruction uses a customer managed key, the identity also needs AWS KMS permissions on the key: `kms:DescribeKey` for `CreateRetrievalInstruction`, `kms:GenerateDataKey` for `CreateRetrievalInstruction` and `UpdateRetrievalInstruction`, and `kms:Decrypt` for those two operations, for `GetRetrievalInstruction`, and for `AgenticRetrieveStream` requests that apply the instruction. For the key policy, see [Encryption of retrieval instructions](encryption-kb.md#encryption-kb-retrieval-instruction).

## Considerations
<a name="kb-retrieval-instruction-considerations"></a>

Keep the following in mind when you use retrieval instructions:
+ Retrieval instructions are available in the same Regions as agentic retrieval. For the list of Regions, see [Supported AWS Regions](kb-managed-regions.md).
+ For the number of instructions per account, versions per instruction, and characters per instruction, see [Service quotas for managed knowledge bases](kb-managed-quotas.md).