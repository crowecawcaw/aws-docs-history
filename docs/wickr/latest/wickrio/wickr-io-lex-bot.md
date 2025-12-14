This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Wickr IO lex bot

## Prerequisites

Before you start, be sure to complete the following before continuing with this
guide:

- Follow steps 1 and 2 in [Quick start](quick-start.md "quick-start.md") to get ready to start the bot
  container.
- Set up AWS CLI, or an AWS credentials file with valid current credentials on your host
  machine. For additional information on how to get credentials, see: [Authentication and access credentials for the AWS CLI](../../../cli/v1/userguide/cli-chap-authentication.md "../../../cli/v1/userguide/cli-chap-authentication.md")
  - For this example, we will assume that the credentials on your host exist at
    `/home/ubuntu/credentials/lex/.aws`. This assumes that your username is ubuntu
    and that you have stored your credentials in the file
    `~/credentials/lex/.aws/credentials`.
  - For long term credentials be sure to follow best practices as outlined in [Authentication and access credentials for the AWS CLI](../../../cli/v1/userguide/cli-chap-authentication.md "../../../cli/v1/userguide/cli-chap-authentication.md").
  - Make sure to collect the following pieces of information
    - Bot ID
    - Deployment Alias ID

## Deploy lex bot

Complete the following procedure to deploy a lex bot.

**Step 1: Deploy and configure**

1. Deploy and configure `wickrio-rekognition-bot` container on your host. For
   more information, see [wickrio-lex-bot](https://www.npmjs.com/package/@wickr-sample-integrations/wickrio-lex-bot "https://www.npmjs.com/package/@wickr-sample-integrations/wickrio-lex-bot") .
2. Start the docker image on your host

```
docker run -v ~/WickrIO:/opt/WickrIO -v /home/ubuntu/
        credentials/lex/.aws:/home/wickriouser/.aws -ti public.ecr.aws/
        x3s2s6k3/wickrio/bot-cloud:latest
```

3. Select your preference for the welcome message.

![The Wickr IO welcome message prompt.](/images/wickr/latest/wickrio/images/wickrio-welcome-message-prompt.png) 4. At the **Enter command:** prompt, enter the command
**add**.

![The Wickr IO lex bot add command.](images/wickrio-lex-add.png) 5. Over the next several prompts, enter the username and password created in the previous
steps.

![The Wickr IO lex bot credentials prompt.](images/wickrio-lex-credentials.png) 6. You are prompted to select an integration. Type
`@wickr-sample-integrations/wickrio-lex-bot` 7. Next, you are prompted for the AWS Region, and for the name of your profile in your
credentials file that you set up earlier. If you are unsure of the AWS Region, you can use
US East (N. Virginia). AWS Wickr is available in the following regions: [AWS Wickr Regional availability](../adminguide/what-is-wickr.md#regional-availability "../adminguide/what-is-wickr.md#regional-availability").

![The Wickr IO lex bot region selection.](images/wickrio-lex-region.png)

**Step 2: Start the bot**

1. Use the **list** command to view a list of available bots.
2. Using the number of the bot that you just created (0 in the example), type the command
   **start #**, where # is the bot number (0 in the example).
3. Enter the password for the bot.
4. Use the **list** command to verify that the bot is running.

**Step 3: Interact with the bot**

1. In the top right corner of the navigation panel, select the new message button.

![The Wickr IO new message image.](images/wickrio-new-message.png) 2. In the pop up menu, choose **New Direct Message**. 3. Search for your bot by display name.

![The Wickr IO lex bot search.](images/wickrio-lex-search.png) 4. Select your bot for a direct message, and send a message.

![The Wickr IO lex bot conversation.](images/wickrio-lex-conversation.png)
