**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Delete endpoints from Amazon Pinpoint programmatically

An endpoint represents a single method of contacting one of your customers. Each
endpoint can refer to a customer's email address, mobile device identifier, phone
number, or other type of destination that you can send messages to. In many
jurisdictions, this type of information might be considered personal. You can delete
endpoints when you no longer want to message a certain destination—such as
when the destination becomes unreachable, or when a customer
closes an account.

## Examples

The following examples show you how to delete an endpoint.

AWS CLIYou can use Amazon Pinpoint by running commands with the AWS CLI.

###### Example Delete endpoint command

To delete an endpoint, use the [`delete-endpoint`](../../../cli/latest/reference/pinpoint/delete-endpoint.md "../../../cli/latest/reference/pinpoint/delete-endpoint.md")
command:

```
`$` `aws pinpoint delete-endpoint \`
`>` `--application-id `application-id` \`
`>` `--endpoint-id `endpoint-id``
```

Where:

- _application-id_ is the ID of
  the Amazon Pinpoint project that contains the endpoint.
- _endpoint-id_ is the ID of
  the endpoint that you're deleting.
  The response to this command is the JSON definition of the endpoint
  that you deleted.

AWS SDK for JavaYou can use the Amazon Pinpoint API in your Java applications by using the client that's provided by the AWS SDK for Java.

###### Example Code

To delete an endpoint, use the `deleteEndpoint` method of
the `AmazonPinpoint` client. Provide a
`DeleteEndpointRequest` object as the method
argument:

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.pinpoint.PinpointClient;
import software.amazon.awssdk.services.pinpoint.model.DeleteEndpointRequest;
import software.amazon.awssdk.services.pinpoint.model.DeleteEndpointResponse;
import software.amazon.awssdk.services.pinpoint.model.PinpointException;

```

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.pinpoint.PinpointClient;
import software.amazon.awssdk.services.pinpoint.model.DeleteEndpointRequest;
import software.amazon.awssdk.services.pinpoint.model.DeleteEndpointResponse;
import software.amazon.awssdk.services.pinpoint.model.PinpointException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DeleteEndpoint {
    public static void main(String[] args) {
        final String usage = """

                Usage:   <appName> <endpointId >

                Where:
                  appId - The id of the application to delete.
                  endpointId - The id of the endpoint to delete.
                """;

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String appId = args[0];
        String endpointId = args[1];
        System.out.println("Deleting an endpoint with id: " + endpointId);
        PinpointClient pinpoint = PinpointClient.builder()
                .region(Region.US_EAST_1)
                .build();

        deletePinEncpoint(pinpoint, appId, endpointId);
        pinpoint.close();
    }

    public static void deletePinEncpoint(PinpointClient pinpoint, String appId, String endpointId) {
        try {
            DeleteEndpointRequest appRequest = DeleteEndpointRequest.builder()
                    .applicationId(appId)
                    .endpointId(endpointId)
                    .build();

            DeleteEndpointResponse result = pinpoint.deleteEndpoint(appRequest);
            String id = result.endpointResponse().id();
            System.out.println("The deleted endpoint id  " + id);

        } catch (PinpointException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        System.out.println("Done");
    }
}

```

For the full SDK example, see [DeleteEndpoint.java](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/pinpoint/src/main/java/com/example/pinpoint/DeleteEndpoint.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/pinpoint/src/main/java/com/example/pinpoint/DeleteEndpoint.java") on [GitHub](https://github.com/ "https://github.com/").

HTTPYou can use Amazon Pinpoint by making HTTP requests directly to the REST API.

###### Example DELETE endpoint request

To delete an endpoint, issue a `DELETE` request to the
[Endpoint](../apireference/apps-application-id-endpoints-endpoint-id.md "../apireference/apps-application-id-endpoints-endpoint-id.md") resource:

```
DELETE /v1/apps/`application-id`/endpoints/`endpoint-id` HTTP/1.1
Host: pinpoint.us-east-1.amazonaws.com
Content-Type: application/json
Accept: application/json
Cache-Control: no-cache
```

Where:

- _application-id_ is the ID of
  the Amazon Pinpoint project that contains the endpoint.
- _endpoint-id_ is the ID of
  the endpoint that you're deleting.
  The response to this request is the JSON definition of the endpoint
  that you deleted.
