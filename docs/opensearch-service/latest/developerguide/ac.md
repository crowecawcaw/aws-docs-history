# Identity and Access Management in Amazon OpenSearch Service

Amazon OpenSearch Service offers several ways to control access to your domains. This topic covers the
various policy types, how they interact with each other, and how to create your own custom
policies.

###### Important

VPC support introduces some additional considerations to OpenSearch Service access control. For more
information, see [About access policies on VPC domains](vpc.md#vpc-security "vpc.md#vpc-security").

## Types of policies

OpenSearch Service supports three types of access policies:

- [Resource-based policies](#ac-types-resource "#ac-types-resource")
- [Identity-based policies](#ac-types-identity "#ac-types-identity")
- [IP-based policies](#ac-types-ip "#ac-types-ip")

### Resource-based policies

You add a resource-based policy, often called the domain access policy, when you
create a domain. These policies specify which actions a principal can perform on the
domain's _subresources_ (with the exception of
[cross-cluster search](cross-cluster-search.md#cross-cluster-search-walkthrough "cross-cluster-search.md#cross-cluster-search-walkthrough")).
Subresources include OpenSearch indexes and APIs. The [Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") JSON policy element in IAM specifies the accounts, users,
or roles that are allowed access. The [Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") JSON policy element specifies which subresources these
principals can access.

For example, the following resource-based policy grants `test-user`
full access (`es:*`) to the subresources on
`test-domain`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::123456789012:user/test-user"
 ]
 },
 "Action": [
 "es:*"
 ],
 "Resource": "arn:aws:es:us-west-1:987654321098:domain/test-domain/*"
 }
 ]
}`

```

Two important considerations apply to this policy:

- These privileges apply only to this domain. Unless you create similar
  policies on other domains, `test-user` can only access
  `test-domain`.
- The trailing `/*` in the `Resource` element is
  significant and indicates that resource-based policies only apply to the
  domain's subresources, not the domain itself. In resource-based policies,
  the `es:*` action is equivalent to
  `es:ESHttp*`.

For example, `test-user` can make requests against an index
(`GET
 https://search-test-domain.us-west-1.es.amazonaws.com/test-index`),
but can't update the domain's configuration (`POST
 https://es.us-west-1.amazonaws.com/2021-01-01/opensearch/domain/test-domain/config`).
Note the difference between the two endpoints. Accessing the configuration
API requires an [identity-based
policy](#ac-types-identity "#ac-types-identity").

You can specify a partial index name by adding a wildcard. This example identifies
any indexes beginning with `commerce`:

```
arn:aws:es:us-west-1:987654321098:domain/test-domain/commerce*
```

In this case, the wildcard means that `test-user` can make requests to
indexes within `test-domain` that have names that begin with
`commerce`.

To further restrict `test-user`, you can apply the following
policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::123456789012:user/test-user"
 ]
 },
 "Action": [
 "es:ESHttpGet"
 ],
 "Resource": "arn:aws:es:us-west-1:987654321098:domain/test-domain/commerce-data/_search"
 }
 ]
}`

```

Now `test-user` can perform only one operation: searches against the
`commerce-data` index. All other indexes within the domain are
inaccessible, and without permissions to use the `es:ESHttpPut` or
`es:ESHttpPost` actions, `test-user` can't add or modify
documents.

Next, you might decide to configure a role for power users. This policy gives
`power-user-role` access to the HTTP GET and PUT methods for all URIs
in the index:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::123456789012:role/power-user-role"
 ]
 },
 "Action": [
 "es:ESHttpGet",
 "es:ESHttpPut"
 ],
 "Resource": "arn:aws:es:us-west-1:987654321098:domain/test-domain/commerce-data/*"
 }
 ]
}`

```

If your domain is in a VPC or uses fine-grained access control, you can use an
open domain access policy. Otherwise, your domain access policy must contain some
restriction, either by principal or IP address.

