# Getting started (SDK)

AWS provides SDKs for various computer languages. The SDK manages many of the
API connection details for your client, such as signature calculation, request retry handling, and error handling. For more
information, see [AWS SDKs](https://aws.amazon.com/tools/#SDKs "https://aws.amazon.com/tools/#SDKs").

The following examples demonstrate how to use Amazon Translate [TranslateText](../APIReference/API_TranslateText.md "../APIReference/API_TranslateText.md")
operation using Java and Python. Use the SDKs to learn
about the Amazon Translate API and as building blocks for your own applications.

###### Topics

- [Translating text using the AWS SDK for Java](#examples-java "#examples-java")
- [Translating text using the AWS SDK for Python (Boto)](#examples-python "#examples-python")
- [Other SDK examples](#examples-other "#examples-other")

## Translating text using the AWS SDK for Java

AWS provides a [GitHub example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/translate/src/test/java/TranslateTest.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/translate/src/test/java/TranslateTest.java") of how to use the [TranslateText](../APIReference/API_TranslateText.md "../APIReference/API_TranslateText.md") operation in Java. To run this example, you need
the AWS SDK for Java. For instructions for installing the SDK for Java, see [Set up the
AWS SDK for Java 2.x](../../../sdk-for-java/latest/developer-guide/setup.md "../../../sdk-for-java/latest/developer-guide/setup.md").

## Translating text using the AWS SDK for Python (Boto)

The following example shows how to use the [TranslateText](../APIReference/API_TranslateText.md "../APIReference/API_TranslateText.md") operation in Python.
To run the example,
install the Python SDK via the AWS CLI. For instructions, see [Install and configure the AWS Command Line Interface (AWS CLI)](setting-up.md#setup-awscli "setting-up.md#setup-awscli").

```
import boto3

translate = boto3.client(service_name='translate', region_name='`region`', use_ssl=True)

result = translate.translate_text(Text="Hello, World",
            SourceLanguageCode="en", TargetLanguageCode="de")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
```

For a list of supported language codes, see [Supported languages and language codes](what-is-languages.md "what-is-languages.md")

## Other SDK examples

See [Code examples for Amazon Translate using AWS SDKs](service_code_examples.md "service_code_examples.md") for examples that
use .NET and SAP ABAP.
