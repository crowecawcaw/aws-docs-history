

# How AWS Network Security Manager works
<a name="concepts"></a>

Use the AWS Network Security Manager resource model to design and manage network security protections for resources in a single account or across multiple accounts in your organization. This chapter explains the five resource types, how they form a hierarchy, and the key concepts that govern their behavior.

## AWS Network Security Manager resource model
<a name="concepts-resource-model"></a>

AWS Network Security Manager uses five resource types arranged in a composition hierarchy:

![Rules and templates are contained within policies. A deployment joins policies to a scope.](https://docs.aws.amazon.com/network-security-manager/latest/devguide/images/nsm-resource-model.png)


Resources reference each other upward through the hierarchy. *Rules* are used within *templates* and *policies*. *Templates*, *rules*, or both are used within *policies*. A *scope* references the resources that *policies* protect within a *deployment*.

The following sections describe each resource type in the hierarchy.

**Rule** – The atomic unit of network security configuration. There are two types of rules – traffic inspection rules and firewall configuration rules. Traffic inspection focuses on how the security service addresses traffic. A configuration rule specifies system operations outside traffic inspection. The structure of a rule varies by firewall type.

**Template** – An ordered, reusable group of *rules* for a single firewall type. Use templates to package related rules together and share them across multiple *policies*. Templates are optional.

**Policy** – Combines an ordered set of *templates* and *rules* with enforcement settings for a firewall type. Each policy carries a priority (a lower number indicates a higher priority). When multiple policies protect the same resource, priority determines how conflicts resolve. For traffic inspection rules, priority determines the order in which rules are aggregated. For firewall configuration rules, priority determines which configuration applies for each resource and its in-scope policies.

**Scope** – A declarative selection of where protections apply. A scope specifies which resource types to protect, and you can optionally filter resources by tag or configuration attribute. In multi-account mode, a scope also specifies which accounts or OUs to include or exclude. In single-account mode, the scope applies to the account itself. A scope's mode is fixed when you create it. You can't switch a scope between multi-account and single-account modes in either direction, so a multi-account scope can never become a single-account scope, or the reverse.

**Deployment** – Binds one or more *policies* to a *scope*. Publishing a deployment activates enforcement. AWS Network Security Manager discovers resources in the scope, computes the intended configuration, and optionally remediates out-of-sync resources.

For resource composition limits, see [AWS Network Security Manager quotas](quotas.md).

## AWS Network Security Manager resource lifecycle, merging, and synchronization
<a name="concepts-key-concepts"></a>

The following sections explain the behaviors and mechanisms that govern how AWS Network Security Manager resources operate after you create them.

### Draft and Active lifecycle
<a name="concepts-lifecycle"></a>

Every AWS Network Security Manager resource – including rules, templates, policies, scopes, and deployments – has a status of either Draft or Active:
+ **Active** – The default status. The resource is published and available for use. Other resources can reference it, and deployments that include it enforce its configuration.
+ **Draft** – The resource is saved but not yet active. Draft resources are not enforced and cannot be referenced by other resources. When you create or update a resource, choose **Save draft** to keep it in draft status.

By default, AWS Network Security Manager creates resources as Active. To create a resource as Draft using the API, set the `isPublished` parameter to `false` in the create or update operation.

When you update a resource, the following scenarios apply:


| Current state | Action | Result | 
| --- | --- | --- | 
| Draft | Choose Save draft | Update the draft (remains Draft) | 
| Draft | Choose Publish | Publish the draft (becomes Active) | 
| Active | Choose Publish | Update and remain active (Active) | 
| Active | Choose Save draft | Create a draft overlay (becomes Draft with an Active resource underneath) | 

The `hasPublishedVersion` field appears on list and get responses. This field tells you whether a published Active resource exists beneath a draft. When a resource has the Draft status and `hasPublishedVersion: true`, a pending draft sits on top of a live, published Active resource.

You cannot delete an Active resource that another Active resource references.

### Versioning
<a name="concepts-snapshots"></a>

Every AWS Network Security Manager resource – including rules, templates, policies, scopes, and deployments – can be versioned. To create a version of an Active resource, select the resource, choose **Action**, then choose **Create versioned snapshot**. Versions are not created automatically on every update.

**AWS CLI alternative**  
You can also create a version using the `Create{Resource}Snapshot` API operation on an Active resource.

Key version properties:
+ Each version has a unique number (a sequential integer) and a version-qualified ARN (for example, `arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123:3`).
+ Versions are immutable. They cannot be updated.
+ You can create up to 10 versions per resource.
+ Versions are taggable.

Use versions to preserve desired configuration variants. To roll back a resource, read a version, then update the live resource with the version's desired configuration.

### Priority-based policy merging
<a name="concepts-priority"></a>

When multiple policies protect the same resource, AWS Network Security Manager merges their configurations into a single result. A lower priority number indicates a higher priority (priority 1 takes precedence over priority 2). When AWS Network Security Manager merges policies that contain traffic inspection rules, priority determines the order in which the rules are aggregated. For firewall configuration rules, the higher-priority policy determines which configuration applies.

AWS Network Security Manager evaluates priority at two levels, in this order:

1. *Administrator priority* – AWS Network Security Manager evaluates administrator priority first. Each organization administrator is assigned a priority, as described in [Administrator and member accounts](#concepts-admin-accounts). When AWS Network Security Manager merges policies, it ranks an administrator policy higher than a member account's own single-account policy. If an administrator policy and a member account's single-account policy both apply to a resource and conflict, the administrator policy's configuration wins. A member account cannot opt out of, override, or exempt itself from an administrator policy.

1. *Policy priority* – Within each account, AWS Network Security Manager then uses policy priority to resolve remaining conflicts. Policy priority values are integers starting from 1 and must be unique per account.

You set the administrator priority with the required `priority` field on the `PutAdminAccount` operation, an integer from 1 to 10. Priority values are unique, so two administrators never share a priority and no tie-breaking is required. For more information, see the [AWS Network Security Manager API Reference](https://docs.aws.amazon.com/network-security-manager/latest/APIReference/).

The merged result of all applicable policies for a resource is the *effective firewall configuration*. AWS Network Security Manager computes this configuration, compares it to the resource's actual configuration, and reports any differences as synchronization status.

When policies conflict, AWS Network Security Manager compares each attribute and applies the value from the higher-priority policy. If the higher-priority policy does not define an attribute, the lower-priority policy value applies. A resource that matches the effective configuration is IN\_SYNC. A resource protected by a lower-priority policy whose settings were overridden by a higher-priority policy reports as OUT\_OF\_SYNC for the lower-priority deployment. This is expected behavior, not a failure.

### Resource discovery with AWS Config
<a name="concepts-config-recorder"></a>

AWS Network Security Manager discovers protected resources in your accounts using a service-linked AWS Config configuration recorder. This recorder is created automatically in each account when that account enters scope of a deployment. Unlike AWS Firewall Manager, you do not need to perform any additional setup. AWS Config usage by AWS Network Security Manager is not charged to the AWS Network Security Manager customer.

Key characteristics of the service-linked recorder:
+ It is named `AWSConfigurationRecorderForNetworkSecurityManager`.
+ It is separate from any customer-managed configuration recorder in the account.
+ It records only the resource types relevant to your active scopes and deployments.
+ You do not need to set up AWS Config or create a configuration recorder. AWS Network Security Manager manages this automatically. AWS Config usage by AWS Network Security Manager is not charged to the customer.
+ You cannot modify or delete the recorder while it is in use. AWS Network Security Manager manages its lifecycle automatically.

You do not need to enable or configure AWS Config manually for AWS Network Security Manager to function. The service handles resource discovery automatically after you publish a deployment.

### Synchronization and remediation
<a name="concepts-synchronization"></a>

Enforcement in AWS Network Security Manager is asynchronous and eventually consistent. After you publish a deployment, or when a resource changes, the following stages occur:

1. **Resource discovery** – AWS Network Security Manager discovers resources in scope using a service-linked AWS Config recorder.

1. **Configuration computation** – For each discovered resource, AWS Network Security Manager computes the effective firewall configuration by merging all applicable policies by priority.

1. **Synchronization evaluation** – AWS Network Security Manager compares the effective configuration to the resource's actual configuration and records a synchronization status.

1. **Remediation** (optional) – If you set `remediationEnabled` on the policy, AWS Network Security Manager corrects out-of-sync resources to match the effective configuration.

Each stage is asynchronous. Consequences for your workflow:
+ There is a delay between publishing a deployment and resources becoming protected.
+ There is a delay between creating a new resource in scope and it being protected.
+ The `Last Checked` timestamp on synchronization status entries tells you when AWS Network Security Manager last evaluated a resource.

Remediation and resource cleanup are policy-level settings. You configure each one per policy in the `policyConfiguration` object.

`remediationEnabled`  
Specifies whether AWS Network Security Manager automatically remediates noncompliant resources. When you enable this setting, AWS Network Security Manager corrects out-of-sync resources to match the effective configuration.

`resourcesCleanUp`  
Specifies whether AWS Network Security Manager automatically removes the resources it created when they are no longer needed. AWS Network Security Manager deletes a firewall it created when you remove the deployment, or when the account or resource goes out of scope.

The `remediationEnabled` and `resourcesCleanUp` settings both default to `false`. AWS Network Security Manager does not remediate or clean up resources until you enable these settings. The `policyConfiguration` object also holds `wafConfig`, which applies to AWS WAF policies. For more information, see the [AWS Network Security Manager API Reference](https://docs.aws.amazon.com/network-security-manager/latest/APIReference/).

When a resource is out of sync, the synchronization status includes out-of-sync reasons with per-setting details that show expected values compared to actual values. The reasons are organized into the following categories:
+ `missingFirewall` – No firewall protection is associated with the resource.
+ `invalidFirewall` – A firewall exists but its configuration differs from the effective configuration. This includes six detail buckets: `incorrectSingleValueConfigurations`, `missingAppendableConfigurationValues`, `unexpectedAppendableConfigurationValues`, `incorrectAppendableConfigurationOrder`, `missingMergeableConfigurationValues`, and `unexpectedMergeableConfigurationValues`.

If remediation is enabled but AWS Network Security Manager cannot fix a resource, the `remediationIssues` field provides an `issueType`, a `message` describing the problem, and a `correctiveAction` suggesting how to resolve it.

AWS Network Security Manager does not evaluate settings that it does not manage. If a field does not appear in any contributing rule, AWS Network Security Manager ignores it during synchronization evaluation.

### Administrator and member accounts
<a name="concepts-admin-accounts"></a>

AWS Network Security Manager uses a cross-account management model built on AWS Organizations:
+ **Administrator account** – The account where you create and manage AWS Network Security Manager resources (rules, templates, policies, scopes, and deployments). You designate one or more administrator accounts, each with a priority from 1 to 10.
+ **Member accounts** – The accounts where AWS Network Security Manager discovers resources, evaluates synchronization status, and optionally remediates out-of-sync configurations. AWS Network Security Manager acts in member accounts through a service-linked role. For more information, see [Service-linked role](#concepts-slr).

You can optionally scope each administrator to a subset of accounts, OUs, and firewall types. Use this capability to delegate management of specific areas to different teams.

AWS Network Security Manager is a regional service. You create resources and deployments per Region with no cross-Region dependencies.

### Service-linked role
<a name="concepts-slr"></a>

AWS Network Security Manager uses an IAM service-linked role named `AWSServiceRoleForNetworkSecurityManager` to act in the member accounts of your organization on your behalf. This role trusts the `network-security-manager.amazonaws.com` service principal. It uses the `NetworkSecurityManagerServiceRolePolicy` AWS managed policy.

AWS Network Security Manager creates this role automatically when you enable the service, so there is no manual setup. The role lets AWS Network Security Manager manage AWS WAF and AWS Shield Advanced protections, discover protected resources through AWS Config, and perform cross-account operations. For more information, see [Using service-linked roles for AWS Network Security Manager](using-service-linked-roles.md).