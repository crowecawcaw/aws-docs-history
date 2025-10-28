# Converse API tool use examples

You can use the [Converse API](conversation-inference.md "conversation-inference.md") to let a
model use a tool in a conversation. The following Python examples show
how to use a tool that returns the most popular song on a fictional radio station. The
[Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") example shows how to synchronously use a tool. The [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") example
shows how use a tool asynchronously. For other code examples, see [Code examples for Amazon Bedrock Runtime using AWS SDKs](service_code_examples_bedrock-runtime.md "service_code_examples_bedrock-runtime.md").

Converse
This example shows how to use a tool with the `Converse`
operation with the _Command R_ model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to use tools with the <noloc>Converse</noloc> API and the Cohere Command R model.
"""

import logging
import json
import boto3


from botocore.exceptions import ClientError


class StationNotFoundError(Exception):
    """Raised when a radio station isn't found."""
    pass


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_top_song(call_sign):
    """Returns the most popular song for the requested station.
    Args:
        call_sign (str): The call sign for the station for which you want
        the most popular song.

    Returns:
        response (json): The most popular song and artist.
    """

    song = ""
    artist = ""
    if call_sign == 'WZPZ':
        song = "Elemental Hotel"
        artist = "8 Storey Hike"

    else:
        raise StationNotFoundError(f"Station {call_sign} not found.")

    return song, artist


def generate_text(bedrock_client, model_id, tool_config, input_text):
    """Generates text using the supplied Amazon Bedrock model. If necessary,
    the function handles tool use requests and sends the result to the model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The Amazon Bedrock model ID.
        tool_config (dict): The tool configuration.
        input_text (str): The input text.
    Returns:
        Nothing.
    """

    logger.info("Generating text with model %s", model_id)

   # Create the initial message from the user input.
    messages = [{
        "role": "user",
        "content": [{"text": input_text}]
    }]

    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages,
        toolConfig=tool_config
    )

    output_message = response['output']['message']
    messages.append(output_message)
    stop_reason = response['stopReason']

    if stop_reason == 'tool_use':
        # Tool use requested. Call the tool and send the result to the model.
        tool_requests = response['output']['message']['content']
        for tool_request in tool_requests:
            if 'toolUse' in tool_request:
                tool = tool_request['toolUse']
                logger.info("Requesting tool %s. Request: %s",
                            tool['name'], tool['toolUseId'])

                if tool['name'] == 'top_song':
                    tool_result = {}
                    try:
                        song, artist = get_top_song(tool['input']['sign'])
                        tool_result = {
                            "toolUseId": tool['toolUseId'],
                            "content": [{"json": {"song": song, "artist": artist}}]
                        }
                    except StationNotFoundError as err:
                        tool_result = {
                            "toolUseId": tool['toolUseId'],
                            "content": [{"text":  err.args[0]}],
                            "status": 'error'
                        }

                    tool_result_message = {
                        "role": "user",
                        "content": [
                            {
                                "toolResult": tool_result

                            }
                        ]
                    }
                    messages.append(tool_result_message)

                    # Send the tool result to the model.
                    response = bedrock_client.converse(
                        modelId=model_id,
                        messages=messages,
                        toolConfig=tool_config
                    )
                    output_message = response['output']['message']

    # print the final response from the model.
    for content in output_message['content']:
        print(json.dumps(content, indent=4))


def main():
    """
    Entrypoint for tool use example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "cohere.command-r-v1:0"
    input_text = "What is the most popular song on WZPZ?"

    tool_config = {
    "tools": [
        {
            "toolSpec": {
                "name": "top_song",
                "description": "Get the most popular song played on a radio station.",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "sign": {
                                "type": "string",
                                "description": "The call sign for the radio station for which you want the most popular song. Example calls signs are WZPZ, and WKRP."
                            }
                        },
                        "required": [
                            "sign"
                        ]
                    }
                }
            }
        }
    ]
}
    bedrock_client = boto3.client(service_name='bedrock-runtime')


    try:
        print(f"Question: {input_text}")
        generate_text(bedrock_client, model_id, tool_config, input_text)

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        print(f"A client error occured: {message}")

    else:
        print(
            f"Finished generating text with model {model_id}.")


if __name__ == "__main__":
    main()

```

ConverseStream
This example shows how to use a tool with the `ConverseStream`
streaming operation and the _Anthropic Claude 3 Haiku_
model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to use a tool with a streaming conversation.
"""

import logging
import json
import boto3

