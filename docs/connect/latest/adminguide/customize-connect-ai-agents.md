# Customize Connect AI agents

You can customize how Connect AI agents work by using the Amazon Connect admin website, no coding required. For example, you
can customize the tone or format of the responses, the language, or the behavior.

Following are a few use cases for how you can customize Connect AI agents:

- Personalize a response based on data. For example, you want your AI agent to provide a
  recommendation to a caller based on their loyalty status and past purchase
  history.
- Make responses more empathetic because of the line of business that it's
  in.
- Create a new tool, such as a self-service password reset for customers.
- Summarize a conversation and pass it to an agent.
  You customize Connect AI agents by creating or editing their AI prompts, AI guardrails, and adding tools.

1. [AI prompt](create-ai-prompts.md "create-ai-prompts.md"): This is a task for the large
   language model (LLM) to do. It provides a task description or instruction for how
   the model should perform. For example, _Given a list of customer orders and
   available inventory, determine which orders can be fulfilled and which items
   have to be restocked_.

To make it easy for non-developers to create AI prompts, Amazon Connect provides a set of
templates that already contain instructions. The templates contain placeholder
instructions written in an easy-to-understand language called YAML. You just replace
the placeholder instructions with your own instructions. 2. [AI guardrail](create-ai-guardrails.md "create-ai-guardrails.md"): Safeguards based on your
use cases and responsible AI policies. Guardrails filter harmful and inappropriate
responses, redact sensitive personal information, and limit incorrect information in
the responses due to potential LLM hallucination. 3. [AI agent](create-ai-agents.md "create-ai-agents.md"): An resource that
configures and customizes end-to-end AI agent functionality. AI agents determine which
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
- [Set the language for Connect AI agents](ai-agent-configure-language-support.md "ai-agent-configure-language-support.md")
- [Add customer data to an AI agent session](ai-agent-session.md "ai-agent-session.md")
