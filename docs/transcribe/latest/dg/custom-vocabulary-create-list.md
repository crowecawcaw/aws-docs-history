# Creating a custom vocabulary using a list

###### Important

Custom vocabularies in list format are being deprecated, so if you're creating a new custom
vocabulary, we strongly recommend using the [table
format](custom-vocabulary-create-table.md "custom-vocabulary-create-table.md").

You can create custom vocabularies from lists using the AWS Management Console, AWS CLI,
or AWS SDKs.

- **AWS Management Console**: You must create and upload a text file containing
  your custom vocabulary. You can use line-separated or comma-separated entries. Note that your list
  must be saved as a text (\*.txt) file in `LF` format. If you use any other format, such as
  `CRLF`, your custom vocabulary is not accepted by Amazon Transcribe.
- **AWS CLI** and **AWS SDKs**:
  You must include your custom vocabulary as comma-separated entries within your API call using the
  [`Phrases`](../APIReference/API_CreateVocabulary.md#transcribe-CreateVocabulary-request-Phrases "../APIReference/API_CreateVocabulary.md#transcribe-CreateVocabulary-request-Phrases") flag.
  If an entry contains multiple words, you must hyphenate each word. For example, you
  include 'Los Angeles' as `Los-Angeles` and 'Andorra la Vella' as
  `Andorra-la-Vella`.

Here are examples of the two valid list formats. Refer to
[Creating custom vocabulary lists](#custom-vocabulary-create-list-examples "#custom-vocabulary-create-list-examples") for method-specific examples.

- Comma-separated entries:

```
Los-Angeles,CLI,Eva-Maria,ABCs,Andorra-la-Vella
```

- Line-separated entries:

```
Los-Angeles
CLI
Eva-Maria
ABCs
Andorra-la-Vella
```

###### Important

You can only use characters that are supported for your language. Refer to your language's
[character set](charsets.md "charsets.md") for details.

Custom vocabulary lists are not supported with the [`CreateMedicalVocabulary`](../APIReference/API_CreateMedicalVocabulary.md "../APIReference/API_CreateMedicalVocabulary.md") operation. If creating a custom medical vocabulary, you must use a table format; refer to [Creating a custom vocabulary using a table](custom-vocabulary-create-table.md "custom-vocabulary-create-table.md") for instructions.

## Creating custom vocabulary lists

To process a custom vocabulary list for use with Amazon Transcribe, see the following
examples:

This example uses the [create-vocabulary](../../../cli/latest/reference/transcribe/create-vocabulary.md "../../../cli/latest/reference/transcribe/create-vocabulary.md") command with a list-formatted custom vocabulary file. For more information, see [`CreateVocabulary`](../APIReference/API_CreateVocabulary.md "../APIReference/API_CreateVocabulary.md").

```
aws transcribe create-vocabulary \
--vocabulary-name `my-first-vocabulary` \
--language-code `en-US` \
--phrases {`CLI,Eva-Maria,ABCs`}
```

Here's another example using the [create-vocabulary](../../../cli/latest/reference/transcribe/create-vocabulary.md "../../../cli/latest/reference/transcribe/create-vocabulary.md") command, and a request body that creates your custom vocabulary.

```
aws transcribe create-vocabulary \
--cli-input-json file://`filepath`/`my-first-vocab-list`.json
```

The file _my-first-vocab-list.json_ contains the following request body.

```
{
  "VocabularyName": "`my-first-vocabulary`",
  "LanguageCode": "`en-US`",
  "Phrases": [
        "`CLI`","`Eva-Maria`","`ABCs`"
  ]
}
```

Once `VocabularyState` changes from `PENDING` to
`READY`, your custom vocabulary is ready to use with a transcription. To view the
current status of your custom vocabulary, run:

```
aws transcribe get-vocabulary \
--vocabulary-name `my-first-vocabulary`
```

This example uses the AWS SDK for Python (Boto3) to create a custom vocabulary from a list
using the
[create_vocabulary](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary") method. For more
information, see [`CreateVocabulary`](../APIReference/API_CreateVocabulary.md "../APIReference/API_CreateVocabulary.md").

For additional examples using the AWS SDKs, including feature-specific, scenario, and
cross-service examples, refer to the [Code examples for Amazon Transcribe using AWS SDKs](service_code_examples.md "service_code_examples.md") chapter.

```
from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe', '`us-west-2`')
vocab_name = "`my-first-vocabulary`"
response = transcribe.create_vocabulary(
    LanguageCode = '`en-US`',
    VocabularyName = vocab_name,
    Phrases = [
        '`CLI`','`Eva-Maria`','`ABCs`'
    ]
)

while True:
    status = transcribe.get_vocabulary(VocabularyName = vocab_name)
    if status['VocabularyState'] in ['READY', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)
```

###### Note

If you create a new Amazon S3 bucket for your custom vocabulary files, make sure the
IAM role making the [`CreateVocabulary`](../APIReference/API_CreateVocabulary.md "../APIReference/API_CreateVocabulary.md")
request has permissions to access this bucket. If the role doesn't have the correct permissions, your request
fails. You can optionally specify an IAM role within your request by including the
`DataAccessRoleArn` parameter. For more information on IAM roles and policies
in Amazon Transcribe, see [Amazon Transcribe identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
