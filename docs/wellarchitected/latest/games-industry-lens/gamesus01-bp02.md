# GAMESUS01-BP02 Use lifecycle policies or TTL expiration to

delete unnecessary games user data, log files, or deprecated
assets

You can use tags and data type to create lifecycle policies or TTL's
to move data to archival storage or remove completely from the
service. This may include temporary configurations, expired archived
content, and historical logs that are no longer needed. Most
services support tagging.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For data stored in S3 you can use lifecycle policies to move the
data to infrequent access and archival tiers of storage. In an S3
Lifecycle configuration, you can define rules to transition
objects from one storage class to another to save on storage
costs. When you don't know the access patterns of your objects, or
if your access patterns are changing over time, you can transition
the objects to the S3 Intelligent-Tiering storage class for
automatic cost savings.

Amazon S3 supports a waterfall model for transitioning between
storage classes, as shown in the following diagram.

You can add transition actions to an S3 Lifecycle configuration to
tell Amazon S3 to delete objects at the end of their lifetime.
When an object reaches the end of its lifetime based on its
lifecycle configuration, Amazon S3 takes an Expiration action
based on which S3 Versioning state the bucket is in:

- **Non-versioned bucket:**
  Amazon S3 queues the object for removal and removes it
  asynchronously, permanently removing the object.
- **Versioning-enabled bucket:**
  If the current object version is not a delete marker, Amazon S3 adds a delete marker with a unique version ID. This makes
  the current version noncurrent, and the delete marker the
  current version.
- **Versioning-suspended
  bucket:** Amazon S3 creates a delete marker with null
  as the version ID. This delete marker replaces an object
  version with a null version ID in the version hierarchy, which
  effectively deletes the object.
- When you add a Lifecycle configuration to a bucket, the
  configuration rules apply to both existing objects and objects
  that you add later. For example, if you add a Lifecycle
  configuration rule today with an expiration action that causes
  objects with a specific prefix to expire 30 days after
  creation, Amazon S3 will queue for removal existing objects
  that are more than 30 days old and that have the specified
  prefix.

Time To Live (TTL) for DynamoDB is a cost-effective method for
deleting items that are no longer relevant. TTL allows you to
define a per-item expiration timestamp that indicates when an item
is no longer needed. DynamoDB automatically deletes expired items
within a few days of their expiration time, without consuming
write throughput.

- To use TTL, first enable it on a table and then define a
  specific attribute to store the TTL expiration timestamp. The
  timestamp must be stored in
  [Unix
  epoch time format](https://en.wikipedia.org/wiki/Unix_time "https://en.wikipedia.org/wiki/Unix_time") at the seconds granularity. Each time
  an item is created or updated, you can compute the expiration
  time and save it in the TTL attribute.
- Items with valid, expired TTL attributes may be deleted by the
  system, typically within a few days of their expiration. You
  can still update the expired items that are pending deletion,
  including changing or removing their TTL attributes. While
  updating an expired item, we recommended that you use a
  condition expression to make sure the item has not been
  subsequently deleted. Use filter expressions to remove expired
  items from
  [Scan](../../../amazondynamodb/latest/developerguide/Scan.md#Scan.FilterExpression "../../../amazondynamodb/latest/developerguide/Scan.md#Scan.FilterExpression")
  and
  [Query](../../../amazondynamodb/latest/developerguide/Query.md "../../../amazondynamodb/latest/developerguide/Query.md")
  results.
- Deleted items work similarly to those deleted through typical
  delete operations. Once deleted, items go into DynamoDB
  Streams as service deletions instead of user deletes and are
  removed from local secondary indexes and global secondary
  indexes just like other delete operations.

With ElastiCache for Redis you can control the freshness of your
cached data by using TTLs or expiration on cached keys. After the
set time has passed, the key is deleted from the cache, and access
to the origin data store is required along with reaching the
updated data. 

- Two principles determine the appropriate TTLs to apply and the
  types of caching patterns to implement. First, it's important
  that you understand the rate of change of the underlying data.
  Second, it's important that you evaluate the risk of outdated
  data being returned to your application instead of its updated
  counterpart.
- With dynamic data that changes often, you might want to apply
  lower TTLs that expire the data at a rate of change that
  matches that of the primary database. This lowers the risk of
  returning outdated data while still providing a buffer to
  offload database requests.
- It's also important to recognize that, even if you are only
  caching data for minutes or seconds versus longer durations,
  appropriately applying TTLs to your cached keys can result in
  a performance boost and an overall better player experience
  with your game.

### Implementation steps

- Use Amazon S3 Lifecycle policies to transition objects to
  infrequent access or archival tiers and configure expiration
  actions to delete unnecessary objects based on lifecycle
  rules.
- Enable Time to Live (TTL) in DynamoDB tables to
  automatically delete expired items without consuming write
  throughput, defining the expiration timestamp in Unix epoch
  time.
- Set appropriate TTLs for ElastiCache keys based on data
  change rates and risk tolerance for outdated data,
  facilitating cached data freshness and improved player
  experience.
