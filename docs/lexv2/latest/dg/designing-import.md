# Importing conversation

transcripts

Importing conversation transcripts is a three-step process:

1. Prepare the transcripts for importing by converting them
   to the correct format. If you are using Contact Lens for
   Amazon Connect the transcripts are already in the correct format.
2. Upload the transcripts to an Amazon S3 bucket. If you are using
   Contact Lens, your transcripts are already in an S3
   bucket.
3. Analyze the transcripts using the Amazon Lex V2 console or API
   operations. The time that it takes to complete training
   depends on the volume of transcripts and the complexity of
   the conversation. Typically, 500 lines of transcripts are
   analyzed every minute.
   Each of these steps is described in the following sections.

## Importing transcripts from

Contact Lens for Amazon Connect

The Amazon Lex V2 automated chatbot designer is compatible with
Contact Lens transcript files. To use Contact Lens transcript
files, you must turn on Contact Lens and note the location of
its output files.

###### To export transcripts from Contact Lens

1. Turn on Contact Lens in your Amazon Connect instance. For
   instructions, see [Enable Contact Lens for Amazon Connect](../../../connect/latest/adminguide/enable-analytics.md "../../../connect/latest/adminguide/enable-analytics.md") in the
   _Amazon Connect administrator
   guide_.
2. Note the location of the S3 bucket that Amazon Connect is using
   for your instance. To see the location, open the
   **Data storage** page in the Amazon Connect
   console. For instructions, see [Update instance settings](../../../connect/latest/adminguide/update-instance-settings.md "../../../connect/latest/adminguide/update-instance-settings.md") in the
   _Amazon Connect administrator
   guide_.

After you have turned on Contact Lens and noted the location
of your transcript files, go to [Analyze your transcripts using
Amazon Lex V2 console](#import-import "#import-import") for instructions to import
and analyze your transcripts.

## Prepare transcripts

Prepare your transcripts by creating transcript files.

- Create one transcript file per conversation listing
  the interaction between the parties. Each interaction in
  the conversation can span multiple lines. You can
  provide both redacted and non-redacted versions of the
  conversation.
- The file must be in the JSON format specified in [Input transcript
  format](designing-input-format.md "designing-input-format.md").
- You must provide at least 1,000 conversational turns.
  To improve the discovery of your intents and slot types,
  you should provide around 10,000 or more conversational turns.
  The automated chatbot designer will only process the first 700,000 turns.
- There is no limit to the number of transcript files that
  you can upload, nor is there a file size restriction.

If you plan to filter the transcripts that you import by date,
the files must be in the following directory structure:

```
<path or bucket root>
   --> yyyy
      --> mm
         --> dd
            --> transcript files
```

The transcript file must contain the date in the format
"yyyy-mm-dd" somewhere in the file name.

###### To export transcripts from other contact center

applications

1. Use your contact center application's tools to export
   conversations. The conversation must contain at least
   the information specified in [Input transcript
   format](designing-input-format.md "designing-input-format.md").
2. Transform the transcripts produced by your contact
   center application to the format described in [Input transcript
   format](designing-input-format.md "designing-input-format.md"). You are
   responsible for performing the transformation.

We provide three scripts for preparing transcripts. They
are:

- A script to combine Contact Lens transcripts with
  Amazon Lex V2 conversation logs. Contact Lens transcripts don't
  include parts of Amazon Connect conversations that interact with
  Amazon Lex V2 bots. The script requires conversation logs to be
  turned on for Amazon Lex V2, and appropriate permissions to
  query conversation log CloudWatch Logs and Contact Lens
  S3 buckets.
- A script to transform Amazon Transcribe call analytics to the
  Amazon Lex V2 input format.
- A script to transform Amazon Connect chat transcripts to the
  Amazon Lex V2 input format.

You can download the scripts from this GitHub repository:
[https://github.com/aws-samples/amazon-lex-bot-recommendation-integration](https://github.com/aws-samples/amazon-lex-bot-recommendation-integration "https://github.com/aws-samples/amazon-lex-bot-recommendation-integration") .

## Upload your transcripts to an S3

bucket

If you are using Contact Lens, your transcript files are
already contained in an S3 bucket. For the location and file
names of your transcript files, see [Example Contact Lens output files](../../../connect/latest/adminguide/contact-lens-example-output-files.md "../../../connect/latest/adminguide/contact-lens-example-output-files.md") in the
_Amazon Connect administrator guide_.

If you are using another contact center application and you
have not set up an S3 bucket for your transcript files, follow
this procedure. Otherwise, if you have an existing S3 bucket,
after logging in to the Amazon S3 console, follow this procedure
starting with step 5.

###### To upload files to an S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. Give the bucket a name and choose a Region. The Region
   must be the same one that you use for Amazon Lex V2. Set the
   other options as required for your use case.
4. Choose **Create bucket**.
5. From the list of buckets, choose an existing bucket or
   the bucket that you just created
6. Choose **Upload**.
7. Add the transcript files that you want to
   upload.
8. Choose **Upload**.

## Analyze your transcripts using

Amazon Lex V2 console

You can only use automated bot design in an empty language.
You can add a new language to an existing bot, or create a new
bot.

###### To create a new language in a new bot

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. Choose **Create bot**
3. Choose **Start with Automated Chatbot Designer**.
   Fill out the information to create your new bot.
4. Choose **Next**
5. In **Add language to bot** fill out
   the information for the language.
6. In the **Transcript file location on
   S3** section, choose the S3 bucket that
   contains your transcript files and the local path to the
   files if necessary.
7. You can optionally choose the following:
   - A AWS KMS key to encrypt the transcript data
     during processing. If you don't select a key, a
     service AWS KMS key is used.
   - To filter the transcripts to a specific date
     range. If you choose to filter the transcripts,
     they must be in the correct folder structure.
     For more information, see [Prepare transcripts](#import-prepare "#import-prepare").

8. Choose **Done**.

Wait for Amazon Lex V2 to process the transcript. You see a
completion message when the analysis is complete.

**How to stop analyzing your
transcript**

In case you need to stop the analysis of the transcripts
you have uploaded, you can stop a running `BotRecommendation` job,
which has a `BotRecommendationStatus` status as
processing. You can click on the **Stop processing**
button present on the banner after submitting a job from the
console or by using CLI SDK for the `StopBotRecommendation`
API. For more information,
see [StopBotRecommendation](../APIReference/API_StopBotRecommendation.md "../APIReference/API_StopBotRecommendation.md")

After calling the `StopBotRecommendation`, the internal
`BotRecommendationStatus` is set to `Stopping`
and you are not charged. To make sure the job has stopped, you can call
the `DescribeBotRecommendation` API and verify that the
`BotRecommendationStatus` is `Stopped`.
This usually takes 3-4 minutes.

You are not charged for the processing after the
`StopBotRecommendation` API is called.
