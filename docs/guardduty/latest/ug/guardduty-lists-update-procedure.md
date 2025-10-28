# Updating an entity list or IP address

list

Entity lists and IP address lists help you customize the threat detection capabilities in GuardDuty. For more
information about these lists, see [Understanding entity lists and IP address
lists](guardduty_upload-lists.md#guardduty-threat-intel-list-entity-sets "guardduty_upload-lists.md#guardduty-threat-intel-list-entity-sets").

You can update the name of a list, S3 bucket location, expected bucket owner account ID,
and the entries in an existing list. If you update the
entries in a list, you must follow the steps to activate the list again for
GuardDuty to use the latest version of the list. After you update or
activate an entity list or IP address list, it might take a few minutes
for this list to be effective. For more information,
see [Important
considerations for GuardDuty lists](guardduty_upload-lists.md#guardduty-lists-entity-sets-considerations "guardduty_upload-lists.md#guardduty-lists-entity-sets-considerations").

###### Note

If the status of a list is **Activating**, **Deactivating**,
or **Delete Pending**, you must wait for a few minutes before performing any action. For information
about these statuses, see [Understanding list statuses](guardduty_upload-lists.md#guardduty-entity-list-statuses "guardduty_upload-lists.md#guardduty-entity-list-statuses").

Choose one of the access methods to update an entity list or IP address list.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Lists**.
3. On the **Lists** page, select the appropriate tab

- **Entity lists** or **IP address
  lists**.

4. Select one list (trusted or threat) that you want to update. This
   will enable the **Action** and
   **Edit** menu.
5. Choose **Edit**.
6. In the dialog box to update the list, specify the details that you
   want to update.

**List naming constraints** – The name of your list can include
lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_).

For an IP address list, the name
of your list must be unique within an AWS account and Region.

Applies only to custom threat and custom trusted entity sets – If you provide a
location URL that doesn't match the following supported formats, then you will receive an error message during list addition and activation. 7. (Optional) For **Expected bucket owner**, you can
enter the AWS account ID that owns the Amazon S3 bucket specified in
the **Location** field.

When you don't specify an AWS account ID owner, then
GuardDuty behaves differently for entity lists and IP address lists. For entity lists,
GuardDuty will validate that the current member account owns the S3 bucket specified in the
**Location** field. For IP address lists, if you don't
specify an AWS account ID owner, GuardDuty doesn't perform any validation.

If GuardDuty finds that this S3 bucket doesn't belong to the specified
account ID, you will get an error at the time of activating the list. 8. Select the **I agree** check box, and then choose
**Update list**.

API/CLI
To begin with the following procedures, you need the ID, such
as `trustedEntitySetId`, `threatEntitySetId`,
`trustedIpSet`, or `threatIpSet`, that is
associated with the list resource you want to update.

###### To update and activate a trusted entity list

1. Run [UpdateTrustedEntitySet](../APIReference/API_UpdateTrustedEntitySet.md "../APIReference/API_UpdateTrustedEntitySet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to update this trusted entity list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

**List naming constraints** – The name of your list can include
lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_). 2. Alternatively, you can do this by running the following
AWS Command Line Interface command that updates the `name` of the list and also activates this list:

```
aws guardduty update-trusted-entity-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--name "`AnyOrganization ListEXAMPLE`" \
--trusted-entity-set-id `d4b94fc952d6912b8f3060768example` \
--activate

```

Replace `detector-id` with the detector ID of the
member account for which you will create the trusted entity
list, and other placeholder values that are `shown in red`.

If you don't want to activate this newly created list, then replace
the parameter `--activate` with `--no-activate`.

The `expected-bucket-owner` parameter is optional. Whether or not
you specify the value for this parameter, GuardDuty validates that the AWS account ID associated
with this `--detector-id` value owns the S3 bucket specified in the
`--location` parameter. If GuardDuty finds that this S3 bucket doesn't
belong to the specified account ID, you will get an error at the time of activating
this list.

Applies only to custom threat and custom trusted entity sets – If you provide a
location URL that doesn't match the following supported formats, then you will receive an error message during list addition and activation.

###### To update and activate a threat entity list

1. Run [UpdateThreatEntitySet](../APIReference/API_UpdateThreatEntitySet.md "../APIReference/API_UpdateThreatEntitySet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to create this threat entity list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

**List naming constraints** – The name of your list can include
lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_). 2. Alternatively, you can do this by running the following
AWS Command Line Interface command that updates the `name` of the list and also activates this list:

```
aws guardduty update-threat-entity-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--name "`AnyOrganization ListEXAMPLE`" \
--threat-entity-set-id `d4b94fc952d6912b8f3060768example` \
--activate

```

Replace `detector-id` with the detector ID of the
member account for which you will create the threat entity
list, and other placeholder values that are `shown in red`.

If you don't want to activate this newly created list, then replace
the parameter `--activate` with `--no-activate`.

The `expected-bucket-owner` parameter is optional. Whether or not
you specify the value for this parameter, GuardDuty validates that the AWS account ID associated
with this `--detector-id` value owns the S3 bucket specified in the
`--location` parameter. If GuardDuty finds that this S3 bucket doesn't
belong to the specified account ID, you will get an error at the time of activating
this list.

Applies only to custom threat and custom trusted entity sets – If you provide a
location URL that doesn't match the following supported formats, then you will receive an error message during list addition and activation.

###### To update and activate a trusted IP address list

1. Run [CreateIPSet](../APIReference/API_CreateIPSet.md "../APIReference/API_CreateIPSet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to update this trusted IP address list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

**List naming constraints** – The name of your list can include
lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_).

For an IP address list, the name
of your list must be unique within an AWS account and Region. 2. Alternatively, you can do this by running the following
AWS Command Line Interface command that also activates the list:

```
aws guardduty update-ip-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--name "`AnyOrganization ListEXAMPLE`" \
--ip-set-id `d4b94fc952d6912b8f3060768example` \
--activate

```

Replace `detector-id` with the detector ID of the
member account for which you will update the trusted IP
list, and other placeholder values that are `shown in red`.

If you don't want to activate this newly created list, then replace
the parameter `--activate` with `--no-activate`.

The `expected-bucket-owner` parameter is optional. When you don't specify
the account ID that owns the S3 bucket, GuardDuty doesn't perform any validation. When you
specify the account ID for the `expected-bucket-owner` parameter, GuardDuty validates that this
AWS account ID owns the S3 bucket specified in the
`--location` parameter. If GuardDuty finds that this S3 bucket doesn't
belong to the specified account ID, you will get an error at the time of activating
this list.

###### To add and activate threat IP lists

1. Run [CreateThreatIntelSet](../APIReference/API_CreateThreatIntelSet.md "../APIReference/API_CreateThreatIntelSet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to create this threat IP address list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

**List naming constraints** – The name of your list can include
lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_).

For an IP address list, the name
of your list must be unique within an AWS account and Region. 2. Alternatively, you can do this by running the following
AWS Command Line Interface command that also activates the list:

```
aws guardduty update-threat-intel-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--name "`AnyOrganization ListEXAMPLE`" \
--threat-intel-set-id `d4b94fc952d6912b8f3060768example` \
--activate

```

Replace `detector-id` with the detector ID of the
member account for which you will update the threat IP
list, and other placeholder values that are `shown in red`.

If you don't want to activate this newly created list, then replace
the parameter `--activate` with `--no-activate`.

The `expected-bucket-owner` parameter is optional. When you don't specify
the account ID that owns the S3 bucket, GuardDuty doesn't perform any validation. When you
specify the account ID for the `expected-bucket-owner` parameter, GuardDuty validates that this
AWS account ID owns the S3 bucket specified in the
`--location` parameter. If GuardDuty finds that this S3 bucket doesn't
belong to the specified account ID, you will get an error at the time of activating
this list.
