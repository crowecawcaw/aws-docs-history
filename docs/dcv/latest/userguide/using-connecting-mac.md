# Connecting to a Amazon DCV session using the macOS

client

###### To connect to a session using the macOS client

1. Launch the macOS client.

If you get an error stating that the application can't be opened because it's from an
unidentified developer, see the [Safely open apps on your Mac](https://support.apple.com/en-ie/HT202491 "https://support.apple.com/en-ie/HT202491") webpage. 2. Choose **Connections Settings**, configure your proxy settings as follows, and then choose
**Apply**.

    * To avoid connecting through a proxy, choose **Connect directly**.
    * To connect to the Amazon DCV server using your preconfigured operating system proxy settings, choose
     **Use system proxy**.
    * To connect to the Amazon DCV server through a specific HTTP proxy server, choose **Get through
     web proxy (HTTP)**. Specify the IP address or hostname of the proxy
     server as well as the communication port. If the HTTP proxy server requires
     authentication, select the **Proxy server requiring password**
     check box and enter your sign-in credentials.
    * To connect to the Amazon DCV server through a specific HTTPS proxy server, choose **Get through
     web proxy (HTTPS)**. Specify the IP address or hostname of the proxy
     server as well as the communication port. If the web proxy server requires
     authentication, select the **Proxy server requiring password**
     check box and enter your sign-in credentials.
    * To select the transport protocol to use for data transport, choose the
     **Protocol** tab. By default, the client uses the QUIC protocol
     (based on UDP) for data transport if it's available. If it isn't available, the
     client uses the WebSocket protocol (based on TCP). This option is always
     available.


    QUIC is available only if the following conditions are met. First, the Amazon DCV server is
     configured to support it. Second, your network configuration supports UDP
     communication between the Amazon DCV client and the Amazon DCV server. Additionally, it's only
     supported for direct client-server communication where there are no intermediate
     proxies, gateways, or load balancers.


    You can force the client to use a data transport protocol by explicitly selecting it.
     To verify which protocol is in use, check the Streaming Modes dialog. Additionally, if the
     QUIC protocol is in use, "QUIC" appears in the titlebar.


    For more information, see [Enable the QUIC UDP transport protocol](../adminguide/enable-quic.md "../adminguide/enable-quic.md") in the *Amazon DCV Administrator
     Guide*.

3. Specify the session details in the following format:

```
`server_hostname_or_IP`:`port`#`session_id`
```

In the following example, the command connects to a session that's named
`my-session`. This session is hosted on a Amazon DCV server with the host name
`my-dcv-server.com`. It's connected over port `8443`.

```
my-dcv-server.com:8443#my-session
```

4. Choose **Connect**.
5. Enter your sign-in credentials and choose **Login**.

###### Note

By default, the connection is terminated after three unsuccessful login attempts. To try
again, restart the connection. 6. If you're prompted to verify the server's certificate, confirm the certificate's fingerprint
with your Amazon DCV administrator. If the fingerprint is valid, choose
**Trust & Connect**.
