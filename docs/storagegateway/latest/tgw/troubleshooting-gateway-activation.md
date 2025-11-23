# Troubleshooting: internal error during

gateway activation

Storage Gateway activation requests traverse two network paths. Incoming activation requests sent
by a client connect to the gateway's virtual machine (VM) or Amazon Elastic Compute Cloud (Amazon EC2) instance over
port 80. If the gateway successfully receives the activation request, then the gateway
communicates with the Storage Gateway endpoints to receive an activation key. If the gateway can't
reach the Storage Gateway endpoints, then the gateway responds to the client with an internal error
message.

Use the following troubleshooting information to determine what to do if you receive an
internal error message when attempting to activate your AWS Storage Gateway.

###### Note

- Make sure you deploy new gateways using the latest virtual machine image file
  or Amazon Machine Image (AMI) version. You will receive an internal error if you
  attempt to activate a gateway that uses an outdated AMI.
- Make sure that you select the correct gateway type that you intend to deploy
  before you download the AMI. The .ova files and AMIs for each gateway type are
  different, and they are not interchangeable.

## Resolve errors when activating your gateway using a public endpoint

To resolve activation errors when activating your gateway using a public endpoint,
perform the following checks and configurations.

### Check the required ports

For gateways deployed on-premises, check that the ports are open on your local
firewall. For gateways deployed on an Amazon EC2 instance, check that the ports are open
on the instance's security group. To confirm that the ports are open, run a telnet
command on the public endpoint from a server. This server must be in the same subnet
as the gateway. For example, the following telnet commands test the connection to
port 443:

```
telnet d4kdq0yaxexbo.cloudfront.net 443
telnet storagegateway.region.amazonaws.com 443
telnet dp-1.storagegateway.region.amazonaws.com 443
telnet proxy-app.storagegateway.region.amazonaws.com 443
telnet client-cp.storagegateway.region.amazonaws.com 443
telnet anon-cp.storagegateway.region.amazonaws.com 443
```

