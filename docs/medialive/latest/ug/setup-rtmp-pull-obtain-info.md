# Obtain information

Obtain the following information from your contact person at the upstream
system:

- The application name and application instance for the source content. (The
  application instance is also known as the _stream_ or
  _stream key_.) There are two sources for a
  standard-class input , or one source for a single-class input. For
  information about input classes and their uses, see [Choosing the channel class and input
  class](class-channel-input.md "class-channel-input.md"). For information about input classes and
  their uses, see [Choosing the channel class and input
  class](class-channel-input.md "class-channel-input.md").

The operator of the upstream system might already have rules for assigning
these names. If not, you might have names that you would like to use. Make
sure that you and the operator of the upstream system are clear about these
names.

In this example, the application name and instance name are identical. But
they could be different:

Application name: `live`, and instance name
`curling`

Application name: `live`, and instance name
`curling`

- The public IP addresses that MediaLive will pull the source content
  from.

These addresses must include port 1935. For example:

`rtmp://203.0.113.13:1935`

`rtmp://198.51.100.54:1935`

- The user name and password to access the upstream system, if the upstream
  system requires authenticated requests. Note that these user credentials
  relate to user authentication, not to the protocol. User authentication is
  about whether the upstream system will accept your request. The protocol is
  about whether the request is sent over a secure connection.
