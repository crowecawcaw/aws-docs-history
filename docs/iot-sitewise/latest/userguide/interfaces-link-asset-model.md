# Apply an interface to an asset model

When applying an interface to an asset model, you map asset model properties and
hierarchies to their interface counterparts. For unmapped interface properties, corresponding
properties are automatically created in the asset model. After linking, the service prevents
changes to the asset model that would violate interface standards.

You can add one asset model to an interface at a time. However, multiple asset models can
be linked to a single interface.

Console

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/") and choose **Models** from
   the navigation pane.
2. Select the asset model to which you want to apply an interface.
3. Choose **Link asset model** in the **Link asset
   models** section. This brings up the **Link interface**
   page.
4. In the **Asset models and interfaces** section, select an asset
   model from the **Select a model to link** dropdown menu.
5. In the **Property mappings** section, map each interface
   property to an existing asset model property or create a new property. AWS IoT SiteWise
   automatically links properties with matching names in the asset model and
   interface.
6. Review the property mappings and choose **Link
   interface**.

AWS CLI
To apply an interface to an asset model, use the
`PutAssetModelInterfaceRelationship` operation:

```
aws iotsitewise put-asset-model-interface-relationship \
  --asset-model-id "`a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`" \
  --interface-asset-model-id "`a1b2c3d4-5678-90ab-cdef-22222EXAMPLE`" \
  --property-mapping-configuration '{
    "createMissingProperty": true,
    "matchByPropertyName": true,
    "overrides": [
      {
        "assetModelPropertyId": "`a1b2c3d4-5678-90ab-cdef-44444EXAMPLE`",
        "interfaceAssetModelPropertyId": "`a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`"
      }
    ]
  }'
```

To retrieve information about an interface relationship, use the
`DescribeAssetModelInterfaceRelationship` operation:

```
aws iotsitewise describe-asset-model-interface-relationship \
  --asset-model-id "`a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`" \
  --interface-asset-model-id "`a1b2c3d4-5678-90ab-cdef-22222EXAMPLE`"
```

To list all asset models that have a specific interface applied to them, use the
`ListInterfaceRelationships` operation:

```
aws iotsitewise list-interface-relationships \
  --interface-asset-model-id "`a1b2c3d4-5678-90ab-cdef-22222EXAMPLE`" \
  --max-results 10
```

To delete an interface relationship, use the
`DeleteAssetModelInterfaceRelationship` operation:

```
aws iotsitewise delete-asset-model-interface-relationship \
  --asset-model-id "`a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`" \
  --interface-asset-model-id "`a1b2c3d4-5678-90ab-cdef-22222EXAMPLE`"
```
