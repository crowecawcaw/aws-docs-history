# Example Contact Lens

conversational analytics output files for a call

The following sections provide examples of the output that results when
Contact Lens conversational analytics detects issues, matches categories,
indicates loudness, redacts sensitive data, and skipped analysis.

Expand each section to learn more.

The following example shows the schema for a call that Contact Lens
conversational analytics has analyzed. The example shows loudness, issue
detection, call drivers, and the information that will be redacted.

Note the following about the analyzed file:

- It doesn't indicate which sensitive data were redacted. All data
  are referred to as PII (personally identifiable information).
- Each turn includes a `Redaction` section only if it
  includes PII.
- If a `Redaction` section exists, it includes the offset
  in milliseconds. In a .wav file, the redacted portion will be
  silence. If desired, you can use the offset to replace the silence
  with something else, such as a beep.
- If two or more PII redactions exist in a turn, the first offset
  applies to the first PII, the second offset applies to the second
  PII, and so on.

```
{
  "Version": "1.1.0",
  "AccountId": "your AWS account ID",
  "Channel": "VOICE",
  "ContentMetadata": {
      "Output": "Raw"
  },
  "JobStatus": "COMPLETED",
  "JobDetails": {
    "SkippedAnalysis": [
        {
            "Feature": "CATEGORIZATION",
            "ReasonCode": "QUOTA_EXCEEDED",
            "SkippedEntities": [
                {
                    "CategoryName": "PotentialFraud"
                    "RuleId": "a1130485-9529-4249-a1d4-5738b4883748"
                },
                {
                    "CategoryName": "Refund"
                    "RuleId": "bbbbbbb-9529-4249-a1d4-5738b4883748"
                }
            ]
        },
        {
            "Feature": "CATEGORIZATION",
            "ReasonCode": "FAILED_SAFETY_GUIDELINES",
            "SkippedEntities": [
                {
                    "CategoryName": "ManagerEscalation"
                    "RuleId": "cccccccc-9529-4249-a1d4-5738b4883748"
                },
            ]
        },
    ]
  },
  "LanguageCode": "en-US",
  "Participants": [
      {
          "ParticipantId": "CUSTOMER",
          "ParticipantRole": "CUSTOMER"
      },

      {
          "ParticipantId": "AGENT",
          "ParticipantRole": "AGENT"
      }
  ],
  "Categories": {
      "MatchedCategories": ["Cancellation"],
      "MatchedDetails": {
          "Cancellation": {
              "PointsOfInterest": [
                  {
                      "BeginOffsetMillis": 7370,
                      "EndOffsetMillis": 11190
                  }
              ]
          }
      }
  },
  "ConversationCharacteristics": {
     "ContactSummary": {
          "PostContactSummary": {
           "Content": "The customer and agent's conversation did not have any clear issues, outcomes or next steps. Agent verified customer information and finished the call."
           }
      },
     "TotalConversationDurationMillis": 32110,
      "Sentiment": {
          "OverallSentiment": {
              "AGENT": 0,
              "CUSTOMER": 3.1
          },
          "SentimentByPeriod": {
              "QUARTER": {
                  "AGENT": [
                      {
                          "BeginOffsetMillis": 0,
                          "EndOffsetMillis": 7427,
                          "Score": 0
                      },
                      {
                          "BeginOffsetMillis": 7427,
                          "EndOffsetMillis": 14855,
                          "Score": -5
                      },
                      {
                          "BeginOffsetMillis": 14855,
                          "EndOffsetMillis": 22282,
                          "Score": 0
                      },
                      {
                          "BeginOffsetMillis": 22282,
                          "EndOffsetMillis": 29710,
                          "Score": 5
                      }
                  ],
                  "CUSTOMER": [
                      {
                          "BeginOffsetMillis": 0,
                          "EndOffsetMillis": 8027,
                          "Score": -2.5
                      },
                      {
                          "BeginOffsetMillis": 8027,
                          "EndOffsetMillis": 16055,
                          "Score": 5
                      },
                      {
                          "BeginOffsetMillis": 16055,
                          "EndOffsetMillis": 24082,
                          "Score": 5
                      },
                      {
                          "BeginOffsetMillis": 24082,
                          "EndOffsetMillis": 32110,
                          "Score": 5
                      }
                  ]
              }
          }
      },
      "Interruptions": {
        "InterruptionsByInterrupter": {
            "CUSTOMER": [
                {
                    "BeginOffsetMillis": 10710,
                    "DurationMillis": 3790,
                    "EndOffsetMillis": 14500
                }
            ],
            "AGENT": [
                {
                    "BeginOffsetMillis": 10710,
                    "DurationMillis": 3790,
                    "EndOffsetMillis": 14500
                }
            ]
        },
        "TotalCount": 2,
        "TotalTimeMillis": 7580
      },
      "NonTalkTime": {
          "TotalTimeMillis": 0,
          "Instances": []
      },
      "TalkSpeed": {
          "DetailsByParticipant": {
              "AGENT": {
                  "AverageWordsPerMinute": 239
              },
              "CUSTOMER": {
                  "AverageWordsPerMinute": 163
              }
          }
      },
      "TalkTime": {
          "TotalTimeMillis": 28698,
          "DetailsByParticipant": {
              "AGENT": {
                  "TotalTimeMillis": 15079
              },
              "CUSTOMER": {
                  "TotalTimeMillis": 13619
              }
          }
      }
  },
  "CustomModels": [
      {    // set via https://docs.aws.amazon.com/connect/latest/adminguide/add-custom-vocabulary.html
           "Type": "TRANSCRIPTION_VOCABULARY",
           "Name": "ProductNames",
           "Id": "4e14b0db-f00a-451a-8847-f6dbf76ae415" // optional field
      }
  ],
  "Transcript": [
      {
          "BeginOffsetMillis": 0,
          "Content": "Okay.",
          "EndOffsetMillis": 90,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "NEUTRAL",
          "LoudnessScore": [
              79.27
          ]
      },
      {
          "BeginOffsetMillis": 160,
          "Content": "Just hello. My name is Peter and help.",
          "EndOffsetMillis": 4640,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "NEUTRAL",
          "LoudnessScore": [
              66.56,
              40.06,
              85.27,
              82.22,
              77.66
          ],
          "Redaction": {
              "RedactedTimestamps": [
                  {
                      "BeginOffsetMillis": 3290,
                      "EndOffsetMillis": 3620
                  }
              ]
          }
      },
      {
          "BeginOffsetMillis": 4640,
          "Content": "Hello. Peter, how can I help you?",
          "EndOffsetMillis": 6610,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "NEUTRAL",
          "LoudnessScore": [
              70.23,
              73.05,
              71.8
          ],
          "Redaction": {
              "RedactedTimestamps": [
                  {
                      "BeginOffsetMillis": 5100,
                      "EndOffsetMillis": 5450
                  }
              ]
          }
      },
      {
          "BeginOffsetMillis": 7370,
          "Content": "I need to cancel. I want to cancel my plan subscription.",
          "EndOffsetMillis": 11190,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "NEGATIVE",
          "LoudnessScore": [
              77.18,
              79.59,
              85.23,
              81.08,
              73.99
          ],
          "IssuesDetected": [
              {
                  "CharacterOffsets": {
                      "BeginOffsetChar": 0,
                      "EndOffsetChar": 55
                  },
                  "Text": "I need to cancel. I want to cancel my plan subscription"
              }
          ]
      },
      {
          "BeginOffsetMillis": 11220,
          "Content": "That sounds very bad. I can offer a 20% discount to make you stay with us.",
          "EndOffsetMillis": 15210,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "NEGATIVE",
          "LoudnessScore": [
              75.92,
              75.79,
              80.31,
              80.44,
              76.31
          ]
      },
      {
          "BeginOffsetMillis": 15840,
          "Content": "That sounds interesting. Thank you accept.",
          "EndOffsetMillis": 18120,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "POSITIVE",
          "LoudnessScore": [
              73.77,
              79.17,
              77.97,
              79.29
          ]
      },
      {
          "BeginOffsetMillis": 18310,
          "Content": "Alright, I made all the changes to the account and now these discounts applied.",
          "EndOffsetMillis": 21820,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "NEUTRAL",
          "LoudnessScore": [
              83.88,
              86.75,
              86.97,
              86.11
          ],
          "OutcomesDetected": [
              {
                  "CharacterOffsets": {
                      "BeginOffsetChar": 9,
                      "EndOffsetChar": 77
                  },
                  "Text": "I made all the changes to the account and now these discounts applied"
              }
          ]
      },
      {
          "BeginOffsetMillis": 22610,
          "Content": "Awesome. Thank you so much.",
          "EndOffsetMillis": 24140,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "POSITIVE",
          "LoudnessScore": [
              79.11,
              81.7,
              78.15
          ]
      },
      {
          "BeginOffsetMillis": 24120,
          "Content": "No worries. I will send you all the details later today and call you back next week to check up on you.",
          "EndOffsetMillis": 29710,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "POSITIVE",
          "LoudnessScore": [
              87.07,
              83.96,
              76.38,
              88.38,
              87.69,
              76.6
          ],
          "ActionItemsDetected": [
              {
                  "CharacterOffsets": {
                      "BeginOffsetChar": 12,
                      "EndOffsetChar": 102
                  },
                  "Text": "I will send you all the details later today and call you back next week to check up on you"
              }
          ]
      },
      {
          "BeginOffsetMillis": 30580,
          "Content": "Thank you. Sir. Have a nice evening.",
          "EndOffsetMillis": 32110,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "POSITIVE",
          "LoudnessScore": [
              81.42,
              82.29,
              73.29
          ]
      }
  ]
  }
}
```

