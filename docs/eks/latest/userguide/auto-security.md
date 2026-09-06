

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Security considerations for Amazon EKS Auto Mode
<a name="auto-security"></a>

This topic describes the security architecture, controls, and best practices for Amazon EKS Auto Mode. As organizations deploy containerized applications at scale, maintaining a strong security posture becomes increasingly complex. EKS Auto Mode implements automated security controls and integrates with AWS security services to help you protect your cluster infrastructure, workloads, and data. Through built-in security features like enforced node lifecycle management and automated patch deployment, EKS Auto Mode helps you maintain security best practices while reducing operational overhead.

Before proceeding with this topic, make sure that you’re familiar with basic EKS Auto Mode concepts and have reviewed the prerequisites for enabling EKS Auto Mode on your clusters. For general information about Amazon EKS security, see [Security in Amazon EKS](security.md).

Amazon EKS Auto Mode builds upon the existing security foundations of Amazon EKS while introducing additional automated security controls for EC2 managed instances.

## API security and authentication
<a name="_api_security_and_authentication"></a>

Amazon EKS Auto Mode uses AWS platform security mechanisms to secure and authenticate calls to the Amazon EKS API.
+ Access to the Kubernetes API is secured through EKS access entries, which integrate with AWS IAM identities.
  + For more information, see [Grant IAM users access to Kubernetes with EKS access entries](access-entries.md).
+ Customers can implement fine-grained access control to the Kubernetes API endpoint through configuration of EKS access entries.

## Network security
<a name="_network_security"></a>

Amazon EKS Auto Mode supports multiple layers of network security:
+  **VPC integration** 
  + Operates within your Amazon Virtual Private Cloud (VPC)
  + Supports custom VPC configurations and subnet layouts
  + Enables private networking between cluster components
  + For more information, see [Managing security responsibilities for Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/security.html) 
+  **Network Policies** 
  + Native support for Kubernetes Network Policies
  + Ability to define granular network traffic rules
  + For more information, see [Limit Pod traffic with Kubernetes network policies](cni-network-policy.md) 

## EC2 managed instance security
<a name="_ec2_managed_instance_security"></a>

Amazon EKS Auto Mode operates EC2 managed instances with the following security controls:

### EC2 security
<a name="_ec2_security"></a>
+ EC2 managed instances maintain the security features of Amazon EC2.
+ For more information about EC2 managed instances, see [Security in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html).

### Instance lifecycle management
<a name="_instance_lifecycle_management"></a>

EC2 managed instances operated by EKS Auto Mode have a maximum lifetime of 21 days. Amazon EKS Auto Mode automatically terminates instances exceeding this lifetime. This lifecycle limit helps prevent configuration drift and maintains security posture.

### Data protection
<a name="_data_protection"></a>
+ Amazon EC2 Instance Storage is encrypted, this is storage directly attached to the instance. For more information, see [Data protection in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html).
+ EKS Auto Mode manages the volumes attached to EC2 instances at creation time, including root and data volumes. EKS Auto Mode does not fully manage EBS volumes created using Kubernetes persistent storage features.

### Patch management
<a name="_patch_management"></a>
+ Amazon EKS Auto Mode automatically applies patches to managed instances.
+ Patches include:
  + Operating system updates
  + Security patches
  + Amazon EKS Auto Mode components

**Note**  
Customers retain responsibility for securing and updating workloads running on these instances.

### Access controls
<a name="_access_controls"></a>
+ Direct instance access is restricted:
  + SSH access is not available.
  +  AWS Systems Manager Session Manager (SSM) access is not available.
+ Management operations are performed through the Amazon EKS API and Kubernetes API.

## Automated resource management
<a name="_automated_resource_management"></a>

Amazon EKS Auto Mode does not fully manage Amazon Elastic Block Store (Amazon EBS) Volumes created using Kubernetes persistent storage features. EKS Auto Mode also does not manage Elastic Load Balancers (ELB). Amazon EKS Auto Mode automates routine tasks for these resources.

### Storage security
<a name="_storage_security"></a>
+  AWS recommends that you enable encryption for EBS Volumes provisioned by Kubernetes persistent storage features. For more information, see [Create a storage class](create-storage-class.md).
+ Encryption at rest using AWS KMS
+ You can configure your AWS account to enforce the encryption of the new EBS volumes and snapshot copies that you create. For more information, see [Enable Amazon EBS encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html) in the Amazon EBS User Guide.
+ For more information, see [Security in Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/security.html).

### Load balancer security
<a name="_load_balancer_security"></a>
+ Automated configuration of Elastic Load Balancers
+ SSL/TLS certificate management through AWS Certificate Manager integration
+ Security group automation for load balancer access control
+ For more information, see [Security in Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security.html).

## Security best practices
<a name="auto-security-bp"></a>

The following section describes security best practices for Amazon EKS Auto Mode.
+ Regularly review AWS IAM policies and EKS access entries.
+ Implement least privilege access patterns for workloads.
+ Monitor cluster activity through AWS CloudTrail and Amazon CloudWatch. For more information, see [Log API calls as AWS CloudTrail events](logging-using-cloudtrail.md) and [Monitor cluster data with Amazon CloudWatch](cloudwatch.md).
+ Use AWS Security Hub for security posture assessment.
+ Implement pod security standards appropriate for your workloads.