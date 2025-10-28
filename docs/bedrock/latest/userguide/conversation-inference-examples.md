# Converse API

examples

The following examples show you how to use the `Converse` and
`ConverseStream` operations.

Text
This example shows how to call the `Converse` operation with
the _Anthropic Claude 3 Sonnet_ model. The example
shows how to send the input text, inference parameters, and additional
parameters that are unique to the model. The code starts a conversation by
asking the model to create a list of songs. It then continues the
conversation by asking that the songs are by artists from the United
Kingdom.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to use the <noloc>Converse</noloc> API with Anthropic Claude 3 Sonnet (on demand).
"""

import logging
import boto3

from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_conversation(bedrock_client,
                          model_id,
                          system_prompts,
                          messages):
    """
    Sends messages to a model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        system_prompts (JSON) : The system prompts for the model to use.
        messages (JSON) : The messages to send to the model.

    Returns:
        response (JSON): The conversation that the model generated.

    """

    logger.info("Generating message with model %s", model_id)

    # Inference parameters to use.
    temperature = 0.5
    top_k = 200

    # Base inference parameters to use.
    inference_config = {"temperature": temperature}
    # Additional inference parameters to use.
    additional_model_fields = {"top_k": top_k}

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompts,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_model_fields
    )

    # Log token usage.
    token_usage = response['usage']
    logger.info("Input tokens: %s", token_usage['inputTokens'])
    logger.info("Output tokens: %s", token_usage['outputTokens'])
    logger.info("Total tokens: %s", token_usage['totalTokens'])
    logger.info("Stop reason: %s", response['stopReason'])

    return response

def main():
    """
    Entrypoint for Anthropic Claude 3 Sonnet example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    # Setup the system prompts and messages to send to the model.
    system_prompts = [{"text": "You are an app that creates playlists for a radio station that plays rock and pop music. Only return song names and the artist."}]
    message_1 = {
        "role": "user",
        "content": [{"text": "Create a list of 3 pop songs."}]
    }
    message_2 = {
        "role": "user",
        "content": [{"text": "Make sure the songs are by artists from the United Kingdom."}]
    }
    messages = []

    try:

        bedrock_client = boto3.client(service_name='bedrock-runtime')

        # Start the conversation with the 1st message.
        messages.append(message_1)
        response = generate_conversation(
            bedrock_client, model_id, system_prompts, messages)

        # Add the response message to the conversation.
        output_message = response['output']['message']
        messages.append(output_message)

        # Continue the conversation with the 2nd message.
        messages.append(message_2)
        response = generate_conversation(
            bedrock_client, model_id, system_prompts, messages)

        output_message = response['output']['message']
        messages.append(output_message)

        # Show the complete conversation.
        for message in messages:
            print(f"Role: {message['role']}")
            for content in message['content']:
                print(f"Text: {content['text']}")
            print()

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

Image
This example shows how to send an image as part of a message and requests
that the model describe the image. The example uses `Converse`
operation and the _Anthropic Claude 3 Sonnet_ model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to send an image with the <noloc>Converse</noloc> API with an accompanying text prompt to Anthropic Claude 3 Sonnet (on demand).
"""

import logging
import boto3


from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_conversation(bedrock_client,
                          model_id,
                          input_text,
                          input_image):
    """
    Sends a message to a model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        input text : The text prompt accompanying the image.
        input_image : The path to the input image.

    Returns:
        response (JSON): The conversation that the model generated.

    """

    logger.info("Generating message with model %s", model_id)

    # Get image extension and read in image as bytes
    image_ext = input_image.split(".")[-1]
    with open(input_image, "rb") as f:
        image = f.read()

    message = {
        "role": "user",
        "content": [
            {
                "text": input_text
            },
            {
                "image": {
                    "format": image_ext,
                    "source": {
                        "bytes": image
                    }
                }
            }
        ]
    }

    messages = [message]

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages
    )

    return response


def main():
    """
    Entrypoint for Anthropic Claude 3 Sonnet example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    input_text = "What's in this image?"
    input_image = "path/to/image"

    try:

        bedrock_client = boto3.client(service_name="bedrock-runtime")

        response = generate_conversation(
            bedrock_client, model_id, input_text, input_image)

        output_message = response['output']['message']

        print(f"Role: {output_message['role']}")

        for content in output_message['content']:
            print(f"Text: {content['text']}")

        token_usage = response['usage']
        print(f"Input tokens:  {token_usage['inputTokens']}")
        print(f"Output tokens:  {token_usage['outputTokens']}")
        print(f"Total tokens:  {token_usage['totalTokens']}")
        print(f"Stop reason: {response['stopReason']}")

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

