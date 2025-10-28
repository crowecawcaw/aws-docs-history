# Amazon Redshift query editor

v2

Amazon Redshift query editor v2 is a web-based SQL client application that you can use to author and
run queries on your Amazon Redshift data warehouse. When you use the Amazon Redshift query editor v2 to connect
to a database, Amazon Redshift can store your credentials in a Secrets Manager [managed secret](service-linked-secrets.md "service-linked-secrets.md") with the prefix
`sqlworkbench`. The cost of storing the secret is included with the charge for
using Amazon Redshift. To update the secret, you must use Amazon Redshift rather than Secrets Manager. For more information,
see [Working
with query editor v2](../../../redshift/latest/mgmt/query-editor-v2-using.md "../../../redshift/latest/mgmt/query-editor-v2-using.md") in the _Amazon Redshift Management Guide_.

For the previous query editor, see [How Amazon Redshift uses AWS Secrets Manager](integrating_how-services-use-secrets_RS.md "integrating_how-services-use-secrets_RS.md").
