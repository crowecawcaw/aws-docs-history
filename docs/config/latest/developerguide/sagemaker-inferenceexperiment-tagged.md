

# sagemaker-inferenceexperiment-tagged
<a name="sagemaker-inferenceexperiment-tagged"></a>

Checks if Amazon SageMaker Inference Experiments have tags. Optionally, required tag keys can be specified. The rule is NON\_COMPLIANT if there are no tags or if the specified tag keys are not present. The rule does not check for tags starting with 'aws:'. 



**Identifier:** SAGEMAKER\_INFERENCEEXPERIMENT\_TAGGED

**Resource Types:** AWS::SageMaker::InferenceExperiment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

requiredKeyTags (Optional)Type: CSV  
Comma-separated list of tag keys for the rule to check. If provided, the rule is NON\_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1463c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).