# Getting started with Amazon Nova in the Amazon Bedrock

console

This section describes how to use the playgrounds in the AWS console to submit a
text prompt to Amazon Nova 2 models and generate a text or image response. Before you run the
following examples, you should check that you have fulfilled the following
prerequisites:

###### Prerequisites

- You have an AWS account and have permissions to access a role in that
  account with the necessary permissions for Amazon Bedrock. Otherwise, follow the steps at
  [Getting started with Amazon Bedrock](../../../bedrock/latest/userguide/getting-started.md "../../../bedrock/latest/userguide/getting-started.md").
- If you are accessing the model from a US region, you must use the US CRIS
  endpoint which involves adding the `us` prefix to the model ID (such
  as `us.amazon.nova-2-lite-v1:0`).
- If you are accessing the model from outside of the US, you can either use the
  global CRIS endpoint (such as `global.amazon.nova-2-lite-v1:0`) or
  prefix the region in the model ID (such as
  `us`/`eu`/`jp`).

## Explore the text playground

The following example demonstrates how to use the text playground:

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
2. From the left navigation pane, choose **Chat /
   Text** under **Playgrounds**.
3. Choose **Select model** and select a provider and model.
   For this example, select **Amazon** then select a Amazon Nova 2
   model (such as Nova 2 Lite, or
   Nova 2 Sonic). Then choose **Apply**.
4. Select a default prompt from below the text panel, or enter a prompt into
   the text panel, such as `Describe the purpose of a "hello world"
program in one line`.
5. To explore the image understanding capabilities of Amazon Nova, you can upload
   an image in JPEG, PNG, GIF, or WEBP format that is less than or equal to 25
   MB from your computer. After the image is uploaded, you can ask Amazon Nova about
   the image.
6. To explore the document understanding capabilities of Amazon Nova, you can
   upload documents in CSV, DOC, DOCX, HTML, MD, PDF, TXT, XLS, or XLSX format
   that are less than or equal to 4.5 MB. After the documents are uploaded, you
   can ask Amazon Nova about the documents.
7. To explore the video understanding capabilities of Amazon Nova, you can upload
   one video in MKV, MOV, or MP4 format that is less than or equal to 25 MB
   from your computer. You can use Amazon S3 for videos up to 1 GB. After the video
   is uploaded, you can ask Amazon Nova about the video.
8. Choose **Run** to run inference on the model. The
   generated text appears below your prompt in the text panel.
