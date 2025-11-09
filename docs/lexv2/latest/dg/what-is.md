# What is Amazon Lex V2?

Amazon Lex V2 is an AWS service for building conversational interfaces for
applications using voice and text. Amazon Lex V2 provides the deep
functionality and flexibility of natural language understanding (NLU)
and automatic speech recognition (ASR) so you can build highly engaging
user experiences with lifelike, conversational interactions, and create
new categories of products.

Amazon Lex V2 enables any developer to build conversational bots quickly.
With Amazon Lex V2, no deep learning expertise is necessary—to create a
bot, you specify the basic conversation flow in the Amazon Lex V2 console.
Amazon Lex V2 manages the dialog and dynamically adjusts the responses in the
conversation. Using the console, you can build, test, and publish your
text or voice chatbot. You can then add the conversational interfaces to
bots on mobile devices, web applications, and chat platforms (for
example, Facebook Messenger).

Amazon Lex V2 provides integration with AWS Lambda, and you can integrate with
many other services on the AWS platform, including Amazon Connect, Amazon Comprehend, and
Amazon Kendra. Integration with Lambda provides bots access to pre-built
serverless enterprise connectors to link to data in SaaS applications
such as Salesforce.

For bots created after August 17, 2022, you can use conditional branching to
control the conversation flow with your bot. With conditional branching
you can create complex conversations without needing to write Lambda
code.

Amazon Lex V2 provides the following benefits:

- **Simplicity** – Amazon Lex V2
  guides you through using the console to create your own bot in
  minutes. You supply a few example phrases, and Amazon Lex V2 builds a
  complete natural language model through which the bot can
  interact using voice and text to ask questions, get answers, and
  complete sophisticated tasks.
- **Democratized deep learning
  technologies** – Amazon Lex V2 provides ASR and NLU
  technologies to create a Speech Language Understanding (SLU)
  system. Through SLU, Amazon Lex V2 takes natural language speech and
  text input, understands the intent behind the input, and
  fulfills the user intent by invoking the appropriate business
  function.

 

Speech recognition and natural language understanding are some
of the most challenging problems to solve in computer science,
requiring sophisticated deep learning algorithms to be trained
on massive amounts of data and infrastructure. Amazon Lex V2 puts deep
learning technologies within reach of all developers. Amazon Lex V2
bots convert incoming speech to text and understand the user
intent to generate an intelligent response so you can focus on
building your bots with added value for your customers and
define entirely new categories of products made possible through
conversational interfaces.

- **Seamless deployment and
  scaling** – With Amazon Lex V2, you can build, test,
  and deploy your bots directly from the Amazon Lex V2 console. Amazon Lex V2
  enables you to publish your voice or text bots for use on mobile
  devices, web apps, and chat services (for example, Facebook
  Messenger). Amazon Lex V2 scales automatically. You don’t need to worry
  about provisioning hardware and managing infrastructure to power
  your bot experience.
- **Built-in integration with the AWS
  platform** – Amazon Lex V2 operates natively with
  other AWS services, such as AWS Lambda and Amazon CloudWatch. You can take
  advantage of the power of the AWS platform for security,
  monitoring, user authentication, business logic, storage, and
  mobile app development.
- **Cost-effectiveness** –
  With Amazon Lex V2, there are no upfront costs or minimum fees. You are
  charged only for the text or speech requests that are made. The
  pay-as-you-go pricing and the low cost per request make the
  service a cost-effective way to build conversational interfaces.
  With the Amazon Lex V2 free tier, you can easily try Amazon Lex V2 without any
  initial investment.

## Paying for

