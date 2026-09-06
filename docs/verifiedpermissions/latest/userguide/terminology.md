

# Amazon Verified Permissions and Cedar policy language terms and concepts
<a name="terminology"></a>

You should understand the following concepts to use Amazon Verified Permissions.

**Topics**
+ [Authorization model](#term-authorization-model)
+ [Authorization request](#term-authorization-request)
+ [Authorization response](#term-authorization-response)
+ [Considered policies](#term-considered-policies)
+ [Context data](#term-context-data)
+ [Determining policies](#term-determining-policies)
+ [Entity data](#term-entity-data)
+ [Permissions, authorization, and principals](#term-permissions-authorization-principals)
+ [Policy enforcement](#term-policy-enforcement)
+ [Policy store](#term-policy-store)
+ [Policy store alias](#term-policy-store-alias)
+ [Policy name](#term-policy-name)
+ [Policy template name](#term-policy-template-name)
+ [Satisfied policies](#term-satisfied-policies)
+ [Differences between Amazon Verified Permissions and the Cedar policy language](terminology-differences-avp-cedar.md)

**Cedar policy language concepts**
+ [Authorization](https://docs.cedarpolicy.com/overview/terminology.html#authorization)
+ [Entity](https://docs.cedarpolicy.com/overview/terminology.html#entity)
+ [Groups and hierarchies](https://docs.cedarpolicy.com/overview/terminology.html#term-group)
+ [Namespaces](https://docs.cedarpolicy.com/policies/validation.html#namespaces)
+ [Policy](https://docs.cedarpolicy.com/overview/terminology.html#policy)
+ [Policy template](https://docs.cedarpolicy.com/overview/terminology.html#policy-template)
+ [Schema](https://docs.cedarpolicy.com/overview/terminology.html#schema)

## Authorization model
<a name="term-authorization-model"></a>

The *authorization model* describes the scope of the [authorization requests](#term-authorization-request) made by the application and the basis for evaluating those requests. It is defined in terms of the different types of resources, the actions taken on those resources, and the types principals that take those actions. It also considers the context in which those actions are being taken.

*Role-based Access Control (RBAC)* is an evaluation basis in which roles are defined and associated with a set of permissions. These roles can then be assigned to one or more identities. The assigned identity acquires the permissions associated with the role. If the permissions associated with the role are modified, then the modification automatically impacts any identity to which the role has been assigned. Cedar can support RBAC decisions through the use of principal groups.

*Attribute-based Access Control (ABAC)* is an evaluation basis in which the permissions associated with an identity are determined by attributes of that identity. Cedar can support ABAC decisions through the use of policy conditions that reference attributes of the principal.

The Cedar policy language enables the combination of RBAC and ABAC in a single policy by allowing permissions to be defined for a group of users, which have attribute-based conditions.

## Authorization request
<a name="term-authorization-request"></a>

An *authorization request* is a request made of Verified Permissions by an application to evaluate a set of policies in order to determine whether a principal may perform an action on a resource for a given context.

## Authorization response
<a name="term-authorization-response"></a>

The *authorization response* is the response to the [authorization request](#term-authorization-request). It includes an allow or deny decision, plus additional information, such as the IDs of the determining policies.

## Considered policies
<a name="term-considered-policies"></a>

*Considered policies* are the full set of policies that are selected by Verified Permissions for inclusion when evaluating an [authorization request](#term-authorization-request).

## Context data
<a name="term-context-data"></a>

*Context data* are attribute values that provide additional information to be evaluated.

## Determining policies
<a name="term-determining-policies"></a>

*Determining policies* are the policies that determine the [authorization response](#term-authorization-response). For example, if there are two [satisfied policies](#term-satisfied-policies), where one is a deny and the other is an allow, then the deny policy will be the determining policy. If there are multiple satisfied permit policies and no satisfied forbid policies, then there are multiple determining policies. In the case that no policies match and the response is deny, there are no determining policies.

## Entity data
<a name="term-entity-data"></a>

*Entity data* are data about the principal, action, and resource. Entity data relevant for policy evaluation are group membership all the way up the entity hierarchy and attribute values of the principal and resource.

## Permissions, authorization, and principals
<a name="term-permissions-authorization-principals"></a>

Verified Permissions manages fine-grained *permissions* and *authorization* within custom applications that you build.

A *principal* is user of an application, either human or machine, that has an identity bound to an identifier such as a username or machine ID. The process of authentication determines whether the principal is truly the identity they claim to be.

Associated with that identity are a set of application *permissions* that determine what that principal is permitted to do within that application. *Authorization* is the process of assessing those permissions to determine whether a principal is permitted to perform a particular action in the application. These permissions can be expressed as [policies](https://docs.cedarpolicy.com/overview/terminology.html#policy).

## Policy enforcement
<a name="term-policy-enforcement"></a>

*Policy enforcement* is the process of enforcing the evaluation decision within the application outside of Verified Permissions. If Verified Permissions evaluation returns a deny, then enforcement would ensure that the principal was prevented from accessing the resource.

## Policy store
<a name="term-policy-store"></a>

A *policy store* is a container for policies and templates. Each store contains a schema that is used to validate policies added to the store. By default, each application has its own policy store, but multiple applications can share a single policy store. When an application makes an authorization request, it identifies the policy store used to evaluate that request. Policy stores provide a way to isolate a set of policies, and can therefore be used in a multi-tenant application to contain the schemas and policies for each tenant. A single application can have separate policy stores for each tenant.

When evaluating an [authorization request](#term-authorization-request), Verified Permissions only considers the subset of the policies in the policy store that are relevant to the request. Relevance is determined based on the *scope* of the policy. The scope identifies the specific principal and resource to which the policy applies, and the actions that the principal can perform on the resource. Defining the scope helps improve performance by narrowing the set of considered policies.

## Policy store alias
<a name="term-policy-store-alias"></a>

A *policy store alias* is a friendly name for a policy store. You can use a policy store alias to identify a policy store in any Verified Permissions operation that accepts a `policyStoreId` parameter. Policy store aliases are independent AWS resources with their own ARNs. Each alias is associated with one policy store at a time, and multiple aliases can be associated with the same policy store. For more information, see [Amazon Verified Permissions policy store aliases](policy-store-aliases.md).

## Policy name
<a name="term-policy-name"></a>

A *policy name* is an optional friendly name for a policy. Policy names must be unique for all policies within the policy store and prefixed with `name/`. You can use a policy name in place of the policy ID in control plane operations that accept a `policyId` parameter. Names can be set when creating or updating a policy. Only `GetPolicy` and `ListPolicies` return the name in the output.

## Policy template name
<a name="term-policy-template-name"></a>

A *policy template name* is an optional friendly name for a policy template. Policy template names must be unique for all policy templates within the policy store and prefixed with `name/`. You can use a policy template name in place of the policy template ID in control plane operations that accept a `policyTemplateId` parameter. Names can be set when creating or updating a policy template. Only `GetPolicyTemplate` and `ListPolicyTemplates` return the name in the output.

## Satisfied policies
<a name="term-satisfied-policies"></a>

*Satisfied policies* are the policies that match the parameters of the [authorization request](#term-authorization-request).