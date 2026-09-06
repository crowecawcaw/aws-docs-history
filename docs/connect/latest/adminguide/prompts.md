

# Create prompts in Connect Customer
<a name="prompts"></a>

Prompts are audio files played in call flows. For example, hold music is a prompt. Connect Customer comes with a set of prompts that you can add to your flows. Or, you can add your own recordings. 

We recommend that you align your prompts and routing policies with each other to ensure a smooth call flow for customers.

You can create and manage prompts by using the Connect Customer admin site as described in the topics in this section. Or you can use the [Prompt actions](https://docs.aws.amazon.com/connect/latest/APIReference/prompts-api.html) documented in the *Connect Customer API Reference Guide*. 

**Topics**
+ [How to create prompts](#howto-prompts)
+ [Supported file types](#supported-file-types-for-prompts)
+ [Maximum length for prompts](#max-length-for-prompts)
+ [Bulk upload of prompts not supported in UI, API, or CLI](#bulk-upload-prompts)
+ [Add text-to-speech to prompts in flow blocks in Amazon Polly](text-to-speech.md)
+ [Create dynamic text strings in Play prompt blocks](create-dynamic-text-strings.md)
+ [Dynamically select which prompts to play in Connect Customer](dynamically-select-prompts.md)
+ [Set up prompts to play from an S3 bucket in Connect Customer](setup-prompts-s3.md)
+ [Choose the text-to-speech voice and language for audio prompts in Connect Customer](voice-for-audio-prompts.md)
+ [Use SSML tags to personalize text-to-speech in Amazon Polly](ssml-prompt.md)
+ [SSML tags in a Connect Customer chat conversation](chat-and-ssml-tags.md)
+ [SSML tags supported by Connect Customer](supported-ssml-tags.md)

## How to create prompts
<a name="howto-prompts"></a>

This topic explains how to use the Connect Customer admin website to create prompts. To create prompts programmatically, see [CreatePrompt](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreatePrompt.html) in the *Connect Customer API Reference Guide*. 

1. Log in to Connect Customer using an account that has the following security profile permission:
   + **Numbers and flows**, **Prompts - Create**

1. On the navigation menu, choose **Routing**, **Prompts**.

1. On the **Prompts** page, choose **Add prompt**.

1. On the **Add Prompt** page, enter a name for the prompt. 

1. In the **Description** box, describe the message. We recommend using this box to provide a detailed description of the prompt. It is helpful for accessibility.

1. Choose the following actions:
   + **Upload**—Select **Choose File** to upload a .wav file that you have legal permission to use. 
   + **Record**—Choose **Start recording** and speak into your microphone to record a message. Choose **Stop recording** when you're finished. You can choose **Crop** to cut sections of the recorded prompt or choose **Clear recording** to record a new prompt.

1. In the **Prompt Settings** section, enter any tags you want to use to manage the prompt. 

   For example, you might have a department that manages prompts for greetings. You can tag those prompts so users can focus on only those recordings that pertain to them. 

1. Optionally, add tags to identify, organize, search for, filter, and control who can access this prompt. For more information, see [Add tags to resources in Connect Customer](tagging.md).

Use the filters on the **Prompts** page to filter the list of prompts by **Name**, **Description**, and **Tags**. To copy the full Amazon Resource Name (ARN) of a prompt with just one choose, choose the **Copy** icon. When you [set up dynamic prompts in a flow](dynamically-select-prompts.md), you'll need to enter the full ARN of the prompt. 

![The prompts page, the filter options, the copy ARN option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/Prompt_cloudscape_Landing_page.png)


## Supported file types
<a name="supported-file-types-for-prompts"></a>

You can upload a pre-recorded .wav file to use for your prompt, or record one in the web application.

We recommend using 8 KHz .wav files that are less than 50 MB and less than 5 minutes long. If you use higher rated audio libraries, such as 16 KHz files, Connect Customer has to down sample them into 8 KHz samples because of PSTN limitations. This might result in low quality audio. For more information, see the following Wikipedia article: [G.711](https://en.wikipedia.org/wiki/G.711). 

## Maximum length for prompts
<a name="max-length-for-prompts"></a>

Connect Customer supports prompts that are less than 50 MB and less than 5 minutes long. 

## Bulk upload of prompts not supported in UI, API, or CLI
<a name="bulk-upload-prompts"></a>

Currently, bulk uploading of prompts is not supported through the Connect Customer console or programmatically using the API or CLI.