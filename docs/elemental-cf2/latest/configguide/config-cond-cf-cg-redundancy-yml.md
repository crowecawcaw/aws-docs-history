This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step B: Create a dbrepl_config.yml File

1. Use a text editor to create a file called `dbrepl_config.yml` in the home/elemental directory.
2. Enter the following lines in the file. Make sure to enter values in single quotes.
   - `primary_hostname`: The hostname for the primary Conductor. Use one of
     the following:
     - The name that you assigned when you installed the Conductor software, regardless of whether
       you installed on a hardware unit or a VM. For example
       `conductor_01`.
     - The name that AWS Elemental assigned to an appliance: `ecle` or
       `ecfe` and the serial number (unless you changed this name at
       some point).

   - `primary_ip`
   - `primary_mac`: The MAC address of the management interface on the primary
     Conductor. You identified this address when getting ready in Step A.
   - `secondary_hostname`: The hostname for the secondary Conductor, as
     described in `primary_hostname`.
   - `secondary_ip`
   - `secondary_mac`
   - `virtual_ip`: You identified this address when getting ready in Step
     A.
   - `virtual_router_id`: You identified this ID when getting ready in Step
     A.
   - `virtual_ip_interface`: You identified this interface when getting ready
     in Step A.

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
