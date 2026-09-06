

# Creating a custom vocabulary using a table
<a name="custom-vocabulary-create-table"></a>

Using a table format is the preferred way to create your custom vocabulary. Vocabulary tables must consist of four columns (Phrase, SoundsLike, IPA, and DisplayAs), which can be included in any order:


| Phrase | SoundsLike | IPA | DisplayAs | 
| --- | --- | --- | --- | 
| Required. Every row in your table must contain an entry in this column.<br />Do not use spaces in this column.<br />If your entry contains multiple words, separate each word with a hyphen (-). For example, **Andorra-la-Vella** or **Los-Angeles**.<br />For acronyms, any pronounced letters must be separated by a period. The trailing period also needs to be pronounced. If your acronym is plural, you must use a hyphen between the acronym and the 's'. For example, 'CLI' is **C.L.I.** (not **C.L.I**) and 'ABCs' is **A.B.C.-s** (not **A.B.C-s**).<br />If your phrase consists of both a word and an acronym, these two components must be separated by a hyphen. For example, 'DynamoDB' is **Dynamo-D.B.**.<br />Do not include digits in this column; numbers must be spelled out. For example, 'VX02Q' is **V.X.-zero-two-Q.**. | `SoundsLike` is no longer supported for Custom Vocabulary. Please leave the column empty. Any values in this column will be ignored. We will remove the support for this column in the future. | `IPA` is no longer supported for Custom Vocabulary. Please leave the column empty. Any values in this column will be ignored. We will remove the support for this column in the future. | Optional. Rows in this column can be left empty.<br />You can use spaces in this column.<br />Defines the how you want your entry to look in your transcription output. For example, **Andorra-la-Vella** in the `Phrase` column is **Andorra la Vella** in the `DisplayAs` column.<br />If a row in this column is empty, Amazon Transcribe uses the contents of the `Phrase` column to determine output.<br />You can include digits (`0-9`) in this column. | 

Things to note when creating your table:
+ Your table must contain all four column headers (Phrase, SoundsLike, IPA, and DisplayAs). The `Phrase` column must contain an entry on each row. The ability to provide pronunciation inputs through `IPA` and `SoundsLike` is no longer supported and you may leave the column empty. Any values in these columns will be ignored.
+ Each column must be TAB or comma (,) delineated; this applies to every row in your custom vocabulary file. If a row contains empty columns, you must still include a delineator (TAB or comma) for each column.
+ Spaces are only allowed within the `IPA` and `DisplayAs` columns. Do not use spaces to separate columns.
+ `IPA` and `SoundsLike` are no longer supported for Custom Vocabulary. Please leave the column empty. Any values in these column will be ignored. We will remove the support for this column in the future.
+ The `DisplayAs` column supports symbols and special characters (for example, C\+\+). All other columns support the characters that are listed on your language's [character set](charsets.md) page.
+ The `Phrase` column has the following formatting rules:
  + Cannot start with a period (`.`), apostrophe (`'`), or hyphen (`-`). For example, **-hello** and **.test** are invalid.
  + Cannot end with an apostrophe (`'`) or hyphen (`-`). For example, **hello-** and **world'** are invalid.
  + Cannot contain repeated hyphens (`--`), repeated periods (`..`), or repeated apostrophes (`''`). For example, **well--known** and **can''t** are invalid.
  + Periods can only be used to denote acronyms (single letters separated by periods, such as **A.B.C.**). A period cannot appear after two or more consecutive non-special characters (for example, **AB.C** is invalid), and cannot be followed by three or more consecutive non-special characters (for example, **A.BCD** is invalid).
  + Only characters listed in your language's [character set](charsets.md) are supported.
