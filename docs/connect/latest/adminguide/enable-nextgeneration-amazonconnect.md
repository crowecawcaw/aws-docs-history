

# Connect Customer
<a name="enable-nextgeneration-amazonconnect"></a>

Connect Customer is an agentic AI solution for customer experience. It supports the full lifecycle of customer interactions — from proactive outreach to self-service resolution to agent assistance — across any channel. For more information about pricing, see [Connect Customer Pricing](https://aws.amazon.com/connect/pricing/).

**Agentic AI:** Connect Customer uses agentic AI, an approach where AI reasons, decides, and acts autonomously rather than following a script or waiting for triggers. At the center are AI agents that handle customer interactions from start to finish. They understand intent, maintain context across channels, and retrieve knowledge. They can also take action, such as processing a return, updating an account, or rebooking a flight. Conversations stay natural, while tasks that must go exactly right, such as identity verification and compliance disclosures, run as structured, rule-based steps. AI agents resolve customer requests and work alongside human agents in real time. They provide step-by-step guidance and suggested responses, so your customers get what they need faster and at lower cost.

**Every channel:** Connect Customer delivers the same AI, routing, and customer context across every channel — voice, chat, email, SMS, web, WhatsApp, Apple Messages, and more — so your customers can move between channels without repeating themselves. With live sync, Connect Customer synchronizes a voice conversation with an on-screen interface, so your customers can see options, fill forms, and complete transactions while they speak. Adding a new channel takes configuration, not a new project.

**Speed to launch:** Connect Customer reduces implementation time from months to weeks. Business and customer experience teams design conversational experiences directly on a visual no-code canvas, with no engineering handoff required for the conversation design itself. Pre-built templates get your first use case live in weeks, not months. Start with a single workflow and expand over time. For teams that want more architectural control, a developer-first path is also available.

**Topics**
+ [AI capabilities](#customer-ai-capabilities)
+ [Features only available in Connect Customer](#connect-customer-only-features)
+ [Updating an existing instance to Connect Customer](#how-to-enable-ac)
+ [How to switch to Customer Basic](#how-to-disable-ac)

## AI capabilities
<a name="customer-ai-capabilities"></a>

Connect Customer embeds AI at every stage of the customer journey. The following capabilities are included with Connect Customer.
+ **End-customer self-service** — agentic voice and agentic chat powered by AI agents
+ **Generative speech** — Amazon Polly generative voices and third-party speech-to-text (STT) and text-to-speech (TTS) model configuration
+ **Real-time agent assistance** — AI-powered recommendations and next-best-action guidance during live conversations
+ **Conversational analytics and post-contact summaries** — sentiment analysis, theme detection, and automated summaries across voice, chat, messaging, and email
+ **AI-powered case summarization** — automatically generated case summaries to accelerate resolution
+ **Performance evaluations** — evaluate both human agents and self-service interactions
+ **Forecasting and agent scheduling** — predict contact volumes and optimize agent schedules
+ **Flow designer analytics** — insights into contact flow performance

## Features only available in Connect Customer
<a name="connect-customer-only-features"></a>

The following features are only available in Connect Customer. They are not included in Connect Customer Basic.
+ [Agentic customer experience designer (ACXD)](acxd.md)
  + No-code visual canvas
  + Blended AI logic — agentic AI reasoning and deterministic AI
  + Live sync of web or mobile app during live voice or chat
+ [Agentic voice](agentic-voice.md)
  + 50\+ languages
  + 100\+ voices
  + Third-party speech-to-text (STT) and text-to-speech (TTS) model support
+ [AI agent observability](monitor-ai-agent-performance.md)
  + Out-of-the-box AI agent performance metrics evaluated using LLM-as-a-judge
+ [AI assistant for natural language configuration](connect-assistant-ui-builder.md)
  + Step-by-step guides
  + Workspace pages
+ Queue management
  + [Contact estimated wait time](get-queue-metrics.md#get-metrics-tips)
  + [Customer-first callbacks](customer-first-cb.md) — dials the customer first and only offers the callback to an agent if the customer answers the call
+ [Conversational analytics](analyze-conversations.md)
  + Email conversational analytics, including:
    + Sensitive data redaction
    + Summarization
    + Categorization
    + Rules-based actions
  + Case summarization
  + Information extraction
    + Rules-based information extraction for voice and chat contacts
  + Recording ingestion and conversational analytics
+ [Performance evaluations](evaluations.md)
  + Self-service interaction evaluations
  + AI agent performance evaluations
+ [Flow designer analytics](monitor-flow-performance.md)
+ [Custom metrics in dashboards and APIs](custom-metrics-topic.md) — build tailored views of contact center performance

## Updating an existing instance to Connect Customer
<a name="how-to-enable-ac"></a>

All new instances are Connect Customer instances.

If your Connect Customer instance was created before Connect Customer was available, you might need to update your instance to Connect Customer.

1. Log in to the AWS Management Console using your AWS account.

1. In the AWS Management Console, in the search box, type **Connect Customer**. Choose **Connect Customer**.

1. On the **Connect Customer virtual contact center instances** page, choose the **instance alias** where you want to enable Connect Customer.

1. In the navigation pane, choose **Connect Customer**.

1. In the **Enable Connect Customer across your entire instance** section, confirm the status is **Not enabled**.

1. Choose **Enable**.

## How to switch to Customer Basic
<a name="how-to-disable-ac"></a>

Connect Customer Basic does not include all the features available in Connect Customer. If you switch to Connect Customer Basic, you lose access to the features listed in [Features only available in Connect Customer](#connect-customer-only-features), and some capabilities you currently use might no longer be available.

**Warning**  
If features only available in Connect Customer are configured in contact flows and you switch to Connect Customer Basic, you might encounter runtime errors.

Complete the following steps to switch from Connect Customer to Connect Customer Basic for a given Connect Customer instance.

1. Log in to the AWS Management Console using your AWS account.

1. In the AWS Management Console, in the search box, type **Connect Customer**. Choose **Connect Customer**.

1. On the **Connect Customer virtual contact center instances** page, choose the **instance alias** where you want to switch to Customer Basic.

1. In the navigation pane, choose **Connect Customer**.

1. In the **Enable Connect Customer across your entire instance** section, confirm the status is **enabled**.

1. Choose **Disable**.

   A dialog box appears prompting you to confirm that you want to switch to Customer Basic. Choose **Disable** to confirm.