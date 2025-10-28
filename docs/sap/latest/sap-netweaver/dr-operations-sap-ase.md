# Disaster recovery

See [Disaster recovery deployment](deploy-options-sap-ase.md#ase-disaster-recovery-deployment "deploy-options-sap-ase.md#ase-disaster-recovery-deployment") to learn about disaster recovery for your SAP ASE database.

## Perform a DNS change

In case of manual failover, you may install SAP application servers using a virtual hostname and perform a DNS change to direct the SAP application servers to the new primary database server. For a DNS resolution in AWS, you can use any of the following options.

- [Amazon Route 53](../../../Route53/latest/DeveloperGuide/dns-configuring.md "../../../Route53/latest/DeveloperGuide/dns-configuring.md") enables you to create a private hosted zone for your environment and an A record for the virtual hostname used for SAP ASE database. Initially, this A record is mapped to the IP address of the primary SAP ASE database instance.
- You can maintain your own DNS server on-premise or on your Amazon EC2 instances. You can create an A record there for your virtual hostname used for SAP ASE database. Initially, this A record is mapped to the IP address of the primary SAP ASE database instance.
- With the [AWS Directory Service](https://aws.amazon.com/directoryservice/ "https://aws.amazon.com/directoryservice/"), you can create an A record for the virtual hostname used for SAP ASE database.

With any of the previously mentioned options, you can change the A record to a private IP address of the primary database instance in case of a failover. This DNS change can also be automated using AWS services and scripts.
