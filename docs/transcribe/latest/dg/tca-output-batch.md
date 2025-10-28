# Post-call analytics output

Post-call analytics transcripts are displayed in a turn-by-turn format by segment.
They include call categorization, call characteristics (loudness scores, interruptions, non-talk
time, talk speed), call summarization (issues, outcomes, and action items), redaction, and
sentiment. Additionally, a summary of conversation characteristics is provided at the end of
the transcript.

To increase accuracy and further customize your transcripts to your use case, such as
including industry-specific terms, add [custom
vocabularies](custom-vocabulary.md "custom-vocabulary.md") or [custom language
models](custom-language-models.md "custom-language-models.md") to your Call Analytics request. To mask, remove, or tag words that you
don't want in your transcription results, such as profanity, add [vocabulary filtering](vocabulary-filtering.md "vocabulary-filtering.md").
If you are unsure of the language code to be passed to the media file, you can enable
[batch language identification](lang-id-batch.md "lang-id-batch.md")
to automatically identify the language in your media file.

The following sections show examples of JSON output at an insight level. For compiled output, see
[Compiled post-call analytics output](#tca-output-batch-compiled "#tca-output-batch-compiled").

## Call categorization

Here's what a category match looks like in your transcription output. This example shows that
the audio from the 40040 millisecond timestamp to the 42460 millisecond timestamp is a match
to the 'positive-resolution' category. In this case, the custom 'positive-resolution' category required
a positive sentiment in last few seconds of speech.

```
"Categories": {
    "MatchedDetails": {
        "`positive-resolution`": {
            "PointsOfInterest": [
                {
                    "BeginOffsetMillis":  `40040`,
                    "EndOffsetMillis":  `42460`
                }
            ]
        }
    },
    "MatchedCategories": [
        " `positive-resolution`"
    ]
},
```

## Call characteristics

Here's what call characteristics look like in your transcription output. Note that loudness scores
are provided for each conversation turn, while all other characteristics are provided at the end of the
transcript.

```
"LoudnessScores": [
    `87.54`,
    `88.74`,
    `90.16`,
    `86.36`,
    `85.56`,
    `85.52`,
    `81.79`,
    `87.74`,
    `89.82`
],

`...`

"ConversationCharacteristics": {
    "NonTalkTime": {
        "Instances": [],
        "TotalTimeMillis": `0`
    },
    "Interruptions": {
        "TotalCount": `2`,
        "TotalTimeMillis": `10700`,
        "InterruptionsByInterrupter": {
            "AGENT": [
                {
                    "BeginOffsetMillis": `26040`,
                    "DurationMillis": `5510`,
                    "EndOffsetMillis": `31550`
                }
            ],
            "CUSTOMER": [
                {
                    "BeginOffsetMillis": `770`,
                    "DurationMillis": `5190`,
                    "EndOffsetMillis": `5960`
                }
            ]
        }
    },
    "TotalConversationDurationMillis": `42460`,

    `...`

    "TalkSpeed": {
        "DetailsByParticipant": {
            "AGENT": {
                "AverageWordsPerMinute": `150`
            },
            "CUSTOMER": {
                "AverageWordsPerMinute": `167`
            }
        }
    },
    "TalkTime": {
        "DetailsByParticipant": {
            "AGENT": {
                "TotalTimeMillis": `32750`
            },
            "CUSTOMER": {
                "TotalTimeMillis": `18010`
            }
        },
        "TotalTimeMillis": `50760`
    }
},
```

**Issues, Action Items and Next Steps**

- In the following example, **issues** are identified as starting at
  character 7 and ending at character 51, which refers to this section of the text:
  "_I would like to cancel my recipe subscription_".

```
"Content": "`Well, I would like to cancel my recipe subscription.`",

"IssuesDetected": [
    {
        "CharacterOffsets": {
            "Begin": `7`,
            "End": `51`
        }
    }
],
```

- In the following example, **outcomes** are identified as starting at
  character 12 and ending at character 78, which refers to this section of the text:
  "_I made all changes to your account and now this discount is applied_".

```
"Content": "`Wonderful. I made all changes to your account and now this discount is applied, please check.`",

"OutcomesDetected": [
    {
        "CharacterOffsets": {
            "Begin": `12`,
            "End": `78`
        }
    }
],
```

- In the following example, **action items** are identified as starting at
  character 0 and ending at character 103, which refers to this section of the text:
  "_I will send an email with all the details to you today, and I will call you back next
  week to follow up_".

```
"Content": "`I will send an email with all the details to you today, and I will call you back next week to follow up. Have a wonderful evening.`",

"ActionItemsDetected": [
    {
        "CharacterOffsets": {
            "Begin": `0`,
            "End": `103`
        }
    }
],
```

## Generative call summarization

Here's what generative call summarization looks like in your transcription output:

```
"ContactSummary": {
    "AutoGenerated": {
        "OverallSummary": {
            "Content": "A customer wanted to check to see if we had a bag allowance. We told them that we didn't have it, but we could add the bag from Canada to Calgary and then do the one coming back as well."
        }
    }
}
```

The analytics job will complete without summary generation in the following cases:

- Insufficient conversation content: The conversation must include at least one turn from both the agent and the customer. When there is insufficient conversation content, the service will return the error code INSUFFICIENT_CONVERSATION_CONTENT.
- Safety guardrails: The conversation must meet safety guardrails in place to ensure appropriate summary is generated. When these guardrails are not met, the service will return the error code FAILED_SAFETY_GUIDELINES.

The error code can be found in `Skipped` section within `AnalyticsJobDetails` in the output. You may also find the error reason in `CallAnalyticsJobDetails` in the [`GetCallAnalyticsJob`](../APIReference/API_GetCallAnalyticsJob.md "../APIReference/API_GetCallAnalyticsJob.md") API Response.

**Sample Error Output**

```
{
    "JobStatus": "COMPLETED",
    "AnalyticsJobDetails": {
        "Skipped": [
            {
                "Feature": "GENERATIVE_SUMMARIZATION",
                "ReasonCode": "INSUFFICIENT_CONVERSATION_CONTENT",
                "Message": "The conversation needs to have at least one turn from both the participants to generate summary"
            }
        ]
    },
    "LanguageCode": "en-US",
    "AccountId": "***************",
    "JobName": "Test2-copy",
    `...`
}
```

## Sentiment analysis

Here is what sentiment analysis looks like in your transcription output.

- Qualitative turn-by-turn sentiment values:

```
"Content": "`That's very sad to hear. Can I offer you a 50% discount to have you stay with us?`",

`...`

"BeginOffsetMillis": `12180`,
"EndOffsetMillis": `16960`,
"Sentiment": "`NEGATIVE`",
"ParticipantRole": "`AGENT`"

`...`

"Content": "`That is a very generous offer. And I accept.`",

`...`

"BeginOffsetMillis": `17140`,
"EndOffsetMillis": `19860`,
"Sentiment": "`POSITIVE`",
"ParticipantRole": "`CUSTOMER`"
```

- Quantitative sentiment values for the entire call:

```
"Sentiment": {
    "OverallSentiment": {
        "AGENT": `2.5`,
        "CUSTOMER": `2.1`
    },
```

- Quantitative sentiment values per participant and per call quarter:

```
"SentimentByPeriod": {
    "QUARTER": {
        "AGENT": [
            {
                "Score": `0.0`,
                "BeginOffsetMillis": `0`,
                "EndOffsetMillis": `9862`
            },
            {
                "Score": `-5.0`,
                "BeginOffsetMillis": `9862`,
                "EndOffsetMillis": `19725`
            },
            {
                "Score": `5.0`,
                "BeginOffsetMillis": `19725`,
                "EndOffsetMillis": `29587`
            },
            {
                "Score": `5.0`,
                "BeginOffsetMillis": `29587`,
                "EndOffsetMillis": `39450`
            }
        ],
        "CUSTOMER": [
            {
                "Score": `-2.5`,
                "BeginOffsetMillis": `0`,
                "EndOffsetMillis": `10615`
            },
            {
                "Score": `5.0`,
                "BeginOffsetMillis": `10615`,
                "EndOffsetMillis": `21230`
            },
            {
                "Score": `2.5`,
                "BeginOffsetMillis": `21230`,
                "EndOffsetMillis": `31845`
            },
            {
                "Score": `5.0`,
                "BeginOffsetMillis": `31845`,
                "EndOffsetMillis": `42460`
            }
        ]
    }
}
```

## PII redaction

Here is what PII redaction looks like in your transcription output.

```
"Content": "[PII], my name is [PII], how can I help?",
"Redaction": [{
    "Confidence": "0.9998",
    "Type": "NAME",
    "Category": "PII"
}]

```

For more information, refer to [Redacting PII in your batch job](pii-redaction-batch.md "pii-redaction-batch.md").

## Language identification

Here is what Language Identification looks like in your transcription output if the feature is enabled.

```
"LanguageIdentification": [{
  "Code": "en-US",
  "Score": "0.8299"
}, {
  "Code": "en-NZ",
  "Score": "0.0728"
}, {
  "Code": "zh-TW",
  "Score": "0.0695"
}, {
  "Code": "th-TH",
  "Score": "0.0156"
}, {
  "Code": "en-ZA",
  "Score": "0.0121"
}]

```

In the above output example, Language Identification will populate the language codes with confidence scores.
The result with the highest score will be selected as the language code for transcription.
For mode details refer to [Identifying the dominant languages in your media](lang-id.md "lang-id.md").

## Compiled post-call analytics output

For brevity, some content is replaced with ellipses in the following transcription
output.

This sample includes optional feature - Generative call summarization.

```
{
    "JobStatus": "COMPLETED",
    "LanguageCode": "en-US",
    "Transcript": [
        {
            "LoudnessScores": [
                78.63,
                78.37,
                77.98,
                74.18
            ],
            "Content": "[PII], my name is [PII], how can I help?",

            `...`

             "Content": "Well, I would like to cancel my recipe subscription.",
             "IssuesDetected": [
                 {
                     "CharacterOffsets": {
                         "Begin": 7,
                         "End": 51
                     }
                 }
             ],

            `...`

            "Content": "That's very sad to hear. Can I offer you a 50% discount to have you stay with us?",
            "Items": [
            `...`
             ],
            "Id": "649afe93-1e59-4ae9-a3ba-a0a613868f5d",
            "BeginOffsetMillis": 12180,
            "EndOffsetMillis": 16960,
            "Sentiment": "NEGATIVE",
            "ParticipantRole": "AGENT"
        },
        {
            "LoudnessScores": [
                    80.22,
                    79.48,
                    82.81
            ],
            "Content": "That is a very generous offer. And I accept.",
            "Items": [
            `...`
            ],
            "Id": "f9266cba-34df-4ca8-9cea-4f62a52a7981",
            "BeginOffsetMillis": 17140,
            "EndOffsetMillis": 19860,
            "Sentiment": "POSITIVE",
            "ParticipantRole": "CUSTOMER"
        },
        {

     `...`

            "Content": "Wonderful. I made all changes to your account and now this discount is applied, please check.",
            "OutcomesDetected": [
                {
                    "CharacterOffsets": {
                        "Begin": 12,
                        "End": 78
                    }
                }
            ],

            `...`

            "Content": "I will send an email with all the details to you today, and I will call you back next week to follow up. Have a wonderful evening.",
            "Items": [
            `...`
            ],
            "Id": "78cd0923-cafd-44a5-a66e-09515796572f",
            "BeginOffsetMillis": 31800,
            "EndOffsetMillis": 39450,
            "Sentiment": "POSITIVE",
            "ParticipantRole": "AGENT"
        },
        {
           "LoudnessScores": [
               78.54,
               68.76,
               67.76
           ],
           "Content": "Thank you very much, sir. Goodbye.",
           "Items": [
           `...`
           ],
           "Id": "5c5e6be0-8349-4767-8447-986f995af7c3",
           "BeginOffsetMillis": 40040,
           "EndOffsetMillis": 42460,
           "Sentiment": "POSITIVE",
           "ParticipantRole": "CUSTOMER"
       }
   ],

   `...`

   "Categories": {
        "MatchedDetails": {
            "positive-resolution": {
                "PointsOfInterest": [
                    {
                        "BeginOffsetMillis": 40040,
                        "EndOffsetMillis": 42460
                    }
                ]
            }
        },
        "MatchedCategories": [
            "positive-resolution"
        ]
    },

    `...`

    "ConversationCharacteristics": {
        "NonTalkTime": {
            "Instances": [],
            "TotalTimeMillis": 0
        },
        "Interruptions": {
            "TotalCount": 2,
            "TotalTimeMillis": 10700,
            "InterruptionsByInterrupter": {
                "AGENT": [
                    {
                        "BeginOffsetMillis": 26040,
                        "DurationMillis": 5510,
                        "EndOffsetMillis": 31550
                    }
                ],
                "CUSTOMER": [
                    {
                        "BeginOffsetMillis": 770,
                        "DurationMillis": 5190,
                        "EndOffsetMillis": 5960
                    }
                ]
            }
        },
        "TotalConversationDurationMillis": 42460,
        "Sentiment": {
            "OverallSentiment": {
                "AGENT": 2.5,
                "CUSTOMER": 2.1
            },
            "SentimentByPeriod": {
                "QUARTER": {
                    "AGENT": [
                        {
                            "Score": 0.0,
                            "BeginOffsetMillis": 0,
                            "EndOffsetMillis": 9862
                        },
                        {
                            "Score": -5.0,
                            "BeginOffsetMillis": 9862,
                            "EndOffsetMillis": 19725
                        },
                        {
                            "Score": 5.0,
                            "BeginOffsetMillis": 19725,
                            "EndOffsetMillis": 29587
                        },
                        {
                            "Score": 5.0,
                            "BeginOffsetMillis": 29587,
                            "EndOffsetMillis": 39450
                        }
                    ],
                    "CUSTOMER": [
                        {
                            "Score": -2.5,
                            "BeginOffsetMillis": 0,
                            "EndOffsetMillis": 10615
                        },
                        {
                            "Score": 5.0,
                            "BeginOffsetMillis": 10615,
                            "EndOffsetMillis": 21230
                        },
                        {
                            "Score": 2.5,
                            "BeginOffsetMillis": 21230,
                            "EndOffsetMillis": 31845
                        },
                        {
                            "Score": 5.0,
                            "BeginOffsetMillis": 31845,
                            "EndOffsetMillis": 42460
                        }
                    ]
                }
            }
        },
        "TalkSpeed": {
            "DetailsByParticipant": {
                "AGENT": {
                    "AverageWordsPerMinute": 150
                },
                "CUSTOMER": {
                    "AverageWordsPerMinute": 167
                }
            }
        },
        "TalkTime": {
            "DetailsByParticipant": {
                "AGENT": {
                    "TotalTimeMillis": 32750
                },
                "CUSTOMER": {
                    "TotalTimeMillis": 18010
                }
            },
            "TotalTimeMillis": 50760
        },
        "ContactSummary": { // Optional feature - Generative call summarization
            "AutoGenerated": {
                "OverallSummary": {
                    "Content": "The customer initially wanted to cancel but the agent convinced them to stay by offering a 50% discount, which the customer accepted after reconsidering cancelling given the significant savings. The agent ensured the discount was applied and said they would follow up to ensure the customer remained happy with the revised subscription."
                }
            }
        }
    },
    "AnalyticsJobDetails": {
        "Skipped": []
    },
    `...`
}
```
