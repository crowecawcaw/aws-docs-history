End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Accessing Audio Logs in Amazon S3

Amazon Lex stores audio logs for your conversations in an S3 bucket.

###### To access audio logs using the console

1. Open the Amazon Lex console [https://console.aws.amazon.com/lex](https://console.aws.amazon.com/lex "https://console.aws.amazon.com/lex").
2. From the list, choose a bot.
3. Choose the **Settings** tab, then from the left menu
   choose **Conversation logs**.
4. Choose the link under **Audio logs** to access the
   logs for the alias in the Amazon S3 console.
   You can also use the Amazon S3 console or API to access audio logs. You can
   see the S3 object key prefix of the audio files in the Amazon Lex console, or in
   the `resourcePrefix` field in the `GetBotAlias`
   operation response.
