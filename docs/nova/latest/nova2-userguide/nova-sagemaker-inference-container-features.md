

# Inference Container Features
<a name="nova-sagemaker-inference-container-features"></a>

The Amazon Nova SageMaker inference container includes a set of features that you can enable to customize model behavior during inference. Each feature is introduced in a specific container version and may require environment variables, request parameters, or both to activate.

This page lists the features available in the inference container, describes how to enable each one, and identifies the container version in which the feature was introduced. Use this reference to determine which features are available for your deployment and how to configure them.

Features that are enabled through environment variables are set when you create the SageMaker model or endpoint configuration. Include them in the `Environment` parameter of the [CreateModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html) API call. Features that are enabled through request parameters are set per invocation in the request body.

**Note**  
Always use the latest container image to get access to all available features. The `SM-Inference-latest` tag currently points to `v1.4`.

## Feature summary
<a name="nova-sagemaker-inference-container-features-summary"></a>

The following table provides a quick reference of all features supported in the Amazon Nova SageMaker inference container.


**Inference container feature summary**  

| Feature | How to enable | Default | Supported models | Introduced in | 
| --- | --- | --- | --- | --- | 
| [Default temperature](#nova-sagemaker-inference-container-feature-default-temperature) | Environment variable | 1.0 | All Amazon Nova models | v1.0 | 
| [Default top-p](#nova-sagemaker-inference-container-feature-default-top-p) | Environment variable | 1.0 | All Amazon Nova models | v1.0 | 
| [Default top-k](#nova-sagemaker-inference-container-feature-default-top-k) | Environment variable | -1 (disabled) | All Amazon Nova models | v1.0 | 
| [Default max new tokens](#nova-sagemaker-inference-container-feature-default-max-new-tokens) | Environment variable | Model's max context length | All Amazon Nova models | v1.0 | 
| [Default logprobs](#nova-sagemaker-inference-container-feature-default-logprobs) | Environment variable | Disabled | All Amazon Nova models | v1.0 | 
| [Eagle3 speculative decoding](#nova-sagemaker-inference-container-feature-speculative-decoding) | Enabled by default | Enabled | All Amazon Nova models | v1.0 | 
| [KV cache data type](#nova-sagemaker-inference-container-feature-kv-cache-dtype) | Environment variable | Same as model data type | All Amazon Nova models | v1.3 | 
| [Quantization](#nova-sagemaker-inference-container-feature-quantization) | Environment variable | Disabled\* | All Amazon Nova models | v1.3 | 
| [Number of speculative tokens](#nova-sagemaker-inference-container-feature-num-speculative-tokens) | Environment variable | 3 | All Amazon Nova models | v1.4 | 
| [Suffix decoding](#nova-sagemaker-inference-container-feature-suffix-decoding) | Environment variable | Disabled | All Amazon Nova models | v1.4 | 

**Important**  
\* FP8 quantization is automatically enabled and cannot be disabled for the following model and instance type combinations:  
Amazon Nova Lite on `ml.g6.12xlarge` or `ml.g6.24xlarge`
Nova 2 Lite on `ml.g6.48xlarge`
For these configurations, you do not need to set `QUANTIZATION_DTYPE`. See [Quantization](#nova-sagemaker-inference-container-feature-quantization) for details.

## Default temperature
<a name="nova-sagemaker-inference-container-feature-default-temperature"></a>

Sets the default sampling temperature for all inference requests sent to the endpoint. Temperature controls how random or predictable the model's output is. A value of `0` makes the model always pick the most likely next word, producing consistent and repeatable output. Higher values (up to `2`) make the model more willing to pick less likely words, producing more creative and varied responses.

**When to use:** Lower the temperature (for example, `0.1` to `0.3`) for tasks that need factual, consistent answers such as classification or data extraction. Raise it (for example, `0.7` to `1.0`) for creative tasks such as story writing or brainstorming. Temperature works together with top-p and top-k — all three control how the model selects tokens, and you can combine them to fine-tune output behavior.

Introduced in  
`v1.0`

Supported models  
All Amazon Nova models

How to enable  
Set the `DEFAULT_TEMPERATURE` environment variable when creating the SageMaker model.

Default value  
`1.0`

Valid values  
Float between `0` and `2` (inclusive)

**Environment variable**

```
"Environment": {
    "DEFAULT_TEMPERATURE": "0.7"
}
```

**Note**  
You can override this default on a per-request basis by including the `temperature` parameter in the request body.

## Default top-p
<a name="nova-sagemaker-inference-container-feature-default-top-p"></a>

Sets the default top-p value for all inference requests. Top-p controls output diversity by limiting the model's choices to a subset of the most likely words. Specifically, the model sorts all possible next words by probability and considers only the smallest group whose combined probability reaches the top-p value. For example, a top-p of `0.9` means the model only considers words that together account for 90% of the probability, ignoring the remaining unlikely options.

**When to use:** Use a lower top-p value (for example, `0.5`) to make the model stick to high-confidence words, producing more focused output. Use a higher value (for example, `0.95`) to allow more variety. Top-p is often used as an alternative to temperature — both control output diversity, but top-p adapts dynamically based on the model's confidence at each step. You can use both together, in which case the model applies whichever constraint is more restrictive at each step.

Introduced in  
`v1.0`

Supported models  
All Amazon Nova models

How to enable  
Set the `DEFAULT_TOP_P` environment variable when creating the SageMaker model.

Default value  
`1.0`

Valid values  
Float between `1e-10` and `1` (inclusive)

**Environment variable**

```
"Environment": {
    "DEFAULT_TOP_P": "0.9"
}
```

**Note**  
You can override this default on a per-request basis by including the `top_p` parameter in the request body.

## Default top-k
<a name="nova-sagemaker-inference-container-feature-default-top-k"></a>

Sets the default top-k value for all inference requests. Top-k limits the model's choices to a fixed number of the most likely next words. For example, a top-k of `50` means the model only considers the 50 most probable words at each step, regardless of their individual probabilities. A value of `-1` disables this limit, allowing the model to consider all possible words.

**When to use:** Use top-k when you want a hard cap on the number of word choices the model considers. Lower values (for example, `10`) produce more predictable output, while higher values allow more variety. Top-k can be combined with temperature and top-p — when multiple sampling controls are active, the model applies all of them, using whichever is most restrictive at each step.

Introduced in  
`v1.0`

Supported models  
All Amazon Nova models

How to enable  
Set the `DEFAULT_TOP_K` environment variable when creating the SageMaker model.

Default value  
`-1` (disabled)

Valid values  
Integer, `-1` or greater. Use `-1` to consider all tokens.

**Environment variable**

```
"Environment": {
    "DEFAULT_TOP_K": "50"
}
```

**Note**  
You can override this default on a per-request basis by including the `top_k` parameter in the request body.

## Default max new tokens
<a name="nova-sagemaker-inference-container-feature-default-max-new-tokens"></a>

Sets the default maximum number of tokens (words or word pieces) the model generates in a response. This value applies to all requests unless overridden. Use this to control response length and manage costs across your endpoint.

**When to use:** Set this when you want to enforce a consistent maximum response length across all requests. For example, set it to `256` for short-answer tasks or `2048` for longer content generation. The maximum allowed value depends on the `CONTEXT_LENGTH` configured for your endpoint, because input tokens plus output tokens cannot exceed the context length.

Introduced in  
`v1.0`

Supported models  
All Amazon Nova models

How to enable  
Set the `DEFAULT_MAX_NEW_TOKENS` environment variable when creating the SageMaker model.

Default value  
Model's maximum context length

Valid values  
Integer, `1` or greater

**Environment variable**

```
"Environment": {
    "DEFAULT_MAX_NEW_TOKENS": "512"
}
```

**Note**  
You can override this default on a per-request basis by including the `max_tokens` or `max_completion_tokens` parameter in the request body. The maximum allowed value depends on the `CONTEXT_LENGTH` configured for your endpoint.

## Default logprobs
<a name="nova-sagemaker-inference-container-feature-default-logprobs"></a>

Sets the default number of log probabilities to return for each generated token. A log probability is a numerical score that indicates how confident the model was in choosing each word. When enabled, the response includes these scores for each output token, which is useful for evaluating model confidence, comparing alternative word choices, and debugging generation behavior.

**When to use:** Enable logprobs when you need to assess how confident the model is in its output — for example, to flag low-confidence responses for human review, or to compare the likelihood of different completions. Enabling logprobs may slightly increase response latency and response payload size.

Introduced in  
`v1.0`

Supported models  
All Amazon Nova models

How to enable  
Set the `DEFAULT_LOGPROBS` environment variable when creating the SageMaker model.

Default value  
Disabled

Valid values  
Integer between `1` and `20` (inclusive)

**Environment variable**

```
"Environment": {
    "DEFAULT_LOGPROBS": "5"
}
```

**Note**  
You can override this default on a per-request basis by including the `logprobs` and `top_logprobs` parameters in the request body. Enabling logprobs may slightly increase response latency.

## Eagle3 speculative decoding
<a name="nova-sagemaker-inference-container-feature-speculative-decoding"></a>

Eagle3 speculative decoding is an optimization technique that speeds up text generation. It works by using a smaller, faster draft model to predict several tokens ahead, then checking those predictions against the primary model in a single step. When the predictions are correct, the model effectively generates multiple tokens in the time it would normally take to generate one. The primary model always verifies the draft tokens, so the final output is identical to what the primary model would produce on its own — only the speed changes, not the quality.

**When to use:** Eagle3 speculative decoding is enabled by default and benefits most workloads. Consider disabling it only if you observe unexpected behavior or need to isolate performance characteristics during debugging.

Introduced in  
`v1.0`. Support for FP8 quantization with Eagle3 speculative decoding was added in `v1.4`.

Supported models  
All Amazon Nova models

How to enable  
Eagle3 speculative decoding is enabled by default with no configuration required. Use `DISABLE_SPECULATIVE_DECODING` to disable it.

Default value  
`false` (Eagle3 speculative decoding is enabled)

Valid values  
`true`, `false`

**Environment variable**

The following example disables Eagle3 speculative decoding:

```
"Environment": {
    "DISABLE_SPECULATIVE_DECODING": "true"
}
```

## KV cache data type
<a name="nova-sagemaker-inference-container-feature-kv-cache-dtype"></a>

Sets the data type for the key-value (KV) cache used during inference. The KV cache stores the model's memory of previous tokens in a conversation, allowing it to generate each new token without reprocessing the entire input. For long sequences, this cache can consume significant GPU memory. Setting the KV cache to a lower-precision data type such as FP8 reduces memory usage and can improve throughput, at the cost of minor numerical differences in output.

**When to use:** Enable FP8 KV cache when you need to support longer context lengths or higher concurrency on your instance. This is especially useful on GPU instances with limited memory. Test your use case to verify that output quality meets your requirements, as lower precision may produce slightly different results.

Introduced in  
`v1.3`

Supported models  
All Amazon Nova models

How to enable  
Set the `KV_CACHE_DTYPE` environment variable when creating the SageMaker model.

Default value  
Same as the model's data type

Valid values  
`fp8`

**Environment variable**

```
"Environment": {
    "KV_CACHE_DTYPE": "fp8"
}
```

**Note**  
Changing the KV cache data type may produce slightly different outputs compared to the default precision. Test your use case to verify that output quality meets your requirements.

## Quantization
<a name="nova-sagemaker-inference-container-feature-quantization"></a>

Sets the quantization data type for model weights. Quantization compresses the model's weights into a lower-precision format (FP8 instead of the default higher precision), which reduces the amount of GPU memory the model requires. This can improve inference throughput and allow larger models to fit on smaller instance types, with minimal impact on output quality.

**When to use:** Use FP8 quantization when you want to reduce memory usage to support higher concurrency or fit a model on a smaller instance type. Note that some model and instance type combinations require FP8 quantization automatically — see the warning below.

Introduced in  
`v1.3`

Supported models  
All Amazon Nova models

How to enable  
Set the `QUANTIZATION_DTYPE` environment variable when creating the SageMaker model.

Default value  
Disabled. However, FP8 quantization is automatically enabled for certain model and instance type combinations. See the note below.

Valid values  
`fp8`

**Environment variable**

```
"Environment": {
    "QUANTIZATION_DTYPE": "fp8"
}
```

**Important**  
The following model and instance type combinations require FP8 quantization. For these configurations, quantization is enabled automatically and cannot be disabled or overridden:  
Amazon Nova Lite on `ml.g6.12xlarge` or `ml.g6.24xlarge`
Nova 2 Lite on `ml.g6.48xlarge`
For all other configurations, see [Supported models and instances](nova-model-sagemaker-inference.md#nova-sagemaker-inference-supported) for details.

## Number of speculative tokens
<a name="nova-sagemaker-inference-container-feature-num-speculative-tokens"></a>

Controls how many tokens the draft model predicts ahead during each Eagle3 speculative decoding step. A higher value means the draft model attempts to predict more tokens at once, which can improve throughput when predictions are accurate. If the draft model's predictions frequently diverge from the primary model, a lower value may be more efficient.

**When to use:** Increase this value when your workload produces predictable output patterns (for example, structured data or templated text) where the draft model is likely to guess correctly. Decrease it for creative or highly variable output where predictions are less reliable.

Introduced in  
`v1.4`

Supported models  
All Amazon Nova models

How to enable  
Set the `NUM_SPECULATIVE_TOKENS` environment variable when creating the SageMaker model.

Default value  
`3`

Valid values  
Integer between `1` and `10` (inclusive)

**Environment variable**

```
"Environment": {
    "NUM_SPECULATIVE_TOKENS": "5"
}
```

**Note**  
This setting only applies when Eagle3 speculative decoding is enabled (`DISABLE_SPECULATIVE_DECODING` is `false`). It has no effect when speculative decoding is disabled or when using suffix decoding.

## Suffix decoding
<a name="nova-sagemaker-inference-container-feature-suffix-decoding"></a>

Suffix decoding is an alternative method for speeding up text generation. Instead of using a separate draft model (as Eagle3 does), suffix decoding looks for repeated patterns in the text that has already been generated or in the input prompt, and reuses those patterns to predict future tokens. This approach works well when the output is likely to contain repeated phrases, structured formats, or content that closely mirrors the input.

**When to use:** Use suffix decoding for tasks where the output contains repetitive patterns, such as generating structured data, filling in templates, or summarizing content that reuses phrases from the source. For general-purpose generation where output is highly varied, the default Eagle3 method typically provides better throughput.

Introduced in  
`v1.4`

Supported models  
All Amazon Nova models

How to enable  
Set the `SPECULATIVE_DECODING_METHOD` environment variable to `suffix` when creating the SageMaker model.

Default value  
`eagle3`

Valid values  
`eagle3`, `suffix`

**Environment variable**

```
"Environment": {
    "SPECULATIVE_DECODING_METHOD": "suffix"
}
```

**Note**  
To use suffix decoding, `DISABLE_SPECULATIVE_DECODING` must be set to `false` (the default). Setting `DISABLE_SPECULATIVE_DECODING` to `true` disables all speculative decoding methods, including suffix decoding.