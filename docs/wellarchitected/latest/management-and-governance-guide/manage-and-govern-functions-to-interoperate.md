# Manage and govern functions to interoperate

The eight management and governance functions, supported by AWS
services and AWS Partner solutions, should interoperate together
in an informative relationship to help you manage and govern your
environments at scale. Outputs from these functions are used to
inform or integrate with other functions.

As an example, a report in
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/") shows a spike in month-to-month EC2 usage in
a development environment. Further investigation leads you to
discover that a new team has been launching `m5.16xlarge` instances,
but using less than two percent of the CPU capacity. AWS Cost Explorer insights reveal that the development environment did not
require the same instance size as test or production. As an input
to controls, you can define a detective AWS Config
rule in the development environment to alert on unapproved
`m5.16xlarge` instances. In addition, you can permit builders to
only self-service provision `nano` instance types in the development
environment by using template constraints from Service Catalog, or you can assign an AWS Organizations service control
policy to restrict the instance types that can be launched in that
environment.

With this interoperability example, you can tune the financial
operations of your IT functions to automate cost controls, which
permit you to continually evaluate mechanisms that can reduce your
AWS costs. Although similar manual mechanisms might be effective,
they are not as efficient as you scale further workloads on AWS.
Throughout this M&G Guide, you will see the additive benefits of an
interoperable and automated foundation of the proposed eight
capabilities in your AWS environments.
