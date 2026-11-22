

# Grant members access to deploy resource blueprints

Blueprint authorization grants link designations to blueprints. A member whose designation is granted a blueprint can deploy that blueprint from the resource gallery in any project where the member holds that designation.

You can apply a grant for a blueprint either across all accounts or for a specific account. When you apply a grant across all accounts, the blueprint can be deployed in any associated account or the domain account.

A grant consists of a designation and a domain unit. The option to select a domain unit appears only when the domain has at least one child domain unit. Otherwise, the grant uses the root domain unit.

![Blueprint account authorization and grants in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/resource-blueprints/resource-blueprints-authorization.png)


**Note**  
Deploying a blueprint requires the designation to include the **Manage Environments** permission.  
For information about managing the designations that grants reference, see [Designations](designations.md).

**Note**  
You can create up to 20 grants.

## Create a grant for a blueprint in all accounts
<a name="grant-deploy-all-accounts"></a>

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the navigation pane, choose **Blueprints**.

1. Choose a blueprint from the list of blueprints.

1. Choose the **Authorization** tab.

1. In the **Account authorization** table, choose **All accounts**.

1. Choose **Add** to add a grant.

1. Select one or more existing designations.

1. If the domain has at least one child domain unit, select a domain unit. If no domain unit dropdown appears, the grant uses the root domain unit.

1. Choose **Add**.

## Create a grant for a blueprint in a specific account
<a name="grant-deploy-specific-account"></a>

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the navigation pane, choose **Blueprints**.

1. Choose a blueprint from the list of blueprints.

1. Choose the **Authorization** tab.

1. In the **Account authorization** table, choose an account.

1. Choose **Add** to add a grant.

1. Select one or more existing designations.

1. If the domain has at least one child domain unit, select a domain unit. If no domain unit dropdown appears, the grant uses the root domain unit.

1. If a grant was previously created for all accounts, the **Grants for all accounts** table shows those grants.

1. Choose **Add**.