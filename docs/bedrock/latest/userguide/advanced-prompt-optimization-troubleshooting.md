

# Troubleshooting
<a name="advanced-prompt-optimization-troubleshooting"></a>


| Error | Cause | Fix | 
| --- | --- | --- | 
| No inference API is accessible for model | Model access not enabled or IAM permission missing | Enable model access in Bedrock console; verify IAM policy includes bedrock:InvokeModelWithResponseStream | 
| Input file is empty | S3 object has 0 bytes | Verify the input JSONL file has content | 
| File is not valid JSONL | Malformed JSON in input file | Validate each line is valid JSON | 
| AccessDenied on S3 | IAM role lacks S3 permissions | Add s3:GetObject for input path and s3:PutObject for output path | 
| ValidationException: multiple evaluation methods | Provided both steeringCriteria AND customLLMJConfig or Lambda | Use only ONE evaluation method per template | 
| ValidationException: missing label | Missing customEvaluationMetricLabel when using LLMJ or Lambda | Add the customEvaluationMetricLabel field | 
| Silent failure: inputVariables | Multiple keys in one inputVariables object | Use one key per object in the array | 
| ValidationException: placeholder mismatch | inputVariables keys don't match {{placeholders}} in template | Ensure keys exactly match placeholder names | 
| ValidationException: wrong bracket syntax | Used {variable} instead of {{variable}} | Use double curly brackets | 
| compressionRatio is 1.0 and the original prompt was returned | With shortenPrompt enabled, the optimized prompt was not both shorter than the original and at least as high scoring. | Refine your evaluation method or dataset and run the job again. A prompt that is already concise may not compress further. | 
| A newly launched model is not available for selection, or a job fails for a specific model | The model has not yet been enabled for Advanced Prompt Optimization, or it is not available in the job's Region | Confirm the model is available in your Region. If it is, try again later. If the model is still unavailable, contact AWS Support. | 
| ValidationException: application inference profile could not be found, or resolves to a model that is not an approved judge model | The customLLMJModelId application inference profile does not exist in your account, or it routes to a model that is not a supported judge model | Use an application inference profile in the same account that routes to a model on the Supported judge models list | 