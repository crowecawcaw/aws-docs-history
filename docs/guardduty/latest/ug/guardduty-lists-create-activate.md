# Adding and activating an entity list or IP

list

Entity lists and IP address lists help you customize the threat detection capabilities in GuardDuty. For more
information about these lists, see [Understanding entity lists and IP address
lists](guardduty_upload-lists.md#guardduty-threat-intel-list-entity-sets "guardduty_upload-lists.md#guardduty-threat-intel-list-entity-sets").
To manage the trusted and threat intelligence data for your AWS environment, GuardDuty
recommends using entity lists. Before you begin, see [Setting up prerequisites for entity lists and IP address
lists](guardduty-lists-prerequisites.md "guardduty-lists-prerequisites.md").

Choose one of the following access methods to add and
activate a trusted entity list, threat entity list, trusted IP list, or a threat IP
list.

Console

###### (Optional)

step 1: Fetching location URL of your list

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose
   **Buckets**.
3. Choose the Amazon S3 bucket name that contains the specific list that
   you want to add.
4. Choose the object (list) name to view its details.
5. Under the **Properties** tab, copy the
   **S3 URI** for this object.

###### Step 2: Adding trusted or threat intelligence data

1.  Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2.  In the navigation pane, choose **Lists**.
3.  On the **Lists** page, choose **Entity
    lists** or **IP address lists**
    tab.
4.  Based on your selected tab, choose to add a trusted list or a
    threat list.
5.  In the dialog box to add either trusted or threat list, do the
    following steps:
    1. For **List name**, enter a name for your
       list.

    **List naming constraints** – The name of your list can include
    lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_).

    For an IP address list, the name
    of your list must be unique within an AWS account and Region. 2. For **Location**, provide the location
    where you have uploaded your list. If you don't already have
    it, see [Step 1: Fetching location URL of your list](#fetch-location-URL-list-manage "#fetch-location-URL-list-manage").

    Applies only to custom threat and custom trusted entity sets – If you provide a
    location URL that doesn't match the following supported formats, then you will receive an error message during list addition and activation.

    ###### Format of location URL:

        * https://s3.amazonaws.com/bucket.name/file.txt
        * https://s3-aws-region.amazonaws.com/bucket.name/file.txt
        * http://bucket.s3.amazonaws.com/file.txt
        * http://bucket.s3-aws-region.amazonaws.com/file.txt
        * s3://bucket.name/file.txt

    3. (Optional) For **Expected bucket owner**,
       you can enter the AWS account ID that owns the Amazon S3 bucket
       specified in the **Location** field.

    When you don't specify an AWS account ID owner, then
    GuardDuty behaves differently for entity lists and IP address lists. For entity lists,
    GuardDuty will validate that the current member account owns the S3 bucket specified in the
    **Location** field. For IP address lists, if you don't
    specify an AWS account ID owner, GuardDuty doesn't perform any validation.

    If GuardDuty finds that this S3 bucket doesn't belong to the specified
    account ID, you will get an error at the time of activating the list. 4. Select the **I agree** check box. 5. Choose **Add list**. By default, the
    **Status** of the added list is
    **Inactive**. For the list to be
    effective, you must activate the list.

###### Step 3: Activating an entity list or IP

address list

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Lists**.
3. On the **Lists** page, select the tab in which
   you want to activate the list - **Entity lists** or
   **IP address lists**.
4. Select one list that you want to activate. This will enable the
   **Action** and **Edit**
   menu.
5. Choose **Action**, and then choose
   **Activate**.

API/CLI

###### To add and activate a trusted entity list

1. Run [CreateTrustedEntitySet](../APIReference/API_CreateTrustedEntitySet.md "../APIReference/API_CreateTrustedEntitySet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to create this trusted entity list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

**List naming constraints** – The name of your list can include
lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_). 2. Alternatively, you can do this by running the following
AWS Command Line Interface command:

```
aws guardduty create-trusted-entity-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--name "`AnyOrganization ListEXAMPLE`" \
--format `TXT` \
--location "`https://s3.amazonaws.com/amzn-s3-demo-bucket/DOC-EXAMPLE-SOURCE-FILE.format`" \
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

###### To add and activate threat entity lists

1. Run [CreateThreatEntitySet](../APIReference/API_CreateThreatEntitySet.md "../APIReference/API_CreateThreatEntitySet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to create this threat entity list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

**List naming constraints** – The name of your list can include
lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_). 2. Alternatively, you can do this by running the following
AWS Command Line Interface command:

```
aws guardduty create-threat-entity-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--name "`AnyOrganization ListEXAMPLE`" \
--format `TXT` \
--location "`https://s3.amazonaws.com/amzn-s3-demo-bucket/DOC-EXAMPLE-SOURCE-FILE.format`" \
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

###### To add and activate a trusted IP address list

1. Run [CreateIPSet](../APIReference/API_CreateIPSet.md "../APIReference/API_CreateIPSet.md"). Make sure to provide the
   `detectorId` of the member account for which you want
   to create this trusted IP address list. To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

For an IP address list, the name
of your list must be unique within an AWS account and Region.

**List naming constraints** – The name of your list can include
lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_). 2. Alternatively, you can do this by running the following
AWS Command Line Interface command and make sure to replace the
`detector-id` with the detector ID of the
member account for which you will update the trusted IP address
list.

```
aws guardduty create-ip-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--name "`AnyOrganization ListEXAMPLE`" \
--format `TXT` \
--location "`https://s3.amazonaws.com/amzn-s3-demo-bucket/DOC-EXAMPLE-SOURCE-FILE.format`" \
--activate

```

Replace `detector-id` with the detector ID of the
member account for which you will create the trusted IP
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
AWS Command Line Interface command and make sure to replace the
`detector-id` with the detector ID of the
member account for which you will update the threat IP
list.

```
aws guardduty create-threat-intel-set \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--name "`AnyOrganization ListEXAMPLE`" \
--format `TXT` \
--location "`https://s3.amazonaws.com/amzn-s3-demo-bucket/DOC-EXAMPLE-SOURCE-FILE.format`" \
--activate

```

Replace `detector-id` with the detector ID of the
member account for which you will create the threat IP
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

After you activate an entity list or IP address list, it might take a few
minutes for this list to be effective. For more information, see [Important
considerations for GuardDuty lists](guardduty_upload-lists.md#guardduty-lists-entity-sets-considerations "guardduty_upload-lists.md#guardduty-lists-entity-sets-considerations").
