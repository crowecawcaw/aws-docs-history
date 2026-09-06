

# Getting started (AWS CLI)
<a name="get-started-cli"></a>

In the following exercise, you use the AWS command line interface (AWS CLI) to translate text. To complete the exercise, you need to be familiar with the CLI and have a text editor. For more information, see [Install and configure the AWS Command Line Interface (AWS CLI)](setting-up.md#setup-awscli).

To use Amazon Translate from the command line, you need to run the command from a region that supports the Amazon Translate service. For a list of available endpoints and regions, see [Amazon Translate Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#translate_region) in the *AWS General Reference*.

## Translate text using the command line
<a name="cli-command-line"></a>

The following example shows how to use the [TranslateText](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html) operation from the command line to translate text. The example is formatted for Unix, Linux, and macOS. For Windows, replace the backslash (\\) Unix continuation character at the end of each line with a caret (^). At the command line, type the following. 

```
aws translate translate-text \
            --region {{region}} \
            --source-language-code "en" \
            --target-language-code "es" \
            --text "hello, world"
```

The response is the following JSON:

```
{
    "TargetLanguageCode": "es",
    "Text": "Hola, mundo",
    "SourceLanguageCode": "en"
}
```

## Next step
<a name="getting-started-next-examples"></a>

To see other ways to use Amazon Translate see [Code examples for Amazon Translate using AWS SDKs](service_code_examples.md).