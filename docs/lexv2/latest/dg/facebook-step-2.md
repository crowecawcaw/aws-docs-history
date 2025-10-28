# Step 2: Integrate Facebook

Messenger with the Amazon Lex V2 bot

In this step you link your Amazon Lex V2 bot with Facebook.

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the list of bots, choose the Amazon Lex V2 bot that you
   created.
3. In the left menu, choose **Channel
   integrations** and then choose **Add
   channel**.
4. In **Create channel**, do the
   following:
   1. For **Platform**, choose
      **Facebook**.
   2. For **Identity policies**, choose
      the AWS KMS key to protect channel information. The
      default key is provided by Amazon Lex V2.
   3. For **Integration
      configuration**, give the channel a name
      and an optional description. Choose the alias that
      points to the version of the bot to use, and choose
      the language that the channel supports.
   4. For **Additional configuration**,
      enter the following:
      - **Alias** – A
        string that identifies the app that is
        calling Amazon Lex V2. You can use any string.
        Record this string, you enter it in the
        Facebook developer console.
      - **Page access token**
        – The page access token that you
        copied from the Facebook developer
        console.
      - **App secret key**
        – The secret key that you copied from
        the Facebook developer console.

   5. Choose **Create**
   6. Amazon Lex V2 shows the list of channels for your bot.
      From the list, choose the channel that you just
      created.
   7. From **Callback URL**, record the
      callback URL. You enter this URL in the Facebook
      developer console.

## Next step

[Step 3: Complete Facebook
integration with your Lex V2 bot](facebook-step-3.md "facebook-step-3.md")
