# De-activating entity list

or IP address list

When you no longer want GuardDuty to use a list, you can deactivate it. It might take
a few minutes for the process to complete. For more information, see
[Important
considerations for GuardDuty lists](guardduty_upload-lists.md#guardduty-lists-entity-sets-considerations "guardduty_upload-lists.md#guardduty-lists-entity-sets-considerations"). After the list gets deactivated,
the entries in the entity list or IP address list will not impact threat detection in GuardDuty.

Choose one of the access methods to deactivate the list.

Console

###### To deactivate entity list or IP address list

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Lists**.
3. On the **List** page, select the tab in which you
   want to deactivate the list - **Entity lists** or
   **IP address list**.
4. In the selected tab, select the list that you want to deactivate.
5. Choose **Actions**, and then choose
   **Deactivate**.
6. Confirm the action and choose **Deactivate**.

API/CLI
To begin with the following procedures, you need the ID, such
as `trustedEntitySetId`, `threatEntitySetId`,
`trustedIpSet`, or `threatIpSet`, that is
associated with the list resource you want to deactivate.

###### To deactivate a trusted entity list

1. Run [UpdateTrustedEntitySet](../APIReference/API_UpdateTrustedEntitySet.md "../APIReference/API_UpdateTrustedEntitySet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to deactivate this trusted entity list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.
2. Alternatively, you can do this by running the following
   AWS Command Line Interface command:

```
aws guardduty update-trusted-entity-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--trusted-entity-set-id `d4b94fc952d6912b8f3060768example` \
--no-activate

```

Replace `detector-id` with the detector ID of the
member account for which you will deactivate the trusted entity
list, and other placeholder values that are `shown in red`.

###### To deactivate threat entity lists

1. Run [UpdateThreatEntitySet](../APIReference/API_UpdateThreatEntitySet.md "../APIReference/API_UpdateThreatEntitySet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to deactivate this threat entity list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.
2. Alternatively, you can do this by running the following
   AWS Command Line Interface command:

```
aws guardduty update-threat-entity-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--threat-entity-set-id `d4b94fc952d6912b8f3060768example` \
--no-activate

```

Replace `detector-id` with the detector ID of the
member account for which you will create the threat entity
list, and other placeholder values that are `shown in red`.

###### To deactivate a trusted IP address list

1. Run [UpdateIPSet](../APIReference/API_UpdateIPSet.md "../APIReference/API_UpdateIPSet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to deactivate this trusted IP address list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.
2. Alternatively, you can do this by running the following
   AWS Command Line Interface command and make sure to replace the
   `detector-id` with the detector ID of the
   member account for which you will deactivate the trusted IP address
   list.

```
aws guardduty update-ip-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--ip-set-id `d4b94fc952d6912b8f3060768example` \
--no-activate

```

###### To deactivate threat IP list

1. Run [UpdateThreatIntelSet](../APIReference/API_UpdateThreatIntelSet.md "../APIReference/API_UpdateThreatIntelSet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to deactivate this threat IP address list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.
2. Alternatively, you can do this by running the following
   AWS Command Line Interface command and make sure to replace the
   `detector-id` with the detector ID of the
   member account for which you will deactivate the threat IP
   list.

```
aws guardduty update-threat-intel-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--threat-intel-set-id `d4b94fc952d6912b8f3060768example` \
--no-activate

```
