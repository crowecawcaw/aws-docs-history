

# Configure a provisioning role for resource blueprints

A provisioning role is a dedicated IAM role that Amazon SageMaker Unified Studio uses to deploy blueprint resources. The provisioning role separates provisioning permissions from the project execution role that members use for their daily work, such as running queries and accessing data.

You can configure a provisioning role either for all blueprints across the account or for a specific blueprint. When you configure a provisioning role across the account, every blueprint uses the same provisioning role when it is deployed. When you configure a provisioning role for a specific blueprint, Amazon SageMaker Unified Studio uses that role only when deploying that blueprint.

Amazon SageMaker Unified Studio selects the provisioning role to use as follows:
+ If a blueprint has its own provisioning role, that role takes precedence.
+ Otherwise, Amazon SageMaker Unified Studio uses the account-wide provisioning role.
+ If no provisioning role is configured, Amazon SageMaker Unified Studio falls back to the project execution role.

**Note**  
The role that you choose needs permissions to create the resources that your blueprints define.

## Set a provisioning role for all blueprints in the account
<a name="provisioning-role-all-blueprints"></a>

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the navigation pane, choose **Accounts**.

1. For **Domain account settings**, choose **Edit**.

1. Choose the **IAM roles** tab.

1. Choose **Edit**.

1. Under **Provisioning role usage**, select the checkbox.

1. Choose a provisioning role.

1. Choose **Save**.

![Edit provisioning role for all blueprints in the account in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/resource-blueprints/resource-blueprints-provisioning.png)


## Set a provisioning role for a specific blueprint
<a name="provisioning-role-per-blueprint"></a>

You can set a provisioning role for a specific blueprint only through the API. After you change the provisioning role through the API, the user interface shows the provisioning role. To view the provisioning role for a blueprint, use the following procedure.

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the navigation pane, choose **Blueprints**.

1. Choose the blueprint from the list of blueprints.

1. Choose the **Authorization** tab.

1. In the **Account authorization** table, choose an account. The provisioning role appears in the **Provisioning role** section.

The following example AWS CLI command updates the provisioning role for a blueprint:

```bash
aws datazone put-environment-blueprint-configuration \
    --domain-identifier {{{domain-id}}} \
    --environment-blueprint-identifier {{{blueprint-id}}} \
    --enabled-regions {{{enabledRegions}}} \
    --provisioning-role-arn arn:aws:iam::111122223333:role/service-role/AmazonDataZoneProvisioning-111122223333 \
    --region {{{region}}}
```