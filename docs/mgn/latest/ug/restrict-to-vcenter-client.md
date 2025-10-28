NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Restrict permission to act on a source server associated with given AWS vCenter

client

To restrict access to source servers associated with a given AWS vCenter client, use the condition element `mgn:VcenterClientId` condition key.

The following example demonstrates a policy that allows an AWS vCenter client to call the `mgn:UpdateAgentSourcePropertiesForMgn` action only on a source server associated with the calling AWS vCenter client.
