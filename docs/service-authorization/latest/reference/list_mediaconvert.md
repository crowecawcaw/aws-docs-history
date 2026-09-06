

# Actions, resources, and condition keys for AWS Elemental MediaConvert
<a name="list_mediaconvert"></a>

AWS Elemental MediaConvert (service prefix: `mediaconvert`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mediaconvert/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mediaconvert/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mediaconvert/mediaconvert.json) for this service.

**Topics**
+ [API operations defined by AWS Elemental MediaConvert](#list_mediaconvert-operations)
+ [Actions defined by AWS Elemental MediaConvert](#list_mediaconvert-actions-as-permissions)
+ [Resource types defined by AWS Elemental MediaConvert](#list_mediaconvert-resources-for-iam-policies)
+ [Condition keys for AWS Elemental MediaConvert](#list_mediaconvert-policy-keys)

## API operations defined by AWS Elemental MediaConvert
<a name="list_mediaconvert-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mediaconvert-actions-as-permissions).




- **   AssociateCertificate  **
  - **IAM action:**  [mediaconvert:AssociateCertificate](#list_mediaconvert-action-AssociateCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelJob  **
  - **IAM action:**  [mediaconvert:CancelJob](#list_mediaconvert-action-CancelJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateJob  **
  - **IAM action:**  [mediaconvert:CreateJob](#list_mediaconvert-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconvert:TagResource](#list_mediaconvert-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconvert.amazonaws.com / **Access level:** Write

- **   CreateJobTemplate  **
  - **IAM action:**  [mediaconvert:CreateJobTemplate](#list_mediaconvert-action-CreateJobTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconvert:TagResource](#list_mediaconvert-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePreset  **
  - **IAM action:**  [mediaconvert:CreatePreset](#list_mediaconvert-action-CreatePreset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconvert:TagResource](#list_mediaconvert-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateQueue  **
  - **IAM action:**  [mediaconvert:CreateQueue](#list_mediaconvert-action-CreateQueue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconvert:TagResource](#list_mediaconvert-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResourceShare  **
  - **IAM action:**  [mediaconvert:CreateResourceShare](#list_mediaconvert-action-CreateResourceShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJobTemplate  **
  - **IAM action:**  [mediaconvert:DeleteJobTemplate](#list_mediaconvert-action-DeleteJobTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicy  **
  - **IAM action:**  [mediaconvert:DeletePolicy](#list_mediaconvert-action-DeletePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePreset  **
  - **IAM action:**  [mediaconvert:DeletePreset](#list_mediaconvert-action-DeletePreset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueue  **
  - **IAM action:**  [mediaconvert:DeleteQueue](#list_mediaconvert-action-DeleteQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeEndpoints  **
  - **IAM action:**  [mediaconvert:DescribeEndpoints](#list_mediaconvert-action-DescribeEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisassociateCertificate  **
  - **IAM action:**  [mediaconvert:DisassociateCertificate](#list_mediaconvert-action-DisassociateCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetJob  **
  - **IAM action:**  [mediaconvert:GetJob](#list_mediaconvert-action-GetJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobTemplate  **
  - **IAM action:**  [mediaconvert:GetJobTemplate](#list_mediaconvert-action-GetJobTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [mediaconvert:ListJobTemplates](#list_mediaconvert-action-ListJobTemplates)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetPolicy  **
  - **IAM action:**  [mediaconvert:GetPolicy](#list_mediaconvert-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPreset  **
  - **IAM action:**  [mediaconvert:GetPreset](#list_mediaconvert-action-GetPreset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [mediaconvert:ListPresets](#list_mediaconvert-action-ListPresets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetQueue  **
  - **IAM action:**  [mediaconvert:GetQueue](#list_mediaconvert-action-GetQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListJobTemplates  **
  - **IAM action:**  [mediaconvert:ListJobTemplates](#list_mediaconvert-action-ListJobTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **IAM action:**  [mediaconvert:ListJobs](#list_mediaconvert-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPresets  **
  - **IAM action:**  [mediaconvert:ListPresets](#list_mediaconvert-action-ListPresets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQueues  **
  - **IAM action:**  [mediaconvert:ListQueues](#list_mediaconvert-action-ListQueues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [mediaconvert:ListTagsForResource](#list_mediaconvert-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVersions  **
  - **IAM action:**  [mediaconvert:ListVersions](#list_mediaconvert-action-ListVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   Probe  **
  - **IAM action:**  [mediaconvert:Probe](#list_mediaconvert-action-Probe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutPolicy  **
  - **IAM action:**  [mediaconvert:PutPolicy](#list_mediaconvert-action-PutPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchJobs  **
  - **IAM action:**  [mediaconvert:SearchJobs](#list_mediaconvert-action-SearchJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [mediaconvert:TagResource](#list_mediaconvert-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [mediaconvert:UntagResource](#list_mediaconvert-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateJobTemplate  **
  - **IAM action:**  [mediaconvert:UpdateJobTemplate](#list_mediaconvert-action-UpdateJobTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePreset  **
  - **IAM action:**  [mediaconvert:UpdatePreset](#list_mediaconvert-action-UpdatePreset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQueue  **
  - **IAM action:**  [mediaconvert:UpdateQueue](#list_mediaconvert-action-UpdateQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Elemental MediaConvert
<a name="list_mediaconvert-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateCertificate](https://docs.aws.amazon.com/mediaconvert/latest/apireference/certificates.html)  **
  - **Description:** Grants permission to associate an AWS Certificate Manager (ACM) Amazon Resource Name (ARN) with AWS Elemental MediaConvert
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelJob](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs-id.html)  **
  - **Description:** Grants permission to cancel an AWS Elemental MediaConvert job that is waiting in queue
  - **Resource types (\*required):** [Job\*](#list_mediaconvert-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateJob](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html)  **
  - **Description:** Grants permission to create and submit an AWS Elemental MediaConvert job
  - **Resource types (\*required):** [JobTemplate](#list_mediaconvert-resource-JobTemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)<br />[mediaconvert:HttpInputsAllowed](#list_mediaconvert-mediaconvert_HttpInputsAllowed)<br />[mediaconvert:HttpsInputsAllowed](#list_mediaconvert-mediaconvert_HttpsInputsAllowed)<br />[mediaconvert:S3InputsAllowed](#list_mediaconvert-mediaconvert_S3InputsAllowed)
  - **Resource types (\*required):** [Preset](#list_mediaconvert-resource-Preset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)<br />[mediaconvert:HttpInputsAllowed](#list_mediaconvert-mediaconvert_HttpInputsAllowed)<br />[mediaconvert:HttpsInputsAllowed](#list_mediaconvert-mediaconvert_HttpsInputsAllowed)<br />[mediaconvert:S3InputsAllowed](#list_mediaconvert-mediaconvert_S3InputsAllowed)
  - **Resource types (\*required):** [Queue](#list_mediaconvert-resource-Queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)<br />[mediaconvert:HttpInputsAllowed](#list_mediaconvert-mediaconvert_HttpInputsAllowed)<br />[mediaconvert:HttpsInputsAllowed](#list_mediaconvert-mediaconvert_HttpsInputsAllowed)<br />[mediaconvert:S3InputsAllowed](#list_mediaconvert-mediaconvert_S3InputsAllowed)
  - **Access level:** Write

- **   [CreateJobTemplate](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs-id.html)  **
  - **Description:** Grants permission to create an AWS Elemental MediaConvert custom job template
  - **Resource types (\*required):** [Preset](#list_mediaconvert-resource-Preset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Resource types (\*required):** [Queue](#list_mediaconvert-resource-Queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePreset](https://docs.aws.amazon.com/mediaconvert/latest/apireference/presets.html)  **
  - **Description:** Grants permission to create an AWS Elemental MediaConvert custom output preset
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Access level:** Write

- **   [CreateQueue](https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues.html)  **
  - **Description:** Grants permission to create an AWS Elemental MediaConvert job queue
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Access level:** Write

- **   [CreateResourceShare](https://docs.aws.amazon.com/mediaconvert/latest/apireference/resourceshares.html)  **
  - **Description:** Grants permission to share an AWS Elemental MediaConvert job
  - **Resource types (\*required):** [Job](#list_mediaconvert-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJobTemplate](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobtemplates-name.html)  **
  - **Description:** Grants permission to delete an AWS Elemental MediaConvert custom job template
  - **Resource types (\*required):** [JobTemplate\*](#list_mediaconvert-resource-JobTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicy](https://docs.aws.amazon.com/mediaconvert/latest/apireference/policy.html)  **
  - **Description:** Grants permission to delete an AWS Elemental MediaConvert policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePreset](https://docs.aws.amazon.com/mediaconvert/latest/apireference/presets-name.html)  **
  - **Description:** Grants permission to delete an AWS Elemental MediaConvert custom output preset
  - **Resource types (\*required):** [Preset\*](#list_mediaconvert-resource-Preset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQueue](https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues-name.html)  **
  - **Description:** Grants permission to delete an AWS Elemental MediaConvert job queue
  - **Resource types (\*required):** [Queue\*](#list_mediaconvert-resource-Queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeEndpoints](https://docs.aws.amazon.com/mediaconvert/latest/apireference/endpoints.html)  **
  - **Description:** Grants permission to subscribe to the AWS Elemental MediaConvert service, by sending a request for an account-specific endpoint. All transcoding requests must be sent to the endpoint that the service returns
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DisassociateCertificate](https://docs.aws.amazon.com/mediaconvert/latest/apireference/certificates-arn.html)  **
  - **Description:** Grants permission to remove an association between the Amazon Resource Name (ARN) of an AWS Certificate Manager (ACM) certificate and an AWS Elemental MediaConvert resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetJob](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs-id.html)  **
  - **Description:** Grants permission to get an AWS Elemental MediaConvert job
  - **Resource types (\*required):** [Job\*](#list_mediaconvert-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJobTemplate](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobtemplates-name.html)  **
  - **Description:** Grants permission to get an AWS Elemental MediaConvert job template
  - **Resource types (\*required):** [JobTemplate\*](#list_mediaconvert-resource-JobTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/mediaconvert/latest/apireference/policy.html)  **
  - **Description:** Grants permission to get an AWS Elemental MediaConvert policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPreset](https://docs.aws.amazon.com/mediaconvert/latest/apireference/presets-name.html)  **
  - **Description:** Grants permission to get an AWS Elemental MediaConvert output preset
  - **Resource types (\*required):** [Preset\*](#list_mediaconvert-resource-Preset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueue](https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues-name.html)  **
  - **Description:** Grants permission to get an AWS Elemental MediaConvert job queue
  - **Resource types (\*required):** [Queue\*](#list_mediaconvert-resource-Queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListJobTemplates](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobtemplates.html)  **
  - **Description:** Grants permission to list AWS Elemental MediaConvert job templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html)  **
  - **Description:** Grants permission to list AWS Elemental MediaConvert jobs
  - **Resource types (\*required):** [Queue](#list_mediaconvert-resource-Queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPresets](https://docs.aws.amazon.com/mediaconvert/latest/apireference/presets.html)  **
  - **Description:** Grants permission to list AWS Elemental MediaConvert output presets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListQueues](https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues.html)  **
  - **Description:** Grants permission to list AWS Elemental MediaConvert job queues
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/mediaconvert/latest/apireference/tags-arn.html)  **
  - **Description:** Grants permission to retrieve the tags for a MediaConvert queue, preset, or job template
  - **Resource types (\*required):** [Job](#list_mediaconvert-resource-Job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [JobTemplate](#list_mediaconvert-resource-JobTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Preset](#list_mediaconvert-resource-Preset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Queue](#list_mediaconvert-resource-Queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListVersions](https://docs.aws.amazon.com/mediaconvert/latest/apireference/versions.html)  **
  - **Description:** Grants permission to list AWS Elemental MediaConvert job engine versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [Probe](https://docs.aws.amazon.com/mediaconvert/latest/apireference/probe.html)  **
  - **Description:** Grants permission to probe a file
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutPolicy](https://docs.aws.amazon.com/mediaconvert/latest/apireference/policy.html)  **
  - **Description:** Grants permission to put an AWS Elemental MediaConvert policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SearchJobs](https://docs.aws.amazon.com/mediaconvert/latest/apireference/search.html)  **
  - **Description:** Grants permission to search AWS Elemental MediaConvert jobs
  - **Resource types (\*required):** [Queue](#list_mediaconvert-resource-Queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/mediaconvert/latest/apireference/tags.html)  **
  - **Description:** Grants permission to add tags to a MediaConvert queue, preset, or job template
  - **Resource types (\*required):** [Job](#list_mediaconvert-resource-Job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Resource types (\*required):** [JobTemplate](#list_mediaconvert-resource-JobTemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Resource types (\*required):** [Preset](#list_mediaconvert-resource-Preset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Resource types (\*required):** [Queue](#list_mediaconvert-resource-Queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconvert-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/mediaconvert/latest/apireference/tags-arn.html)  **
  - **Description:** Grants permission to remove tags from a MediaConvert queue, preset, or job template
  - **Resource types (\*required):** [Job](#list_mediaconvert-resource-Job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Resource types (\*required):** [JobTemplate](#list_mediaconvert-resource-JobTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Resource types (\*required):** [Preset](#list_mediaconvert-resource-Preset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Resource types (\*required):** [Queue](#list_mediaconvert-resource-Queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconvert-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateJobTemplate](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobtemplates-name.html)  **
  - **Description:** Grants permission to update an AWS Elemental MediaConvert custom job template
  - **Resource types (\*required):** [JobTemplate\*](#list_mediaconvert-resource-JobTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Preset](#list_mediaconvert-resource-Preset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Queue](#list_mediaconvert-resource-Queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePreset](https://docs.aws.amazon.com/mediaconvert/latest/apireference/presets-name.html)  **
  - **Description:** Grants permission to update an AWS Elemental MediaConvert custom output preset
  - **Resource types (\*required):** [Preset\*](#list_mediaconvert-resource-Preset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateQueue](https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues-name.html)  **
  - **Description:** Grants permission to update an AWS Elemental MediaConvert job queue
  - **Resource types (\*required):** [Queue\*](#list_mediaconvert-resource-Queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Elemental MediaConvert
<a name="list_mediaconvert-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [CertificateAssociation](https://docs.aws.amazon.com/mediaconvert/latest/apireference/certificates.html)  | arn:${Partition}:mediaconvert:${Region}:${Account}:certificates/${CertificateArn} |   | 
|  [Job](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html)  | arn:${Partition}:mediaconvert:${Region}:${Account}:jobs/${JobId} | [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_) | 
|  [JobTemplate](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobtemplates.html)  | arn:${Partition}:mediaconvert:${Region}:${Account}:jobTemplates/${JobTemplateName} | [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_) | 
|  [Preset](https://docs.aws.amazon.com/mediaconvert/latest/apireference/presets.html)  | arn:${Partition}:mediaconvert:${Region}:${Account}:presets/${PresetName} | [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_) | 
|  [Queue](https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues.html)  | arn:${Partition}:mediaconvert:${Region}:${Account}:queues/${QueueName} | [aws:ResourceTag/${TagKey}](#list_mediaconvert-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Elemental MediaConvert
<a name="list_mediaconvert-policy-keys"></a>

AWS Elemental MediaConvert defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/mediaconvert/latest/apireference/tags.html)  | Filters access by tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/mediaconvert/latest/apireference/tags.html)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/mediaconvert/latest/apireference/tags.html)  | Filters access by tag keys in the request | ArrayOfString | 
|   [mediaconvert:HttpInputsAllowed](https://docs.aws.amazon.com/mediaconvert/latest/apireference/input-policies.html)  | Filters access by an HTTP input policy present in the account | Bool | 
|   [mediaconvert:HttpsInputsAllowed](https://docs.aws.amazon.com/mediaconvert/latest/apireference/input-policies.html)  | Filters access by an HTTPS input policy present in the account | Bool | 
|   [mediaconvert:S3InputsAllowed](https://docs.aws.amazon.com/mediaconvert/latest/apireference/input-policies.html)  | Filters access by an S3 input policy present in the account | Bool | 