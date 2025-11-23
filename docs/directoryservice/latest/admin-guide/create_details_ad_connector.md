# What gets created with your

AD Connector

When you create an AD Connector, Directory Service automatically creates and associates an
elastic network interface (ENI) with each of your AD Connector instances. Each of
these ENIs are essential for connectivity between your VPC and Directory Service AD Connector and
should never be deleted. You can identify all network interfaces reserved for use with
Directory Service by the description: "AWS created network interface for directory
_directory-id_". For more information, see [Elastic Network
Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the Amazon EC2 User Guide.

###### Note

AD Connector instances are deployed across two Availability Zones in a Region by
default and connected to your Amazon Virtual Private Cloud (VPC). AD Connector
instances that fail are automatically replaced in the same Availability Zone using
the same IP address.

When you sign in to any AWS application or service integrated with an AD Connector
(AWS IAM Identity Center included), the app or service forwards your authentication request to
AD Connector which then forwards the request to a domain controller in your
self-managed Active Directory for authentication. If you are successfully authenticated
to your self-managed Active Directory, AD Connector then returns an authentication
token to the app or service (similar to a Kerberos token). At this point, you can now
access the AWS app or service.
