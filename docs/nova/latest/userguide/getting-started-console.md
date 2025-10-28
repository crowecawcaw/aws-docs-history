# Getting started with Amazon Nova in the Amazon Bedrock console

This section describes how to use the playgrounds in the AWS console to submit a text
prompt to Amazon Nova models and generate a text or image response. Before you run
the following examples, you should check that you have fulfilled the following
prerequisites:

###### Prerequisites

- You have an AWS account and have permissions to access a role in that account with
  the necessary permissions for Amazon Bedrock. Otherwise, follow the steps at [Getting started with Amazon Bedrock](../../../bedrock/latest/userguide/getting-started.md "../../../bedrock/latest/userguide/getting-started.md").
- You've requested access to the Amazon Nova models. Otherwise, follow the steps at [Request access to an Amazon Bedrock foundation model](../../../bedrock/latest/userguide/getting-started.md#getting-started-model-access "../../../bedrock/latest/userguide/getting-started.md#getting-started-model-access") and request access to **Amazon Nova Lite** and **Amazon Nova Canvas**.
- You're in the US East (N. Virginia) (us-east-1) Region. To change regions, choose the
  Region name at the top right of the console, next to your IAM role. Then select
  US East (N. Virginia) (us-east-1).

###### Topics

- [Requesting model access](#getting-started-access "#getting-started-access")
- [Explore the text playground](#getting-started-text "#getting-started-text")
- [Explore the image playground](#getting-started-image "#getting-started-image")

## Requesting model access

Complete the following steps to request access to Amazon Nova models.

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
2. From the left navigation pane, choose **Model access** under
   **Bedrock configurations**.
3. In **What is model access**, choose **Enable specific models**.
4. Choose **Nova Lite** and **Nova Canvas** from the **Base models** list. The examples in this section use only these two models, but you can request access to all of the Amazon Nova models. Then choose **Next**
5. On the **Review and submit** page, choose **Submit**.
6. Refresh the **Base models** table. If you will see the Amazon Nova models in the **Access granted** status you are ready to proceed to the next parts of the example.

Note that the region from which you request model access is the only region from which you can use the models.

## Explore the text playground

The following example demonstrates how to use the text playground:

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
2. From the left navigation pane, choose **Chat / Text** under
   **Playgrounds**.
3. Choose **Select model** and select a provider and model. For this
   example, select **Amazon** then **Nova Lite**. Then choose
   **Apply**
4. Select a default prompt from below the text panel, or enter a prompt into the text
   panel, such as `Describe the purpose of a "hello world" program in one
line`.
5. To explore the image understanding capabilities of Amazon Nova, you can upload an
   image in JPEG, PNG, GIF, or WEBP format that is less than or equal to 25 MB from your computer. After the
   image is uploaded, you can ask Amazon Nova about the image.
6. To explore the document understanding capabilities of Amazon Nova, you can upload a
   documents in CSV, DOC, DOCX, HTML, MD, PDF, TXT, XLS, or XLSX format that is less than
   or equal to 4.5 MB. After the documents are uploaded, you can ask Amazon Nova about the
   documents.
7. To explore the video understanding capabilities of Amazon Nova, you can upload one
   video in MKV, MOV, or MP4 format that is less than or equal to 25 MB from your computer. You can use Amazon S3
   for videos up to 1 GB. After the video is uploaded, you can ask Amazon Nova about the
   video.
8. Choose **Run** to run inference on the model. The generated text
   appears below your prompt in the text panel.

## Explore the image playground

The following example demonstrates how to use the image playground.

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
2. From the left navigation pane, choose **Image / Video** under
   **Playgrounds**.
3. Choose **Select model** and select a provider and model. For this
   example, select **Amazon** then select **Nova Canvas**. Then choose
   **Apply**
4. Select a default prompt from below the text panel, or enter a prompt into the text
   panel, such as `Generate an image of happy cats`.
5. In the **Configurations** pane, change the **Number of
   images** to `1`.
6. Choose **Run** to run inference on the model. The generated image
   appears above the prompt.