For information about all available actions, see [Policy element reference](#ac-reference "#ac-reference").
For far more granular control over your data, use an open domain access policy with
[fine-grained access control](fgac.md "fgac.md").

### Identity-based policies

Unlike resource-based policies, which are a part of each OpenSearch Service domain, you attach
identity-based policies to users or roles using the AWS Identity and Access Management (IAM) service. Just
like [resource-based policies](#ac-types-resource "#ac-types-resource"),
identity-based policies specify who can access a service, which actions they can
perform, and if applicable, the resources on which they can perform those
actions.

While they certainly don't have to be, identity-based policies tend to be more
generic. They often govern only the configuration API actions a user can perform.
After you have these policies in place, you can use resource-based policies (or
[fine-grained access control](fgac.md "fgac.md")) in OpenSearch Service to offer users
access to OpenSearch indexes and APIs.

###### Note

Users with the AWS managed
`AmazonOpenSearchServiceReadOnlyAccess` policy can't see cluster
health status on the console. To allow them to see cluster health status (and
other OpenSearch data), add the `es:ESHttpGet` action to an access
policy and attach it to their accounts or roles.

Because identity-based policies attach to users or roles (principals), the JSON
doesn't specify a principal. The following policy grants access to actions that
begin with `Describe` and `List`. This combination of actions
provides read-only access to domain configurations, but not to the data stored in
the domain itself:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "es:Describe*",
 "es:List*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

An administrator might have full access to OpenSearch Service and all data stored on all
domains:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "es:*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

Identity-based policies let you use tags to control access to the configuration
API. The following policy, for example, lets attached principals view and update a
domain's configuration if the domain has the `team:devops` tag:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Action": [
 "es:UpdateDomainConfig",
 "es:DescribeDomain",
 "es:DescribeDomainConfig"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:ResourceTag/team": [
 "devops"
 ]
 }
 }
 }]
}`

```

You can also use tags to control access to the OpenSearch API. Tag-based
policies for the OpenSearch API only apply to HTTP methods. For example, the
following policy lets attached principals send GET and PUT requests to the
OpenSearch API if the domain has the `environment:production`
tag:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Action": [
 "es:ESHttpGet",
 "es:ESHttpPut"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:ResourceTag/environment": [
 "production"
 ]
 }
 }
 }]
}`

```

For more granular control of the OpenSearch API, consider using [fine-grained access control](fgac.md "fgac.md").

###### Note

After you add one or more OpenSearch APIs to any tag-based policy, you must
perform a single [tag
operation](managedomains-awsresourcetagging.md "managedomains-awsresourcetagging.md") (such as adding, removing, or modifying a tag) in order for
the changes to take effect on a domain. You must be on service software
R20211203 or later to include OpenSearch API operations in tag-based
policies.

OpenSearch Service supports the `RequestTag` and `TagKeys` global
condition keys for the configuration API, not the OpenSearch API. These conditions
only apply to API calls that include tags within the request, such as
`CreateDomain`, `AddTags`, and `RemoveTags`.
The following policy lets attached principals create domains, but only if they
include the `team:it` tag in the request:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "es:CreateDomain",
 "es:AddTags"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/team": [
 "it"
 ]
 }
 }
 }
}`

```

For more information about using tags for access control and the differences
between resource-based and identity-based policies, see the [Define permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the
_IAM User Guide_.

### IP-based policies

IP-based policies restrict access to a domain to one or more IP addresses or CIDR
blocks. Technically, IP-based policies are not a distinct type of policy. Instead,
they are just resource-based policies that specify an anonymous principal and
include a special Condition. For information, see [IAM JSON
policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the
_IAM User Guide_.

The primary appeal of IP-based policies is that they allow unsigned requests to an
OpenSearch Service domain, which lets you use clients like [curl](https://curl.haxx.se/ "https://curl.haxx.se/") and [OpenSearch Dashboards](dashboards.md "dashboards.md") or
access the domain through a proxy server. To learn more, see [Using a proxy to access OpenSearch Service from
Dashboards](dashboards.md#dashboards-proxy "dashboards.md#dashboards-proxy").

###### Note

If you enabled VPC access for your domain, you can't configure an IP-based
policy. Instead, you can use `security groups` to control which IP
addresses can access the domain. For more information, see the following topics:

- [About access policies on VPC domains](vpc.md#vpc-security "vpc.md#vpc-security")
- [Control traffic
  to your AWS resources using security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") in the
  _Amazon VPC User Guide_

The following policy grants all HTTP requests that originate from the specified IP
range access to `test-domain`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "es:ESHttp*"
 ],
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "192.0.2.0/24"
 ]
 }
 },
 "Resource": "arn:aws:es:us-west-1:987654321098:domain/test-domain/*"
 }
 ]
}`

```

