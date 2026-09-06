

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Infrastructure security
<a name="sec-infrastructure"></a>

**Note**  
Additional information on this topic is available by accessing AWS Artifact reports. For more information, see [Downloading reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html). To access AWS Artifact, you can contact your CSDM for instructions or go to [Getting Started with AWS Artifact](https://aws.amazon.com/artifact/getting-started). This information is not included in this user guide because it contains sensitive security content.



## Using security groups
<a name="sec-group-intro"></a>

A security group acts as a virtual firewall that controls the traffic for one or more instances. AMS security groups allow you to set inbound traffic rules and outbound traffic rules on an instance-level basis. You can create a security group and specify resources in your AMS account, Amazon EC2 instances, Amazon RDS DB instances, Load Balancers, Deep Security Manager (DSM) replication instances, EFS mount targets, and ElastiCache clusters, to associate with the security group. Once associated, traffic to or from those instances is constrained by the rules set in the security group.

To better understand general AWS security, see [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/) and [Amazon EC2 Security Groups for Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html).

AMS now has a set of change types for creating and managing security groups:
+ Deployment \| Advanced stack components \| Security group \| Create (ct-1oxx2g2d7hc90)
+ Management \| Advanced stack components \| Security group \| Delete (ct-3cp96z7r065e4)
+ Management \| Advanced stack components \| Security group \| Update (ct-3memthlcmvc1b)

For examples, see [Security groups](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-sec-group-create-delete-update.html).