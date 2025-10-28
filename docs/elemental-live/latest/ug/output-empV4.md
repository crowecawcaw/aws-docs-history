# Delivering HLS output to MediaPackage version

2

This section describes how to deliver an HLS output from AWS Elemental Live to an AWS Elemental MediaPackage
channel that uses MediaPackage v2. You can optionally configure the video output
for low latency, to support a glass-to-glass low latency workflow.

The information in this section assumes that you are familiar with the
general steps for creating an event.

1. Obtain the following information from the MediaPackage operator:
   - The URL for each destination for the output group. For
     delivery to MediaPackage v2, the URL will always include the string
     `mediapackagev2`.

   - The credentials that Elemental Live must include to deliver
     this output to MediaPackage v2. For example:

   An _access key ID_ that
   looks like this:
   `AKIAIOSFODNN7EXAMPLE`

   A _secret access key_ that
   looks like this:
   `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

2. In the Elemental Live event, go to **Output
   Groups**, then to **Apple HLS**.
3. Set up the output group in the usual way. Complete the following
   fields as specified:

| Section                       | Field                                                                            | Description                                                                                                                                                                                     |
| ----------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Apple HLS Settings            | Destination                                                                      | The URL that you obtained from the MediaPackage operator. When you tab out of this field, two fields automatically appear: **Username or Access Key ID** and **Password or Secret Access Key**. |
| Username or Access Key ID     | Enter the access key ID that you obtained from the MediaPackage operator.        |                                                                                                                                                                                                 | Password or Secret Access Key | Enter the secret access key that you obtained from the MediaPackage operator.     |
| HTTP Push Dialect             | Choose **Basic PUT**                                                             |                                                                                                                                                                                                 | Advanced > Encryption         | Choose **Disabled** because MediaPackage doesn't support encryption.              |
| Advanced > Chunked Transfer   | Choose **Disabled**.                                                             |                                                                                                                                                                                                 | Outputs                       | Segment Type                                                                      | Choose **TS**. You can't send fMP4 to MediaPackage.                                     | 4. If you want to implement low latency in the encoder, follow the guidance for these fields: |
| Section                       | Field                                                                            | Description                                                                                                                                                                                     |
| ---                           | ---                                                                              | ---                                                                                                                                                                                             |
| Apple HLS Settings            | Segment Length                                                                   | We recommend 1 second for better latency.                                                                                                                                                       |
| Minimum Segment Length        | A value is required for delivery to MediaPackage. This value can affect latency. |                                                                                                                                                                                                 | Retry Interval                | We recommend the same value as the segment length. This value can affect latency. |
| Num Retries                   | This value can affect latency.                                                   |                                                                                                                                                                                                 | FileCache Size                | This value can affect latency. We recommend a lower number.                       |
| Restart Delay                 | This value can affect latency.                                                   |                                                                                                                                                                                                 | Outputs                       | Advanced > GOP Size                                                               | This value can affect latency because the segment length is a function of the GOP size. |
| Advanced > Closed GOP Cadence | This value can affect latency.                                                   |
