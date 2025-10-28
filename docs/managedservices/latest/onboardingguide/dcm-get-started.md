# Getting Started with Direct Change mode

Begin by checking prerequisites and then submitting a request for change (RFC) in your eligible AMS Advanced account.

1. Confirm that the account that you want to use with DCM meets the requirements:
   - The account is AMS Advanced Plus or Premium.
   - The account doesn't have Service Catalog enabled. We currently don't support onboarding accounts to both DCM and Service Catalog
     at the same time. If you are already onboarded to Service Catalog but are interested in DCM, discuss your needs with your cloud service delivery manager (CSDM).
     If you decide to switch from Service Catalog to DCM, offboard Service Catalog, to do that, include the ask in the request for change below.
     For details about Service Catalog in AMS, see
     [AMS and Service Catalog](../userguide/ams-service-catalog.md "../userguide/ams-service-catalog.md").

2. Submit a request for change (RFC) using the Management | Managed account | Direct Change mode | Enable change type (ct-3rd4781c2nnhp). For an
   example walkthrough, see
   [Direct Change mode | Enable](../ctref/management-managed-direct-change-mode-enable.md "../ctref/management-managed-direct-change-mode-enable.md").

After the CT is processed, the predefined IAM roles, `AWSManagedServicesCloudFormationAdminRole` and
`AWSManagedServicesUpdateRole` are provisioned in the specified account. 3. Assign the appropriate role to the users that require DCM access using your internal federation process.

###### Note

You can specify any number of SAMLIdentityProviders, AWS Services, and IAM Entities (Roles, Users etc) to assume
the roles. You must provide at least one: `SAMLIdentityProviderARNs`, `IAMEntityARNs`, or
`AWSServicePrincipals`. For more information, consult with your company's IAM department or with your AMS cloud architect (CA).

## Direct Change mode IAM roles and policies

When Direct Change mode is enabled in an account, these new IAM entities are deployed:

`AWSManagedServicesCloudFormationAdminRole`: This role grants access to the CloudFormation console,
create and update CloudFormation stacks, view drift reports, and create and execute CloudFormation ChangeSets. Access to this role
is managed through the your SAML provider.

Managed policies that are deployed and attached to the role `AWSManagedServicesCloudFormationAdminRole` are:

- AMS Advanced multi-account landing zone (MALZ) Application account
  - AWSManagedServices_CloudFormationAdminPolicy1
  - AWSManagedServices_CloudFormationAdminPolicy2
    - This policy represents the permissions granted to the `AWSManagedServicesCloudFormationAdminRole`. You
      and partners use this policy to grant access to an existing role in the account and allow that role to launch and update
      CloudFormation stacks in the account. This might require additional AMS service control policy (SCP) updates to allow
      other IAM entities to launch CloudFormation stacks.

- AMS Advanced single-account landing zone (SALZ) account
  - AWSManagedServices_CloudFormationAdminPolicy1
  - AWSManagedServices_CloudFormationAdminPolicy2
  - cdk-legacy-mode-s3-access [in-line policy]
  - AWS ReadOnlyAccess policy

`AWSManagedServicesUpdateRole`: This role grants restricted access to downstream
AWS service APIs. The role is deployed with managed policies that provide mutating and non-mutating API operations, but in
general restricts mutating operations (such as Create/Delete/PUT), against certain services such as IAM, KMS,GuardDuty,
VPC, AMS infrastructure resources and configuration, and so forth. Access to this role is managed through the your SAML provider.

Managed policies that are deployed and attached to the role `AWSManagedServicesUpdateRole` are:

- AMS Advanced multi-account landing zone Application account
  - AWSManagedServicesUpdateBasePolicy
  - AWSManagedServicesUpdateDenyPolicy
  - AWSManagedServicesUpdateDenyProvisioningPolicy
  - AWSManagedServicesUpdateEC2AndRDSPolicy
  - AWSManagedServicesUpdateDenyActionsOnAMSInfraPolicy

- AMS Advanced single-account landing zone account
  - AWSManagedServicesUpdateBasePolicy
  - AWSManagedServicesUpdateDenyProvisioningPolicy
  - AWSManagedServicesUpdateEC2AndRDSPolicy
  - AWSManagedServicesUpdateDenyActionsOnAMSInfraPolicy1
  - AWSManagedServicesUpdateDenyActionsOnAMSInfraPolicy2

Besides these, the managed policy `AWSManagedServicesUpdateRole` role also has the AWS managed policy
`ViewOnlyAccess` attached to it.
