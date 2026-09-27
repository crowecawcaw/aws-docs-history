

# Updating a custom vocabulary
<a name="custom-vocabulary-updating"></a>

To update the content of an existing custom vocabulary, use the [`UpdateVocabulary`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateVocabulary.html) operation.

When updating a custom vocabulary, note the following:
+ Your vocabulary must be in a terminal state (`READY` or `FAILED`). You cannot update a vocabulary while it is being processed. Use [`GetVocabulary`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetVocabulary.html) to check the current state.
+ The update replaces the existing vocabulary with the new content you provide.
+ You must include either `Phrases` or `VocabularyFileUri` in your request.
+ (Optional) Include an `EncryptionConfiguration` to encrypt your vocabulary with a customer-managed key. You must also provide the new vocabulary content, because encryption cannot be changed independently. For more information about encrypting resource artifacts with a customer-managed key, see [Encrypting resource artifacts with a customer-managed key](data-encryption.md#kms-resource-encryption).

To update a custom vocabulary, see the following for examples:

## AWS CLI
<a name="vocab-update-cli"></a>

This example uses the [update-vocabulary](https://docs.aws.amazon.com/cli/latest/reference/transcribe/update-vocabulary.html) command. For more information, see [`UpdateVocabulary`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateVocabulary.html).

```
aws transcribe update-vocabulary \
--vocabulary-name {{my-first-vocabulary}} \
--vocabulary-file-uri s3://{{amzn-s3-demo-bucket}}/{{my-vocabularies}}/{{my-updated-vocabulary-file}}.txt \
--language-code {{en-US}}
```

Here's another example using the [update-vocabulary](https://docs.aws.amazon.com/cli/latest/reference/transcribe/update-vocabulary.html) command, and a request body that updates your custom vocabulary.

```
aws transcribe update-vocabulary \
--cli-input-json file://{{filepath}}/{{my-updated-vocab}}.json
```

The file *my-updated-vocab.json* contains the following request body.

```
{
  "VocabularyName": "{{my-first-vocabulary}}",
  "VocabularyFileUri": "s3://{{amzn-s3-demo-bucket}}/{{my-vocabularies}}/{{my-updated-vocabulary-file}}.txt",
  "LanguageCode": "{{en-US}}"
}
```