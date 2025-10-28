# JSON format for importing and

exporting bots in Lex V2

You import and export bots, bot locales, or custom vocabularies
from Amazon Lex V2 using a .zip file that contains JSON structures that
describe the parts of the resource. When you export a resource,
Amazon Lex V2 creates the .zip file and makes it available to you using an
Amazon S3 pre-signed URL. When you import a resource, you must create a
.zip file that contains the JSON structures and upload it to an S3
pre-signed URL.

Amazon Lex creates the following directory structure in the .zip file
when you export a bot. When you export a bot locale, only the
structure under the locale is exported. When you export a custom
vocabulary, only the structure under the custom vocabulary is
exported.

```
`BotName`_`BotVersion`_`ExportID`_LexJson.zip
            -or-
`BotName`_`BotVersion`_`LocaleId`_`ExportId`_LEX_JSON.zip
        --> manifest.json
        --> `BotName`
        ----> Bot.json
        ----> BotLocales
        ------> `Locale_A`
        --------> BotLocale.json
        --------> Intents
        ----------> `Intent_A`
        ------------> Intent.json
        ------------> Slots
        --------------> `Slot_A`
        ----------------> Slot.json
        --------------> `Slot_B`
        ----------------> Slot.json
        ----------> `Intent_B`
                       ...
        --------> SlotTypes
        ----------> `SlotType_A`
        ------------> SlotType.json
        ----------> `SlotType_B`
                        ...
        --------> CustomVocabulary
        ------------> CustomVocabulary.json

        ------> `Locale_B`
                        ...

```

## Manifest file structure

The manifest file contains metadata for the export
file.

```
{
    "metadata": {
        "schemaVersion": "1.0",
        "fileFormat": "LexJson",
        "resourceType": "`Bot` | `BotLocale` | `CustomVocabulary`"
    }
}
```

## Bot file structure

The bot file contains the configuration information for the
bot.

```
{
    "name": "`BotName`",
    "identifier": "`identifier`",
    "version": "`number`",
    "description": "`description`",
    "dataPrivacy": {
        "childDirected": `true` | `false`
    },
    "idleSessionTTLInSeconds": `seconds`
}
```

## Bot locale file

structure

The bot locale file contains a description of the locale or
language of a bot. When you export a bot, there can be more than
one bot locale file in the .zip file. When you export a bot
locale, there is only one locale in the zip file.

```
{
    "name": "`locale name`",
    "identifier": "`locale ID`",
    "version": "`number`",
    "description": "`description`",
    "voiceSettings": {
        "voiceId": "`voice`",
        "engine": "`standard | neural`
    },
    "nluConfidenceThreshold": `number`
}
```

## Intent file structure

The intent file contains the configuration information for an
intent. There is one intent file in the .zip file for each
intent in a specific locale.

The following is an example of a JSON structure for the
BookCar intent in the sample BookTrip bot. For a complete
example of the JSON structure for an intent, see the
[CreateIntent](../APIReference/API_CreateIntent.md "../APIReference/API_CreateIntent.md") operation.

```
{
    "name": "BookCar",
    "identifier": "891RWHHICO",
    "description": "Intent to book a car.",
    "parentIntentSignature": null,
    "sampleUtterances": [
        {
            "utterance": "Book a car"
        },
        {
            "utterance": "Reserve a car"
        },
        {
            "utterance": "Make a car reservation"
        }
    ],
    "intentConfirmationSetting": {
        "confirmationPrompt": {
            "messageGroupList": [
                {
                    "message": {
                        "plainTextMessage": {
                            "value": "OK, I have you down for a {CarType} hire in {PickUpCity} from {PickUpDate} to {ReturnDate}.  Should I book the reservation?"
                        },
                        "ssmlMessage": null,
                        "customPayload": null,
                        "imageResponseCard": null
                    },
                    "variations": null
                }
            ],
            "maxRetries": 2
        },
        "declinationResponse": {
            "messageGroupList": [
                {
                    "message": {
                        "plainTextMessage": {
                            "value": "OK, I have cancelled your reservation in progress."
                        },
                        "ssmlMessage": null,
                        "customPayload": null,
                        "imageResponseCard": null
                    },
                    "variations": null
                }
            ]
        }
    },
    "intentClosingSetting": null,
    "inputContexts": null,
    "outputContexts": null,
    "kendraConfiguration": null,
    "dialogCodeHook": null,
    "fulfillmentCodeHook": null,
    "slotPriorities": [
        {
            "slotName": "DriverAge",
            "priority": 4
        },
        {
            "slotName": "PickUpDate",
            "priority": 2
        },
        {
            "slotName": "ReturnDate",
            "priority": 3
        },
        {
            "slotName": "PickUpCity",
            "priority": 1
        },
        {
            "slotName": "CarType",
            "priority": 5
        }
    ]
}
```

