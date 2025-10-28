# Real-time analysis using the API

The following examples demonstrate how to use Amazon Comprehend API for real-time analysis, using the AWS CLI, and the AWS
SDKs for .NET, Java, and Python. Use the examples to learn about the Amazon Comprehend synchronous operations and as building
blocks for your own applications.

The .NET examples in this section use the [AWS SDK for .NET](../../../sdk-for-net/latest/developer-guide/welcome.md "../../../sdk-for-net/latest/developer-guide/welcome.md"). You can use the [AWS Toolkit for Visual Studio](../../../AWSToolkitVS/latest/UserGuide/welcome.md "../../../AWSToolkitVS/latest/UserGuide/welcome.md") to develop AWS applications
using .NET. It includes helpful templates and the AWS Explorer for deploying
applications and managing services. For a .NET developer perspective of AWS, see the
[AWS guide for .NET developers](../../../sdk-for-net/latest/developer-guide/welcome.md "../../../sdk-for-net/latest/developer-guide/welcome.md").

###### Topics

- [Detecting the dominant language](#get-started-api-dominant-language "#get-started-api-dominant-language")
- [Detecting named entities](#get-started-api-entities "#get-started-api-entities")
- [Detecting key phrases](#get-started-api-key-phrases "#get-started-api-key-phrases")
- [Determining sentiment](#get-started-api-sentiment "#get-started-api-sentiment")
- [Real-time analysis for targeted sentiment](#get-started-api-targeted-sentiment "#get-started-api-targeted-sentiment")
- [Detecting syntax](#get-started-api-syntax "#get-started-api-syntax")
- [Real-time batch APIs](#get-started-batch "#get-started-batch")

## Detecting the dominant language

To determine the dominant language used in text, use the [DetectDominantLanguage](../APIReference/API_DetectDominantLanguage.md "../APIReference/API_DetectDominantLanguage.md")
operation. To detect the dominant language in up to 25 documents in a batch, use the
[BatchDetectDominantLanguage](../APIReference/API_BatchDetectDominantLanguage.md "../APIReference/API_BatchDetectDominantLanguage.md") operation. For more information,
see [Real-time batch APIs](#get-started-batch "#get-started-batch").

###### Topics

- [Using the AWS Command Line Interface](#get-started-api-dominant-language-cli "#get-started-api-dominant-language-cli")
- [Using the AWS SDK for Java, SDK for Python, or SDK for .NET](#get-started-api-dominant-language-java "#get-started-api-dominant-language-java")

### Using the AWS Command Line Interface

The following example demonstrates using the `DetectDominantLanguage`
operation with the AWS CLI.

The example is formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

```
aws comprehend detect-dominant-language \
    --region `region` \
    --text "It is raining today in Seattle."

```

Amazon Comprehend responds with the following:

```
{
    "Languages": [
        {
            "LanguageCode": "en",
            "Score": 0.9793661236763
        }
    ]
}

```

### Using the AWS SDK for Java, SDK for Python, or SDK for .NET

For SDK examples of how to determine the dominant language, see [Use DetectDominantLanguage with an AWS SDK or CLI](example_comprehend_DetectDominantLanguage_section.md "example_comprehend_DetectDominantLanguage_section.md").

## Detecting named entities

To determine the named entities in a document, use the [DetectEntities](../APIReference/API_DetectEntities.md "../APIReference/API_DetectEntities.md") operation. To
detect entities in up to 25 documents in a batch, use the [BatchDetectEntities](../APIReference/API_BatchDetectEntities.md "../APIReference/API_BatchDetectEntities.md")
operation. For more information, see [Real-time batch APIs](#get-started-batch "#get-started-batch").

###### Topics

- [Using the AWS Command Line Interface](#get-started-api-entities-cli "#get-started-api-entities-cli")
- [Using the AWS SDK for Java, SDK for Python, or SDK for .NET](#get-started-api-entities-java "#get-started-api-entities-java")

### Using the AWS Command Line Interface

The following example demonstrates using the `DetectEntities` operation
using the AWS CLI. You must specify the language of the input text.

The example is formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

```
aws comprehend detect-entities \
    --region `region` \
    --language-code "en" \
    --text "It is raining today in Seattle."

```

Amazon Comprehend responds with the following:

```
{
    "Entities": [
        {
            "Text": "today",
            "Score": 0.97,
            "Type": "DATE",
            "BeginOffset": 14,
            "EndOffset": 19
        },
        {
            "Text": "Seattle",
            "Score": 0.95,
            "Type": "LOCATION",
            "BeginOffset": 23,
            "EndOffset": 30
        }
    ],
    "LanguageCode": "en"
}

```

### Using the AWS SDK for Java, SDK for Python, or SDK for .NET

For SDK examples of how to determine the dominant language, see [Use DetectEntities with an AWS SDK or CLI](example_comprehend_DetectEntities_section.md "example_comprehend_DetectEntities_section.md").

## Detecting key phrases

To determine the key noun phrases used in text, use the [DetectKeyPhrases](../APIReference/API_DetectKeyPhrases.md "../APIReference/API_DetectKeyPhrases.md") operation. To
detect the key noun phrases in up to 25 documents in a batch, use the [BatchDetectKeyPhrases](../APIReference/API_BatchDetectKeyPhrases.md "../APIReference/API_BatchDetectKeyPhrases.md")
operation. For more information, see [Real-time batch APIs](#get-started-batch "#get-started-batch").

###### Topics

- [Using the AWS Command Line Interface](#get-started-api-key-phrases-cli "#get-started-api-key-phrases-cli")
- [Using the AWS SDK for Java, SDK for Python, or SDK for .NET](#get-started-api-key-phrases-java "#get-started-api-key-phrases-java")

### Using the AWS Command Line Interface

The following example demonstrates using the `DetectKeyPhrases`
operation with the AWS CLI. You must specify the language of the input text.

The example is formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

```
aws comprehend detect-key-phrases \
    --region `region` \
    --language-code "en" \
    --text "It is raining today in Seattle."

```

Amazon Comprehend responds with the following:

```
{
    "LanguageCode": "en",
    "KeyPhrases": [
        {
            "Text": "today",
            "Score": 0.89,
            "BeginOffset": 14,
            "EndOffset": 19
        },
        {
            "Text": "Seattle",
            "Score": 0.91,
            "BeginOffset": 23,
            "EndOffset": 30
        }
    ]
}
```

### Using the AWS SDK for Java, SDK for Python, or SDK for .NET

For SDK examples that detect key phrases, see [Use DetectKeyPhrases with an AWS SDK or CLI](example_comprehend_DetectKeyPhrases_section.md "example_comprehend_DetectKeyPhrases_section.md").

## Determining sentiment

Amazon Comprehend provides the following API operations for analyzing sentiment:

- [DetectSentiment](../APIReference/API_DetectSentiment.md "../APIReference/API_DetectSentiment.md") – Determines the overall emotional
  sentiment of a document.
- [BatchDetectSentiment](../APIReference/API_BatchDetectSentiment.md "../APIReference/API_BatchDetectSentiment.md")
  – Determine the overall sentiment in up to 25 documents in a batch. For more information, see
  [Real-time batch APIs](#get-started-batch "#get-started-batch")
- [StartSentimentDetectionJob](../APIReference/API_StartSentimentDetectionJob.md "../APIReference/API_StartSentimentDetectionJob.md") –
  Starts an asynchronous sentiment detection job for a collection of documents.
- [ListSentimentDetectionJobs](../APIReference/API_ListSentimentDetectionJobs.md "../APIReference/API_ListSentimentDetectionJobs.md") –
  Returns the list of sentiment detection jobs that you have submitted.
- [DescribeSentimentDetectionJob](../APIReference/API_DescribeSentimentDetectionJob.md "../APIReference/API_DescribeSentimentDetectionJob.md") –
  Gets the properties (including status) associated with the specified sentiment detection job.
- [StopSentimentDetectionJob](../APIReference/API_StopSentimentDetectionJob.md "../APIReference/API_StopSentimentDetectionJob.md") –
  Stops the specified in-progress sentiment job.

###### Topics

- [Using the AWS Command Line Interface](#get-started-api-sentiment-cli "#get-started-api-sentiment-cli")
- [Using the AWS SDK for Java, SDK for Python, or SDK for .NET](#get-started-api-sentiment-java "#get-started-api-sentiment-java")

### Using the AWS Command Line Interface

The following example demonstrates using the `DetectSentiment`
operation with the AWS CLI. This example specifies the language of the input
text.

The example is formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

```
aws comprehend detect-sentiment \
    --region `region` \
    --language-code "en" \
    --text "It is raining today in Seattle."

```

Amazon Comprehend responds with the following:

```
{
    "SentimentScore": {
        "Mixed": 0.014585512690246105,
        "Positive": 0.31592071056365967,
        "Neutral": 0.5985543131828308,
        "Negative": 0.07093945890665054
    },
    "Sentiment": "NEUTRAL",
    "LanguageCode": "en"
}

```

### Using the AWS SDK for Java, SDK for Python, or SDK for .NET

For SDK examples that determine the sentiment of input text, see [Use DetectSentiment with an AWS SDK or CLI](example_comprehend_DetectSentiment_section.md "example_comprehend_DetectSentiment_section.md").

## Real-time analysis for targeted sentiment

Amazon Comprehend provides the following API operations for targeted sentiment real-time analysis:

- [DetectTargetedSentiment](../APIReference/API_DetectTargetedSentiment.md "../APIReference/API_DetectTargetedSentiment.md") – Analyzes sentiment
  of the entities mentioned in a document.
- [BatchDetectTargetedSentiment](../APIReference/API_BatchDetectTargetedSentiment.md "../APIReference/API_BatchDetectTargetedSentiment.md")
  – Analyzes targeted sentiment for up to 25 documents in a batch. For more information, see
  [Real-time batch APIs](#get-started-batch "#get-started-batch")

If the text you are analyzing doesn't include any targeted sentiment [Entity types](how-targeted-sentiment.md#how-targeted-sentiment-entities "how-targeted-sentiment.md#how-targeted-sentiment-entities"), the API returns an
empty Entities array.

### Using the AWS Command Line Interface

The following example demonstrates using the `DetectTargetedSentiment`
operation with the AWS CLI. This example specifies the language of the input
text.

The example is formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

```
aws comprehend detect-targeted-sentiment \
    --region `region` \
    --language-code "en" \
    --text "The burger was cooked perfectly but it was cold. The service was OK."

```

Amazon Comprehend responds with the following:

```
{
"Entities": [
    {
      "DescriptiveMentionIndex": [
        0
      ],
      "Mentions": [
        {
          "BeginOffset": 4,
          "EndOffset": 10,
          "Score": 1,
          "GroupScore": 1,
          "Text": "burger",
          "Type": "OTHER",
          "MentionSentiment": {
            "Sentiment": "POSITIVE",
            "SentimentScore": {
              "Mixed": 0.001515,
              "Negative": 0.000822,
              "Neutral": 0.000243,
              "Positive": 0.99742
            }
          }
        },
        {
          "BeginOffset": 36,
          "EndOffset": 38,
          "Score": 0.999843,
          "GroupScore": 0.999661,
          "Text": "it",
          "Type": "OTHER",
          "MentionSentiment": {
            "Sentiment": "NEGATIVE",
            "SentimentScore": {
              "Mixed": 0,
              "Negative": 0.999996,
              "Neutral": 0.000004,
              "Positive": 0
            }
          }
        }
      ]
    },
    {
      "DescriptiveMentionIndex": [
        0
      ],
      "Mentions": [
        {
          "BeginOffset": 53,
          "EndOffset": 60,
          "Score": 1,
          "GroupScore": 1,
          "Text": "service",
          "Type": "ATTRIBUTE",
          "MentionSentiment": {
            "Sentiment": "NEUTRAL",
            "SentimentScore": {
              "Mixed": 0.000033,
              "Negative": 0.000089,
              "Neutral": 0.993325,
              "Positive": 0.006553
            }
          }
        }
      ]
    }
  ]
}

```

## Detecting syntax

To parse text to extract the individual words and determine the parts of speech for
each word, use the [DetectSyntax](../APIReference/API_DetectSyntax.md "../APIReference/API_DetectSyntax.md")
operation. To parse the syntax of up to 25 documents in a batch, use the
[BatchDetectSyntax](../APIReference/API_BatchDetectSyntax.md "../APIReference/API_BatchDetectSyntax.md") operation.
For more information, see [Real-time batch APIs](#get-started-batch "#get-started-batch").

###### Topics

- [Using the AWS Command Line Interface.](#get-started-api-syntax-cli "#get-started-api-syntax-cli")
- [Using the AWS SDK for Java, SDK for Python, or SDK for .NET](#get-started-api-syntax-java "#get-started-api-syntax-java")

### Using the AWS Command Line Interface.

The following example demonstrates using the `DetectSyntax` operation
with the AWS CLI. This example specifies the language of the input text.

The example is formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret (^).

```
aws comprehend detect-syntax \
   --region `region` \
   --language-code "en" \
   --text "It is raining today in Seattle."
```

Amazon Comprehend responds with the following:

```
{
    "SyntaxTokens": [
        {
            "Text": "It",
            "EndOffset": 2,
            "BeginOffset": 0,
            "PartOfSpeech": {
                "Tag": "PRON",
                "Score": 0.8389829397201538
            },
            "TokenId": 1
        },
        {
            "Text": "is",
            "EndOffset": 5,
            "BeginOffset": 3,
            "PartOfSpeech": {
                "Tag": "AUX",
                "Score": 0.9189288020133972
            },
            "TokenId": 2
        },
        {
            "Text": "raining",
            "EndOffset": 13,
            "BeginOffset": 6,
            "PartOfSpeech": {
                "Tag": "VERB",
                "Score": 0.9977611303329468
            },
            "TokenId": 3
        },
        {
            "Text": "today",
            "EndOffset": 19,
            "BeginOffset": 14,
            "PartOfSpeech": {
                "Tag": "NOUN",
                "Score": 0.9993606209754944
            },
            "TokenId": 4
        },
        {
            "Text": "in",
            "EndOffset": 22,
            "BeginOffset": 20,
            "PartOfSpeech": {
                "Tag": "ADP",
                "Score": 0.9999061822891235
            },
            "TokenId": 5
        },
        {
            "Text": "Seattle",
            "EndOffset": 30,
            "BeginOffset": 23,
            "PartOfSpeech": {
                "Tag": "PROPN",
                "Score": 0.9940338730812073
            },
            "TokenId": 6
        },
        {
            "Text": ".",
            "EndOffset": 31,
            "BeginOffset": 30,
            "PartOfSpeech": {
                "Tag": "PUNCT",
                "Score": 0.9999997615814209
            },
            "TokenId": 7
        }
    ]
}
```

### Using the AWS SDK for Java, SDK for Python, or SDK for .NET

For SDK examples that detect the syntax of input text, see [Use DetectSyntax with an AWS SDK or CLI](example_comprehend_DetectSyntax_section.md "example_comprehend_DetectSyntax_section.md").

## Real-time batch APIs

To send batches of up to 25 documents, you can use the Amazon Comprehend real-time batch operations. Calling
a batch operation is identical to calling the single document APIs for each document in
the request. Using the batch APIs can result in better performance for your
applications. For more information, see [Multiple document synchronous processing](concepts-processing-modes.md#how-batch "concepts-processing-modes.md#how-batch").

###### Topics

- [Batch processing with the AWS CLI](#batch-cli "#batch-cli")
- [Batch processing with the AWS SDK for .NET](#batch-csharp "#batch-csharp")

### Batch processing with the AWS CLI

These examples show how to use the batch API operations using the AWS Command Line Interface. All
of the operations except `BatchDetectDominantLanguage` use the following
JSON file called `process.json` as input. For that operation the
`LanguageCode` entity is not included.

The third document in the JSON file (`"$$$$$$$$"`) will cause an error
during batch processing. It is included so that the operations will include an [BatchItemError](../APIReference/API_BatchItemError.md "../APIReference/API_BatchItemError.md") in the
response.

```
{
   "LanguageCode": "en",
   "TextList": [
      "I have been living in Seattle for almost 4 years",
      "It is raining today in Seattle",
      "$$$$$$$$"
   ]
}
```

The examples are formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

###### Topics

- [Detect the dominant language using a
  batch (AWS CLI)](#batch-dominant-language "#batch-dominant-language")
- [Detect entities using a batch (AWS CLI)](#batch-entities "#batch-entities")
- [Detect key phrases using a batch
  (AWS CLI)](#batch-key-phrase "#batch-key-phrase")
- [Detect sentiment using a batch (AWS CLI)](#batch-sentiment "#batch-sentiment")

#### Detect the dominant language using a

batch (AWS CLI)

The [BatchDetectDominantLanguage](../APIReference/API_BatchDetectDominantLanguage.md "../APIReference/API_BatchDetectDominantLanguage.md") operation determines the
dominant language of each document in a batch. For a list of the languages that
Amazon Comprehend can detect, see [Dominant language](how-languages.md "how-languages.md"). The following AWS CLI command calls the
`BatchDetectDominantLanguage` operation.

```
aws comprehend batch-detect-dominant-language \
    --endpoint `endpoint` \
    --region `region` \
    --cli-input-json file://`path to input file`/process.json
```

The following is the response from the
`BatchDetectDominantLanguage` operation:

```
{
    "ResultList": [
        {
          "Index": 0,
          "Languages":[
            {
              "LanguageCode":"en",
              "Score": 0.99
            }
          ]
        },
        {
          "Index": 1
          "Languages":[
            {
              "LanguageCode":"en",
              "Score": 0.82
            }
          ]
        }
    ],
    "ErrorList": [
      {
        "Index": 2,
        "ErrorCode": "InternalServerException",
        "ErrorMessage": "Unexpected Server Error. Please try again."
      }
    ]
}
```

#### Detect entities using a batch (AWS CLI)

Use the [BatchDetectEntities](../APIReference/API_BatchDetectEntities.md "../APIReference/API_BatchDetectEntities.md") operation to find the entities
present in a batch of documents. For more information about entities, see [Entities](how-entities.md "how-entities.md"). The following AWS CLI
command calls the `BatchDetectEntities` operation.

```
aws comprehend batch-detect-entities \
    --endpoint `endpoint` \
    --region `region` \
    --cli-input-json file://`path to input file`/process.json
```

#### Detect key phrases using a batch

(AWS CLI)

The [BatchDetectKeyPhrases](../APIReference/API_BatchDetectKeyPhrases.md "../APIReference/API_BatchDetectKeyPhrases.md") operation returns the key noun
phrases in a batch of documents. The following AWS CLI command calls the
`BatchDetectKeyNounPhrases` operation.

```
aws comprehend batch-detect-key-phrases
    --endpoint `endpoint`
    --region `region`
    --cli-input-json file://`path to input file`/process.json
```

#### Detect sentiment using a batch (AWS CLI)

Detect the overall sentiment of a batch of documents using the [BatchDetectSentiment](../APIReference/API_BatchDetectSentiment.md "../APIReference/API_BatchDetectSentiment.md")
operation. The following AWS CLI command calls the
`BatchDetectSentiment` operation.

```
aws comprehend batch-detect-sentiment \
    --endpoint `endpoint` \
    --region `region` \
    --cli-input-json file://`path to input file`/process.json
```

### Batch processing with the AWS SDK for .NET

The following sample program shows how to use the [BatchDetectEntities](../APIReference/API_BatchDetectEntities.md "../APIReference/API_BatchDetectEntities.md")
operation with the SDK for .NET. The response from the server contains a
[BatchDetectEntitiesItemResult](../APIReference/API_BatchDetectEntitiesItemResult.md "../APIReference/API_BatchDetectEntitiesItemResult.md") object
for each document that was successfully processed. If there is an error processing a document, there will be a
record in the error list in the response. The example gets each of the documents with an error and resends
them.

The .NET example in this section uses the [AWS SDK for .NET](../../../sdk-for-net/latest/developer-guide/welcome.md "../../../sdk-for-net/latest/developer-guide/welcome.md"). You can use the [AWS Toolkit for Visual Studio](../../../AWSToolkitVS/latest/UserGuide/welcome.md "../../../AWSToolkitVS/latest/UserGuide/welcome.md") to develop AWS applications
using .NET. It includes helpful templates and the AWS Explorer for deploying
applications and managing services. For a .NET developer perspective of AWS, see the
[AWS guide for .NET developers](../../../sdk-for-net/latest/developer-guide/welcome.md "../../../sdk-for-net/latest/developer-guide/welcome.md").

```
using System;
using System.Collections.Generic;
using Amazon.Comprehend;
using Amazon.Comprehend.Model;

namespace Comprehend
{
    class Program
    {
        // Helper method for printing properties
        static private void PrintEntity(Entity entity)
        {
            Console.WriteLine("     Text: {0}, Type: {1}, Score: {2}, BeginOffset: {3} EndOffset: {4}",
                entity.Text, entity.Type, entity.Score, entity.BeginOffset, entity.EndOffset);
        }

        static void Main(string[] args)
        {
            AmazonComprehendClient comprehendClient = new AmazonComprehendClient(Amazon.RegionEndpoint.USWest2);

            List<String> textList = new List<String>()
            {
                { "I love Seattle" },
                { "Today is Sunday" },
                { "Tomorrow is Monday" },
                { "I love Seattle" }
            };

            // Call detectEntities API
            Console.WriteLine("Calling BatchDetectEntities");
            BatchDetectEntitiesRequest batchDetectEntitiesRequest = new BatchDetectEntitiesRequest()
            {
                TextList = textList,
                LanguageCode = "en"
            };
            BatchDetectEntitiesResponse batchDetectEntitiesResponse = comprehendClient.BatchDetectEntities(batchDetectEntitiesRequest);

            foreach (BatchDetectEntitiesItemResult item in batchDetectEntitiesResponse.ResultList)
            {
                Console.WriteLine("Entities in {0}:", textList[item.Index]);
                foreach (Entity entity in item.Entities)
                    PrintEntity(entity);
            }

            // check if we need to retry failed requests
            if (batchDetectEntitiesResponse.ErrorList.Count != 0)
            {
                Console.WriteLine("Retrying Failed Requests");
                List<String> textToRetry = new List<String>();
                foreach(BatchItemError errorItem in batchDetectEntitiesResponse.ErrorList)
                    textToRetry.Add(textList[errorItem.Index]);

                batchDetectEntitiesRequest = new BatchDetectEntitiesRequest()
                {
                    TextList = textToRetry,
                    LanguageCode = "en"
                };

                batchDetectEntitiesResponse = comprehendClient.BatchDetectEntities(batchDetectEntitiesRequest);

                foreach(BatchDetectEntitiesItemResult item in batchDetectEntitiesResponse.ResultList)
                {
                    Console.WriteLine("Entities in {0}:", textList[item.Index]);
                    foreach (Entity entity in item.Entities)
                        PrintEntity(entity);
                }
            }
            Console.WriteLine("End of DetectEntities");
        }
    }
}
```
