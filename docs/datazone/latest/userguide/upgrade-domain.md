# Upgrade Amazon DataZone domains to Amazon SageMaker unified

domains

## Considerations before you upgrade your

domain

Before upgrading your Amazon DataZone domain to an Amazon SageMaker unified domain,
review these important considerations to ensure a smooth upgrade process.

- The upgrade process is available only through the AWS management
  console. Currently, no API support is offered for upgrading your domain. You
  can initialize the upgrade process from the domain details page of your
  Amazon DataZone domain.
- The upgrade process requires the following roles to be configured (you can
  select existing roles or have Amazon SageMaker Unified Studio create the
  roles on your behalf):
  - Domain Execution role - for an Amazon DataZone domain, you're using the
    [AmazonDataZoneDomainExecutionRole](AmazonDataZoneDomainExecutionRole.md "AmazonDataZoneDomainExecutionRole.md") that is required by
    Amazon DataZone to catalog, discover, govern, share, and analyze data in
    your domain. With an Amazon SageMaker unified domain, you must
    either use the existing of create a new [AmazonSageMakerDomainExecution](../../../sagemaker-unified-studio/latest/adminguide/AmazonSageMakerDomainExecution.md "../../../sagemaker-unified-studio/latest/adminguide/AmazonSageMakerDomainExecution.md") role.
  - Domain Service role - Amazon DataZone does not require a Domain Service
    role. With an Amazon SageMaker unified domain, you must either use
    the existing of create a new [AmazonSageMakerDomainService](../../../sagemaker-unified-studio/latest/adminguide/AmazonSageMakerDomainService.md "../../../sagemaker-unified-studio/latest/adminguide/AmazonSageMakerDomainService.md") role. This is a service
    role for domain level actions performed by Amazon SageMaker Unified
    Studio.

- Root domain ownership considerations:
  - IAM users or SSO users/groups can be optionally assigned as root
    domain owners during the upgrade process.
  - If the root domain unit only has IAM roles assigned as owners, it
    is recommended that you add an IAM user or an SSO user/group as
    owner. For more information, see [User management](../../../sagemaker-unified-studio/latest/adminguide/user-management.md "../../../sagemaker-unified-studio/latest/adminguide/user-management.md") in the Amazon DataZone Administrator
    Guide.
  - **Important**: IAM roles cannot log
    in to the Amazon SageMaker Unified Studio.

- Associated accounts and AWS Resource Access Manager (AWS RAM)
  changes:
  - Associated accounts use resource shares from AWS RAM to permit
    API actions from the root domain account.
  - The upgrade process changes the underlying managed permissions for
    the AWS RAM share that is created and managed by Amazon DataZone. The
    affected managed permissions are
    `AWSRAMPermissionsAmazonDatazoneDomainExtendedServiceAccess`
    and
    `AWSRAMPermissionsAmazonDatazoneDomainExtendedServiceWithPortalAccess`.

- Amazon Q subscription changes - the upgraded domain will have Amazon Q
  subscription defaulted to the free-tier. Domain administrators can change
  this after the domain upgrade is complete.
- After the upgrade, the domain's `domainVersion` attribute
  changes from `V1` to `V2`.

## Upgrade your Amazon DataZone domain to an

Amazon SageMaker unified domain

You can complete the following procedure to upgrade your Amazon DataZone domain to an
Amazon SageMaker unified domain.

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region
   selector in the top navigation bar to choose the appropriate AWS
   Region.
2. Choose the Amazon DataZone domain that you want to upgrade and navigate to its
   details page.
3. On the domain's details page, choose the **Get started**
   button located in the **Upgrade your domain to Amazon SageMaker
   Unified Studio** notification.
4. On the **Upgrade your domain to Amazon SageMaker Unified
   Studio** page, choose **Start**.
5. Next, specify the Domain Execution role and the Domain Service roles for
   the domain and the root domain unit owners if your Amazon DataZone domain that
   you are upgrading doesn’t have owners that are of type IAM user, SSO
   user/group. Then choose **Upgrade domain**.

## Frequently asked questions about upgrading

Amazon DataZone domains to Amazon SageMaker unified domains

- **Which properties and configurations carry over with
  the domain after the upgrade?**

All properties configured on the Amazon DataZone domain carry over to the
upgraded Amazon SageMaker unified domain. This includes data encryption
properties, authentication application properties, etc.

- **Do I need to set up single sign-on (SSO) access
  again for my users?**

No. Your IAM Identity Center SSO application associated to the domain will
carry over to the upgraded Amazon SageMaker unified domain. Additionally,
any IAM user or role assigned to the domain will be available in the
upgraded Amazon SageMaker unified domain.

- **Can I still use the Amazon DataZone portal after the
  upgrade?**

Yes. After the upgrade both Amazon DataZone portal and Amazon SageMaker Unified
Studio will be available for end users to interact with. Both portals will
remain open until a domain administrator deactivates the Amazon DataZone portal
from the Amazon SageMaker management console.

- **Will I see the projects and other entities that were
  created in the Amazon DataZone portal in Amazon SageMaker Unified
  Studio?**

Yes. Most entities (projects, metadata forms, glossaries, domain units)
created through the Amazon DataZone portal will be visible in Amazon SageMaker
Unified Studio. Projects will carry over all assets, metadata forms and
glossaries associated to assets, subscriptions to assets, members, etc.
These projects require querying the data from AWS Athena or Amazon
Redshift query editors. Metadata forms and glossaries will appear in Amazon
SageMaker Unified Studio and they can be edited from Amazon SageMaker and
assigned to assets from projects created through Amazon SageMaker.
Environments and environment profiles from Amazon DataZone will not show in
Amazon SageMaker Unified Studio - these entities have been replaced by
Amazon SageMaker project profiles. Projects created in the Amazon SageMaker
Unified Studio will not be visible through the Amazon DataZone portal.

- **What happens to the domain identifier and the
  project identifiers after the upgrade to Amazon SageMaker unified
  domain?**

All entity identifiers, including the domain and projects, will remain the
same after the upgrade.

- **Will my AWS CloudFormation (CFN) stacks continue
  to work for the newly upgrade Amazon SageMaker unified
  domain?**

Amazon SageMaker Unified Studio uses the same APIs as Amazon DataZone. However,
some modifications to the logic within CFN templates will be needed. For
example, domains from Amazon DataZone are distinguished from Amazon SageMaker
unified domains by an attribute named domainVersion (values V1 | V2).

- **What happens when the upgrade is rolled
  back?**
  - Rolling back the upgrade changes the domain version from V2 to V1.
    Amazon SageMaker Unified Studio will no longer be accessible. The
    console view for the domain will return to the Amazon DataZone view.
    Resources created before the roll back will remain so long as they
    are not tied to a project that was created from Amazon SageMaker
    Unified Studio - rolling back is only permitted when no projects
    that were created from within Amazon SageMaker Unified Studio are
    present.
  - Settings such as AWS Q subscription will also persist after the
    roll back.
  - If VPCs were created for the use of Amazon SageMaker, these will
    persist after the roll back. VPC's created by the SageMaker service
    will have tag: Name = SageMakerUnifiedStudioVPC
  - The managed permission under the RAM resource share will not be
    rolled back. The managed permission is a superset of both Amazon DataZone
    and Amazon SageMaker Unified Studio.
  - A domain that had been rolled back can again be upgraded to Amazon
    SageMaker unified domain.
