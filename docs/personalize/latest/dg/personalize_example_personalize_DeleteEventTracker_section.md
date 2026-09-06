

# Use `DeleteEventTracker` with an AWS SDK
<a name="personalize_example_personalize_DeleteEventTracker_section"></a>

The following code example shows how to use `DeleteEventTracker`.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/personalize#code-examples). 

```
    public static void deleteEventTracker(PersonalizeClient personalizeClient, String eventTrackerArn) {
        try {
            DeleteEventTrackerRequest deleteEventTrackerRequest = DeleteEventTrackerRequest.builder()
                    .eventTrackerArn(eventTrackerArn)
                    .build();

            int status = personalizeClient.deleteEventTracker(deleteEventTrackerRequest).sdkHttpResponse().statusCode();

            System.out.println("Status code:" + status);

        } catch (PersonalizeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DeleteEventTracker](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/DeleteEventTracker) in *AWS SDK for Java 2.x API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon Personalize with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.