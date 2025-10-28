# Use a computer use tool to complete an Amazon Bedrock model response

Computer use is an Anthropic Claude model capability (in beta) available with
Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. With computer use, Claude can help you automate
tasks through basic GUI actions.

###### Warning

Computer use feature is made available to you as a ‘Beta Service’ as defined in the AWS Service Terms. It is subject to your Agreement with AWS and the AWS Service Terms, and the applicable model EULA. Please be aware that the Computer Use API poses
unique risks that are distinct from standard API features or chat interfaces. These risks are
heightened when using the Computer Use API to interact with the Internet. To minimize risks,
consider taking precautions such as:

- Operate computer use functionality in a dedicated Virtual Machine or container with minimal privileges to
  prevent direct system attacks or accidents.
- To prevent information theft, avoid giving the Computer Use API access to sensitive accounts or data.
- Limiting the computer use API’s internet access to required domains to reduce exposure to malicious
  content.
- To ensure proper oversight, keep a human in the loop for sensitive tasks (such as making decisions that
  could have meaningful real-world consequences) and for anything requiring affirmative consent (such as
  accepting cookies, executing financial transactions, or agreeing to terms of service).
  Any content that you enable Claude to see or access can potentially override instructions or cause
  Claude to make mistakes or perform unintended actions. Taking proper precautions, such as
  isolating Claude from sensitive surfaces, is essential — including to avoid risks related to prompt
  injection.
  Before enabling or requesting permissions necessary to enable computer use features in your own
  products, please inform end users of any relevant risks, and obtain their consent as appropriate.

The computer use API offers several pre-defined computer use tools
(_computer_20241022_, _bash_20241022_, and
_text_editor_20241022_) for you to use. You can then create a prompt
with your request, such as “send an email to Ben with the notes from my last meeting” and a
screenshot (when required). The response contains a list of `tool_use` actions in
JSON format (for example, scroll_down, left_button_press, screenshot). Your code runs the
computer actions and provides Claude with screenshot showcasing outputs (when
requested).

The tools parameter has been updated to accept polymorphic tool types; a new `tool.type`
property is being added to distinguish them. `type` is optional; if omitted, the tool is
assumed to be a custom tool (previously the only tool type supported). Additionally, a new
parameter, `anthropic_beta`, has been added, with a corresponding enum value:
`computer-use-2024-10-22`. Only requests made with this parameter and enum can use the new
computer use tools. It can be specified as follows: `"anthropic_beta":
 ["computer-use-2024-10-22"]` .

To use computer use with Anthropic Claude 3.5 Sonnet v2 you can use the Converse API
([Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md")). You specify the computer use specific fields in the
`additionalModelRequestFields` field. For general information about calling
the Converse API, see [Carry out a conversation with the
Converse API operations](conversation-inference.md "conversation-inference.md").

It is possible to use tools with the base inference operations ([InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or
[InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")). To find the inference parameters that you pass in the request body,
see the [Anthropic Claude
Messages API](model-parameters-anthropic-claude-messages.md "model-parameters-anthropic-claude-messages.md").

For more information, see [Computer use
(beta)](https://docs.anthropic.com/en/docs/build-with-claude/computer-use "https://docs.anthropic.com/en/docs/build-with-claude/computer-use") in the Anthropic documentation.

###### Topics

- [Example code](#computer-use-example-code "#computer-use-example-code")
- [Example response](#example-response "#example-response")

## Example code

The following code shows how to call the computer use API. The input is an image of the AWS console.

```
with open('test_images/console.png', 'rb') as f:
        png = f.read()

    response = bedrock.converse(
        modelId='anthropic.claude-3-5-sonnet-20241022-v2:0',
        messages=[
            {
                'role': 'user',
                'content': [
                    {
                        'text': 'Go to the bedrock console'
                    },
                    {
                        'image': {
                            'format': 'png',
                            'source': {
                                'bytes': png
                            }
                        }
                    }
                ]
            }
        ],
        additionalModelRequestFields={
            "tools": [
                {
                    "type": "computer_20241022",
                    "name": "computer",
                    "display_height_px": 768,
                    "display_width_px": 1024,
                    "display_number": 0
                },
                {
                    "type": "bash_20241022",
                    "name": "bash",

                },
                {
                    "type": "text_editor_20241022",
                    "name": "str_replace_editor",
                }
            ],
            "anthropic_beta": ["computer-use-2024-10-22"]
        },
        toolConfig={
            'tools': [
                {
                    'toolSpec': {
                        'name': 'get_weather',
                        'inputSchema': {
                            'json': {
                                'type': 'object'
                            }
                        }
                    }
                }
            ]
        })

    print(json.dumps(response, indent=4))
```

## Example response

The example code emits output similar to the following.

```
{
   "id": "msg_bdrk_01Ch8g9MF3A9FTrmeywrwfMZ",
   "type": "message",
   "role": "assistant",
   "content": [
        {
            "type": "text",
            "text": "I can see from the screenshot that we're already in the AWS Console. To go to the Amazon Bedrock console specifically, I'll click on the Amazon Bedrock service from the \"Recently Visited\" section."
        },
        {
            "type": "tool_use",
            "id": "toolu_bdrk_013sAzs1gsda9wLrfD8bhYQ3",
            "name": "computer",
            "input": {
                "action": "screenshot"
            }
        }
   ],
   "stop_reason": "tool_use",
   "stop_sequence": null,
   "usage": {
       "input_tokens": 3710,
       "output_tokens": 97
   }
}
```
