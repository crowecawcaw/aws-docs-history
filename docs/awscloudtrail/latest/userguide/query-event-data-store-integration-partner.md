# Create an integration with a CloudTrail partner with the console

When you create an integration with an event source outside AWS, you can
choose one of these partners as your event source. When you create an integration in
CloudTrail with a partner application, the partner needs the Amazon Resource Name (ARN) of
the channel that you create in this workflow to send events to CloudTrail. After you create the
integration, you finish configuring the integration by following the partner's
instructions to provide the required channel ARN to the partner. The integration starts
ingesting partner events into CloudTrail after the partner calls `PutAuditEvents`
on the integration's channel.

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, under **Lake**, choose **Integrations**.
3. On the **Add integration** page, enter a name for your
   channel. The name can be 3-128 characters. Only letters, numbers, periods,
   underscores, and dashes are allowed.
4. Choose the partner application source from which you want to get events. If you're integrating with
   events from your own applications hosted on-premises or in the cloud, choose
   **My custom integration**.
5. From **Event delivery location**, choose to
   log the same activity events to existing event data stores, or
   create a new event data store.

If you choose to create a new event data store, enter a name for the event
data store, choose the pricing option, and specify the retention period in days. The event data
store retains event data for the specified number of days.

If you choose to log activity events to
one or more existing event data stores, choose the event data stores from the list.
The event data stores can only include activity events.
The event type in the console must be **Events from
integrations**. In the API, the `eventCategory`
value must be `ActivityAuditLog`. 6. In **Resource policy**, configure the resource policy for
the integration's channel. Resource policies are JSON policy documents that
specify what actions a specified principal can perform on the resource and
under what conditions. The accounts defined as principals in the resource
policy can call the `PutAuditEvents` API to deliver events to
your channel. The resource owner has implicit access to the
resource if their IAM policy allows the
`cloudtrail-data:PutAuditEvents` action.

The information required for the policy is determined by the integration
type. For a direction integration, CloudTrail automatically adds the partner's AWS account IDs, and requires you to enter the unique external ID provided by the partner. For a solution integration, you
must specify at least one AWS account ID as principal, and can optionally enter an external ID to prevent against confused deputy.

###### Note

If you do not create a resource policy for the channel, only the channel owner can call the `PutAuditEvents` API on the channel.

    1. For a direct integration, enter the external ID provided by your
     partner. The integration partner provides a unique external ID, such
     as an account ID or a randomly generated string, to use for the
     integration to prevent against confused deputy. The partner is
     responsible for creating and providing a unique external ID.



     You can choose **How to find this?** to view the partner's documentation
     that describes how to find the external ID.




    ![Partner documentation for external ID](images/integration-external-id.png)

    ###### Note

    If the resource policy includes an external ID, all calls to the
     `PutAuditEvents` API must include the external ID. However,
     if the policy does not define an external ID, the
     partner can still call the `PutAuditEvents`
     API and specify an `externalId` parameter.
    2. For a solution integration, choose **Add AWS
     account** to specify an AWS account ID to add as a
     principal in the policy.

7. (Optional) In the **Tags** area, you can add up to 50 tag
   key and value pairs to help you identify, sort, and control access to your
   event data store and channel. For more information about how to use IAM
   policies to authorize access to an event data store based on tags, see [Examples: Denying
   access to create or delete event data stores based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags"). For
   more information about how you can use tags in AWS, see [Tagging
   AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the
   _AWS General Reference_.
8. When you are ready to create the new integration, choose **Add
   integration**. There is no review page. CloudTrail creates the
   integration, but you must provide the channel Amazon Resource Name (ARN) to the partner application. Instructions for providing the channel ARN
   to the partner application are found on the partner documentation website.
   For more information, choose the **Learn more**
   link for the partner on the **Available sources** tab of the **Integrations** page to open the partner's page in
   AWS Marketplace.
   To finish the setup for your
   integration, provide the channel ARN to the partner or source application. Depending upon the integration type, either you,
   the partner, or the application runs the `PutAuditEvents` API to deliver activity events to the event data store for your
   AWS account. After your activity events are delivered, you can use CloudTrail Lake to search,
   query, and analyze the data that is logged from your applications. Your event data includes fields that match CloudTrail
   event payload, such as `eventVersion`, `eventSource`, and
   `userIdentity`.