This section shows an example redacted file for a call after it's been
analyzed by Contact Lens conversational analytics. It's a twin of the
original analyzed file. The only difference is that sensitive data are
redacted. In this example, three entities were selected for redaction:
"`CREDIT_DEBIT_NUMBER`", "`NAME`",
"`USERNAME`".

In this example, `RedactionMaskMode` is set to PII. When an
entity is redacted, Contact Lens replaces it with `[PII]`.
If it were set to `ENTITY_TYPE`, Contact Lens would
replace the data with the name of the entity, for example,
`[CREDIT_DEBIT_NUMBER]`.

```
{
  "Version": "1.1.0",
  "AccountId": "your AWS account ID",
  "ContentMetadata": {
      "Output": "Redacted",
      "RedactionTypes": ["PII"],
      "RedactionTypesMetadata": {
          "PII": {
              "RedactionEntitiesRequested": ["CREDIT_DEBIT_NUMBER", "NAME", "USERNAME"],
              "RedactionMaskMode": "PII" // if you were to choose ENTITY_TYPE instead, the redaction would say, for example, [NAME]
          }
      }
  },
  "Channel": "VOICE",
  "JobStatus": "COMPLETED",
  "JobDetails": {
    "SkippedAnalysis": [
        {
            "Feature": "CATEGORIZATION",
            "ReasonCode": "QUOTA_EXCEEDED",
            "SkippedEntities": [
                {
                    "CategoryName": "PotentialFraud"
                    "RuleId": "a1130485-9529-4249-a1d4-5738b4883748"
                },
                {
                    "CategoryName": "Refund"
                    "RuleId": "bbbbbbb-9529-4249-a1d4-5738b4883748"
                }
            ]
        },
        {
            "Feature": "CATEGORIZATION",
            "ReasonCode": "FAILED_SAFETY_GUIDELINES",
            "SkippedEntities": [
                {
                    "CategoryName": "ManagerEscalation"
                    "RuleId": "cccccccc-9529-4249-a1d4-5738b4883748"
                },
            ]
        },
    ]
  },
  "LanguageCode": "en-US",
  "Participants": [
      {
          "ParticipantId": "CUSTOMER",
          "ParticipantRole": "CUSTOMER"
      },

      {
          "ParticipantId": "AGENT",
          "ParticipantRole": "AGENT"
      }
  ],
  "Categories": {
      "MatchedCategories": ["Cancellation"],
      "MatchedDetails": {
          "Cancellation": {
              "PointsOfInterest": [
                  {
                      "BeginOffsetMillis": 7370,
                      "EndOffsetMillis": 11190
                  }
              ]
          }
      }
  },
  "ConversationCharacteristics": {
       "ContactSummary": {
             "PostContactSummary": {
               "Content": "The customer and agent's conversation did not have any clear issues, outcomes or next steps. Agent verified customer information and finished the call."
              }
      },
      "TotalConversationDurationMillis": 32110,
      "Sentiment": {
          "OverallSentiment": {
              "AGENT": 0,
              "CUSTOMER": 3.1
          },
          "SentimentByPeriod": {
              "QUARTER": {
                  "AGENT": [
                      {
                          "BeginOffsetMillis": 0,
                          "EndOffsetMillis": 7427,
                          "Score": 0
                      },
                      {
                          "BeginOffsetMillis": 7427,
                          "EndOffsetMillis": 14855,
                          "Score": -5
                      },
                      {
                          "BeginOffsetMillis": 14855,
                          "EndOffsetMillis": 22282,
                          "Score": 0
                      },
                      {
                          "BeginOffsetMillis": 22282,
                          "EndOffsetMillis": 29710,
                          "Score": 5
                      }
                  ],
                  "CUSTOMER": [
                      {
                          "BeginOffsetMillis": 0,
                          "EndOffsetMillis": 8027,
                          "Score": -2.5
                      },
                      {
                          "BeginOffsetMillis": 8027,
                          "EndOffsetMillis": 16055,
                          "Score": 5
                      },
                      {
                          "BeginOffsetMillis": 16055,
                          "EndOffsetMillis": 24082,
                          "Score": 5
                      },
                      {
                          "BeginOffsetMillis": 24082,
                          "EndOffsetMillis": 32110,
                          "Score": 5
                      }
                  ]
              }
          }
      },
      "Interruptions": {
        "InterruptionsByInterrupter": {
            "CUSTOMER": [
                {
                    "BeginOffsetMillis": 10710,
                    "DurationMillis": 3790,
                    "EndOffsetMillis": 14500
                }
            ],
            "AGENT": [
                {
                    "BeginOffsetMillis": 10710,
                    "DurationMillis": 3790,
                    "EndOffsetMillis": 14500
                }
            ]
        },
        "TotalCount": 2,
        "TotalTimeMillis": 7580
      },
      "NonTalkTime": {
          "TotalTimeMillis": 0,
          "Instances": []
      },
      "TalkSpeed": {
          "DetailsByParticipant": {
              "AGENT": {
                  "AverageWordsPerMinute": 239
              },
              "CUSTOMER": {
                  "AverageWordsPerMinute": 163
              }
          }
      },
      "TalkTime": {
          "TotalTimeMillis": 28698,
          "DetailsByParticipant": {
              "AGENT": {
                  "TotalTimeMillis": 15079
              },
              "CUSTOMER": {
                  "TotalTimeMillis": 13619
              }
          }
      }
  },
  "CustomModels": [
      {   // set via https://docs.aws.amazon.com/connect/latest/adminguide/add-custom-vocabulary.html
           "Type": "TRANSCRIPTION_VOCABULARY",
           "Name": " LNK POPProductNames",
           "Id": "4e14b0db-f00a-451a-8847-f6dbf76ae415" // optional field
      }
  ],
  "Transcript": [
      {
          "BeginOffsetMillis": 0,
          "Content": "Okay.",
          "EndOffsetMillis": 90,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "NEUTRAL",
          "LoudnessScore": [
              79.27
          ]
      },
      {
          "BeginOffsetMillis": 160,
          "Content": "Just hello. My name is [PII] and help.",
          "EndOffsetMillis": 4640,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "NEUTRAL",
          "LoudnessScore": [
              66.56,
              40.06,
              85.27,
              82.22,
              77.66
          ],
          "Redaction": {
              "RedactedTimestamps": [
                  {
                      "BeginOffsetMillis": 3290,
                      "EndOffsetMillis": 3620
                  }
              ]
          }
      },
      {
          "BeginOffsetMillis": 4640,
          "Content": "Hello. [PII], how can I help you?",
          "EndOffsetMillis": 6610,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "NEUTRAL",
          "LoudnessScore": [
              70.23,
              73.05,
              71.8
          ],
          "Redaction": {
              "RedactedTimestamps": [
                  {
                      "BeginOffsetMillis": 5100,
                      "EndOffsetMillis": 5450
                  }
              ]
          }
      },
      {
          "BeginOffsetMillis": 7370,
          "Content": "I need to cancel. I want to cancel my plan subscription.",
          "EndOffsetMillis": 11190,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "NEGATIVE",
          "LoudnessScore": [
              77.18,
              79.59,
              85.23,
              81.08,
              73.99
          ],
          "IssuesDetected": [
              {
                  "CharacterOffsets": {
                      "BeginOffsetChar": 0,
                      "EndOffsetChar": 55
                  },
                  "Text": "I need to cancel. I want to cancel my plan subscription"
              }
          ]
      },
      {
          "BeginOffsetMillis": 11220,
          "Content": "That sounds very bad. I can offer a 20% discount to make you stay with us.",
          "EndOffsetMillis": 15210,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "NEGATIVE",
          "LoudnessScore": [
              75.92,
              75.79,
              80.31,
              80.44,
              76.31
          ]
      },
      {
          "BeginOffsetMillis": 15840,
          "Content": "That sounds interesting. Thank you accept.",
          "EndOffsetMillis": 18120,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "POSITIVE",
          "LoudnessScore": [
              73.77,
              79.17,
              77.97,
              79.29
          ]
      },
      {
          "BeginOffsetMillis": 18310,
          "Content": "Alright, I made all the changes to the account and now these discounts applied.",
          "EndOffsetMillis": 21820,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "NEUTRAL",
          "LoudnessScore": [
              83.88,
              86.75,
              86.97,
              86.11
          ],
          "OutcomesDetected": [
              {
                  "CharacterOffsets": {
                      "BeginOffsetChar": 9,
                      "EndOffsetChar": 77
                  },
                  "Text": "I made all the changes to the account and now these discounts applied"
              }
          ]
      },
      {
          "BeginOffsetMillis": 22610,
          "Content": "Awesome. Thank you so much.",
          "EndOffsetMillis": 24140,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "POSITIVE",
          "LoudnessScore": [
              79.11,
              81.7,
              78.15
          ]
      },
      {
          "BeginOffsetMillis": 24120,
          "Content": "No worries. I will send you all the details later today and call you back next week to check up on you.",
          "EndOffsetMillis": 29710,
          "Id": "the ID of the turn",
          "ParticipantId": "AGENT",
          "Sentiment": "POSITIVE",
          "LoudnessScore": [
              87.07,
              83.96,
              76.38,
              88.38,
              87.69,
              76.6
          ],
          "ActionItemsDetected": [
              {
                  "CharacterOffsets": {
                      "BeginOffsetChar": 12,
                      "EndOffsetChar": 102
                  },
                  "Text": "I will send you all the details later today and call you back next week to check up on you"
              }
          ]
      },
      {
          "BeginOffsetMillis": 30580,
          "Content": "Thank you. Sir. Have a nice evening.",
          "EndOffsetMillis": 32110,
          "Id": "the ID of the turn",
          "ParticipantId": "CUSTOMER",
          "Sentiment": "POSITIVE",
          "LoudnessScore": [
              81.42,
              82.29,
              73.29
          ]
      }
  ]
}
```
