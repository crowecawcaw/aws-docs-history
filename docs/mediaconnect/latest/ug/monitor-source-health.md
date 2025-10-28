# Monitoring the health of a MediaConnect source

In the AWS Elemental MediaConnect console, you can view Amazon CloudWatch metrics that show the health of
the source over a period of time. Source health is reported with the following
metrics:

- **Source bitrate** – The bitrate of
  the incoming video.
- **Total packets received** – The total
  number of packets that MediaConnect received.

###### To monitor the health of a source (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the
   flow.
3. Choose the **Source** tab and view the status of your
   source. This includes:
   - The **Source health** field provides the current
     status of the source.
     - **Connected** indicates that the flow is
       connected successfully to its source.
     - **Disconnected** indicates that the flow
       is not connected to its source. To resolve this issue,
       verify that the source is actually sending content. Also,
       check the source settings on the flow such as the allowlist
       CIDR and the protocol configuration.
     - **The flow is inactive** indicates that
       the flow has not been started. To resolve this issue, [start the flow](flows-start.md "flows-start.md").
     - **Error** indicates that MediaConnect doesn't
       have permission to communicate with CloudWatch. To resolve the
       error, you must sign in to the AWS Management Console as an entity
       that allows MediaConnect to get metric statistics from CloudWatch. For
       guidance, see [this example](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console").

   - The **Source health metrics** section is visible
     only if your source health is **Connected**. The
     charts show source bitrate and total packets received over the last
     hour. You can choose different time periods from the dropdown in the
     top-right corner of the section.

   ###### Note

   MediaConnect refreshes data from CloudWatch automatically every 1 minute, 5
   minutes, or 30 minutes, depending on the time period that you
   chose. When the charts refresh, data is 1 minute behind real
   time.
