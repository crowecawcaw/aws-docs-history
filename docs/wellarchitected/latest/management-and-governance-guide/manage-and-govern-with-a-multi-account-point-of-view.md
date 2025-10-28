# Manage and govern with a multi-account point of view

AWS helps enable you to experiment, innovate, and scale more quickly, while providing
flexible and secure cloud environments. An AWS account provides natural security, access,
and billing boundaries for your AWS resources. The AWS account as a boundary helps you to
achieve resource isolation as described in the [Security Pillar
whitepaper](../security-pillar/welcome.md "../security-pillar/welcome.md"). The Security Pillar specifically recommends the following best practices:
separate workloads using accounts, secure AWS accounts, manage accounts centrally, set
controls centrally, configure services and resources centrally.

The multi-account strategy prescriptive guidance provided in the [Organizing Your AWS Environment Using Multiple Accounts whitepaper](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md") describes
specific mechanisms to organize accounts. In addition, it describes how to apply a consistent
set of controls so that you can efficiently manage your cloud assets. In AWS, accounts are a
hard boundary. Account-level separation is recommended for isolating production workloads from
development and test workloads. For instance, sandbox environments might need a different set
of controls, network, change processes, and financial limits compared to other environments.
Using this strategy helps you to centrally manage resources, permissions, and security
standards across environments and accounts, improving your operational efficacy.

The M&G Guide complements the Security Pillar and the
multi-account strategy to further define a set of eight
foundational capabilities required to prepare your environments
and operate efficiently in the AWS Cloud. You can start automating
provisioning your accounts following this strategy with
[AWS Control Tower](https://aws.amazon.com/controltower "https://aws.amazon.com/controltower"). With this service you will provision a landing zone
from your home Region, and deploy further accounts following your
multi-account strategy.

The [Organizing Your AWS Environment Using Multiple Accounts whitepaper](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md") recommends
that you build a multi-account strategy using account boundaries to separate workloads.
However, it is important to evaluate and plan your account management with automation and
operational capacity in mind. That is, your accounts should employ the least privilege access,
and provide boundaries to limit the effect of workload failures. Do not create more accounts
than are feasible to operationally manage or scale. Furthermore, as you scale, consider
reviewing your service quotas and deployment latencies when performing actions on a large
number of accounts.
