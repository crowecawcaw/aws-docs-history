# Use `UntagResource` with an AWS SDK or CLI

The following code examples show how to use `UntagResource`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Tagging a data store](example_medical-imaging_Scenario_TaggingDataStores_section.md "example_medical-imaging_Scenario_TaggingDataStores_section.md")
- [Tagging an image set](example_medical-imaging_Scenario_TaggingImageSets_section.md "example_medical-imaging_Scenario_TaggingImageSets_section.md")

CLI

**AWS CLI**

**Example 1: To untag a data store**

The following `untag-resource` code example untags a data store.

```
`aws medical-imaging untag-resource \
 --resource-arn `"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012"` \
 --tag-keys '`["Deployment"]`'`

```

This command produces no output.

**Example 2: To untag an image set**

The following `untag-resource` code example untags an image set.

```
`aws medical-imaging untag-resource \
 --resource-arn `"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012/imageset/18f88ac7870584f58d56256646b4d92b"` \
 --tag-keys '`["Deployment"]`'`

```

This command produces no output.

- For API details, see
  [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/untag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/untag-resource.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

```
    public static void untagMedicalImagingResource(MedicalImagingClient medicalImagingClient,
            String resourceArn,
            Collection<String> tagKeys) {
        try {
            UntagResourceRequest untagResourceRequest = UntagResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .tagKeys(tagKeys)
                    .build();

            medicalImagingClient.untagResource(untagResourceRequest);

            System.out.println("Tags have been removed from the resource.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }


```

- For API details, see
  [UntagResource](../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/UntagResource.md "../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/UntagResource.md")
  in _AWS SDK for Java 2.x API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

```
import { UntagResourceCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} resourceArn - The Amazon Resource Name (ARN) for the data store or image set.
 * @param {string[]} tagKeys - The keys of the tags to remove.
 */
export const untagResource = async (
  resourceArn = "arn:aws:medical-imaging:us-east-1:xxxxxx:datastore/xxxxx/imageset/xxx",
  tagKeys = [],
) => {
  const response = await medicalImagingClient.send(
    new UntagResourceCommand({ resourceArn: resourceArn, tagKeys: tagKeys }),
  );
  console.log(response);
  // {
  //     '$metadata': {
  //        httpStatusCode: 204,
  //         requestId: '8a6de9a3-ec8e-47ef-8643-473518b19d45',
  //         extendedRequestId: undefined,
  //         cfId: undefined,
  //         attempts: 1,
  //         totalRetryDelay: 0
  //    }
  // }

  return response;
};


```

- For API details, see
  [UntagResource](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/UntagResourceCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/UntagResourceCommand.md")
  in _AWS SDK for JavaScript API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples").

Python

**SDK for Python (Boto3)**

```
class MedicalImagingWrapper:
    def __init__(self, health_imaging_client):
        self.health_imaging_client = health_imaging_client


    def untag_resource(self, resource_arn, tag_keys):
        """
        Untag a resource.

        :param resource_arn: The ARN of the resource.
        :param tag_keys: The tag keys to remove.
        """
        try:
            self.health_imaging_client.untag_resource(
                resourceArn=resource_arn, tagKeys=tag_keys
            )
        except ClientError as err:
            logger.error(
                "Couldn't untag resource. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise



```

The following code instantiates the MedicalImagingWrapper object.

```
    client = boto3.client("medical-imaging")
    medical_imaging_wrapper = MedicalImagingWrapper(client)


```

- For API details, see
  [UntagResource](../../../goto/boto3/medical-imaging-2023-07-19/UntagResource.md "../../../goto/boto3/medical-imaging-2023-07-19/UntagResource.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples").

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