## Slot file structure

The slot file contains the configuration information for a
slot in an intent. There is one slot file in the .zip file for
each slot defined for an intent in a specific locale.

The following example is the JSON structure of a slot that
enables the customer to choose the type of car they wish to rent
in the BookCar intent in the BookTrip example bot. For a
complete example of the JSON structure for an slot, see the
[CreateSlot](../APIReference/API_CreateSlot.md "../APIReference/API_CreateSlot.md") operation.

```
{
    "name": "CarType",
    "identifier": "KDHJWNGZGC",
    "description": "Type of car being reserved.",
    "multipleValuesSetting": {
        "allowMutlipleValues": false
    },
    "slotTypeName": "CarTypeValues",
    "obfuscationSetting": null,
    "slotConstraint": "Required",
    "defaultValueSpec": null,
    "slotValueElicitationSetting": {
        "promptSpecification": {
            "messageGroupList": [
                {
                    "message": {
                        "plainTextMessage": {
                            "value": "What type of car would you like to rent?  Our most popular options are economy, midsize, and luxury"
                        },
                        "ssmlMessage": null,
                        "customPayload": null,
                        "imageResponseCard": null
                    },
                    "variations": null
                }
            ],
            "maxRetries": 2
        },
        "sampleValueElicitingUtterances": null,
        "waitAndContinueSpecification": null,
    }
}
```

The following example shows the JSON structure of a composite slot.

```
{
  "name": "CarType",
  "identifier": "KDHJWNGZGC",
  "description": "Type of car being reserved.",
  "multipleValuesSetting": {
      "allowMutlipleValues": false
  },
  "slotTypeName": "CarTypeValues",
  "obfuscationSetting": null,
  "slotConstraint": "Required",
  "defaultValueSpec": null,
  "slotValueElicitationSetting": {
      "promptSpecification": {
          "messageGroupList": [
              {
                  "message": {
                      "plainTextMessage": {
                          "value": "What type of car would you like to rent?  Our most popular options are economy, midsize, and luxury"
                      },
                      "ssmlMessage": null,
                      "customPayload": null,
                      "imageResponseCard": null
                  },
                  "variations": null
              }
          ],
          "maxRetries": 2
      },
      "sampleValueElicitingUtterances": null,
      "waitAndContinueSpecification": null,
  },
  "subSlotSetting": {
    "slotSpecifications": {
      "firstname": {
        "valueElicitationSetting": {
          "promptSpecification": {
            "allowInterrupt": false,
            "messageGroupsList": [
              {
                "message": {
                  "imageResponseCard": null,
                  "ssmlMessage": null,
                  "customPayload": null,
                  "plainTextMessage": {
                    "value": "please provide firstname"
                  }
                },
                "variations": null
              }
            ],
            "maxRetries": 2,
            "messageSelectionStrategy": "Random"
          },
          "defaultValueSpecification": null,
          "sampleUtterances": [
            {
              "utterance": "my name is {firstName}"
            }
          ],
          "waitAndContinueSpecification": null
        },
        "slotTypeId": "AMAZON.FirstName"
      },
      "eyeColor": {
        "valueElicitationSetting": {
          "promptSpecification": {
            "allowInterrupt": false,
            "messageGroupsList": [
              {
                "message": {
                  "imageResponseCard": null,
                  "ssmlMessage": null,
                  "customPayload": null,
                  "plainTextMessage": {
                    "value": "please provide eye color"
                  }
                },
                "variations": null
              }
            ],
            "maxRetries": 2,
            "messageSelectionStrategy": "Random"
          },
          "defaultValueSpecification": null,
          "sampleUtterances": [
            {
              "utterance": "eye color is {eyeColor}"
            },
            {
              "utterance": "I have eyeColor eyes"
            }
          ],
          "waitAndContinueSpecification": null
        },
        "slotTypeId": "7FEVCB2PQE"
      }
    },
    "expression": "(firstname OR eyeColor)"
  }
}
```

