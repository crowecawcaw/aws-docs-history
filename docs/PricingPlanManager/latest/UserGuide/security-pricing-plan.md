# Managing Access to AWS Flat-Rate Plans

You can use AWS Identity and Access Management (IAM) to control access to AWS Flat-Rate Plans. The namespace for Flat-Rate Plans is `pricingplanmanager`.

## Available Actions

The following table lists the `pricingplanmanager` actions you can perform in the console and specify in an IAM policy to allow or deny specific operations:

| Action                                | Description                                                     |
| ------------------------------------- | --------------------------------------------------------------- |
| AssociateResourcesToSubscription      | Grants permission to associate resources with a subscription    |
| CancelSubscription                    | Grants permission to cancel a subscription                      |
| CancelSubscriptionChange              | Grants permission to cancel a pending change for a subscription |
| CreateSubscription                    | Grants permission to create a subscription                      |
| DisassociateResourcesFromSubscription | Grants permission to disassociate resources from a subscription |
| GetSubscription                       | Grants permission to get the details for a subscription         |
| ListSubscriptions                     | Grants permission to list subscriptions in your account         |
| UpdateSubscription                    | Grants permission to update a subscription                      |

For information about how to create an IAM policy, see [Creating IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the IAM User Guide.
