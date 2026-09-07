

This guide provides documentation for Wickr IO Integrations. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Deploy an existing bot
<a name="deploy-existing-bot"></a>

Complete the following procedure to deploy an existing bot.

**Wickr IO Hello World Bot**

1. Follow Steps 1-3 in [Quick start](quick-start.md) to get the bot container created and running.

1. At the **Enter command:** prompt, enter the command **add**.  
![The Wickr IO demo add command.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickrio-deploy.png)

1. Over the next several prompts, enter the **username** and **password** created in the previously. 

1. Next you are prompted to select an integration. In the sample, we used `@wickr-sample-integrations/wickrio-hello-world-bot`.  
![The Wickr IO sample bot image.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickrio-integration.png)

1. Start the bot by doing the following:

   1. Use the **list** command to view a list of available bots.  
![The Wickr IO list command output.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickrio-list-command.png)

   1. Using the number of the bot that you just created (0 in the example), type the command **start \#**, where \# is the bot number (0 in the example).

   1. Enter the password for the bot.

   1. Wait several seconds, and then use the **list** command again to verify that the bot is running.  
![The Wickr IO start command output.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickrio-start-command.png)

1. Interact with the bot:

   1. Using your Wickr user, choose the **New Direct Message** button.  
![The Wickr IO new message button.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickrio-new-message.png)

   1. In the search bar, search for your bot by display name.  
![The Wickr IO search for bot.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickrio-search-bot.png)

   1. Select your bot for a direct message, and send a message.  
![The Wickr IO bot conversation.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickrio-bot-conversation.png)