from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class StationNotFoundError(Exception):
    """Raised when a radio station isn't found."""
    pass


def get_top_song(call_sign):
    """Returns the most popular song for the requested station.
    Args:
        call_sign (str): The call sign for the station for which you want
        the most popular song.

    Returns:
        response (json): The most popular song and artist.
    """

    song = ""
    artist = ""
    if call_sign == 'WZPZ':
        song = "Elemental Hotel"
        artist = "8 Storey Hike"

    else:
        raise StationNotFoundError(f"Station {call_sign} not found.")

    return song, artist


def stream_messages(bedrock_client,
                    model_id,
                    messages,
                    tool_config):
    """
    Sends a message to a model and streams the response.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        messages (JSON) : The messages to send to the model.
        tool_config : Tool Information to send to the model.

    Returns:
        stop_reason (str): The reason why the model stopped generating text.
        message (JSON): The message that the model generated.

    """

    logger.info("Streaming messages with model %s", model_id)

    response = bedrock_client.converse_stream(
        modelId=model_id,
        messages=messages,
        toolConfig=tool_config
    )

    stop_reason = ""

    message = {}
    content = []
    message['content'] = content
    text = ''
    tool_use = {}


    #stream the response into a message.
    for chunk in response['stream']:
        if 'messageStart' in chunk:
            message['role'] = chunk['messageStart']['role']
        elif 'contentBlockStart' in chunk:
            tool = chunk['contentBlockStart']['start']['toolUse']
            tool_use['toolUseId'] = tool['toolUseId']
            tool_use['name'] = tool['name']
        elif 'contentBlockDelta' in chunk:
            delta = chunk['contentBlockDelta']['delta']
            if 'toolUse' in delta:
                if 'input' not in tool_use:
                    tool_use['input'] = ''
                tool_use['input'] += delta['toolUse']['input']
            elif 'text' in delta:
                text += delta['text']
                print(delta['text'], end='')
        elif 'contentBlockStop' in chunk:
            if 'input' in tool_use:
                tool_use['input'] = json.loads(tool_use['input'])
                content.append({'toolUse': tool_use})
                tool_use = {}
            else:
                content.append({'text': text})
                text = ''

        elif 'messageStop' in chunk:
            stop_reason = chunk['messageStop']['stopReason']

    return stop_reason, message


def main():
    """
    Entrypoint for streaming tool use example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-haiku-20240307-v1:0"
    input_text = "What is the most popular song on WZPZ?"

    try:
        bedrock_client = boto3.client(service_name='bedrock-runtime')

        # Create the initial message from the user input.
        messages = [{
            "role": "user",
            "content": [{"text": input_text}]
        }]

        # Define the tool to send to the model.
        tool_config = {
            "tools": [
                {
                    "toolSpec": {
                        "name": "top_song",
                        "description": "Get the most popular song played on a radio station.",
                        "inputSchema": {
                            "json": {
                                "type": "object",
                                "properties": {
                                    "sign": {
                                        "type": "string",
                                        "description": "The call sign for the radio station for which you want the most popular song. Example calls signs are WZPZ and WKRP."
                                    }
                                },
                                "required": ["sign"]
                            }
                        }
                    }
                }
            ]
        }


        # Send the message and get the tool use request from response.
        stop_reason, message = stream_messages(
            bedrock_client, model_id, messages, tool_config)
        messages.append(message)

        if stop_reason == "tool_use":

            for content in message['content']:
                if 'toolUse' in content:
                    tool = content['toolUse']

                    if tool['name'] == 'top_song':
                        tool_result = {}
                        try:
                            song, artist = get_top_song(tool['input']['sign'])
                            tool_result = {
                                "toolUseId": tool['toolUseId'],
                                "content": [{"json": {"song": song, "artist": artist}}]
                            }
                        except StationNotFoundError as err:
                            tool_result = {
                                "toolUseId": tool['toolUseId'],
                                "content": [{"text":  err.args[0]}],
                                "status": 'error'
                            }

                        tool_result_message = {
                            "role": "user",
                            "content": [
                                {
                                    "toolResult": tool_result

                                }
                            ]
                        }
                        # Add the result info to message.
                        messages.append(tool_result_message)

        #Send the messages, including the tool result, to the model.
        stop_reason, message  = stream_messages(
            bedrock_client, model_id, messages, tool_config)


    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        print("A client error occured: " +
              format(message))

    else:
        print(
            f"\nFinished streaming messages with model {model_id}.")


if __name__ == "__main__":
    main()

```
