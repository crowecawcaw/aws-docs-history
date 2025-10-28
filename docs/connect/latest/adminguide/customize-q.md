# Customize Amazon Q in Connect

You can customize how Amazon Q in Connect works by using the Amazon Connect admin website, no coding required. For example, you
can customize the tone or format of the responses, the language, or the behavior.

Following are a few use cases for how you can customize Amazon Q in Connect:

- Personalize a response based on data. For example, you want Amazon Q in Connect to provide a
  recommendation to a caller based on their loyalty status and past purchase
  history.
- Make responses more empathetic because of the line of business that it's
  in.
- Create a new tool, such as a self-service password reset for customers.
- Summarize a conversation and pass it to an agent.
  You customize Amazon Q in Connect by creating or editing AI prompts, AI guardrails, and AI
  agents.

1. [AI prompt](create-ai-prompts.md "create-ai-prompts.md"): This is a task for the large
   language model (LLM) to do. It provides a task description or instruction for how
   the model should perform. For example, _Given a list of customer orders and
   available inventory, determine which orders can be fulfilled and which items
   have to be restocked_.

To make it easy for non-developers to create AI prompts, Amazon Q in Connect provides a set of
templates that already contain instructions. The templates contain placeholder
instructions written in an easy-to-understand language called YAML. You just replace
the placeholder instructions with your own instructions. 2. [AI guardrail](create-ai-guardrails.md "create-ai-guardrails.md"): Safeguards based on your
use cases and responsible AI policies. Guardrails filter harmful and inappropriate
responses, redact sensitive personal information, and limit incorrect information in
the responses due to potential LLM hallucination. 3. [AI agent](create-ai-agents.md "create-ai-agents.md"): An Amazon Q in Connect resource that
configures and customizes end-to-end Amazon Q in Connect functionality. AI agents determine which
AI prompts and AI guardrails are used in different use cases: answer
recommendations, manual search, and self-service.
You can edit or create each of these components independently of each other. However, we
recommend a happy path where you first customize your AI prompts and/or AI guardrails. Then
add them to your AI agents. Finally create a Lambda and use the [AWS Lambda
function](invoke-lambda-function-block.md "invoke-lambda-function-block.md") block to associate the customized
AI agents with your flows.

###### Contents

- [Default AI prompts and AI
  agents](default-ai-system.md "default-ai-system.md")
- [Create AI prompts](create-ai-prompts.md "create-ai-prompts.md")
- [Create AI guardrails](create-ai-guardrails.md "create-ai-guardrails.md")
- [Create AI agents](create-ai-agents.md "create-ai-agents.md")
- [Set the language for Amazon Q in Connect](configure-language-support-for-q-in-connect.md "configure-language-support-for-q-in-connect.md")
- [Add custom data to an Amazon Q in Connect
  session](custom-data-q.md "custom-data-q.md")
