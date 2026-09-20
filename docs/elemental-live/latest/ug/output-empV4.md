

# Delivering HLS output to MediaPackage version 2
<a name="output-empV4"></a>

This section describes how to deliver an HLS output from AWS Elemental Live to an AWS Elemental MediaPackage channel that uses MediaPackage v2. You can optionally configure the video output for low latency, to support a glass-to-glass low latency workflow. 

The information in this section assumes that you are familiar with the general steps for creating an event. 

1. Obtain the following information from the MediaPackage operator:
   + The URL for each destination for the output group. For delivery to MediaPackage v2, the URL will always include the string `mediapackagev2`. 
   + The credentials that Elemental Live must include to deliver this output to MediaPackage v2. For example:

     An *access key ID* that looks like this: **AKIAIOSFODNN7EXAMPLE**

     A *secret access key* that looks like this: **wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY**

1. In the Elemental Live event, go to **Output Groups**, then to **Apple HLS**.

1. Set up the output group in the usual way. Complete the following fields as specified:


<table>
<thead>
  <tr><th>Section</th><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td rowspan="6">Apple HLS Settings</td><td>Destination</td><td>The URL that you obtained from the MediaPackage operator. When you tab out of this field, two fields automatically appear: <b>Username or Access Key ID</b> and <b>Password or Secret Access Key</b>.</td></tr>
  <tr><td>Username or Access Key ID</td><td>Enter the access key ID that you obtained from the MediaPackage operator. </td></tr>
  <tr><td>Password or Secret Access Key</td><td>Enter the secret access key that you obtained from the MediaPackage operator. </td></tr>
  <tr><td>HTTP Push Dialect</td><td>Choose <b>Basic PUT</b></td></tr>
  <tr><td>Advanced &gt; Encryption</td><td>Choose <b>Disabled</b> because MediaPackage doesn't support encryption.</td></tr>
  <tr><td>Advanced &gt; Chunked Transfer</td><td>Choose <b>Disabled</b>.</td></tr>
  <tr><td>Outputs</td><td>Segment Type</td><td>Choose <b>TS</b>. You can't send fMP4 to MediaPackage.</td></tr>
</tbody>
</table>


1. If you want to implement low latency in the encoder, follow the guidance for these fields:


<table>
<thead>
  <tr><th>Section</th><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td rowspan="6">Apple HLS Settings</td><td>Segment Length</td><td>We recommend 1 second for better latency.</td></tr>
  <tr><td>Minimum Segment Length</td><td>A value is required for delivery to MediaPackage. This value can affect latency.</td></tr>
  <tr><td>Retry Interval</td><td>We recommend the same value as the segment length. This value can affect latency.</td></tr>
  <tr><td>Num Retries</td><td>This value can affect latency.</td></tr>
  <tr><td>FileCache Size</td><td>This value can affect latency. We recommend a lower number.</td></tr>
  <tr><td>Restart Delay</td><td>This value can affect latency.</td></tr>
  <tr><td rowspan="2">Outputs</td><td>Advanced &gt; GOP Size</td><td>This value can affect latency because the segment length is a function of the GOP size. </td></tr>
  <tr><td>Advanced &gt; Closed GOP Cadence</td><td>This value can affect latency.</td></tr>
</tbody>
</table>
