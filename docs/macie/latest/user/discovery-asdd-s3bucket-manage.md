# Adjusting sensitivity scores for S3

buckets

As you review and evaluate statistics, data, and other results of automated sensitive data discovery, there might be
cases where you want to fine tune sensitivity assessments of your Amazon Simple Storage Service (Amazon S3) buckets. You
might also want to capture the results of investigations that you or your organization performs
for specific buckets. If you're the Amazon Macie administrator for an organization or you have a standalone
Macie account, you can make these changes by adjusting the sensitivity score and other settings for
individual buckets. If you have a member account in an organization, work with your Macie administrator
to adjust the settings for buckets that you own. Only the Macie administrator for your organization can
adjust these settings for your buckets.

If you're a Macie administrator or you have a standalone Macie account, you can adjust the
sensitivity score for an S3 bucket in the following ways:

- **Assign a sensitivity score** – By default, Macie
  automatically calculates a bucket's sensitivity score. The score is based primarily on the amount
  of sensitive data that Macie has found in a bucket, and the amount of data that Macie has
  analyzed in a bucket. For more information, see [Sensitivity scoring for S3
  buckets](discovery-scoring-s3.md "discovery-scoring-s3.md").

You can override a bucket's calculated score and manually assign the maximum score
(_100_), which also applies the _Sensitive_ label to the bucket. If you do this, Macie continues to perform
automated sensitive data discovery for the bucket. However, subsequent analyses don't affect the bucket's score. To
calculate the score automatically again, change the setting again.

- **Exclude or include sensitive data types in the
  sensitivity score** – If it's calculated automatically, a bucket's sensitivity score
  is based partly on the amount of sensitive data that Macie has found in the bucket. This
  derives primarily from the nature and number of sensitive data types that Macie has found,
  and the number of occurrences of each type. By default, Macie includes occurrences of all
  types of sensitive data when it calculates a bucket's score.

You can adjust the calculation by excluding or including specific types of sensitive
data in a bucket's score. For example, if Macie detected mailing addresses in a bucket and
you determine that this is acceptable, you can exclude all occurrences of mailing addresses
from the bucket's score. If you exclude a sensitive data type, Macie continues to inspect
the bucket for that type of data, and report occurrences that it finds. However, those
occurrences don't affect the bucket's score. To include a sensitive data type in the score
again, change the setting again.
You can also exclude an S3 bucket from subsequent analyses. If you exclude a bucket,
existing sensitive data discovery statistics and details for the bucket persist. For example, the bucket's current
sensitivity score remains unchanged. However, Macie stops analyzing objects in the bucket when it
performs automated sensitive data discovery. After you exclude a bucket, you can include it again later.

If you change a setting that affects the sensitivity score for an S3 bucket,
Macie immediately begins to recalculate the score. Macie also updates relevant statistics and
other information that it provides about the bucket and your Amazon S3 data overall. For example, if
you assign the maximum score to a bucket, Macie increments the count of _Sensitive_ buckets in aggregated statistics.

###### To adjust the sensitivity score or other settings for an S3 bucket

To adjust the sensitivity score or other settings for an S3 bucket, you can use the Amazon Macie
console or the Amazon Macie API.

Console
Follow these steps to adjust the sensitivity score or a setting for an S3 bucket by using
the Amazon Macie console.

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **S3 buckets**. The **S3
   buckets** page displays your bucket inventory.