If your domain has a public endpoint and doesn't use [fine-grained access control](fgac.md "fgac.md"), we recommend combining IAM principals and
IP addresses. This policy grants `test-user` HTTP access only if the
request originates from the specified IP range:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::987654321098:user/test-user"
 ]
 },
 "Action": [
 "es:ESHttp*"
 ],
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "192.0.2.0/24"
 ]
 }
 },
 "Resource": "arn:aws:es:us-west-1:987654321098:domain/test-domain/*"
 }]
}`

```

## When policies collide

Complexities arise when policies disagree or make no explicit mention of a user.
[How
IAM works](../../../IAM/latest/UserGuide/intro-structure.md "../../../IAM/latest/UserGuide/intro-structure.md") in the _IAM User Guide_
provides a concise summary of policy evaluation logic:

- By default, all requests are denied.
- An explicit allow overrides this default.
- An explicit deny overrides any allows.

For example, if a resource-based policy grants you access to a domain subresource (an
OpenSearch index or API), but an identity-based policy denies you access, you are
denied access. If an identity-based policy grants access and a resource-based policy
does not specify whether or not you should have access, you are allowed access. See the
following table of intersecting policies for a full summary of outcomes for domain
subresources.

|                                                            | Allowed in resource-based policy | Denied in resource-based policy | Neither allowed nor denied in resource-based policy |
| ---------------------------------------------------------- | -------------------------------- | ------------------------------- | --------------------------------------------------- |
| **Allowed in identity-based policy**                       | Allow                            | Deny                            | Allow                                               |
| **Denied in identity-based policy**                        | Deny                             | Deny                            | Deny                                                |
| **Neither allowed nor denied in identity-based<br>policy** | Allow                            | Deny                            | Deny                                                |

## Policy element reference

