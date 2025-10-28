# Configuring settings for automated sensitive data discovery

If you enable automated sensitive data discovery for your account or organization, you can adjust your automated discovery
settings to refine the analyses that Amazon Macie performs. The settings specify Amazon Simple Storage Service (Amazon S3)
buckets to exclude from analyses. They also specify the types and occurrences of sensitive data
to detect and report—the managed data identifiers, custom data identifiers, and allow
lists to use when analyzing S3 objects.

By default, Macie performs automated sensitive data discovery for all the S3 general purpose buckets for your
account. If you're the Macie administrator for an organization, this includes buckets that your member
accounts own. You can exclude specific buckets from the analyses. For example, you might exclude
buckets that typically store AWS logging data, such as AWS CloudTrail event logs. If you exclude a
bucket, you can include it again later.

In addition, Macie analyzes S3 objects by using only the set of managed data identifiers
that we recommend for automated sensitive data discovery. Macie doesn't use custom data identifiers or allow lists that
you defined. To customize the analyses, you can add or remove specific managed data identifiers,
custom data identifiers, and allow lists.

If you change a setting, Macie applies your change when the next evaluation and analysis
cycle starts, typically within 24 hours. In addition, your change applies only to the current
AWS Region. To make the same change in additional Regions, repeat the applicable steps in each
additional Region.

###### Topics

