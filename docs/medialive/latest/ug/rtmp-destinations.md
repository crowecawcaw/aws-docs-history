

# Fields for the output destination
<a name="rtmp-destinations"></a>

The following fields configure the location and names of the RTMP output files (the destination).
+ **Output** – **RTMP destination** sections

**To specify the destination for the output**

1. When you [discussed your requirements](origin-server-rtmp.md) with the operator of the RTMP server, you should have obtained the following information:
   + The protocol for MediaLive to use—RTMP or RTMPS.
   + IP address.
   + Port number.
   + Application name. Also called *app name*.
   + Stream name. Also called *application instance* or *app instance* or *stream key*.

     The operator might give you the application name and stream name as separate pieces of data. Or they might give you a complete path in the format **string/string**. In this case, the first string is the application name and the second string is the stream name.
   + The user name and password to access the server, if the downstream system requires authenticated requests. 

   Here is an example of the information that the operator will give you:

   `rtmp://203.0.113.17:80/xyz/ywq7b`

   Where `xyz` is the application name, and `ywq7b` is the stream name.

1. Enter the different portions of the destination in the appropriate fields. 


<table>
<thead>
  <tr><th>Portion of the destination URL</th><th>Field</th></tr>
</thead>
<tbody>
  <tr><td>protocol, IP address, port, application name</td><td>The two <b>URL</b> fields in the <b>RTMP destination</b> section. (Note that these fields are on the <b>Output</b> page, not the <b>Output group</b> page.)For example:<b>rtmp://203.0.113.17:80/xyz</b><br />Specify two destinations when the channel is set up as a <a href="channel-class.md">Channel class</a>, or one destination when it is set up as a single-pipeline channel.</td></tr>
  <tr><td>Stream name</td><td>The two <b>Stream name</b> fields in the <b>RTMP outputs </b> section.For example:<b>ywq7b</b></td></tr>
</tbody>
</table>


1. Complete the **Credentials** section, if the server the downstream system provided you with a user name and password. For the password, enter the name of the password stored on the AWS Systems Manager Parameter Store. Don't enter the password itself. For more information, see [Requirements for AWS Systems Manager password parameters](requirements-for-EC2.md). 