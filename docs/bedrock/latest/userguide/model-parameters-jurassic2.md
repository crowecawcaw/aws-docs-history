# AI21 Labs Jurassic-2 models

This section provides inference parameters and a code example for using AI21 Labs
AI21 Labs Jurassic-2 models.

###### Topics

- [Inference parameters](#model-parameters-jurassic2-request-response "#model-parameters-jurassic2-request-response")
- [Code example](#api-inference-examples-a2i-jurassic "#api-inference-examples-a2i-jurassic")

## Inference parameters

The AI21 Labs Jurassic-2 models support the following inference parameters.

###### Topics

- [Randomness and Diversity](#model-parameters-jurassic2-random "#model-parameters-jurassic2-random")
- [Length](#model-parameters-jurassic2-length "#model-parameters-jurassic2-length")
- [Repetitions](#model-parameters-jurassic2-reps "#model-parameters-jurassic2-reps")
- [Model invocation request body field](#model-parameters-jurassic2-request-body "#model-parameters-jurassic2-request-body")
- [Model invocation response body field](#model-parameters-jurassic2-response-body "#model-parameters-jurassic2-response-body")

### Randomness and Diversity

The AI21 Labs Jurassic-2 models support the following parameters to control randomness
and diversity in the response.

- **Temperature** (`temperature`)– Use a lower value to decrease randomness in the response.
- **Top P** (`topP`) – Use a lower value to ignore less probable options.

### Length

The AI21 Labs Jurassic-2 models support the following parameters to control the length
of the generated response.

- **Max completion length** (`maxTokens`) – Specify the
  maximum number of tokens to use in the generated response.
- **Stop sequences** (`stopSequences`) – Configure stop
  sequences that the model recognizes and after which it stops generating further tokens.
  Press the Enter key to insert a newline character in a stop sequence. Use the Tab key to finish inserting a
  stop sequence.

### Repetitions

The AI21 Labs Jurassic-2 models support the following parameters to control repetition
in the generated response.

- **Presence penalty** (`presencePenalty`) – Use a higher value to lower
  the probability
  of generating new tokens that already appear at least once in the prompt or in the
  completion.
- **Count penalty** (`countPenalty`) – Use a higher value to lower
  the probability of
  generating new tokens that already appear at least once in the prompt or in the
  completion. Proportional to the number of appearances.
- **Frequency penalty** (`frequencyPenalty`) – Use a high value to lower
  the probability
  of generating new tokens that already appear at least once in the prompt or in the
  completion. The value is proportional to the frequency of the token appearances (normalized to
  text length).
- **Penalize special tokens** – Reduce the probability of repetition of special characters. The default values are `true`.
  - **Whitespaces** (`applyToWhitespaces`) – A `true` value applies the penalty to whitespaces and new lines.
  - **Punctuations** (`applyToPunctuation`) – A `true` value applies the penalty to punctuation.
  - **Numbers** (`applyToNumbers`) – A `true` value applies the penalty to numbers.
  - **Stop words** (`applyToStopwords`) – A `true` value applies the penalty to stop words.
  - **Emojis** (`applyToEmojis`) – A `true` value excludes emojis from the penalty.

### Model invocation request body field

When you make an [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") call using an AI21 Labs model, fill the `body` field with a JSON object that conforms to the one below. Enter the prompt in the `prompt` field.

```
{
    "prompt": string,
    "temperature": float,
    "topP": float,
    "maxTokens": int,
    "stopSequences": [string],
    "countPenalty": {
        "scale": float
    },
    "presencePenalty": {
        "scale": float
    },
    "frequencyPenalty": {
        "scale": float
    }
}
```

To penalize special tokens, add those fields to any of the penalty objects. For example, you can modify the `countPenalty` field as follows.

```
"countPenalty": {
    "scale": float,
    "applyToWhitespaces": boolean,
    "applyToPunctuations": boolean,
    "applyToNumbers": boolean,
    "applyToStopwords": boolean,
    "applyToEmojis": boolean
}
```

The following table shows the minimum, maximum, and default values for the numerical parameters.

| Category                  | Parameter                                 | JSON object format | Minimum | Maximum | Default |
| ------------------------- | ----------------------------------------- | ------------------ | ------- | ------- | ------- | ----------------- | ---------------- | --- | --- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Randomness and diversity  | Temperature                               | temperature        | 0       | 1       | 0.5     |
| Top P                     | topP                                      | 0                  | 1       | 0.5     |
| Length                    | Max tokens (mid, ultra, and large models) | maxTokens          | 0       | 8,191   | 200     |
| Max tokens (other models) | 0                                         | 2,048              | 200     |
| Repetitions               | Presence penalty                          | presencePenalty    | 0       | 5       | 0       |
| Count penalty             | countPenalty                              | 0                  | 1       | 0       |         | Frequency penalty | frequencyPenalty | 0   | 500 | 0   | ### Model invocation response body field For information about the format of the `body` field in the response, see [https://docs.ai21.com/reference/j2-complete-api-ref](https://docs.ai21.com/reference/j2-complete-api-ref "https://docs.ai21.com/reference/j2-complete-api-ref"). ###### Note Amazon Bedrock returns the response identifier (`id`) as an integer value. ## Code example This examples shows how to call the _A2I AI21 Labs Jurassic-2 Mid_ model. `import boto3 import json brt = boto3.client(service_name='bedrock-runtime') body = json.dumps({ "prompt": "Translate to spanish: 'Amazon Bedrock is the easiest way to build and scale generative AI applications with base models (FMs)'.", "maxTokens": 200, "temperature": 0.5, "topP": 0.5 }) modelId = 'ai21.j2-mid-v1' accept = 'application/json' contentType = 'application/json' response = brt.invoke_model( body=body, modelId=modelId, accept=accept, contentType=contentType ) response_body = json.loads(response.get('body').read()) # text print(response_body.get('completions')[0].get('data').get('text'))` |
