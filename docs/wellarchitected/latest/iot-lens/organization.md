# Organization

For decades, we have seen manufacturing companies attempt to bring information technology (IT) systems into operations technology (OT) environments. Smart manufacturing increases efficiency and productivity, optimizes costs, and enhances product quality by integrating advanced technologies like robotics, AI, and IoT. Smart manufacturing provides greater flexibility and evolves through data-driven decision-making.

Leaders can develop a collaborative culture where open dialogue and trust are encouraged. Clarifying roles and responsibilities and establishing accountability between teams is crucial.

While converging OT and IT brings new efficiencies, it also brings
new risks. The merging of OT and IT has begun at most companies
and includes the merging of systems, organizations, and policies.
These components are often at different points along their
journey, making it necessary to identify each one and where it is
in the process to determine where additional attention is needed.
It is important to understand that OT is no longer an air-gapped
system that is hidden away from cyber risks, and so it now shares
many of the same risks as IT.

| IOTOPS01: How do you evaluate governance<br>and compliance requirements? |
| ------------------------------------------------------------------------ |
|                                                                          |

A robust governance strategy across people, process and technology
covering both internal and external stakeholders can help run
business efficiently. From a people perspective, well-documented
policies and processes, different team's role clarity with
measurable goals, and a transparent decision-making framework are
essential. Process-wise, a business case-driven approach to
selecting investments, proven program management methodology,
financial discipline, hardware supply chain and a robust risk
framework are key. And, from a technology perspective, a
technology architecture blue-print for IoT and IIoT adoption,
playbooks, runbooks, and drills for operational functions such as system
design, maintenance, telemetry, incident response and disaster
recovery with assigned ownership are crucial.

## IOTOPS01-BP01 Conduct an OT and IT cybersecurity risk assessment using a common framework

When taking advantage of IT technologies in OT environments, it
is important to conduct a cybersecurity risk assessment using
frameworks to fully understand and proactively manage risks (for
example, ISA/IEC 62443).
Companies with maturing OT and IT convergence display common
patterns. 

**Level of risk exposed if this best practice is not established:** Medium

**Prescriptive guidance IOTOPS01-BP01-01:** _Conduct a cyber-security risk assessment so that the risks, gaps and vulnerabilities are fully understood and can be proactively managed. Create and maintain an up-to-date threat model._

- Proactively managing risks, gaps, and vulnerabilities
  between OT and IT
- Up to date threat modeling capabilities for both OT and IT
- Define the system being assessed
- Identify threats, vulnerabilities and consequences of
  unintended access or behavior
- Rank the discovered risks
- Develop a risk mitigation strategy

## IOTOPS01-BP02 Evaluate if OT and IT teams use separate policies and controls to manage cybersecurity risks or if they use the same policy

The ongoing maturity and adoption of cloud within IT and now
within OT creates a more common environment. A comprehensive
enterprise and OT security policy will encompass risks across
the entirety of the business. This allows for OT risks such as
safety to be recognized and addressed within IT. Conversely,
this allows for IT risks such as bots and ransomware to be
addressed within OT. While policies might converge, mitigation
strategies will still differ in many cases.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive
guidance IOTOPS01-BP02-01**

- OT and IT maintaining separate risk policies.
- The degree of isolation for process control and safety
  networks.
- Interconnectedness of OT and IT systems and networks.
- Security risks that were applicable to either IT or OT might
  now apply to both.
- Singular security control policy that governs both OT and
  IT.
- Different mitigation strategies as appropriate for OT and
  for IT. For example, the speed of patching is often
  different between OT and IT by design.
- The use of holistic approaches to manage OT and IT risk.

### Resources

- [How
  to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/ "https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/")
- [AWS Threat Modeling workshop](https://maturitymodel.security.aws.dev/en/3.-efficient/threat-modeling/ "https://maturitymodel.security.aws.dev/en/3.-efficient/threat-modeling/")
- [Assessing
  OT and IIoT cybersecurity risk](https://aws.amazon.com/blogs/iot/assessing-ot-and-iiot-cybersecurity-risk/ "https://aws.amazon.com/blogs/iot/assessing-ot-and-iiot-cybersecurity-risk/")
- [Guidance
  on using ISA/IEC 62443 for IIoT projects](https://aws.amazon.com/blogs/iot/guidance-on-using-isa-iec-62443-for-iiot-projects/ "https://aws.amazon.com/blogs/iot/guidance-on-using-isa-iec-62443-for-iiot-projects/")

| IOTOPS02: Is there a central cloud<br>center of excellence (CCoE) with equivalent representation<br>from OT and IT in industrial organizations? |
| ----------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                 |

Given the historical nature of the separation of IT and OT,
organizations might still operate in silos. An indication of
converging maturity is how well those teams are working across
divisions or have even removed silos altogether. Meaningful
OT/IT convergence requires focused and organized effort, which
a CCoE can facilitate. A CCoE is a multi-disciplinary team of
passionate OT and IT subject matter experts (SMEs) who act as
change agents to accelerate IIoT adoption by standardizing and
evangelizing best practices, developing repeatable patterns to
scale implementation, driving governance, and providing
thought leadership. The CCoE can start small with 3-5 members,
cross-trained in both IT and OT aspects and can scale as
needed. For a CCoE to be successful, it requires executive
sponsorship and ability to act autonomously. The CCoE can
focus on making incremental improvements instead of a big-bang
approach. A prioritization framework is used to identify pilot
use cases starting with low-risk, high value, and low effort
use cases with measurable success metrics. After the pilot use
cases are deployed and business value demonstrated, this
activity continues cyclically to implement the pipeline of
prioritized use cases.

## IOTOPS02-BP01 Consolidate resources into centers of excellence to bring focus to new or transforming enterprises

You can consider creating CCoEs around security to consolidate
experts from around the company. Such focused areas are a
central point of technical authority and accelerates decision
making.

**Level of risk exposed if this best practice is not established:** Low

**Prescriptive guidance IOTOPS02-BP01-01**

- Consolidating resources into centers of excellence.
- Security experts consolidated from around the company into a
  singular organization.
- Defining security focus areas based on risk priorities.
- Having a central point of security authority.
- OT and IT teams operating uniformly.
- Well understood and applied incident response decision
  rights in OT.
- Availability is vital in OT. Systems must run in order to
  produce and manufacture product. Downtime equals lost
  revenue.
- Security defenses are often designed to wrap around OT zones
  while restricting the conduits between them.

### Resources

- [AWS Blogs: 7 Pitfalls to Avoid When Building a CCOE](https://aws.amazon.com/blogs/enterprise-strategy/7-pitfalls-to-avoid-when-building-a-ccoe/ "https://aws.amazon.com/blogs/enterprise-strategy/7-pitfalls-to-avoid-when-building-a-ccoe/")
- [AWS Blogs: Using a CCOE to Transform the Entire
  Enterprise](https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/ "https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/")
- [Managing
  Organizational Transformation for successful OT/IT
  convergence](https://aws.amazon.com/blogs/iot/managing-organizational-transformation-for-successful-ot-it-convergence/ "https://aws.amazon.com/blogs/iot/managing-organizational-transformation-for-successful-ot-it-convergence/")
