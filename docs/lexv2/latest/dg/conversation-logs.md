# Logging conversations with conversation logs in Lex V2

You enable _conversation logs_ to store bot
interactions. You can use these logs to review the performance of your bot
and to troubleshoot issues with conversations. You can log text for the
[RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md") operation. You can log both
text and audio for the [RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md") operation. By enabling
conversation logs, you get a detailed view of conversations that users have
with your bot.

For example, a session with your bot has a session ID. You can use this
ID to get the transcript of the conversation including user utterances and
the corresponding bot responses. You also get metadata such as intent name
and slot values for an utterance.

###### Note

You can't use conversation logs with a bot subject to the Children's
Online Privacy Protection Act (COPPA).

Conversation logs are configured for an alias. Each alias can have
different settings for their text and audio logs. You can enable text logs,
audio logs, or both for each alias. Text logs store text input, transcripts
of audio input, and associated metadata in CloudWatch Logs. Audio logs store audio
input in Amazon S3. You can enable encryption of text and audio logs using AWS KMS
customer managed CMKs.

To configure logging, use the console or the
[CreateBotAlias](../APIReference/API_CreateBotAlias.md "../APIReference/API_CreateBotAlias.md") or [UpdateBotAlias](../APIReference/API_UpdateBotAlias.md "../APIReference/API_UpdateBotAlias.md")
operation. After enabling conversation logs for an alias, using the
[RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md") or [RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md")
operation for that alias
logs the text or audio utterances in the configured CloudWatch Logs log group or S3
bucket.

###### Topics

- [IAM Policies for Conversation
  Logs](conversation-logs-policies.md "conversation-logs-policies.md")
- [Configuring conversation
  logs for your Lex V2 bot](conversation-logs-configure.md "conversation-logs-configure.md")
- [Viewing text logs in Amazon CloudWatch Logs from Lex V2](conversation-logs-cw.md "conversation-logs-cw.md")
- [Accessing audio logs in Amazon S3](conversation-logs-s3.md "conversation-logs-s3.md")
- [Monitoring conversation log
  status with CloudWatch metrics](conversation-logs-monitoring.md "conversation-logs-monitoring.md")
