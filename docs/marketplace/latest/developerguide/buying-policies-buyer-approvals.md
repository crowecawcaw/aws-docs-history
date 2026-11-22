

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Configuring buyer approvals

With buyer approvals, you can require approval before a purchase in AWS Marketplace is completed. You create procurement approval rules that decide which purchases need review and where each request is sent. When a buyer submits a purchase that matches a rule, AWS Marketplace sends an approval request to the rule's approvers. After every required approval is granted, AWS Marketplace creates the agreement. Purchases that don't match any rule don't need approval.

To configure buyer approvals with the AWS Marketplace Catalog API, complete the following steps in order:

1. Add the approvers. For email approvers, see [Adding email approvers](#private-marketplace-approvals-trusted-actors). For a procurement system, see [Connecting a procurement system](#buying-policies-api-connect-system).

1. Group email approvers into an approval chain. See [Creating an approval chain](#private-marketplace-approvals-workflows).

1. Create the rules that route purchases to the AWS Marketplace console, an approval chain, or a procurement system. See [Creating a procurement approval rule](#private-marketplace-approvals-policy).

Configuration changes are asynchronous. After each `StartChangeSet` call, poll `DescribeChangeSet` until the status is `SUCCEEDED` before you use the new entity in the next step.

## How buyer approvals work
<a name="buying-policies-api-approvals-concepts"></a>

Buyer approvals use the following building blocks.

Procurement approval rule  
Defines which purchases a rule applies to and what happens when a purchase matches. In the API, a rule is an entry in the `Rules` list of an `AGREEMENT_APPROVAL_POLICY`. Its `Conditions` are the approval criteria, and a purchase must match all of them. Its `Effect` is `REQUIRE_APPROVAL` (Require approval in the console) or `AUTO_REJECT` (Decline purchase in the console).

Approval routing  
Defines where a `REQUIRE_APPROVAL` rule sends its requests. A rule with no `Workflows` sends requests to the AWS Marketplace console, where your management account or delegated administrator reviews them. A rule whose `Workflows` names an approval chain sends requests to that chain's email approvers, or to the procurement system that is the chain's only approver.

Email approver  
A person who receives approval requests by email and acts on them through a secure link and a one-time passcode, without an AWS account. In the API, an email approver is a `TrustedActor` entity with the `Type` of `EMAIL`. An email approver must verify their email address before you add them to an approval chain.

Approval chain  
A reusable, ordered group of approvers organized into one or more approval levels. In the API, an approval chain is an `ApprovalWorkflow` entity. You can reference the same approval chain from multiple rules.

**Approval levels**  
An approval chain can have up to 6 levels, with up to 10 approvers at each level. Each level reviews the request in order, and the next level gets the request only after the current level approves it. If a level has more than one approver, only one of them needs to approve. Level 1 reviews every purchase that reaches the chain. For level 2 and later, you can set a spend amount where the level starts reviewing, so that larger purchases escalate to more approvers.

**When a purchase matches more than one rule**  
A purchase is checked against every rule. Each `REQUIRE_APPROVAL` rule that a purchase matches creates its own approval request, and every request must be approved before the agreement is created. If any request is declined, cancelled, or expires, the other requests for the purchase are cancelled. If a purchase matches an `AUTO_REJECT` rule, the purchase is declined, even if it also matches a `REQUIRE_APPROVAL` rule.

**Rule limit**  
Your organization can have up to 10 rules in total, across the approval policies on all of your experiences.

## Where approval rules apply
<a name="buying-policies-api-approvals-scope"></a>

An approval policy applies to purchases from the accounts in the audience of the experience that it's attached to:
+ To apply rules to your whole organization, attach the approval policy to an experience whose audience is your organization. Rules created on the **Procurement approval rules** page of the AWS Management Console are organization-wide rules of this kind.
+ To apply different rules to different parts of your organization, attach an approval policy to an experience that is associated with specific OUs or accounts. Organization-wide rules still apply to those accounts.

If an experience has no audience, the rules in its approval policy don't apply to any purchases until you associate an audience with it. For more information, see [Associating principals to experiences](work-with-private-marketplace.md#private-marketplace-associate-accounts).

## Adding email approvers
<a name="private-marketplace-approvals-trusted-actors"></a>

An email approver is a `TrustedActor` entity with the `Type` of `EMAIL`. A trusted actor's identifier has the prefix `trustedactor-`. To add an email approver, complete the following steps.

1. Call `StartChangeSet` with the `CreateTrustedActor` change type, the email address, and a display name. No email is sent yet.

   ```json
   POST /StartChangeSet HTTP/1.1
   Content-type: application/json
   
   {
     "Catalog": "AWSMarketplace",
     "ChangeSet":
     [
       {
         "ChangeType": "CreateTrustedActor",
         "Entity":
         {
           "Type": "TrustedActor@1.0"
         },
         "DetailsDocument":
         {
           "Type": "EMAIL",
           "Details":
           {
             "EmailAddress": "finance.approver@example.com",
             "Name": "Finance Approver"
           }
         }
       }
     ]
   }
   ```

1. Call `StartChangeSet` with the `VerifyTrustedActor` change type to send the verification email. Use the same change type later to resend it.

   ```json
   POST /StartChangeSet HTTP/1.1
   Content-type: application/json
   
   {
     "Catalog": "AWSMarketplace",
     "ChangeSet":
     [
       {
         "ChangeType": "VerifyTrustedActor",
         "Entity":
         {
           "Type": "TrustedActor@1.0",
           "Identifier": "trustedactor-1a2b3c4d5e6f7"
         }
       }
     ]
   }
   ```

1. Wait for the approver to open the link and verify their address. Then call `DescribeEntity` on the trusted actor and confirm that `VerificationStatus` is `VERIFIED` and `ActiveStatus` is `ACTIVE`. You can add only verified email approvers to an approval chain.

To remove an email approver, first update every approval chain that references it. Then call `StartChangeSet` with the `RevokeTrustedActor` change type.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "RevokeTrustedActor",
      "Entity":
      {
        "Type": "TrustedActor@1.0",
        "Identifier": "trustedactor-1a2b3c4d5e6f7"
      }
    }
  ]
}
```

**Note**  
You can't edit a trusted actor. To change an email address, revoke the trusted actor and create a new one. An email address can belong to only one trusted actor in your organization.  
Approver names and email addresses are personal data. They're returned only by `DescribeEntity`, to the owning account and the delegated administrator. `ListEntities` shows the owning account ID as the trusted actor's name.

## Creating an approval chain
<a name="private-marketplace-approvals-workflows"></a>

An approval chain is an `ApprovalWorkflow` entity. To create one, call `StartChangeSet` with the `CreateApprovalWorkflow` change type and a `WorkflowType` of `AGREEMENT_APPROVAL`. An approval chain's identifier has the prefix `approvalworkflow-`.

Each entry in `Levels` is an approval level, with the following settings:
+ `Name` – 1–50 characters: letters, digits, spaces, `_`, and `-`.
+ `Approvers` – 1–10 verified email approvers, referenced by trusted actor identifier. Any one of them can approve the level.
+ `ApprovalsRequired` – Always `ONE`.
+ `Conditions` – Optional, for level 2 and later. One `AgreementValue` `GTE` condition sets the spend amount where the level starts reviewing. Level 1 must not have conditions, and amounts must not decrease from one level to the next.

The following example creates a two-level approval chain in which, for example, a finance approver joins if the purchase value is USD 10,000 or more.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "CreateApprovalWorkflow",
      "Entity":
      {
        "Type": "ApprovalWorkflow@1.0"
      },
      "DetailsDocument":
      {
        "Name": "Finance chain",
        "Description": "Manager, then Finance for large purchases",
        "Definition":
        {
          "WorkflowType": "AGREEMENT_APPROVAL",
          "Detail":
          {
            "AgreementApprovalWorkflowDefinition":
            {
              "Levels":
              [
                {
                  "Name": "Manager",
                  "ApprovalsRequired": "ONE",
                  "Approvers": [ { "Identifier": "trustedactor-1a2b3c4d5e6f7" } ]
                },
                {
                  "Name": "Finance",
                  "ApprovalsRequired": "ONE",
                  "Conditions":
                  [
                    { "Attribute": "AgreementValue", "Operator": "GTE", "Value": 10000 }
                  ],
                  "Approvers": [ { "Identifier": "trustedactor-7g6f5e4d3c2b1" } ]
                }
              ]
            }
          }
        }
      }
    }
  ]
}
```

