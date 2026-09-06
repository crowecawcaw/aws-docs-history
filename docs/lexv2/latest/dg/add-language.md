

# Adding a new language to an Amazon Lex V2 bot
<a name="add-language"></a>

You add one or more languages and locales to your bot to enable it to communicate with users in their languages. You define the intents, slots, and slot types separately for each language so that the utterances, prompts, and slot values are specific to the language.

Your bot must contain at least one language.

**To add a language to your bot**

1. Sign in to the AWS Management Console and open the Amazon Lex console at [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/).

1. In the **Bots** section, choose the bot you want to add a language to.

1. In the **Add languages** section, click **View languages**.

1. In the **All languages** section, click **Add language**.

1. In the **Add a new language** section, choose **Add a language from scratch**.

1. In the **Language details** section, choose the language that you want to add.

1. If your bot supports voice interaction, in the **Voice** section, choose the Amazon Polly voice that Amazon Lex V2 uses to communicate with the user. If your bot doesn't support voice, choose **None**.

1. In the **Classification confidence score threshold**section, set the value that Amazon Lex V2 uses to determine whether an intent is correct. You can adjust this value after testing your bot.

1. Choose **Add**.