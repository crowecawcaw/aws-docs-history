

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Troubleshooting segments
<a name="segments-troubleshooting"></a>

Verify that logging is turned on to assist in identifying the cause of failure. For more information, see [Monitoring and logging](troubleshooting.md#troubleshooting-logging). 

## Segment import failed
<a name="troubleshooting-segment-import"></a>

If a segment import fails, you might see the following error message or similar: 

**Import job**: Import failed for file SampleTemplate.csv with segment name SampleTemplate. Bad request: The data we received didn't match the format we expected for the createImportJob operation. Confirm that the information in your request is formatted properly, and then submit your request again.

****Issue and solution****
+ This error occurs when the imported template isn't formatted correctly.
+ Verify that the template is in valid JSON or CSV format. See [Segment files](segments-importing.md#segments-importing-examples-files) for an example of the correct format. A sample template can also be downloaded from the Console. Under your project, select **Segments**, **Create a segment**, **Import a segment**, and select **Download example CSV**.
+ Verify that all specified attributes are valid. **ChannelType** and **address** are required fields when importing segments. Attribute names are case-sensitive. For a complete list of possible attributes that can be added to a template, see [Supported attributes](segments-importing.md#segments-importing-available-attributes).

## Segment export failed
<a name="troubleshooting-segment-export"></a>

****Issue and solution****
+ Large export jobs may fail when performing this action from the console.
+ As a workaround for this limitation, the segment can be exported to an Amazon S3 bucket using the [CreateExportJob](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-export.html#apps-application-id-jobs-exportpost) API through the command line reference (CLI) or SDK.

## Endpoint count for a dynamic segment
<a name="troubleshooting-dynamic-segment"></a>

****Issues and solutions****
+ When using a dynamic segment to create a campaign, the number of endpoint count is an approximation and may not be accurate. This is because endpoint data in dynamic segments are subject to change over time based on the defined criteria. The segment can be exported to confirm the exact number of endpoints at a given point in time.

## BadRequestException: Exceeded maximum endpoint per user count: 15
<a name="troubleshooting-badrequestexception"></a>

This error occurs when attempting to add more than 15 endpoints associated with the same `UserId`.

**Note**  
If the new endpoint has a channel type of ADM, GCM, APNS, APNS\_VOICE, APNS\_VOIP\_SANDBOX, or BAIDU, the request will succeed if there's already an endpoint with one of those channel types. For more information, see [Managing an audience members maximum number of endpoints](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-auto-inactive.html) in the *Amazon Pinpoint Developer Guide*.

****Issue and solution****
+ You might see this error when creating new endpoints or editing existing ones using the [update-endpoint](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/update-endpoint.html) API, and the specific endpoint exceeds the maximum number of 15 endpoint addresses.
+ This limit is currently a hard limit with the service. It can't be increased. For more information, see [Endpoint quotas](https://docs.aws.amazon.com/pinpoint/latest/developerguide/quotas.html#quotas-endpoint).

## BadRequestException when calling the UpdateEndpointsBatch or UpdateEndpoints operation: Too many custom attributes
<a name="troubleshooting-attributes"></a>

This error occurs when attempting to add more than 250 attributes. Custom attributes can be a maximum of 15 KB per endpoint.

****Issue and solution****
+ Export the segment and inspect it to confirm the number of custom attributes.
+ To help resolve the exception, see [How do I resolve a "too many attributes" error in Amazon Pinpoint?](https://repost.aws/knowledge-center/pinpoint-additional-attributes)