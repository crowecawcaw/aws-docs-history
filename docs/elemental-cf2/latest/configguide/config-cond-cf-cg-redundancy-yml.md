

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step B: Create a dbrepl\_config.yml File
<a name="config-cond-cf-cg-redundancy-yml"></a>

1. Use a text editor to create a file called `dbrepl_config.yml` in the home/elemental directory.

1. Enter the following lines in the file. Make sure to enter values in single quotes. 
   + **primary\_hostname**: The hostname for the primary Conductor. Use one of the following:
     + The name that you assigned when you installed the Conductor software, regardless of whether you installed on a hardware unit or a VM. For example **conductor\_01**. 
     + The name that AWS Elemental assigned to an appliance: `ecle` or `ecfe` and the serial number (unless you changed this name at some point).
   + **primary\_ip**
   + **primary\_mac**: The MAC address of the management interface on the primary Conductor. You identified this address when getting ready in Step A.
   + **secondary\_hostname**: The hostname for the secondary Conductor, as described in `primary_hostname`.
   + **secondary\_ip**
   + **secondary\_mac** 
   + **virtual\_ip**: You identified this address when getting ready in Step A.
   + **virtual\_router\_id**: You identified this ID when getting ready in Step A.
   + **virtual\_ip\_interface**: You identified this interface when getting ready in Step A.

**Example**  

```
primary_hostname: 'cl_primary'
primary_ip: '10.4.138.230'
primary_mac: '00:50:56:AE:A5:5D'
secondary_hostname: 'cl_secondary'
secondary_ip: '10.4.138.231'
secondary_mac: '00:50:56:AE:A5:60'
virtual_ip: '10.4.138.232'
virtual_router_id: 42
virtual_ip_interface: 'eth0'
```