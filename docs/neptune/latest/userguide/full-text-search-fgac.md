# Querying from an OpenSearch cluster with Fine-grained access control (FGAC) enabled

If you have enabled [fine-grained access
control](../../../opensearch-service/latest/developerguide/fgac.md "../../../opensearch-service/latest/developerguide/fgac.md") on your OpenSearch cluster, you need to [enable
IAM authentication](iam-auth-enable.md "iam-auth-enable.md") in your Neptune database as well.

The IAM entity (User or Role) used for connecting to the Neptune database
should have permissions both for Neptune and the OpenSearch cluster. This
means that your user or role must have an OpenSearch Service policy like this attached:

See [Creating custom IAM policy statements to access data in Amazon Neptune](iam-data-access-policies.md "iam-data-access-policies.md")
for more information.