To change an approval chain, call `UpdateApprovalWorkflow`. The update replaces the entire `Definition`, so send all levels. You can't change the `WorkflowType`, and you can't delete an approval chain after you create it. Approval requests that are already in progress continue to use the version of the chain that was in effect when they started.

## Connecting a procurement system
<a name="buying-policies-api-connect-system"></a>

To route approval requests to your organization's procurement system, such as Coupa, SAP Ariba, or Jaggaer, represent the system as a `TrustedActor` entity with the `Type` of `TOOL`. Then make it the only approver in a single-level approval chain. The procurement system runs your own approval workflow and returns an approved purchase order to AWS Marketplace.

Before you create the trusted actor, set up the connection between AWS Marketplace and your procurement system. For more information, see [Integrating AWS Marketplace with procurement systems](https://docs.aws.amazon.com/marketplace/latest/buyerguide/procurement-system-integration.html) in the *AWS Marketplace Buyer Guide*.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "CreateTrustedActor",
      "Entity":
      {
        "Type": "TrustedActor@1.0"
      },
      "DetailsDocument":
      {
        "Type": "TOOL",
        "Details":
        {
          "ToolType": "COUPA"
        }
      }
    }
  ]
}
```

Supported values for `ToolType` are `COUPA`, `SAP_BUSINESS_NETWORK`, and `JAGGAER`.

Your organization can connect one procurement system at a time. To replace it, first update every approval chain that references its trusted actor. Then call `StartChangeSet` with the `RevokeTrustedActor` change type, and create a trusted actor for the new procurement system. A procurement system trusted actor must be the only approver in a single-level approval chain, and you can't combine it with email approvers.

## Creating a procurement approval rule
<a name="private-marketplace-approvals-policy"></a>

Procurement approval rules belong to an approval policy, which is a `ProcurementPolicy` entity with the `PolicyType` of `AGREEMENT_APPROVAL_POLICY`. Create the policy with `CreateProcurementPolicy`, and specify the experience that it applies to as the `Entity`. An experience can have one approval policy.

Each rule in `ApprovalConfiguration.Rules` has the following fields:
+ `Name` – 1–50 characters: letters, digits, spaces, `_`, and `-`.
+ `Conditions` – The approval criteria, up to 10. A purchase must match all of them. Omit `Conditions` for a rule that matches every purchase. An empty list is rejected.
+ `Effect` – `REQUIRE_APPROVAL` or `AUTO_REJECT`.
+ `Workflows` – The approval routing for a `REQUIRE_APPROVAL` rule: at most one approval chain identifier. Omit it to route requests to the AWS Marketplace console. An `AUTO_REJECT` rule must not name an approval chain.

The following table lists the conditions that you can use in rules.


| Attribute | Operators | Allowed values | Notes | 
| --- | --- | --- | --- | 
| `AgreementValue` | `GTE`, `LTE` | A number from 0 to 10,000,000,000,000 | Can appear at most twice in a rule to express a range. Requires a `CurrencyCode` condition in the same rule. | 
| `CurrencyCode` | `EQUALS` | `USD`, `EUR`, `GBP`, `AUD`, `JPY`, `CNY`, `CAD`, `INR`, `NZD`, `SGD`, `CLP` | One value. | 
| `DeliveryMethods` | `IN`, `NOT_IN` | `SaaS`, `Ami`, `ProfessionalServices`, `MachineLearning`, `Container` | Products with another delivery type never match a `DeliveryMethods` condition. | 
| `Manufacturers` | `IN`, `NOT_IN` | Up to 50 seller profile IDs, such as `seller-1a2b3c4d5e6f7` | Use the seller of record ID from the offer. | 
| `OfferTypes` | `IN`, `NOT_IN` | `PrivateOffer`, `PublicOffer` |   | 

Each attribute can appear once per rule, except `AgreementValue`, which can appear twice to express a range (for example, USD 1,000 to USD 10,000). Purchase amount conditions apply to one currency only, so create a separate rule for each currency.

The following example creates an approval policy with three rules. The first routes purchases of USD 10,000 and above to an approval chain. The second routes container products to the AWS Marketplace console. The third declines purchases from one seller.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "CreateProcurementPolicy",
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example"
      },
      "DetailsDocument":
      {
        "Name": "Purchase approvals",
        "PolicyType": "AGREEMENT_APPROVAL_POLICY",
        "ApprovalConfiguration":
        {
          "Rules":
          [
            {
              "Name": "High value to finance chain",
              "Effect": "REQUIRE_APPROVAL",
              "Workflows": [ "approvalworkflow-9z8y7x6w5v4u3" ],
              "Conditions":
              [
                { "Attribute": "CurrencyCode", "Operator": "EQUALS", "Value": "USD" },
                { "Attribute": "AgreementValue", "Operator": "GTE", "Value": 10000 }
              ]
            },
            {
              "Name": "Container products need admin approval",
              "Effect": "REQUIRE_APPROVAL",
              "Conditions":
              [
                { "Attribute": "DeliveryMethods", "Operator": "IN", "Value": [ "Container" ] }
              ]
            },
            {
              "Name": "Block one seller",
              "Effect": "AUTO_REJECT",
              "Conditions":
              [
                { "Attribute": "Manufacturers", "Operator": "IN", "Value": [ "seller-1a2b3c4d5e6f7" ] }
              ]
            }
          ]
        }
      }
    }
  ]
}
```

