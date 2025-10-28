# IPv6 support for Transfer Family servers

AWS Transfer Family supports dual-stack (IPv4 and IPv6) endpoints for the following resources:

- SFTP public endpoints
- VPC internal endpoints for all protocols (SFTP/FTPS/FTP and AS2)
- Public endpoints for AS2-enabled Transfer Family servers, by using the steps provided in
  [Using an Application Load Balancer for dual-stack AS2
  server connectivity](#ipv6-alb-as2 "#ipv6-alb-as2")
- API endpoints
  With dual-stack support, your Transfer Family endpoints can communicate with both IPv4 and IPv6
  enabled clients. This enables you to gradually transition from IPv4 to IPv6 based systems
  without needing to switch all at once, meet IPv6 compliance requirements, and remove the
  need for expensive networking equipment to handle address translation between IPv4 and IPv6.
  For details, see [DNS and Endpoints](../APIReference/Welcome.md#dns-endpoints "../APIReference/Welcome.md#dns-endpoints")
  in the _AWS Transfer Family API Reference_. For a complete list of
  available endpoints, see [AWS Transfer Family endpoints and quotas](../../../general/latest/gr/transfer-service.md "../../../general/latest/gr/transfer-service.md") in
  the _AWS General Reference_.

## IPv6 limitations

The following Transfer Family resources do not currently support IPv6:

- VPC-Internet endpoints
- Web apps
- VPC_ENDPOINT endpoint type (deprecated)

The FTPS protocol supports the PASV and EPSV commands for requesting an open data port
for file listing, getting, and putting operations. However, PASV doesn't work with IPv6
because it requires an IPv4-specific response. EPSV continues to work because it returns
only port information.

To use FTPS, we recommend one of the following:

- Configure your FTPS client to use EPSV
- Use IPv4 instead of IPv6

SFTP supports both IPv4 and IPv6. We recommend using SFTP instead of FTPS when working
with dual-stack endpoints.

## Configuring IPv6 for servers

When creating a new server or updating an existing server, you can choose the IP
address type:

- **IPv4** (default): For backwards compatibility, the server
  will only accept IPv4 connections.
- **Dual-stack**: The server will accept both IPv4 and IPv6
  connections.

To update an existing server's IP address type:

1. Stop the server.
2. Edit the endpoint details.
3. Change the IP address type to **Dual-stack**.
4. Start the server.

###### Note

For VPC-Internet endpoints, dual-stack mode is not currently supported.

## Using an Application Load Balancer for dual-stack AS2

server connectivity

You can enable dual-stack (IPv4 and IPv6) connectivity to your AS2 server by using an
Application Load Balancer that has a public-facing endpoint. This allows trading
partners to connect to your AS2 server using either IPv4 or IPv6.

To set up a dual-stack Application Load Balancer for your AS2 server

1. Create a VPC with the following settings:
   - VPC only
   - Manual IPv4 CIDR input
   - Amazon-provided IPv6 CIDR block

2. Create at least two subnets in different Availability Zones:
   - Add IPv6 CIDRs to the subnets
   - When creating subnets, allocate only a subset of the VPC's IPv4/IPv6
     addresses to leave addresses available for additional subnets

3. Create an internet gateway for the VPC.
4. Edit the route table and add two routes:
   - One route with _Destination_
     `0.0.0.0/0`
   - One route with _Destination_
     `::/0`
   - Set both route targets to the internet gateway you created

5. Create an AS2-enabled server in the VPC that you created in step 1. Make sure
   to specify the `IpAddressType` as `DUALSTACK`.

For details on how to create a Transfer Family server that uses the AS2 protocol, see
[Create an AS2 server](create-as2-transfer-server.md "create-as2-transfer-server.md"). 6. Create a target group:

    * For *Specify group details*, configure:




    	+ Target type: IP addresses
    	+ Name: Enter a name
    	+ Protocol: HTTP
    	+ Port: 5080
    	+ VPC: Select the VPC you created
    	+ Protocol version: HTTP1
    	+ Health checks: Use defaults
    * For *Register targets*:




    	+ Enter your AS2 server's private IPv4 address
    	+ Choose *Include as pending below*

7. Create an Application Load Balancer:
   - Enter a name
   - For _Scheme_, choose
     _Internet-facing_
   - For _IP address type_, choose
     _Dualstack_
   - For _Network mapping_:
     - Select the VPC you created
     - Select the Availability Zones where you created subnets

   - For _Security groups_, select a security group that
     allows inbound IPv4 and IPv6 traffic from any IP address on port
     80
   - For _Listeners and routing_:
     - Protocol: HTTP
     - Port: 80
     - Default action: Forward to the target group you created

   - Choose _Create load balancer_

After you create the Application Load Balancer, trading partners can use its DNS name
to send traffic to your AS2 server. This configuration enables your AS2 server to accept
connections from both IPv4 and IPv6 clients through the dual-stack Application Load
Balancer.
