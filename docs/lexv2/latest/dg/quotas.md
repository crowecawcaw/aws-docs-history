# Quotas

Service quotas, also referred to as limits, are the maximum number of service
resources allowed for your AWS account. For more information, see [AWS service
quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the _AWS general reference_.

Some service quotas can be adjusted or increased. Refer to the
**Adjustable** column in the following tables to see whether
a quota can be adjusted and to the **Self-service** column to
see whether you can request a quota adjustment through the
[Service quotas](https://console.aws.amazon.com/servicequotas/home/services/lex/quotas "https://console.aws.amazon.com/servicequotas/home/services/lex/quotas")
console. Contact Support to increase a quota that is adjustable, but not through self-service.
It can take a few days to increase a service quota. If you're increasing your quota as part of
a larger project, be sure to add this time to your plan.

###### Note

Character limits are calculated as the number of [Unicode code units](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Character.html#unicode "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Character.html#unicode"). In most cases, one Unicode character is equivalent to one Unicode code unit. Some special characters might be greater than one unit and counts might differ for different encodings. For more information on calculating string length, see [this documentation](<https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#length()> "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#length()").

## Build-time quotas

The following maximum quotas are enforced when you are
creating a bot.

| Description                                                                                                 | Default                                                                        | Adjustable | Self-service |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------- | ------------ |
| Bots per AWS account                                                                                        | 100                                                                            | Yes        | Yes          |
| Bot channel associations per AWS<br>account                                                                 | 5,000                                                                          | No         | N/A          |
| Parallel locale builds per AWS account                                                                      | 5                                                                              | Yes        | No           |
| Bots per bot network                                                                                        | 5                                                                              | No         | N/A          |
| Bot networks per bot                                                                                        | 25                                                                             | No         | N/A          |
| Versions per bot                                                                                            | 100                                                                            | No         | N/A          |
| Intents per locale in each bot                                                                              | • 1,000 in en-AU, en-GB, and<br>en-US<br>• 250 in all other locales            | Yes        | No           |
| Slots per locale in each bot                                                                                | • 4,000 in en-AU, en-GB, and<br>en-US<br>• 2,000 in all other locales          | No         | N/A          |
| Custom slot types per bot locale                                                                            | • 250 in en-AU, en-GB, and<br>en-US<br>• 100 in all other locales              | No         | N/A          |
| Custom slot type values and synonyms per<br>locale in each bot                                              | 50,000                                                                         | No         | N/A          |
| Total characters in sample utterances per<br>locale in each bot                                             | • 2,000,000 in en-AU, en-GB, and<br>en-US<br>• 200,000 in all other<br>locales | No         | N/A          |
| Channel associations per bot alias                                                                          | 10                                                                             | No         | N/A          |
| Slots per intent                                                                                            | 100                                                                            | No         | N/A          |
| Sample utterances per intent                                                                                | 1,500                                                                          | Yes        | Yes          |
| Characters per sample utterance                                                                             | 500                                                                            | No         | N/A          |
| Text response length                                                                                        | 4,000                                                                          | No         | N/A          |
| Sample utterances per slot                                                                                  | 10                                                                             | Yes        | Yes          |
| Characters per sample slot utterance                                                                        | 500                                                                            | No         | N/A          |
| Prompts per slot                                                                                            | 30                                                                             | No         | N/A          |
| Values and synonyms per custom slot<br>type                                                                 | 10,000                                                                         | No         | N/A          |
| Characters per custom slot type value                                                                       | 500                                                                            | No         | N/A          |
| Characters in a channel association<br>name                                                                 | 100                                                                            | No         | N/A          |
| Number of concurrent Automated Chatbot Designer analysis jobs<br>across all bots in your account per Region | 10                                                                             | No         | N/A          |
| Size of custom grammar slot type XML file                                                                   | 100 KB                                                                         | No         | N/A          |

## Runtime quotas

The following maximum quotas are enforced at runtime.

| Description                                                                                                                                                                                                                                                         | Default         | Adjustable | Self-service |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ---------- | ------------ |
| Input text size for [RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md")<br>and [RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md") | 1024 characters | No         | N/A          |
| Speech input length for<br>`RecognizeUtterance`<br>operation                                                                                                                                                                                                        | 55 seconds      | Yes        | No           |
| Size of `RecognizeUtterance`<br>headers                                                                                                                                                                                                                             | 16 KB           | No         | N/A          |
| Size of combined request and session headers<br>for `RecognizeUtterance`                                                                                                                                                                                            | 12 KB           | No         | N/A          |
| Maximum number of concurrent text-mode<br>conversations for `RecognizeText`,<br>`RecognizeUtterance`, or<br>`StartConversation` for the<br>TestBotAlias                                                                                                             | 2               | No         | N/A          |
| Maximum number of concurrent text-mode<br>conversations for `RecognizeText`,<br>`RecognizeUtterance`, or<br>`StartConversation` for other<br>aliases                                                                                                                | 50              | Yes        | No           |
| Maximum number of concurrent voice-mode<br>conversations for<br>`RecognizeUtterance` for the<br>TestBotAlias                                                                                                                                                        | 2               | No         | N/A          |
| Maximum number of concurrent voice-mode<br>conversations for<br>`RecognizeUtterance` for other<br>aliases                                                                                                                                                           | 125             | Yes        | No           |
| Maximum number of concurrent voice-mode<br>conversations for `StartConversation`<br>for the TestBotAlias                                                                                                                                                            | 2               | No         | N/A          |
| Maximum number of concurrent voice-mode<br>conversations for `StartConversation`<br>for other aliases                                                                                                                                                               | 200             | Yes        | No           |
| Maximum number of concurrent session<br>management operations (`PutSession`,<br>`GetSession`, or<br>`DeleteSession`) when using the<br>TestBotAlias                                                                                                                 | 2               | No         | N/A          |
| Maximum number of concurrent session<br>management operations (`PutSession`,<br>`GetSession`, or<br>`DeleteSession`) when using other<br>aliases                                                                                                                    | 50              | Yes        | No           |
| Maximum input size to a Lambda<br>function                                                                                                                                                                                                                          | 12 KB           | No         | N/A          |
| Maximum output size of a Lambda<br>function                                                                                                                                                                                                                         | 50 KB           | No         | N/A          |
| Maximum size of session attributes in Lambda<br>function output (after base-64 encoding)                                                                                                                                                                            | 12 KB           | No         | N/A          |
| Maximum timeout of a Lambda function                                                                                                                                                                                                                                | 30 seconds      | Yes        | No           |
| Maximum duration for a single conversation                                                                                                                                                                                                                          | 15 minutes      | No         | No           |
| Maximum audio length                                                                                                                                                                                                                                                | 55 seconds      | No         | No           |
