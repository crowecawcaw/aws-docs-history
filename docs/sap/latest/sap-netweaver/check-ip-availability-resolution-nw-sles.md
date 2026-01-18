# Check IP availability and resolution

## Add Overlay IP for SAP Installation

SAP Installation should be done using the virtual names assigned to the overlay IP. Before adding the overlay IPs to the instances, ensure that the VPC route table entries have been created as described in [Add VPC Route Table Entries for Overlay IPs](sap-nw-pacemaker-sles-infra-setup.md#rt-sles "sap-nw-pacemaker-sles-infra-setup.md#rt-sles").

To facilitate SAP installation, manually add the Overlay IPs to the instances:

1. To the instance where you intend to install the **ASCS**

```
 # ip addr add <ascs_overlayip>/32 dev eth0
```

2. To the instance where you intend to install the **ERS**

```
 # ip addr add <ers_overlayip>/32 dev eth0
```

Note the following:

- Route table entries for the overlay IPs must be created first (see [Add VPC Route Table Entries for Overlay IPs](sap-nw-pacemaker-sles-infra-setup.md#rt-sles "sap-nw-pacemaker-sles-infra-setup.md#rt-sles"))
- This IP configuration is temporary and will be lost after instance reboot
- The cluster will take over management of these IPs once configured

## Hostname Resolution

You must ensure that all instances can resolve all hostnames in use. Add the hostnames for cluster nodes to `/etc/hosts` file on all cluster nodes. This ensures that hostnames for cluster nodes can be resolved even in case of DNS issues. Configure the `/etc/hosts` file for a two-node cluster:

```
 # cat /etc/hosts
<primary_ip_1> <hostname_1>.example.com <hostname_1>
<primary_ip_2> <hostname_2>.example.com <hostname_2>
<ascs_overlayip> <ascs_virt_hostname>.example.com <ascs_virt_hostname>
<ers_overlayip> <ers_virt_hostname>.example.com <ers_virt_hostname>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
 # cat /etc/hosts
10.1.10.1 slxhost01.example.com slxhost01
10.1.20.1 slxhost02.example.com slxhost02
172.16.30.5 slxascs.example.com slxascs
172.16.30.6 slxers.example.com slxers
```

In this configuration, the secondary IPs used for the second cluster ring are not mentioned. They are only used in the cluster configuration. You can allocate virtual hostnames for administration and identification purposes.

###### Important

The Overlay IP is out of VPC range, and cannot be reached from locations not associated with the route table, including on-premises.
