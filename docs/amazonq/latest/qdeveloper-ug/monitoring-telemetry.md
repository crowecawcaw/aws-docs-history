# Identifying actions by specific users with Amazon CloudWatch Logs

It's possible to get user-level metrics on your Amazon Q Developer usage. To figure out which user
has taken a particular action, look for the events called SendTelemetryEvent, and examine
the JSON object of type SendTelemetryEventRequest that they contain. Within that object, the
schema appears as follows.

###### Tip

You can also output individual users' activity in Amazon Q Developer to a report in CSV
format. For more information, see [Viewing the activity of specific users in Amazon Q Developer](q-admin-user-telemetry.md "q-admin-user-telemetry.md").

```
http://json-schema.org/draft-07/schema#",
    "definitions": {
        "ProgrammingLanguage": {
            "type": "object",
            "properties": {
                "languageName": {
                    "type": "string",
                    "enum": [
                        "python",
                        "javascript",
                        "java",
                        "csharp",
                        "typescript",
                        "c",
                        "cpp",
                        "go",
                        "kotlin",
                        "php",
                        "ruby",
                        "rust",
                        "scala",
                        "shell",
                        "sql",
                        "json",
                        "yaml",
                        "vue",
                        "tf",
                        "tsx",
                        "jsx",
                        "plaintext"
                    ],
                    "description": "Programming Languages supported by Q"
                }
            }
        },
        "Dimension": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "must match ^[-a-zA-Z0-9._]*$ and be between 1 and 255 characters"
                },
                "value": {
                    "type": "string",
                    "description": "must match ^[-a-zA-Z0-9._]*$ and be between 1 and 1024 characters"
                }
            }
        }
    },
    "telemetryEvents": {
        "UserTriggerDecisionEvent": {
            "type": "object",
            "properties": {
                "sessionId": {
                    "type": "string",
                    "description": "UUID for the session"
                },
                "requestId": {
                    "type": "string",
                    "description": "UUID for the request"
                },
                "customizationArn": {
                    "type": "string",
                    "description": "ARN of the customization matching pattern: ^arn:[-.a-z0-9]{1,63}:codewhisperer:([-.a-z0-9]{0,63}:){2}([a-zA-Z0-9-_:/]){1,1023}$"
                },
                "programmingLanguage": {
                    "$ref": "#/definitions/ProgrammingLanguage"
                },
                "completionType": {
                    "type": "string",
                    "enum": [
                        "BLOCK",
                        "LINE"
                    ]
                },
                "suggestionState": {
                    "type": "string",
                    "enum": [
                        "ACCEPT",
                        "REJECT",
                        "DISCARD",
                        "EMPTY"
                    ]
                },
                "recommendationLatencyMilliseconds": {
                    "type": "number"
                },
                "timestamp": {
                    "type": "string",
                    "description": "datetime, example: Jul 23, 2024, 12:11:02 AM"
                },
                "triggerToResponseLatencyMilliseconds": {
                    "type": "number"
                },
                "suggestionReferenceCount": {
                    "type": "integer"
                },
                "generatedLine": {
                    "type": "integer"
                },
                "numberOfRecommendations": {
                    "type": "integer"
                }
            },
            "required": [
                "sessionId",
                "requestId",
                "programmingLanguage",
                "completionType",
                "suggestionState",
                "recommendationLatencyMilliseconds",
                "timestamp"
            ]
        },
        "CodeCoverageEvent": {
            "type": "object",
            "properties": {
                "customizationArn": {
                    "type": "string",
                    "description": "ARN of the customization matching pattern: ^arn:[-.a-z0-9]{1,63}:codewhisperer:([-.a-z0-9]{0,63}:){2}([a-zA-Z0-9-_:/]){1,1023}$"
                },
                "programmingLanguage": {
                    "$ref": "#/definitions/ProgrammingLanguage"
                },
                "acceptedCharacterCount": {
                    "type": "integer"
                },
                "totalCharacterCount": {
                    "type": "integer"
                },
                "timestamp": {
                    "type": "string",
                    "description": "datetime, example: Jul 23, 2024, 12:11:02 AM"
                },
                "unmodifiedAcceptedCharacterCount": {
                    "type": "integer"
                }
            },
            "required": [
                "programmingLanguage",
                "acceptedCharacterCount",
                "totalCharacterCount",
                "timestamp"
            ]
        },
        "UserModificationEvent": {
            "type": "object",
            "properties": {
                "sessionId": {
                    "type": "string",
                    "description": "UUID for the session"
                },
                "requestId": {
                    "type": "string",
                    "description": "UUID for the request"
                },
                "programmingLanguage": {
                    "$ref": "#/definitions/ProgrammingLanguage"
                },
                "modificationPercentage": {
                    "type": "number",
                    "description": "This is the percentage of AI generated code which has been modified by the user"
                },
                "customizationArn": {
                    "type": "string",
                    "description": "ARN of the customization matching pattern: ^arn:[-.a-z0-9]{1,63}:codewhisperer:([-.a-z0-9]{0,63}:){2}([a-zA-Z0-9-_:/]){1,1023}$"
                },
                "timestamp": {
                    "type": "string",
                    "description": "datetime, example: Jul 23, 2024, 12:11:02 AM"
                }
            },
            "required": [
                "sessionId",
                "requestId",
                "programmingLanguage",
                "modificationPercentage",
                "timestamp"
            ]
        },
        "CodeScanEvent": {
            "type": "object",
            "properties": {
                "programmingLanguage": {
                    "$ref": "#/definitions/ProgrammingLanguage"
                },
                "codeScanJobId": {
                    "type": "string"
                },
                "timestamp": {
                    "type": "string",
                    "description": "datetime, example: Jul 23, 2024, 12:11:02 AM"
                },
                "codeAnalysisScope": {
                    "type": "string",
                    "enum": [
                        "FILE",
                        "PROJECT"
                    ]
                }
            },
            "required": [
                "programmingLanguage",
                "codeScanJobId",
                "timestamp"
            ]
        },
        "CodeScanRemediationsEvent": {
            "type": "object",
            "properties": {
                "programmingLanguage": {
                    "$ref": "#/definitions/ProgrammingLanguage"
                },
                "CodeScanRemediationsEventType": {
                    "type": "string",
                    "enum": [
                        "CODESCAN_ISSUE_HOVER",
                        "CODESCAN_ISSUE_APPLY_FIX",
                        "CODESCAN_ISSUE_VIEW_DETAILS"
                    ]
                },
                "timestamp": {
                    "type": "string",
                    "description": "datetime, example: Jul 23, 2024, 12:11:02 AM"
                },
                "detectorId": {
                    "type": "string"
                },
                "findingId": {
                    "type": "string"
                },
                "ruleId": {
                    "type": "string"
                },
                "component": {
                    "type": "string"
                },
                "reason": {
                    "type": "string"
                },
                "result": {
                    "type": "string"
                },
                "includesFix": {
                    "type": "boolean"
                }
            }
        },
        "MetricData": {
            "type": "object",
            "properties": {
                "metricName": {
                    "type": "string",
                    "description": "must match pattern ^[-a-zA-Z0-9._]*$ and be between 1 and 1024 characters"
                },
                "metricValue": {
                    "type": "number"
                },
                "timestamp": {
                    "type": "string",
                    "description": "datetime, example: Jul 23, 2024, 12:11:02 AM"
                },
                "product": {
                    "type": "string",
                    "description": "must match pattern ^[-a-zA-Z0-9._]*$ and be between 1 and 128 characters"
                },
                "dimensions": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Dimension"
                    },
                    "description": "maximum size of 30"
                }
            },
            "required": [
                "metricName",
                "metricValue",
                "timestamp",
                "product"
            ]
        },
        "ChatAddMessageEvent": {
            "type": "object",
            "properties": {
                "conversationId": {
                    "type": "string",
                    "description": "ID which represents a multi-turn conversation, length between 1 and 128"
                },
                "messageId": {
                    "type": "string",
                    "description": "Unique identifier for the chat message"
                },
                "customizationArn": {
                    "type": "string",
                    "description": "ARN of the customization matching pattern: ^arn:[-.a-z0-9]{1,63}:codewhisperer:([-.a-z0-9]{0,63}:){2}([a-zA-Z0-9-_:/]){1,1023}$"
                },
                "userIntent": {
                    "type": "string",
                    "enum": [
                        "SUGGEST_ALTERNATE_IMPLEMENTATION",
                        "APPLY_COMMON_BEST_PRACTICES",
                        "IMPROVE_CODE",
                        "SHOW_EXAMPLES",
                        "CITE_SOURCES",
                        "EXPLAIN_LINE_BY_LINE",
                        "EXPLAIN_CODE_SELECTION",
                        "GENERATE_CLOUDFORMATION_TEMPLATE"
                    ]
                },
                "hasCodeSnippet": {
                    "type": "boolean"
                },
                "programmingLanguage": {
                    "$ref": "#/definitions/ProgrammingLanguage"
                },
                "activeEditorTotalCharacters": {
                    "type": "integer"
                },
                "timeToFirstChunkMilliseconds": {
                    "type": "number"
                },
                "timeBetweenChunks": {
                    "type": "array",
                    "items": {
                        "type": "number"
                    },
                    "description": "maximum size of 100"
                },
                "fullResponselatency": {
                    "type": "number"
                },
                "requestLength": {
                    "type": "integer"
                },
                "responseLength": {
                    "type": "integer"
                },
                "numberOfCodeBlocks": {
                    "type": "integer"
                },
                "hasProjectLevelContext": {
                    "type": "boolean"
                }
            },
            "required": [
                "conversationId",
                "messageId"
            ]
        },
        "ChatInteractWithMessageEvent": {
            "type": "object",
            "properties": {
                "conversationId": {
                    "type": "string",
                    "description": "ID which represents a multi-turn conversation, length between 1 and 128"
                },
                "messageId": {
                    "type": "string",
                    "description": "Unique identifier for the chat message"
                },
                "customizationArn": {
                    "type": "string",
                    "description": "ARN of the customization matching pattern: ^arn:[-.a-z0-9]{1,63}:codewhisperer:([-.a-z0-9]{0,63}:){2}([a-zA-Z0-9-_:/]){1,1023}$"
                },
                "interactionType": {
                    "type": "string",
                    "enum": [
                        "INSERT_AT_CURSOR",
                        "COPY_SNIPPET",
                        "COPY",
                        "CLICK_LINK",
                        "CLICK_BODY_LINK",
                        "CLICK_FOLLOW_UP",
                        "HOVER_REFERENCE",
                        "UPVOTE",
                        "DOWNVOTE"
                    ],
                    "description": "Chat Message Interaction Type"
                },
                "interactionTarget": {
                    "type": "string",
                    "description": "Target of message interaction"
                },
                "acceptedCharacterCount": {
                    "type": "integer"
                },
                "acceptedLineCount": {
                    "type": "integer"
                },
                "acceptedSnippetHasReference": {
                    "type": "boolean"
                },
                "hasProjectLevelContext": {
                    "type": "boolean"
                }
            },
            "required": [
                "conversationId",
                "messageId"
            ]
        },
        "ChatUserModificationEvent": {
            "type": "object",
            "properties": {
                "conversationId": {
                    "type": "string",
                    "description": "ID which represents a multi-turn conversation, length between 1 and 128"
                },
                "customizationArn": {
                    "type": "string",
                    "description": "ARN of the customization matching pattern: ^arn:[-.a-z0-9]{1,63}:codewhisperer:([-.a-z0-9]{0,63}:){2}([a-zA-Z0-9-_:/]){1,1023}$"
                },
                "messageId": {
                    "type": "string",
                    "description": "Unique identifier for the chat message"
                },
                "programmingLanguage": {
                    "$ref": "#/definitions/ProgrammingLanguage"
                },
                "modificationPercentage": {
                    "type": "number",
                    "description": "This is the percentage of AI generated code which has been modified by the user"
                },
                "hasProjectLevelContext": {
                    "type": "boolean"
                }
            },
            "required": [
                "conversationId",
                "messageId",
                "modificationPercentage"
            ]
        },
        "SuggestionState": {
            "type": "string",
            "enum": [
                "ACCEPT",
                "REJECT",
                "DISCARD",
                "EMPTY"
            ]
        },
        "TerminalUserInteractionEvent": {
            "type": "object",
            "properties": {
                "terminalUserInteractionEventType": {
                    "type": "string",
                    "enum": [
                        "CODEWHISPERER_TERMINAL_TRANSLATION_ACTION",
                        "CODEWHISPERER_TERMINAL_COMPLETION_INSERTED"
                    ],
                    "description": "Terminal User Interaction Event Type"
                },
                "terminal": {
                    "type": "string"
                },
                "terminalVersion": {
                    "type": "string"
                },
                "shell": {
                    "type": "string"
                },
                "shellVersion": {
                    "type": "string"
                },
                "duration": {
                    "type": "integer"
                },
                "timeToSuggestion": {
                    "type": "integer"
                },
                "isCompletionAccepted": {
                    "type": "boolean"
                },
                "cliToolCommand": {
                    "type": "string"
                }
            }
        },
        "FeatureDevEvent": {
            "type": "object",
            "properties": {
                "conversationId": {
                    "type": "string",
                    "description": "ID which represents a multi-turn conversation, length between 1 and 128"
                }
            },
            "required": [
                "conversationId"
            ]
        }
    },
    "SendTelemetryEventRequest": {
        "type": "object",
        "properties": {
            "clientToken": {
                "type": "string",
                "description": "The client's authentication token"
            },
            "telemetryEvent": {
                "properties": {
                    "oneOf": [
                        {
                            "_comment": "This event is emitted when a user accepts or rejects an inline code suggestion",
                            "$ref": "#/definitions/userTriggerDecisionEvent"
                        },
                        {
                            "_comment": "This event is emitted every five minutes. It details how much code is written by inline code suggestion and in total during that period",
                            "$ref": "#/definitions/codeCoverageEvent"
                        },
                        {
                            "_comment": "This event is emitted when a code snippet from inline code suggestion has been edited by a user. It details the percentage of that code snippet modified by the user",
                            "$ref": "#/definitions/userModificationEvent"
                        },
                        {
                            "_comment": "This field is emitted when a security scan is requested by a user",
                            "$ref": "#/definitions/codeScanEvent"
                        },
                        {
                            "_comment": "This field is emitted when a security scan recommended remediation is accepted by a user",
                            "$ref": "#/definitions/codeScanRemediationsEvent"
                        },
                        {
                            "_comment": "This event is deprecated but may still occur in telemetry. Do not use this.",
                            "$ref": "#/definitions/metricData"
                        },
                        {
                            "_comment": "This event is emitted when Q adds an AI generated message to the chat window",
                            "$ref": "#/definitions/chatAddMessageEvent"
                        },
                        {
                            "_comment": "This event is emitted when a user interacts with a chat message",
                            "$ref": "#/definitions/chatInteractWithMessageEvent"
                        },
                        {
                            "_comment": "This event is emitted when a user modifies a code snippet sourced from chat. It gives a percentage of the code snippet which has been modified",
                            "$ref": "#/definitions/chatUserModificationEvent"
                        },
                        {
                            "_comment": "This event is emitted when a user interacts with a terminal suggestion",
                            "$ref": "#/definitions/terminalUserInteractionEvent"
                        },
                        {
                            "_comment": "This event is emitted when a user first prompts the /dev feature.",
                            "$ref": "#/definitions/featureDevEvent"
                        }
                    ]
                }
            },
            "optOutPreference": {
                "type": "string",
                "enum": [
                    "OPTIN",
                    "OPTOUT"
                ],
                "description": "OPTOUT and telemetry is only provided to the account of purchasing enterprise, OPTIN and telemetry may also be used for product improvement"
            },
            "userContext": {
                "type": "object",
                "properties": {
                    "ideCategory": {
                        "type": "string",
                        "enum": [
                            "JETBRAINS",
                            "VSCODE",
                            "CLI",
                            "JUPYTER_MD",
                            "JUPYTER_SM"
                        ]
                    },
                    "operatingSystem": {
                        "type": "string",
                        "description": "The operating system being used"
                    },
                    "product": {
                        "type": "string",
                        "description": "The name of the product being used"
                    },
                    "clientId": {
                        "type": "string",
                        "description": "A UUID representing the individual client being used"
                    },
                    "ideVersion": {
                        "type": "string",
                        "description": "The version of the Q plugin"
                    }
                },
                "required": [
                    "ideCategory",
                    "operatingSystem",
                    "product",
                    "clientId",
                    "ideVersion"
                ]
            },
            "profileArn": {
                "type": "string",
                "description": "The arn of the Q Profile used to configure individual user accounts."
```

