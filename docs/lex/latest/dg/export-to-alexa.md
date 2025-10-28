End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Exporting to an Alexa Skill

You can export your bot schema in a format compatible with an Alexa skill. After you
export the bot to a JSON file, you upload it to Alexa using the skill builder.

###### To export a bot and its schema (interaction model)

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. Choose the bot that you want to export.
3. For **Actions**, choose **Export**.
4. Choose the version of the bot that you want to export. For the format, choose
   **Alexa Skills Kit**, then choose
   **Export**.
5. If a download dialog box appears, choose a location to save the file, then
   choose **Save**.
   The downloaded file is a .zip archive containing one file with the name of the
   exported bot. It contains the information necessary to import the bot as an Alexa
   skill.

###### Note

Amazon Lex and the Alexa Skills Kit differ in the following ways:

- Session attributes, denoted by square brackets ([]), are not supported by
  the Alexa Skills Kit. You need to update prompts that use session
  attributes.
- Punctuation marks are not supported by the Alexa Skills Kit. You need to
  update utterances that use punctuation.

###### To upload the bot to an Alexa Skill

1. Log in to the developer portal at [https://developer.amazon.com/](https://developer.amazon.com/edw/home.html#/ "https://developer.amazon.com/edw/home.html#/").
2. On the **Alexa Skills** page, choose **Create
   Skill**.
3. On the **Create a new skill** page, enter a skill name and
   the default language for the skill. Make sure that **Custom**
   is selected for the skill model, and then choose **Create
   skill**.
4. Make sure that **Start from scratch** is selected and the
   choose **Choose**.
5. From the left menu, choose **JSON Editor**. Drag the JSON
   file that you exported from Amazon Lex to the JSON editor.
6. Choose **Save Model** to save your interaction model.
   After uploading the schema into the Alexa skill, make changes necessary for running
   the skill with Alexa. For more information about creating an Alexa skill, see [Use the Skill Builder (Beta)](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/ask-define-the-vui-with-gui "https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/ask-define-the-vui-with-gui") in the _Alexa Skills Kit_.
