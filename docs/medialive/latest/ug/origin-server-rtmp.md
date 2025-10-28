# Coordinate with the downstream system

You and the operator of the downstream system must agree about the destination for
each
output of the RTMP output group.

An RTMP output group requires one set of destination addresses for each output.

1.  If the RTMP server is a social media site, the host of the site might have
    instructions that can supplement the following information. Obtain these
    instructions.
2.  Decide if you need two destinations for the output:
    - If the MediaLive channel is a [standard
      channel](plan-redundancy.md "plan-redundancy.md"), you need two destinations.
    - If the MediaLive channel is a single-pipeline channel, you need one
      destination.

3.  Make sure that the RTMP operator sets up to expect MediaLive output at one or
    two inputs on the RTMP server, as appropriate.
4.  Obtain the following information from the RTMP operator:

        * The protocol for MediaLive to use—RTMP or RTMPS.
        * The user name and password to access the downstream system, if the
         downstream system requires authenticated requests. Note that these user
         credentials relate to user authentication, not to the protocol. User
         authentication is about whether the downstream system will accept your
         request. The protocol is about whether the request is sent over a secure
         connection.
        * IP address.
        * Port number.
        * Application name. Also called *app
         name*.
        * Stream name. Also called *application
         instance* or *app
         instance* or *stream
         key*.


        The operator might give you the application name and stream name as
         separate pieces of data. Or they might give you a complete path in the
         format `string/string`. In this case, the first
         string is the application name and the second string is the stream
         name.

    Here is an example of the information that the operator will give you:

`rtmp://203.0.113.28:80/xyz/ywq7b`

`rtmp://203.0.113.17:80/xyz/ywq7b`

Where `xyz` is the application name, and `ywq7b` is the
stream name.

In this example, the two URLs have different IP addresses but the same
application name/stream name portion. Your RTMP server might follow a different
rule.
