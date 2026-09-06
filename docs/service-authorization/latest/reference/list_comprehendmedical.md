

# Actions, resources, and condition keys for Amazon Comprehend Medical
<a name="list_comprehendmedical"></a>

Amazon Comprehend Medical (service prefix: `comprehendmedical`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/comprehend-medical/latest/dev/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/comprehend-medical/latest/api/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/comprehend-medical/latest/dev/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/comprehendmedical/comprehendmedical.json) for this service.

**Topics**
+ [API operations defined by Amazon Comprehend Medical](#list_comprehendmedical-operations)
+ [Actions defined by Amazon Comprehend Medical](#list_comprehendmedical-actions-as-permissions)
+ [Resource types defined by Amazon Comprehend Medical](#list_comprehendmedical-resources-for-iam-policies)
+ [Condition keys for Amazon Comprehend Medical](#list_comprehendmedical-policy-keys)

## API operations defined by Amazon Comprehend Medical
<a name="list_comprehendmedical-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_comprehendmedical-actions-as-permissions).




- **   DescribeEntitiesDetectionV2Job  **
  - **IAM action:**  [comprehendmedical:DescribeEntitiesDetectionV2Job](#list_comprehendmedical-action-DescribeEntitiesDetectionV2Job) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeICD10CMInferenceJob  **
  - **IAM action:**  [comprehendmedical:DescribeICD10CMInferenceJob](#list_comprehendmedical-action-DescribeICD10CMInferenceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePHIDetectionJob  **
  - **IAM action:**  [comprehendmedical:DescribePHIDetectionJob](#list_comprehendmedical-action-DescribePHIDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRxNormInferenceJob  **
  - **IAM action:**  [comprehendmedical:DescribeRxNormInferenceJob](#list_comprehendmedical-action-DescribeRxNormInferenceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSNOMEDCTInferenceJob  **
  - **IAM action:**  [comprehendmedical:DescribeSNOMEDCTInferenceJob](#list_comprehendmedical-action-DescribeSNOMEDCTInferenceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectEntitiesV2  **
  - **IAM action:**  [comprehendmedical:DetectEntitiesV2](#list_comprehendmedical-action-DetectEntitiesV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectPHI  **
  - **IAM action:**  [comprehendmedical:DetectPHI](#list_comprehendmedical-action-DetectPHI) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InferICD10CM  **
  - **IAM action:**  [comprehendmedical:InferICD10CM](#list_comprehendmedical-action-InferICD10CM) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InferRxNorm  **
  - **IAM action:**  [comprehendmedical:InferRxNorm](#list_comprehendmedical-action-InferRxNorm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InferSNOMEDCT  **
  - **IAM action:**  [comprehendmedical:InferSNOMEDCT](#list_comprehendmedical-action-InferSNOMEDCT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEntitiesDetectionV2Jobs  **
  - **IAM action:**  [comprehendmedical:ListEntitiesDetectionV2Jobs](#list_comprehendmedical-action-ListEntitiesDetectionV2Jobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListICD10CMInferenceJobs  **
  - **IAM action:**  [comprehendmedical:ListICD10CMInferenceJobs](#list_comprehendmedical-action-ListICD10CMInferenceJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPHIDetectionJobs  **
  - **IAM action:**  [comprehendmedical:ListPHIDetectionJobs](#list_comprehendmedical-action-ListPHIDetectionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRxNormInferenceJobs  **
  - **IAM action:**  [comprehendmedical:ListRxNormInferenceJobs](#list_comprehendmedical-action-ListRxNormInferenceJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSNOMEDCTInferenceJobs  **
  - **IAM action:**  [comprehendmedical:ListSNOMEDCTInferenceJobs](#list_comprehendmedical-action-ListSNOMEDCTInferenceJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartEntitiesDetectionV2Job  **
  - **IAM action:**  [comprehendmedical:StartEntitiesDetectionV2Job](#list_comprehendmedical-action-StartEntitiesDetectionV2Job)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehendmedical.amazonaws.com / **Access level:** Write

- **   StartICD10CMInferenceJob  **
  - **IAM action:**  [comprehendmedical:StartICD10CMInferenceJob](#list_comprehendmedical-action-StartICD10CMInferenceJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehendmedical.amazonaws.com / **Access level:** Write

- **   StartPHIDetectionJob  **
  - **IAM action:**  [comprehendmedical:StartPHIDetectionJob](#list_comprehendmedical-action-StartPHIDetectionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehendmedical.amazonaws.com / **Access level:** Write

- **   StartRxNormInferenceJob  **
  - **IAM action:**  [comprehendmedical:StartRxNormInferenceJob](#list_comprehendmedical-action-StartRxNormInferenceJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehendmedical.amazonaws.com / **Access level:** Write

- **   StartSNOMEDCTInferenceJob  **
  - **IAM action:**  [comprehendmedical:StartSNOMEDCTInferenceJob](#list_comprehendmedical-action-StartSNOMEDCTInferenceJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehendmedical.amazonaws.com / **Access level:** Write

- **   StopEntitiesDetectionV2Job  **
  - **IAM action:**  [comprehendmedical:StopEntitiesDetectionV2Job](#list_comprehendmedical-action-StopEntitiesDetectionV2Job) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopICD10CMInferenceJob  **
  - **IAM action:**  [comprehendmedical:StopICD10CMInferenceJob](#list_comprehendmedical-action-StopICD10CMInferenceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopPHIDetectionJob  **
  - **IAM action:**  [comprehendmedical:StopPHIDetectionJob](#list_comprehendmedical-action-StopPHIDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopRxNormInferenceJob  **
  - **IAM action:**  [comprehendmedical:StopRxNormInferenceJob](#list_comprehendmedical-action-StopRxNormInferenceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopSNOMEDCTInferenceJob  **
  - **IAM action:**  [comprehendmedical:StopSNOMEDCTInferenceJob](#list_comprehendmedical-action-StopSNOMEDCTInferenceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Comprehend Medical
<a name="list_comprehendmedical-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DescribeEntitiesDetectionV2Job](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribeEntitiesDetectionV2Job.html)  | Grants permission to describe the properties of a medical entity detection job that you have submitted |  |   | Read | 
|   [DescribeICD10CMInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribeICD10CMInferenceJob.html)  | Grants permission to describe the properties of an ICD-10-CM linking job that you have submitted |  |   | Read | 
|   [DescribePHIDetectionJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribePHIDetectionJob.html)  | Grants permission to describe the properties of a PHI entity detection job that you have submitted |  |   | Read | 
|   [DescribeRxNormInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribeRxNormInferenceJob.html)  | Grants permission to describe the properties of an RxNorm linking job that you have submitted |  |   | Read | 
|   [DescribeSNOMEDCTInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribeSNOMEDCTInferenceJob.html)  | Grants permission to describe the properties of a SNOMED-CT linking job that you have submitted |  |   | Read | 
|   [DetectEntitiesV2](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DetectEntitiesV2.html)  | Grants permission to detect the named medical entities, and their relationships and traits within the given text document |  |   | Read | 
|   [DetectPHI](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DetectPHI.html)  | Grants permission to detect the protected health information (PHI) entities within the given text document |  |   | Read | 
|   [InferICD10CM](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InferICD10CM.html)  | Grants permission to detect the medical condition entities within the given text document and link them to ICD-10-CM codes |  |   | Read | 
|   [InferRxNorm](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InferRxNorm.html)  | Grants permission to detect the medication entities within the given text document and link them to RxCUI concept identifiers from the National Library of Medicine RxNorm database |  |   | Read | 
|   [InferSNOMEDCT](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InferSNOMEDCT.html)  | Grants permission to detect the medical condition, anatomy, and test, treatment, and procedure entities within the given text document and link them to SNOMED-CT codes |  |   | Read | 
|   [ListEntitiesDetectionV2Jobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListEntitiesDetectionV2Jobs.html)  | Grants permission to list the medical entity detection jobs that you have submitted |  |   | Read | 
|   [ListICD10CMInferenceJobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListICD10CMInferenceJobs.html)  | Grants permission to list the ICD-10-CM linking jobs that you have submitted |  |   | Read | 
|   [ListPHIDetectionJobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListPHIDetectionJobs.html)  | Grants permission to list the PHI entity detection jobs that you have submitted |  |   | Read | 
|   [ListRxNormInferenceJobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListRxNormInferenceJobs.html)  | Grants permission to list the RxNorm linking jobs that you have submitted |  |   | Read | 
|   [ListSNOMEDCTInferenceJobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListSNOMEDCTInferenceJobs.html)  | Grants permission to list the SNOMED-CT linking jobs that you have submitted |  |   | Read | 
|   [StartEntitiesDetectionV2Job](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartEntitiesDetectionV2Job.html)  | Grants permission to start an asynchronous medical entity detection job for a collection of documents |  |   | Write | 
|   [StartICD10CMInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartICD10CMInferenceJob.html)  | Grants permission to start an asynchronous ICD-10-CM linking job for a collection of documents |  |   | Write | 
|   [StartPHIDetectionJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartPHIDetectionJob.html)  | Grants permission to start an asynchronous PHI entity detection job for a collection of documents |  |   | Write | 
|   [StartRxNormInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartRxNormInferenceJob.html)  | Grants permission to start an asynchronous RxNorm linking job for a collection of documents |  |   | Write | 
|   [StartSNOMEDCTInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartSNOMEDCTInferenceJob.html)  | Grants permission to start an asynchronous SNOMED-CT linking job for a collection of documents |  |   | Write | 
|   [StopEntitiesDetectionV2Job](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopEntitiesDetectionV2Job.html)  | Grants permission to stop a medical entity detection job |  |   | Write | 
|   [StopICD10CMInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopICD10CMInferenceJob.html)  | Grants permission to stop an ICD-10-CM linking job |  |   | Write | 
|   [StopPHIDetectionJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopPHIDetectionJob.html)  | Grants permission to stop a PHI entity detection job |  |   | Write | 
|   [StopRxNormInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopRxNormInferenceJob.html)  | Grants permission to stop an RxNorm linking job |  |   | Write | 
|   [StopSNOMEDCTInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopSNOMEDCTInferenceJob.html)  | Grants permission to stop a SNOMED-CT linking job |  |   | Write | 

## Resource types defined by Amazon Comprehend Medical
<a name="list_comprehendmedical-resources-for-iam-policies"></a>

Amazon Comprehend Medical does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon Comprehend Medical
<a name="list_comprehendmedical-policy-keys"></a>

Amazon Comprehend Medical defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 