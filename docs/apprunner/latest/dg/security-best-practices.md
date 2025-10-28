# Security best practices for App Runner

AWS App Runner provides several security features to consider as you develop and implement your own security policies. The following best practices
are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your
environment, treat them as helpful considerations, not prescriptions.

For other App Runner security topics, see [Security in App Runner](security.md "security.md").

## Preventive security best practices

Preventive security controls attempt to prevent incidents before they occur.

### Implement least privilege access

App Runner provides AWS Identity and Access Management (IAM) managed policies for [IAM users](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-users "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-users") and the [access role](security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service.access "security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service.access"). These managed policies specify all permissions that might be
necessary for the correct operation of your App Runner service.

Your application might not require all the permissions in our managed policies. You can customize them and grant only the permissions that are
required for your users and your App Runner service to perform their tasks. This is particularly relevant to user policies, where different user roles might
have different permission needs. Implementing least privilege access is fundamental in reducing security risk and the impact that could result from
errors or malicious intent.

### Scan

your images for vulnerabilities

You can use the Amazon ECR's APIs to help identify software vulnerabilities in your container images. For more information, see the [Amazon ECR documentation](../../../AmazonECR/latest/userguide/image-scanning.md "../../../AmazonECR/latest/userguide/image-scanning.md").

## Detective security best practices

Detective security controls identify security violations after they have occurred. They can help you detect a potential security threat or
incident.

### Implement monitoring

Monitoring is an important part of maintaining the reliability, security, availability, and performance of your App Runner solutions. AWS provides
several tools and services to help you monitor your AWS services.

The following are some examples of items to monitor:

- _Amazon CloudWatch metrics for App Runner_ – Set alarms for key App Runner metrics and for your application's custom metrics. For details,
  see [Metrics (CloudWatch)](monitor-cw.md "monitor-cw.md").
- _AWS CloudTrail entries_ – Track actions that might impact availability, like `PauseService` or
  `DeleteConnection`. For details, see [API actions (CloudTrail)](monitor-ct.md "monitor-ct.md").
