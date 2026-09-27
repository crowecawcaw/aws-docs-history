

# Changing encryption configuration for a custom language model
<a name="custom-language-models-updating"></a>

To change the encryption configuration of an existing custom language model, use the [`UpdateLanguageModel`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateLanguageModel.html) operation. This operation does not support changes to the model content or training data. To retrain a model, create a new custom language model.

When changing encryption for a custom language model, note the following:
+ Your model must not be currently processing an update. You cannot submit another update while a previous update is in progress. Use [`DescribeLanguageModel`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DescribeLanguageModel.html) to check the current state.

**Note**  
In the isolated AWS Regions, avoid using customer-managed key encryption for custom language models that are trained on very large amounts of text if you plan to use them for streaming transcription. Because of compute capacity constraints in these Regions, decrypting the artifacts of a large model when it is loaded for a streaming transcription can be slow or fail to complete. Batch transcription is not affected. To use a large custom language model for streaming in these Regions, do not provide a customer-managed key. The model is then encrypted with the default AWS-owned key.

To update a custom language model, see the following for examples:

## AWS CLI
<a name="model-update-cli"></a>

This example uses the [update-language-model](https://docs.aws.amazon.com/cli/latest/reference/transcribe/update-language-model.html) command. For more information, see [`UpdateLanguageModel`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateLanguageModel.html).

```
aws transcribe update-language-model \
--model-name {{my-first-language-model}} \
--encryption-configuration KMSKey=arn:aws:kms:{{us-west-2}}:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}} \
--data-access-role-arn arn:aws:iam::{{111122223333}}:role/{{ExampleRole}}
```

Here's another example using the [update-language-model](https://docs.aws.amazon.com/cli/latest/reference/transcribe/update-language-model.html) command, and a request body that updates your custom language model.

```
aws transcribe update-language-model \
--cli-input-json file://{{filepath}}/{{my-updated-language-model}}.json
```

The file *my-updated-language-model.json* contains the following request body.

```
{
  "ModelName": "{{my-first-language-model}}",
  "EncryptionConfiguration": {
      "KMSKey": "arn:aws:kms:{{us-west-2}}:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
  },
  "DataAccessRoleArn": "arn:aws:iam::{{111122223333}}:role/{{ExampleRole}}"
}
```