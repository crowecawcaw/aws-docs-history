# Use `GetLexicon` with an AWS SDK or CLI

The following code examples show how to use `GetLexicon`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Polly#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Polly#code-examples").

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Polly;
    using Amazon.Polly.Model;

    /// <summary>
    /// Retrieves information about a specific Amazon Polly lexicon.
    /// </summary>
    public class GetLexicon
    {
        public static async Task Main(string[] args)
        {
            string lexiconName = "SampleLexicon";

            var client = new AmazonPollyClient();

            await GetPollyLexiconAsync(client, lexiconName);
        }

        public static async Task GetPollyLexiconAsync(AmazonPollyClient client, string lexiconName)
        {
            var getLexiconRequest = new GetLexiconRequest()
            {
                Name = lexiconName,
            };

            try
            {
                var response = await client.GetLexiconAsync(getLexiconRequest);
                Console.WriteLine($"Lexicon:\n Name: {response.Lexicon.Name}");
                Console.WriteLine($"Content: {response.Lexicon.Content}");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }
    }



```

- For API details, see
  [GetLexicon](../../../goto/DotNetSDKV3/polly-2016-06-10/GetLexicon.md "../../../goto/DotNetSDKV3/polly-2016-06-10/GetLexicon.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To retrieve the content of a lexicon**

The following `get-lexicon` example retrieves the content of the specified pronunciation lexicon.

```
`aws polly get-lexicon \
 --name `w3c``

```

Output:

```
{
    "Lexicon": {
        "Content": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<lexicon version=\"1.0\" \n      xmlns=    \"http://www.w3.org/2005/01/pronunciation-lexicon\"\n      xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" \n          xsi:schemaLocation=\"http://www.w3.org/2005/01/pronunciation-lexicon \n        http://www.w3.org/TR/2007/CR-pronunciation-    lexicon-20071212/pls.xsd\"\n      alphabet=\"ipa\" \n      xml:lang=\"en-US\">\n  <lexeme>\n    <grapheme>W3C</grapheme>\n        <alias>World Wide Web Consortium</alias>\n  </lexeme>\n</lexicon>\n",
        "Name": "w3c"
    },
    "LexiconAttributes": {
        "Alphabet": "ipa",
        "LanguageCode": "en-US",
        "LastModified": 1603908910.99,
        "LexiconArn": "arn:aws:polly:us-west-2:880185128111:lexicon/w3c",
        "LexemesCount": 1,
        "Size": 492
    }
}
```

For more information, see [Using the GetLexicon operation](gs-get-lexicon.md "gs-get-lexicon.md") in the _Amazon Polly Developer Guide_.

- For API details, see
  [GetLexicon](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-lexicon.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-lexicon.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/polly#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/polly#code-examples").

```
class PollyWrapper:
    """Encapsulates Amazon Polly functions."""

    def __init__(self, polly_client, s3_resource):
        """
        :param polly_client: A Boto3 Amazon Polly client.
        :param s3_resource: A Boto3 Amazon Simple Storage Service (Amazon S3) resource.
        """
        self.polly_client = polly_client
        self.s3_resource = s3_resource
        self.voice_metadata = None


    def get_lexicon(self, name):
        """
        Gets metadata and contents of an existing lexicon.

        :param name: The name of the lexicon to retrieve.
        :return: The retrieved lexicon.
        """
        try:
            response = self.polly_client.get_lexicon(Name=name)
            logger.info("Got lexicon %s.", name)
        except ClientError:
            logger.exception("Couldn't get lexicon %s.", name)
            raise
        else:
            return response



```

- For API details, see
  [GetLexicon](../../../goto/boto3/polly-2016-06-10/GetLexicon.md "../../../goto/boto3/polly-2016-06-10/GetLexicon.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Polly with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
