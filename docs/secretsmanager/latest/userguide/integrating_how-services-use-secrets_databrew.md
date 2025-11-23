# How AWS Glue DataBrew uses

AWS Secrets Manager

AWS Glue DataBrew is a visual data preparation tool that you can use to clean and normalize
data without writing any code. In DataBrew, a set of data transformation steps is called a
recipe. AWS Glue DataBrew provides the [`DETERMINISTIC_DECRYPT`](../../../databrew/latest/dg/recipe-actions.md "../../../databrew/latest/dg/recipe-actions.md"), [`DETERMINISTIC_ENCRYPT`](../../../databrew/latest/dg/recipe-actions.md "../../../databrew/latest/dg/recipe-actions.md"), and [`CRYPTOGRAPHIC_HASH`](../../../databrew/latest/dg/recipe-actions.md "../../../databrew/latest/dg/recipe-actions.md") recipe steps to perform transformations
on personally identifiable information (PII) in a dataset, which use an encryption key
stored in a Secrets Manager secret. If you use the DataBrew _default secret_ to
store the encryption key, DataBrew creates a [managed
secret](service-linked-secrets.md "service-linked-secrets.md") with the prefix `databrew`. The cost of storing the secret
is included with the charge for using DataBrew. If you create a new secret to store the
encryption key, DataBrew creates a secret with the prefix `AwsGlueDataBrew`. You
are charged for that secret.
