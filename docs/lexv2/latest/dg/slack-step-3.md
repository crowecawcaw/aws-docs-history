# Step 3: Integrate the Slack

application with the Amazon Lex V2 bot

In this section, integrate the Slack application you created
with the Amazon Lex V2 bot you created by using Channel integrations.

1.  Sign in to the AWS Management Console and open the Amazon Lex console at
    [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2.  From the list of bots, choose the Amazon Lex V2 bot that you
    created.
3.  In the left menu, choose **Channel
    integrations** and then choose **Add
    channel**.
4.  In **Create channel**, do the
    following:
    1. For **Platform**, choose
       **Slack**.
    2. For **Identity policies**, choose
       the AWS KMS key to protect channel information. The
       default key is provided by Amazon Lex V2.
    3. For **Integration
       configuration**, give the channel a name
       and an optional description. Choose the alias that
       points to the version of the bot to use, and choose
       the language that the channel supports.

    ###### Note

    If your bot is available in multiple languages,
    you must create a different channel and a different
    application for each language. 4. For **Additional configuration**,
    enter the following:

        * **Client ID** –
         enter the client ID from Slack.
        * **Client secret** –
         enter the client secret from Slack.
        * **Verification token**
         – enter the verification token from
         Slack.
        * **Success page URL**
         – The URL of the page that Slack
         should open when the user is authenticated.
         Typically you leave this blank.

5.  Choose **Create** to create the
    channel.
6.  Amazon Lex V2 shows the list of channels for your bot. From the
    list, choose the channel that you just created.
7.  From **Callback URL**, record the
    endpoint and the OAuth endpoint.

## Next step

[Step 4: Complete Slack
integration with your Lex V2 bot](slack-step-4.md "slack-step-4.md")
