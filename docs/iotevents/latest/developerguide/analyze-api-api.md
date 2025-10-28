End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Analyze a detector model in AWS IoT Events (AWS CLI)

Analyzing your AWS IoT Events detector models programmatically provides valuable insights into
their structure, behavior, and performance. This API-based approach allows for automated
analysis, integration with your existing workflows, and the ability to perform bulk
operations across multiple detector models. By leveraging the [StartDetectorModelAnalysis](../apireference/API_StartDetectorModelAnalysis.md "../apireference/API_StartDetectorModelAnalysis.md") API, you can initiate in-depth examinations of your
models, helping you identify potential issues, optimize logic flows, and ensure that your
IoT event processing aligns with your business requirements.

The following steps use the AWS CLI to analyze a detector model.

###### To analyze a detector model using AWS CLI

1. Run the following command to start an analysis.

```
aws iotevents start-detector-model-analysis --cli-input-json file://`file-name`.json
```

###### Note

Replace `file-name` with the name of the file that
contains the detector model definition.

###### Example Detector model definition

```
{
    "detectorModelDefinition": {
        "states": [
            {
                "stateName": "TemperatureCheck",
                "onInput": {
                    "events": [
                        {
                            "eventName": "Temperature Received",
                            "condition": "isNull($input.TemperatureInput.sensorData.temperature)==false",
                            "actions": [
                                {
                                    "iotTopicPublish": {
                                        "mqttTopic": "IoTEvents/Output"
                                    }
                                }
                            ]
                        }
                    ],
                    "transitionEvents": []
                },
                "onEnter": {
                    "events": [
                        {
                            "eventName": "Init",
                            "condition": "true",
                            "actions": [
                                {
                                    "setVariable": {
                                        "variableName": "temperatureChecked",
                                        "value": "0"
                                    }
                                }
                            ]
                        }
                    ]
                },
                "onExit": {
                    "events": []
                }
            }
        ],
        "initialStateName": "TemperatureCheck"
    }
}
```

If you use the AWS CLI to analyze an existing detector
model,
choose one of the following to retrieve the detector model
definition:

    * If you want to use the AWS IoT Events console, do the following:




    	1. In navigation pane, choose **Detector
    	 models**.
    	2. Under **Detector models**, choose the target
    	 detector model.
    	3. Choose **Export detector model** from
    	 **Action** to download the detector model. The
    	 detector model is saved in JSON.
    	4. Open the detector model JSON file.
    	5. You only need the `detectorModelDefinition` object.
    	 Remove the following:




    		+ The first curly bracket (`{`) at the top of the
    		 page
    		+ The `detectorModel` line
    		+ The `detectorModelConfiguration` object
    		+ The last curly bracket (`}`) at the bottom of
    		 the page
    	6. Save the file.
    * If you want to use the AWS CLI, do the following:




    	1. Run the following command in a terminal.



    	```
    	aws iotevents describe-detector-model --detector-model-name `detector-model-name`
    	```
    	2. Replace `detector-model-name` with the
    	 name of your detector model.
    	3. Copy the `detectorModelDefinition` object to a text
    	 editor.
    	4. Add curly brackets (`{}`) outside of the
    	 `detectorModelDefinition`.
    	5. Save the file in JSON.

###### Example response

```
{
    "analysisId": "c1133390-14e3-4204-9a66-31efd92a4fed"
}
```

2. Copy the analysis ID from the output.
3. Run the following command to retrieve the status of the analysis.

```
aws iotevents describe-detector-model-analysis --analysis-id "`analysis-id`"
```

###### Note

Replace `analysis-id` with the analysis ID that you
copied.

###### Example response

```
{
    "status": "COMPLETE"
}
```

The status can be one of the following values:

    * `RUNNING` – AWS IoT Events is analyzing your detector model. This
     process can take up to one minute to complete.
    * `COMPLETE` – AWS IoT Events finished analyzing your detector
     model.
    * `FAILED` – AWS IoT Events couldn't analyze your detector model.
     Try again later.

4. Run the following command to retrieve one or more analysis results of the detector
   model.

###### Note

Replace `analysis-id` with the analysis ID that you
copied.

```
aws iotevents get-detector-model-analysis-results --analysis-id "`analysis-id`"
```

###### Example response

```
{
    "analysisResults": [
        {
            "type": "data-type",
            "level": "INFO",
            "message": "Inferred data types [Integer] for $variable.temperatureChecked",
            "locations": []
        },
        {
            "type": "referenced-resource",
            "level": "ERROR",
            "message": "Detector Model Definition contains reference to Input 'TemperatureInput' that does not exist.",
            "locations": [
                {
                    "path": "states[0].onInput.events[0]"
                }
            ]
        }
    ]
}
```

###### Note

After AWS IoT Events starts analyzing your detector model, you have up to 24 hours to retrieve
the analysis results.
