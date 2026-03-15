# Cross-Region and cross-account data access

OpenSearch UI supports accessing data from OpenSearch domains across different
AWS accounts and AWS Regions. You can choose from two approaches depending on your
requirements. The following table compares the two approaches.

###### Note

Both cross-account data access and cross-cluster search work only with
OpenSearch domains. Neither approach supports OpenSearch Serverless collections.

| Aspect                                  | Cross-account data access                                                                  | Cross-cluster search                                                                                                  |
| --------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| Feature                                 | Associate domains from other accounts as direct data sources in<br>OpenSearch UI           | Query data across connected domains using cross-cluster search<br>connections                                         |
| Mechanism                               | Direct access – OpenSearch UI connects directly to the<br>target domain in another account | Indirect access – requires a local domain in the same account<br>as OpenSearch UI to relay requests to remote domains |
| Cross-account support                   | Yes                                                                                        | Yes                                                                                                                   |
| Cross-Region support                    | No – source and target domains must be in the same<br>AWS Region                           | Yes – source and destination domains can be in different<br>AWS Regions                                               |
| Union data across domains               | No – each domain is queried independently as a separate data<br>source                     | Yes – a single query can aggregate results from multiple<br>connected domains                                         |
| Authentication methods                  | IAM and AWS IAM Identity Center                                                            | IAM (with fine-grained access control)                                                                                |
| Setup complexity                        | Lower – requires a cross-account IAM role for<br>validation                                | Higher – requires cross-cluster connections, access policies<br>on both domains, and fine-grained access control      |
| Data source visibility in OpenSearch UI | Each cross-account domain appears as a separate data source                                | Remote domains are accessed through the local source domain's<br>connection aliases                                   |
| Write access to remote domain           | Yes – controlled by the target domain's access policy                                      | No – cross-cluster search provides read-only access to remote<br>domains                                              |

###### Topics

- [Cross-account data access to OpenSearch domains](application-cross-account-data-access-domains.md "application-cross-account-data-access-domains.md")
- [Cross-cluster search](application-cross-cluster-search.md "application-cross-cluster-search.md")
