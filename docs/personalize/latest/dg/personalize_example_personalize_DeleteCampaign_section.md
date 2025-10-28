# Use `DeleteCampaign` with an AWS SDK

The following code example shows how to use `DeleteCampaign`.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/personalize#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/personalize#code-examples").

```
    public static void deleteSpecificCampaign(PersonalizeClient personalizeClient, String campaignArn) {
        try {
            DeleteCampaignRequest campaignRequest = DeleteCampaignRequest.builder()
                    .campaignArn(campaignArn)
                    .build();

            personalizeClient.deleteCampaign(campaignRequest);
            System.out.println("Delete request sent successfully.");
        } catch (PersonalizeException e) {
            System.err.println("Error deleting campaign: " + e.awsErrorDetails().errorMessage());
            throw new RuntimeException(e);
        }
    }
}


```

- For API details, see
  [DeleteCampaign](../../../goto/SdkForJavaV2/personalize-2018-05-22/DeleteCampaign.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DeleteCampaign.md")
  in _AWS SDK for Java 2.x API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Personalize with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