By default, the page doesn't display data for buckets that are currently excluded
from analyses. If you're the Macie administrator for an organization, it also doesn't display
data for accounts that automated sensitive data discovery is currently disabled for. To display this data,
choose **X** in the **Is monitored by automated
discovery** filter token below the filter box. 3. Choose the S3 bucket that has a setting to adjust. You can choose the bucket by
using the table view (
![The table view button, which is a button that displays three black horizontal lines.](images/btn-s3-table-view.png)
) or the interactive map
(
![The map view button, which is a button that displays four black squares.](/images/macie/latest/user/images/btn-s3-map-view.png)
). 4. In the details panel, do any of the following:

    * To override the calculated sensitivity score and manually assign a score, turn on
     **Assign maximum score** (
    ![A toggle switch with a gray background and the toggle positioned to the left.](images/tgl-gray-off.png)
    ). This changes the bucket's score to *100* and applies the *Sensitive*
     label to the bucket.
    * To assign a sensitivity score that Macie calculates automatically, turn off
     **Assign maximum score** (
    ![A toggle switch with a blue background and the toggle positioned to the right.](images/tgl-blue-on.png)
    ).
    * To exclude or include specific types of sensitive data in the sensitivity score,
     choose the **Sensitivity** tab. In the
     **Detections** table, select the checkbox for the sensitive
     data type to exclude or include. Then, on the **Actions** menu,
     choose **Exclude from score** to exclude the type or choose
     **Include in score** to include the type.


    In the table, the **Sensitive data type** field specifies the
     managed data identifier or custom data identifier that detected the data. For a
     managed data identifier, this is a unique identifier (ID) that describes the type
     of sensitive data that the identifier is designed to detect—for example,
     **USA\_PASSPORT\_NUMBER** for US passport numbers. For details
     about each managed data identifier, see [Using managed data
     identifiers](managed-data-identifiers.md "managed-data-identifiers.md").
    * To exclude the bucket from subsequent analyses, turn on **Exclude from
     automated discovery** (
    ![A toggle switch with a gray background and the toggle positioned to the left.](images/tgl-gray-off.png)
    ).
    * To include the bucket in subsequent analyses, if you previously excluded it,
     turn off **Exclude from automated discovery** (
    ![A toggle switch with a blue background and the toggle positioned to the right.](images/tgl-blue-on.png)
    ).

API
To adjust the sensitivity score or a setting for an S3 bucket programmatically, you have
several options. The appropriate option depends on what you want to adjust.

**Assign a sensitivity score**
To assign a sensitivity score to an S3 bucket, use the [UpdateResourceProfile](../APIReference/resource-profiles.md "../APIReference/resource-profiles.md")
operation. In your request, use the `resourceArn` parameter to specify the
Amazon Resource Name (ARN) of the bucket. For the `sensitivityScoreOverride`
parameter, do one of the following:

- To override the calculated score and manually assign the maximum score, specify
  `100`.
- To assign a score that Macie calculates automatically, omit the parameter. If this
  parameter is null, Macie calculates and assigns the score.

If you're using the AWS Command Line Interface (AWS CLI), run the [update-resource-profile](../../../cli/latest/reference/macie2/update-resource-profile.md "../../../cli/latest/reference/macie2/update-resource-profile.md") command to assign a sensitivity score to an S3 bucket. In
your request, use the `resource-arn` parameter to specify the ARN of the
bucket. Omit or use the `sensitivity-score-override` parameter to specify which
score to assign.

If your request succeeds, Macie assigns the specified score and returns an empty
response.

**Exclude or include sensitive data types in the
sensitivity score**

To exclude or include sensitive data types in the sensitivity score for an S3 bucket, use
the [UpdateResourceProfileDetections](../APIReference/resource-profiles-detections.md "../APIReference/resource-profiles-detections.md") operation. When you use this operation, you
overwrite the current inclusion and exclusion settings for a bucket's score. Therefore,
it's a good idea to first retrieve the current settings and determine which ones you want
to keep. To retrieve the current settings, use the [ListResourceProfileDetections](../APIReference/resource-profiles-detections.md "../APIReference/resource-profiles-detections.md") operation.

When you're ready to update the settings, use the `resourceArn` parameter
to specify the ARN of the S3 bucket. For the `suppressDataIdentifiers`
parameter, do one of the following:

- To exclude a sensitive data type from the bucket's score, use the
  `type` parameter to specify the type of data identifier that detected the
  data, a managed data identifier (`MANAGED`) or a custom data identifier
  (`CUSTOM`). Use the `id` parameter to specify the unique
  identifier for the managed or custom data identifier that detected the data.
- To include a sensitive data type in the bucket's score, don't specify any details
  for the managed or custom data identifier that detected the data.
- To include all sensitive data types in the bucket's score, don't specify any
  values. If the value for the `suppressDataIdentifiers` parameter is null
  (empty), Macie includes all types of detections when it calculates the score.

