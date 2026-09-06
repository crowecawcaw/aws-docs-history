

# Create an agent assist intent from a Connect Customer instance
<a name="create-qic-intent-connect"></a>

You can use the generative AI capabilities powered by agent assist for your bot by enabling the [AMAZON.QinConnectIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-qinconnect.html) in your bot. This is an Amazon Lex built-in intent. 

Complete the following steps to enable agent assist.

1. Open the bot for which you want to add the **AMAZON.QinConnectIntent** intent.

1. Navigate to the **Configuration** tab in the bot builder interface.

1. Enable the **AMAZON.QinConnectIntent** intent by setting the toggle to on. The following image shows the location of the toggle.  
![A sample configuration page for an unconfigured bot.](http://docs.aws.amazon.com/connect/latest/adminguide/images/enable-qic-bot.png)

   The **agent assist intent** toggle is only supported for bots created directly within the Connect Customer admin website. To add Amazon Q capabilities to intents for bots created outside of Connect Customer admin website, use the Amazon Lex console to update the configuration.

1. In the **Enable agent assist intent **dialog box, use the dropdown menu to choose the Amazon Resource Name (ARN) of the agent assist intent.  
![A Enable agent assist intent dialog box.](http://docs.aws.amazon.com/connect/latest/adminguide/images/qic-intent-dropdownbox.png)

1. Choose **Confirm** to add **AMAZON.QinConnectIntent** intent support.
**Important**  
You cannot use **AMAZON.QInConnectIntent** along with intents without specific utterances such as **AMAZON.QnAIntent**, **AMAZON.BedrockAgentIntent** in the same bot locale. For more information, see [AMAZON.QinConnectIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-qinconnect.html) in the *Amazon Lex V2 Developer Guide*. 