Amazon Lex V2 charges you only for the text or speech requests that you make. This model gives you a variable-cost service that can grow with your business while giving you the cost advantages of the AWS infrastructure. For more information, see [Pricing](https://aws.amazon.com/lex/pricing "https://aws.amazon.com/lex/pricing").

When you sign up for AWS, your AWS account is automatically signed up for all services in AWS, including . However, you are charged only for the services that you use. If you are a new customer, you can get started with for free. For more information, see [AWS free tier](https://aws.amazon.com/free "https://aws.amazon.com/free").

To see your bill, go to the Billing and Cost Management Dashboard in the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/"). To learn more about AWS account billing, see the [_AWS Billing User Guide_](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md"). If you have
questions concerning AWS billing and AWS accounts, contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Are You a First-time User of

Amazon Lex V2?

If you are a first-time user of Amazon Lex V2, we recommend that you read
the following sections in order:

1. **[Amazon Lex V2 core concepts](how-it-works.md "how-it-works.md")** –
   This section introduces Amazon Lex V2 and the features that you use
   to create a chatbot.
2. **[Getting started with Amazon Lex V2](getting-started.md "getting-started.md")** –
   In this section, you set up your account and test Amazon Lex V2.
3. **[API Reference](../APIReference/welcome.md "../APIReference/welcome.md")** – This section contains details about API operations.

## Using Amazon Lex V2 with an AWS SDK

Beyond the console interface, Amazon Lex V2 provides comprehensive programmatic access through AWS SDKs. This enables you to integrate conversational AI capabilities directly into your applications, automate bot management tasks, and build scalable solutions.

When you use an AWS SDK with Amazon Lex V2, you can:

- **Automate bot creation and management** – Programmatically create, update, and deploy bots without manual console interaction
- **Integrate with existing applications** – Add conversational interfaces to web applications, mobile apps, and enterprise systems
- **Scale bot operations** – Manage multiple bots, intents, and slot types efficiently through code
- **Implement custom workflows** – Build sophisticated conversation flows that integrate with your business logic

The table below shows the AWS SDKs that support Amazon Lex V2 operations. Choose the SDK that matches your development environment and follow the provided links to get started with installation and implementation.

| Programming Language | AWS SDK                    | Getting Started Resources                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Java                 | AWS SDK for Java 2.x       | [Developer Guide](../../../sdk-for-java/latest/developer-guide.md "../../../sdk-for-java/latest/developer-guide.md")<br>[API Reference](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/lexmodelsv2/package-summary.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/lexmodelsv2/package-summary.html")                                 |
| Python               | AWS SDK for Python (Boto3) | [Getting Started](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html")<br>[API Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html") |
| JavaScript/Node.js   | AWS SDK for JavaScript v3  | [Developer Guide](../../../sdk-for-javascript/v3/developer-guide.md "../../../sdk-for-javascript/v3/developer-guide.md")<br>[API Reference](../../../AWSJavaScriptSDK/v3/latest/clients/client-lex-models-v2.md "../../../AWSJavaScriptSDK/v3/latest/clients/client-lex-models-v2.md")                                                                                                           |
| .NET/C#              | AWS SDK for .NET           | [Developer Guide](../../../sdk-for-net/latest/developer-guide.md "../../../sdk-for-net/latest/developer-guide.md")<br>[API Reference](../../../sdkfornet/v3/apidocs/items/LexModelsV2/NLexModelsV2.md "../../../sdkfornet/v3/apidocs/items/LexModelsV2/NLexModelsV2.md")                                                                                                                         |
| Go                   | AWS SDK for Go v2          | [Developer Guide](https://aws.github.io/aws-sdk-go-v2/docs/ "https://aws.github.io/aws-sdk-go-v2/docs/")<br>[API Reference](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lexmodelsv2 "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lexmodelsv2")                                                                                                                           |
| Ruby                 | AWS SDK for Ruby           | [Developer Guide](../../../sdk-for-ruby/v3/developer-guide.md "../../../sdk-for-ruby/v3/developer-guide.md")<br>[API Reference](../../../sdk-for-ruby/v3/api/Aws/LexModelsV2.md "../../../sdk-for-ruby/v3/api/Aws/LexModelsV2.md")                                                                                                                                                               |
| PHP                  | AWS SDK for PHP            | [Developer Guide](../../../sdk-for-php/v3/developer-guide.md "../../../sdk-for-php/v3/developer-guide.md")<br>[API Reference](../../../aws-sdk-php/v3/api/class-Aws.LexModelsV2.md "../../../aws-sdk-php/v3/api/class-Aws.LexModelsV2.md")                                                                                                                                                       |

To get started with any SDK:

1. Install the SDK for your preferred programming language using the installation instructions in the Developer Guide
2. Configure your AWS credentials and region settings
3. Set up the necessary IAM permissions for Amazon Lex V2 operations
4. Review the API Reference documentation for the specific operations you need
5. Start with basic operations like creating a bot or listing existing resources

For detailed examples and step-by-step guidance on creating bots programmatically, see the SDK documentation links provided in the table above.
