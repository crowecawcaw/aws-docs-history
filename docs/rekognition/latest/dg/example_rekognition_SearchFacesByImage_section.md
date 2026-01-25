# Use `SearchFacesByImage` with an AWS SDK or CLI

The following code examples show how to use `SearchFacesByImage`.

For more information, see [Searching for a face (image)](search-face-with-image-procedure.md "search-face-with-image-procedure.md").

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
    /// Uses the Amazon Rekognition Service to search for images matching those
    /// in a collection.
    /// </summary>
    public class SearchFacesMatchingImage
    {
        public static async Task Main()
        {
            string collectionId = "MyCollection";
            string bucket = "amzn-s3-demo-bucket";
            string photo = "input.jpg";

            var rekognitionClient = new AmazonRekognitionClient();

            // Get an image object from S3 bucket.
            var image = new Image()
            {
                S3Object = new S3Object()
                {
                    Bucket = bucket,
                    Name = photo,
                },
            };

            var searchFacesByImageRequest = new SearchFacesByImageRequest()
            {
                CollectionId = collectionId,
                Image = image,
                FaceMatchThreshold = 70F,
                MaxFaces = 2,
            };

            SearchFacesByImageResponse searchFacesByImageResponse = await rekognitionClient.SearchFacesByImageAsync(searchFacesByImageRequest);

            Console.WriteLine("Faces matching largest face in image from " + photo);
            searchFacesByImageResponse.FaceMatches.ForEach(face =>
            {
                Console.WriteLine($"FaceId: {face.Face.FaceId}, Similarity: {face.Similarity}");
            });
        }
    }



