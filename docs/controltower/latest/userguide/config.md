# Govern Resource Configurations with AWS Config

AWS Config provides a detailed view of the resources associated with your AWS account,
including how they are configured, how they are related to one another, and how the
configurations and their relationships have changed over time. For more information, see
_[AWS Config Developer Guide](../../../config/latest/developerguide.md "../../../config/latest/developerguide.md")_.

AWS Config resources provisioned by AWS Control Tower are tagged automatically with
`aws-control-tower` and a value of
`managed-by-control-tower`.

For more information about how AWS Config monitors and records resources in AWS Control Tower,
and how it bills you for them, see [Monitor resource changes with AWS Config](monitoring-with-config.md "monitoring-with-config.md").

AWS Control Tower uses AWS Config Rules to implement detective controls. For more information, see [About
controls in AWS Control Tower](controls.md "controls.md").

## AWS Config Integration in Control Tower Landing Zone 4.0

### Service-Linked Config Aggregator (SLCA)

AWS Control Tower now implements a Service-Linked Config Aggregator (SLCA) as part
of Landing Zone 4.0+. This change represents a significant improvement in how
AWS Config data is aggregated and managed across your organization.

### Key Changes

**New Service-Linked Config Aggregator Deployment**

- A Service-Linked Config Aggregator is deployed in your designated
  AWS Config integration account.
- For existing customers, this will be your audit account
- For new customers, this will be the account specified in the manifest's
  `config.accountId` field

**Delegated Administrator**

- The AWS Config aggregator account becomes the delegated administrator for AWS Config
- AWS Control Tower automatically configures the delegated admin settings
- This enables centralized management of AWS Config across your organization

**Migration from Legacy Aggregators**

During the upgrade to Landing Zone 4.0:

- The organization aggregator in the management account will be removed.
- The account aggregator in the audit account will be removed.
- These are replaced by the new service-linked Config Aggregator in the AWS Config integration aggregator account.

### Enhanced Data Aggregation

The service-linked Config Aggregator provides improved capabilities for Config data aggregation:

- Can aggregate data from any AWS Config recorder in your organization
- Includes data from accounts not managed by Control Tower
- Provides a comprehensive view of configuration items across your organization
- Supports enhanced data perimeter controls

### Important Considerations

**Delegated Administrator Configuration**

- AWS Control Tower will use the account specified in your manifest for AWS Config integration
- This account will be automatically configured as the delegated administrator
- No additional action is required from customers for this configuration
- For existing customers, your previous Security Roles integration account (Audit account) will be configured as the AWS Config central aggregator account during Landing Zone 4.0 upgrade

**Data Aggregation Scope**

- Service-Linked Config Aggregator can aggregate configuration data from:
  - Control Tower managed accounts
  - Non-Control Tower managed accounts
  - Any account with an active Config recorder in your organization

**Access Controls**

- Access to aggregated data is managed through IAM policies
- The AWS Config central aggregator account has central access to all aggregated data
- Member accounts maintain their individual AWS Config recorders

### Best Practices

**Config Central Aggregator Account Selection**

- Choose an account dedicated to security and compliance monitoring
- Ensure appropriate access controls are in place
- Consider using an existing audit or security account

**Data Management**

- Regularly review aggregated configuration data
- Implement appropriate retention policies
- Monitor AWS Config recorder status across accounts

### Migration Impact

When upgrading to Landing Zone 4.0:

**Before Migration**

- Document existing AWS Config rules and aggregators
- Review current AWS Config data access patterns
- Plan for any necessary IAM policy updates

**During Migration**

- Legacy AWS Config aggregators will be automatically removed
- Service-Linked Config Aggregator will be deployed
- Delegated administrator will be configured

**After Migration**

- Verify Service-Linked Config Aggregator is functioning correctly
- Confirm data aggregation from member accounts
- Update monitoring and reporting tools as needed
