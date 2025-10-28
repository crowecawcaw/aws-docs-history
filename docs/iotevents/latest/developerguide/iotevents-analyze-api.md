End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Troubleshooting a detector model by running

analyses in AWS IoT Events

AWS IoT Events can analyze your detector model and generate analysis results without sending input
data to your detector model. AWS IoT Events performs a series of analyses described in this section
to check your detector model. This advanced troubleshooting solution also summarizes
diagnostic information, including the severity level and location, so that you can quickly
find and fix potential issues in your detector model. For more information about diagnostic
error types and messages for your detector model, see [Detector model analysis and diagnostic
information for AWS IoT Events](analyze-diagnostic-information.md "analyze-diagnostic-information.md").

You can use the AWS IoT Events console, [API](../apireference.md "../apireference.md"), [AWS Command Line Interface (AWS CLI)](../../../cli/latest/reference/iotevents/index.md "../../../cli/latest/reference/iotevents/index.md"), or [AWS SDK](../../../iot/latest/developerguide/iot-sdks.md "../../../iot/latest/developerguide/iot-sdks.md") to view diagnostic error messages from the analysis of your detector model.

###### Note

- You must fix all errors before you can publish your detector model.
- We recommend that you review warnings
  and take necessary actions before you use your detector model in production environments.
  Otherwise, the detector model might not work as expected.
- You can have up to 10 analyses in the `RUNNING` status at the
  same time.
  To learn how to analyze your detector model, see [Analyze a detector model for AWS IoT Events (Console)](analyze-api-console.md "analyze-api-console.md") or
  [Analyze a detector model in AWS IoT Events (AWS CLI)](analyze-api-api.md "analyze-api-api.md").

###### Topics

- [Detector model analysis and diagnostic
  information for AWS IoT Events](analyze-diagnostic-information.md "analyze-diagnostic-information.md")
- [Analyze a detector model for AWS IoT Events (Console)](analyze-api-console.md "analyze-api-console.md")
- [Analyze a detector model in AWS IoT Events (AWS CLI)](analyze-api-api.md "analyze-api-api.md")
