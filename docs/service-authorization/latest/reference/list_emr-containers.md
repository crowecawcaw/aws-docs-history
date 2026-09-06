

# Actions, resources, and condition keys for Amazon EMR on EKS (EMR Containers)
<a name="list_emr-containers"></a>

Amazon EMR on EKS (EMR Containers) (service prefix: `emr-containers`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/emr-containers/emr-containers.json) for this service.

**Topics**
+ [API operations defined by Amazon EMR on EKS (EMR Containers)](#list_emr-containers-operations)
+ [Actions defined by Amazon EMR on EKS (EMR Containers)](#list_emr-containers-actions-as-permissions)
+ [Resource types defined by Amazon EMR on EKS (EMR Containers)](#list_emr-containers-resources-for-iam-policies)
+ [Condition keys for Amazon EMR on EKS (EMR Containers)](#list_emr-containers-policy-keys)

## API operations defined by Amazon EMR on EKS (EMR Containers)
<a name="list_emr-containers-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_emr-containers-actions-as-permissions).




- **   CancelJobRun  **
  - **IAM action:**  [emr-containers:CancelJobRun](#list_emr-containers-action-CancelJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateJobTemplate  **
  - **IAM action:**  [emr-containers:CreateJobTemplate](#list_emr-containers-action-CreateJobTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [emr-containers:TagResource](#list_emr-containers-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateManagedEndpoint  **
  - **IAM action:**  [emr-containers:CreateManagedEndpoint](#list_emr-containers-action-CreateManagedEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [emr-containers:TagResource](#list_emr-containers-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ec2:AuthorizeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:AuthorizeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:CreateSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:DeleteSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSecurityGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:RevokeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:RevokeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** pods.eks.amazonaws.com / **Access level:** Write

- **   CreateSecurityConfiguration  **
  - **IAM action:**  [emr-containers:CreateSecurityConfiguration](#list_emr-containers-action-CreateSecurityConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [emr-containers:TagResource](#list_emr-containers-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVirtualCluster  **
  - **IAM action:**  [emr-containers:CreateVirtualCluster](#list_emr-containers-action-CreateVirtualCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [emr-containers:TagResource](#list_emr-containers-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteJobTemplate  **
  - **IAM action:**  [emr-containers:DeleteJobTemplate](#list_emr-containers-action-DeleteJobTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteManagedEndpoint  **
  - **IAM action:**  [emr-containers:DeleteManagedEndpoint](#list_emr-containers-action-DeleteManagedEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:DeleteSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSecurityGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:RevokeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:RevokeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteSecurityConfiguration  **
  - **IAM action:**  [emr-containers:DeleteSecurityConfiguration](#list_emr-containers-action-DeleteSecurityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVirtualCluster  **
  - **IAM action:**  [emr-containers:DeleteVirtualCluster](#list_emr-containers-action-DeleteVirtualCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:AssociateAccessPolicy](https://docs.aws.amazon.com/eks/latest/APIReference/API_AssociateAccessPolicy.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:DeleteAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteAccessEntry.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:DescribeAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAccessEntry.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [eks:DisassociateAccessPolicy](https://docs.aws.amazon.com/eks/latest/APIReference/API_DisassociateAccessPolicy.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:ListAssociatedAccessPolicies](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAssociatedAccessPolicies.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeJobRun  **
  - **IAM action:**  [emr-containers:DescribeJobRun](#list_emr-containers-action-DescribeJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobTemplate  **
  - **IAM action:**  [emr-containers:DescribeJobTemplate](#list_emr-containers-action-DescribeJobTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeManagedEndpoint  **
  - **IAM action:**  [emr-containers:DescribeManagedEndpoint](#list_emr-containers-action-DescribeManagedEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSecurityConfiguration  **
  - **IAM action:**  [emr-containers:DescribeSecurityConfiguration](#list_emr-containers-action-DescribeSecurityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVirtualCluster  **
  - **IAM action:**  [emr-containers:DescribeVirtualCluster](#list_emr-containers-action-DescribeVirtualCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedEndpointSessionCredentials  **
  - **IAM action:**  [emr-containers:GetManagedEndpointSessionCredentials](#list_emr-containers-action-GetManagedEndpointSessionCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListJobRuns  **
  - **IAM action:**  [emr-containers:ListJobRuns](#list_emr-containers-action-ListJobRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobTemplates  **
  - **IAM action:**  [emr-containers:ListJobTemplates](#list_emr-containers-action-ListJobTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedEndpoints  **
  - **IAM action:**  [emr-containers:ListManagedEndpoints](#list_emr-containers-action-ListManagedEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSecurityConfigurations  **
  - **IAM action:**  [emr-containers:ListSecurityConfigurations](#list_emr-containers-action-ListSecurityConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [emr-containers:ListTagsForResource](#list_emr-containers-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVirtualClusters  **
  - **IAM action:**  [emr-containers:ListVirtualClusters](#list_emr-containers-action-ListVirtualClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartJobRun  **
  - **IAM action:**  [emr-containers:DescribeJobTemplate](#list_emr-containers-action-DescribeJobTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [emr-containers:StartJobRun](#list_emr-containers-action-StartJobRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [emr-containers:TagResource](#list_emr-containers-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** pods.eks.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [emr-containers:TagResource](#list_emr-containers-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [emr-containers:UntagResource](#list_emr-containers-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by Amazon EMR on EKS (EMR Containers)
<a name="list_emr-containers-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CancelJobRun.html)  **
  - **Description:** Grants permission to cancel a job run
  - **Resource types (\*required):** [jobRun\*](#list_emr-containers-resource-jobRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCertificate](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateCertificate.html)  **
  - **Description:** Grants permission to call the CreateCertificate method to accept the CertificateSigningRequest, and return the signed certificate
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateJobTemplate](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateJobTemplate.html)  **
  - **Description:** Grants permission to create a job template
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Access level:** Write

- **   [CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html)  **
  - **Description:** Grants permission to create a managed endpoint
  - **Resource types (\*required):** [virtualCluster\*](#list_emr-containers-resource-virtualCluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)<br />[emr-containers:ExecutionRoleArn](#list_emr-containers-emr-containers_ExecutionRoleArn)
  - **Access level:** Write

- **   [CreateSecurityConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateSecurityConfiguration.html)  **
  - **Description:** Grants permission to create a security configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVirtualCluster](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateVirtualCluster.html)  **
  - **Description:** Grants permission to create a virtual cluster
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteJobTemplate](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DeleteJobTemplate.html)  **
  - **Description:** Grants permission to delete a job template
  - **Resource types (\*required):** [jobTemplate\*](#list_emr-containers-resource-jobTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DeleteManagedEndpoint.html)  **
  - **Description:** Grants permission to delete a managed endpoint
  - **Resource types (\*required):** [managedEndpoint\*](#list_emr-containers-resource-managedEndpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSecurityConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DeleteSecurityConfiguration.html)  **
  - **Description:** Grants permission to delete a security configuration
  - **Resource types (\*required):** [securityConfiguration\*](#list_emr-containers-resource-securityConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVirtualCluster](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DeleteVirtualCluster.html)  **
  - **Description:** Grants permission to delete a virtual cluster
  - **Resource types (\*required):** [virtualCluster\*](#list_emr-containers-resource-virtualCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeJobRun.html)  **
  - **Description:** Grants permission to describe a job run
  - **Resource types (\*required):** [jobRun\*](#list_emr-containers-resource-jobRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJobTemplate](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeJobTemplate.html)  **
  - **Description:** Grants permission to describe a job template
  - **Resource types (\*required):** [jobTemplate\*](#list_emr-containers-resource-jobTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeManagedEndpoint.html)  **
  - **Description:** Grants permission to describe a managed endpoint
  - **Resource types (\*required):** [managedEndpoint\*](#list_emr-containers-resource-managedEndpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSecurityConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeSecurityConfiguration.html)  **
  - **Description:** Grants permission to describe a security configuration
  - **Resource types (\*required):** [securityConfiguration\*](#list_emr-containers-resource-securityConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVirtualCluster](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeVirtualCluster.html)  **
  - **Description:** Grants permission to describe a virtual cluster
  - **Resource types (\*required):** [virtualCluster\*](#list_emr-containers-resource-virtualCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetManagedEndpointSessionCredentials](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_GetManagedEndpointSessionCredentials.html)  **
  - **Description:** Grants permission to generate a session token used to connect to a managed endpoint
  - **Resource types (\*required):** [managedEndpoint\*](#list_emr-containers-resource-managedEndpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListJobRuns](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListJobRuns.html)  **
  - **Description:** Grants permission to list job runs associated with a virtual cluster
  - **Resource types (\*required):** [virtualCluster\*](#list_emr-containers-resource-virtualCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListJobTemplates](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListJobTemplates.html)  **
  - **Description:** Grants permission to list job templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedEndpoints](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListManagedEndpoints.html)  **
  - **Description:** Grants permission to list managed endpoints associated with a virtual cluster
  - **Resource types (\*required):** [virtualCluster\*](#list_emr-containers-resource-virtualCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSecurityConfigurations](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListSecurityConfigurations.html)  **
  - **Description:** Grants permission to list security configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for the specified resource
  - **Resource types (\*required):** [jobRun](#list_emr-containers-resource-jobRun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [jobTemplate](#list_emr-containers-resource-jobTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [managedEndpoint](#list_emr-containers-resource-managedEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securityConfiguration](#list_emr-containers-resource-securityConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualCluster](#list_emr-containers-resource-virtualCluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVirtualClusters](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListVirtualClusters.html)  **
  - **Description:** Grants permission to list virtual clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html)  **
  - **Description:** Grants permission to start a job run
  - **Resource types (\*required):** [virtualCluster\*](#list_emr-containers-resource-virtualCluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)<br />[emr-containers:ExecutionRoleArn](#list_emr-containers-emr-containers_ExecutionRoleArn)<br />[emr-containers:JobTemplateArn](#list_emr-containers-emr-containers_JobTemplateArn)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag the specified resource
  - **Resource types (\*required):** [jobRun](#list_emr-containers-resource-jobRun) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Resource types (\*required):** [jobTemplate](#list_emr-containers-resource-jobTemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Resource types (\*required):** [managedEndpoint](#list_emr-containers-resource-managedEndpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Resource types (\*required):** [securityConfiguration](#list_emr-containers-resource-securityConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Resource types (\*required):** [virtualCluster](#list_emr-containers-resource-virtualCluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-containers-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag the specified resource
  - **Resource types (\*required):** [jobRun](#list_emr-containers-resource-jobRun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Resource types (\*required):** [jobTemplate](#list_emr-containers-resource-jobTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Resource types (\*required):** [managedEndpoint](#list_emr-containers-resource-managedEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Resource types (\*required):** [securityConfiguration](#list_emr-containers-resource-securityConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Resource types (\*required):** [virtualCluster](#list_emr-containers-resource-virtualCluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-containers-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by Amazon EMR on EKS (EMR Containers)
<a name="list_emr-containers-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [jobRun](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs.html)  | arn:${Partition}:emr-containers:${Region}:${Account}:/virtualclusters/${VirtualClusterId}/jobruns/${JobRunId} | [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_) | 
|  [jobTemplate](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-templates.html)  | arn:${Partition}:emr-containers:${Region}:${Account}:/jobtemplates/${JobTemplateId} | [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_) | 
|  [managedEndpoint](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-eks-cluster.html#emr-studio-create-managed-endpoint)  | arn:${Partition}:emr-containers:${Region}:${Account}:/virtualclusters/${VirtualClusterId}/endpoints/${EndpointId} | [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_) | 
|  [securityConfiguration](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_fgac-lf-enable.html#security_iam_fgac-lf-security-config)  | arn:${Partition}:emr-containers:${Region}:${Account}:/securityconfigurations/${SecurityConfigurationId} | [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_) | 
|  [virtualCluster](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/virtual-cluster.html)  | arn:${Partition}:emr-containers:${Region}:${Account}:/virtualclusters/${VirtualClusterId} | [aws:ResourceTag/${TagKey}](#list_emr-containers-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon EMR on EKS (EMR Containers)
<a name="list_emr-containers-policy-keys"></a>

Amazon EMR on EKS (EMR Containers) defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs present in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys present in the request | ArrayOfString | 
|   [emr-containers:ExecutionRoleArn](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/iam-execution-role.html)  | Filters access by the execution role arn present in the request | ARN | 
|   [emr-containers:JobTemplateArn](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/iam-job-template.html)  | Filters access by the job template arn present in the request | ARN | 