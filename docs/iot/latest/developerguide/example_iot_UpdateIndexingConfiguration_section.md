# Use `UpdateIndexingConfiguration` with an AWS SDK or CLI

The following code examples show how to use `UpdateIndexingConfiguration`.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/iot#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/iot#code-examples").

```
//! Update the indexing configuration.
/*!
  \param thingIndexingConfiguration: A ThingIndexingConfiguration object which is ignored if not set.
  \param thingGroupIndexingConfiguration: A ThingGroupIndexingConfiguration object which is ignored if not set.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::IoT::updateIndexingConfiguration(
        const Aws::IoT::Model::ThingIndexingConfiguration &thingIndexingConfiguration,
        const Aws::IoT::Model::ThingGroupIndexingConfiguration &thingGroupIndexingConfiguration,
        const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::IoT::IoTClient iotClient(clientConfiguration);

    Aws::IoT::Model::UpdateIndexingConfigurationRequest request;

    if (thingIndexingConfiguration.ThingIndexingModeHasBeenSet()) {
        request.SetThingIndexingConfiguration(thingIndexingConfiguration);
    }

    if (thingGroupIndexingConfiguration.ThingGroupIndexingModeHasBeenSet()) {
        request.SetThingGroupIndexingConfiguration(thingGroupIndexingConfiguration);
    }

    Aws::IoT::Model::UpdateIndexingConfigurationOutcome outcome = iotClient.UpdateIndexingConfiguration(
            request);

    if (outcome.IsSuccess()) {
        std::cout << "UpdateIndexingConfiguration succeeded." << std::endl;
    }
    else {
        std::cerr << "UpdateIndexingConfiguration failed."
                  << outcome.GetError().GetMessage() << std::endl;
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [UpdateIndexingConfiguration](../../../goto/SdkForCpp/iot-2015-05-28/UpdateIndexingConfiguration.md "../../../goto/SdkForCpp/iot-2015-05-28/UpdateIndexingConfiguration.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**To enable thing indexing**

The following `update-indexing-configuration` example enables thing indexing to support searching registry data, shadow data, and thing connectivity status using the AWS_Things index.

```
`aws iot update-indexing-configuration
 --thing-indexing-configuration `thingIndexingMode=REGISTRY_AND_SHADOW,thingConnectivityIndexingMode=STATUS``

```

This command produces no output.

For more information, see [Managing Thing Indexing](managing-index.md "managing-index.md") in the _AWS IoT Developers Guide_.

- For API details, see
  [UpdateIndexingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-indexing-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-indexing-configuration.html")
  in _AWS CLI Command Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS IoT with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
