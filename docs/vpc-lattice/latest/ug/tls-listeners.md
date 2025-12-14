# TLS listeners for VPC Lattice services

A listener is a process that checks for connection requests. You can define a listener
when you create your VPC Lattice service. You can add listeners to your service at any time.

You can create a TLS listener so that VPC Lattice passes encrypted traffic through
to your applications without decrypting it.

If you prefer that VPC Lattice decrypts encrypted traffic and sends unencrypted
traffic to your applications, create an HTTPS listener instead. For more information,
see [HTTPS listeners](https-listeners.md "https-listeners.md").

## Considerations

The following considerations apply to TLS listeners:

- The VPC Lattice service must have a custom domain name. The service custom
  domain name is used as a Service Name Indication (SNI) match. If you
  specified a certificate when you created the service, it is not used.
- The only rule allowed for a TLS listener is the default rule.
- The default action for a TLS listener must be a forward action to a TCP
  target group.
- By default, health checks are disabled for TCP target groups. If you
  enable health checks for a TCP target group, you must specify a protocol
  and protocol version.
- TLS listeners route requests using the SNI field of the client-hello
  message. You can use wildcard and SAN certificates on your targets if the
  matching condition is an exact match to the client-hello.
- Because all traffic remains encrypted from the client to the target,
  VPC Lattice can't read the HTTP headers and can't insert or remove HTTP headers.
  Therefore, with a TLS listener, the following limitations exist:
  - Connection duration is limited to 10 minutes
  - Auth policies are limited to anonymous principals
  - Lambda targets are not supported

- Websocket connections can use TLS Listeners to connect to ,
  VPC Lattice services. The following limitations exist:
  - Connection duration is limited to 10 minutes
  - Auth policies are limited to anonymous principals
  - Lambda targets are not supported

- Encrypted Client Hello (ECH) isn't supported.
- Encrypted Server Name Indication (ESNI) isn't supported.

## Add a TLS listener

You configure a listener with a protocol and a port for connections from clients
to the service, and a target group for the default listener rule. For more
information, see [Listener configuration](listeners.md#listener-configuration "listeners.md#listener-configuration").

###### To add a TLS listener using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Services**.
3. Select the name of the service to open its details page.
4. On the **Routing** tab, choose **Add listener**.
5. For **Listener name**, you can either provide a custom
   listener name or use the protocol and port of your listener as the listener
   name. A custom name that you specify can have up to 63 characters, and it
   must be unique for every service in your account. The valid characters are
   a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last
   character, or immediately after another hyphen. You cannot change the name
   of a listener after you create it.
6. For **Protocol**, choose **TLS**.
   For **Port**, enter a port number.
7. For **Forward to target group**, choose a VPC Lattice target
   group that uses the TCP protocol to receive the traffic, and choose the
   weight to assign to this target group. You can optionally add another target
   group. Choose **Add target group** and then choose a target
   group and enter its weight.
8. (Optional) To add tags, expand **Listener tags**, choose
   Add new tag, and enter a tag key and tag value.
9. Review your configuration, and then choose **Add**.

###### To add a TLS listener using the AWS CLI

Use the [create-listener](../../../cli/latest/reference/vpc-lattice/create-listener.md "../../../cli/latest/reference/vpc-lattice/create-listener.md")
command to create a listener with a default rule. Specify the TLS_PASSTHROUGH protocol.
