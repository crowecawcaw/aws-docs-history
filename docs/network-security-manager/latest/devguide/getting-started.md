

# Deploy your first network security protection
<a name="getting-started"></a>

This tutorial walks you through deploying an AWS WAF web ACL using the AWS Network Security Manager console. You complete the following steps:

1. Create a rule

1. Create a template

1. Create a policy

1. Create a scope

1. Create and publish a deployment

1. Monitor synchronization status

In this tutorial, you create an AWS WAF web ACL that protects Application Load Balancers across your selected accounts. This process is largely identical for all security services and firewalls supported by AWS Network Security Manager.

**Time to complete:** approximately 10 minutes

**Cost:** This tutorial uses AWS services that might incur charges. For current pricing, see [AWS Network Security Manager pricing](https://aws.amazon.com/network-security-manager/pricing/) on the AWS website.

## Prerequisites
<a name="getting-started-prerequisites"></a>

Before you begin, verify that you meet the following requirements:
+ Completed setup steps as described in [Setting up AWS Network Security Manager](setting-up.md).
+ An AWS Identity and Access Management (IAM) identity with AWS Network Security Manager permissions.
+ An AWS Organizations organization with all features enabled and a designated AWS Network Security Manager administrator account (required for multi-account deployments).
+ Access to the AWS Network Security Manager console.

## Step 1: Create a rule
<a name="getting-started-step1"></a>

A rule is the building block of your security configuration. In this step, you create two AWS WAF rules: one that sets the default action and one that sets the visibility configuration. Default Action and VisibilityConfig are required fields for an AWS WAF web ACL.

To create the Default Action rule, follow these steps:

1. Open the AWS Network Security Manager console at [https://console.aws.amazon.com/network-security-manager/](https://console.aws.amazon.com/network-security-manager/).

1. In the navigation pane, choose **Overview**.

1. On the Overview page, choose **Create rule**.

1. For **Rule name**, enter a descriptive name, such as `my-default-action-rule`.

1. In the **Rule definition** section, for **Firewall type**, choose **AWS WAF**.

1. For **Select type of rule**, choose **Configuration**.

1. Choose **Insert config types**, then select **Default Action**. A JSON editor appears with a default configuration.

1. In the JSON editor, remove the `Block` section and keep only the `Allow` section.

1. Choose **Create rule**.

To create the VisibilityConfig rule, follow these steps:

1. In the navigation pane, choose **Overview**.

1. On the Overview page, choose **Create rule**.

1. For **Rule name**, enter a descriptive name, such as `my-visibility-config-rule`.

1. In the **Rule definition** section, for **Firewall type**, choose **AWS WAF**.

1. For **Select type of rule**, choose **Configuration**.

1. Choose **Insert config types**, then select **VisibilityConfig**. A JSON editor appears with a default configuration.

1. Choose **Create rule**.

**AWS CLI alternative**  
You can also create rules with the AWS CLI:  

```
aws network-security-manager create-rule \
    --rule-name "my-default-action-rule" \
    --firewall-type WAF \
    --rule-type CONFIGURATION \
    --configuration '{"DefaultAction": {"Allow": {}}}' \
    --is-published true

aws network-security-manager create-rule \
    --rule-name "my-visibility-config-rule" \
    --firewall-type WAF \
    --rule-type CONFIGURATION \
    --configuration '{"VisibilityConfig": {"SampledRequestsEnabled": true, "CloudWatchMetricsEnabled": true, "MetricName": "my-web-acl-metric"}}' \
    --is-published true
```

## Step 2: Create a template
<a name="getting-started-step2"></a>

A template groups one or more rules for reuse across policies. In this step, you create a template that includes the rule from Step 1:

1. In the navigation pane, choose **Overview**.

1. On the Overview page, choose **Create template**.

1. For **Template name**, enter a descriptive name, such as `my-waf-template`.

1. For **Firewall type**, choose **AWS WAF**.

1. In the **Rules** section, choose **Add rule** and select the rules you created in Step 1.

1. Choose **Create template**.

**AWS CLI alternative**  
You can also create a template with the AWS CLI:  

```
aws network-security-manager create-template \
    --template-name "my-waf-template" \
    --firewall-type WAF \
    --associated-rule-list '[{"ruleIdentifier": "{{rule-arn-from-step-1}}"}]' \
    --is-published true
```

## Step 3: Create a policy
<a name="getting-started-step3"></a>

A policy combines templates with enforcement settings. In this step, you create a policy that references your template and enables automatic remediation:

1. In the navigation pane, choose **Overview**.

1. On the Overview page, choose **Create policy**.

1. For **Policy name**, enter a descriptive name, such as `my-waf-policy`.

1. For **Firewall type**, choose **AWS WAF**.

1. In the **Policy priority** section, existing policies and their priorities display. Review the new policy's priority. If you need to adjust it, choose the priority field and change the value to `1` or any unused priority number.

1. In the **Templates and rules** section, choose **Add template** and select the template you created in Step 2.

1. For **Remediation**, select **Enabled**.

1. For **Existing customer web ACL resolution**, choose **No remediation**.

1. Choose **Create policy**.

**AWS CLI alternative**  
You can also create a policy with the AWS CLI:  

```
aws network-security-manager create-policy \
    --policy-name "my-waf-policy" \
    --firewall-type WAF \
    --priority 1 \
    --associated-template-and-rule-list '[{"templateIdentifier": "{{template-arn-from-step-2}}"}]' \
    --policy-configuration '{"remediationEnabled": true, "resourcesCleanUp": false, "wafConfig": {"existingCustomerWebACLResolution": "NO_REMEDIATION"}}' \
    --is-published true
```

## Step 4: Create a scope
<a name="getting-started-step4"></a>

A scope defines where your protections apply. In this step, you create a scope that targets Application Load Balancers in your accounts:

1. In the navigation pane, choose **Overview**.

1. On the Overview page, choose **Create scope**.

1. For **Scope name**, enter a descriptive name, such as `my-alb-scope`.

1. (Optional) In the **Account and organizational unit selection** section, for **Select method of controlling administrative scope**, select **Scope to entire AWS Organization (all OUs and accounts)**. Skip this step for single-account deployments.

1. In the **Resources** section, for **Resource types**, select **Application Load Balancer**.

1. Choose **Create scope**.

**AWS CLI alternative**  
You can also create a scope with the AWS CLI:  

```
aws network-security-manager create-scope \
    --scope-name "my-alb-scope" \
    --scope-configuration '{
        "accountFilter": {"includeAll": {}},
        "resourceScopes": {
            "AWS::ElasticLoadBalancingV2::LoadBalancer::application": {
                "includeAll": true
            }
        }
    }' \
    --is-published true
```

## Step 5: Create and publish a deployment
<a name="getting-started-step5"></a>

A deployment binds policies to a scope and activates enforcement. To create and publish a deployment:

1. In the navigation pane, choose **Overview**.

1. On the Overview page, choose **Create deployment**.

1. For **Deployment name**, enter a descriptive name, such as `my-first-deployment`.

1. In the **Policies** section, choose **Add policy** and select the policy you created in Step 3.

1. In the **Scopes** section, choose **Add scope** and select the scope you created in Step 4.

1. Choose **Create deployment**.

AWS Network Security Manager begins discovering resources and applying protections. This process is asynchronous and might take a few minutes to complete.

**AWS CLI alternative**  
You can also create and publish a deployment with the AWS CLI:  

```
aws network-security-manager create-deployment \
    --deployment-name "my-first-deployment" \
    --associated-policy-list '[{"policyIdentifier": "{{policy-arn-from-step-3}}"}]' \
    --associated-scope-list '[{"scopeIdentifier": "{{scope-arn-from-step-4}}"}]' \
    --deployment-configuration '{"enableCrossAccountVisibility": true}' \
    --is-published true
```

## Step 6: Monitor synchronization status
<a name="getting-started-step6"></a>

After you publish a deployment, AWS Network Security Manager discovers resources and synchronizes their configurations. To monitor the status of each resource:

1. In the navigation pane, choose **Overview**.

1. Choose the **Deployments** tab.

1. Choose the deployment you created in Step 5.

1. Choose the **Synchronization** tab.

1. Review the synchronization status for each resource:
   + **IN\_SYNC** – The resource configuration matches your intended protection settings.
   + **OUT\_OF\_SYNC** – The resource configuration does not match. AWS Network Security Manager remediates this automatically when remediation is enabled.
   + **NOT\_APPLICABLE** – The resource is in scope but cannot be evaluated by this deployment.

**AWS CLI alternative**  
You can also check synchronization status with the AWS CLI:  

```
aws network-security-manager list-resource-synchronization-statuses \
    --deployment-identifier "{{deployment-arn-from-step-5}}"
```

## Step 7: Clean up
<a name="getting-started-cleanup"></a>

If you no longer need the resources you created, delete them in reverse order to stop enforcement and remove protections from in-scope resources:

The reverse order matters because these resources reference each other. To see what is associated with a resource before you delete it, call `ListResourceAssociations` with that resource's ARN. It returns each associated resource's ARN and resource type. For more information, see the [AWS Network Security Manager API Reference](https://docs.aws.amazon.com/network-security-manager/latest/APIReference/).

1. In the navigation pane, choose **Overview**. Choose the **Deployments** tab. Select your deployment, choose **Action**, then choose **Delete**.

1. Choose the **Scopes** tab. Select your scope, choose **Action**, then choose **Delete**.

1. Choose the **Policies** tab. Select your policy, choose **Action**, then choose **Delete**.

1. Choose the **Templates** tab. Select your template, choose **Action**, then choose **Delete**.

1. Choose the **Rules** tab. Select your rule, choose **Action**, then choose **Delete**.

**AWS CLI alternative**  
Before you delete a resource, check its associations to plan the delete order:  

```
aws network-security-manager list-resource-associations \
    --resource-arn "{{resource-arn}}"
```
If a resource still has associations, remove or delete the associated resources first.  
You can delete resources with the AWS CLI in reverse order:  

```
aws network-security-manager delete-deployment \
    --deployment-identifier "{{deployment-arn}}"

aws network-security-manager delete-scope \
    --scope-identifier "{{scope-arn}}"

aws network-security-manager delete-policy \
    --policy-identifier "{{policy-arn}}"

aws network-security-manager delete-template \
    --template-identifier "{{template-arn}}"

aws network-security-manager delete-rule \
    --rule-identifier "{{rule-arn}}"
```

## Next steps
<a name="getting-started-next-steps"></a>

Now that you have a working deployment, explore the following ways to expand your network security protection:
+ Learn about the resource model and lifecycle in [How AWS Network Security Manager works](concepts.md).
+ Use the draft/publish workflow to stage changes before they take effect. For more information, see [Draft and Active lifecycle](concepts.md#concepts-lifecycle).
+ Create snapshots to preserve known-good configurations. For more information, see [Versioning](concepts.md#concepts-snapshots).
+ Use `GenerateRuleConfiguration` to create rules from natural-language descriptions. For more information, see the [AWS Network Security Manager API Reference](https://docs.aws.amazon.com/network-security-manager/latest/APIReference/).
+ Explore managing AWS WAF and AWS Shield Advanced protections across your organization. For more information, see [Managing firewalls and security services](managing-firewalls-security-services.md).