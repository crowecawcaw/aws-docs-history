

# What quick response resources are mirrored in the replica instance

Connect Customer Global Resiliency mirrors the following resources across your linked AWS Regions:
+ Quick responses, including their tags
+ The `QUICK_RESPONSES` knowledge base that stores the quick responses, including its tags
+ The integration association of type `WISDOM_QUICK_RESPONSES` that links the knowledge base to your instance

For more information about how integration associations replicate, see [Understanding how integrations replicate](update-integrations-across-regions.md#update-integrations-how-changes-replicate).

**Managing customer managed keys and routing profiles**  
If you encrypt the knowledge base with a customer managed key, the knowledge base and its quick responses don't replicate until you register a key for the replica Region. For more information, see [Using customer managed keys with your knowledge base](global-resiliency-quick-responses-cmk.md).  
A quick response grouped by routing profile replicates only if the replica instance has those routing profiles. For more information, see [Replicating quick responses grouped by routing profile](global-resiliency-quick-responses-considerations.md#global-resiliency-quick-responses-routing-profiles).

## Replicating changes
<a name="global-resiliency-quick-responses-how-changes-replicate"></a>

Changes to quick responses replicate in both directions. When you create, update, or delete a quick response in either Region, Connect Customer Global Resiliency makes the same change in the other Region.

Changes to the knowledge base replicate in one direction, from the source Region to the replica Region. You can change the knowledge base only in the source Region.