To confirm that the gateway itself can reach the endpoint, access the gateway's
local VM console (for gateways deployed on-premises). Or, you can SSH to the
gateway's instance (for gateways deployed on Amazon EC2). Then, run a network
connectivity test. Confirm that the test returns `[PASSED]`. For more
information, see [Testing Your Gateway Connection to the Internet](manage-on-premises-common.md#MaintenanceTestGatewayConnectivity-common "manage-on-premises-common.md#MaintenanceTestGatewayConnectivity-common").

###### Note

The default login user name for the gateway console is `admin`, and
the default password is `password`.

### Make sure firewall security does not modify packets sent from the gateway to

the public endpoints

SSL inspections, deep packet inspections, or other forms of firewall security can
interfere with packets sent from the gateway. The SSL handshake fails if the SSL
certificate is modified from what the activation endpoint expects. To confirm that
there's no SSL inspection in progress, run an OpenSSL command on the main activation
endpoint ( `anon-cp.storagegateway.region.amazonaws.com`) on port 443.
You must run this command from a machine that's in the same subnet as the
gateway:

```
$ openssl s_client -connect  anon-cp.storagegateway.`region`.amazonaws.com:443 -servername anon-cp.storagegateway.region.amazonaws.com
```

###### Note

Replace `region` with your AWS Region.

If there's no SSL inspection in progress, then the command returns a response
similar to the following:

```
$ openssl s_client -connect anon-cp.storagegateway.us-east-2.amazonaws.com:443 -servername anon-cp.storagegateway.us-east-2.amazonaws.com
CONNECTED(00000003)
depth=2 C = US, O = Amazon, CN = Amazon Root CA 1
verify return:1
depth=1 C = US, O = Amazon, OU = Server CA 1B, CN = Amazon
verify return:1
depth=0 CN = anon-cp.storagegateway.us-east-2.amazonaws.com
verify return:1
---
Certificate chain
 0 s:/CN=anon-cp.storagegateway.us-east-2.amazonaws.com
   i:/C=US/O=Amazon/OU=Server CA 1B/CN=Amazon
 1 s:/C=US/O=Amazon/OU=Server CA 1B/CN=Amazon
   i:/C=US/O=Amazon/CN=Amazon Root CA 1
 2 s:/C=US/O=Amazon/CN=Amazon Root CA 1
   i:/C=US/ST=Arizona/L=Scottsdale/O=Starfield Technologies, Inc./CN=Starfield Services Root Certificate Authority - G2
 3 s:/C=US/ST=Arizona/L=Scottsdale/O=Starfield Technologies, Inc./CN=Starfield Services Root Certificate Authority - G2
   i:/C=US/O=Starfield Technologies, Inc./OU=Starfield Class 2 Certification Authority
---
```

If there is an ongoing SSL inspection, then the response shows an altered
certificate chain, similar to the following:

```
$ openssl s_client -connect  anon-cp.storagegateway.ap-southeast-1.amazonaws.com:443 -servername anon-cp.storagegateway.ap-southeast-1.amazonaws.com
CONNECTED(00000003)
depth=0 DC = com, DC = amazonaws, OU = AWS, CN = anon-cp.storagegateway.ap-southeast-1.amazonaws.com
`verify error:num=20:unable to get local issuer certificate`
verify return:1
depth=0 DC = com, DC = amazonaws, OU = AWS, CN = anon-cp.storagegateway.ap-southeast-1.amazonaws.com
`verify error:num=21:unable to verify the first certificate`
verify return:1
---
Certificate chain
 0 s:/DC=com/DC=amazonaws/OU=AWS/CN=anon-cp.storagegateway.ap-southeast-1.amazonaws.com
   i:/C=IN/O=Company/CN=Admin/ST=KA/L=New town/OU=SGW/emailAddress=admin@company.com
---
```

The activation endpoint accepts SSL handshakes only if it recognizes the SSL
certificate. This means that the gateway's outbound traffic to the endpoints must be
exempt from inspections performed by firewalls in your network. These inspections
might be an SSL inspection or a deep packet inspection.

### Check gateway time synchronization

Excessive time skews can cause SSL handshake errors. For on-premises gateways, you
can use the gateway's local VM console to check your gateway's time synchronization.
The time skew should be no larger than 60 seconds. For more information, see [Synchronizing
Your Gateway VM Time](MaintenanceTimeSync-hyperv.md "MaintenanceTimeSync-hyperv.md").

The **System Time Management** option isn't available on gateways
that are hosted on Amazon EC2 instances. To make sure Amazon EC2 gateways can properly
synchronize time, confirm that the Amazon EC2 instance can connect to the following NTP
server pool list over ports UDP and TCP 123:

- 0.amazon.pool.ntp.org
- 1.amazon.pool.ntp.org
- 2.amazon.pool.ntp.org
- 3.amazon.pool.ntp.org

## Resolve errors when activating your gateway using an Amazon VPC endpoint

To resolve activation errors when activating your gateway using an Amazon Virtual Private Cloud (Amazon VPC)
endpoint, perform the following checks and configurations.

### Check the required ports

Make sure the required ports within your local firewall (for gateways deployed
on-premises) or security group (for gateways deployed in Amazon EC2) are open. The ports
required for connecting a gateway to a Storage Gateway VPC endpoint differ from those
required when connecting a gateway to public endpoints. The following ports are
required for connecting to a Storage Gateway VPC endpoint:

- TCP 443
- TCP 1026
- TCP 1027
- TCP 1028
- TCP 1031
- TCP 2222

For more information, see [Creating a VPC endpoint for Storage Gateway](gateway-private-link.md#create-vpc-endpoint "gateway-private-link.md#create-vpc-endpoint").

Additionally, check the security group that's attached to your Storage Gateway VPC
endpoint. The default security group attached to the endpoint might not allow the
required ports. Create a new security group that allows traffic from your gateway's
IP address range over the required ports. Then, attach that security group to the
VPC endpoint.

###### Note

Use the [Amazon VPC console](https://console.aws.amazon.com//vpc/ "https://console.aws.amazon.com//vpc/") to verify the
security group that's attached to the VPC endpoint. View your Storage Gateway VPC
endpoint from the console, and then choose the **Security
Groups** tab.

To confirm that the required ports are open, you can run telnet commands on the
Storage Gateway VPC Endpoint. You must run these commands from a server that's in the same
subnet as the gateway. You can run the tests on the first DNS name that doesn't
specify an Availability Zone. For example, the following telnet commands test the
required port connections using the DNS name
vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com:

```
telnet vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com 443
telnet vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com 1026
telnet vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com 1027
telnet vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com 1028
telnet vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com 1031
telnet vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com 2222
```

### Make sure firewall security does not modify packets sent from the gateway to

your Storage Gateway Amazon VPC endpoint

SSL inspections, deep packet inspections, or other forms of firewall security can
interfere with packets sent from the gateway. The SSL handshake fails if the SSL
certificate is modified from what the activation endpoint expects. To confirm that
there's no SSL inspection in progress, run an OpenSSL command on your Storage Gateway VPC
endpoint. You must run this command from a machine that's in the same subnet as the
gateway. Run the command for each required port:

```
$ openssl s_client -connect vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com:443 -servername vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com

$ openssl s_client -connect vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com:1026 -servername vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com

$ openssl s_client -connect vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com:1027 -servername vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com

$ openssl s_client -connect vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com:1028 -servername vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com

$ openssl s_client -connect vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com:1031 -servername vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com

$ openssl s_client -connect vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com:2222 -servername vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com
```

If there's no SSL inspection in progress, then the command returns a response
similar to the following:

```
openssl s_client -connect vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com:1027 -servername vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com
CONNECTED(00000005)
depth=2 C = US, O = Amazon, CN = Amazon Root CA 1
verify return:1
depth=1 C = US, O = Amazon, OU = Server CA 1B, CN = Amazon
verify return:1
depth=0 CN = anon-cp.storagegateway.us-east-1.amazonaws.com
verify return:1
---
Certificate chain
 0 s:CN = anon-cp.storagegateway.us-east-1.amazonaws.com
   i:C = US, O = Amazon, OU = Server CA 1B, CN = Amazon
 1 s:C = US, O = Amazon, OU = Server CA 1B, CN = Amazon
   i:C = US, O = Amazon, CN = Amazon Root CA 1
 2 s:C = US, O = Amazon, CN = Amazon Root CA 1
   i:C = US, ST = Arizona, L = Scottsdale, O = "Starfield Technologies, Inc.", CN = Starfield Services Root Certificate Authority - G2
 3 s:C = US, ST = Arizona, L = Scottsdale, O = "Starfield Technologies, Inc.", CN = Starfield Services Root Certificate Authority - G2
   i:C = US, O = "Starfield Technologies, Inc.", OU = Starfield Class 2 Certification Authority
---
```

If there is an ongoing SSL inspection, then the response shows an altered
certificate chain, similar to the following:

```
openssl s_client -connect vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com:1027 -servername vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com
CONNECTED(00000005)
depth=2 C = US, O = Amazon, CN = Amazon Root CA 1
verify return:1
depth=1 C = US, O = Amazon, OU = Server CA 1B, CN = Amazon
verify return:1
depth=0 DC = com, DC = amazonaws, OU = AWS, CN = anon-cp.storagegateway.us-east-1.amazonaws.com
`verify error:num=21:unable to verify the first certificate`
verify return:1
---
Certificate chain
 0 s:/DC=com/DC=amazonaws/OU=AWS/CN=anon-cp.storagegateway.us-east-1.amazonaws.com
   i:/C=IN/O=Company/CN=Admin/ST=KA/L=New town/OU=SGW/emailAddress=admin@company.com
---
```

The activation endpoint accepts SSL handshakes only if it recognizes the SSL
certificate. This means that the gateway's outbound traffic to your VPC endpoint
over required ports is exempt from inspections performed by your network firewalls.
These inspections might be SSL inspections or deep packet inspections.

### Check gateway time synchronization

Excessive time skews can cause SSL handshake errors. For on-premises gateways, you
can use the gateway's local VM console to check your gateway's time synchronization.
The time skew should be no larger than 60 seconds. For more information, see [Synchronizing
Your Gateway VM Time](MaintenanceTimeSync-hyperv.md "MaintenanceTimeSync-hyperv.md").

The **System Time Management** option isn't available on gateways
that are hosted on Amazon EC2 instances. To make sure Amazon EC2 gateways can properly
synchronize time, confirm that the Amazon EC2 instance can connect to the following NTP
server pool list over ports UDP and TCP 123:

- 0.amazon.pool.ntp.org
- 1.amazon.pool.ntp.org
- 2.amazon.pool.ntp.org
- 3.amazon.pool.ntp.org

### Check for an HTTP proxy and confirm associated security group

settings

Before activation, check if you have an HTTP proxy on Amazon EC2 configured on the
on-premises gateway VM as a Squid proxy on port 3128. In this case, confirm the
following:

- The security group attached to the HTTP proxy on Amazon EC2 must have an
  inbound rule. This inbound rule must allow Squid proxy traffic on port 3128
  from the gateway VM's IP address.
- The security group attached to the Amazon EC2 VPC endpoint must have inbound
  rules. These inbound rules must allow traffic on ports 1026-1028, 1031,
  2222, and 443 from the IP address of the HTTP proxy on Amazon EC2.

## Resolve errors when activating your gateway using a public endpoint and there is

a Storage Gateway VPC endpoint in the same VPC

To resolve errors when activating your gateway using a public endpoint when there is a
Amazon Virtual Private Cloud (Amazon VPC) enpoint in the same VPC, perform the following checks and
configurations.

### Confirm that the **Enable Private DNS Name** setting isn't

enabled on your Storage Gateway VPC endpoint

If **Enable Private DNS Name** is enabled, you can't activate any
gateways from that VPC to the public endpoint.

###### To disable the private DNS name option:

1. Open the [Amazon VPC console](https://console.aws.amazon.com//vpc/ "https://console.aws.amazon.com//vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose your Storage Gateway VPC endpoint.
4. Choose **Actions**.
5. Choose **Manage Private DNS Names**.
6. For **Enable Private DNS Name**, clear **Enable
   for this Endpoint**.
7. Choose **Modify Private DNS Names** to save the
   setting.
