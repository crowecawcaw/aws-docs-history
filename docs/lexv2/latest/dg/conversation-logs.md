

# Logging conversations with conversation logs in Lex V2
<a name="conversation-logs"></a>

You enable *conversation logs* to store bot interactions. You can use these logs to review the performance of your bot and to troubleshoot issues with conversations. You can log text for the [RecognizeText](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html) operation. You can log both text and audio for the [RecognizeUtterance](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html) operation. By enabling conversation logs, you get a detailed view of conversations that users have with your bot.

For example, a session with your bot has a session ID. You can use this ID to get the transcript of the conversation including user utterances and the corresponding bot responses. You also get metadata such as intent name and slot values for an utterance.

**Note**  
You can't use conversation logs with a bot subject to the Children's Online Privacy Protection Act (COPPA).

Conversation logs are configured for an alias. Each alias can have different settings for their text and audio logs. You can enable text logs, audio logs, or both for each alias. Text logs store text input, transcripts of audio input, and associated metadata in CloudWatch Logs. Audio logs store audio input in Amazon S3. You can enable encryption of text and audio logs using AWS KMS customer managed CMKs.

To configure logging, use the console or the [CreateBotAlias](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotAlias.html) or [UpdateBotAlias](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotAlias.html) operation. After enabling conversation logs for an alias, using the [RecognizeText](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html) or [RecognizeUtterance](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html) operation for that alias logs the text or audio utterances in the configured CloudWatch Logs log group or S3 bucket.

**Topics**
+ [IAM Policies for Conversation Logs](conversation-logs-policies.md)
+ [Configuring conversation logs for your Lex V2 bot](conversation-logs-configure.md)
+ [Viewing text logs in Amazon CloudWatch Logs from Lex V2](conversation-logs-cw.md)
+ [Accessing audio logs in Amazon S3](conversation-logs-s3.md)
+ [Monitoring conversation log status with CloudWatch metrics](conversation-logs-monitoring.md)