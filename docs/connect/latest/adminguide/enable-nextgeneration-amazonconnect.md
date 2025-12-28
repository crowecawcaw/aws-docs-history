# Amazon Connect pricing

Amazon Connect is an AI-powered contact center solution that turns every customer
touchpoint into a deeper relationship and better outcome.

When you create an Amazon Connect instance, unlimited AI pricing is enabled.

Amazon Connect unlimited AI pricing provides unlimited use of Amazon Connect AI capabilities that power customer self-service,
agent assistance, and supervisor experiences. It allows you to optimize every step of your
customer journey without cost-driven compromises.

For more information, visit [Amazon Connect Pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/").

###### Contents

- [How Amazon Connect billing works](#how-ac-billing-works "#how-ac-billing-works")
- [Amazon Connect pricing options](#bestpractices-ac-billing "#bestpractices-ac-billing")
- [How to disable unlimited AI pricing](#how-to-disable-ac "#how-to-disable-ac")
- [How to enable unlimited AI pricing](#how-to-enable-ac "#how-to-enable-ac")

## How Amazon Connect billing works

Amazon Connect is a pay-as-you-go customer experience solution that makes it simple to leverage native AI in every touchpoint across all channels. There are no required minimum monthly fees, long-term commitments, or upfront license charges, and pricing is not based on peak capacity, agent seats, or maintenance; you only pay for what you use. This flexible pricing model enables you to scale up and down depending on seasonality and the needs of your business, without worrying about capacity constraints or licensing costs.

For global resiliency pricing, contact your AWS Technical Account Manager or Solutions Architect.

## Amazon Connect pricing options

There are two pricing models available: unlimited AI pricing and per feature pricing.
You can select a different pricing model for each Amazon Connect instance and change that selection at any time, giving you the flexibility to choose the option that best suits your needs.

**Unlimited AI pricing** is the default option. It enables
you to use an all-inclusive channel pricing model that covers all optimization
features, including:

- Conversational analytics
- Performance evaluations
- Screen recording
- Agent scheduling tools
- AI-powered voice and chat through Amazon Lex and Amazon Q in Connect
- AI-powered generative voice for text-to-speech (TTS) in Amazon Connect

###### Note

We recommend reviewing [Service Improvement and how to opt out from using your data for service improvement](data-opt-out.md "data-opt-out.md") to learn which Amazon Connect services use your
customer's data to train machine learning models, and how you can opt
out.

- OR -

**Per feature pricing** where you pay separately for channels and any optimization features you choose to use.

## How to disable unlimited AI pricing

Complete the following steps to disable unlimited AI pricing and instead use per feature pricing for a given Amazon Connect instance.

1. Log in to the AWS Management Console using your AWS account.
2. In the AWS Management Console, in the search box, type
   **Amazon Connect**. Choose **Amazon Connect**.
3. On the **Amazon Connect virtual contact center instances** page,
   choose the **instance alias** where you want to disable unlimited AI pricing.
4. In the navigation pane, choose **Amazon Connect**.
5. In the **Enable unlimited AI pricing across your entire contact center** section,
   confirm the status is **enabled**.
6. Choose **Disable**.

A dialog box appears prompting you to confirm that you want to disable unlimited AI pricing and instead
use the per feature pricing model. Choose **Disable** to confirm.

###### Warning

Disabling unlimited AI pricing will not disable the individual features used. If those features continue to be used after unlimited AI pricing is disabled, you will be charged based on each individual feature's price.

Exception: If you are using the [customer first callback](setup-queued-cb.md "setup-queued-cb.md") feature, it is disabled when you choose to disable unlimited AI pricing.

## How to enable unlimited AI pricing

If you have disabled unlimited AI pricing and want to enable again, or you
created your Amazon Connect before this option was released, here's how you can enable it now.
Also use these steps if you want to verify if unlimited AI pricing is enabled.

Complete the following steps to enable unlimited AI pricing for a given Amazon Connect instance.

1. Log in to the AWS Management Console using your AWS account.
2. In the AWS Management Console, in the search box, type
   **Amazon Connect**. Choose **Amazon Connect**.
3. On the **Amazon Connect virtual contact center instances** page,
   choose the **instance alias** where you want to enable unlimited AI pricing.
4. In the navigation pane, choose **Amazon Connect**.
5. In the **Enable unlimited AI pricing across your entire contact center** section,
   confirm the status is **Not enabled**.
6. Choose **Enable**.

###### Warning

When you enable unlimited AI, any active free trials of Amazon Connect features end, such as free
trials of conversational analytics, performance evaluation, and agent scheduling.