OpenSearch Service supports most policy elements in the [IAM Policy
Elements Reference](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md"), with the exception of `NotPrincipal`. The
following table shows the most common elements.

| JSON policy element | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Version`           | The current version of the policy language is<br>`2012-10-17`. All access policies should specify this<br>value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `Effect`            | This element specifies whether the statement allows or denies<br>access to the specified actions. Valid values are `Allow`<br>or `Deny`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `Principal`         | This element specifies the AWS account or IAM role or user<br>that is allowed or denied access to a resource and can take several<br>forms:<br>• **AWS accounts**:<br>`"Principal":{"AWS": ["123456789012"]}` or<br>`"Principal":{"AWS":<br>["arn:aws:iam::123456789012:root"]}`<br>• **IAM users**:<br>`"Principal":{"AWS":<br>["arn:aws:iam::123456789012:user/test-user"]}`<br>• **IAM roles**:<br>`"Principal":{"AWS":<br>["arn:aws:iam::123456789012:role/test-role"]}`<br>ImportantSpecifying the `*` wildcard enables anonymous<br>access to the domain, which we don't recommend unless you add an<br>[IP-based condition](#ac-types-ip "#ac-types-ip"), use<br>[VPC support](vpc.md "vpc.md"), or enable [fine-grained access control](fgac.md "fgac.md"). In<br>addition, carefully inspect the following policies to confirm<br>that they do not grant broad access:<br>• Identity-based policies attached to associated AWS<br>principals (for example, IAM roles)<br>• Resource-based policies attached to associated AWS<br>resources (for example, AWS Key Management Service KMS keys)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Action`            | OpenSearch Service uses `ESHttp*` actions for OpenSearch HTTP<br>methods. The rest of the actions apply to the configuration<br>API.Certain `es:` actions support<br>resource-level permissions. For example, you can give a user<br>permissions to delete one particular domain without giving that user<br>permissions to delete _any<br>• domain.<br>Other actions apply only to the service itself. For example,<br>`es:ListDomainNames` makes no sense in the context of<br>a single domain and thus requires a wildcard.For a list<br>of all available actions and whether they apply to the domain<br>subresources (`test-domain/_`), to the domain<br>configuration (`test-domain`), or only to the service<br>(`*`), see [Actions, resources, and condition keys for Amazon OpenSearch Service](../../../service-authorization/latest/reference/list_amazonopensearchservice.md "../../../service-authorization/latest/reference/list_amazonopensearchservice.md") in<br>the *Service Authorization Reference*Resource-based<br>policies differ from resource-level permissions. [Resource-based policies](#ac-types-resource "#ac-types-resource") are full<br>JSON policies that attach to domains. Resource-level permissions let you<br>restrict actions to particular domains or subresources. In practice, you<br>can think of resource-level permissions as an optional part of a<br>resource<br>• or identity-based policy.While resource-level<br>permissions for `es:CreateDomain` might seem<br>unintuitive—after all, why give a user permissions to create<br>a domain that already exists?—the use of a wildcard lets you<br>enforce a simple naming scheme for your domains, such as<br>`"Resource":<br>"arn:aws:es:us-west-1:987654321098:domain/my-team-name-*"`.Of<br>course, nothing prevents you from including actions alongside less<br>restrictive resource elements, such as the<br>following:<br>JSON<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"es:ESHttpGet",<br>"es:DescribeDomain"<br>],<br>"Resource": "\*"<br>}<br>]<br>}`<br>```<br>To learn more about pairing actions and resources, see the<br>`Resource` element in this table. |
| `Condition`         | OpenSearch Service supports most conditions that are described in [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys") in the<br>_IAM User Guide_. Notable exceptions<br>include the `aws:PrincipalTag` key, which OpenSearch Service does not<br>support.<br>When configuring an [IP-based<br>policy](#ac-types-ip "#ac-types-ip"), you specify the IP addresses or CIDR block as a<br>condition, such as the following:<br>`<br>"Condition": {<br>"IpAddress": {<br>"aws:SourceIp": [<br>"192.0.2.0/32"<br>]<br>}<br>}<br>`<br>As noted in [Identity-based policies](#ac-types-identity "#ac-types-identity"), the<br>`aws:ResourceTag`, `aws:RequestTag`, and<br>`aws:TagKeys` condition keys apply to the<br>configuration API as well as the OpenSearch APIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Resource`          | OpenSearch Service uses `Resource` elements in three basic<br>ways:<br>• For actions that apply to OpenSearch Service itself, like<br>`es:ListDomainNames`, or to allow full<br>access, use the following syntax:<br>`<br>"Resource": "*"<br>`<br>• For actions that involve a domain's configuration, like<br>`es:DescribeDomain`, you can use the<br>following syntax:<br>``<br>"Resource": "arn:aws:es:`region`:`aws-account-id`:domain/`domain-name`"<br>``<br>• For actions that apply to a domain's subresources, like<br>`es:ESHttpGet`, you can use the following<br>syntax:<br>``<br>"Resource": "arn:aws:es:`region`:`aws-account-id`:domain/`domain-name`/*"<br>``<br>You don't have to use a wildcard. OpenSearch Service lets you define a<br>different access policy for each OpenSearch index or API.<br>For example, you might limit a user's permissions to the<br>`test-index` index:<br>``<br>"Resource": "arn:aws:es:`region`:`aws-account-id`:domain/`domain-name`/test-index"<br>``<br>Instead of full access to `test-index`, you<br>might prefer to limit the policy to just the search<br>API:<br>``<br>"Resource": "arn:aws:es:`region`:`aws-account-id`:domain/`domain-name`/test-index/_search"<br>``<br>You can even control access to individual<br>documents:<br>``<br>"Resource": "arn:aws:es:`region`:`aws-account-id`:domain/`domain-name`/test-index/test-type/1"<br>``<br>Essentially, if OpenSearch expresses the subresource as<br>a URI, you can control access to it using an access policy.<br>For even more control over which resources a user can<br>access, see [Fine-grained access control in Amazon OpenSearch Service](fgac.md "fgac.md").<br>For details about which actions support resource-level<br>permissions, see the `Action` element in this<br>table.                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Advanced options and API considerations

OpenSearch Service has several advanced options, one of which has access control implications:
`rest.action.multi.allow_explicit_index`. At its default setting of true,
it allows users to bypass subresource permissions under certain circumstances.

For example, consider the following resource-based policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::123456789012:user/test-user"
 ]
 },
 "Action": [
 "es:ESHttp*"
 ],
 "Resource": [
 "arn:aws:es:us-west-1:987654321098:domain/test-domain/test-index/*",
 "arn:aws:es:us-west-1:987654321098:domain/test-domain/_bulk"
 ]
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::123456789012:user/test-user"
 ]
 },
 "Action": [
 "es:ESHttpGet"
 ],
 "Resource": "arn:aws:es:us-west-1:987654321098:domain/test-domain/restricted-index/*"
 }
 ]
}`

```