[Show moreShow less](# "#")Observe that a SendTelemetryEvent may contain one of a number of telemetry events. Each of
these describes a specific interaction between the development environment.

A more detailed description of each event appears below.

## UserTriggerDecisionEvent

This event is triggered when a user interacts with a suggestion made by Amazon Q. It
captures whether the suggestion was accepted, rejected, or modified, along with relevant
metadata.

- `completionType`: Whether the completion was a block or a
  line.
- `suggestionState`: Whether the user accepted, rejected, or
  discarded the suggestion.

## CodeScanEvent

This event is logged when a code scan is performed. It helps track the scope and
result of the scan, providing insights into security and code quality checks.

- `codeScanJobId`: The unique identifier for the code scan
  job.
- `codeAnalysisScope`: Whether the scan was performed at the file
  level or the project level.
- `programmingLanguage`: The language being scanned.

## CodeScanRemediationsEvent

This event captures user interactions with Amazon Q’s remediation suggestions, such as
applying fixes or viewing issue details.

- `CodeScanRemediationsEventType`: The type of remediation action
  taken (e.g., viewing details or applying a fix).
- `includesFix`: A boolean indicating whether the code issue includes
  a suggested fix.

## ChatAddMessageEvent

This event is triggered when a new message is added to an ongoing chat conversation.
It captures the user’s intent and any code snippets involved.

- `conversationId`: The unique identifier for the
  conversation.
- `messageId`: The unique identifier for the chat message.
- `userIntent`: The user’s intent, such as improving code or
  explaining code.
- `programmingLanguage`: The language related to the chat
  message.

## ChatInteractWithMessageEvent

This event captures when users interact with chat messages, such as copying code
snippets, clicking links, or hovering over references.

- `interactionType`: The type of interaction (for example, copy,
  hover, click).
- `interactionTarget`: The target of the interaction (for example, a
  code snippet or a link).
- `acceptedCharacterCount`: The number of characters from the message
  that were accepted.
- `acceptedSnippetHasReference`: A boolean indicating if the accepted
  snippet included a reference.

## TerminalUserInteractionEvent

This event logs user interactions with terminal commands or completions in the
terminal environment.

- `terminalUserInteractionEventType`: The type of interaction (for
  example, terminal translation or code completion).
- `isCompletionAccepted`: A boolean indicating whether the completion
  was accepted by the user.
- `duration`: The time taken for the interaction.
