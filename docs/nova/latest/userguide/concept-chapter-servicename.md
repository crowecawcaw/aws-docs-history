# Generating structured output with Nova

Structured output is critical for machine-to-machine communication use cases, as this enables downstream use
cases to more effectively consume and process the generated outputs. Whether it's extracting information from documents,
creating assistants that fetch data from APIs, or developing agents that take actions, these tasks require foundation models
to generate outputs in specific structured formats.

The Nova Models leverage Constrained Decoding to ensure high model reliability in the output generated and to allow the
model to handle complex schemas with ease. Constrained decoding relies on a grammar to “constrain” the possible tokens a model
can output at each step. This is differentiated from the prompting techniques historically used because this changes the actual
tokens a model can choose from when generating an output. For example, when closing a JSON object the model would be constrained
to just a } token to select. Constrained decoding is leveraged every time that a tool configuration is passed. Because tool use
provides us a specific schema already, we are able to use that to generate a grammar dynamically based on the schema desired by
the developer. Constrained decoding prevents the model from generating invalid keys and enforces correct data types based on the
defined schema.

To leverage tool use with structured output, the primary step is define the JSON schema you require for the output.
Below is an example of a JSON schema defined within a `tool_config` definition:

```

  tool_config = {
  "tools": [
    {
      "toolSpec": {
        "name": "ProductAnalysis",
        "description": "Analyze product information from text.",
        "inputSchema": {
          "json": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "Product name"
              },
              "rating": {
                "maximum": 5,
                "description": "Customer rating 1-5",
                "type": [
                  "number",
                  "null"
                ],
                "minimum": 1
              },
              "features": {
                "description": "Key product features",
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "category": {
                "type": "string",
                "description": "Product category"
              },
              "price": {
                "type": "number",
                "description": "Price in USD"
              }
            },
            "required": [
              "name",
              "category",
              "price",
              "features"
            ]
          }
        }
      }
    }
  ],
  "toolChoice": {
    "tool": {
      "name": "ProductAnalysis"
    }
  }
}

```

When you call the tool later using the model, you will receive an output that responds in the schema format. For example,
below is an example of calling the model in Python:

```

  import boto3

client = boto3.client("bedrock-runtime")
model_id = "amazon.nova-lite-1-5-v1:0"

user_query = """The Amazon Kindle Scribe is a state-of-the-art e-reader designed for both reading and writing, featuring a 10.2-inch paper-like display and a premium stylus. This versatile device allows users to enjoy books, take notes, annotate PDFs, and even sketch, making it ideal for readers, students, and professionals. Priced at $339.99, it falls under the electronics category and boasts features like a front light, adjustable warm light settings, and up to 12 weeks of battery life on a single charge. Customer ratings for the Kindle Scribe average around 4.5 stars, reflecting its high user satisfaction."""

messages = [{
   "role": "user",
   "content": [{
        "text": user_query
   }]
}]

system = [{"text": "Leverage the ProductAnalysis tool to extract product information"}]
inference_params = {"temperature": 0}

response = client.converse(modelId=model_id, system=system, messages=messages, toolConfig=tool_config, inferenceConfig=inference_params)
print(next(
    block["toolUse"]
    for block in response["output"]["message"]["content"]
    if "toolUse" in block
))

```

The output then appears like this:

```

 {
  "toolUseId": "tooluse_hke1FUeuRbKXK8DPqIptVg",
  "name": "ProductAnalysis",
  "input": {
    "name": "Amazon Kindle Scribe",
    "rating": 4.5,
    "features": [
      "10.2-inch paper-like display",
      "premium stylus",
      "front light",
      "adjustable warm light settings",
      "up to 12 weeks of battery life"
    ],
    "category": "electronics",
    "price": 339.99
  }
}

```
