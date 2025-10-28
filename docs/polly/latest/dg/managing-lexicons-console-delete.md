# Deleting a lexicon

The following process describes how to delete a lexicon.
After deleting the lexicon, you must add it back before you can use it again. You
can delete one or more lexicons at the same time by selecting the check boxes next to individual
lexicons.

Console

###### To delete a lexicon

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/ "https://console.aws.amazon.com/polly/").
2. Choose the **Lexicons** tab.
3. Choose one or more lexicons that you want to delete from the list.
4. Choose **Delete**.
5. Enter confirmation text and then choose **Delete**
   to remove the lexicon from the Region or **Cancel** to
   keep it.

AWS CLI
Amazon Polly provides the [DeleteLexicon](API_DeleteLexicon.md "API_DeleteLexicon.md") API operation to delete a pronunciation lexicon
from a specific AWS Region in your account. The following AWS CLI deletes the
specified lexicon.

The following AWS CLI example is formatted for Unix, Linux, and macOS.
For Windows, replace the backslash (\) Unix continuation character at the end of each line with a caret (^) and use full quotation marks (") around the input text with single quotes (') for interior tags.

```
aws polly delete-lexicon \
--name `example`
```

The following resources contain additional information for the DeleteLexicon operation:

- Java Sample: [DeleteLexicon](DeleteLexiconSample.md "DeleteLexiconSample.md")
- Python (Boto3) Sample: [DeleteLexicon](DeleteLexiconPython.md "DeleteLexiconPython.md")