```

- For API details, see
  [SearchFacesByImage](../../../goto/DotNetSDKV3/rekognition-2016-06-27/SearchFacesByImage.md "../../../goto/DotNetSDKV3/rekognition-2016-06-27/SearchFacesByImage.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To search for faces in a collection that match the largest face in an image.**

The following `search-faces-by-image` command searches for faces in a collection that match the largest face in the specified image.:

```
`aws rekognition search-faces-by-image \
 --image '`{"S3Object":{"Bucket":"MyImageS3Bucket","Name":"ExamplePerson.jpg"}}`' \
 --collection-id `MyFaceImageCollection`

`{`
 "SearchedFaceBoundingBox": `{`
 "Width": `0.18562500178813934,`
 "Top": `0.1618015021085739,`
 "Left": `0.5575000047683716,`
 "Height": `0.24770642817020416`
 `},`
 "SearchedFaceConfidence": `99.993408203125,`
 "FaceMatches": `[`
 `{`
 "Face": `{`
 "BoundingBox": `{`
 "Width": `0.18562500178813934,`
 "Top": `0.1618019938468933,`
 "Left": `0.5575000047683716,`
 "Height": `0.24770599603652954`
 `},`
 "FaceId": "ce7ed422-2132-4a11-ab14-06c5c410f29f",
 "ExternalImageId": "example-image.jpg",
 "Confidence": `99.99340057373047,`
 "ImageId": `"8d67061e-90d2-598f-9fbd-29c8497039c0"`
 `},`
 "Similarity": `99.97913360595703`
 `},`
 `{`
 "Face": `{`
 "BoundingBox": `{`
 "Width": `0.18562500178813934,`
 "Top": `0.1618019938468933,`
 "Left": `0.5575000047683716,`
 "Height": `0.24770599603652954`
 `},`
 "FaceId": "13692fe4-990a-4679-b14a-5ac23d135eab",
 "ExternalImageId": "image3.jpg",
 "Confidence": `99.99340057373047,`
 "ImageId": `"8df18239-9ad1-5acd-a46a-6581ff98f51b"`
 `},`
 "Similarity": `99.97913360595703`
 `},`
 `{`
 "Face": `{`
 "BoundingBox": `{`
 "Width": `0.41499999165534973,`
 "Top": `0.09187500178813934,`
 "Left": `0.28083300590515137,`
 "Height": `0.3112500011920929`
 `},`
 "FaceId": "8d3cfc70-4ba8-4b36-9644-90fba29c2dac",
 "ExternalImageId": "image2.jpg",
 "Confidence": `99.99769592285156,`
 "ImageId": `"a294da46-2cb1-5cc4-9045-61d7ca567662"`
 `},`
 "Similarity": `99.18069458007812`
 `},`
 `{`
 "Face": `{`
 "BoundingBox": `{`
 "Width": `0.48166701197624207,`
 "Top": `0.20999999344348907,`
 "Left": `0.21250000596046448,`
 "Height": `0.36125001311302185`
 `},`
 "FaceId": "bd4ceb4d-9acc-4ab7-8ef8-1c2d2ba0a66a",
 "ExternalImageId": "image1.jpg",
 "Confidence": `99.99949645996094,`
 "ImageId": `"5e1a7588-e5a0-5ee3-bd00-c642518dfe3a"`
 `},`
 "Similarity": `98.66607666015625`
 `},`
 `{`
 "Face": `{`
 "BoundingBox": `{`
 "Width": `0.5349419713020325,`
 "Top": `0.29124999046325684,`
 "Left": `0.16389399766921997,`
 "Height": `0.40187498927116394`
 `},`
 "FaceId": "745f7509-b1fa-44e0-8b95-367b1359638a",
 "ExternalImageId": "image9.jpg",
 "Confidence": `99.99979400634766,`
 "ImageId": `"67a34327-48d1-5179-b042-01e52ccfeada"`
 `},`
 "Similarity": `98.24278259277344`
 `},`
 `{`
 "Face": `{`
 "BoundingBox": `{`
 "Width": `0.5307819843292236,`
 "Top": `0.2862499952316284,`
 "Left": `0.1564060002565384,`
 "Height": `0.3987500071525574`
 `},`
 "FaceId": "2eb5f3fd-e2a9-4b1c-a89f-afa0a518fe06",
 "ExternalImageId": "image10.jpg",
 "Confidence": `99.99970245361328,`
 "ImageId": `"3c314792-197d-528d-bbb6-798ed012c150"`
 `},`
 "Similarity": `98.10665893554688`
 `},`
 `{`
 "Face": `{`
 "BoundingBox": `{`
 "Width": `0.5074880123138428,`
 "Top": `0.3774999976158142,`
 "Left": `0.18302799761295319,`
 "Height": `0.3812499940395355`
 `},`
 "FaceId": "086261e8-6deb-4bc0-ac73-ab22323cc38d",
 "ExternalImageId": "image6.jpg",
 "Confidence": `99.99930572509766,`
 "ImageId": `"ae1593b0-a8f6-5e24-a306-abf529e276fa"`
 `},`
 "Similarity": `98.10526275634766`
 `},`
 `{`
 "Face": `{`
 "BoundingBox": `{`
 "Width": `0.5574039816856384,`
 "Top": `0.37187498807907104,`
 "Left": `0.14559100568294525,`
 "Height": `0.4181250035762787`
 `},`
 "FaceId": "11c4bd3c-19c5-4eb8-aecc-24feb93a26e1",
 "ExternalImageId": "image5.jpg",
 "Confidence": `99.99960327148438,`
 "ImageId": `"80739b4d-883f-5b78-97cf-5124038e26b9"`
 `},`
 "Similarity": `97.94659423828125`
 `},`
 `{`
 "Face": `{`
 "BoundingBox": `{`
 "Width": `0.5773710012435913,`
 "Top": `0.34437501430511475,`
 "Left": `0.12396000325679779,`
 "Height": `0.4337500035762787`
 `},`
 "FaceId": "57189455-42b0-4839-a86c-abda48b13174",
 "ExternalImageId": "image8.jpg",
 "Confidence": `100.0,`
 "ImageId": `"0aff2f37-e7a2-5dbc-a3a3-4ef6ec18eaa0"`
 `},`
 "Similarity": `97.93476867675781`
 `}`
 `],`
 "FaceModelVersion": `"3.0"`
`}``

