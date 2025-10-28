# Set up AWS IoT SiteWise object IDs

AWS IoT SiteWise defines various types of persistent objects, such as assets, asset models, properties, and
hierarchies. All such objects have unique identifiers that you can use to retrieve, update, and delete them.

AWS IoT SiteWise has different options for customers for ID creation. AWS IoT SiteWise generates one for you
by default at object creation time. Users can also provide their own IDs to your objects.

###### Topics

- [Work with object UUIDs](#object-uuids "#object-uuids")
- [Use external IDs](#external-ids "#external-ids")

## Work with object UUIDs

Every persistent object in AWS IoT SiteWise has a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier "https://en.wikipedia.org/wiki/Universally_unique_identifier") to identify it. For example, asset
models have an asset model ID, assets have an asset ID, and so on. This ID is assigned at the time that you
create the object, and remains unchanged for the object's lifetime.

When you create a new object, AWS IoT SiteWise generates a unique ID for you by default. You can also provide your
own ID at creation time in UUID format.

###### Note

UUIDs **must** be globally unique within the AWS Region where it's created,
and for the same object type. When AWS IoT SiteWise auto-generates an ID for you, it's always unique. If you choose your
own ID, make sure that it's unique.

For example, if you create a new asset model by calling [CreateAssetModel](../APIReference/API_CreateAssetModel.md "../APIReference/API_CreateAssetModel.md"), you can provide your own
UUID in the optional `assetModelId` field of the request.

By contrast, if you omit `assetModelId` from the request, AWS IoT SiteWise generates a
UUID for the new asset model.

## Use external IDs

To define your own ID in some format other than UUID, you can assign an _external ID_.
For example, you can do this if you reuse an ID that you're using in a system that's not AWS, or to be more
human-readable. External IDs have a more flexible format. You can use them to reference your objects in AWS IoT SiteWise
API operations where you would otherwise use the UUID.

Like the UUIDs, each external ID must be unique within its context. For example, you
can't have two asset models with the same external ID. Also, like the UUIDs, an object can
only have one external ID in its lifetime, which can't change.

### Differences between external IDs and

UUIDs

External IDs differ from UUIDs in the following ways:

- Every object has a UUID, but external IDs are optional.
- AWS IoT SiteWise never generates external IDs. You provide these yourself.
- If the object does not already have one, you can assign an external ID at any time.

### Format of external IDs

A valid external ID has the following properties:

- Is between 2 and 128 characters long.
- The first and last characters must be alphanumeric (A-Z, a-z, 0-9).
- Characters other than first and last must either be alphanumeric, or else one of
  the following: `_-.:`

For example, an external ID must conform to the following regular expression:

`[a-zA-Z0-9][a-zA-Z0-9_\-.:]*[a-zA-Z0-9]+`

### Reference objects with external IDs

In many places that you could reference an object using its UUID, you can use its
external ID instead, if it has one. To do so, append the external ID to the string
`externalId:`.

For example, suppose you have an asset model whose UUID (asset model ID) is
`a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`, which also has the external ID `myExternalId`.
Call [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md") to get details about it. You could use either of the
following as the value of `assetModelId`:

- With the asset model ID (UUID) itself: `a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`
- With the external ID: `externalId:myExternalId`

```
aws iotsitewise describe-asset-model --asset-model-id a1b2c3d4-5678-90ab-cdef-11111EXAMPLE
aws iotsitewise describe-asset-model --asset-model-id externalId:myExternalId

```

###### Note

The `externalId:` prefix is not, itself, part of the external ID.
You only need to provide the prefix when you supply an external ID to an API operation
that accepts either UUIDs or external IDs. For example, supply the prefix when you query
or update an existing object.

When you define an external ID for an object, such as when you create an asset
model, don't include the prefix.

You can use external IDs in place of UUIDs in this fashion for many API operations in AWS IoT SiteWise, but not
all. For example, the [GetAssetPropertyValue](../APIReference/API_GetAssetPropertyValue.md "../APIReference/API_GetAssetPropertyValue.md"), **must** use UUIDs; it doesn't support external ID
usage.

To determine whether a particular API operation supports this usage, consult the
[API
Reference](../APIReference/API_Operations.md "../APIReference/API_Operations.md").
