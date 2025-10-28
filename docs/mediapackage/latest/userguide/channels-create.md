# Creating a channel in AWS Elemental MediaPackage

These steps show how to create a channel in MediaPackage to start receiving content streams.
Later, you add an origin endpoint to the channel. This endpoint is the access point for
content playback requests. We recommend that you spread out channels between channel
groups, such as putting redundant channels in the same AWS Region in different channel
groups.

You can use the MediaPackage console, MediaPackage API, or AWS CLI to create a channel. When
you're creating a channel, don't put sensitive identifying information like customer
account numbers into free-form fields such as the name or description field. MediaPackage
doesn’t require that you supply any customer data. This includes when you work with
MediaPackage using the MediaPackage console, MediaPackage API, AWS CLI, or AWS SDKs. Any data that you
enter into MediaPackage might get picked up for inclusion in diagnostic logs or Amazon CloudWatch Events.

###### To create a channel

1. Access the channel group that the channel will be associated with, as
   described in [Viewing channel group details in AWS Elemental MediaPackage](channel-group-view.md "channel-group-view.md").
2. Choose **Create channel** from the
   **Channels** list.
3. For **Name**, enter a name that describes the channel. The
   name is the primary identifier for the channel, and must be unique for your
   account in the AWS Region and channel group. Supported characters are
   **A-Z**, **a-z**,
   **0-9**, **\_**
   (underscore), and **-** (hyphen) with a length of 1
   to 256 characters. You can't use spaces in the name, and you can't change the
   name after you create the channel.

The name is the primary identifier for the channel, and it must be unique for
your account in the AWS Region and channel group. 4. (Optional) For **Description**, enter descriptive text to
help you identify the channel. 5. Choose the **Input type** that you want to use for your
channel:

    * **HLS** input type requires your live encoder to
     produce HLS with TS streams and to ingest it onto MediaPackage using plain HTTP
     PUT requests.
    * **CMAF** requires your live encoder to follow
     the [DASH-IF Live Media Ingest Protocol version 1.2](https://dashif.org/guidelines/others/#dash-if-technical-specification-live-media-ingest "https://dashif.org/guidelines/others/#dash-if-technical-specification-live-media-ingest"), producing
     and ingesting CMAF streams using Interface-1 (CMAF Ingest, described in
     section 6).


    MediaPackage CMAF Ingest has currently been tested with MediaLive and the AWS
     Elemental Live encoder. A detailed specification of the MediaPackage encoder
     requirements for CMAF ingest is available upon request to live-encoder
     manufacturers who would want to validate interoperability of their
     solution with MediaPackage CMAF Ingest.

###### Important

Once you will have created your channel, you will not be able to change
its input type. Certain features, like cross-region failover support, are
available only on channels using CMAF ingest - and more upcoming features
will also be available only with CMAF ingest. We advise you to leverage CMAF
Ingest if you can. 6. (Optional) If you're using CMAF inputs, make your selections for
**Media quality confidence score (MQCS) settings**.

    * To allow MediaPackage to switch inputs based on the quality score from
     AWS Elemental MediaLive, choose **Enable input switch based on
     MQCS**.
    * To include the MQCS in the outputs from your endpoints on this
     channel, choose **Enable MQCS publishing in Common Media Server
     Data (CMSD)**.
    * (Optional) To specify which input MediaPackage should prefer when both inputs
     have equal MQCS scores, choose a value for **Preferred
     input**. Select **Input 1** to prefer the
     first ingest endpoint, or **Input 2** to prefer the
     second ingest endpoint. If you don't specify a preferred input, MediaPackage
     uses its default switching behavior when MQCS scores are equal.


    The preferred input setting helps ensure consistent behavior across
     multiple MediaPackage channels in different regions when using cross-region
     architectures.

You can choose one, both, or none of the settings.

For information about MQCS, including workflow set up requirements and how
preferred input selection works, see [Leveraging media quality scores with AWS Elemental MediaPackage](mqcs.md "mqcs.md"). For information about CMSD headers, see [CMSD headers from AWS Elemental MediaPackage](cmsd.md "cmsd.md"). 7. Choose your channel's IAM policy settings from the following options:

    * **Don't attach a policy** – Restrict access to
     only those who have access to this account's credentials.


    Choose this option if you're using AWS Elemental MediaLive in the same account as
     MediaPackage.
    * **Attach a custom policy** – Define your own
     policy and restrict access to as few or as many accounts and resources
     you want. Enter a valid JSON object with the same structure as other
     IAM policies. The policy should follow the standard security advice of
     granting least privilege, or granting only the permissions required to
     perform a task.


    If you're not using MediaLive, choose this option and define your
     policy.

For more information about policies, see [Resource-based policy examples](using-iam-policies.md "using-iam-policies.md"). 8. Choose **Create**.

MediaPackage displays the new channel's details page.

After you create a channel, MediaPackage provides two ingest endpoint domain URLs
that are fixed for the lifetime of the channel. The channel is active and can
start receiving content as soon as it's created. Provide this information for
the upstream encoder stream destination settings. MediaPackage dynamically adjusts
resources to increase capacity for your traffic.

If you're using input redundancy and one of the inputs stops sending content,
then MediaPackage automatically switches to the other input for the source content. For
more information about how input redundancy works, see [Live input redundancy AWS Elemental MediaPackage processing
flow](what-is-flow-ir.md "what-is-flow-ir.md").

While you create a channel, if you exceed the quotas on the account, you'll
receive an error. The error will be similar to **`Too many requests,
 please try again. Resource limit exceeded`**. This error means that
either you exceeded the API request quotas, or that you reached the maximum
number of channels that your account permits.
To permit downstream video players and content delivery networks (CDNs) to request
content playback from MediaPackage, you must add an origin endpoint to a channel.

For instructions on adding endpoints to a channel from the MediaPackage console,
see [Working with origin endpoints in AWS Elemental MediaPackage](endpoints.md "endpoints.md").
