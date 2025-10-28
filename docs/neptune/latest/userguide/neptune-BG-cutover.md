# Cutting over from the production blue cluster to the updated green cluster

Before promoting the green cluster to production, ensure that the commit difference
between the blue and green clusters is zero and then disable all write traffic to
the blue cluster. Continuing to write to the blue cluster while switching the database
endpoint to the green cluster can result in data corruption caused by writing partial
data to both clusters. You may not need to disable read traffic yet.

If you have enabled IAM authentication on the source (blue) cluster, be sure
to update any IAM policies used in your applications to point to the green cluster
(for an example of such a policy, see this [unrestricted access policy](iam-data-access-examples.md#iam-auth-data-policy-example-general "iam-data-access-examples.md#iam-auth-data-policy-example-general")).

After disabling write traffic, wait for replication to finish and then enable
write traffic on the green cluster (but not on the blue cluster). Switch read traffic
from the blue to the green cluster as well.
