

# Enable assisted slot resolution in the Generative AI configuration screen
<a name="assisted-slot-genai"></a>

You can enable assisted slot resolution for supported built-in slots by navigating to the Generative AI screen.

If the slot is an supported built-in slot, you will have the option to activate the assisted slot resolution at the slot level.

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home).

1. In the navigation pane under **Bots**, select the bot you want to use for assisted slot resolution.

1. Select the language **English (US**) for the bot you want to enable.

1. Go to the **Generative AI configuration** section on the screen.

1. Select **Go to Amazon Bedrock** to sign up and enable the feature, if the feature has not been enabled.
**Note**  
If you do not have access to Amazon Bedrock foundation models, you should see **Go to Amazon Bedrock**. Click on **Go to Amazon Bedrock** to go to the Amazon Bedrock page where you can sign up for access to foundation models. Assisted slot resolution currently supports Anthropic Claude. We suggest using Anthropic Claude for best results.

1. If you already have access to Amazon Bedrock Foundation models, you should see a **Configure** button. Click on this button to go the generative AI configuration page to activate generative AI features in Lex.  
![Image of configure button for generative AI.](http://docs.aws.amazon.com/lexv2/latest/dg/images/assist-slot/assist-slot-genai.png)

1. In the upper right corner of the box, move the slider to the right to choose the **Enabled** setting.

1. Choose the **Enable** button to activate assisted slot resolution for the selected slots.

1. You can disable assisted slot resolution by selecting the slots from the list and selecting the **Disable** button.