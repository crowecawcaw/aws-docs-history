# Step 2: Integrate the Twilio message

service endpoint with the Amazon Lex V2 bot

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
      **Twilio**.
   2. For **Identity policies**, choose
      the AWS KMS key to protect channel information. The
      default key is provided by Amazon Lex V2.
   3. For **Integration
      configuration**, give the channel a name
      and an optional description. Choose the alias that
      points to the version of the bot to use, and choose
      the language that the channel supports.
   4. For **Additional configuration**,
      enter the account SID and authentication token from
      the Twilio dashboard.

5. Choose **Create**.
6. From the list of channels, choose the channel that you
   just created.
7. Copy the **Callback URL**.

## Next step

[Step 3: Complete Twilio
integration between your Lex V2 bot and Twilio](twilio-step-3.md "twilio-step-3.md")
