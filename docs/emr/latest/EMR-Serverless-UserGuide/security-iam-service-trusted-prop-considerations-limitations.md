# Considerations and limitations for EMR Serverless Trusted-Identity-Propagation

integration

Consider the following points when you use IAM Identity Center Trusted-Identity-Propagation with EMR Serverelss Application:

- Trusted Identity Propagation through Identity Center is supported on Amazon EMR 7.8.0 and higher, and only with Apache Spark.
- Trusted Identity Propagation can only be used for [interactive workloads
  with EMR Serverless through an Apache Livy endpoint](interactive-workloads-livy-endpoints.md "interactive-workloads-livy-endpoints.md"). Interactive workloads through EMR Studio doesn't
  support Trusted Identity Propagation
- Batch jobs and streaming jobs doesn't support trusted-identity-propagation
- Fine-grained access controls using AWS Lake Formation that use Trusted Identity Propagation are available
  for [interactive workloads with EMR Serverless through
  an Apache Livy endpoint](interactive-workloads-livy-endpoints.md "interactive-workloads-livy-endpoints.md").
- Trusted Identity Propagation with Amazon EMR is supported in the following AWS Regions:
  - af-south-1 – Africa (Cape Town)
  - ap-east-1 – Asia Pacific (Hong Kong)
  - ap-northeast-1 – Asia Pacific (Tokyo)
  - ap-northeast-2 – Asia Pacific (Seoul)
  - ap-northeast-3 – Asia Pacific (Osaka)
  - ap-south-1 – Asia Pacific (Mumbai)
  - ap-southeast-1 – Asia Pacific (Singapore)
  - ap-southeast-2 – Asia Pacific (Sydney)
  - ap-southeast-3 – Asia Pacific (Jakarta)
  - ca-central-1 – Canada (Central)
  - ca-west-1 – Canada (Calgary)
  - eu-central-1 – Europe (Frankfurt)
  - eu-north-1 – Europe (Stockholm)
  - eu-south-1 – Europe (Milan)
  - eu-south-2 – Europe (Spain)
  - eu-west-1 – Europe (Ireland)
  - eu-west-2 – Europe (London)
  - eu-west-3 – Europe (Paris)
  - me-central-1 – Middle East (UAE)
  - me-south-1 – Middle East (Bahrain)
  - sa-east-1 – South America (São Paulo)
  - us-east-1 – US East (N. Virginia)
  - us-east-2 – US East (Ohio)
  - us-west-1 – US West (N. California)
  - us-west-2 – US West (Oregon)