This policy grants `test-user` full access to `test-index` and
the OpenSearch bulk API. It also allows `GET` requests to
`restricted-index`.

The following indexing request, as you might expect, fails due to a permissions
error:

```
PUT https://search-test-domain.us-west-1.es.amazonaws.com/restricted-index/movie/1
{
  "title": "Your Name",
  "director": "Makoto Shinkai",
  "year": "2016"
}
```

Unlike the index API, the bulk API lets you create, update, and delete many documents
in a single call. You often specify these operations in the request body, however,
rather than in the request URL. Because OpenSearch Service uses URLs to control access to domain
subresources, `test-user` can, in fact, use the bulk API to make changes to
`restricted-index`. Even though the user lacks `POST`
permissions on the index, the following request **succeeds**:

```
POST https://search-test-domain.us-west-1.es.amazonaws.com/_bulk
{ "index" : { "_index": "restricted-index", "_type" : "movie", "_id" : "1" } }
{ "title": "Your Name", "director": "Makoto Shinkai", "year": "2016" }

```

In this situation, the access policy fails to fulfill its intent. To prevent users
from bypassing these kinds of restrictions, you can change
`rest.action.multi.allow_explicit_index` to false. If this value is
false, all calls to the bulk, mget, and msearch APIs that specify index names in the
request body stop working. In other words, calls to `_bulk` no longer work,
but calls to `test-index/_bulk` do. This second endpoint contains an index
name, so you don't need to specify one in the request body.

[OpenSearch Dashboards](dashboards.md "dashboards.md") relies heavily on mget and
msearch, so it is unlikely to work properly after this change. For partial remediation,
you can leave `rest.action.multi.allow_explicit_index` as true and deny
certain users access to one or more of these APIs.

For information about changing this setting, see [Advanced cluster
settings](createupdatedomains.md#createdomain-configure-advanced-options "createupdatedomains.md#createdomain-configure-advanced-options").

Similarly, the following resource-based policy contains two subtle issues:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:user/test-user"
 },
 "Action": "es:ESHttp*",
 "Resource": "arn:aws:es:us-west-1:987654321098:domain/test-domain/*"
 },
 {
 "Effect": "Deny",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:user/test-user"
 },
 "Action": "es:ESHttp*",
 "Resource": "arn:aws:es:us-west-1:987654321098:domain/test-domain/restricted-index/*"
 }
 ]
}`

```

- Despite the explicit deny, `test-user` can still make calls such as
  `GET
https://search-test-domain.us-west-1.es.amazonaws.com/_all/_search`
  and `GET
https://search-test-domain.us-west-1.es.amazonaws.com/*/_search` to
  access the documents in `restricted-index`.
- Because the `Resource` element references
  `restricted-index/*`, `test-user` doesn't have
  permissions to directly access the index's documents. The user does, however,
  have permissions to _delete the entire index_.
  To prevent access and deletion, the policy instead must specify
  `restricted-index*`.

Rather than mixing broad allows and focused denies, the safest approach is to follow
the principle of [least
privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") and grant only the permissions that are required to perform a
task. For more information about controlling access to individual indexes or
OpenSearch operations, see [Fine-grained access control in Amazon OpenSearch Service](fgac.md "fgac.md").

###### Important

Specifying the \* wildcard enables anonymous access to your domain. It is not
recommended you use the wildcard In addition, carefully inspect the following
policies to confirm that they do not grant broad access:

- Identity-based policies attached to associated AWS principals (for
  example, IAM roles)
- Resource-based policies attached to associated AWS resources (for
  example, AWS Key Management Service KMS keys)

## Configuring access policies

- For instructions on creating or modifying resource- and IP-based policies in
  OpenSearch Service, see [Configuring access
  policies](createupdatedomains.md#createdomain-configure-access-policies "createupdatedomains.md#createdomain-configure-access-policies").
- For instructions on creating or modifying identity-based policies in IAM,
  see [Define custom IAM
  permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
  _IAM User Guide_.

## Additional sample policies

Although this chapter includes many sample policies, AWS access control is a complex
subject that is best understood through examples. For more, see [Example IAM identity-based policies](../../../IAM/latest/UserGuide/access_policies_examples.md "../../../IAM/latest/UserGuide/access_policies_examples.md") in the
_IAM User Guide_.
