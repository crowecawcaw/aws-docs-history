

# Using security configurations with Amazon EMR WAL
<a name="emr-hbase-wal-security"></a>

Amazon EMR automatically encrypts both data in transit between your cluster and Amazon EMR WAL service, and the data at rest in Amazon EMR WAL. For more information, see [Encryption at rest for Amazon EMR WAL](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-data-encryption-options.html#emr-encryption-WAL). You can also use a security configuration to bring your own keys from AWS Key Management Service (KMS) service and encrypt the data that you store in Amazon EMR WAL. 

Use one of the following methods to select a security configuration when you create a cluster:

------
#### [ Console ]

From the AWS Management Console, specify the configuration under **Security configuration and EC2 key pair**.

![Security configuration section with search field showing DO-NOT-DELETE-disable-IM and buttons for Browse and Create security configuration.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/wal-configure-security.png)


------
#### [ CLI ]

From the AWS CLI, set the `--security-configuration` parameter when you use the [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html) command.

------

For more information, see [Encryption at rest for Amazon EMR WAL](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-data-encryption-options.html#emr-encryption-WAL) and [Use security configurations to set up cluster security](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-security-configurations.html) in the *Amazon EMR Management Guide*.

For more security-related information about WAL, see [Using service-linked roles for write-ahead logging](https://docs.aws.amazon.com/emr/latest/ManagementGuide/using-service-linked-roles-wal.html).