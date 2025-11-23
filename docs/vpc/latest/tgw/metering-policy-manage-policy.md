# Manage AWS Transit Gateway metering policies

After creating a metering policy, you can manage it by viewing current settings, modifying configuration options, or deleting the policy when no longer needed. Management operations allow you to add or remove middlebox attachments as your network requirements change. You can only create or delete a policy entry. If you need to modify an existing rule, you can delete the entry and create a new one with the modified configuration. All management operations require transit gateway owner permissions and take effect after two billing hour.

Effective metering policy management is crucial for maintaining accurate cost allocation as your network architecture evolves. Organizations often need to adjust their policies when business units change, new applications are deployed, or network topologies are modified. For example middlebox metering support settings may require updates when firewall security architectures change or when new inspection services are introduced into the traffic path.

Policy modifications support various operational scenarios including seasonal traffic pattern changes, merger and acquisition activities, and compliance requirement updates. When managing policies, consider the impact on existing billing arrangements and communicate changes to affected stakeholders before implementation.

Regular policy reviews help ensure that cost allocation remains aligned with business objectives and organizational structures. Best practices include documenting policy changes, testing modifications in non-production environments when possible, and coordinating with finance teams to understand billing implications. Additionally, consider the timing of policy changes to minimize disruption to monthly billing cycles and financial reporting processes.

###### Topics

- [Edit a metering policy](metering-policy-edit.md "metering-policy-edit.md")
- [Delete a metering policy](metering-policy-delete.md "metering-policy-delete.md")
