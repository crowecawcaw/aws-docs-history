

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with buying policies using the AWS Marketplace API

Buying policies give procurement, finance, and cloud governance teams control over how purchases in AWS Marketplace are approved. A private marketplace controls *which* products users in your organization can buy. Buying policies control *how* individual purchases are approved and what buyers must provide when they purchase. You can use the AWS Marketplace Catalog API to do the following:
+ **Require approval for purchases** – Create procurement approval rules that decide which purchases need review or are declined, and where each request is sent. For more information, see [Configuring buyer approvals](buying-policies-buyer-approvals.md).
+ **Require purchase order numbers** – Require buyers to enter a purchase order number before they subscribe, for specific offer types and pricing types. For more information, see [Configuring mandatory purchase orders](buying-policies-po-number-requirements.md#buying-policies-api-mandatory-po).
+ **Display a procurement administrator message** – Explain your organization's procurement requirements to buyers on AWS Marketplace procurement pages. For more information, see [Configuring custom procurement messaging](buying-policies-po-number-requirements.md#buying-policies-api-procurement-message).

For information about configuring buying policies in the AWS Management Console, see [Configuring buying policies in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buying-policies.html) in the *AWS Marketplace Buyer Guide*.

**Required permissions**  
Call the buying policy change types from the management account of your organization or from a delegated administrator account for private marketplace. Use an IAM user or role that has the `AWSPrivateMarketplaceAdminFullAccess` AWS managed policy. Buying policies are AWS Marketplace purchasing settings. They're separate from IAM policies and AWS Organizations policies, such as service control policies (SCPs).

## How buying policies map to the AWS Marketplace API
<a name="buying-policies-api-concepts"></a>

Every buying policy is a `ProcurementPolicy` entity attached to an `Experience`. Its `PolicyType` determines what it does. You create and change buying policies with the `StartChangeSet` action, using the same `CreateProcurementPolicy` and `UpdateProcurementPolicy` change types that you use for a product curation policy. Buyer approvals also use two other entities: `TrustedActor` for approvers and `ApprovalWorkflow` for approval chains.

The following table maps the terms used in the AWS Management Console to the entities, fields, and change types in the AWS Marketplace Catalog API.


| Console term | API entity or field | Change types | 
| --- | --- | --- | 
| Procurement approval rule | A rule in `ApprovalConfiguration.Rules` of a `ProcurementPolicy` with the `PolicyType` of `AGREEMENT_APPROVAL_POLICY` | `CreateProcurementPolicy`<br />`UpdateProcurementPolicy` | 
| Require approval, Decline purchase | The rule's `Effect`: `REQUIRE_APPROVAL` or `AUTO_REJECT` | `CreateProcurementPolicy`<br />`UpdateProcurementPolicy` | 
| Approval criteria | The rule's `Conditions` | `CreateProcurementPolicy`<br />`UpdateProcurementPolicy` | 
| Approval routing: AWS Marketplace console (shown to buyers as Organization administrator) | A `REQUIRE_APPROVAL` rule with no `Workflows` | `CreateProcurementPolicy`<br />`UpdateProcurementPolicy` | 
| Approval routing: email approval chain | A rule whose `Workflows` names an `ApprovalWorkflow` with email approvers | `CreateProcurementPolicy`<br />`UpdateProcurementPolicy` | 
| Approval routing: external system | A rule whose `Workflows` names an `ApprovalWorkflow` whose only approver is a procurement system | `CreateProcurementPolicy`<br />`UpdateProcurementPolicy` | 
| Email approver | A `TrustedActor` entity with the `Type` of `EMAIL` | `CreateTrustedActor`<br />`VerifyTrustedActor`<br />`RevokeTrustedActor` | 
| Connected procurement system | A `TrustedActor` entity with the `Type` of `TOOL` | `CreateTrustedActor` | 
| Approval chain | An `ApprovalWorkflow` entity with the `WorkflowType` of `AGREEMENT_APPROVAL` | `CreateApprovalWorkflow`<br />`UpdateApprovalWorkflow` | 
| Approval level, and the spend amount where a level starts reviewing | An entry in the workflow's `Levels`, and its `AgreementValue` `GTE` condition | `CreateApprovalWorkflow`<br />`UpdateApprovalWorkflow` | 
| Mandatory purchase order settings | A `ProcurementPolicy` with the `PolicyType` of `PURCHASE_ORDER_POLICY` and its `MandatoryPurchaseOrderConfig` | `CreateProcurementPolicy`<br />`UpdateProcurementPolicy` | 
| Procurement administrator message | The `ProcurementMessage` field in the `Configuration` of the experience's `BrandingSettings` | `UpdateBrandingSettings` | 

## Prerequisites for buying policies
<a name="buying-policies-api-prerequisites"></a>

Before you configure buying policies with the AWS Marketplace Catalog API, complete the following setup.

1. **Create the private marketplace integration with AWS Organizations.** This one-time setup, from your management account, enables trusted access across your organization and creates the private marketplace service-linked role. If you already created the integration for private marketplace, skip this step. For the steps, see [Prerequisites for buying policies](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buying-policies.html#buying-policies-prerequisites) in the *AWS Marketplace Buyer Guide*.

1. **Identify the experience to attach your policies to.** Every buying policy is attached to an `Experience`, and it applies to the accounts in that experience's audience. When you configure buying policies in the AWS Management Console, AWS Marketplace creates an organization-wide experience for you if one doesn't exist. With the API, you attach each policy to an experience yourself:
   + To use an existing experience, call `ListEntities` with an `EntityType` of `Experience` and note its identifier.
   + To create one, create the experience, associate your organization (or the OUs or accounts that the policy applies to) as its audience, and enable it. For more information, see [Creating a private marketplace](work-with-private-marketplace.md#creating-a-private-marketplace) and [Associating principals to experiences](work-with-private-marketplace.md#private-marketplace-associate-accounts).

An experience can have at most one policy of each `PolicyType`, and you can't change a policy's type after you create it.

## Entity types defined by buying policies
<a name="entity-types-defined-by-buying-policies"></a>

The following table lists the entity types used by buying policies, their purpose, and the actions on which each can be specified. For more details on ARN formats, see [Catalog API entities](catalog-apis.md#catalog-api-entities).


| Entity | Purpose | Actions | 
| --- | --- | --- | 
| `ProcurementPolicy` | With the `PolicyType` of `AGREEMENT_APPROVAL_POLICY`, stores procurement approval rules. With `PURCHASE_ORDER_POLICY`, stores mandatory purchase order settings. | `StartChangeSet`<br />`DescribeEntity` | 
| `ApprovalWorkflow` | Stores an approval chain: its approval levels and approvers. | `StartChangeSet`<br />`DescribeEntity` | 
| `TrustedActor` | Stores an approver: an email approver or a connected procurement system. | `StartChangeSet`<br />`DescribeEntity` | 