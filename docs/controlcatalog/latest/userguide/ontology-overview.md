# Ontology overview

AWS has developed a standard classification system to help classify, organize, and
create mappings among controls. This ontology can be used to map controls to existing and
new regulatory standards, including 24 frameworks, as well as regulatory standards such as
PCI, HIPAA, and others. We also map to industry standards such as NIST and ISO, and to
Amazon-specific frameworks, including the Well-Architected framework.

###### The ontology has four core aspects

- **Classification of controls by Control domain, Control objective, and
  Common controls.** The ontology helps organize and group related
  controls into three levels—

      + L1: Control domain,
      + L2: Control objective,
      + L3: Common control.

  These levels have a strict hierarchical relationship. That is, each domain has
  multiple control objectives, but each control objective must have a single parent
  domain. Each control objective has multiple common controls, but each common control
  has a single parent objective.

- **Mapping to regulatory standards.** The ontology has a
  concept called a _Standard control_ (L4) that represents a
  specific requirement within a regulatory or industry standard. These Standard
  controls are mapped to Common controls that help address those specific
  requirements.

For example, **PCI-DSS v3.2.1. ID 4.1**
_Use strong cryptography and security protocols to safeguard sensitive
cardholder data during transmission over open, public networks_ and
**NIST 800.53.r5 ID SC-16**
_Transmission of security and privacy attributes_ are two
Standard controls, both mapping to the _Encrypt data in transit_
Common control.

- **Control implementations and control evidence.** The
  ontology has a concept of _Control implementations_ (L6) that can
  represent either a specific control implementation in AWS, for example, an
  AWS Control Tower control, an AWS Security Hub CSPM check, an AWS Config rule, and so forth, or a non-technical
  implementation outside AWS, such as process guidance. A separate concept of
  _Control evidence_ (L7) represents data sources that can be
  used as evidence for controls by AWS Audit Manager, third-party tools, or customers
  themselves. These evidence sources could be AWS sources such as AWS CloudTrail events,
  API call logs, and AWS Config rule evaluation results. Or, they could be external sources
  such as customer documentation.
- **The concept of a Core control (L5).** The Core
  control is a mapping layer that consolidates all control implementations (L6),
  corresponding evidence sources (L7), related standard controls (L4), and Common
  controls (L3) into a single holistic object. The Core control is more of a mapping
  document than a control itself. It helps answer the question of _show me
  all the info related to control X_. Each core control can have
  multiple control implementations (L6) and multiple evidence sources (L7).
  In summary, the AWS control catalog ontology contains seven layers. Three are hierarchical classification
  layers (Control domains, Control objectives, Common controls). Another layer (Standard
  controls) describes the regulatory or industry standard requirements. A mapping layer (Core
  control) describes a control outcome for a given resource type. Two layers (Control
  implementations, Control evidences) describe the specific control implementations and
  evidence sources.

This ontology was designed by an AWS team of certified auditors, based on their
experience working with hundreds of customers for compliance audits. The concepts of Control
domains, Control objectives, Common controls, and Standard controls (L1-L4)
are used industry-wide. They match common industry patterns and NIST recommendations. The
remaining three layers (L5-L7) were designed based on existing AWS concepts, such as
resource types and managed controls.
