# Use `PutAnomalyDetector` with an AWS SDK or CLI

The following code examples show how to use `PutAnomalyDetector`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Learn the basics](example_cloudwatch_GetStartedMetricsDashboardsAlarms_section.md "example_cloudwatch_GetStartedMetricsDashboardsAlarms_section.md")

.NET


**SDK for .NET (v4)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples").
 



```
    /// <summary>
    /// Add an anomaly detector for a single metric.
    /// </summary>
    /// <param name="anomalyDetector">A single metric anomaly detector.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutAnomalyDetector(SingleMetricAnomalyDetector anomalyDetector)
    {
        var putAlarmDetectorResult = await _amazonCloudWatch.PutAnomalyDetectorAsync(
            new PutAnomalyDetectorRequest()
            {
                SingleMetricAnomalyDetector = anomalyDetector
            });

        return putAlarmDetectorResult.HttpStatusCode == HttpStatusCode.OK;
    }


```


* For API details, see
 [PutAnomalyDetector](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAnomalyDetector")
 in *AWS SDK for .NET API Reference*.




CLI


**AWS CLI**

**To create an anomaly detection model**


The following `put-anomaly-detector` example creates an anomaly detection model for a CloudWatch metric.



```
`aws cloudwatch put-anomaly-detector \
 --namespace `AWS/Logs` \
 --metric-name `IncomingBytes` \
 --stat `SampleCount``

```

This command produces no output.


For more information, see [Using CloudWatch anomaly detection](CloudWatch_Anomaly_Detection.md "CloudWatch_Anomaly_Detection.md") in the *Amazon CloudWatch User Guide*.



* For API details, see
 [PutAnomalyDetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-anomaly-detector.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-anomaly-detector.html")
 in *AWS CLI Command Reference*.




Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples").
 



```

    /**
     * Adds an anomaly detector for the given file.
     *
     * @param fileName the name of the file containing the anomaly detector configuration
     * @return a {@link CompletableFuture} that completes when the anomaly detector has been added
     */
    public CompletableFuture<Void> addAnomalyDetectorAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser); // Return the root node
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            try {
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                SingleMetricAnomalyDetector singleMetricAnomalyDetector = SingleMetricAnomalyDetector.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .stat("Maximum")
                    .build();

                PutAnomalyDetectorRequest anomalyDetectorRequest = PutAnomalyDetectorRequest.builder()
                    .singleMetricAnomalyDetector(singleMetricAnomalyDetector)
                    .build();

                return getAsyncClient().putAnomalyDetector(anomalyDetectorRequest).thenAccept(response -> {
                    logger.info("Added anomaly detector for metric {}", customMetricName);
                });
            } catch (Exception e) {
                throw new RuntimeException("Failed to create anomaly detector", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error adding anomaly detector", exception);
            }
        });
    }


```


* For API details, see
 [PutAnomalyDetector](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAnomalyDetector")
 in *AWS SDK for Java 2.x API Reference*.




Kotlin


**SDK for Kotlin**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples").
 



```
suspend fun addAnomalyDetector(fileName: String?) {
    // Read values from the JSON file.
    val parser = JsonFactory().createParser(File(fileName))
    val rootNode = ObjectMapper().readTree<JsonNode>(parser)
    val customMetricNamespace = rootNode.findValue("customMetricNamespace").asText()
    val customMetricName = rootNode.findValue("customMetricName").asText()

    val singleMetricAnomalyDetectorVal =
        SingleMetricAnomalyDetector {
            metricName = customMetricName
            namespace = customMetricNamespace
            stat = "Maximum"
        }

    val anomalyDetectorRequest =
        PutAnomalyDetectorRequest {
            singleMetricAnomalyDetector = singleMetricAnomalyDetectorVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putAnomalyDetector(anomalyDetectorRequest)
        println("Added anomaly detector for metric $customMetricName.")
    }
}


```


* For API details, see
 [PutAnomalyDetector](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
 in *AWS SDK for Kotlin API reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Using CloudWatch with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
