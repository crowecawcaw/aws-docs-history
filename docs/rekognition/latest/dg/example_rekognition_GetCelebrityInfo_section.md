# Use `GetCelebrityInfo` with an AWS SDK or CLI

The following code examples show how to use `GetCelebrityInfo`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Rekognition/#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Rekognition/#code-examples").

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Rekognition;
    using Amazon.Rekognition.Model;

    /// <summary>
    /// Shows how to use Amazon Rekognition to retrieve information about the
    /// celebrity identified by the supplied celebrity Id.
    /// </summary>
    public class CelebrityInfo
    {
        public static async Task Main()
        {
            string celebId = "nnnnnnnn";

            var rekognitionClient = new AmazonRekognitionClient();

            var celebrityInfoRequest = new GetCelebrityInfoRequest
            {
                Id = celebId,
            };

            Console.WriteLine($"Getting information for celebrity: {celebId}");

            var celebrityInfoResponse = await rekognitionClient.GetCelebrityInfoAsync(celebrityInfoRequest);

            // Display celebrity information.
            Console.WriteLine($"celebrity name: {celebrityInfoResponse.Name}");
            Console.WriteLine("Further information (if available):");
            celebrityInfoResponse.Urls.ForEach(url =>
            {
                Console.WriteLine(url);
            });
        }
    }



```

- For API details, see
  [GetCelebrityInfo](../../../goto/DotNetSDKV3/rekognition-2016-06-27/GetCelebrityInfo.md "../../../goto/DotNetSDKV3/rekognition-2016-06-27/GetCelebrityInfo.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To get information about a celebrity**

The following `get-celebrity-info` command displays information about the specified celebrity. The `id` parameter comes from a previous call to `recognize-celebrities`.

```
`aws rekognition get-celebrity-info --id `nnnnnnn``

```

Output:

```
{
    "Name": "Celeb A",
    "Urls": [
        "www.imdb.com/name/aaaaaaaaa"
    ]
}
```

For more information, see [Getting Information About a Celebrity](get-celebrity-info-procedure.md "get-celebrity-info-procedure.md") in the _Amazon Rekognition Developer Guide_.

- For API details, see
  [GetCelebrityInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-celebrity-info.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-celebrity-info.html")
  in _AWS CLI Command Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Rekognition with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
