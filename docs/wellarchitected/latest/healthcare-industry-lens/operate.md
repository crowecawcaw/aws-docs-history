# Operate

| HCL_OPS5. How do you demonstrate<br>continuous compliance? |
| ---------------------------------------------------------- |
|                                                            |

**Partition workloads
involving sensitive data into separate
environments**

Minimize access to sensitive data by isolating workloads to
separate environments requiring additional controls for
access. Segmenting can be done by AWS accounts, VPCs, or Amazon Simple Storage Service buckets. Minimize
using sensitive data in non-production environments.

**Architect and build with
the ability to generate evidence that demonstrate continuous
compliance**

Healthcare organizations must be able to demonstrate their
compliance posture.  Evidence that includes the safeguards
used to protect sensitive healthcare data, as well as the
documented policies and procedures, can all be used to
demonstrate compliance. The cloud services used to architect a
compliant foundation in the cloud, can also be used to gather
the necessary evidence to demonstrate compliance posture. For
example, using infrastructure as code, coupled with a software
development lifecycle, can demonstrate a mature change
management process, which is an important compliance control.
Being able to demonstrate the full scope of a compliance
posture is critical for all stakeholders, whether that is an
organizations leadership, shareholders, customers, and
patients.

There are several key concepts to consider when building out a
continuous compliance posture. While AWS cannot assure
compliance for your environment per the shared responsibility
model, the following approach will make it easier for your
organization to demonstrate compliance on AWS. In general, use
managed services from AWS or third-party solutions, such as
those available in AWS Marketplace, to simplify your approach.

**Identify resources in
the cloud environment**

An accurate representation of your cloud environments is
necessary to demonstrate continuous compliance. Understand
what AWS resources exist and how they interact with each
other. AWS Config will help you identify these resources and
how they are configured. Use distributed tracing solutions,
such as AWS X-Ray, to understand how components of your system
interact, and to map network accessibility between different
resources in your environment.

**Restrict resources and
applications to pre-defined configurations**

Coupling AWS Config with infrastructure as code will allow you
to test application configurations before they are deployed in
your environment. Apply governance to your AWS deployments
using infrastructure as code tools like AWS CloudFormation,
AWS Cloud Development Kit (AWS CDK), Terraform, and Service Catalog. Verify that all configurations are
_secure-by-default_ with best practices
around encryption, logging, and least privilege.

**Implement
compliance-as-code for configuration**

For each configuration you specify, test the controls you put
in place. Use AWS Config as the central location to evaluate
configuration changes. Where possible, use AWS Config managed
rules, but also implement custom evaluations with AWS Lambda,
fully capturing environment configuration. Configuration
triggers will also shorten the time to identify AWS resources
that are out of compliance compared to periodic triggers. This
helps you demonstrate your compliance posture by automatically
building and maintaining a list of resources within your AWS
environment. It also allows you to continuously evaluate your
compliance posture against the technical controls identified
by your organization. For example, you can create an AWS Config rule that marks an Amazon S3 bucket as non-compliant if
server-side encryption is not enabled or the Amazon S3 bucket
policy allows unencrypted uploads. AWS provides
[sample
rules bundled into conformance packs](../../../config/latest/developerguide/conformancepack-sample-templates.md "../../../config/latest/developerguide/conformancepack-sample-templates.md") that align with
many common regulatory frameworks and best practices, allowing
you to start creating a compliance monitoring solution.

**Centralize security and
compliance findings**

Many customers will use multiple AWS accounts (such as
development, test, and prod, or department-specific accounts).
Configuration management, while important, is not the only set
of technical controls you may require. For example, you may
combine your configuration posture with additional findings,
from third-party solutions or AWS security services like
Amazon GuardDuty. Technical controls and findings should be
grouped together as evidence using a solution such as AWS Security Hub CSPM.

**Map technical controls
to compliance requirements using automation.**

Simplify maintaining a complete view of your compliance
posture by automatically mapping controls and findings to your
internal policies. For example, if you have a compliance
policy around encryption at-rest, you may have individual
controls on the configuration of each AWS resource to verify
encryption is enabled.

AWS Audit Manager helps automate evidence collection from a
variety of sources within AWS, including Security Hub CSPM and
Config. Bundling multiple pieces of evidence together under a
single policy makes it easier to demonstrate compliance with a
specific framework or regulation. You can use Audit Manager’s
prebuilt frameworks, and you can manually specify a list of
controls and policies that are important to your organization.

**Use up-to-date
artifacts.**

The creation of artifacts that document the compliance posture
of a cloud environment should be automated. Use services such
as AWS Config, AWS Audit Manager, and AWS Security Hub CSPM to
automatically collect and report the compliance state of a
cloud environment.

| HCL_OPS6. How do you automate<br>remediation of compliance violations? |
| ---------------------------------------------------------------------- |
|                                                                        |

There are several key concepts to consider when creating an
automated remediation solution. While your organization is
responsible for compliance for your environment, per the
shared responsibility model, the following approach will make
it easier to demonstrate compliance on AWS. In general, use
managed services either from AWS or a third-party solution,
such as one available in AWS Marketplace, to simplify your
approach.  Similar to the recommendations for demonstrating
continuous compliance, define compliance requirements and
create associated policies and procedures for remediation
before creating the remediation solution.

**Automate remediation
actions for non-compliant resources**

Automate remediation of configurations that are out of
compliance with your technical controls for rapid, consistent
application of your policies. Event-driven architectures
improve remediation times. Not everything can be predicted
ahead of time. Certain remediations may be manual at first,
but investigated when they occur and automated when possible
in future occurrences.

In developing automated remediations, there are several steps
you can follow:

1. **Specify controls:** Define the evidence and
   configuration you want to track. Use AWS Config and Security Hub CSPM to identify and surface
   findings.
2. **Identify when configuration changes happen:** Use AWS
   services that support event-driven architectures for identification. For example,
   AWS Config can monitor resource changes and Amazon EventBridge can serve as an event bus for
   additional resource changes.
3. **Implement remediation:** Services such as AWS Lambda and
   AWS Systems Manager can implement configuration changes.
4. **Rerun evaluation:** Verify remediation was implemented
   and the environment is back in compliance.

For example, you can create an AWS Config rule that marks an Amazon S3 bucket as non-compliant if the server-side encryption is not enabled.
That rule can invoke a corresponding remediation Lambda function that configures server-side encryption on the bucket, bringing the bucket to a compliant state.
For more information, refer to [Remediating Noncompliant AWS Resources by AWS Config Rules](../../../config/latest/developerguide/remediation.md "../../../config/latest/developerguide/remediation.md").
AWS also provides sample AWS Config rules with remediation actions for [Amazon DynamoDB](../../../config/latest/developerguide/templateswithremediation.md "../../../config/latest/developerguide/templateswithremediation.md")
and [Amazon S3](../../../config/latest/developerguide/templateswithremediation.md "../../../config/latest/developerguide/templateswithremediation.md").
