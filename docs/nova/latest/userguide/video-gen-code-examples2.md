# Multi-shot video generation code examples

The following examples provide sample code for various multi-shot (longer than 6 seconds) video generation tasks.

Automated video generation
In this example, all shots in the video are generated from a single prompt and no input image is provided.

```
import json
import os

import boto3
from dotenv import load_dotenv

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Configure Nova Reel model inputs.
model_input = {
    "taskType": "MULTI_SHOT_AUTOMATED",
    "multiShotAutomatedParams": {
        "text": "Cinematic documentary showcasing the stunning beauty of the natural world. Drone footage flying over fantastical and varied natural wonders."
    },
    "videoGenerationConfig": {
        "seed": `1234`,
        "durationSeconds": `18`,  # Must be a multiple of 6 in range [12, 120]
        "fps": 24,  # Must be 24
        "dimension": "1280x720",  # Must be "1280x720"
    },
}

try:
    # Start the asynchronous video generation job.
    invocation = bedrock_runtime.start_async_invoke(
        modelId="amazon.nova-reel-v1:1",
        modelInput=model_input,
        outputDataConfig={"s3OutputDataConfig": {"s3Uri": "s3://`your-s3-bucket`"}},
    )

    # Print the response JSON.
    print(json.dumps(invocation, indent=2, default=str))

except Exception as err:
    print("Exception:")
    if hasattr(err, "response"):
        # Pretty print the response JSON.
        print(json.dumps(err.response, indent=2, default=str))
    else:
        print(err)
```

Manual video generation - Amazon S3 input image
In this example, a two shot video is generated. Each shot is generated with a separate prompt and input image that is provided in an Amazon S3 location.

```
import json
import os

import boto3
from dotenv import load_dotenv

# === Helper Function ===


def image_to_base64(image_path: str):
    """
    Convert an image file to a base64 encoded string.
    """
    import base64

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode("utf-8")


# === Main Code ===

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Configure Nova Reel model inputs. This example includes three shots, two of
# which include images to use as starting frames. These images are stored in S3.
model_input = {
    "taskType": "MULTI_SHOT_MANUAL",
    "multiShotManualParams": {
        "shots": [
            {"text": "aerial view of a city with tall glass and metal skyscrapers"},
            {
                "text": "closeup of a vehicle wheel in motion as the pavement speeds by with motion blur",
                "image": {
                    "format": "png",  # Must be "png" or "jpeg"
                    "source": {
                        "s3Location": {
                            "uri": "s3://`your-s3-bucket/images/SUV-wheel-closeup.png`"
                        }
                    },
                },
            },
            {
                "text": "tracking shot, the vehicle drives through the city, trees and buildings line the street",
                "image": {
                    "format": "png",  # Must be "png" or "jpeg"
                    "source": {
                        "s3Location": {
                            "uri": "s3://`your-s3-bucket/images/SUV-downtown-back.png`"
                        }
                    },
                },
            },
        ]
    },
    "videoGenerationConfig": {
        "seed": 1234,
        "fps": 24,  # Must be 24
        "dimension": "1280x720",  # Must be "1280x720"
    },
}

try:
    # Start the asynchronous video generation job.
    invocation = bedrock_runtime.start_async_invoke(
        modelId="amazon.nova-reel-v1:1",
        modelInput=model_input,
        outputDataConfig={"s3OutputDataConfig": {"s3Uri": "s3://`your-s3-bucket`"}},
    )

    # Print the response JSON.
    print(json.dumps(invocation, indent=2, default=str))

except Exception as err:
    print("Exception:")
    if hasattr(err, "response"):
        # Pretty print the response JSON.
        print(json.dumps(err.response, indent=2, default=str))
    else:
        print(err)
```

Manual video generation - base64 input image
In this example, a three shot video is generated. The first shot is generated with just a prompt, and the next two shot are generated with a new prompt and input image each.

```
import json
import os

import boto3
from dotenv import load_dotenv

# === Helper Function ===


def image_to_base64(image_path: str):
    """
    Convert an image file to a base64 encoded string.
    """
    import base64

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode("utf-8")


# === Main Code ===

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Configure Nova Reel model inputs. This example includes three shots, two of
# which include images to use as starting frames.
model_input = {
    "taskType": "MULTI_SHOT_MANUAL",
    "multiShotManualParams": {
        "shots": [
            {
                "text": "Drone footage of a Pacific Northwest forest with a meandering stream seen from a high altitude, top-down view"
            },
            {
                "text": "camera arcs slowly around two SUV vehicles in a forest setting with a stream in the background",
                "image": {
                    "format": "png",  # Must be "png" or "jpeg"
                    "source": {"bytes": image_to_base64("images/SUV-roadside.png")},
                },
            },
            {
                "text": "tracking shot, a SUV vehicle drives toward the camera through a forest roadway, the SUV's ring-shaped headlights glow white",
                "image": {
                    "format": "png",  # Must be "png" or "jpeg"
                    "source": {"bytes": image_to_base64("images/SUV-forest-front.png")},
                },
            },
        ]
    },
    "videoGenerationConfig": {
        "seed": 1234,
        "fps": 24,  # Must be 24
        "dimension": "1280x720",  # Must be "1280x720"
    },
}

try:
    # Start the asynchronous video generation job.
    invocation = bedrock_runtime.start_async_invoke(
        modelId="amazon.nova-reel-v1:1",
        modelInput=model_input,
        outputDataConfig={"s3OutputDataConfig": {"s3Uri": "s3://`your-s3-bucket`"}},
    )

    # Print the response JSON.
    print(json.dumps(invocation, indent=2, default=str))

except Exception as err:
    print("Exception:")
    if hasattr(err, "response"):
        # Pretty print the response JSON.
        print(json.dumps(err.response, indent=2, default=str))
    else:
        print(err)
```
