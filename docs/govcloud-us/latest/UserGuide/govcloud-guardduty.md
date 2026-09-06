

# Amazon GuardDuty in AWS GovCloud (US)
<a name="govcloud-guardduty"></a>

Amazon GuardDuty is a continuous security monitoring service. Amazon GuardDuty can help to identify unexpected and potentially unauthorized or malicious activity in your AWS environment.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon GuardDuty differs
<a name="govcloud-gdu-diffs"></a>

The following differences apply to Amazon GuardDuty:
+ When using [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html) (including EKS Runtime Monitoring), make the following changes in the AWS GovCloud (US) Regions:

  1.  **For both Amazon EC2 and Amazon EKS **– In the prerequisite step for creating an Amazon VPC endpoint manually, the **Service name** in the AWS GovCloud (US) Region should be `com.amazonaws.<us-gov-east-1>.guardduty-data-fips`.

     Replace <us-gov-east-1> with your Region. This must be the same Region as your Amazon EC2 instance (or Amazon EKS cluster) that belongs to your AWS account ID.

  1. With the initial release of Runtime Monitoring, GuardDuty starts the support with the following security agent versions:
     +  Amazon EKS - v1.11.1
     +  Amazon EC2 - v1.8.0
     +  Fargate-Amazon ECS - v1.8.0

  For more information, see [GuardDuty security agent release versions](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-release-history.html).

  1.  **For Amazon EC2 **– When managing the security agent manually using [Method 2 - Using Linux Package Managers](https://docs.aws.amazon.com/guardduty/latest/ug/installing-gdu-security-agent-ec2-manually.html), use the following AWS account IDs and Regions for both RPM installation and Debian installation:
     +  AWS GovCloud (US-East) (`us-gov-east-1`) – 383115532789
     +  AWS GovCloud (US-West) (`us-gov-west-1`) – 383110348953

  1.  **For Amazon EKS and Fargate-Amazon ECS resources**– For [Amazon ECR repository hosting GuardDuty agent](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-ecr-repository-gdu-agent.html), use the following ECR repository for your Amazon EKS and Fargate-Amazon ECS resources:
     +  ** Amazon ECR repository for EKS resources:** 

        AWS GovCloud (US-East) - `151742754352.dkr.ecr.us-gov-east-1.amazonaws.com` 

        AWS GovCloud (US-West) - `013241004608.dkr.ecr.us-gov-west-1.amazonaws.com` 
     +  ** Amazon ECR repository for Fargate-ECS resources:** 

        AWS GovCloud (US-East) - `383115532789.dkr.ecr.us-gov-east-1.amazonaws.com/aws-guardduty-agent-fargate` 

        AWS GovCloud (US-West) - `383110348953.dkr.ecr.us-gov-west-1.amazonaws.com/aws-guardduty-agent-fargate` 
+ The entity lists capability in [Customizing threat detection with entity lists and IP address lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html) is not available in AWS GovCloud (US) Regions. GuardDuty continues to support IP address lists.
+ The [Extended Threat Detection](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html) coverage for EKS clusters supports detecting multi-stage attacks through available EKS Protection finding types (EKS audit log monitoring) and AWS API activity.
+ The following [EKS Protection](https://docs.aws.amazon.com/guardduty/latest/ug/kubernetes-protection.html) (EKS audit log monitoring) finding types are not available in the AWS GovCloud (US) Regions:
  +  [CredentialAccess:Kubernetes/AnomalousBehavior.SecretsAccessed](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credaccess-kubernetes-anomalousbehavior-secretsaccessed) 
  +  [PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleBindingCreated](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-rolebindingcreated) 
  +  [Execution:Kubernetes/AnomalousBehavior.ExecInPod](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#execution-kubernetes-anomalousbehvaior-execinprod) 
  +  [PrivilegeEscalation:Kubernetes/AnomalousBehavior.WorkloadDeployed\!PrivilegedContainer](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-workloaddeployed-privcontainer) 
  +  [Persistence:Kubernetes/AnomalousBehavior.WorkloadDeployed\!ContainerWithSensitiveMount](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-workloaddeployed-containerwithsensitivemount) 
  +  [Execution:Kubernetes/AnomalousBehavior.WorkloadDeployed](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#exec-kubernetes-anomalousbehavior-workloaddeployed) 
  +  [PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleCreated](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-rolecreated) 
  +  [Discovery:Kubernetes/AnomalousBehavior.PermissionChecked](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-anomalousbehavior-permissionchecked) 
+ In [Malware Protection for EC2](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html), the support for scanning instances with `productCode` as `marketplace` is not available. GuardDuty will skip the malware scan for such instances and log the skip reason as `UNSUPPORTED_PRODUCT_CODE_TYPE`.
+ In [Malware Protection for Backup](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-backup.html), the scanning of EC2 and EBS Recovery points is not available. In these cases GuardDuty will not perform a scan on the input recovery point resource.
+ Cross-region data transfer is not available.
+ Preview of [GuardDuty Investigation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-investigation.html) and its associated APIs are not available in AWS GovCloud (US) Regions.
+ Member accounts invitation notifications through AWS Health Dashboard and email are not available.
+ In AWS GovCloud (US) Regions, AWS doesn’t use or store Customer Content processed by Amazon GuardDuty to develop and improve the service or technologies of AWS or its affiliates. Opt-out policies are currently not applicable to these Regions.
+ The following IAM finding types are not available in the AWS GovCloud (US) Regions:
  +  [CredentialAccess:IAMUser/CompromisedCredentials](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types.html#credentialaccess-iam-compromisedcredentials) 

## Documentation
<a name="govcloud-gdu-docs"></a>
+  [Amazon GuardDuty documentation](https://docs.aws.amazon.com/documentation/guardduty/) 

## Export-controlled content
<a name="govcloud-guardduty-itar-2"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.

No data will leave the AWS GovCloud (US) Regions for this service.