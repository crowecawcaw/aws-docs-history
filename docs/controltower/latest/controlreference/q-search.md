# Search for controls with Amazon Q

When you are logged into the AWS management console, Amazon Q can help you find the
controls that you need to manage your AWS Control Tower environment. You can type prompts to Q, and
find sumarized information about specific types or use cases for controls, such as these
examples:

- What are the Digital Sovereignty controls?
- What controls in AWS Control Tower monitor S3?
- I have an AWS service running that uses Amazon ECS to host it, which controls from
  AWS Control Tower should I enable?
- What are preventive controls in AWS Control Tower?
  Any time you'd like a paraphrase of information from the documentation, and a list of
  links for further reading, you can _ask Q_.

Amazon Q is more proficient
at summarizing information from the documentation than at giving complete lists of controls.
The lists of controls you may receive are helpful starting points. Amazon Q also provides tips for security and best practices.

###### Here's an example answer to the last example prompt.

_What are preventive controls in AWS Control Tower?_

Preventive controls in AWS Control Tower are an important part of the service's governance and
compliance capabilities. Here's an overview of preventive controls in AWS Control Tower:

**Purpose**: Preventive controls are designed to disallow actions
that could lead to policy violations or security risks. They help enforce configurations
and prevent non-compliant resource changes.

**Implementation**: Preventive controls are implemented using Service
Control Policies (SCPs), which are part of AWS Organizations.

**Scope**: These controls apply to entire organizational units (OUs)
and affect every AWS account within the OU.

**Function**: They help express policy intentions and enforce
governance rules across your AWS environment.

Examples of preventive controls:

- Requiring encryption at rest for certain services
- Enforcing multi-Availability Zone deployments for improved resiliency
- Restricting access to specific AWS Regions
- Digital Sovereignty: AWS Control Tower offers preventive controls that enhance digital
  sovereignty governance, covering areas such as data residency, granular access
  restrictions, encryption, and resiliency
  **Customization**: While some controls are mandatory, others are
  strongly recommended or elective, allowing you to tailor your governance posture to your
  specific needs.

**Management**: You can view and manage these controls in the
AWS Control Tower console, including a dedicated group for digital sovereignty-related
controls

**Exceptions**: It's important to note that the root user and
administrators in the management account have exceptions to these controls to prevent
the account from becoming unusable.

When implementing preventive controls, it's crucial to follow the principle of least
privilege and regularly review your control settings to ensure they align with your
organization's security and compliance requirements. For the most up-to-date information
on available controls and their specific functionalities, please refer to the official
AWS Control Tower documentation.