If you're using the AWS CLI, run the [update-resource-profile-detections](../../../cli/latest/reference/macie2/update-resource-profile-detections.md "../../../cli/latest/reference/macie2/update-resource-profile-detections.md") command to exclude or include
sensitive data types in the sensitivity score for an S3 bucket. Use the
`resource-arn` parameter to specify the ARN of the bucket. Use the
`suppress-data-identifiers` parameter to specify which sensitive data
types to exclude or include in the bucket's score. To first retrieve and review the
current settings for the bucket, run the [list-resource-profile-detections](../../../cli/latest/reference/macie2/list-resource-profile-detections.md "../../../cli/latest/reference/macie2/list-resource-profile-detections.md") command.

If your request succeeds, Macie updates the settings and returns an empty
response.

**Exclude or include an S3 bucket in analyses**

To exclude or subsequently include an S3 bucket in analyses, use the [UpdateClassificationScope](../APIReference/classification-scopes-id.md "../APIReference/classification-scopes-id.md") operation. Or, if you're using the AWS CLI, run
the [update-classification-scope](../../../cli/latest/reference/macie2/update-classification-scope.md "../../../cli/latest/reference/macie2/update-classification-scope.md") command. For additional details and examples,
see [Excluding or including S3 buckets
in automated sensitive data discovery](discovery-asdd-account-configure.md#discovery-asdd-account-configure-s3buckets "discovery-asdd-account-configure.md#discovery-asdd-account-configure-s3buckets").

The following examples show how to use the AWS CLI to adjust individual settings for an
S3 bucket. This first example manually assigns the maximum sensitivity score (`100`)
to a bucket. It overrides the bucket's calculated score.

```
`$` `aws macie2 update-resource-profile --resource-arn `arn:aws:s3:::amzn-s3-demo-bucket` --sensitivity-score-override 100`
```

Where `arn:aws:s3:::amzn-s3-demo-bucket` is the ARN of the S3
bucket.

The next example changes the sensitivity score for an S3 bucket to a score that Macie
calculates automatically. The bucket currently has a manually assigned score that
overrides the calculated score. This example removes that override by omitting the
`sensitivity-score-override` parameter from the request.

```
`$` `aws macie2 update-resource-profile --resource-arn `arn:aws:s3:::amzn-s3-demo-bucket2``
```

Where `arn:aws:s3:::amzn-s3-demo-bucket2` is the ARN of the
S3 bucket.

The following examples exclude particular types of sensitive data from the
sensitivity score for an S3 bucket. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 update-resource-profile-detections \
--resource-arn `arn:aws:s3:::amzn-s3-demo-bucket3` \
--suppress-data-identifiers '[{"type":"MANAGED","id":"`ADDRESS`"},{"type":"CUSTOM","id":"`3293a69d-4a1e-4a07-8715-208ddexample`"}]'`
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 update-resource-profile-detections ^
--resource-arn `arn:aws:s3:::amzn-s3-demo-bucket3` ^
--suppress-data-identifiers=[{\"type\":\"MANAGED\",\"id\":\"`ADDRESS`\"},{\"type\":\"CUSTOM\",\"id\":\"`3293a69d-4a1e-4a07-8715-208ddexample`\"}]`
```

Where:

- `arn:aws:s3:::amzn-s3-demo-bucket3` is the ARN of the S3
  bucket.
- `ADDRESS` is the unique identifier for the managed data
  identifier that detected a type of sensitive data to exclude (mailing
  addresses).
- `3293a69d-4a1e-4a07-8715-208ddexample` is the unique
  identifier for the custom data identifier that detected a type of sensitive data to
  exclude.

This next set of examples later includes all types of sensitive data in the
sensitivity score for the S3 bucket. It overwrites the current exclusion settings for the
bucket by specifying an empty (null) value for the `suppress-data-identifiers`
parameter. For Linux, macOS, or Unix:

```
`$` `aws macie2 update-resource-profile-detections --resource-arn `arn:aws:s3:::amzn-s3-demo-bucket3` --suppress-data-identifiers '[]'`
```

For Microsoft Windows:

```
`C:\>` `aws macie2 update-resource-profile-detections --resource-arn `arn:aws:s3:::amzn-s3-demo-bucket3` --suppress-data-identifiers=[]`
```

Where `arn:aws:s3:::amzn-s3-demo-bucket3` is the ARN of the S3
bucket.
