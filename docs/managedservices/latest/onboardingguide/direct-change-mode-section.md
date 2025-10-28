# Direct Change mode in AMS

###### Topics

- [Getting Started with Direct Change mode](dcm-get-started.md "dcm-get-started.md")
- [Security and compliance](dcm-security-n-compliance.md "dcm-security-n-compliance.md")
- [Change management in Direct Change mode](dcm-change-mgmt.md "dcm-change-mgmt.md")
- [Creating stacks using Direct Change mode](dcm-creating-stacks.md "dcm-creating-stacks.md")
- [Direct Change Mode use cases](dcm-use-cases.md "dcm-use-cases.md")
  AWS Managed Services (AMS) Direct Change mode (DCM) extends AMS Advanced change management by providing native AWS access to AMS Advanced Plus and
  Premium accounts to provision and update AWS resources. With DCM, you have the option to use native AWS API (console or CLI/SDK) or
  AMS Advanced change management requests for change (RFCs), and in either case the resources and changes to them are fully supported by AMS,
  including monitoring, patch, backup, incident response management. Resources provisioned through DCM are registered in the AMS service
  knowledge management system (SKMS), joined to the AMS managed Active Directory domain (when applicable), and run AMS management
  agents. Use existing tooling (for example, CloudFormation, AWS SDK, and CDK) to develop and deploy AMS-managed CloudFormation stacks.

###### Note

Direct Change mode does not remove AMS change management RFCs. You have full access to AMS RFCs with DCM.
