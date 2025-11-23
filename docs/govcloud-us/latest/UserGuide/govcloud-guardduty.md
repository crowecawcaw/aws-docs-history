# Amazon GuardDuty in AWS GovCloud (US)

Amazon GuardDuty is a continuous security monitoring service. Amazon GuardDuty can help to identify unexpected and potentially unauthorized or malicious activity in your AWS environment.

## How Amazon GuardDuty differs for AWS GovCloud (US) Regions

The following list indicates the differences in the feature availability in AWS GovCloud (US) Regions:

- When using [Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring.md "../../../guardduty/latest/ug/runtime-monitoring.md") (including EKS Runtime Monitoring), make the following changes in the AWS GovCloud (US) Regions:

      1. **For both Amazon EC2 and Amazon EKS** – In the prerequisite step for creating an Amazon VPC endpoint manually, the **Service name** in the AWS GovCloud (US) Region should be `com.amazonaws.<us-gov-east-1>.guardduty-data-fips`.


      Replace <us-gov-east-1> with your Region.
      This must be the same Region as your Amazon EC2 instance (or Amazon EKS cluster) that belongs to your AWS account ID.
      2. With the initial release of Runtime Monitoring, GuardDuty starts the support with the following security agent versions:




      	+ Amazon EKS - v1.11.1
      	+ Amazon EC2 - v1.8.0
      	+ Fargate-Amazon ECS - v1.8.0

  For more information, see [GuardDuty security agent release versions](../../../guardduty/latest/ug/runtime-monitoring-agent-release-history.md "../../../guardduty/latest/ug/runtime-monitoring-agent-release-history.md").

      1. **For Amazon EC2** – When managing the security agent manually using [Method 2 - Using Linux Package Managers](../../../guardduty/latest/ug/installing-gdu-security-agent-ec2-manually.md "../../../guardduty/latest/ug/installing-gdu-security-agent-ec2-manually.md"), use the following AWS account IDs and Regions for both RPM installation and Debian installation:




      	+ AWS GovCloud (US-East) (`us-gov-east-1`) – 383115532789
      	+ AWS GovCloud (US-West) (`us-gov-west-1`) – 383110348953
      2. **For Amazon EKS and Fargate-Amazon ECS resources**– For [Amazon ECR repository hosting GuardDuty agent](../../../guardduty/latest/ug/runtime-monitoring-ecr-repository-gdu-agent.md "../../../guardduty/latest/ug/runtime-monitoring-ecr-repository-gdu-agent.md"), use the following ECR repository for your Amazon EKS and Fargate-Amazon ECS resources:




      	+ **Amazon ECR repository for EKS resources:**



      	AWS GovCloud (US-East) - `151742754352.dkr.ecr.us-gov-east-1.amazonaws.com`



      	AWS GovCloud (US-West) - `013241004608.dkr.ecr.us-gov-west-1.amazonaws.com`
      	+ **Amazon ECR repository for Fargate-ECS resources:**



      	AWS GovCloud (US-East) - `383115532789.dkr.ecr.us-gov-east-1.amazonaws.com/aws-guardduty-agent-fargate`



      	AWS GovCloud (US-West) - `383110348953.dkr.ecr.us-gov-west-1.amazonaws.com/aws-guardduty-agent-fargate`

- The entity lists capability in [Customizing threat detection with entity lists and IP address lists](../../../guardduty/latest/ug/guardduty_upload-lists.md "../../../guardduty/latest/ug/guardduty_upload-lists.md") is not supported in AWS GovCloud (US) Regions. GuardDuty continues to support IP address lists.
- The [Extended Threat Detection](../../../guardduty/latest/ug/guardduty-extended-threat-detection.md "../../../guardduty/latest/ug/guardduty-extended-threat-detection.md") coverage for EKS clusters supports detecting multi-stage attacks through available EKS Protection finding types (EKS audit log monitoring) and AWS API activity in AWS GovCloud (US) Regions.
- The following [EKS Protection](../../../guardduty/latest/ug/kubernetes-protection.md "../../../guardduty/latest/ug/kubernetes-protection.md") (EKS audit log monitoring) finding types are not available in the AWS GovCloud (US) Regions:
  - [CredentialAccess:Kubernetes/AnomalousBehavior.SecretsAccessed](../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#credaccess-kubernetes-anomalousbehavior-secretsaccessed "../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#credaccess-kubernetes-anomalousbehavior-secretsaccessed")
  - [PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleBindingCreated](../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-rolebindingcreated "../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-rolebindingcreated")
  - [Execution:Kubernetes/AnomalousBehavior.ExecInPod](../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#execution-kubernetes-anomalousbehvaior-execinprod "../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#execution-kubernetes-anomalousbehvaior-execinprod")
  - [PrivilegeEscalation:Kubernetes/AnomalousBehavior.WorkloadDeployed!PrivilegedContainer](../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-workloaddeployed-privcontainer "../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-workloaddeployed-privcontainer")
  - [Persistence:Kubernetes/AnomalousBehavior.WorkloadDeployed!ContainerWithSensitiveMount](../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-workloaddeployed-containerwithsensitivemount "../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-workloaddeployed-containerwithsensitivemount")
  - [Execution:Kubernetes/AnomalousBehavior.WorkloadDeployed](../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#exec-kubernetes-anomalousbehavior-workloaddeployed "../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#exec-kubernetes-anomalousbehavior-workloaddeployed")
  - [PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleCreated](../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-rolecreated "../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-rolecreated")
  - [Discovery:Kubernetes/AnomalousBehavior.PermissionChecked](../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-rolecreated "../../../guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.md#privesc-kubernetes-anomalousbehavior-rolecreated")

- In [Malware Protection for EC2](../../../guardduty/latest/ug/malware-protection.md "../../../guardduty/latest/ug/malware-protection.md"), the support for scanning instances with `productCode` as `marketplace` is not supported. GuardDuty will skip the malware scan for such instances and log the skip reason as `UNSUPPORTED_PRODUCT_CODE_TYPE`.
- In [Malware Protection for Backup](../../../guardduty/latest/ug/malware-protection-backup.md "../../../guardduty/latest/ug/malware-protection-backup.md"), the scanning of EC2 and EBS Recovery points is not supported. In these cases GuardDuty will not perform a scan on the input recovery point resource.
- Cross-region data transfer is not supported in AWS GovCloud (US) Regions.
- Member accounts invitation notifications through AWS Health Dashboard and email are not supported in AWS GovCloud (US) Regions.
- In AWS GovCloud (US) Regions, AWS doesn’t use or store Customer Content processed by Amazon GuardDuty to develop and improve the service or technologies of AWS or its affiliates. Opt-out policies are currently not applicable to these Regions.

## Documentation for Amazon GuardDuty

[Amazon GuardDuty documentation](https://aws.amazon.com/documentation/guardduty/ "https://aws.amazon.com/documentation/guardduty/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.

No data will leave the AWS GovCloud (US) Regions for this service.
