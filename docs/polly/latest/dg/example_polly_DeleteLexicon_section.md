# Use `DeleteLexicon` with an AWS SDK or CLI

The following code examples show how to use `DeleteLexicon`.

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
    /// Deletes an existing Amazon Polly lexicon using the AWS SDK for .NET.
    /// </summary>
    public class DeleteLexicon
    {
        public static async Task Main()
        {
            string lexiconName = "SampleLexicon";

            var client = new AmazonPollyClient();

            var success = await DeletePollyLexiconAsync(client, lexiconName);

            if (success)
            {
                Console.WriteLine($"Successfully deleted {lexiconName}.");
            }
            else
            {
                Console.WriteLine($"Could not delete {lexiconName}.");
            }
        }

        /// <summary>
        /// Deletes the named Amazon Polly lexicon.
        /// </summary>
        /// <param name="client">The initialized Amazon Polly client object.</param>
        /// <param name="lexiconName">The name of the Amazon Polly lexicon to
        /// delete.</param>
        /// <returns>A Boolean value indicating the success of the operation.</returns>
        public static async Task<bool> DeletePollyLexiconAsync(
            AmazonPollyClient client,
            string lexiconName)
        {
            var deleteLexiconRequest = new DeleteLexiconRequest()
            {
                Name = lexiconName,
            };

            var response = await client.DeleteLexiconAsync(deleteLexiconRequest);

            return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
        }
    }



```

- For API details, see
  [DeleteLexicon](../../../goto/DotNetSDKV3/polly-2016-06-10/DeleteLexicon.md "../../../goto/DotNetSDKV3/polly-2016-06-10/DeleteLexicon.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To delete a lexicon**

The following `delete-lexicon` example deletes the specified lexicon.

```
`aws polly delete-lexicon \
 --name `w3c``

```

This command produces no output.

For more information, see [Using the DeleteLexicon operation](gs-delete-lexicon.md "gs-delete-lexicon.md") in the _Amazon Polly Developer Guide_.

- For API details, see
  [DeleteLexicon](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/delete-lexicon.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/delete-lexicon.html")
  in _AWS CLI Command Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Polly with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
