# Enabling permissions for a third-party query

engine to call application integration API operations

Follow these steps to allow a third-party query engine to call application integration API
operations through the AWS Lake Formation console, the AWS CLI or API/SDK.

Console

###### To register your account for external data filtering:

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the left-side navigation, expand **Administration**, and then
   choose **Application integration setting**.
3. On the **Application integration setting** page, choose the
   option **Allow external engines to filter data in Amazon S3
   locations registered with Lake Formation**.
4. Enter the session tags that you created for the third-party engine. For
   information about session tags, see [Passing
   session tags in AWS STS](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md") in the _AWS Identity and Access Management User
   Guide_.
5. Enter the account IDs for users that can use the third-party engine to access
   unfiltered metadata information and the data access credentials of resources in the
   current account.

You can also use the AWS account ID field for configuring cross-account
access.

![The screenshot shows the Application integration settings page for Lake Formation. The option Allow external engines to filter data in Amazon S3 locations registered with Lake Formationis selected. For Session tag values, the text box is empty, but there are six tags displayed below the field, with the values "engine1, "engine2", "engine3", "session1", "session2", and "session3". The last field shows the AWS account IDs field. The text field is empty, but there are three tags displayed below this field with account IDs. The account ID values are redacted.](images/cred-vending-external-data-filtering.png)

CLI
Use the `put-data-lake-settings` CLI command to set the following
parameters.

There are three fields to configure when using this AWS CLI command:

- `allow-external-data-filtering` – (boolean) Indicates that a
  third-party engine can access unfiltered metadata information and data access
  credentials of resources in the current account.
- `external-data-filtering-allow-list` – (array) A list of
  account IDs that can access unfiltered metadata information and data access
  credentials of resources in the current account when using a third-party engine.
  When AllowExternalDataFiltering is set to true, the ExternalDataFilteringAllowList
  property must include at least one account ID. An empty list is not
  allowed.
- `authorized-sessions-tag-value-list` – (array) A list of
  authorized session tag values (strings). If an IAM role credential has been
  attached with an authorized key-value pair, then if the session tag is included in
  the list, the session is granted access to unfiltered metadata information and data
  access credentials on resources in the configured account. The authorized session
  tag key is defined as `*LakeFormationAuthorizedCaller*`.
- `AllowFullTableExternalDataAccess` - (boolean) Whether to allow a
  third-party query engine to get data access credentials without session tags when
  a caller has full data access permissions.

For example:

```
aws lakeformation put-data-lake-settings --cli-input-json file://datalakesettings.json

{
  "DataLakeSettings": {
    "DataLakeAdmins": [
      {
        "DataLakePrincipalIdentifier": "arn:aws:iam::111111111111:user/lakeAdmin"
      }
    ],
    "CreateDatabaseDefaultPermissions": [],
    "CreateTableDefaultPermissions": [],
    "TrustedResourceOwners": [],
    "AllowExternalDataFiltering": true,
    "ExternalDataFilteringAllowList": [
        {"DataLakePrincipalIdentifier": "111111111111"}
        ],
    "AuthorizedSessionTagValueList": ["engine1"],
    "AllowFullTableExternalDataAccess": false
    }


}
```

API/SDK
Use the `PutDataLakeSetting` API operation to set the following parameters.

There are three fields to configure when using this API operation:

- `AllowExternalDataFiltering` – (Boolean) Indicates whether a
  third-party engine can access unfiltered metadata information and data access
  credentials of resources in the current account.
- `ExternalDataFilteringAllowList` – (array) A list of account IDs that
  can access unfiltered metadata information and the data access credentials of resources
  in the current account using a third-party engine.
- `AuthorizedSectionsTagValueList` – (array) A list of authorized tag
  values (strings). If an IAM role credential has been attached with an authorized
  tag, then the session is granted access to unfiltered metadata information and the data
  access credentials on resources in the configured account. The authorized session
  tag key is defined as `*LakeFormationAuthorizedCaller*`.
- `AllowFullTableExternalDataAccess` - (boolean) Whether to allow a third-party query engine to get data access credentials without session tags when a caller has full data access permissions.

For example:

```
//Enable session tag on existing data lake settings
public void sessionTagSetUpForExternalFiltering(AWSLakeFormationClient lakeformation) {
    GetDataLakeSettingsResult getDataLakeSettingsResult = lfClient.getDataLakeSettings(new GetDataLakeSettingsRequest());
    DataLakeSettings dataLakeSettings = getDataLakeSettingsResult.getDataLakeSettings();

    //set account level flag to allow external filtering
    dataLakeSettings.setAllowExternalDataFiltering(true);

    //set account that are allowed to call credential vending or Glue GetFilteredMetadata API
    List<DataLakePrincipal> allowlist = new ArrayList<>();
    allowlist.add(new DataLakePrincipal().withDataLakePrincipalIdentifier("111111111111"));
    dataLakeSettings.setWhitelistedForExternalDataFiltering(allowlist);

    //set registered session tag values
    List<String> registeredTagValues = new ArrayList<>();
    registeredTagValues.add("engine1");
    dataLakeSettings.setAuthorizedSessionTagValueList(registeredTagValues);

    lakeformation.putDataLakeSettings(new PutDataLakeSettingsRequest().withDataLakeSettings(dataLakeSettings));
}
```
