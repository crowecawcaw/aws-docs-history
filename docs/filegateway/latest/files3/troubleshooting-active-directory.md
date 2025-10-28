# Troubleshooting: issues joining gateway

to Active Directory

Use the following troubleshooting information to determine what to do if you receive error
messages such as `NETWORK_ERROR`, `TIMEOUT`, or
`ACCESS_DENIED` when trying to join your File Gateway to a Microsoft Active
Directory domain.

To resolve these errors, perform the following checks and configurations.

## Confirm that the gateway can reach the domain controller by running an nping

test

###### To run an nping test:

1. Connect to the gateway local console using your hypervisor management software
   (VMware, Hyper-V, or KVM) for on-premises gateways, or using ssh for Amazon EC2
   gateways.
2. Enter the corresponding numeral to select **Gateway
   Console**, and then enter `h` to list all available
   commands. To test the connectivity between the Storage Gateway virtual machine and the
   domain, run the following command:

`nping -d `corp.domain.com`-p
`389` -c 1 -t tcp`

###### Note

Replace `corp.domain.com` with your Active Directory domain DNS
name and replace `389` with the LDAP port for your
environment.

Verify that you have opened the required ports within your
firewall.

The following is an example of a successful nping test where the gateway was able to
reach the domain controller:

```
nping -d corp.domain.com -p 389 -c 1 -t tcp

Starting Nping 0.6.40 ( http://nmap.org/nping ) at 2022-06-30 16:24 UTC
SENT (0.0553s) TCP 10.10.10.21:9783 > 10.10.10.10:389 S ttl=64 id=730 iplen=40  seq=2597195024 win=1480
RCVD (0.0556s) TCP 10.10.10.10:389 > 10.10.10.21:9783 SA ttl=128 id=22332 iplen=44  seq=4170716243 win=8192 <mss 8961>

Max rtt: 0.310ms | Min rtt: 0.310ms | Avg rtt: 0.310ms
Raw packets sent: 1 (40B) | `Rcvd: 1 (44B)` | Lost: 0 (0.00%)
Nping done: 1 IP address pinged in 1.09 seconds<br>
```

The following is an example of an nping test where there is no connectivity to or
response from the `corp.domain.com` destination:

```
nping -d corp.domain.com -p 389 -c 1 -t tcp

Starting Nping 0.6.40 ( http://nmap.org/nping ) at 2022-06-30 16:26 UTC
SENT (0.0421s) TCP 10.10.10.21:47196 > 10.10.10.10:389  S ttl=64 id=30318 iplen=40 seq=1762671338 win=1480

Max rtt: N/A | Min rtt: N/A | Avg rtt: N/A
Raw packets sent: 1 (40B) | Rcvd: 0 (0B) | `Lost: 1 (100.00%)`
Nping done: 1 IP address pinged in 1.07 seconds
```

## Check the DHCP options set for the VPC of your Amazon EC2 gateway instance

If the File Gateway is running on an Amazon EC2 instance, then you must make sure a DHCP
options set is properly configured and attached to the Amazon Virtual Private Cloud (VPC) that contains the
gateway instance. For more information, see [DHCP option sets in Amazon
VPC](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md").

## Confirm that the gateway can resolve the domain by running a dig query

If the domain isn't resolvable by the gateway, then the gateway can't join the
domain.

###### To run a dig query:

1. Connect to the gateway local console using your hypervisor management software
   (VMware, Hyper-V, or KVM) for on-premises gateways, or using ssh for Amazon EC2
   gateways.
2. Enter the corresponding numeral to select **Gateway
   Console**, and then enter `h` to list all available
   commands. To test whether the gateway can resolve the domain, run the following
   command:

`dig -d `corp.domain.com``

###### Note

Replace `corp.domain.com` with your Active Directory domain DNS
name.

The following is an example of a successful response:

```
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.amzn2.5.2 <<>> corp.domain.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 24817
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;corp.domain.com.        IN    A

;; ANSWER SECTION:
`corp.domain.com. 600 IN A 10.10.10.10
corp.domain.com. 600 IN A 10.10.20.10`

;; Query time: 0 msec
;; SERVER: 10.10.20.228#53(10.10.20.228)
;; WHEN: Thu Jun 30 16:36:32 UTC 2022
;; MSG SIZE  rcvd: 78
```

## Check the domain controller settings and roles

Verify that the domain controller isn't set to read-only, and that the domain
controller has enough roles for computers to join. To test this, try joining other
servers from the same VPC subnet as the gateway VM to the domain.

## Check that the gateway is joined to the nearest domain controller

As a best practice, we recommend joining your gateway to a domain controller that is
geographically close to the gateway appliance. If the gateway appliance can't
communicate with the domain controller within 20 seconds due to network latency, then
the domain joining process can time out. For example, the process might time out if the
gateway appliance is in the US East (N. Virginia) AWS Region and the domain controller is
in the Asia Pacific (Singapore) AWS Region.

###### Note

To increase the default timeout value of 20 seconds, you can run the [join-domain command](../../../cli/latest/reference/storagegateway/join-domain.md "../../../cli/latest/reference/storagegateway/join-domain.md") in the AWS Command Line Interface (AWS CLI) and include the
`--timeout-in-seconds` option to increase the time. You can also use
the [JoinDomain API call](https://amazonaws.com/storagegateway/latest/APIReference/API_JoinDomain.html "https://amazonaws.com/storagegateway/latest/APIReference/API_JoinDomain.html") and include the `TimeoutInSeconds`
parameter to increase the time. The maximum timeout value is 3,600 seconds.

If you receive errors when running AWS CLI commands, make sure that you’re using the
most recent AWS CLI version.

## Confirm that Active Directory creates new computer objects in the default

organizational unit (OU)

Make sure Microsoft Active Directory does not have any Group Policy Objects that
create new computer objects in any location other than the default OU. Before you can
join your gateway to the Active Directory domain, a new computer object must exist in
the default OU. Some Active Directory environments are customized to have different OUs
for newly created objects. To guarantee that a new computer object for the gateway VM
exists in the default OU, try creating the computer object manually on your domain
controller before you join the gateway to the domain. You can also run the [join-domain command](../../../cli/latest/reference/storagegateway/join-domain.md "../../../cli/latest/reference/storagegateway/join-domain.md") using the AWS CLI. Then, specify the option for
`--organizational-unit`.

###### Note

The process of creating the computer object is called pre-staging.

## Check your domain controller event logs

If you can't join the gateway to the domain after trying all other checks and
configurations described in the previous sections, we recommend examining your domain
controller event logs. Check for any errors in the event viewer of the domain
controller. Verify that the gateway queries have reached the domain controller.
