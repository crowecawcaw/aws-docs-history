

# Use `GetLexicon` with an AWS SDK or CLI
<a name="example_polly_GetLexicon_section"></a>

The following code examples show how to use `GetLexicon`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Getting started with text-to-speech synthesis](example_polly_GettingStarted_082_section.md) 

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Polly#code-examples). 

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
+  For API details, see [GetLexicon](https://docs.aws.amazon.com/goto/DotNetSDKV3/polly-2016-06-10/GetLexicon) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To retrieve the content of a lexicon**  
The following `get-lexicon` example retrieves the content of the specified pronunciation lexicon.  

```
aws polly get-lexicon \
    --name {{w3c}}
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
For more information, see [Using the GetLexicon operation](https://docs.aws.amazon.com/polly/latest/dg/gs-get-lexicon.html) in the *Amazon Polly Developer Guide*.  
+  For API details, see [GetLexicon](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-lexicon.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/polly#code-examples). 

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
+  For API details, see [GetLexicon](https://docs.aws.amazon.com/goto/boto3/polly-2016-06-10/GetLexicon) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ply#code-examples). 

```
    TRY.
        oo_result = lo_ply->getlexicon( iv_name ).
        DATA(lo_lexicon) = oo_result->get_lexicon( ).
        IF lo_lexicon IS BOUND.
          DATA(lv_lex_name) = lo_lexicon->get_name( ).
          MESSAGE |Retrieved lexicon: { lv_lex_name }| TYPE 'I'.
        ENDIF.
      CATCH /aws1/cx_plylexiconnotfoundex.
        MESSAGE 'Lexicon not found.' TYPE 'E'.
      CATCH /aws1/cx_plyservicefailureex.
        MESSAGE 'Service failure occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [GetLexicon](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon Polly with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.