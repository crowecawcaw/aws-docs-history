# How Amazon ElastiCache uses AWS Secrets Manager

In ElastiCache you can use a feature called Role-Based Access Control (RBAC) to secure the
cluster. You can store these credentials in Secrets Manager. Secrets Manager provides a [rotation template](reference_available-rotation-templates.md#template-ELC "reference_available-rotation-templates.md#template-ELC") for this type of secret. For more
information, see [Automatically
rotating passwords for users](../../../AmazonElastiCache/latest/red-ug/User-Secrets-Manager.md "../../../AmazonElastiCache/latest/red-ug/User-Secrets-Manager.md") in the
_Amazon ElastiCache User Guide_.
