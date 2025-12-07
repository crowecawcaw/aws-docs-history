# Use `DeleteAlarms` with an AWS SDK or CLI

The following code examples show how to use `DeleteAlarms`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Learn the basics](example_cloudwatch_GetStartedMetricsDashboardsAlarms_section.md "example_cloudwatch_GetStartedMetricsDashboardsAlarms_section.md")
- [Get started with alarms](example_cloudwatch_Scenario_GettingStarted_section.md "example_cloudwatch_Scenario_GettingStarted_section.md")
- [Manage metrics and alarms](example_cloudwatch_Usage_MetricsAlarms_section.md "example_cloudwatch_Usage_MetricsAlarms_section.md")

.NET

**SDK for .NET (v4)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples").

```
    /// <summary>
    /// Delete a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAlarms(List<string> alarmNames)
    {
        var deleteAlarmsResult = await _amazonCloudWatch.DeleteAlarmsAsync(
            new DeleteAlarmsRequest()
            {
                AlarmNames = alarmNames
            });

        return deleteAlarmsResult.HttpStatusCode == HttpStatusCode.OK;
    }


```

- For API details, see
  [DeleteAlarms](../../../goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarms.md "../../../goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarms.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cloudwatch#code-examples").

Include the required files.

```
#include <aws/core/Aws.h>
#include <aws/monitoring/CloudWatchClient.h>
#include <aws/monitoring/model/DeleteAlarmsRequest.h>
#include <iostream>


```

Delete the alarm.

```
        Aws::CloudWatch::CloudWatchClient cw;
        Aws::CloudWatch::Model::DeleteAlarmsRequest request;
        request.AddAlarmNames(alarm_name);

        auto outcome = cw.DeleteAlarms(request);
        if (!outcome.IsSuccess())
        {
            std::cout << "Failed to delete CloudWatch alarm:" <<
                outcome.GetError().GetMessage() << std::endl;
        }
        else
        {
            std::cout << "Successfully deleted CloudWatch alarm " << alarm_name
                << std::endl;
        }


```

- For API details, see
  [DeleteAlarms](../../../goto/SdkForCpp/monitoring-2010-08-01/DeleteAlarms.md "../../../goto/SdkForCpp/monitoring-2010-08-01/DeleteAlarms.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**To delete an alarm**

The following example uses the `delete-alarms` command to delete the Amazon CloudWatch alarm
named "myalarm":

```
`aws cloudwatch delete-alarms --alarm-names `myalarm``

```

Output:

```
This command returns to the prompt if successful.
```

- For API details, see
  [DeleteAlarms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-alarms.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-alarms.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples").

```
    /**
     * Deletes a CloudWatch alarm.
     *
     * @param alarmName the name of the alarm to be deleted
     * @return a {@link CompletableFuture} representing the asynchronous operation to delete the alarm
     * the {@link DeleteAlarmsResponse} is returned when the operation completes successfully,
     * or a {@link RuntimeException} is thrown if the operation fails
     */
    public CompletableFuture<DeleteAlarmsResponse> deleteCWAlarmAsync(String alarmName) {
        DeleteAlarmsRequest request = DeleteAlarmsRequest.builder()
            .alarmNames(alarmName)
            .build();

        return getAsyncClient().deleteAlarms(request)
            .whenComplete((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to delete the alarm:{} " + alarmName, exception);
                } else {
                    logger.info("Successfully deleted alarm {} ", alarmName);
                }
            });
    }


```

- For API details, see
  [DeleteAlarms](../../../goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms.md "../../../goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cloudwatch#code-examples").

Import the SDK and client modules and call the API.

```
import { DeleteAlarmsCommand } from "@aws-sdk/client-cloudwatch";
import { client } from "../libs/client.js";

const run = async () => {
  const command = new DeleteAlarmsCommand({
    AlarmNames: [process.env.CLOUDWATCH_ALARM_NAME], // Set the value of CLOUDWATCH_ALARM_NAME to the name of an existing alarm.
  });

  try {
    return await client.send(command);
  } catch (err) {
    console.error(err);
  }
};

export default run();


```

Create the client in a separate module and export it.

```
import { CloudWatchClient } from "@aws-sdk/client-cloudwatch";

export const client = new CloudWatchClient({});


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/cloudwatch-examples-creating-alarms.md#cloudwatch-examples-creating-alarms-deleting "../../../sdk-for-javascript/v3/developer-guide/cloudwatch-examples-creating-alarms.md#cloudwatch-examples-creating-alarms-deleting").
- For API details, see
  [DeleteAlarms](../../../AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/DeleteAlarmsCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/DeleteAlarmsCommand.md")
  in _AWS SDK for JavaScript API Reference_.

**SDK for JavaScript (v2)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/cloudwatch#code-examples").

Import the SDK and client modules and call the API.

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatch service object
var cw = new AWS.CloudWatch({ apiVersion: "2010-08-01" });

var params = {
  AlarmNames: ["Web_Server_CPU_Utilization"],
};

cw.deleteAlarms(params, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data);
  }
});


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v2/developer-guide/cloudwatch-examples-creating-alarms.md#cloudwatch-examples-creating-alarms-deleting "../../../sdk-for-javascript/v2/developer-guide/cloudwatch-examples-creating-alarms.md#cloudwatch-examples-creating-alarms-deleting").
- For API details, see
  [DeleteAlarms](../../../goto/AWSJavaScriptSDK/monitoring-2010-08-01/DeleteAlarms.md "../../../goto/AWSJavaScriptSDK/monitoring-2010-08-01/DeleteAlarms.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples").

```
suspend fun deleteAlarm(alarmNameVal: String) {
    val request =
        DeleteAlarmsRequest {
            alarmNames = listOf(alarmNameVal)
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.deleteAlarms(request)
        println("Successfully deleted alarm $alarmNameVal")
    }
}


```

- For API details, see
  [DeleteAlarms](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cloudwatch#code-examples").

```
class CloudWatchWrapper:
    """Encapsulates Amazon CloudWatch functions."""

    def __init__(self, cloudwatch_resource):
        """
        :param cloudwatch_resource: A Boto3 CloudWatch resource.
        """
        self.cloudwatch_resource = cloudwatch_resource


    def delete_metric_alarms(self, metric_namespace, metric_name):
        """
        Deletes all of the alarms that are currently watching the specified metric.

        :param metric_namespace: The namespace of the metric.
        :param metric_name: The name of the metric.
        """
        try:
            metric = self.cloudwatch_resource.Metric(metric_namespace, metric_name)
            metric.alarms.delete()
            logger.info(
                "Deleted alarms for metric %s.%s.", metric_namespace, metric_name
            )
        except ClientError:
            logger.exception(
                "Couldn't delete alarms for metric %s.%s.",
                metric_namespace,
                metric_name,
            )
            raise




```

- For API details, see
  [DeleteAlarms](../../../goto/boto3/monitoring-2010-08-01/DeleteAlarms.md "../../../goto/boto3/monitoring-2010-08-01/DeleteAlarms.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cwt#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cwt#code-examples").

```
    TRY.
        lo_cwt->deletealarms(
          it_alarmnames = it_alarm_names ).
        MESSAGE 'Alarms deleted.' TYPE 'I'.
      CATCH /aws1/cx_cwtresourcenotfound.
        MESSAGE 'Resource being accessed is not found.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [DeleteAlarms](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using CloudWatch with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
