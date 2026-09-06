

# Getting started (SDK)
<a name="get-started-sdk"></a>

AWS provides SDKs for various computer languages. The SDK manages many of the API connection details for your client, such as signature calculation, request retry handling, and error handling. For more information, see [AWS SDKs](https://aws.amazon.com/tools/#SDKs).

The following examples demonstrate how to use Amazon Translate [TranslateText](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html) operation using Java and Python. Use the SDKs to learn about the Amazon Translate API and as building blocks for your own applications.

**Topics**
+ [Translating text using the AWS SDK for Java](#examples-java)
+ [Translating text using the AWS SDK for Python (Boto)](#examples-python)
+ [Other SDK examples](#examples-other)

## Translating text using the AWS SDK for Java
<a name="examples-java"></a>

AWS provides a [GitHub example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/translate/src/test/java/TranslateTest.java) of how to use the [TranslateText](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html) operation in Java. To run this example, you need the AWS SDK for Java. For instructions for installing the SDK for Java, see [ Set up the AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html). 

## Translating text using the AWS SDK for Python (Boto)
<a name="examples-python"></a>

The following example shows how to use the [TranslateText](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html) operation in Python. To run the example, install the Python SDK via the AWS CLI. For instructions, see [Install and configure the AWS Command Line Interface (AWS CLI)](setting-up.md#setup-awscli).

```
import boto3

translate = boto3.client(service_name='translate', region_name='{{region}}', use_ssl=True)

result = translate.translate_text(Text="Hello, World", 
            SourceLanguageCode="en", TargetLanguageCode="de")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
```

For a list of supported language codes, see [Supported languages and language codes](what-is-languages.md)

## Other SDK examples
<a name="examples-other"></a>

See [Code examples for Amazon Translate using AWS SDKs](service_code_examples.md) for examples that use .NET and SAP ABAP.