# Connect Customer

Connect Customer is an AI-native solution that helps companies of any scale deliver
exceptional customer experiences at every touchpoint. You can use fully autonomous AI agents,
a blend of AI and human agents working together, or fully human-supported experiences. AI is
embedded across all channels for every customer, with simple per-channel pricing. For more
information, visit [Connect Customer
Pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/").

###### Contents

- [AI capabilities](#customer-ai-capabilities "#customer-ai-capabilities")
- [Updating existing Connect Customer instances](#how-to-enable-ac "#how-to-enable-ac")
- [How to switch to Customer Basic](#how-to-disable-ac "#how-to-disable-ac")

## AI capabilities

Connect Customer embeds AI at every stage of the customer journey. The following
capabilities are included with Connect Customer.

- **End-customer self-service** — agentic
  voice and agentic chat powered by AI agents
- **Generative speech** — Amazon Polly
  generative voices and third-party speech-to-text (STT) and text-to-speech
  (TTS) model configuration
- **Real-time agent assistance** —
  AI-powered recommendations and next-best-action guidance during live
  conversations
- **Conversational analytics and post-contact
  summaries** — sentiment analysis, theme detection, and
  automated summaries across voice, chat, messaging, and email
- **AI-powered case summarization** —
  automatically generated case summaries to accelerate resolution
- **Performance evaluations** — evaluate
  both human agents and self-service interactions
- **Forecasting and agent scheduling** —
  predict contact volumes and optimize agent schedules
- **Flow designer analytics** — insights
  into contact flow performance
- **Custom metrics in dashboards and APIs**
  — build tailored views of contact center performance
- **Customer-first callbacks** — dials
  the customer first and only offers the callback to an agent if the customer
  answers the call

## Updating existing Connect Customer instances

All new instances are Connect Customer instances.

If your Connect Customer instance was created before Connect Customer was available, you might need to
update your instance to Connect Customer.

1. Log in to the AWS Management Console using your AWS account.
2. In the AWS Management Console, in the search box, type
   **Connect Customer**. Choose **Connect Customer**.
3. On the **Connect Customer virtual contact center instances** page,
   choose the **instance alias** where you want to enable
   Connect Customer.
4. In the navigation pane, choose **Connect Customer**.
5. In the **Enable Connect Customer across your entire
   instance** section, confirm the status is **Not
   enabled**.
6. Choose **Enable**.

## How to switch to Customer Basic

Connect Customer Basic does not include all the AI capabilities available in Connect Customer. If you switch to Connect Customer Basic, some capabilities you are using today might no longer
be available, including:

- Agentic customer experience designer (ACXD)

  - No-code visual canvas
  - Blended AI logic - agentic AI reasoning and deterministic AI
  - Live sync of web or mobile app during live voice or chat

- [Agentic voice](agentic-voice.md "agentic-voice.md")

  - 50+ languages
  - 100+ voices
  - Third-party speech-to-text (STT) and text-to-speech (TTS) model support

- [AI agent observability](monitor-ai-agent-performance.md "monitor-ai-agent-performance.md")

  - Out-of-the-box AI agent performance metrics evaluated using LLM-as-a-judge

- [AI assistant for natural language configuration](connect-assistant-ui-builder.md "connect-assistant-ui-builder.md")

  - Step-by-step guides
  - Workspace pages

- Queue management

  - [Contact estimated wait time](get-queue-metrics.md#get-metrics-tips "get-queue-metrics.md#get-metrics-tips")
  - [Customer-first callbacks](customer-first-cb.md "customer-first-cb.md")

- [Conversational analytics](analyze-conversations.md "analyze-conversations.md")

  - Email conversational analytics, including:

    - Sensitive data redaction
    - Summarization
    - Categorization
    - Rules-based actions

  - Case summarization
  - Information extraction

    - Rules-based information extraction for voice and chat contacts

  - Recording ingestion and conversational analytics

- [Performance evaluations](evaluations.md "evaluations.md")

  - Self-service interaction evaluations
  - AI agent performance evaluations

- [Flow designer analytics](monitor-flow-performance.md "monitor-flow-performance.md")
- [Custom metrics in dashboards and APIs](custom-metrics-topic.md "custom-metrics-topic.md")

###### Warning

If these features are configured in contact flows, you might encounter runtime
errors.

Complete the following steps to switch from Connect Customer to Connect Customer Basic for a
given Connect Customer instance.

1. Log in to the AWS Management Console using your AWS account.
2. In the AWS Management Console, in the search box, type
   **Connect Customer**. Choose **Connect Customer**.
3. On the **Connect Customer virtual contact center instances** page,
   choose the **instance alias** where you want to switch to
   Customer Basic.
4. In the navigation pane, choose **Connect Customer**.
5. In the **Enable Connect Customer across your entire
   instance** section, confirm the status is
   **enabled**.
6. Choose **Disable**.

A dialog box appears prompting you to confirm that you want to switch to
Customer Basic. Choose **Disable** to confirm.
