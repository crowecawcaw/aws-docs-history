# Prepare

| HCL_OPS1. Have you defined a formal risk management program? |
| ------------------------------------------------------------ |
|                                                              |

**Create and document a risk management program**

Many regulatory frameworks are intended to reduce risk in one
way or another. Organizations usually understand that they
must reduce their risk, but may struggle to determine what the
appropriate risk appetite is and how to manage it. This is
accomplished using a documented risk management program.

In healthcare, the risk management program is designed to
safeguard patient data, as well as the overall organization’s
assets and reputation.  For example, a healthcare provider’s
risk management program also covers clinical quality, which is
critical to reducing potential patient risk.  Healthcare
organizations should create a comprehensive risk management
program that includes all operational, clinical, strategic,
financial, legal, environmental, and any other potential risk
domains.

When designing your risk management program, ask questions
similar to the following:

- Have you defined risk and compliance roles for the cloud?
- Have you created a risk management program for the cloud?
- Have you assessed your workload against regulatory needs?
- Have you performed a security risk assessment?
- Have you created a cloud governance program?
- Have you created a responsibility model?

**Create a risk authority
team**

Creating an effective risk management program for the cloud
should be defined by the appropriate risk authority team.  The
risk authority within the organization (for example, board of
directors, chief risk officers, or business risk officers)
must evaluate the criticality of a business process (and the
underlying workloads that support that process) and specify
the level of availability they require for the process.
Consider the potential impact a disruption may have on the
process, organization, and customers. Weigh the impact against
the cost of operating the workload in a high availability
mode, consequences for business agility, and pace of
innovation. Working backwards from established risk appetites
allows you to define operational priorities and corresponding
cloud architectures that can meet your business objectives.

AWS publishes the [Amazon Web Services: Risk and Compliance whitepaper](../../../whitepapers/latest/aws-risk-and-compliance/welcome.md "../../../whitepapers/latest/aws-risk-and-compliance/welcome.md") that outlines
the mechanisms used to manage risk on the
AWS side of the shared responsibility model. This whitepaper
also provides tools that customers can use to ensure these
mechanisms are being implemented effectively.

| HCL_OPS2. What policies and<br>procedures has your organization adopted for cloud<br>governance? |
| ------------------------------------------------------------------------------------------------ |
|                                                                                                  |

**Create policies and
procedures to govern cloud workloads**

Cloud governance is a set of policies and procedures that
outline, or govern, how an organization manages their cloud
workloads.  A mature governance program requires understanding
the compliance objectives and requirements and establishing a
control environment that meets those objectives and
requirements.  Organizations that host and process healthcare
data can be required to meet specific standards and
regulations, such as HIPAA or General Data
Protection Regulation (GDPR). A mature governance
program can help verify that the necessary controls are
implemented.

As outlined in the
[Amazon Web Services: Risk and Compliance
whitepaper](../../../whitepapers/latest/aws-risk-and-compliance/welcome.md "../../../whitepapers/latest/aws-risk-and-compliance/welcome.md"), AWS customers are responsible for maintaining adequate governance
over their entire IT control environment, regardless of how or
where IT is deployed. Recommended practices include:

- Understanding the required compliance objectives and
  requirements (from relevant sources)
- Establishing a control environment that meets those
  objectives and requirements
- Understanding the validation required based on the
  organization’s risk tolerance and applicable regulatory
  requirements
- Verifying the operating effectiveness of their control
  environment

Cloud deployments give organizations different options to
apply various types of controls and various verification
methods.

Strong customer compliance and governance on AWS should
include the following:

- Reviewing the
  [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"),
  [AWS security documentation](../../../security.md "../../../security.md"),
  [AWS compliance reports](https://aws.amazon.com/artifact/?nc2=h_ql_prod_se_ar "https://aws.amazon.com/artifact/?nc2=h_ql_prod_se_ar"), and other information available
  from AWS, together with other customer-specific
  documentation. Try to understand as much of the entire IT
  environment as possible, and document all compliance
  requirements into a comprehensive cloud control framework.
- Designing and implementing control objectives to meet the
  enterprise compliance requirements as laid out in the
  [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").
- Identifying and documenting controls owned by outside
  parties.
- Verifying that all control objectives are met and all key
  controls are designed and working.

Approaching compliance governance this way helps you better
understanding you control environment. It can also delineate
the verification activities that must be performed.

| HCL_OPS3. How do you map security<br>controls to compliance requirements? |
| ------------------------------------------------------------------------- |
|                                                                           |

**Determine regulatory
frameworks and security controls that are applicable to your
business and your cloud workload**

Organizations that host and process health data must verify
that they are adhering to all applicable regulatory frameworks
and standards. As healthcare organizations evolve and grow,
they may either want, or be required, to adhere to multiple
regulations or certifications. For example, a European
organization may be required to meet GDPR and additional country-specific
regulations in each country it operates in.

**Map applicable frameworks
and controls to AWS controls to align with regulatory
frameworks**

There are two common approaches to addressing multiple
compliance regimes. First, organizations may choose to address
each set of requirements from the beginning and develop
mappings unique to each. Alternatively, organizations can
choose to map to a common security framework, and leverage
published controls mappings from that framework to many
others in a hub-and-spoke model. AWS recommends the latter
approach where possible to avoid duplicating effort.

As an example, here are steps you might take if you use NIST
800-53 as your security framework, and apply it to the HIPAA
Security Rule on AWS:

1. Map NIST 800-53 to applicability within the AWS
   environment, considering the shared responsibility model
   with AWS and any third parties you may work with.
2. Use prebuilt AWS compliance checks for NIST or other
   frameworks with AWS config conformance packs, as well as
   implement any additional custom checks to monitor your AWS
   environments. Implement immutable logging to archive
   compliance posture over time.
3. Use NIST Special Publication 800-66 to map controls from
   NIST 800-53 to the HIPAA Security Rule

In other words, create a crosswalk to map your AWS controls to
a common security control framework. Use this crosswalk to
connect controls in your cloud environment to the regulation
standards as required.

Another example is to create a
[responsibility
assignment matrix](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix "https://en.wikipedia.org/wiki/Responsibility_assignment_matrix")
(RACI) that designates roles who are responsible, accountable,
consulted, and informed for regulatory controls. A policy with
a RACI matrix clarifies accountability and helps affirm
that proper actions are taken by designated owners. A
consulted party offers guidance related to the control.
Finally, the informed party is made aware of the situation and
any actions taken. Using RACI matrices can help organizations
properly implement plans and procedures when dealing with
regulatory controls.

| HCL_OPS4. How do you educate<br>employees on access to sensitive data? |
| ---------------------------------------------------------------------- |
|                                                                        |

**Ensure employees who may
have access to sensitive healthcare data are trained on the
rules and regulations**

Organizations that host or process PHI should ensure that
employees who have access to healthcare data, either
intentionally or accidentally as part of their job function,
are trained on the rules and regulations that govern the
organization. Employees should have knowledge on what to do
when viewing sensitive data. They should know how and where to
host or process that data, and how to protect it. Train
employees on any other regulation-based requirements, such as
breach disclosure. Document all of this in your risk
management program.

**Create and document a
policy and procedure aligned to each control and
safeguard**

Organizations that are hosting and processing sensitive
healthcare data should have a documented policy that aligns
with each control or safeguard in place to secure the data. In
addition, each policy should have an associated procedure
document that outlines how the policy will be implemented.
These policy and procedure documents will help educate
employees on the safeguards used, and can help demonstrate
your compliance posture to your stakeholders. These documents
help create a stronger culture of compliance for your
organization.
