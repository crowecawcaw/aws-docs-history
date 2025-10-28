End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# PathfindingSample console

client fails to connect

You might get the following error from the console client when you connect to the
`PathfindingSample` simulation described in the tutorials in [Getting started with SimSpace Weaver](getting-started.md "getting-started.md"). This error occurs
because the client can't open a network connection to the `ViewApp` at the
combined IP address and port number that you provided.

```
Fatal error in function nng_dial. Error code: 268435577. Error message: no link
```

###### For a simulation in the AWS Cloud

- **Is your network connection working correctly?**
  Verify that you can connect to other IP addresses or web sites that should work.
  Make sure that your web browser isn't loading a web site from its cache.
- **Is your simulation running?** You can use the
  **ListSimulations** API to get the status of
  your simulation. For more information, see [Get the IP address and port number of a custom app](working-with_get-ip.md "working-with_get-ip.md"). You can also use the
  [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver") to check the status of your simulations.
- **Are your apps running?** You can use the
  **DescribeApp** API to get the status of your
  apps. For more information, see [Get the IP address and port number of a custom app](working-with_get-ip.md "working-with_get-ip.md"). You can also use the
  [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver") to check the status of your simulations.
- **Are your apps running?** You can use the
  **DescribeApp** API to get the status of your
  apps. For more information, see [Get the IP address and port number of a custom app](working-with_get-ip.md "working-with_get-ip.md"). You can also use the
  [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver") to check the status of your simulations.
- **Did you use the correct IP address and port
  number?** When you connect over the internet, you must use the IP
  address and `Actual` port number of the `ViewApp`. You can
  find the IP `Address` and `Actual` port number in the
  `EndpointInfo` block of the **DescribeApp** API output. You can also use the
  [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver") to find the IP address (**URI**) and
  port number (**Ingress port**) for your `ViewApp` in
  the `MyViewDomain` detail page.
- **Is your network connection going through a
  firewall?** Your firewall might block your connection to the IP
  address or port number (or both). Check your firewall settings or check with
  your firewall administrator.

###### For a local simulation

- **Can you connect to your loopback address
  (127.0.0.1)?** If you have the `ping` command line tool
  in Windows, you can open a command prompt window and try to ping 127.0.0.1.
  Press **Ctrl**-**C** to end the ping.

```
ping 127.0.0.1
```

###### Example ping output

```
C:\>ping 127.0.0.1

Pinging 127.0.0.1 with 32 bytes of data:
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
Reply from 127.0.0.1: bytes=32 time=1ms TTL=128

Ping statistics for 127.0.0.1:
    Packets: Sent = 3, Received = 3, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 1ms, Average = 0ms
Control-C
^C
C:\>

```

If the ping says it lost packets, you might have other software (such as a
local firewall, security settings, or anti-malware programs) that is blocking
your connection.

- **Are your apps running?** Your local simulation
  runs as separate windows for each app. Make sure the windows for your spatial
  apps and `ViewApp` are open. For more information, see [Local development in SimSpace Weaver](working-with_local-development.md "working-with_local-development.md").
- **Did you use the correct IP address and port
  number?** You must use `tcp://127.0.0.1:7000` when you
  connect to a local simulation. For more information, see [Local development in SimSpace Weaver](working-with_local-development.md "working-with_local-development.md").
- **Do you have local security software that could block
  your connection?** Check your security settings, local firewall, or
  anti-malware programs to see if they are blocking your connection to
  `127.0.0.1` on TCP port `7000`.
