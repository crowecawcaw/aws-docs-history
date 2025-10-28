# AWS Server Migration Service in AWS GovCloud (US)

###### Important

**Product update**

On March 31, 2022, AWS discontinued AWS Server Migration Service (AWS SMS). We recommend [AWS Application Migration Service](govcloud-mgn.md "govcloud-mgn.md") as the primary migration service for lift-and-shift migrations in AWS GovCloud (US).

AWS Server Migration Service (AWS SMS) combines data collection tools with automated server replication to speed the migration of on-premises servers to AWS.

To use the Server Migration Connector with AWS GovCloud (US) Regions, follow these steps on your
Server Migration Connector VM. The following procedure permanently converts your connector
virtual appliance to an AWS GovCloud (US) connector.

1. Install the Server Migration Connector as described in [Getting Started with AWS Server Migration Service](../../../server-migration-service/latest/userguide/SMS_setup.md "../../../server-migration-service/latest/userguide/SMS_setup.md").
2. Open the connector's virtual machine console and log in as `ec2-user` with the password `ec2pass`. Supply a new password if prompted.
3. Run the following command:

```
`sudo enable-govcloud`
```

4. In a web browser, access the connector VM at its IP address
   (`https://ip-address-of-connector/`). In the setup wizard, under
   **AWS Region**, the AWS GovCloud (US) Regions should now be the Regions listed.

## How AWS Server Migration Service differs for AWS GovCloud (US)

This service has no differences between the AWS GovCloud (US) and the standard AWS Regions.

## Documentation for AWS Server Migration Service

[AWS SMS User Guide](../../../server-migration-service/latest/userguide.md "../../../server-migration-service/latest/userguide.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Virtual machine metadata is not permitted to contain export-controlled data.
  For example, text displayed outside of a virtual machine console in vSphere
  Client, SCVMM, or Hyper-V Manager is not permitted to contain export-controlled
  data.
- Do not enter export-controlled data in the following fields:
  - VM names or paths
  - Virtual machine disk file paths
  - IP addresses or host names of VMs, ESXi hosts, vCenter, Hyper-V hosts,
    or SCVMM
  - User name of any service account or Active Directory user created for
    Service Migration Connector to log into vCenter, SCVMM, or
    Hyper-V

- Do not enter export-controlled data into the root or boot partition of any
  virtual machine being imported using the AWS Server Migration Service
