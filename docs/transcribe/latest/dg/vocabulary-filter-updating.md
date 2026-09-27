

# Updating a custom vocabulary filter
<a name="vocabulary-filter-updating"></a>

To update the word list in an existing custom vocabulary filter, use the [`UpdateVocabularyFilter`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateVocabularyFilter.html) operation.

When updating a custom vocabulary filter, note the following:
+ The update replaces the existing filter with the new content you provide.
+ You must include either `Words` or `VocabularyFilterFileUri` in your request.
+ (Optional) Include an `EncryptionConfiguration` to encrypt your vocabulary filter with a customer-managed key. You must also provide the new filter content, because encryption cannot be changed independently. For more information about encrypting resource artifacts with a customer-managed key, see [Encrypting resource artifacts with a customer-managed key](data-encryption.md#kms-resource-encryption).

To update a custom vocabulary filter, see the following for examples:

## AWS CLI
<a name="vocab-filter-update-cli"></a>

This example uses the [update-vocabulary-filter](https://docs.aws.amazon.com/cli/latest/reference/transcribe/update-vocabulary-filter.html) command. For more information, see [`UpdateVocabularyFilter`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateVocabularyFilter.html).

```
aws transcribe update-vocabulary-filter \
--vocabulary-filter-name {{my-first-vocabulary-filter}} \
--vocabulary-filter-file-uri s3://{{amzn-s3-demo-bucket}}/{{my-vocabulary-filters}}/{{my-updated-vocabulary-filter}}.txt
```

Here's another example using the [update-vocabulary-filter](https://docs.aws.amazon.com/cli/latest/reference/transcribe/update-vocabulary-filter.html) command, and a request body that updates your custom vocabulary filter.

```
aws transcribe update-vocabulary-filter \
--cli-input-json file://{{filepath}}/{{my-updated-vocab-filter}}.json
```

The file *my-updated-vocab-filter.json* contains the following request body.

```
{
  "VocabularyFilterName": "{{my-first-vocabulary-filter}}",
  "VocabularyFilterFileUri": "s3://{{amzn-s3-demo-bucket}}/{{my-vocabulary-filters}}/{{my-updated-vocabulary-filter}}.txt"
}
```