+ If you want to include numbers in the `Phrase` column, you must spell them out. Digits (`0-9`) are only supported in the `DisplayAs` column.
+ You must save your table as a plaintext (\*.txt) file. Both `LF` and `CRLF` line endings are supported.
+ You must upload your custom vocabulary file into an Amazon S3 bucket and process it using [`CreateVocabulary`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateVocabulary.html) before you can include it in a transcription request. Refer to [Creating custom vocabulary tables](#custom-vocabulary-create-table-examples) for instructions.

**Note**  
Enter acronyms, or other words whose letters should be pronounced individually, as single letters separated by periods (**A.B.C.**). To enter the plural form of an acronym, such as 'ABCs', separate the 's' from the acronym with a hyphen (**A.B.C.-s**). You can use upper or lower case letters to define an acronym. Acronyms are not supported in all languages; refer to [Supported languages and language-specific features](supported-languages.md).

Here is a sample custom vocabulary table (where **[TAB]** represents a tab character):

```
Phrase[TAB]SoundsLike[TAB]IPA[TAB]DisplayAs
Los-Angeles[TAB][TAB][TAB]Los Angeles
Eva-Maria[TAB][TAB][TAB]
A.B.C.-s[TAB][TAB][TAB]ABCs
Amazon-dot-com[TAB][TAB][TAB]Amazon.com
C.L.I.[TAB][TAB][TAB]CLI
Andorra-la-Vella[TAB][TAB][TAB]Andorra la Vella
Dynamo-D.B.[TAB][TAB][TAB]DynamoDB
V.X.-zero-two[TAB][TAB][TAB]VX02
V.X.-zero-two-Q.[TAB][TAB][TAB]VX02Q
```

For visual clarity, here is the same table with aligned columns. **Do not** add spaces between columns in your custom vocabulary table; your table should look misaligned like the preceding example.

```
Phrase          [TAB]SoundsLike          [TAB]IPA                [TAB]DisplayAs  
Los-Angeles     [TAB]                    [TAB]                   [TAB]Los Angeles   
Eva-Maria       [TAB]                    [TAB]                   [TAB]
A.B.C.-s        [TAB]                    [TAB]                   [TAB]ABCs  
amazon-dot-com  [TAB]                    [TAB]                   [TAB]amazon.com
C.L.I.          [TAB]                    [TAB]                   [TAB]CLI   
Andorra-la-Vella[TAB]                    [TAB]                   [TAB]Andorra la Vella
Dynamo-D.B.     [TAB]                    [TAB]                   [TAB]DynamoDB
V.X.-zero-two   [TAB]                    [TAB]                   [TAB]VX02
V.X.-zero-two-Q.[TAB]                    [TAB]                   [TAB]VX02Q
```

## Creating custom vocabulary tables
<a name="custom-vocabulary-create-table-examples"></a>

To process a custom vocabulary table for use with Amazon Transcribe, see the following examples:

### AWS Management Console
<a name="vocab-create-table-console"></a>

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/transcribe/).

1. In the navigation pane, choose **Custom vocabulary**. This opens the **Custom vocabulary** page where you can view existing vocabularies or create a new one.

