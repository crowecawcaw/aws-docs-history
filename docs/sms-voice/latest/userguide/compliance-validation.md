

# Compliance validation for AWS End User Messaging SMS
<a name="compliance-validation"></a>

Our new AWS sign-up experience is not designed for regulated workloads. If you're using our new AWS sign-up experience, but you want to use AWS for regulated workloads, you can [sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) or [activate advanced features](https://docs.aws.amazon.com/accounts/latest/reference/activate-advanced-features.html) for your AWS environment.

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).

## Security Assurance Program Considerations for SMS
<a name="compliance-validation-sms"></a>

The AWS End User Messaging capabilities are eligible for the security assurance programs list in [Compliance Resources](https://aws.amazon.com/compliance/resources/). This means that it is possible to build compliant solutions using SMS. For customers to build compliant solutions, they should consult their own security teams.

When dealing with sensitive data in SMS messages, it's crucial to follow relevant regulations and industry standards. While AWS provides robust security measures within our cloud environment, the responsibility for protecting data is shared with you, our customer. This shared responsibility model ensures that you have the flexibility to build solutions tailored to your specific needs, even when data leaves the AWS boundary.

While AWS End User Messaging SMS encrypts all data at rest and in transit, the final channel, such as SMS, may not be encrypted, and customers should configure any channel in a manner consistent with their requirements.