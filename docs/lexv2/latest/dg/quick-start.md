

# Quick Start: Create a chatbot in 5 minutes
<a name="quick-start"></a>

This quick start guide helps you create a working Amazon Lex V2 chatbot in just 5 minutes using pre-built templates. You'll have a functional chatbot that you can immediately test and customize for your needs.

## Step 1: Choose a Template
<a name="choose-template"></a>

Amazon Lex V2 provides several pre-built templates for common use cases:
+ **Customer Support FAQ** – Handle common customer service inquiries
+ **Appointment Booking** – Schedule and manage appointments
+ **Order Status** – Check order information and delivery status
+ **IT Helpdesk** – Provide technical support and troubleshooting

**To select a template**

1. Open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/](https://console.aws.amazon.com/lexv2/).

1. Choose **Create bot**.

1. Select **Start with a template**.

1. Choose the **Customer Support FAQ** template for this quick start.

1. Enter a bot name, such as **MyFirstChatbot**.

1. Choose **Create**.

## Step 2: Quick Customization (Optional)
<a name="customize-template"></a>

The template comes pre-configured, but you can quickly customize it for your specific needs:

**To customize your chatbot**

1. In the bot overview, review the pre-configured intents.

1. Choose an intent to modify, such as **GetAccountInfo**.

1. Add your own sample utterances that match how your customers might phrase requests.

1. Update the response messages to match your brand voice.

1. Choose **Save intent**.

## Step 3: Test Your Bot
<a name="test-bot"></a>

Test your chatbot immediately using the built-in test console:

**To test your chatbot**

1. Choose **Build** to compile your bot.

1. Wait for the build to complete (usually 1-2 minutes).

1. In the test console on the right, type: **I need help with my account**

1. Press Enter and observe the bot's response.

1. Try other phrases to test the bot's understanding.

## Step 4: Deploy Your Bot
<a name="deploy-bot"></a>

Once you're satisfied with your chatbot's responses, deploy it for use:

**To deploy your chatbot**

1. Choose **Publish** from the bot actions menu.

1. Create a new version by choosing **Create version**.

1. Create an alias (such as "Production") that points to your version.

1. Choose your integration method.

## Next Steps
<a name="next-steps-quick"></a>

Congratulations\! You now have a working Amazon Lex V2 chatbot. Here's what you can do next:
+ **Enable Assisted NLU** – Improve understanding with AI-powered natural language processing.
+ **Add More Intents** – Expand your chatbot's capabilities with additional use cases.
+ **Integrate with Lambda** – Add business logic and external system integration. See [Integrating an AWS Lambda function into your Amazon Lex V2 bot](lambda.md).
+ **Set Up Monitoring** – Track usage and performance. See [Measuring operational metrics with Amazon CloudWatch](monitoring-cloudwatch.md).
+ **Learn Advanced Features** – Explore conversation flow management, multi-turn dialogs, and context switching.

For a more detailed walkthrough, continue with [Exercise 1: Create a chatbot from a template](exercise-1.md).