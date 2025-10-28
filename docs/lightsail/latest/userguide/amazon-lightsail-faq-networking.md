# Networking

## How do I use IP addresses in Lightsail?

Each Lightsail instance automatically gets a private IPv4 address, a public IPv4
address, or a public IPv6 address (IPv6 must be manually enabled for instances created
before January 12, 2021). You can use the private IP to transmit data between Lightsail
instances and AWS resources privately, for free. You can use the public IP to connect to
your instance from the Internet, such as through a registered domain name or through an SSH
or RDP connection from your local computer. You can also attach a static IPv4 address to the
instance, which substitutes the public IPv4 address with an IPv4 address that doesn't change
even if the instance is stopped and started. IPv6 addresses assigned to the instance remain
unchanged until the instance is deleted or the IPv6 address is manually released by
disabling IPv6 on the instance.

## Does Lightsail support

IPv6-only instances?

Yes, Lightsail instances support dual-stack (IPv4 and IPv6) and IPv6-only
configurations.

## What is a static IP?

A [static IP](understanding-static-ip-addresses-in-amazon-lightsail.md "understanding-static-ip-addresses-in-amazon-lightsail.md") is a fixed, public IP address that is dedicated to your Lightsail
account. You can assign a static IPv4 address to an instance, replacing its public IPv4. If
you decide to replace your instance with another one, you can reassign the static IP to the
new instance. In this way, you don't have to reconfigure any external systems (like DNS
records) to point to a new IP address every time you want to replace your instance.
Lightsail currently supports static IPs for IPv4 only. Static IPv6 addresses are not
available. However, IPv6 addresses assigned to the instance remain unchanged until the
instance is deleted or the IPv6 address is manually released by disabling IPv6 on the
instance.

## How many static IPs can I attach to an

instance?

You can attach only one static IP to an instance at a time.

## What are DNS records?

DNS is a globally distributed service that translates human readable names like
`www.example.com` into alphanumeric IP addresses, like `192.0.2.1`
that computers use to connect to each other. With Lightsail, you can easily map your
registered domain names such as `photos.example.com` to the public IPs of your
Lightsail instances. In this way, when users type human readable names like
`example.com` into their browsers, Lightsail automatically translates the
address into the IP of the instance you want to direct your users to. Each of these
translations is referred to as a DNS query.

It's important to know that to use a domain in Lightsail, you must first register it.
You can register domains by using [Lightsail](amazon-lightsail-domain-registration.md "amazon-lightsail-domain-registration.md"), or your preferred DNS registrar.

## Can I manage firewall settings for my

instance?

Yes. You can control the data traffic for your instances by using the Lightsail
firewall. From the Lightsail console, you can set rules about which ports of your instance
are publicly accessible for different types of traffic.
