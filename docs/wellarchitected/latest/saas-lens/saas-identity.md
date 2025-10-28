# SaaS Identity

Most systems already rely on an identity provider for
authentication. In the world of SaaS, we need to extend the notion
of identity to incorporate tenancy into our definition of
identity. This means that, after authenticating a user, we need to
know who the user is as well as which tenant that user is
associated with. This merging of the user identity with the tenant
identity is referred to as a SaaS identity. This concept is a
foundational element of a SaaS architecture, providing the tenant
context that is used to implement the underlying multi-tenant
policies and strategies that are part of a SaaS application.
