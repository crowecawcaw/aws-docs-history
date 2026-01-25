# Use `DescribeCollection` with an AWS SDK or CLI

The following code examples show how to use `DescribeCollection`.

For more information, see [Describing a collection](describe-collection-procedure.md "describe-collection-procedure.md").

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
    /// Uses the Amazon Rekognition Service to describe the contents of a
    /// collection.
    /// </summary>
    public class DescribeCollection
    {
        public static async Task Main()
        {
            var rekognitionClient = new AmazonRekognitionClient();

            string collectionId = "MyCollection";
            Console.WriteLine($"Describing collection: {collectionId}");

            var describeCollectionRequest = new DescribeCollectionRequest()
            {
                CollectionId = collectionId,
            };

            var describeCollectionResponse = await rekognitionClient.DescribeCollectionAsync(describeCollectionRequest);
            Console.WriteLine($"Collection ARN: {describeCollectionResponse.CollectionARN}");
            Console.WriteLine($"Face count: {describeCollectionResponse.FaceCount}");
            Console.WriteLine($"Face model version: {describeCollectionResponse.FaceModelVersion}");
            Console.WriteLine($"Created: {describeCollectionResponse.CreationTimestamp}");
        }
    }



```

- For API details, see
  [DescribeCollection](../../../goto/DotNetSDKV3/rekognition-2016-06-27/DescribeCollection.md "../../../goto/DotNetSDKV3/rekognition-2016-06-27/DescribeCollection.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To describe a collection**

The following `describe-collection` example displays the details about the specified collection.

```
`aws rekognition describe-collection \
 --collection-id `MyCollection``

```

Output:

```
{
    "FaceCount": 200,
    "CreationTimestamp": 1569444828.274,
    "CollectionARN": "arn:aws:rekognition:us-west-2:123456789012:collection/MyCollection",
    "FaceModelVersion": "4.0"
}
```

For more information, see [Describing a Collection](describe-collection-procedure.md "describe-collection-procedure.md") in the _Amazon Rekognition Developer Guide_.

- For API details, see
  [DescribeCollection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-collection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-collection.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/rekognition/#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/rekognition/#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.DescribeCollectionRequest;
import software.amazon.awssdk.services.rekognition.model.DescribeCollectionResponse;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DescribeCollection {
    public static void main(String[] args) {
        final String usage = """
            Usage:    <collectionName>

            Where:
                collectionName - The name of the Amazon Rekognition collection.\s
            """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String collectionName = args[0];
        Region region = Region.US_EAST_1;
        RekognitionClient rekClient = RekognitionClient.builder()
                .region(region)
                .build();

        describeColl(rekClient, collectionName);
        rekClient.close();
    }

    /**
     * Describes an Amazon Rekognition collection.
     *
     * @param rekClient         The Amazon Rekognition client used to make the request.
     * @param collectionName    The name of the collection to describe.
     *
     * @throws RekognitionException If an error occurs while describing the collection.
     */
    public static void describeColl(RekognitionClient rekClient, String collectionName) {
        try {
            DescribeCollectionRequest describeCollectionRequest = DescribeCollectionRequest.builder()
                    .collectionId(collectionName)
                    .build();

            DescribeCollectionResponse describeCollectionResponse = rekClient
                    .describeCollection(describeCollectionRequest);
            System.out.println("Collection Arn : " + describeCollectionResponse.collectionARN());
            System.out.println("Created : " + describeCollectionResponse.creationTimestamp().toString());

        } catch (RekognitionException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [DescribeCollection](../../../goto/SdkForJavaV2/rekognition-2016-06-27/DescribeCollection.md "../../../goto/SdkForJavaV2/rekognition-2016-06-27/DescribeCollection.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/rekognition#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/rekognition#code-examples").

```
suspend fun describeColl(collectionName: String) {
    val request =
        DescribeCollectionRequest {
            collectionId = collectionName
        }

    RekognitionClient.fromEnvironment { region = "us-east-1" }.use { rekClient ->
        val response = rekClient.describeCollection(request)
        println("The collection Arn is ${response.collectionArn}")
        println("The collection contains this many faces ${response.faceCount}")
    }
}


```

- For API details, see
  [DescribeCollection](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rekognition#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rekognition#code-examples").

```
class RekognitionCollection:
    """
    Encapsulates an Amazon Rekognition collection. This class is a thin wrapper
    around parts of the Boto3 Amazon Rekognition API.
    """

    def __init__(self, collection, rekognition_client):
        """
        Initializes a collection object.

        :param collection: Collection data in the format returned by a call to
                           create_collection.
        :param rekognition_client: A Boto3 Rekognition client.
        """
        self.collection_id = collection["CollectionId"]
        self.collection_arn, self.face_count, self.created = self._unpack_collection(
            collection
        )
        self.rekognition_client = rekognition_client

    @staticmethod
    def _unpack_collection(collection):
        """
        Unpacks optional parts of a collection that can be returned by
        describe_collection.

        :param collection: The collection data.
        :return: A tuple of the data in the collection.
        """
        return (
            collection.get("CollectionArn"),
            collection.get("FaceCount", 0),
            collection.get("CreationTimestamp"),
        )


    def describe_collection(self):
        """
        Gets data about the collection from the Amazon Rekognition service.

        :return: The collection rendered as a dict.
        """
        try:
            response = self.rekognition_client.describe_collection(
                CollectionId=self.collection_id
            )
            # Work around capitalization of Arn vs. ARN
            response["CollectionArn"] = response.get("CollectionARN")
            (
                self.collection_arn,
                self.face_count,
                self.created,
            ) = self._unpack_collection(response)
            logger.info("Got data for collection %s.", self.collection_id)
        except ClientError:
            logger.exception("Couldn't get data for collection %s.", self.collection_id)
            raise
        else:
            return self.to_dict()



```

- For API details, see
  [DescribeCollection](../../../goto/boto3/rekognition-2016-06-27/DescribeCollection.md "../../../goto/boto3/rekognition-2016-06-27/DescribeCollection.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rek#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rek#code-examples").

```
    TRY.
        oo_result = lo_rek->describecollection(
          iv_collectionid = iv_collection_id ).
        DATA(lv_face_count) = oo_result->get_facecount( ).
        DATA(lv_msg) = |Collection described: { lv_face_count } face(s) indexed.|.
        MESSAGE lv_msg TYPE 'I'.
      CATCH /aws1/cx_rekresourcenotfoundex.
        MESSAGE 'Collection not found.' TYPE 'E'.
      CATCH /aws1/cx_rekinvalidparameterex.
        MESSAGE 'Invalid parameter value.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [DescribeCollection](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Rekognition with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
