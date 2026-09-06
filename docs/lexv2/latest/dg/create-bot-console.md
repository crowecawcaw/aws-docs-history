

# Creating a bot using the Amazon Lex V2 console
<a name="create-bot-console"></a>

You create an Amazon Lex V2 bot to interact with your users to elicit information to accomplish a task. For example, you can create a bot that gathers the information needed to order flowers or to book a hotel room. To create a bot using the AWS Console, start by defining the name, description, and some basic information.

1. Sign in to the AWS Management Console and open the Amazon Lex console at [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/).

1. Choose **Create bot**.

1. In the **Creation method** section, choose **Traditional** and then select **Create a blank bot**.

1. In the **Bot configuration** section, give the bot a name and an optional description.

1. In the **IAM permissions** section, choose an AWS Identity and Access Management (IAM) role that provides Amazon Lex V2 permission to access other AWS services, such as Amazon CloudWatch. You can have Amazon Lex V2 create the role, or you can choose an existing role with CloudWatch permissions. 

1. In the **Children's Online Privacy Protection Act (COPPA)** section, choose the appropriate response.

1. In the **Idle session timeout** section, choose the duration that Amazon Lex V2 keeps a session with a user open. Amazon Lex V2 maintains session variables for the duration of the session so that your bot can resume a conversation with the same variables.

1. In the **Advanced settings** (optional) section, add tags that help identify the bot, control access and monitor resources.

1. Choose **Next** to create the bot and move to adding a language.