1. Select **Create vocabulary**.  
![Amazon Transcribe console screenshot: the 'custom vocabulary' page.](http://docs.aws.amazon.com/transcribe/latest/dg/images/vocab-create-console.png)

   This takes you to the **Create vocabulary** page. Enter a name for your new custom vocabulary.

   Here, you have three options:

   1. Upload a txt or csv file from your computer.

      You can either create your custom vocabulary from scratch or download a template to help you get started. Your vocabulary is then auto-populated in the **View and edit vocabulary** pane.  
![Amazon Transcribe console screenshot: the 'create and import vocabulary' page.](http://docs.aws.amazon.com/transcribe/latest/dg/images/vocab-create-console-upload.png)

   1. Import a txt or csv file from an Amazon S3 location.

      You can either create your custom vocabulary from scratch or download a template to help you get started. Upload your finished vocabulary file to an Amazon S3 bucket and specify its URI in your request. Your vocabulary is then auto-populated in the **View and edit vocabulary** pane.  
![Amazon Transcribe console screenshot: the 'create and import vocabulary' page.](http://docs.aws.amazon.com/transcribe/latest/dg/images/vocab-create-console-s3.png)

   1. Manually create your vocabulary in the console.

      Scroll to the **View and edit vocabulary** pane and select **Add 10 rows**. You can now manually enter terms.  
![Amazon Transcribe console screenshot: the 'create and import vocabulary' page.](http://docs.aws.amazon.com/transcribe/latest/dg/images/vocab-create-console-manual.png)

1. You can edit your vocabulary the **View and edit vocabulary** pane. To make changes, click on the entry you want to modify.  
![Amazon Transcribe console screenshot: the 'create and edit vocabulary' pane.](http://docs.aws.amazon.com/transcribe/latest/dg/images/vocab-create-edit2.png)

   If you make an error, you get a detailed error message so you can correct any issues prior to processing your vocabulary. Note that if you don't correct all errors before selecting **Create vocabulary**, your vocabulary request fails.  
![Amazon Transcribe console screenshot: the 'create and edit vocabulary' pane.](http://docs.aws.amazon.com/transcribe/latest/dg/images/vocab-create-edit3.png)

   Select the check mark (✓) to save your changes or the 'X' to discard your changes.

1. Optionally, add tags to your custom vocabulary. Once you have all fields completed and are happy with your vocabulary, select **Create vocabulary** at the bottom of the page. This takes you back to the **Custom vocabulary** page where you can view the status of your custom vocabulary. When the status changes from 'Pending' to 'Ready' your custom vocabulary can be used with a transcription.  
![Amazon Transcribe console screenshot: custom vocabulary in pending status while processing.](http://docs.aws.amazon.com/transcribe/latest/dg/images/vocab-create-console-pending.png)

1. If the status changes to 'Failed', select the name of your custom vocabulary to go to its information page.  
![Amazon Transcribe console screenshot: 'custom vocabulary' page showing one vocabulary as complete and one as failed.](http://docs.aws.amazon.com/transcribe/latest/dg/images/vocab-create-console-failed.png)

   There is a **Failure reason** banner at the top of this page that provides information on why your custom vocabulary failed. Correct the error in your text file and try again.  
![Amazon Transcribe console screenshot: vocabulary's information page shows failure reason.](http://docs.aws.amazon.com/transcribe/latest/dg/images/vocab-create-console-failed2.png)

### AWS CLI
<a name="vocab-create-table-cli"></a>

This example uses the [create-vocabulary](https://docs.aws.amazon.com/cli/latest/reference/transcribe/create-vocabulary.html) command with a table-formatted vocabulary file. For more information, see [`CreateVocabulary`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateVocabulary.html).

To use an existing custom vocabulary in a transcription job, set the `VocabularyName` in the [`Settings`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Settings.html) field when you call the [`StartTranscriptionJob`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_StartTranscriptionJob.html) operation or, from the AWS Management Console, choose the custom vocabulary from the dropdown list.

```
aws transcribe create-vocabulary \ 
--vocabulary-name {{my-first-vocabulary}} \ 
--vocabulary-file-uri s3://{{amzn-s3-demo-bucket}}/{{my-vocabularies}}/{{my-vocabulary-file}}.txt \
--language-code {{en-US}}
```

Here's another example using the [create-vocabulary](https://docs.aws.amazon.com/cli/latest/reference/transcribe/create-vocabulary.html) command, and a request body that creates your custom vocabulary.

```
aws transcribe create-vocabulary \
--cli-input-json file://{{filepath}}/{{my-first-vocab-table}}.json
```

The file *my-first-vocab-table.json* contains the following request body.

```
{
  "VocabularyName": "{{my-first-vocabulary}}",
  "VocabularyFileUri": "s3://{{amzn-s3-demo-bucket}}/{{my-vocabularies}}/{{my-vocabulary-table}}.txt",
  "LanguageCode": "{{en-US}}"
}
```

Once `VocabularyState` changes from `PENDING` to `READY`, your custom vocabulary is ready to use with a transcription. To view the current status of your custom vocabulary, run:

```
aws transcribe get-vocabulary \
--vocabulary-name {{my-first-vocabulary}}
```

### AWS SDK for Python (Boto3)
<a name="vocab-create-table-python-batch"></a>

This example uses the AWS SDK for Python (Boto3) to create a custom vocabulary from a table using the [create\_vocabulary](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary) method. For more information, see [`CreateVocabulary`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateVocabulary.html).

To use an existing custom vocabulary in a transcription job, set the `VocabularyName` in the [`Settings`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Settings.html) field when you call the [`StartTranscriptionJob`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_StartTranscriptionJob.html) operation or, from the AWS Management Console, choose the custom vocabulary from the dropdown list.

For additional examples using the AWS SDKs, including feature-specific, scenario, and cross-service examples, refer to the [Code examples for Amazon Transcribe using AWS SDKs](service_code_examples.md) chapter.

```
from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe', '{{us-west-2}}')
vocab_name = "{{my-first-vocabulary}}"
response = transcribe.create_vocabulary(
    LanguageCode = '{{en-US}}',
    VocabularyName = vocab_name,
    VocabularyFileUri = 's3://{{amzn-s3-demo-bucket}}/{{my-vocabularies}}/{{my-vocabulary-table}}.txt'
)

while True:
    status = transcribe.get_vocabulary(VocabularyName = vocab_name)
    if status['VocabularyState'] in ['READY', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)
```

**Note**  
If you create a new Amazon S3 bucket for your custom vocabulary files, make sure the IAM role making the [`CreateVocabulary`](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateVocabulary.html) request has permissions to access this bucket. If the role doesn't have the correct permissions, your request fails. You can optionally specify an IAM role within your request by including the `DataAccessRoleArn` parameter. For more information on IAM roles and policies in Amazon Transcribe, see [Amazon Transcribe identity-based policy examples](security_iam_id-based-policy-examples.md).