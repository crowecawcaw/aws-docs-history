

# Understanding important things about Global Resiliency for quick responses
<a name="global-resiliency-quick-responses-considerations"></a>

Deleting a knowledge base doesn't delete its integration association with your instance. To remove the association, call the [DeleteIntegrationAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteIntegrationAssociation.html) API.

## Replicating quick responses grouped by routing profile
<a name="global-resiliency-quick-responses-routing-profiles"></a>

If a quick response is grouped by routing profile, it replicates only if all of those routing profiles exist in the replica instance.

If you delete a routing profile, quick responses that are still grouped by it don't replicate. Update the grouping configuration of the quick response to enable replication after you delete a routing profile. Make this change in the Region where the quick response is up to date. If you edit the older copy, it replaces the newer one in both Regions. For instructions on editing a quick response, see [Edit quick responses in Connect Customer](edit-quick-responses.md). After you save the change, the quick response replicates.