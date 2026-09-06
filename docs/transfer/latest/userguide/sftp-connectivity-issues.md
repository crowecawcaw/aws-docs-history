

# Troubleshoot SFTP connectivity and transfer issues
<a name="sftp-connectivity-issues"></a>

This section describes possible solutions for SFTP connectivity and file transfer issues.

**Topics**
+ [Troubleshoot SFTP connectivity issues](#connection-issues)
+ [Troubleshoot SFTP client issues](#sftp-client-troubleshooting-issues)
+ [Troubleshoot file upload issues](#file-upload-issues)
+ [Troubleshoot VPC egress type SFTP connector issues](#vpc-connector-connectivity-issues)

## Troubleshoot SFTP connectivity issues
<a name="connection-issues"></a>

**Description**

Your SFTP client cannot initiate the connection. This issue can happen continuously or intermittently. For example, you might see the following sequence of events in your SFTP client debug logs:

```
sftp -vvv username@1.1.1.1
.................................
debug1: Local version string ...........
kex_exchange_identification: read: Connection reset by peer
Connection reset by 1.1.1.1 port 22
Connection closed.
```

**Cause**

There is an edge case where the zero-byte TCP ACK (ACK without data), also known as the three-way handshake, is either dropped or delayed.

**Solution**

As a workaround, Transfer Family offers a solution that uses a different configuration to solve this issue, but may cause compatibility issues with older clients. For that reason, this solution is available only on port 2223.

In the procedure for creating a Transfer Family server in a VPC ([Create a server in a virtual private cloud](create-server-in-vpc.md)), when you specify a security group, configure SSH traffic to use port 2223.

## Troubleshoot SFTP client issues
<a name="sftp-client-troubleshooting-issues"></a>

SFTP client side messages are described in [SFTP messages](transfer-file.md#sftp-transfer-activity-types). The best way to troubleshoot SFTP client issues is to check the SFTP client logs and, if necessary, reach out to your network administrator.

## Troubleshoot file upload issues
<a name="file-upload-issues"></a>

This section describes possible solutions for the following file upload issues.

**Topics**
+ [Troubleshoot Amazon S3 file upload errors](#random-access-writes-s3)
+ [Troubleshoot unreadable file names](#non-utf8-issues)

### Troubleshoot Amazon S3 file upload errors
<a name="random-access-writes-s3"></a>

**Description**

When you are attempting to upload a file to Amazon S3 storage using Transfer Family, you receive the following error message: AWS Transfer does not support random access writes to S3 objects.

**Cause**

When you're using Amazon S3 for your server's storage, Transfer Family does not support multiple connections for a single transfer.

**Solution**

If your Transfer Family server is using Amazon S3 for its storage, disable any options for your client software that mention using multiple connections for a single transfer.

### Troubleshoot unreadable file names
<a name="non-utf8-issues"></a>

**Description**

You see corrupted file names in some of your uploaded files. Users sometimes encounter problems with FTP and SFTP transfers that garble certain characters in file names, such as umlauts, accented letters, or certain scripts, such as Chinese or Arabic. 

**Cause**

Although the FTP and SFTP protocols can allow for character encoding of files names to be negotiated by clients, Amazon S3 and Amazon EFS do not. Instead, they require UTF-8 character encoding. As a result, certain characters are not rendered correctly. 

**Solution**

To solve this problem, review your client application for file name character encoding and make sure it is set to UTF-8.

## Troubleshoot VPC egress type SFTP connector issues
<a name="vpc-connector-connectivity-issues"></a>

If you're experiencing issues with VPC egress type SFTP connectors, check the following:

### Connector status is PENDING
<a name="vpc-connector-pending-status"></a>

**Description**

Your VPC egress type connector remains in PENDING status for several minutes after creation, and TestConnection returns "Connector not available".

**Cause**

DNS resolution for VPC connectors can take several minutes to complete after creation.

**Solution**

Wait for the connector status to become ACTIVE before attempting file transfers. This is normal behavior for VPC egress type connectors.

### Connection timeouts
<a name="vpc-connector-timeouts"></a>

**Description**

Your VPC egress type connector times out when attempting to connect to the SFTP server.

**Cause**

Security groups may not allow traffic on port 22 between your Resource Gateway subnets and the target SFTP server.

**Solution**

Verify that security groups allow traffic on port 22 between your Resource Gateway subnets and the target SFTP server.

### Resource Configuration errors
<a name="vpc-resource-configuration-errors"></a>

**Description**

Your VPC egress type connector fails to connect due to Resource Configuration issues.

**Cause**

The Resource Configuration may point to an incorrect IP address or DNS name, or the Resource Gateway may not be in the same VPC as your SFTP server (for private endpoints).

**Solution**

Ensure your Resource Configuration points to the correct IP address or DNS name, and that the Resource Gateway is in the same VPC as your SFTP server (for private endpoints). For more information, see [Resource configurations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html) in the *Amazon VPC Lattice User Guide*.

### Public endpoint issues
<a name="vpc-public-endpoint-issues"></a>

**Description**

Your VPC egress type connector cannot connect to public SFTP endpoints.

**Cause**

For public endpoints, you must use a DNS name (not an IP address) in your Resource Configuration, and your VPC must have a NAT Gateway for outbound internet access.

**Solution**

Ensure you're using a DNS name, not an IP address, in your Resource Configuration. Verify that your VPC has a NAT Gateway for outbound internet access.

### Availability Zone issues
<a name="vpc-az-availability-issues"></a>

**Description**

You cannot create a Resource Gateway due to Availability Zone limitations.

**Cause**

Resource Gateways require subnets in at least 2 Availability Zones, and not all AZs support VPC Lattice.

**Solution**

Check the supported Availability Zones for VPC Lattice in your region and ensure you have subnets in at least 2 supported AZs.