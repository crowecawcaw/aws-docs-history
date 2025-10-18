# Cluster

Contains information about an AWS CloudHSM cluster.


## Contents





**BackupPolicy** 


The cluster's backup policy.


Type: String


Valid Values: `DEFAULT`



Required: No




**BackupRetentionPolicy** 


A policy that defines how the service retains backups.


Type: [BackupRetentionPolicy](API_BackupRetentionPolicy.md "API_BackupRetentionPolicy.md") object


Required: No




**Certificates** 


Contains one or more certificates or a certificate signing request (CSR).


Type: [Certificates](API_Certificates.md "API_Certificates.md") object


Required: No




**ClusterId** 


The cluster's identifier (ID).


Type: String


Pattern: `cluster-[2-7a-zA-Z]{11,16}`



Required: No




**CreateTimestamp** 


The date and time when the cluster was created.


Type: Timestamp


Required: No




**Hsms** 


Contains information about the HSMs in the cluster.


Type: Array of [Hsm](API_Hsm.md "API_Hsm.md") objects


Required: No




**HsmType** 


The type of HSM that the cluster contains.


Type: String


Length Constraints: Maximum length of 32.


Pattern: `((p|)hsm[0-9][a-z.]*\.[a-zA-Z]+)`



Required: No




**HsmTypeRollbackExpiration** 


The timestamp until when the cluster can be rolled back to its original HSM type.


Type: Timestamp


Required: No




**Mode** 


The mode of the cluster.


Type: String


Valid Values: `FIPS | NON_FIPS`



Required: No




**NetworkType** 


The cluster's NetworkType can be IPv4 (the default) or DUALSTACK.
 The IPv4 NetworkType restricts communication between your application and the hardware security modules (HSMs) to the IPv4 protocol only. The DUALSTACK NetworkType enables communication over both IPv4 and IPv6 protocols.
 To use DUALSTACK, configure your virtual private cloud (VPC) and subnets to support both IPv4 and IPv6.
 This configuration involves adding IPv6 Classless Inter-Domain Routing (CIDR) blocks to the existing IPv4 CIDR blocks in your subnets.
 The NetworkType you choose affects the network addressing options for your cluster. DUALSTACK provides more flexibility by supporting both IPv4 and IPv6 communication.


Type: String


Valid Values: `IPV4 | DUALSTACK`



Required: No




**PreCoPassword** 


The default password for the cluster's Pre-Crypto Officer (PRECO) user.


Type: String


Length Constraints: Minimum length of 7. Maximum length of 32.


Required: No




**SecurityGroup** 


The identifier (ID) of the cluster's security group.


Type: String


Pattern: `sg-[0-9a-fA-F]{8,17}`



Required: No




**SourceBackupId** 


The identifier (ID) of the backup used to create the cluster. This value exists only
 when the cluster was created from a backup.


Type: String


Pattern: `backup-[2-7a-zA-Z]{11,16}`



Required: No




**State** 


The cluster's state.


Type: String


Valid Values: `CREATE_IN_PROGRESS | UNINITIALIZED | INITIALIZE_IN_PROGRESS | INITIALIZED | ACTIVE | UPDATE_IN_PROGRESS | MODIFY_IN_PROGRESS | ROLLBACK_IN_PROGRESS | PENDING_ROLLBACK | DELETE_IN_PROGRESS | DELETED | DEGRADED`



Required: No




**StateMessage** 


A description of the cluster's state.


Type: String


Length Constraints: Maximum length of 300.


Pattern: `.*`



Required: No




**SubnetMapping** 


A map from availability zone to the cluster’s subnet in that availability zone.


Type: String to string map


Key Pattern: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d[a-z]`



Value Pattern: `subnet-[0-9a-fA-F]{8,17}`



Required: No




**TagList** 


The list of tags for the cluster.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Minimum number of 1 item. Maximum number of 50 items.


Required: No




**VpcId** 


The identifier (ID) of the virtual private cloud (VPC) that contains the
 cluster.


Type: String


Pattern: `vpc-[0-9a-fA-F]`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/Cluster "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/Cluster")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/Cluster "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/Cluster")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/Cluster "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/Cluster")
