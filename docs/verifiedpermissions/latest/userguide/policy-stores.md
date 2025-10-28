# Amazon Verified Permissions policy stores

A policy store is a container for policies and policy templates. In each policy store, you can create a schema that
is used to validate policies added to the policy store. In addition, you can turn on policy
validation. If you add a policy to a policy store with policy validation enabled, the entity types,
common types, and actions defined in the policy are validated against the schema and invalid
policies are rejected.

Deletion protection prevents accidental deletion of a policy store. Deletion protection is
enabled on all new policy stores created through the AWS Management Console. By contrast, it is disabled
for all policy stores created through an API or SDK call.

We recommend creating one policy store per application, or one policy store per tenant for multi-tenant
applications. You must specify a policy store when making an [authorization request](terminology.md#term-authorization-request "terminology.md#term-authorization-request").

We recommend using _namespaces_ to Cedar entities in your policy stores to
prevent ambiguity. A namespace is a string prefix for a type, separated by a pair of colons
(`::`) as a delimiter. For example `MyApplicationNamespace::exampleType`. Verified Permissions supports one namespace per policy store. These
namespaces help keep things straight when you’re working with multiple similar applications.
For example, in multi-tenant applications, using a namespace to append the name of the
tenant to the types defined in the schema will make them distinct from their similar
counterparts used by the other tenants. When looking at the logs for the authorization
requests, you’ll be able to easily indentify the tenant that processed the authorization
request. For more information, see [Namespaces](https://docs.cedarpolicy.com/overview/terminology.html#term-namespaces "https://docs.cedarpolicy.com/overview/terminology.html#term-namespaces")
in the _Cedar policy language Reference Guide_.

###### Topics

- [Creating Verified Permissions policy stores](policy-stores-create.md "policy-stores-create.md")
- [API-linked policy stores](policy-stores-api-userpool.md "policy-stores-api-userpool.md")
- [Deleting policy stores](policy-stores-delete.md "policy-stores-delete.md")
