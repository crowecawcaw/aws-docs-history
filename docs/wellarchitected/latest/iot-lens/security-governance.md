# Security governance

Managing the security of IoT devices requires a team of people
with clearly defined roles and responsibilities. In many
organizations, there is already a security governance team. In
these cases, security governance of IoT devices and IoT
applications should work in coordination with the security
governance team for the organization. There will be overlap
between governance of cloud-hosted aspects of IoT applications and
overall security governance for the organization so having clearly
defined roles and responsibilities will enable quick and efficient
identification of how must do what actions when an incident is
suspected or detected.

Like security governance for the organization, usage of DevOps and
DevSecOps mechanisms will spread some of the roles and
responsibilities for managing security across both operations and
development teams. The more that these teams work together and use
common tools and methods to manage, maintain, and operate the IoT
applications, the easier it will be to answer questions, prepare
for audits, and respond to incidents. By codifying security policy
into testable controls and using policy as code techniques, many
parts of security governance can be built into the develop, build,
test, and deploy automation used to manage, maintain, and improve
IoT applications.

There should be a risk assessment and risk management process for
IoT devices or gateways and applications which builds upon
existing risk assessment and risk management mechanisms in place
for the organization. Special attention should be paid
environmental and human safety concerns when assessing and
managing risk for IoT applications.

| IOTSEC 14: How do you govern the security<br>of your IoT applications? |
| ---------------------------------------------------------------------- |
|                                                                        |

The governance of IoT applications should be based on and
integrated with the governance of other applications built and
used by the organization. By using and extending existing
governance teams and processes to cover IoT applications,
appropriate teams can be informed and aware of potential risks
from using IoT services and applications and put in place
appropriate controls and mitigations for those risks.

## IOTSEC14-BP01 Establish a security governance team for your IoT applications or extend the security governance team for the organization

A security governance team will evaluate IoT applications
against a risk management framework. By establishing the
potential risks that each IoT application poses, teams can then
identify mitigations for those risks and update or remediate IoT
applications appropriately. Security governance applies to
people, processes, and tools used by the organization to
establish, evaluate, and update the security posture of
applications.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC14-BP01-01** _Coordinate activities
between security governance teams._

If there are multiple security governance teams throughout the
organization, coordinate the activities across these teams so
that decisions made by one team are consistent and carried out
by other parts of the organization which might be affected by
those decisions.

## IOTSEC14-BP02 Define security policy so that it can be written into verifiable checks using policy as code techniques

Security policies for an organization generally begin from
existing standards such as
[NIST
800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final"),

[ISO/IEC
27001](https://www.iso.org/isoiec-27001-information-security.html "https://www.iso.org/isoiec-27001-information-security.html"),

[ISA/IEC
62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards "https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards"), and

[CIS](https://www.cisecurity.org/ "https://www.cisecurity.org/"). Using
the controls identified in those standards along with the
specific architecture and implementation of applications,
verifiable checks of the configuration of the application can be
created which result in the controls being expressed in code.
These codified checks can then be automated so that compliance
can be evaluated on a repeated and ongoing basis. Reports
provide feedback on the compliance status of applications and
logs of the automated checks provide evidence of ongoing
evaluation of the environment.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC14-BP02-01** _Codify security policy
into verifiable checks._

Use tools such as
[AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") and the rules development kit (RDK) to codify
security policies into verifiable checks. Additional services
including
[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/"),

[AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/ "https://aws.amazon.com/iot-device-defender/"), and

[Amazon
Security Lake](https://aws.amazon.com/security-lake/ "https://aws.amazon.com/security-lake/") help to log compliance checks and provide
reports on the compliance status of applications.

**Prescriptive guidance
IOTSEC14-BP02-02** _Implement security policy
checks as part of the develop, build, test, and deploy workflow
and automation._

Security policy checks can also be implemented through source
code scanning as well as policy checking during deployment
processing. Use build automation and code scanning tools to
check for security configuration and report findings into
services such as
[Amazon
Security Lake](https://aws.amazon.com/security-lake/ "https://aws.amazon.com/security-lake/"). Use

[AWS CloudFormation Hooks](../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md"), a feature of

[AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/"), to add compliance checks into the
deployment processing of applications to check for and report
issues with the configuration of infrastructure which supports
applications.

## IOTSEC14-BP03 Implement a risk assessment and risk management process

A risk management process includes procedures for identify,
assess, and monitor risks as well as implementing mitigations
for those risks. The
[NIST
Risk Management Framework](https://csrc.nist.gov/Projects/risk-management "https://csrc.nist.gov/Projects/risk-management") provides an example process
which can be worked from if your organization does not already
have a process to follow. If your organization has an existing
risk management process, evaluate the process for any potential
adjustments which are specific to IoT applications. Consider the
environmental and human safety risks that may be applicable in
IoT application environments.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC14-BP03-01** _Integrate risk assessment
and risk management with other problem management tools that are
used by the development and operations teams._

Any work items or tasks which are generated from risk assessment
and risk management activities as well as findings from
automated compliance scanning performed during development,
build, and deployment of applications should be reflected back
into the problem management tools used by the application and
infrastructure development teams. Depending on the tools used to
perform compliance checks, this integration can be built into
the environment by using services such as
[Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") coupled with

[Amazon Simple Queue Service (SQS)](https://aws.amazon.com/pm/sqs/ "https://aws.amazon.com/pm/sqs/") and

[AWS Lambda](https://aws.amazon.com/pm/lambda/ "https://aws.amazon.com/pm/lambda/").

**Prescriptive guidance
IOTSEC14-BP03-02** _Identify what
environmental and human safety concerns are applicable to the
IoT application._

IoT applications often have direct interaction with humans
and the environment. Pay particular attention to the risks
related to environmental and human safety caused by the
decisions, processing and actions taken by the IoT application.
