# Protecting data in transit

_Data in transit_ is any data that is sent from one system to another. This
includes communication between resources within your workload as well as communication between
other services and your end users. By providing the appropriate level of protection for your
data in transit, you protect the confidentiality and integrity of your workload’s data.

**Secure data from between VPC or on-premises locations:**
You can use [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") to create a
secure and private network connection between Amazon Virtual Private Cloud (Amazon VPC) or on-premises connectivity to
services hosted in AWS. You can access AWS services, third-party services, and services in
other AWS accounts as if they were on your private network. With AWS PrivateLink, you can
access services across accounts with overlapping IP CIDRs without needing an Internet Gateway
or NAT. You also do not have to configure firewall rules, path definitions, or route tables.
Traffic stays on the Amazon backbone and doesn’t traverse the internet, therefore your data is
protected. You can maintain compliance with industry-specific compliance regulations, such as
HIPAA and EU/US Privacy Shield. AWS PrivateLink seamlessly works with third-party solutions to
create a simplified global network, allowing you to accelerate your migration to the cloud and
take advantage of available AWS services.

###### Best practices

- [SEC09-BP01 Implement secure key and certificate
  management](sec_protect_data_transit_key_cert_mgmt.md "sec_protect_data_transit_key_cert_mgmt.md")
- [SEC09-BP02 Enforce encryption in transit](sec_protect_data_transit_encrypt.md "sec_protect_data_transit_encrypt.md")
- [SEC09-BP03 Authenticate network communications](sec_protect_data_transit_authentication.md "sec_protect_data_transit_authentication.md")
