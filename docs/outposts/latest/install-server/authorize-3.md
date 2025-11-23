# Configure and test the Outposts server connection to AWS

Use the following procedures to configure and test the connection between your server and
AWS using the Outpost Configuration Tool. You don't need IAM credentials to test the connection. Your
connection must resolve DNS to access the AWS Region.

Before you begin, ensure the following prerequisites:

1. Your laptop is connected to the Outposts server through the USB cable as described in [Connect your laptop](authorize-1.md "authorize-1.md").
2. You created a serial connection to the server as described in [Create a serial connection](authorize-2.md "authorize-2.md").
3. You see the `Outpost` prompt.

###### Tasks

- [Configure static networking](#w2aac17c15c11 "#w2aac17c15c11")
- [Test the links](#w2aac17c15c13 "#w2aac17c15c13")
- [Test for DNS resolution](#w2aac17c15c15 "#w2aac17c15c15")
- [Test for access to the AWS Region](#w2aac17c15c17 "#w2aac17c15c17")

## Configure static networking

###### Note

If you are using Dynamic Host Configuration Protocol (DHCP) for IP address
configuration, skip this step.

Configure your Outposts server's service link and DNS (Domain Name Server) IP addresses statically.

###### To configure static IP and DNS addresses

1. From the `Outpost` prompt, you can run **help** to see the possible commands.
2. Set the static IP using **set-service-link-static-ip**. You will need
   the following arguments to run this command: the IP, subnet mask, and gateway.

Run: **set-service-link-static-ip `ip`
`netmask`
`gateway`**

For example, **set-service-link-static-ip**
``192.168.1.2`
`255.255.255.0`
`192.168.1.1`` sets the static IP to
`192.168.1.2`, the netmask to `255.255.255.0`, and the gateway
to `192.168.1.1`. 3. Set the DNS address using **set-dns**. This command requires one
argument, the DNS address.

Run: **set-dns**
`dns`

For example, **set-dns**
`8.8.8.8` sets the DNS address to
`8.8.8.8`. 4. Optional. To verify that all values are correct, use
**get-service-link-static-ip** and **get-dns** to
display the values set in the previous two steps. 5. Reboot the server for the static IP to take effect.

Run: **reboot** 6. When the server comes back online it should be using the static IP. To
verify:

    1. Create the serial connection to the server as described in [Create a serial connection](authorize-2.md "authorize-2.md"). The
     `Outpost>` prompt appears.
    2. From the `Outpost>` prompt, run
     **describe-ip**.In the information that appears, you should see `mode: static` along with

the statically configured values for IP, netmask, gateway, and DNS.

```
`Outpost>``describe-ip`
`---

links:
-
 name: service_link
 configured: True
 mode: static
 ip: `192.168.1.2`
 netmask: `255.255.255.0`
 gateway: `192.168.1.1`
 dns: [ "`8.8.8.8`" ]
 ntp: [ ]
checksum: `0xDB88E57A`
...`
```

## Test the links

###### To test the links

1. Plug the USB cable into your laptop first and then into the server.
2. Use a serial terminal program, such as PuTTY or **screen**, to
   connect to the server. For more information, see [Create a serial connection to the Outposts server](authorize-2.md "authorize-2.md").
3. Press **Enter** to access the Outpost Configuration Tool command prompt.

```
`Outpost>`
```

###### Note

If you see a persistent red light inside the chassis of the server on the left-hand side after
you power on and you can't connect to Outpost Configuration Tool, you might need to power down and drain the
server to proceed. To drain the server, disconnect all network and power cables,
wait five minutes, then power up and connect to the network again. 4. Use **describe-links** to return information about the network links
on the server. Outposts servers must have one service link and one local network interface
(LNI) link.

```
`Outpost>``describe-links`
`---
service_link_connected: True
local_link_connected: False
links:
-
 name: local_link
 connected: False
 mac: `00:00:00:00:00:00`
-
 name: service_link
 connected: True
 mac: `0A:DC:FE:D7:8E:1F`
checksum: `0x46FDC542``
```

If you get `connected: False` for either link, troubleshoot the network
connection on the hardware. 5. Use **describe-ip** to return the IP assignment status and
configuration of the service link.

```
`Outpost>``describe-ip`
`---
links:
-
 name: service_link
 configured: True
 ip: `192.168.0.0`
 netmask: `255.255.0.0`
 gateway: `192.168.1.1`
 dns: [ "`192.168.1.1`" ]
 ntp: [ ]
checksum: `0x8411B47C``
```

The NTP value might be missing as NTP is optional in a DHCP option set. You should
have no other missing values.

## Test for DNS resolution

###### To test for DNS

1. Plug the USB cable into your laptop first and then into the server.
2. Use a serial terminal program, such as PuTTY or **screen**, to
   connect to the server. For more information, see [Create a serial connection to the Outposts server](authorize-2.md "authorize-2.md").
3. Press **Enter** to access the Outpost Configuration Tool command prompt.

```
`Outpost>`
```

###### Note

If you see a persistent red light inside the chassis of the server on the left-hand side after
you power on and you can't connect to Outpost Configuration Tool, you might need to power down and drain the
server to proceed. To drain the server, disconnect all network and power cables,
wait five minutes, then power up and connect to the network again. 4. Use **export** to enter the parent Region of the Outposts server as the
value for `AWS_DEFAULT_REGION`.

`AWS_DEFAULT_REGION=``Region`

```
`Outpost>``export AWS_DEFAULT_REGION=`us-west-2``

`result: OK
checksum: `0xB2A945RE``
```

    * Do not include a space before or after the equal (=) sign.
    * No environment values are saved. You must export AWS Region each time you run
     Outpost Configuration Tool.
    * If you are using a third party to install the server, you must provide them with
     the parent Region.

5. Use **describe-resolve** to determine if the Outposts server can reach a DNS
   resolver and resolve the IP address of the Outpost configuration endpoint in the Region.
   Requires at least one link with an IP configuration.

```
`Outpost>``describe-resolve`
`---
dns_responding: True
dns_resolving: True
dns: [ "`198.xx.xxx.xx`", "`198.xx.xxx.xx`" ]
query: `outposts.us-west-2.amazonaws.com`
records: [ "`18.xxx.xx.xxx`", "`44.xxx.xxx.xxx`", "44.xxx.xxx.xxx" ]
checksum: `0xB6A961CE``
```

## Test for access to the AWS Region

###### To test access to AWS Regions

1. Plug the USB cable into your laptop first and then into the server.
2. Use a serial terminal program, such as PuTTY or **screen**, to
   connect to the server. For more information, see [Create a serial connection to the Outposts server](authorize-2.md "authorize-2.md").
3. Press **Enter** to access the Outpost Configuration Tool command prompt.

```
`Outpost>`
```

###### Note

If you see a persistent red light inside the chassis of the server on the left-hand side after
you power on and you can't connect to Outpost Configuration Tool, you might need to power down and drain the
server to proceed. To drain the server, disconnect all network and power cables,
wait five minutes, then power up and connect to the network again. 4. Use **export** to enter the parent Region of the Outposts server as the
value for `AWS_DEFAULT_REGION`.

`AWS_DEFAULT_REGION=``Region`

```
`Outpost>``export AWS_DEFAULT_REGION=`us-west-2``

`result: OK
checksum: `0xB2A945RE``
```

    * Do not include a space before or after the equal (=) sign.
    * No environment values are saved. You must export AWS Region each time you run
     Outpost Configuration Tool.
    * If you are using a third party to install the server, you must provide the them
     with the parent Region.

5. Use **describe-reachability** to determine if the Outposts server can reach
   the Outpost configuration endpoint in the Region. Requires a working DNS configuration,
   which you can determine by using **describe-resolve**.

```
`Outpost>``describe-reachability``---
is_reachable: True
src_ip: `10.0.0.0`
dst_ip: `54.xx.x.xx`
dst_port: `xxx`
checksum: `0xCB506615``
```

    * `is_reachable` indicates the outcome of the test
    * `src_ip` is the IP address of the server
    * `dst_ip` is the IP address of the Outpost configuration endpoint in
     the Region
    * `dst_port` is the port the server used to connect to
     `dst_ip`