- [Configuration options for
  organizations](#discovery-asdd-configure-options-orgs "#discovery-asdd-configure-options-orgs")
- [Excluding or including
  S3 buckets](#discovery-asdd-account-configure-s3buckets "#discovery-asdd-account-configure-s3buckets")
- [Adding or removing managed
  data identifiers](#discovery-asdd-account-configure-mdis "#discovery-asdd-account-configure-mdis")
- [Adding or removing custom
  data identifiers](#discovery-asdd-account-configure-cdis "#discovery-asdd-account-configure-cdis")
- [Adding or removing allow
  lists](#discovery-asdd-account-configure-als "#discovery-asdd-account-configure-als")

###### Note

To configure settings for automated sensitive data discovery, you must be the Macie administrator for an organization or
have a standalone Macie account. If your account is part of an organization, only the
Macie administrator for your organization can configure and manage the settings for accounts in your
organization. If you have a member account, contact your Macie administrator to learn about the settings
for your account and organization.

## Configuration options for organizations

If an account is part of an organization that centrally manages multiple Amazon Macie
accounts, the Macie administrator for the organization configures and manages automated sensitive data discovery for accounts in
the organization. This includes settings that define the scope and nature of the analyses that
Macie performs for the accounts. Members can't access these settings for their own
accounts.

If you're the Macie administrator for an organization, you can define the scope of the analyses in
several ways:

- Automatically enable automated sensitive data discovery for accounts – When
  you enable automated sensitive data discovery, you specify whether to enable it for all existing accounts and new
  member accounts, only for new member accounts, or no member accounts. If you enable it for new
  member accounts, it's enabled automatically for any account that subsequently joins your
  organization, when the account joins your organization in Macie. If it's enabled for an
  account, Macie includes S3 buckets that the account owns. If it's disabled for an account,
  Macie excludes buckets that the account owns.
- Selectively enable automated sensitive data discovery for accounts – With
  this option, you enable or disable automated sensitive data discovery for individual accounts on a case-by-case basis.
  If you enable it for an account, Macie includes S3 buckets that the account owns. If you don't
  enable it or you disable it for an account, Macie excludes buckets that the account
  owns.
- Exclude specific S3 buckets from automated sensitive data discovery – If
  you enable automated sensitive data discovery for an account, you can exclude particular S3 buckets that the account
  owns. Macie then skips the buckets when it performs automated discovery. To exclude particular buckets, add
  them to the exclusion list in the configuration settings for your administrator account. You
  can exclude as many as 1,000 buckets for your organization.

By default, automated sensitive data discovery is enabled automatically for all new and existing accounts in an
organization. In addition, Macie includes all the S3 buckets that the accounts own. If you keep
the default settings, this means that Macie performs automated discovery for all the buckets for your
administrator account, which includes all the buckets that your member accounts own.

As a Macie administrator, you also define the nature of the analyses that Macie performs for your
organization. You do this by configuring additional settings for your administrator
account—the managed data identifiers, custom data identifiers, and allows lists that you
want Macie to use when it analyzes S3 objects. Macie uses the settings for your administrator
account when it analyzes S3 objects for other accounts in your organization.

## Excluding or including S3 buckets

in automated sensitive data discovery

By default, Amazon Macie performs automated sensitive data discovery for all the S3 general purpose buckets for your
account. If you're the Macie administrator for an organization, this includes buckets that your member
accounts own.

To refine the scope, you can exclude as many as 1,000 S3 buckets from analyses. If you
exclude a bucket, Macie stops selecting and analyzing objects in the bucket when it performs
automated sensitive data discovery. Existing sensitive data discovery statistics and details for the bucket persist. For example, the bucket's
current sensitivity score remains unchanged. After you exclude a bucket, you can include it again
later.

###### To exclude or include an S3 bucket in automated sensitive data discovery

You can exclude or subsequently include an S3 bucket by using the Amazon Macie console or the
Amazon Macie API.

Console
Follow these steps to exclude or subsequently include an S3 bucket by using the
Amazon Macie console.

###### To exclude or include an S3 bucket

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to exclude or include specific S3 buckets in
   analyses.
3. In the navigation pane, under **Settings**, choose
   **Automated sensitive data discovery**.

The **Automated sensitive data discovery** page appears and displays
your current settings. On that page, the **S3 buckets** section lists S3
buckets that are currently excluded, or it indicates that all buckets are currently
included. 4. In the **S3 buckets** section, choose
**Edit**. 5. Do one of the following:

    * To exclude one or more S3 buckets, choose **Add buckets to the exclude
     list**. Then, in the **S3 buckets** table, select the checkbox
     for each bucket to exclude. The table lists all the general purpose buckets for your
     account or organization in the current Region.
    * To include one or more S3 buckets that you previously excluded, choose
     **Remove buckets from the exclude list**. Then, in the **S3
     buckets** table, select the checkbox for each bucket to include. The table
     lists all the buckets that are currently excluded from analyses.

To find specific buckets more easily, enter search criteria in the search box above
the table. You can also sort the table by choosing a column heading. 6. When you finish selecting buckets, choose **Add** or
**Remove**, depending on the option that you chose in the preceding
step.

###### Tip

You can also exclude or include individual S3 buckets on a case-by-case basis while you
review bucket details on the console. To do this, choose the bucket on the **S3
buckets** page. Then, in the details panel, change the **Exclude from
automated discovery** setting for the bucket.

API
To exclude or subsequently include an S3 bucket programmatically, use the Amazon Macie API
to update the classification scope for your account. The classification scope specifies
buckets that you don't want Macie to analyze when it performs automated sensitive data discovery. It defines a bucket
exclusion list for automated discovery.

When you update the classification scope, you specify whether to add or remove
individual buckets from the exclusion list, or overwrite the current list with a new list.
Therefore, it's a good idea to start by retrieving and reviewing your current list. To
retrieve the list, use the [GetClassificationScope](../APIReference/classification-scopes-id.md "../APIReference/classification-scopes-id.md")
operation. If you're using the AWS Command Line Interface (AWS CLI), run the [get-classification-scope](../../../cli/latest/reference/macie2/get-classification-scope.md "../../../cli/latest/reference/macie2/get-classification-scope.md") command to retrieve the list.

To retrieve or update the classification scope, you have to specify its unique
identifier (`id`). You can get this identifier by using the [GetAutomatedDiscoveryConfiguration](../APIReference/automated-discovery-configuration.md "../APIReference/automated-discovery-configuration.md") operation. This operation retrieves your current
configuration settings for automated sensitive data discovery, including the unique identifier for the classification
scope for your account in the current AWS Region. If you're using the AWS CLI, run the [get-automated-discovery-configuration](../../../cli/latest/reference/macie2/get-automated-discovery-configuration.md "../../../cli/latest/reference/macie2/get-automated-discovery-configuration.md") command to retrieve this information.

When you're ready to update the classification scope, use the [UpdateClassificationScope](../APIReference/classification-scopes-id.md "../APIReference/classification-scopes-id.md") operation or, if you're using the AWS CLI, run the [update-classification-scope](../../../cli/latest/reference/macie2/update-classification-scope.md "../../../cli/latest/reference/macie2/update-classification-scope.md") command. In your request, use the supported parameters
to exclude or include an S3 bucket in subsequent analyses:

- To exclude one or more buckets, specify the name of each bucket for the
  `bucketNames` parameter. For the `operation` parameter, specify
  `ADD`.
- To include one or more buckets that you previously excluded, specify the name of each
  bucket for the `bucketNames` parameter. For the `operation`
  parameter, specify `REMOVE`.
- To overwrite the current list with a new list of buckets to exclude, specify
  `REPLACE` for the `operation` parameter. For the
  `bucketNames` parameter, specify the name of each bucket to exclude.

Each value for the `bucketNames` parameter must be the full name of an
existing general purpose bucket in the current Region. Values are case sensitive. If your
request succeeds, Macie updates the classification scope and returns an empty
response.

The following examples show how to use the AWS CLI to update the classification scope for
an account. The first set of examples excludes two S3 buckets
(`amzn-s3-demo-bucket1` and
`amzn-s3-demo-bucket2`) from subsequent analyses. It adds the
buckets to the list of buckets to exclude.

This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 update-classification-scope \
--id 117aff7ed76b59a59c3224ebdexample \
--s3 '{"excludes":{"bucketNames":["`amzn-s3-demo-bucket1`","`amzn-s3-demo-bucket2`"],"operation": "ADD"}}'`
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 update-classification-scope ^
--id 117aff7ed76b59a59c3224ebdexample ^
--s3={\"excludes\":{\"bucketNames\":[\"`amzn-s3-demo-bucket1`\",\"`amzn-s3-demo-bucket2`\"],\"operation\":\"ADD\"}}`
```

The next set of examples later includes the buckets
(`amzn-s3-demo-bucket1` and
`amzn-s3-demo-bucket2`) in subsequent analyses. It removes the
buckets from the list of buckets to exclude. For Linux, macOS, or Unix:

```
`$` `aws macie2 update-classification-scope \
--id 117aff7ed76b59a59c3224ebdexample \
--s3 '{"excludes":{"bucketNames":["`amzn-s3-demo-bucket1`","`amzn-s3-demo-bucket2`"],"operation": "REMOVE"}}'`
```

For Microsoft Windows:

```
`C:\>` `aws macie2 update-classification-scope ^
--id 117aff7ed76b59a59c3224ebdexample ^
--s3={\"excludes\":{\"bucketNames\":[\"`amzn-s3-demo-bucket1`\",\"`amzn-s3-demo-bucket2`\"],\"operation\":\"REMOVE\"}}`
```

The following examples overwrite and replace the current list with a new list of S3
buckets to exclude. The new list specifies three buckets to exclude:
`amzn-s3-demo-bucket`,
`amzn-s3-demo-bucket2`, and
`amzn-s3-demo-bucket3`. For Linux, macOS, or Unix:

```
`$` `aws macie2 update-classification-scope \
--id 117aff7ed76b59a59c3224ebdexample \
--s3 '{"excludes":{"bucketNames":["`amzn-s3-demo-bucket`","`amzn-s3-demo-bucket2`","`amzn-s3-demo-bucket3`"],"operation": "REPLACE"}}'`
```

For Microsoft Windows:

```
`C:\>` `aws macie2 update-classification-scope ^
--id 117aff7ed76b59a59c3224ebdexample ^
--s3={\"excludes\":{\"bucketNames\":[\"`amzn-s3-demo-bucket`\",\"`amzn-s3-demo-bucket2`\",\"`amzn-s3-demo-bucket3`\"],\"operation\":\"REPLACE\"}}`
```

## Adding or removing managed data

identifiers from automated sensitive data discovery

A _managed data identifier_ is a set of built-in criteria
and techniques that are designed to detect a specific type of sensitive data—for example,
credit card numbers, AWS secret access keys, or passport numbers for a particular country or
region. By default, Amazon Macie analyzes S3 objects by using the set of managed data identifiers
that we recommend for automated sensitive data discovery. To review a list of these identifiers, see [Default settings for automated sensitive data discovery](discovery-asdd-settings-defaults.md "discovery-asdd-settings-defaults.md").

You can tailor the analyses to focus on specific types of sensitive data:

- Add managed data identifiers for the types of sensitive data that you want Macie to
  detect and report, and
- Remove managed data identifiers for the types of sensitive data that you don't want Macie
  to detect and report.

For a complete list of all the managed data identifiers that Macie currently provides and
details for each one, see [Using managed data
identifiers](managed-data-identifiers.md "managed-data-identifiers.md").

If you remove a managed data identifier, your change doesn't affect existing sensitive data discovery statistics
and details for S3 buckets. For example, if you remove the managed data identifier for AWS
secret access keys and Macie previously detected that data in a bucket, Macie continues to
report those detections. However, instead of removing the identifier, which affects subsequent
analyses of all buckets, consider excluding its detections from sensitivity scores for only
particular buckets. For more information, see [Adjusting sensitivity scores for S3
buckets](discovery-asdd-s3bucket-manage.md "discovery-asdd-s3bucket-manage.md").

###### To add or remove managed data identifiers from automated sensitive data discovery

You can add or remove managed data identifiers by using the Amazon Macie console or the
Amazon Macie API.

Console
Follow these steps to add or remove a managed data identifier by using the Amazon Macie
console.

###### To add or remove a managed data identifier

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to add or remove a managed data identifier from
   analyses.
3. In the navigation pane, under **Settings**, choose
   **Automated sensitive data discovery**.

The **Automated sensitive data discovery** page appears and displays
your current settings. On that page, the **Managed data identifiers**
section displays your current settings, organized into two tabs:

    * **Added to default** – This tab lists managed data
     identifiers that you added. Macie uses these identifiers in addition to the ones that are
     in the default set and you haven't removed.
    * **Removed from default** – This tab lists managed data
     identifiers that you removed. Macie doesn't use these identifiers.

4.  In the **Managed data identifiers** section, choose
    **Edit**.
5.  Do any of the following:

        * To add one or more managed data identifiers, choose the **Added to
         default** tab. Then, in the table, select the checkbox for each managed data
         identifier to add. If a checkbox is already selected, you already added that
         identifier.
        * To remove one or more managed data identifiers, choose the **Removed from
         default** tab. Then, in the table, select the checkbox for each managed data
         identifier to remove. If a checkbox is already selected, you already removed that
         identifier.

    On each tab, the table displays a list of all the managed data identifiers that Macie
    currently provides. In the table, the first column specifies each managed data identifier's
    ID. The ID describes the type of sensitive data that an identifier is designed to
    detect—for example, **USA_PASSPORT_NUMBER** for US passport
    numbers. To find specific managed data identifiers more easily, enter search criteria in
    the search box above the table. You can also sort the table by choosing a column
    heading.

6.  When you finish, choose **Save**.

API
To add or remove a managed data identifier programmatically, use the Amazon Macie API to
update the sensitivity inspection template for your account. The template stores settings
that specify which managed data identifiers to use (_include_) in addition to the ones in the default set. They also specify managed
data identifiers to not use (_exclude_). The settings also
specify any custom data identifiers and allow lists that you want Macie to use.

When you update the template, you overwrite its current settings. Therefore, it's a good
idea to start by retrieving your current settings and determining which ones you want to
keep. To retrieve your current settings, use the [GetSensitivityInspectionTemplate](../APIReference/templates-sensitivity-inspections-id.md "../APIReference/templates-sensitivity-inspections-id.md") operation. If you're using the AWS Command Line Interface (AWS CLI),
run the [get-sensitivity-inspection-template](../../../cli/latest/reference/macie2/get-sensitivity-inspection-template.md "../../../cli/latest/reference/macie2/get-sensitivity-inspection-template.md") command to retrieve the settings.

To retrieve or update the template, you have to specify its unique identifier
(`id`). You can get this identifier by using the [GetAutomatedDiscoveryConfiguration](../APIReference/automated-discovery-configuration.md "../APIReference/automated-discovery-configuration.md") operation. This operation retrieves your current
configuration settings for automated sensitive data discovery, including the unique identifier for the sensitivity
inspection template for your account in the current AWS Region. If you're using the AWS CLI,
run the [get-automated-discovery-configuration](../../../cli/latest/reference/macie2/get-automated-discovery-configuration.md "../../../cli/latest/reference/macie2/get-automated-discovery-configuration.md") command to retrieve this information.

When you're ready to update the template, use the [UpdateSensitivityInspectionTemplate](../APIReference/templates-sensitivity-inspections-id.md "../APIReference/templates-sensitivity-inspections-id.md") operation or, if you're using the AWS CLI, run
the [update-sensitivity-inspection-template](../../../cli/latest/reference/macie2/update-sensitivity-inspection-template.md "../../../cli/latest/reference/macie2/update-sensitivity-inspection-template.md") command. In your request, use the
appropriate parameters to add or remove one or more managed data identifiers from subsequent
analyses:

- To start using a managed data identifier, specify its ID for the
  `managedDataIdentifierIds` parameter of the `includes`
  parameter.
- To stop using a managed data identifier, specify its ID for the
  `managedDataIdentifierIds` parameter of the `excludes`
  parameter.
- To restore the default settings, don't specify any IDs for the `includes`
  and `excludes` parameters. Macie then starts using only the managed data
  identifiers that are in the default set.

In addition to the parameters for managed data identifiers, use the appropriate
`includes` parameters to specify any custom data identifiers
(`customDataIdentifierIds`) and allow lists (`allowListIds`) that you
want Macie to use. Also specify the Region that your request applies to. If your request
succeeds, Macie updates the template and returns an empty response.

The following examples show how to use the AWS CLI to update the sensitivity inspection
template for an account. The examples add one managed data identifier and remove another from
subsequent analyses. They also maintain current settings that specify two custom data
identifiers to use.

This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 update-sensitivity-inspection-template \
--id `fd7b6d71c8006fcd6391e6eedexample` \
--excludes '{"managedDataIdentifierIds":["`UK_ELECTORAL_ROLL_NUMBER`"]}' \
--includes '{"managedDataIdentifierIds":["`STRIPE_CREDENTIALS`"],"customDataIdentifierIds":["`3293a69d-4a1e-4a07-8715-208ddexample`","`6fad0fb5-3e82-4270-bede-469f2example`"]}'`
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 update-sensitivity-inspection-template ^
--id `fd7b6d71c8006fcd6391e6eedexample` ^
--excludes={\"managedDataIdentifierIds\":[\"`UK_ELECTORAL_ROLL_NUMBER`\"]} ^
--includes={\"managedDataIdentifierIds\":[\"`STRIPE_CREDENTIALS`\"],\"customDataIdentifierIds\":[\"`3293a69d-4a1e-4a07-8715-208ddexample`\",\"`6fad0fb5-3e82-4270-bede-469f2example`\"]}`
```

Where:

- `fd7b6d71c8006fcd6391e6eedexample` is the unique identifier
  for the sensitivity inspection template to update.
- `UK_ELECTORAL_ROLL_NUMBER` is the ID for the managed data
  identifier to stop using (_exclude_).
- `STRIPE_CREDENTIALS` is the ID for the managed data
  identifier to start using (_include_).
- `3293a69d-4a1e-4a07-8715-208ddexample` and
  `6fad0fb5-3e82-4270-bede-469f2example` are the unique identifiers
  for the custom data identifiers to use.

## Adding or removing custom data

identifiers from automated sensitive data discovery

A _custom data identifier_ is a set of criteria that you define to
detect sensitive data. The criteria consist of a regular expression (_regex_) that defines a text pattern to match and, optionally, character sequences
and a proximity rule that refine the results. To learn more, see [Building custom data
identifiers](custom-data-identifiers.md "custom-data-identifiers.md").

By default, Amazon Macie doesn't use custom data identifiers when it performs automated sensitive data discovery. If
you want Macie to use specific custom data identifiers, you can add them to subsequent analyses.
Macie then uses the custom data identifiers in addition to any managed data identifiers that you
configure Macie to use.

If you add a custom data identifier, you can later remove it. Your change doesn't affect
existing sensitive data discovery statistics and details for S3 buckets. That is to say, if you remove a custom data
identifier that previously produced detections for a bucket, Macie continues to report those
detections. However, instead of removing the identifier, which affects subsequent analyses of
all buckets, consider excluding its detections from sensitivity scores for only particular
buckets. For more information, see [Adjusting sensitivity scores for S3
buckets](discovery-asdd-s3bucket-manage.md "discovery-asdd-s3bucket-manage.md").

###### To add or remove custom data identifiers from automated sensitive data discovery

You can add or remove custom data identifiers by using the Amazon Macie console or the
Amazon Macie API.

Console
Follow these steps to add or remove a custom data identifier by using the Amazon Macie
console.

###### To add or remove a custom data identifier

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to add or remove a custom data identifier from
   analyses.
3. In the navigation pane, under **Settings**, choose
   **Automated sensitive data discovery**.

The **Automated sensitive data discovery** page appears and displays
your current settings. On that page, the **Custom data identifiers**
section lists custom data identifiers that you already added, or it indicates that you
haven't added any custom data identifiers. 4. In the **Custom data identifiers** section, choose
**Edit**. 5. Do any of the following:

    * To add one or more custom data identifiers, select the checkbox for each custom data
     identifier to add. If a checkbox is already selected, you already added that
     identifier.
    * To remove one or more custom data identifiers, clear the checkbox for each custom
     data identifier to remove. If a checkbox is already cleared, Macie doesn't currently use
     that identifier.

###### Tip

To review or test the settings for a custom data identifier before you add or remove
it, choose the link icon (
![The link icon, which is a blue box that has an arrow in it.](images/icon-external-link.png)
) next to the identifier's name. Macie opens
a page that displays the identifier's settings. To also test the identifier with sample
data, enter up to 1,000 characters of text in the **Sample data** box on
that page. Then choose **Test**. Macie evaluates the sample data and
reports the number of matches. 6. When you finish, choose **Save**.

API
To add or remove a custom data identifier programmatically, use the Amazon Macie API to
update the sensitivity inspection template for your account. The template stores settings
that specify which custom data identifiers you want Macie to use when performing automated sensitive data discovery.
The settings also specify which managed data identifiers and allow lists to use.

When you update the template, you overwrite its current settings.
Therefore, it's a good idea to start by retrieving your current settings and determining
which ones you want to keep. To retrieve your current settings, use the [GetSensitivityInspectionTemplate](../APIReference/templates-sensitivity-inspections-id.md "../APIReference/templates-sensitivity-inspections-id.md") operation. If you're using the AWS Command Line Interface (AWS CLI),
run the [get-sensitivity-inspection-template](../../../cli/latest/reference/macie2/get-sensitivity-inspection-template.md "../../../cli/latest/reference/macie2/get-sensitivity-inspection-template.md") command to retrieve the settings.

To retrieve or update the template, you have to specify its unique identifier
(`id`). You can get this identifier by using the [GetAutomatedDiscoveryConfiguration](../APIReference/automated-discovery-configuration.md "../APIReference/automated-discovery-configuration.md") operation. This operation retrieves your current
configuration settings for automated sensitive data discovery, including the unique identifier for the sensitivity
inspection template for your account in the current AWS Region. If you're using the AWS CLI,
run the [get-automated-discovery-configuration](../../../cli/latest/reference/macie2/get-automated-discovery-configuration.md "../../../cli/latest/reference/macie2/get-automated-discovery-configuration.md") command to retrieve this information.

When you're ready to update the template, use the [UpdateSensitivityInspectionTemplate](../APIReference/templates-sensitivity-inspections-id.md "../APIReference/templates-sensitivity-inspections-id.md") operation or, if you're using the AWS CLI, run
the [update-sensitivity-inspection-template](../../../cli/latest/reference/macie2/update-sensitivity-inspection-template.md "../../../cli/latest/reference/macie2/update-sensitivity-inspection-template.md") command. In your request, use the
`customDataIdentifierIds` parameter to add or remove one or more custom data
identifiers from subsequent analyses:

- To start using a custom data identifier, specify its unique identifier for the
  parameter.
- To stop using a custom data identifier, omit its unique identifier from the
  parameter.

Use additional parameters to specify which managed data identifiers and allow lists you
want Macie to use. Also specify the Region that your request applies to. If your request
succeeds, Macie updates the template and returns an empty response.

The following examples show how to use the AWS CLI to update the sensitivity inspection
template for an account. The examples add two custom data identifiers to subsequent analyses.
They also maintain current settings that specify which managed data identifiers and allow
lists to use: use the default set of managed data identifiers and one allow list.

This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 update-sensitivity-inspection-template \
--id `fd7b6d71c8006fcd6391e6eedexample` \
--includes '{"allowListIds":["`nkr81bmtu2542yyexample`"],"customDataIdentifierIds":["`3293a69d-4a1e-4a07-8715-208ddexample`","`6fad0fb5-3e82-4270-bede-469f2example`"]}'`
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 update-sensitivity-inspection-template ^
--id `fd7b6d71c8006fcd6391e6eedexample` ^
--includes={\"allowListIds\":[\"`nkr81bmtu2542yyexample`\"],\"customDataIdentifierIds\":[\"`3293a69d-4a1e-4a07-8715-208ddexample`\",\"`6fad0fb5-3e82-4270-bede-469f2example`\"]}`
```

Where:

- `fd7b6d71c8006fcd6391e6eedexample` is the unique identifier
  for the sensitivity inspection template to update.
- `nkr81bmtu2542yyexample` is the unique identifier for the
  allow list to use.
- `3293a69d-4a1e-4a07-8715-208ddexample` and
  `6fad0fb5-3e82-4270-bede-469f2example` are the unique identifiers
  for the custom data identifiers to use.

## Adding or removing allow lists from

automated sensitive data discovery

In Amazon Macie, an allow list defines specific text or a text pattern that you want Macie to
ignore when it inspects S3 objects for sensitive data. If text matches an entry or pattern in an
allow list, Macie doesn’t report the text. This is the case even if the text matches the
criteria of a managed or custom data identifier. To learn more, see [Defining sensitive data exceptions with allow
lists](allow-lists.md "allow-lists.md").

By default, Macie doesn't use allow lists when it performs automated sensitive data discovery. If you want Macie to
use specific allow lists, you can add them to subsequent analyses. If you add an allow list, you
can later remove it.

###### To add or remove allow lists from automated sensitive data discovery

You can add or remove allow lists by using the Amazon Macie console or the Amazon Macie
API.

Console
Follow these steps to add or remove an allow list by using the Amazon Macie console.

###### To add or remove an allow list

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to add or remove an allow list from analyses.
3. In the navigation pane, under **Settings**, choose **Automated
   sensitive data discovery**.

The **Automated sensitive data discovery** page appears and displays
your current settings. On that page, the **Allow lists** section specifies
allow lists that you already added, or it indicates that you haven't added any allow
lists. 4. In the **Allow lists** section, choose **Edit**. 5. Do any of the following:

    * To add one or more allow lists, select the checkbox for each allow list to add. If a
     checkbox is already selected, you already added that list.
    * To remove one or more allow lists, clear the checkbox for each allow list to remove. If
     a checkbox is already cleared, Macie doesn't currently use that list.

###### Tip

To review the settings for an allow list before you add or remove it, choose the link
icon (
![The link icon, which is a blue box that has an arrow in it.](images/icon-external-link.png)
) next to the list's name. Macie opens a page that displays the
list's settings. If the list specifies a regular expression (_regex_), you can also use this page to test the regex with sample data. To do
this, enter up to 1,000 characters of text in the **Sample data** box, and
then choose **Test**. Macie evaluates the sample data and reports the number
of matches. 6. When you finish, choose **Save**.

API
To add or remove an allow list programmatically, use the Amazon Macie API to update the
sensitivity inspection template for your account. The template stores settings that specify
which allow lists you want Macie to use when performing automated sensitive data discovery. The settings also specify
which managed data identifiers and custom data identifiers to use.

When you update the template, you overwrite its current settings. Therefore, it's a good
idea to start by retrieving your current settings and determining which ones you want to
keep. To retrieve your current settings, use the [GetSensitivityInspectionTemplate](../APIReference/templates-sensitivity-inspections-id.md "../APIReference/templates-sensitivity-inspections-id.md") operation. If you're using the AWS Command Line Interface (AWS CLI),
run the [get-sensitivity-inspection-template](../../../cli/latest/reference/macie2/get-sensitivity-inspection-template.md "../../../cli/latest/reference/macie2/get-sensitivity-inspection-template.md") command to retrieve the settings.

To retrieve or update the template, you have to specify its unique identifier
(`id`). You can get this identifier by using the [GetAutomatedDiscoveryConfiguration](../APIReference/automated-discovery-configuration.md "../APIReference/automated-discovery-configuration.md") operation. This operation retrieves your current
configuration settings for automated sensitive data discovery, including the unique identifier for the sensitivity
inspection template for your account in the current AWS Region. If you're using the AWS CLI,
run the [get-automated-discovery-configuration](../../../cli/latest/reference/macie2/get-automated-discovery-configuration.md "../../../cli/latest/reference/macie2/get-automated-discovery-configuration.md") command to retrieve this information.

When you're ready to update the template, use the [UpdateSensitivityInspectionTemplate](../APIReference/templates-sensitivity-inspections-id.md "../APIReference/templates-sensitivity-inspections-id.md") operation or, if you're using the AWS CLI, run
the [update-sensitivity-inspection-template](../../../cli/latest/reference/macie2/update-sensitivity-inspection-template.md "../../../cli/latest/reference/macie2/update-sensitivity-inspection-template.md") command. In your request, use the
`allowListIds` parameter to add or remove one or more allow lists from subsequent
analyses:

- To start using an allow list, specify its unique identifier for the parameter.
- To stop using an allow list, omit its unique identifier from the parameter.

Use additional parameters to specify which managed data identifiers and custom data
identifiers you want Macie to use. Also specify the Region that your request applies to. If
your request succeeds, Macie updates the template and returns an empty response.

The following examples show how to use the AWS CLI to update the sensitivity inspection
template for an account. The examples add an allow list to subsequent analyses. They also
maintain current settings that specify which managed data identifiers and custom data
identifiers to use: use the default set of managed data identifiers and two custom data
identifiers.

This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 update-sensitivity-inspection-template \
--id `fd7b6d71c8006fcd6391e6eedexample` \
--includes '{"allowListIds":["`nkr81bmtu2542yyexample`"],"customDataIdentifierIds":["`3293a69d-4a1e-4a07-8715-208ddexample`","`6fad0fb5-3e82-4270-bede-469f2example`"]}'`
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 update-sensitivity-inspection-template ^
--id `fd7b6d71c8006fcd6391e6eedexample` ^
--includes={\"allowListIds\":[\"`nkr81bmtu2542yyexample`\"],\"customDataIdentifierIds\":[\"`3293a69d-4a1e-4a07-8715-208ddexample`\",\"`6fad0fb5-3e82-4270-bede-469f2example`\"]}`
```

Where:

- `fd7b6d71c8006fcd6391e6eedexample` is the unique identifier
  for the sensitivity inspection template to update.
- `nkr81bmtu2542yyexample` is the unique identifier for the
  allow list to use.
- `3293a69d-4a1e-4a07-8715-208ddexample` and
  `6fad0fb5-3e82-4270-bede-469f2example` are the unique identifiers
  for the custom data identifiers to use.
