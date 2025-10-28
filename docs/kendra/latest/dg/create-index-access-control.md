# Controlling user access to documents with

tokens

###### Note

Feature support varies by index type and search API being used. To see if this feature
is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

###### Important

Amazon Kendra GenAI Enterprise Edition indices don't support token-based user access
control.

You can control which users or groups can access certain documents in your index or see
certain documents in their search results. This is called user context filtering. It is a
kind of personalized search with the benefit of controlling access to documents. For
example, not all teams that search the company portal for information should access
top-secret company documents, nor are these documents relevant to all users. Only specific
users or groups of teams given access to top-secret documents should see these documents in
their search results.

Amazon Kendra Enterprise and Developer indices support token-based user access
control using the following token types:

- Open ID
- JWT with a shared secret
- JWT with a public key
- JSON
  Amazon Kendra can be used to deliver secure enterprise search for your retrieval and
  search applications. During query and retrieval, Amazon Kendra filters search results
  based on `AttributeFilters` and `UserContext` provided in the request.
  Amazon Kendra reads document access control lists (ACLs) collected by the its
  connectors during crawl and ingestion. The retrieval and search results return URLs pointing
  back to the original document repositories plus short excerpts. Access to the full document
  is still enforced by the original repository.

###### Topics

- [Using OpenID](create-index-access-control-tokens-openid.md "create-index-access-control-tokens-openid.md")
- [Using a JSON Web Token (JWT) with
  a shared secret](create-index-access-control-tokens-jwtshared.md "create-index-access-control-tokens-jwtshared.md")
- [Using a JSON Web Token (JWT) with
  a public key](create-index-access-control-tokens-jwtpublic.md "create-index-access-control-tokens-jwtpublic.md")
- [Using JSON](create-index-access-control-tokens-json.md "create-index-access-control-tokens-json.md")
