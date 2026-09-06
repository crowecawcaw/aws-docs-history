

# Manage interfaces, linked asset models, and properties
<a name="interfaces-manage"></a>

After creating interfaces and linking them to asset models, you can manage relationships, edit, and delete interfaces through the console or AWS CLI.

## Modify an interface and asset model relationship
<a name="interface-edit"></a>

To change an interface's relationship to an asset model, do the following in either the AWS IoT SiteWise console or through AWS CLI:

------
#### [ Console ]

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/) and choose **Models** from the navigation pane.

1. Select the interface you want modify.

1. Choose the asset model to modify and edit it.

   You can follow the [Apply an interface to an asset model](interfaces-link-asset-model.md) instructions to link a different asset model.

1. Choose **Apply interface** to save your changes.

------
#### [ AWS CLI ]

To edit an interface and asset model relationship, use the `PutAssetModelInterfaceRelationship` action. Replace {{your-asset-model-id}} and {{your-interface-asset-model-id}} with your own values. For more information, see [PutAssetModelInterfaceRelationship](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutAssetModelInterfaceRelationship.html) in the *AWS IoT SiteWise API Reference*.

```
aws iotsitewise put-asset-model-interface-relationship \
    --asset-model-id {{your-asset-model-id}} \
    --interface-asset-model-id {{your-interface-asset-model-id}}
```

------

## Modify an interface property mapping
<a name="interface-edit-property"></a>

To change an interface's property, do the following in either the AWS IoT SiteWise console or through AWS CLI:

------
#### [ Console ]

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/) and choose **Models** from the navigation pane.

1. Select the interface for which you want modify property mappings. The **Edit property mappings** page appears.

1. In the **Property mappings** section, filter the list to find the appropriate property mappings.

1. Change the properties using the **Model property** column.

------
#### [ AWS CLI ]

To edit an interface and asset model relationship, use the `PutAssetModelInterfaceRelationship` action. Replace {{your-asset-model-id}} and {{your-interface-asset-model-id}} with your own values. For more information, see [PutAssetModelInterfaceRelationship](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutAssetModelInterfaceRelationship.html) in the *AWS IoT SiteWise API Reference*.

```
aws iotsitewise put-asset-model-interface-relationship \
    --asset-model-id {{your-asset-model-id}} \
    --interface-asset-model-id {{your-interface-asset-model-id}} \
```

------

## List interfaces linked to an asset model
<a name="interface-list"></a>

To get a list of interfaces applied to an asset model, do the following in either the AWS IoT SiteWise console or through AWS CLI:

------
#### [ Console ]

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/) and choose **Models** from the navigation pane.

1. In the **Models** section, choose the appropriate asset model or interface. You can view a list of either applied interfaces or linked asset models on the model's corresponding details page. 
   + When viewing a particular interface, see the **Linked asset models** section.
   + When viewing a particular asset model, see the **Applied interfaces** section.

------
#### [ AWS CLI ]

To list interfaces, you can use the `ListInterfaceRelationships` operation. Replace {{your-interface-asset-model-id}} with your own value. For more information, see [ListInterfaceRelationships](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListInterfaceRelationships.html) in the *AWS IoT SiteWise API Reference*.

```
aws iotsitewise list-interface-relationships \
    --interface-asset-model-id {{your-interface-asset-model-id}} \
    [--next-token {{your-next-token}}] \
    [--max-results {{20}}]
```

------

## View the details of an interface and asset model relationship
<a name="interface-view-details"></a>

To see the details of an interface applied to an asset model, do the following in either the AWS IoT SiteWise console or through AWS CLI:

------
#### [ Console ]

View the details of applied interfaces and linked asset models.

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/) and choose **Models** from the navigation pane.

1. In the **Models** section, search for the appropriate asset model or interface. Select the model or interface's **Name** to open up a page containing more details.

------
#### [ AWS CLI ]

To view interface details for an interface and asset model relationship, use the `DescribeAssetModelInterfaceRelationship` action. Replace {{your-asset-model-id}} and {{your-interface-asset-model-id}} with your own values. For more information, see [DescribeAssetModelInterfaceRelationship](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModelInterfaceRelationship.html) in the *AWS IoT SiteWise API Reference*.

```
aws iotsitewise describe-asset-model-interface-relationship \
    --asset-model-id {{your-asset-model-id}} \
    --interface-asset-model-id {{your-interface-asset-model-id}}
```

------

## Remove an interface applied to an asset model
<a name="interface-remove"></a>

To remove an interface applied to an asset model, do the following in either the AWS IoT SiteWise console or through AWS CLI:

------
#### [ Console ]

We recommend removing an interface through the asset model. You can also delete an interface or unlink an interface through a particular interface's page.

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/) and choose **Models** from the navigation pane.

1. Select the appropriate asset model from which to remove the interface relationship.

1. Choose **Unlink asset model**.

------
#### [ AWS CLI ]

To remove an interface relationship from an asset model, you can use the `DeleteAssetModelInterfaceRelationship` action. Replace {{your-interface-asset-model-id}} with your own value. For more information, see [DeleteAssetModelInterfaceRelationship](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAssetModelInterfaceRelationship.html) in the *AWS IoT SiteWise API Reference*.

```
aws iotsitewise delete-asset-model-interface-relationship \
    --asset-model-id {{your-asset-model-id}} \
    --interface-asset-model-id {{your-interface-asset-model-id}}
```

------