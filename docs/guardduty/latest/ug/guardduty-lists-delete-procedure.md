

# Deleting entity list or IP address list
<a name="guardduty-lists-delete-procedure"></a>

When you no longer want to keep a list entry in your entity set or IP address set, you can delete it. It might take a few minutes for the process to complete. For more information, see [Important considerations for GuardDuty lists](guardduty_upload-lists.md#guardduty-lists-entity-sets-considerations). 

If the status of the list is **Activating** or **Deactivating**, you must wait for a few minutes before performing any action. For more information, see [Understanding list statuses](guardduty_upload-lists.md#guardduty-entity-list-statuses).

Choose one of the access methods to delete the list.

------
#### [ Console ]

**To delete entity list or IP address list**

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Lists**.

1. On the **List** page, select the tab in which you want to delete the list - **Entity lists** or **IP address list**. 

1. In the selected tab, select the list that you want to delete. 

1. Choose **Actions**, and then choose **Delete**. 

   The list status will change to **Delete Pending**. It might take a few minutes for the list to get deleted.

------
#### [ API/CLI ]

To begin with the following procedures, you need the ID, such as `trustedEntitySetId`, `threatEntitySetId`, `trustedIpSet`, or `threatIpSet`, that is associated with the list resource you want to delete. 

**To delete a trusted entity list**

1. Run [DeleteTrustedEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteTrustedEntitySet.html). Make sure to provide the `detectorId` of the member account for which you want to delete this trusted entity list. To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API. 

1. Alternatively, you can do this by running the following AWS Command Line Interface command: 

   ```
   aws guardduty delete-trusted-entity-set \
   --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} \
   --trusted-entity-set-id {{d4b94fc952d6912b8f3060768example}}
   ```

   Replace `detector-id` with the detector ID of the member account for which you will delete the trusted entity list, and other placeholder values that are {{shown in red}}.

**To deactivate threat entity lists**

1. Run [DeleteThreatEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteThreatEntitySet.html). Make sure to provide the `detectorId` of the member account for which you want to delete this threat entity list. To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API. 

1. Alternatively, you can do this by running the following AWS Command Line Interface command: 

   ```
   aws guardduty delete-threat-entity-set \
   --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} \
   --threat-entity-set-id {{d4b94fc952d6912b8f3060768example}}
   ```

   Replace `detector-id` with the detector ID of the member account for which you will delete the threat entity list, and other placeholder values that are {{shown in red}}.

**To delete a trusted IP address list**

1. Run [DeleteIPSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteIPSet.html). Make sure to provide the `detectorId` of the member account for which you want to delete this trusted IP address list. To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API. 

1. Alternatively, you can do this by running the following AWS Command Line Interface command and make sure to replace the `detector-id` with the detector ID of the member account for which you will delete the trusted IP address list.

   ```
   aws guardduty delete-ip-set \
   --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} \
   --ip-set-id {{d4b94fc952d6912b8f3060768example}}
   ```

   Replace `detector-id` with the detector ID of the member account for which you will delete the threat entity list, and other placeholder values that are {{shown in red}}.

**To delete threat IP list**

1. Run [DeleteThreatIntelSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteThreatIntelSet.html). Make sure to provide the `detectorId` of the member account for which you want to delete this threat IP address list. To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API. 

1. Alternatively, you can do this by running the following AWS Command Line Interface command and make sure to replace the `detector-id` with the detector ID of the member account for which you will delete the threat IP list.

   ```
   aws guardduty delete-threat-intel-set \
   --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} \
   --threat-intel-set-id {{d4b94fc952d6912b8f3060768example}}
   ```

   Replace `detector-id` with the detector ID of the member account for which you will delete the threat entity list, and other placeholder values that are {{shown in red}}.

------