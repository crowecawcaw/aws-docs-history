

# Use `DeleteSolution` with an AWS SDK
<a name="personalize_example_personalize_DeleteSolution_section"></a>

The following code example shows how to use `DeleteSolution`.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/personalize#code-examples). 

```
    public static void deleteGivenSolution(PersonalizeClient personalizeClient, String solutionArn) {

        try {
            DeleteSolutionRequest solutionRequest = DeleteSolutionRequest.builder()
                    .solutionArn(solutionArn)
                    .build();

            personalizeClient.deleteSolution(solutionRequest);
            System.out.println("Done");

        } catch (PersonalizeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DeleteSolution](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/DeleteSolution) in *AWS SDK for Java 2.x API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon Personalize with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.