Document
This example shows how to send a document as part of a message and
requests that the model describe the contents of the document. The example
uses `Converse` operation and the _Anthropic
Claude 3 Sonnet_ model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to send an document as part of a message to Anthropic Claude 3 Sonnet (on demand).
"""

import logging
import boto3


from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_message(bedrock_client,
                     model_id,
                     input_text,
                     input_document_path):
    """
    Sends a message to a model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        input text : The input message.
        input_document_path : The path to the input document.

    Returns:
        response (JSON): The conversation that the model generated.

    """

    logger.info("Generating message with model %s", model_id)

    # Get format from path and read the path
    input_document_format = input_document_path.split(".")[-1]
    with open(input_document_path, 'rb') as input_document_file:
        input_document = input_document_file.read()

    # Message to send.
    message = {
        "role": "user",
        "content": [
            {
                "text": input_text
            },
            {
                "document": {
                    "name": "MyDocument",
                    "format": input_document_format,
                    "source": {
                        "bytes": input_document
                    }
                }
            }
        ]
    }

    messages = [message]

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages
    )

    return response


def main():
    """
    Entrypoint for Anthropic Claude 3 Sonnet example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    input_text = "What's in this document?"
    input_document_path = "path/to/document"

    try:

        bedrock_client = boto3.client(service_name="bedrock-runtime")


        response = generate_message(
            bedrock_client, model_id, input_text, input_document_path)

        output_message = response['output']['message']

        print(f"Role: {output_message['role']}")

        for content in output_message['content']:
            print(f"Text: {content['text']}")

        token_usage = response['usage']
        print(f"Input tokens:  {token_usage['inputTokens']}")
        print(f"Output tokens:  {token_usage['outputTokens']}")
        print(f"Total tokens:  {token_usage['totalTokens']}")
        print(f"Stop reason: {response['stopReason']}")

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

Streaming
This example shows how to call the `ConverseStream` operation
with the _Anthropic Claude 3 Sonnet_ model. The example
shows how to send the input text, inference parameters, and additional
parameters that are unique to the model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to use the <noloc>Converse</noloc> API to stream a response from Anthropic Claude 3 Sonnet (on demand).
"""

import logging
import boto3


from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def stream_conversation(bedrock_client,
                    model_id,
                    messages,
                    system_prompts,
                    inference_config,
                    additional_model_fields):
    """
    Sends messages to a model and streams the response.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        messages (JSON) : The messages to send.
        system_prompts (JSON) : The system prompts to send.
        inference_config (JSON) : The inference configuration to use.
        additional_model_fields (JSON) : Additional model fields to use.

    Returns:
        Nothing.

    """

    logger.info("Streaming messages with model %s", model_id)

    response = bedrock_client.converse_stream(
        modelId=model_id,
        messages=messages,
        system=system_prompts,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_model_fields
    )

    stream = response.get('stream')
    if stream:
        for event in stream:

            if 'messageStart' in event:
                print(f"\nRole: {event['messageStart']['role']}")

            if 'contentBlockDelta' in event:
                print(event['contentBlockDelta']['delta']['text'], end="")

            if 'messageStop' in event:
                print(f"\nStop reason: {event['messageStop']['stopReason']}")

            if 'metadata' in event:
                metadata = event['metadata']
                if 'usage' in metadata:
                    print("\nToken usage")
                    print(f"Input tokens: {metadata['usage']['inputTokens']}")
                    print(
                        f":Output tokens: {metadata['usage']['outputTokens']}")
                    print(f":Total tokens: {metadata['usage']['totalTokens']}")
                if 'metrics' in event['metadata']:
                    print(
                        f"Latency: {metadata['metrics']['latencyMs']} milliseconds")


def main():
    """
    Entrypoint for streaming message API response example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    system_prompt = """You are an app that creates playlists for a radio station
      that plays rock and pop music. Only return song names and the artist."""

    # Message to send to the model.
    input_text = "Create a list of 3 pop songs."

    message = {
        "role": "user",
        "content": [{"text": input_text}]
    }
    messages = [message]

    # System prompts.
    system_prompts = [{"text" : system_prompt}]

    # inference parameters to use.
    temperature = 0.5
    top_k = 200
    # Base inference parameters.
    inference_config = {
        "temperature": temperature
    }
    # Additional model inference parameters.
    additional_model_fields = {"top_k": top_k}

    try:
        bedrock_client = boto3.client(service_name='bedrock-runtime')

        stream_conversation(bedrock_client, model_id, messages,
                        system_prompts, inference_config, additional_model_fields)

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        print("A client error occured: " +
              format(message))

    else:
        print(
            f"Finished streaming messages with model {model_id}.")


if __name__ == "__main__":
    main()

```

Video
This example shows how to send a video as part of a message and requests
that the model describes the video. The example uses `Converse`
operation and the Amazon Nova Pro model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to send a video with the <noloc>Converse</noloc> API to Amazon Nova Pro (on demand).
"""

import logging
import boto3


from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_conversation(bedrock_client,
                          model_id,
                          input_text,
                          input_video):
    """
    Sends a message to a model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        input text : The input message.
        input_video : The input video.

    Returns:
        response (JSON): The conversation that the model generated.

    """

    logger.info("Generating message with model %s", model_id)

    # Message to send.

    with open(input_video, "rb") as f:
        video = f.read()

    message = {
        "role": "user",
        "content": [
            {
                "text": input_text
            },
            {
                    "video": {
                        "format": 'mp4',
                        "source": {
                            "bytes": video
                        }
                    }
            }
        ]
    }

    messages = [message]

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages
    )

    return response


def main():
    """
    Entrypoint for Amazon Nova Pro example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "amazon.nova-pro-v1:0"
    input_text = "What's in this video?"
    input_video = "path/to/video"

    try:

        bedrock_client = boto3.client(service_name="bedrock-runtime")

        response = generate_conversation(
            bedrock_client, model_id, input_text, input_video)

        output_message = response['output']['message']

        print(f"Role: {output_message['role']}")

        for content in output_message['content']:
            print(f"Text: {content['text']}")

        token_usage = response['usage']
        print(f"Input tokens:  {token_usage['inputTokens']}")
        print(f"Output tokens:  {token_usage['outputTokens']}")
        print(f"Total tokens:  {token_usage['totalTokens']}")
        print(f"Stop reason: {response['stopReason']}")

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