## Editing and deleting rules
<a name="buying-policies-api-manage-rules"></a>

To edit, add, or delete rules, call `StartChangeSet` with the `UpdateProcurementPolicy` change type on the approval policy. An update replaces all of the policy's rules. Call `DescribeEntity` on the policy, change the rules, and send the complete list. To delete a rule, leave it out of the list.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateProcurementPolicy",
      "Entity":
      {
        "Type": "ProcurementPolicy@2.0",
        "Identifier": "procpolicy-1234example"
      },
      "DetailsDocument":
      {
        "ApprovalConfiguration":
        {
          "Rules":
          [
            {
              "Name": "High value to finance chain",
              "Effect": "REQUIRE_APPROVAL",
              "Workflows": [ "approvalworkflow-9z8y7x6w5v4u3" ],
              "Conditions":
              [
                { "Attribute": "CurrencyCode", "Operator": "EQUALS", "Value": "USD" },
                { "Attribute": "AgreementValue", "Operator": "GTE", "Value": 25000 }
              ]
            }
          ]
        }
      }
    }
  ]
}
```

Approval requests that are already in progress aren't affected by rule changes.

## Viewing your buyer approvals configuration
<a name="private-marketplace-approvals-view"></a>

Use the following read actions to check your configuration.
+ `DescribeChangeSet` returns the status of a change and, for a failure, the reason in `ErrorDetailList`. For the error codes, see [Errors for buyer approvals](#buying-policies-error-codes).
+ `ListEntities` with an `EntityType` of `TrustedActor`, `ApprovalWorkflow`, or `ProcurementPolicy` lists what exists. You can filter trusted actors by type, approval chains by `WorkflowType` and `Approvers`, and policies by `PolicyType`.
+ `DescribeEntity` returns an approval policy's rules, an approval chain's levels, or a trusted actor's type and verification status. On an `Experience`, it returns `AgreementApprovalProcurementPolicies`.

## Managing approval requests
<a name="buying-policies-api-approval-requests"></a>

The change types in this section configure buyer approvals. Approval requests are created, approved, declined, and overridden at purchase time through the AWS Marketplace Agreement API. For information about managing approval requests, see [Configuring buyer approvals](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-approvals.html) in the *AWS Marketplace Buyer Guide*.

## Errors for buyer approvals
<a name="buying-policies-error-codes"></a>

The following errors are specific to the buyer approvals change types. They're returned in `ErrorDetailList` when you call `DescribeChangeSet` on a failed change set.


| Change type | Error code | Error message | Description | 
| --- | --- | --- | --- | 
| CreateTrustedActor | INVALID\_EMAIL | Email already used by another trusted actor in this organization. | Use a unique email address, or reuse the existing trusted actor. | 
| CreateTrustedActor | INCOMPATIBLE\_OPERATION\_CREATE\_TRUSTED\_ACTOR | A procurement tool is already connected or being connected, or no connectable procurement portal exists. | Only one procurement tool can be connected per organization. Revoke the existing tool trusted actor before creating a new one, or connect a supported procurement portal first. | 
| VerifyTrustedActor | INCOMPATIBLE\_OPERATION\_VERIFY\_TRUSTED\_ACTOR | The trusted actor is a procurement tool (which can't be verified) or is already verified. | Call `VerifyTrustedActor` only on email trusted actors that aren't already verified. | 
| RevokeTrustedActor | INCOMPATIBLE\_OPERATION\_REVOKE\_TRUSTED\_ACTOR | The trusted actor is still referenced by an approval workflow. | Update the approval workflows that reference the trusted actor first, then revoke it. | 
| CreateApprovalWorkflow, UpdateApprovalWorkflow | INVALID\_APPROVER\_ID | Approver is a missing or foreign trusted actor, or a procurement tool already assigned to another workflow. | Reference a trusted actor that exists in your organization. A procurement tool trusted actor can be used on only one approval workflow at a time. | 
| CreateApprovalWorkflow, UpdateApprovalWorkflow | INVALID\_APPROVER\_STATUS | The approver is revoked, or hasn't been verified. | Verify email trusted actors before you add them to a workflow, and remove revoked trusted actors from the workflow. | 
| CreateApprovalWorkflow, UpdateApprovalWorkflow | INVALID\_APPROVERS | A procurement tool shares its level or workflow with other approvers or levels, or a level lists the same approver twice. | A procurement tool must be the only approver in a single-level workflow. Each approver can appear only once per level. | 
| CreateApprovalWorkflow, UpdateApprovalWorkflow, CreateProcurementPolicy, UpdateProcurementPolicy | INVALID\_LEVELS | A level needs activation conditions because a lower level has them, the first level has conditions, a level threshold is lower than an earlier level's, or the workflow has too many levels. | Level 1 must not have conditions. Thresholds on later levels must be non-decreasing. A workflow can have up to 6 levels. | 
| UpdateApprovalWorkflow | INVALID\_DEFINITION | The `Definition` variant in the update doesn't match the workflow's `WorkflowType`. | Send a `Definition` whose variant matches the workflow's `WorkflowType`. You can't change `WorkflowType` after creation. | 
| CreateProcurementPolicy, UpdateProcurementPolicy | INVALID\_APPROVAL\_WORKFLOW\_ID | Approval workflow *[Id]* not found. Provide the ID of an existing approval workflow in your account. | A rule's `Workflows` references an approval workflow that doesn't exist or is owned by another account. | 
| CreateProcurementPolicy, UpdateProcurementPolicy | INVALID\_APPROVAL\_WORKFLOW\_TYPE | Approval workflow *[Id]* has WorkflowType *[actual]*, expected *[expected]*. | A rule's `Workflows` must reference a workflow whose `WorkflowType` is `AGREEMENT_APPROVAL`. | 
| CreateApprovalWorkflow, UpdateApprovalWorkflow, CreateProcurementPolicy, UpdateProcurementPolicy | INVALID\_CONDITION\_ATTRIBUTE | A condition uses an attribute that the context doesn't support. | Use an attribute that's allowed for the rule or level. See the conditions table in [Creating a procurement approval rule](#private-marketplace-approvals-policy). | 
| CreateApprovalWorkflow, UpdateApprovalWorkflow, CreateProcurementPolicy, UpdateProcurementPolicy | INVALID\_CONDITION\_OPERATOR | A condition uses an operator that the attribute doesn't support. | Use one of the operators listed for the attribute in the conditions table. | 
| CreateApprovalWorkflow, UpdateApprovalWorkflow, CreateProcurementPolicy, UpdateProcurementPolicy | INVALID\_CONDITION\_VALUE | A condition value has the wrong shape, type, range, count, or content. | Match the value's type and allowed set to the attribute (see the conditions table). | 
| CreateApprovalWorkflow, UpdateApprovalWorkflow, CreateProcurementPolicy, UpdateProcurementPolicy | INVALID\_CONDITIONS | Conditions in one rule conflict: an attribute repeats too often, bounds are inverted, or `AgreementValue` has no `CurrencyCode`. | Each attribute can appear once per rule, except `AgreementValue` (twice, to express a range). In a procurement approval rule, a condition on `AgreementValue` also requires a `CurrencyCode` condition. This requirement doesn't apply to approval level conditions in an approval chain. | 