# Custom vocabularies

Use custom vocabularies to improve transcription accuracy for one or more specific words. These
are generally domain-specific terms, such as brand names and acronyms, proper nouns, and words that
Amazon Transcribe isn't rendering correctly.

Custom vocabularies can be used with all supported languages. Note that only the characters listed
in your language's [character set](charsets.md "charsets.md") can be used in a custom vocabulary.

###### Important

You are responsible for the integrity of your own data when you use Amazon Transcribe. Do not enter
confidential information, personal information (PII), or protected health information (PHI) into a custom
vocabulary.

Considerations when creating a custom vocabulary:

- You can have up to 100 custom vocabulary files per AWS account
- The size limit for each custom vocabulary file is 50 Kb
- If using the API to create your custom vocabulary, your vocabulary file must be in text (\*.txt)
  format. If using the AWS Management Console, your vocabulary file can be in text (\*.txt) format or
  comma-separated value (\*.csv) format.
- Each entry within a custom vocabulary cannot exceed 256 characters
- To use a custom vocabulary, it must have been created in the same AWS Region as
  your transcription.

###### Tip

You can test your custom vocabulary using the AWS Management Console. Once your custom
vocabulary is ready to use, log in to the AWS Management Console, select **Real-time
transcription**, scroll to **Customizations**, toggle on
**Custom vocabulary**, and select your custom vocabulary from the dropdown
list. Then select **start streaming**. Speak some of the words in your custom
vocabulary into your microphone to see if they render correctly.

## Custom vocabulary tables versus lists

###### Important

Custom vocabularies in list format are being deprecated. If you're creating a new custom
vocabulary, use the [table format](custom-vocabulary-create-table.md "custom-vocabulary-create-table.md").

Tables give you more options for—and more control over—the input and
output of words within your custom vocabulary. With tables, you must specify multiple categories
(Phrase and DisplayAs), allowing you to fine-tune your output.

Lists don't have additional options, so you can only type in entries as you want them to
appear in your transcript, replacing all spaces with hyphens.

The AWS Management Console, AWS CLI, and AWS SDKs all use custom
vocabulary tables in the same way; lists are used differently for each method and thus may require
additional formatting for successful use between methods.

For more information, see [Creating a custom vocabulary using a table](custom-vocabulary-create-table.md "custom-vocabulary-create-table.md") and [Creating a custom vocabulary using a list](custom-vocabulary-create-list.md "custom-vocabulary-create-list.md").

To dive a little deeper and learn how
to use Amazon Augmented AI with custom vocabularies, see:

###### API operations specific to custom vocabularies

[`CreateVocabulary`](../APIReference/API_CreateVocabulary.md "../APIReference/API_CreateVocabulary.md"),
[`DeleteVocabulary`](../APIReference/API_DeleteVocabulary.md "../APIReference/API_DeleteVocabulary.md"),
[`GetVocabulary`](../APIReference/API_GetVocabulary.md "../APIReference/API_GetVocabulary.md"),
[`ListVocabularies`](../APIReference/API_ListVocabularies.md "../APIReference/API_ListVocabularies.md"),
[`UpdateVocabulary`](../APIReference/API_UpdateVocabulary.md "../APIReference/API_UpdateVocabulary.md")
