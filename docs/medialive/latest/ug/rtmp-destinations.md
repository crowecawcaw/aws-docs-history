# Fields for the output

destination

The following fields configure the location and names of
the RTMP output files (the destination).

- **Output** – **RTMP
  destination** sections

###### To specify the destination for the output

1.  When you [discussed your requirements](origin-server-rtmp.md "origin-server-rtmp.md") with the
    operator of the RTMP server, you should have
    obtained the following information:

        * The protocol for MediaLive to use—RTMP
         or RTMPS.
        * IP address.
        * Port number.
        * Application name. Also called *app
         name*.
        * Stream name. Also called *application
         instance* or *app instance* or
         *stream
         key*.


        The operator might give you the
         application name and stream name as separate
         pieces of data. Or they might give you a
         complete path in the format
         `string/string`. In
         this case, the first string is the
         application name and the second string is
         the stream name.
        * The user name and password to access the
         server, if the downstream system requires
         authenticated requests.

    Here is an example of the information that the
    operator will give you:

`rtmp://203.0.113.17:80/xyz/ywq7b`

Where `xyz` is the application name,
and `ywq7b` is the stream name. 2. Enter the different portions of the destination in
the appropriate fields.

| Portion of the destination<br>URL               | Field                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| protocol, IP address, port,<br>application name | The two **URL**<br>fields in the **RTMP<br>destination\*<br>• section. (Note<br>that these fields are on the<br>**Output\*<br>• page, not<br>the **Output group**<br>page.)For<br>example:`rtmp://203.0.113.17:80/xyz`Specify<br>two destinations when the channel is set<br>up as a [Channel class](channel-class.md "channel-class.md"),<br>or one destination when it is set up as<br>a single-pipeline<br>channel. |
| Stream name                                     | The two **Stream<br>name\*<br>• fields in the<br>**RTMP outputs\*\*<br>section.For<br>example:`ywq7b`                                                                                                                                                                                                                                                                                                                  |

3. Complete the **Credentials**
   section, if the server the downstream system
   provided you with a user name and password. For the
   password, enter the name of the password stored on
   the AWS Systems Manager Parameter Store. Don't enter the
   password itself. For more information, see [Requirements for AWS Systems Manager password parameters](requirements-for-EC2.md "requirements-for-EC2.md").
