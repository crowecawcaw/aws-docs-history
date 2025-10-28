# Troubleshooting data collection issues related to

network and server connections in AWS DMS

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service
Fleet Advisor. After May 20, 2026, you will no longer be able to access the
AWS DMS Fleet Advisor console or AWS DMS Fleet Advisor resources. For more
information, see [AWS DMS Fleet
Advisor end of support](dms_fleet.md "dms_fleet.md").

If you run into issues related to network and server connections with the DMS data collector, try the following actions.

**NET: An exception occurred during a ping request.**

Check the name of the computer to see if it's in a state where it can't be
resolved to an IP address.

For example, check if the computer is switched off, disconnected from the
network, or decommissioned.

**NET: Timed Out**

Turn on the inbound firewall rule "File and Printer Sharing (Echo Request

- ICMPv4-In)". For example:

`* Inbound ICMPv4`

**NET: DestinationHostUnreachable**

Check the IP address of the computer. Specifically, check if it's on
the same subnet as the computer running DMS data collector and whether it responds
to Address Resolution Protocol (ARP) requests.

If the computer is on a different subnet, then the IP address of the gateway
can't be resolved to the media access control (MAC) address.

Also, check if the computer is switched off, disconnected from the
network, or decommissioned.
