

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Access control for the AWS Marketplace Agreement API
<a name="agreement-api-access-control"></a>

To manage agreements in AWS Marketplace using the Agreement Service, you must ensure that your AWS Identity and Access Management (IAM) policies and roles are set up. Users must have the following policies/permissions to allow them to carry out the actions:
+ `CreateAgreementRequest` – Grants permission to users to start a new request to create a new agreement or update an existing agreement.
+ `AcceptAgreementRequest` – Grants permission to users to accept a previously created request to materialize into an agreement. Note: While accepting the agreement request, if users provide purchase orders, they will need to have `UpdatePurchaseOrders` permission as well to perform the action.
+ `GetAgreementEntitlements` – Grants permission to users to list the entitlements of an agreement.
+ `CancelAgreement` – Grants permission to users to cancel an active agreement they participate in.
+ `ListAgreementCharges` – Grants permission to users to list charges for an agreement.
+ `UpdatePurchaseOrders` – Grants permission to users to update purchase orders for agreement charges.
+ `SendAgreementCancellationRequest` – Grants permission to users to send a cancellation request.
+ `AcceptAgreementCancellationRequest` – Grants permission to users to accept a cancellation request initiated by the seller for an agreement they participate in as acceptor. Note: Users also need `CancelAgreement` permission because approving the cancellation request leads to agreement cancellation.
+ `RejectAgreementCancellationRequest` – Grants permission to users to reject a cancellation request initiated by the seller for an agreement they participate in as acceptor.
+ `SendAgreementPaymentRequest` – Grants permission to users to send a payment request.
+ `AcceptAgreementPaymentRequest` – Grants permission to users to accept a payment request initiated by the seller for an agreement they participate in as acceptor.
+ `RejectAgreementPaymentRequest` – Grants permission to users to reject a payment request initiated by the seller for an agreement they participate in as acceptor.
+ `GetAgreementCancellationRequest` – Grants permission to users to retrieve detailed information about a specific cancellation request for an agreement they participate in as acceptor.
+ `ListAgreementCancellationRequests` – Grants permission to users to list cancellation requests for agreements they participate in as acceptor.
+ `GetAgreementPaymentRequest` – Grants permission to users to retrieve detailed information about a specific payment request for an agreement they participate in as acceptor.
+ `ListAgreementPaymentRequests` – Grants permission to users to list payment requests for agreements they participate in as acceptor.
+ `DescribeAgreement` – Grants permission to users to obtain detailed metadata about any of their agreements.
+ `GetAgreementTerms` – Grants permission to users to obtain details about the terms of an agreement.
+ `SearchAgreements` – Grants permission to users to search through all their agreements.

**Note**  
For more information about these permissions, see [Policies and permissions for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html) in the *AWS Marketplace Seller Guide* and [Controlling access to AWS Marketplace subscriptions](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html) in *AWS Marketplace Buyer Guide*.

## Allowing actions with AWS managed policies
<a name="agreement-aws-managed-policies"></a>

AWS Marketplace defines persona specific managed policies. You can use managed policies for your IAM identities which will by-default narrows down the scope of the policy for specified role. Using managed policy will allow you to follow best practices and receive policy updates as new features became available in Marketplace.

For more information about these permissions, see [Policies and permissions for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html) in the *AWS Marketplace Seller Guide* and [Controlling access to AWS Marketplace subscriptions](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html) in *AWS Marketplace Buyer Guide*.

You're not limited to the permissions in the AWS managed policies that are described here. You can use IAM to create policies with custom permissions and then add those policies to IAM roles. For more information, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) and [Adding IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

## Allowing actions with customer managed policies
<a name="agreement-customer-managed-policies"></a>

You can also define a customer managed policy to control access to Agreement service APIs. You can customize the policy with mix of effect, actions and supported conditions.

To access the AWS Marketplace Agreements API for managing the product subscriptions, you can create following policy to allow access.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:CreateAgreementRequest",
        "aws-marketplace:AcceptAgreementRequest"
      ],
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws-marketplace:AgreementType": ["PurchaseAgreement"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:CancelAgreement",
        "aws-marketplace:GetAgreementEntitlements",
        "aws-marketplace:UpdatePurchaseOrders",
        "aws-marketplace:ListAgreementCharges"
      ],
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws-marketplace:AgreementType": ["PurchaseAgreement"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:AcceptAgreementCancellationRequest",
        "aws-marketplace:RejectAgreementCancellationRequest",
        "aws-marketplace:GetAgreementCancellationRequest",
        "aws-marketplace:ListAgreementCancellationRequests",
        "aws-marketplace:CancelAgreement"
      ],
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws-marketplace:AgreementType": ["PurchaseAgreement"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:AcceptAgreementPaymentRequest",
        "aws-marketplace:RejectAgreementPaymentRequest",
        "aws-marketplace:GetAgreementPaymentRequest",
        "aws-marketplace:ListAgreementPaymentRequests"
      ],
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws-marketplace:AgreementType": ["PurchaseAgreement"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:DescribeAgreement",
        "aws-marketplace:SearchAgreements",
        "aws-marketplace:GetAgreementTerms"
      ],
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws-marketplace:AgreementType": ["PurchaseAgreement"]
        },
        "StringEquals": {
          "aws-marketplace:PartyType": "Acceptor"
        }
      }
    }
  ]
}
```

## Customizing the policy with service defined condition keys
<a name="agreement-condition-keys"></a>

### Using AgreementType condition key
<a name="agreement-condition-agreementtype"></a>

Below statement limits the access to `UpdatePurchaseOrders` operation only for `PurchaseAgreement` agreement type.

```
{
  "Effect": "Allow",
  "Action": [
    "aws-marketplace:UpdatePurchaseOrders"
  ],
  "Resource": "*",
  "Condition": {
    "ForAllValues:StringEquals": {
      "aws-marketplace:AgreementType": ["PurchaseAgreement"]
    }
  }
}
```

### Using ProductId condition key
<a name="agreement-condition-productid"></a>

Below statement limits the access to `CreateAgreementRequest` and `AcceptAgreementRequest` to only specified AWS Marketplace product ids. You can include this statement to allow creating only pre-approved product ids, such as limiting to Bedrock foundational models.

```
{
  "Effect": "Allow",
  "Action": [
    "aws-marketplace:CreateAgreementRequest",
    "aws-marketplace:AcceptAgreementRequest"
  ],
  "Resource": "*",
  "Condition": {
    "ForAnyValue:StringEquals": {
      "aws-marketplace:ProductId": [
        "model-product-id-1",
        "model-product-id-2"
      ]
    }
  }
}
```

### Using PartyType condition key
<a name="agreement-condition-partytype"></a>

Below statement grants the access to read details of any agreement if the user is proposer of the agreement.

```
{
  "Effect": "Allow",
  "Action": [
    "aws-marketplace:DescribeAgreement"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "aws-marketplace:PartyType": "Proposer"
    }
  }
}
```