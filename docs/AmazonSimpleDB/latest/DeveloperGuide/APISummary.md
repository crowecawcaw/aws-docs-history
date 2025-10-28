# API Summary

The Amazon SimpleDB service consists of a small group of API calls that provide the core
functionality you need to build your application. See [Operations](SDB_API_Operations.md "SDB_API_Operations.md") in the API Reference chapter for detailed descriptions of each option.

- CreateDomain—Create domains to contain your data;
  you can create up to 250 domains. If you require additional domains, go to
  [https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains").
- DeleteDomain—Delete any of your
  domains
- ListDomains—List all domains within your
  account
- PutAttributes—Add, modify, or remove data within your
  Amazon SimpleDB domains
- BatchPutAttributes—Generate multiple put operations in
  a single call
- DeleteAttributes—Remove items, attributes, or
  attribute values from your domain
- BatchDeleteAttributes—Generate multiple delete operations in
  a single call
- GetAttributes—Retrieve the attributes and values of
  any item ID that you specify
- Select—Query the specified domain using a
  SQL SELECT expression
- DomainMetadata—View information about the domain,
  such as the creation date, number of items and attributes, and the size of attribute names and values
