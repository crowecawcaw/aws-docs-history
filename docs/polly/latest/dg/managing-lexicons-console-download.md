# Downloading lexicons on the console

The following process describes how to download one or more lexicons. You can add, remove, or modify lexicon entries in the file and then upload it again to keep your lexicon up-to-date.

Console

###### To download one or more lexicons

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/ "https://console.aws.amazon.com/polly/").
2. Choose the **Lexicons** tab.
3. Choose the lexicon or lexicons you want to download.
   1. To download a single lexicon, choose its name from the list.
   2. To download multiple lexicons as a single compressed archive file,
      select the check box next to each entry in the list that you want to download.

4. Choose **Download**.
5. Open the folder where you want to download the lexicon.
6. Choose **Save**.

AWS CLI
Amazon Polly provides the [GetLexicon](API_GetLexicon.md "API_GetLexicon.md") API operation to retrieve the content of a
pronunciation lexicon you stored in your account in a specific region.

The following `get-lexicon` AWS CLI command retrieves the content of the
`example` lexicon.

```
aws polly get-lexicon \
--name `example`
```

If you don't already have a lexicon stored in your account,
you can use the `PutLexicon` operation to store one.
For more information, see [Uploading a lexicon](managing-lexicons-console-upload.md "managing-lexicons-console-upload.md").

The following is a sample response. In addition to the lexicon content, the
response returns the metadata, such as the language code to which the lexicon
applies, number of lexemes defined in the lexicon, the Amazon Resource Name (ARN) of
the resource, and the size of the lexicon in bytes. The `LastModified`
value is a Unix timestamp.

```
{
    "Lexicon": {
        "Content": "`lexicon content in plain text PLS format`",
        "Name": "example"
    },
    "LexiconAttributes": {
        "LanguageCode": "en-US",
        "LastModified": 1474222543.989,
        "Alphabet": "ipa",
        "LexemesCount": 1,
        "LexiconArn": "arn:aws:polly:us-east-2:`account-id`:lexicon/example",
        "Size": 495
    }
}
```

The following resources contain additional code samples for the GetLexicon operation:

- Java Sample: [GetLexicon](GetLexiconSample.md "GetLexiconSample.md")
- Python (Boto3) Sample: [GetLexicon](GetLexiconSamplePython.md "GetLexiconSamplePython.md")
