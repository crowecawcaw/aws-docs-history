

# Quotas for Amazon Verified Permissions
<a name="quotas"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for Verified Permissions, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **Verified Permissions**.

To request a quota increase, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

Your AWS account has the following quotas related to Verified Permissions.

**Topics**
+ [Quotas for resources](#quotas-resources)
+ [Quotas for hierarchies](#quotas-hierarchies)
+ [Quotas for operations per second](#quotas-tps)

## Quotas for resources
<a name="quotas-resources"></a>


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
|  Policy stores per Region per account  | Each supported Region: 30,000  |  [ Yes ](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-919F2C9C)  |  The maximum number of policy stores.  | 
|  Policy templates per policy store  | Each supported Region: 40  |  [ Yes ](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-97BDA0CF)  |  The maximum number of policy templates in a policy store.  | 
| Identity sources per policy store | 1 | No | The maximum number of identity sources that you can define for a policy store. | 
| Policy store aliases per policy store | 10 | Yes | The maximum number of policy store aliases that you can associate with a single policy store. | 
| Authorization request size¹ | 1 MB | No | The maximum size of an authorization request. | 
| Policy size | 10,000 bytes | Yes | The maximum size of an individual policy. | 
| Schema size | 100,000 bytes | Yes | The maximum size of the schema of a policy store. | 
| Namespaces per policy store schema | 100 | Yes | The maximum number of namespaces that you can define in a policy store schema. | 
| Policy size per resource | 200,000 bytes² | Yes | The maximum size of all policies that reference a specific resource. | 

¹ The quota for an authorization request is the same for both [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html).



² The default limit for the total size of all the policies that reference a single resource is 200,000 bytes. Policies that don't specify a resource share a separate total of 200,000 bytes for the `"unspecified"` resource. For details about how Verified Permissions calculates this quota, examples, and strategies for staying within it, see [Policy size per resource](policy-size-per-resource.md).

## Quotas for hierarchies
<a name="quotas-hierarchies"></a>

**Note**  
Each transitive parent quota applies to each entity individually and counts both direct and indirect (transitive) parents toward the total. For example, if the limit of *Transitive parents per principal* is 100, a principal can have 100 direct parent groups with no nested groups. Alternatively, a principal can have 10 direct parent groups that each belong to 9 additional parent groups. Any combination that totals 100 parents for that principal is valid.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Transitive parents per principal | 100 | No | The maximum number of transitive parents for each principal. | 
| Transitive parents per action | 100 | No | The maximum number of transitive parents for each action. | 
| Transitive parents per resource | 100 | No | The maximum number of transitive parents for each resource. | 

The diagram below illustrates how transitive parents can be defined for an entity (principal, action, or resource).

![Transitive parents per entity](http://docs.aws.amazon.com/verifiedpermissions/latest/userguide/images/quotas-transitive-parents.png)


## Quotas for operations per second
<a name="quotas-tps"></a>

Verified Permissions throttles requests to service endpoints in an AWS Region when application requests exceed the quota for an API operation. Verified Permissions might return an exception when you exceed the quota in requests per second, or you attempt simultaneous write operations. You can view your current RPS quotas in [Service Quotas](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas). To prevent applications from exceeding the quota for an operation, you must optimize them for retries and exponential backoff. For more information, see [Retry with backoff pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html) and [Managing and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/).


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| BatchGetPolicy requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-DE99D97D)  | The maximum number of BatchGetPolicy requests per second per policy store. | 
| BatchIsAuthorized requests per second per Region per policy store | Each supported Region: 30 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-9DB5CAA4)  | The maximum number of BatchIsAuthorized requests per second per policy store. | 
| BatchIsAuthorizedWithToken requests per second per Region per policy store | Each supported Region: 30 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-1FC83DB7)  | The maximum number of BatchIsAuthorizedWithToken requests per second per policy store. | 
| CreateIdentitySource requests per second per Region per policy store | Each supported Region: 1 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-6DD21905)  | The maximum number of CreateIdentitySource requests per second per policy store. | 
| CreatePolicy requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-9647C866)  | The maximum number of CreatePolicy requests per second per policy store. | 
| CreatePolicyStore requests per second per Region per account | Each supported Region: 1 | No | The maximum number of CreatePolicyStore requests per second. | 
| CreatePolicyTemplate requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-8D5CB09F)  | The maximum number of CreatePolicyTemplate requests per second per policy store. | 
| DeleteIdentitySource requests per second per Region per policy store | Each supported Region: 1 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-38A7DE67)  | The maximum number of DeleteIdentitySource requests per second per policy store. | 
| DeletePolicy requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-F81CF58F)  | The maximum number of DeletePolicy requests per second per policy store. | 
| DeletePolicyStore requests per second per Region per account | Each supported Region: 1 | No | The maximum number of DeletePolicyStore requests per second. | 
| DeletePolicyTemplate requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-5CA93A13)  | The maximum number of DeletePolicyTemplate requests per second per policy store. | 
| GetIdentitySource requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-5A76F227)  | The maximum number of GetIdentitySource requests per second per policy store. | 
| GetPolicy requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-C9736881)  | The maximum number of GetPolicy requests per second per policy store. | 
| GetPolicyStore requests per second per Region per account | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-E1924570)  | The maximum number of GetPolicyStore requests per second. | 
| GetPolicyTemplate requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-D82415D2)  | The maximum number of GetPolicyTemplate requests per second per policy store. | 
| GetSchema requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-B49B9779)  | The maximum number of GetSchema requests per second per policy store. | 
| IsAuthorized requests per second per Region per policy store | Each supported Region: 200 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-771544C7)  | The maximum number of IsAuthorized requests per second per policy store. | 
| IsAuthorizedWithToken requests per second per Region per policy store | Each supported Region: 200 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-645D3857)  | The maximum number of IsAuthorizedWithToken requests per second per policy store. | 
| ListIdentitySources requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-8E2326FF)  | The maximum number of ListIdentitySources requests per second per policy store. | 
| ListPolicies requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-4E0E8AFD)  | The maximum number of ListPolicies requests per second per policy store. | 
| ListPolicyStores requests per second per Region per account | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-271BE7E8)  | The maximum number of ListPolicyStores requests per second. | 
| ListPolicyTemplates requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-70239429)  | The maximum number of ListPolicyTemplates requests per second per policy store. | 
| PutSchema requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-886D79EB)  | The maximum number of PutSchema requests per second per policy store. | 
| UpdateIdentitySource requests per second per Region per policy store | Each supported Region: 1 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-D2870CD3)  | The maximum number of UpdateIdentitySource requests per second per policy store. | 
| UpdatePolicy requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-2AFF096D)  | The maximum number of UpdatePolicy requests per second per policy store. | 
| UpdatePolicyStore requests per second per Region per account | Each supported Region: 10 | No | The maximum number of UpdatePolicyStore requests per second. | 
| UpdatePolicyTemplate requests per second per Region per policy store | Each supported Region: 10 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/verifiedpermissions/quotas/L-DC54B663)  | The maximum number of UpdatePolicyTemplate requests per second per policy store. | 