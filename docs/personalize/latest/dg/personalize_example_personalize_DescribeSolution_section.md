

# Use `DescribeSolution` with an AWS SDK
<a name="personalize_example_personalize_DescribeSolution_section"></a>

The following code example shows how to use `DescribeSolution`.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/personalize#code-examples). 

```
    public static void describeSpecificSolution(PersonalizeClient personalizeClient, String solutionArn) {

        try {
            DescribeSolutionRequest solutionRequest = DescribeSolutionRequest.builder()
                    .solutionArn(solutionArn)
                    .build();

            DescribeSolutionResponse response = personalizeClient.describeSolution(solutionRequest);
            System.out.println("The Solution name is " + response.solution().name());

        } catch (PersonalizeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DescribeSolution](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/DescribeSolution) in *AWS SDK for Java 2.x API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon Personalize with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.