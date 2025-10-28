# Filtering the lexicon list on the console

The following procedure describes how to filter the lexicons list so that only lexicons of
a chosen language are displayed.

Console

###### To filter the lexicons listed by language

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/ "https://console.aws.amazon.com/polly/").
2. Choose the **Lexicons** tab.
3. Choose **Any language**.
4. From the list of languages, choose the language you want to filter on.

The list displays only the lexicons for the chosen language.

AWS CLI
Amazon Polly provides the [ListLexicons](API_ListLexicons.md "API_ListLexicons.md") API operation that you can use to get the
list of pronunciation lexicons in your account in a specific AWS Region. The
following AWS CLI call lists the lexicons in your account in the us-east-2
region.

```
aws polly list-lexicons
```

The following is an example response, showing two lexicons named `w3c` and `tomato`.
For each lexicon, the response returns metadata such as the language code to which
the lexicon applies, the number of lexemes defined in the lexicon, the size in
bytes, and so on. The language code describes a language and locale to which the
lexemes defined in the lexicon apply.

```
{
    "Lexicons": [
        {
            "Attributes": {
                "LanguageCode": "en-US",
                "LastModified": 1474222543.989,
                "Alphabet": "ipa",
                "LexemesCount": 1,
                "LexiconArn": "arn:aws:polly:`aws-region`:`account-id`:lexicon/w3c",
                "Size": 495
            },
            "Name": "w3c"
        },
        {
            "Attributes": {
                "LanguageCode": "en-US",
                "LastModified": 1473099290.858,
                "Alphabet": "ipa",
                "LexemesCount": 1,
                "LexiconArn": "arn:aws:polly:`aws-region`:`account-id`:lexicon/tomato",
                "Size": 645
            },
            "Name": "tomato"
        }
    ]
}
```

The following resources contain additional information for the ListLexicons operation:

- Java Sample: [ListLexicons](ListLexiconsSample.md "ListLexiconsSample.md")
- Python (Boto3) Sample: [ListLexicon](ListLexiconSamplePython.md "ListLexiconSamplePython.md")