```

For more information, see [Searching for a Face Using an Image](search-face-with-image-procedure.md "search-face-with-image-procedure.md") in the _Amazon Rekognition Developer Guide_.

- For API details, see
  [SearchFacesByImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces-by-image.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces-by-image.html")
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
import software.amazon.awssdk.services.rekognition.model.SearchFacesRequest;
import software.amazon.awssdk.services.rekognition.model.SearchFacesResponse;
import software.amazon.awssdk.services.rekognition.model.FaceMatch;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class SearchFaceMatchingIdCollection {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <collectionId> <sourceImage>

                Where:
                   collectionId - The id of the collection. \s
                   sourceImage - The path to the image (for example, C:\\AWS\\pic1.png).\s
                """;

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String collectionId = args[0];
        String faceId = args[1];
        Region region = Region.US_WEST_2;
        RekognitionClient rekClient = RekognitionClient.builder()
                .region(region)
                .build();

        System.out.println("Searching for a face in a collections");
        searchFacebyId(rekClient, collectionId, faceId);
        rekClient.close();
    }

    public static void searchFacebyId(RekognitionClient rekClient, String collectionId, String faceId) {
        try {
            SearchFacesRequest searchFacesRequest = SearchFacesRequest.builder()
                    .collectionId(collectionId)
                    .faceId(faceId)
                    .faceMatchThreshold(70F)
                    .maxFaces(2)
                    .build();

            SearchFacesResponse imageResponse = rekClient.searchFaces(searchFacesRequest);
            System.out.println("Faces matching in the collection");
            List<FaceMatch> faceImageMatches = imageResponse.faceMatches();
            for (FaceMatch face : faceImageMatches) {
                System.out.println("The similarity level is  " + face.similarity());
                System.out.println();
            }

        } catch (RekognitionException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [SearchFacesByImage](../../../goto/SdkForJavaV2/rekognition-2016-06-27/SearchFacesByImage.md "../../../goto/SdkForJavaV2/rekognition-2016-06-27/SearchFacesByImage.md")
  in _AWS SDK for Java 2.x API Reference_.

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


    def search_faces_by_image(self, image, threshold, max_faces):
        """
        Searches for faces in the collection that match the largest face in the
        reference image.

        :param image: The image that contains the reference face to search for.
        :param threshold: The match confidence must be greater than this value
                          for a face to be included in the results.
        :param max_faces: The maximum number of faces to return.
        :return: A tuple. The first element is the face found in the reference image.
                 The second element is the list of matching faces found in the
                 collection.
        """
        try:
            response = self.rekognition_client.search_faces_by_image(
                CollectionId=self.collection_id,
                Image=image.image,
                FaceMatchThreshold=threshold,
                MaxFaces=max_faces,
            )
            image_face = RekognitionFace(
                {
                    "BoundingBox": response["SearchedFaceBoundingBox"],
                    "Confidence": response["SearchedFaceConfidence"],
                }
            )
            collection_faces = [
                RekognitionFace(face["Face"]) for face in response["FaceMatches"]
            ]
            logger.info(
                "Found %s faces in the collection that match the largest "
                "face in %s.",
                len(collection_faces),
                image.image_name,
            )
        except ClientError:
            logger.exception(
                "Couldn't search for faces in %s that match %s.",
                self.collection_id,
                image.image_name,
            )
            raise
        else:
            return image_face, collection_faces



```

- For API details, see
  [SearchFacesByImage](../../../goto/boto3/rekognition-2016-06-27/SearchFacesByImage.md "../../../goto/boto3/rekognition-2016-06-27/SearchFacesByImage.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rek#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rek#code-examples").

```
    TRY.
        " Create S3 object reference for the image
        DATA(lo_s3object) = NEW /aws1/cl_reks3object(
          iv_bucket = iv_s3_bucket
          iv_name = iv_s3_key ).

        " Create image object
        DATA(lo_image) = NEW /aws1/cl_rekimage(
          io_s3object = lo_s3object ).

        " Search for matching faces
        oo_result = lo_rek->searchfacesbyimage(
          iv_collectionid = iv_collection_id
          io_image = lo_image
          iv_facematchthreshold = iv_threshold
          iv_maxfaces = iv_max_faces ).

        DATA(lt_face_matches) = oo_result->get_facematches( ).
        DATA(lv_match_count) = lines( lt_face_matches ).
        DATA(lv_msg4) = |Face search completed: { lv_match_count } match(es) found.|.
        MESSAGE lv_msg4 TYPE 'I'.
      CATCH /aws1/cx_rekresourcenotfoundex.
        MESSAGE 'Collection not found.' TYPE 'E'.
      CATCH /aws1/cx_rekinvalids3objectex.
        MESSAGE 'Invalid S3 object.' TYPE 'E'.
      CATCH /aws1/cx_rekinvalidparameterex.
        MESSAGE 'Invalid parameter value.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [SearchFacesByImage](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Rekognition with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