## Slot type file

structure

The slot type file contains the configuration information for
a custom slot type used in a language or locale. There is one
slot type file in the .zip file for each custom slot type in a
specific locale.

The following is the JSON structure for the slot type that
lists the types of cars available in the BookTrip example bot.
For a complete example of the JSON structure for a slot type,
see the [CreateSlotType](../APIReference/API_CreateSlotType.md "../APIReference/API_CreateSlotType.md") operation.

```
{
    "name": "CarTypeValues",
    "identifier": "T1YUHGD9ZR",
    "description": "Enumeration representing possible types of cars available for hire",
    "slotTypeValues": [{
        "synonyms": null,
        "sampleValue": {
            "value": "economy"
        }
    }, {
        "synonyms": null,
        "sampleValue": {
            "value": "standard"
        }
    }, {
        "synonyms": null,
        "sampleValue": {
            "value": "midsize"
        }
    }, {
        "synonyms": null,
        "sampleValue": {
            "value": "full size"
        }
    }, {
        "synonyms": null,
        "sampleValue": {
            "value": "luxury"
        }
    }, {
        "synonyms": null,
        "sampleValue": {
            "value": "minivan"
        }
    }],
    "parentSlotTypeSignature": null,
    "valueSelectionSetting": {
        "resolutionStrategy": "TOP_RESOLUTION",
        "advancedRecognitionSetting": {
            "audioRecognitionStrategy": "UseSlotValuesAsCustomVocabulary"
        },
        "regexFilter": null
    }
}
```

The following example shows the JSON structure for a composite slot type.

```
{
  "name": "CarCompositeType",
  "identifier": "TPA3CC9V",
  "description": null,
  "slotTypeValues": null,
  "parentSlotTypeSignature": null,
  "valueSelectionSetting": {
    "regexFilter": null,
    "resolutionStrategy": "CONCATENATION"
  },
  "compositeSlotTypeSetting": {
    "subSlots": [
      {
        "name": "model",
        "slotTypeId": "MODELTYPEID" # custom slot type Id for model
      },
      {
        "name": "city",
        "slotTypeId": "AMAZON.City"
      },
      {
        "name": "country",
        "slotTypeId": "AMAZON.Country"
      },
      {
        "name": "make",
        "slotTypeId": "MAKETYPEID" # custom slot type Id for make
      }
    ]
  }
}
```

The following is a slot type that uses a custom grammar to
understand the customer's utterances. For more information,
see [Grammar slot type](building-srgs.md "building-srgs.md").

```
{
  "name": "custom_grammar",
  "identifier": "7KEAQIQKPX",
  "description": "Slot type using a custom grammar",
  "slotTypeValues": null,
  "parentSlotTypeSignature": null,
  "valueSelectionSetting": null,
  "externalSourceSetting": {
    "grammarSlotTypeSetting": {
      "source": {
        "kmsKeyArn": "arn:aws:kms:`Region`:`123456789012`:alias/customer-grxml-key",
        "s3BucketName": "grxml-test",
        "s3ObjectKey": "grxml_files/grammar.grxml"
      }
    }
  }
}
```

## Custom vocabulary file

structure

The custom vocabulary file contains the entries in a custom
vocabulary for single language or locale. There is one custom
vocabulary file in the .zip file for each locale that has a
custom vocabulary.

The following is a custom vocabulary file for a bot that takes
restaurant orders. There is one file per locale in the
bot.

```
{
    "customVocabularyItems": [
        {
            "weight": 3,
            "phrase": "wafers"
        },
        {
            "weight": null,
            "phrase": "extra large"
        },
        {
            "weight": null,
            "phrase": "cremini mushroom soup"
        },
        {
            "weight": null,
            "phrase": "ramen"
        },
        {
            "weight": null,
            "phrase": "orzo"
        }
    ]
}
```
