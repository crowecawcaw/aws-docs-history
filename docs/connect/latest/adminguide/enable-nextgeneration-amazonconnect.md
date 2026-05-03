# Amazon Connect Customer

Amazon Connect Customer is an AI-native solution that helps companies of any scale deliver
exceptional customer experiences at every touchpoint. You can use fully autonomous AI agents,
a blend of AI and human agents working together, or fully human-supported experiences. AI is
embedded across all channels for every customer, with simple per-channel pricing. For more
information, visit [Amazon Connect
Pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/").

###### Contents

- [AI capabilities](#customer-ai-capabilities "#customer-ai-capabilities")
- [Updating existing Amazon Connect instances](#how-to-enable-ac "#how-to-enable-ac")
- [How to switch to Customer Basic](#how-to-disable-ac "#how-to-disable-ac")

## AI capabilities

Amazon Connect Customer embeds AI at every stage of the customer journey. The following
capabilities are included with Amazon Connect Customer.

- **End-customer self-service** — agentic
  voice and agentic chat powered by AI agents
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
- **Generative speech** — Amazon Polly
  generative voices and third-party speech-to-text (STT) and text-to-speech
  (TTS) model configuration
- **Customer first callbacks** — let
  customers request a callback instead of waiting on hold

## Updating existing Amazon Connect instances

All new instances are Amazon Connect Customer instances.

If your Amazon Connect instance was created before Amazon Connect Customer was available, you may need to
update your instance to Amazon Connect Customer.

1. Log in to the AWS Management Console using your AWS account.
2. In the AWS Management Console, in the search box, type
   **Amazon Connect**. Choose **Amazon Connect**.
3. On the **Amazon Connect virtual contact center instances** page,
   choose the **instance alias** where you want to enable
   Amazon Connect Customer.
4. In the navigation pane, choose **Amazon Connect**.
5. In the **Enable Amazon Connect Customer across your entire
   instance** section, confirm the status is **Not
   enabled**.
6. Choose **Enable**.

## How to switch to Customer Basic

Amazon Connect Customer Basic does not include all the AI capabilities available in Amazon Connect
Customer. If you move to Customer Basic, some capabilities you are using today may no longer
be available, including:

- Conversational analytics for email
- AI-powered case summarization
- Performance evaluations of self-service interactions
- Flow designer analytics
- Custom metrics in dashboards and APIs
- Agentic voice with Amazon Nova Sonic
- Third-party speech-to-text (STT) and text-to-speech (TTS) model
  configuration
- Customer first callbacks

###### Warning

If these features are configured in contact flows, you may encounter runtime
errors.

Complete the following steps to switch from Amazon Connect Customer to Customer Basic for a
given Amazon Connect instance.

1. Log in to the AWS Management Console using your AWS account.
2. In the AWS Management Console, in the search box, type
   **Amazon Connect**. Choose **Amazon Connect**.
3. On the **Amazon Connect virtual contact center instances** page,
   choose the **instance alias** where you want to switch to
   Customer Basic.
4. In the navigation pane, choose **Amazon Connect**.
5. In the **Enable Amazon Connect Customer across your entire
   instance** section, confirm the status is
   **enabled**.
6. Choose **Disable**.

A dialog box appears prompting you to confirm that you want to switch to
Customer Basic. Choose **Disable** to confirm.
