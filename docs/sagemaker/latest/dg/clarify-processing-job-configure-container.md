# Prebuilt SageMaker Clarify

Containers

Amazon SageMaker AI provides prebuilt SageMaker Clarify container images that include the libraries and other
dependencies needed to compute bias metrics and feature attributions for explainability.
These images are capable of running SageMaker Clarify [processing jobs](processing-job.md "processing-job.md") in your account.

The image URIs for the containers are in the following form:

```
`<ACCOUNT_ID>`.dkr.ecr.`<REGION_NAME>`.amazonaws.com/sagemaker-clarify-processing:1.0
```

For example:

```
`111122223333`.dkr.ecr.us-east-1.amazonaws.com/sagemaker-clarify-processing:1.0
```

The following table lists the addresses by AWS Region.

Docker Images for SageMaker Clarify Processing Jobs

| Region                    | Image address                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | 205585389593.dkr.ecr.us-east-1.amazonaws.com/sagemaker-clarify-processing:1.0         |
| US East (Ohio)            | 211330385671.dkr.ecr.us-east-2.amazonaws.com/sagemaker-clarify-processing:1.0         |
| US West (N. California)   | 740489534195.dkr.ecr.us-west-1.amazonaws.com/sagemaker-clarify-processing:1.0         |
| US West (Oregon)          | 306415355426.dkr.ecr.us-west-2.amazonaws.com/sagemaker-clarify-processing:1.0         |
| Asia Pacific (Hong Kong)  | 098760798382.dkr.ecr.ap-east-1.amazonaws.com/sagemaker-clarify-processing:1.0         |
| Asia Pacific (Mumbai)     | 452307495513.dkr.ecr.ap-south-1.amazonaws.com/sagemaker-clarify-processing:1.0        |
| Asia Pacific (Jakarta)    | 705930551576.dkr.ecr.ap-southeast-3.amazonaws.com/sagemaker-clarify-processing:1.0    |
| Asia Pacific (Tokyo)      | 377024640650.dkr.ecr.ap-northeast-1.amazonaws.com/sagemaker-clarify-processing:1.0    |
| Asia Pacific (Seoul)      | 263625296855.dkr.ecr.ap-northeast-2.amazonaws.com/sagemaker-clarify-processing:1.0    |
| Asia Pacific (Osaka)      | 912233562940.dkr.ecr.ap-northeast-3.amazonaws.com/sagemaker-clarify-processing:1.0    |
| Asia Pacific (Singapore)  | 834264404009.dkr.ecr.ap-southeast-1.amazonaws.com/sagemaker-clarify-processing:1.0    |
| Asia Pacific (Sydney)     | 007051062584.dkr.ecr.ap-southeast-2.amazonaws.com/sagemaker-clarify-processing:1.0    |
| Canada (Central)          | 675030665977.dkr.ecr.ca-central-1.amazonaws.com/sagemaker-clarify-processing:1.0      |
| Europe (Frankfurt)        | 017069133835.dkr.ecr.eu-central-1.amazonaws.com/sagemaker-clarify-processing:1.0      |
| Europe (Zurich)           | 730335477804.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-clarify-processing:1.0      |
| Europe (Ireland)          | 131013547314.dkr.ecr.eu-west-1.amazonaws.com/sagemaker-clarify-processing:1.0         |
| Europe (London)           | 440796970383.dkr.ecr.eu-west-2.amazonaws.com/sagemaker-clarify-processing:1.0         |
| Europe (Paris)            | 341593696636.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-clarify-processing:1.0         |
| Europe (Stockholm)        | 763603941244.dkr.ecr.eu-north-1.amazonaws.com/sagemaker-clarify-processing:1.0        |
| Middle East (Bahrain)     | 835444307964.dkr.ecr.me-south-1.amazonaws.com/sagemaker-clarify-processing:1.0        |
| South America (São Paulo) | 520018980103.dkr.ecr.sa-east-1.amazonaws.com/sagemaker-clarify-processing:1.0         |
| Africa (Cape Town)        | 811711786498.dkr.ecr.af-south-1.amazonaws.com/sagemaker-clarify-processing:1.0        |
| Europe (Milan)            | 638885417683.dkr.ecr.eu-south-1.amazonaws.com/sagemaker-clarify-processing:1.0        |
| China (Beijing)           | 122526803553.dkr.ecr.cn-north-1.amazonaws.com.cn/sagemaker-clarify-processing:1.0     |
| China (Ningxia)           | 122578899357.dkr.ecr.cn-northwest-1.amazonaws.com.cn/sagemaker-clarify-processing:1.0 |
