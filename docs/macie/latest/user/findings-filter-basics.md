# Fundamentals of filtering Macie findings

When you filter findings, keep the following features and guidelines in mind. Also note that
filtered results are limited to the preceding 90 days and the current AWS Region.
Amazon Macie stores your findings for only 90 days in each AWS Region.

###### Topics

- [Using multiple
  conditions in a filter](#findings-filter-basics-multiple-criteria "#findings-filter-basics-multiple-criteria")
- [Specifying values for
  fields](#findings-filter-basics-value-types "#findings-filter-basics-value-types")
- [Specifying multiple
  values for a field](#findings-filter-basics-multiple-values "#findings-filter-basics-multiple-values")
- [Using operators in
  conditions](#findings-filter-basics-operators "#findings-filter-basics-operators")

## Using multiple conditions in a

filter

A filter can include one or more conditions. Each condition, also referred to as a
_criterion_, consists of three parts:

- An attribute-based field, such as **Severity** or
  **Finding type**. For a list of fields that you can use, see
  [Fields for filtering Macie findings](findings-filter-fields.md "findings-filter-fields.md").
- An operator, such as _equals_ or _not equals_. For a list of operators that you can use, see
  [Using operators in conditions](#findings-filter-basics-operators "#findings-filter-basics-operators").
- One or more values. The type and number of values depends on the field and
  operator that you choose.

If a filter contains multiple conditions, Amazon Macie uses AND logic to join the conditions
and evaluate the filter criteria. This means that a finding matches the filter criteria
only if it matches _all_ the conditions in the
filter.

For example, if you add a condition to include only high-severity findings and add
another condition to include only sensitive data findings, Macie returns all high-severity,
sensitive data findings. In other words, Macie excludes all policy findings and all
medium-severity and low-severity sensitive data findings.

You can use a field only once in a filter. However, you can specify multiple values for
many fields.

For example, if a condition uses the **Severity** field to include only
high-severity findings, you can’t use the **Severity** field in another
condition to include medium-severity or low-severity findings. Instead, specify multiple
values for the existing condition, or use a different operator for the existing condition.
For example, to include all medium-severity and high-severity findings, add a
**Severity**
_equals_
_Medium, High_ condition or add a
**Severity**
_not equals_
_Low_ condition.

## Specifying values for fields

When you specify a value for a field, the value has to conform to the underlying data
type for the field. Depending on the field, you can specify one of the following types of
values.

Array of text (strings)

Specifies a list of text (string) values for a field. Each string correlates to
a predefined or existing value for a field—for example, _High_ for the **Severity** field,
_SensitiveData:S3Object/Financial_ for the
**Finding type** field, or the name of an S3 bucket for the
**S3 bucket name** field.

If you use an array, note the following:

- Values are case sensitive.
- You can’t specify partial values or use wildcard characters in values.
  You have to specify a complete, valid value for the field.

For example, to filter findings for an S3 bucket named _my-S3-bucket_, enter `my-S3-bucket` as the
value for the **S3 bucket name** field. If you enter any other
value, such as `my-s3-bucket` or
`my-S3`, Macie won’t return findings for the bucket.

For a list of valid values for each field, see [Fields for filtering Macie findings](findings-filter-fields.md "findings-filter-fields.md").

You can specify as many as 50 values in an array. How you specify the values
depends on whether you use the Amazon Macie console or the Amazon Macie API, as
discussed in [Specifying multiple values for a
field](#findings-filter-basics-multiple-values "#findings-filter-basics-multiple-values").

Boolean

Specifies one of two mutually exclusive values for a field.

If you use the Amazon Macie console to specify this type of value, the console
provides a list of values to choose from. If you use the Amazon Macie API, specify
`true` or `false` for the value.

Date/Time (and time ranges)

Specifies an absolute date and time for a field. If you specify this type of
value, you have to specify both a date and time.

On the Amazon Macie console, date and time values are in your local time zone and
use 24-hour notation. In all other contexts, these values are in Coordinated
Universal Time (UTC) and extended ISO 8601 format—for example
`2020-09-01T14:31:13Z` for 2:31:13 PM UTC September 1, 2020.

If a field stores a date/time value, you can use the field to define a fixed or
relative time range. For example, you can include only those findings that were
created between two specific dates and times, or only those findings that were
created before or after a specific date and time. How you define a time range
depends on whether you use the Amazon Macie console or the Amazon Macie API:

- On the console, use a date picker or enter text directly in the
  **From** and **To** boxes.
- With the API, define a fixed time range by adding a condition that
  specifies the first date and time in the range, and add another condition
  that specifies the last date and time in the range. If you do this, Macie
  uses AND logic to join the conditions. To define a relative time range, add
  one condition that specifies the first or last date and time in the range.
  Specify the values as Unix timestamps in milliseconds—for example,
  `1604616572653` for 22:49:32 UTC November 5, 2020.

On the console, time ranges are inclusive. With the API, time ranges can be
inclusive or exclusive, depending on the operator that you choose.

Number (and numeric ranges)

Specifies a long integer for a field.

If a field stores a numeric value, you can use the field to define a fixed or
relative numeric range. For example, you can include only those findings that
report 50-90 occurrences of sensitive data in an S3 object. How you define a
numeric range depends on whether you use the Amazon Macie console or the Amazon Macie
API:

- On the console, use the **From** and
  **To** boxes to enter the lowest and highest numbers in
  the range, respectively.
- With the API, define a fixed numeric range by adding a condition that
  specifies the lowest number in the range, and add another condition that
  specifies the highest number in the range. If you do this, Macie uses AND
  logic to join the conditions. To define a relative numeric range, add one
  condition that specifies the lowest or highest number in the range.

On the console, numeric ranges are inclusive. With the API, numeric ranges can
be inclusive or exclusive, depending on the operator that you choose.

Text (string)

Specifies a single text (string) value for a field. The string correlates to a
predefined or existing value for a field—for example, _High_ for the **Severity** field, the
name of an S3 bucket for the **S3 bucket name** field, or the
unique identifier for a sensitive data discovery job for the **Job
ID** field.

If you specify a single text string, note the following:

- Values are case sensitive.
- You can’t use partial values or use wildcard characters in values. You
  have to specify a complete, valid value for the field.

For example, to filter findings for an S3 bucket named _my-S3-bucket_, enter `my-S3-bucket` as
the value for the **S3 bucket name** field. If you enter
any other value, such as `my-s3-bucket` or
`my-S3`, Macie won’t return findings for the
bucket.

For a list of valid values for each field, see [Fields for filtering Macie findings](findings-filter-fields.md "findings-filter-fields.md").

## Specifying multiple values for a

field

With certain fields and operators, you can specify multiple values for a field. If you do
this, Amazon Macie uses OR logic to join the values and evaluate the filter criteria. This
means that a finding matches the criteria if it has _any_ of the values for the field.

For example, if you add a condition to include findings where the value for the
**Finding type** field equals _SensitiveData:S3Object/Financial, SensitiveData:S3Object/Personal_, Macie
returns sensitive data findings for S3 objects that contain only financial information,
and S3 objects that contain only personal information. In other words, Macie excludes
all policy findings. Macie also excludes all sensitive data findings for objects that
contain other types of sensitive data or multiple types of sensitive data.

The exception is conditions that use the _eqExactMatch_ operator. For this operator, Macie uses AND
logic to join the values and evaluate the filter criteria. This means that a finding
matches the criteria only if it has _all_ the values
for the field and _only_ those values for the field. To
learn more about this operator, see [Using operators in conditions](#findings-filter-basics-operators "#findings-filter-basics-operators").

How you specify multiple values for a field depends on whether you use the Amazon Macie API
or the Amazon Macie console. With the API, you use an array that lists the values.

On the console, you typically choose the values from a list. However, for some fields,
you have to add a distinct condition for each value. For example, to include findings for
data that Macie detected using certain custom data identifiers, do the following:

1. Place your cursor in the **Filter criteria** box and then choose the
   **Custom data identifier name** field. Enter the name of a
   custom data identifier, and then choose **Apply**.
2. Repeat the preceding step for each additional custom data identifier that you want
   to specify for the filter.

For a list of fields that you need to do this for, see [Fields for filtering Macie findings](findings-filter-fields.md "findings-filter-fields.md").

## Using operators in conditions

You can use the following types of operators in individual conditions.

Equals (eq)

Matches (=) any value specified for the field. You can use the _equals_ operator with the following types of values:
array of text (strings), Boolean, date/time, number, and text (string).

For many fields, you can use this operator and specify as many as 50 values for the
field. If you do this, Amazon Macie uses OR logic to join the values. This
means that a finding matches the criteria if it has _any_ of the values specified for the field.

For example:

- To include findings that report occurrences of financial information,
  personal information, or both financial and personal information, add a
  condition that uses the **Sensitive data category** field
  and this operator, and specify _Financial
  information_ and _Personal
  information_ as the values for the field.
- To include findings that report occurrences of credit card numbers, mailing addresses,
  or both credit card numbers and mailing addresses, add a condition
  for the **Sensitive data detection type** field,
  use this operator, and specify _CREDIT_CARD_NUMBER_ and _ADDRESS_ as the values
  for the field.

If you use the Amazon Macie API to define a condition that uses this operator with a date/time value, specify the value as a Unix timestamp in
milliseconds—for example, `1604616572653` for 22:49:32 UTC November 5, 2020.

Equals exact match (eqExactMatch)

Exclusively matches all the values specified for the field. You can use the
_equals exact match_ operator with a select
set of fields.

If you use this operator and specify multiple values for a field, Macie uses AND logic to
join the values. This means that a finding matches the criteria only if it
has _all_ the values specified for the
field and _only_ those values for the
field. You can specify as many as 50 values for the field.

For example:

- To include findings that report occurrences of credit card numbers and no other type of
  sensitive data, add a condition for the **Sensitive data
  detection type** field, use this operator, and specify
  _CREDIT_CARD_NUMBER_ as the only value
  for the field.
- To include findings that report occurrences of both credit card numbers and mailing
  addresses (and no other types of sensitive data), add a condition
  for the **Sensitive data detection type** field,
  use this operator, and specify _CREDIT_CARD_NUMBER_ and _ADDRESS_ as the values
  for the field.

Because Macie uses AND logic to join the values for a field, you can't use this
operator in combination with any other operators for the same field. In other
words, if you use the _equals exact match_
operator with a field in one condition, you have to use it in all other conditions
that use the same field.

Like other operators, you can use the _equals exact
match_ operator in more than one condition in a filter. If you
do this, Macie uses AND logic to join the conditions and evaluate the
filter. This means that a finding matches the filter criteria only if it has
_all_ the values specified by _all_ the conditions in the filter.

For example, to include findings that were created after a certain time, report
occurrences of credit card numbers, and don't report any other type of sensitive
data, do the following:

1. Add a condition that uses the **Created at** field, uses
   the _greater than_ operator, and specifies
   the starting date and time for the filter.
2. Add another condition that uses the **Sensitive data detection type**
   field, uses the _equals exact
   match_ operator, and specifies _CREDIT_CARD_NUMBER_ as the only
   value for the field.

You can use the _equals exact match_ operator
with the following fields:

- Custom data identifier ID
  (`customDataIdentifiers.detections.arn`)
- Custom data identifier name
  (`customDataIdentifiers.detections.name`)
- S3 bucket tag key
  (`resourcesAffected.s3Bucket.tags.key`)
- S3 bucket tag value
  (`resourcesAffected.s3Bucket.tags.value`)
- S3 object tag key
  (`resourcesAffected.s3Object.tags.key`)
- S3 object tag value
  (`resourcesAffected.s3Object.tags.value`)
- Sensitive data detection type
  (`sensitiveData.detections.type`)
- Sensitive data category (`sensitiveData.category`)

In the preceding list, the parenthetical name uses dot notation to indicate the
name of the field in JSON representations of findings and the Amazon Macie
API.

Greater than (gt)

Is greater than (>) the value specified for the field. You can use the
_greater than_ operator with number and
date/time values.

For example, to include only those findings that report more than 90
occurrences of sensitive data in an S3 object, add a condition that uses the
**Sensitive data total count** field and this operator, and
specify 90 as the value for the field. To do this on the Amazon Macie console, enter
`91` in the **From** box, don't enter a
value in the **To** box, and then choose
**Apply**. Numeric and time-based comparisons are inclusive on
the console.

If you use the Amazon Macie API to define a time range that uses this operator, you have to specify the date/time values as Unix timestamps in
milliseconds—for example, `1604616572653` for 22:49:32 UTC November 5, 2020.

Greater than or equal to (gte)

Is greater than or equal to (>=) the value specified for the field.
You can use the _greater than or equal to_
operator with number and date/time values.

For example, to include only those findings that report 90 or more occurrences
of sensitive data in an S3 object, add a condition that uses the
**Sensitive data total count** field and this operator, and
specify 90 as the value for the field. To do this on the Amazon Macie console, enter
`90` in the **From** box, don't enter a
value in the **To** box, and then choose
**Apply**.

If you use the Amazon Macie API to define a time range that uses this operator, you have to specify the date/time values as Unix timestamps in
milliseconds—for example, `1604616572653` for 22:49:32 UTC November 5, 2020.

Less than (lt)

Is less than (<) the value specified for the field. You can use the
_less than_ operator with number and date/time
values.

For example, to include only those findings that report fewer than 90
occurrences of sensitive data in an S3 object, add a condition that uses the
**Sensitive data total count** field and this operator, and
specify 90 as the value for the field. To do this on the Amazon Macie console, enter
`89` in the **To** box, don't enter a
value in the **From** box, and then choose
**Apply**. Numeric and time-based comparisons are inclusive on
the console.

If you use the Amazon Macie API to define a time range that uses this operator, you have to specify the date/time values as Unix timestamps in
milliseconds—for example, `1604616572653` for 22:49:32 UTC November 5, 2020.

Less than or equal to (lte)

Is less than or equal to (<=) the value specified for the field. You
can use the _less than or equal to_ operator with
number and date/time values.

For example, to include only those findings that report 90 or fewer occurrences
of sensitive data in an S3 object, add a condition that uses the
**Sensitive data total count** field and this operator, and
specify 90 as the value for the field. To do this on the Amazon Macie console, enter
`90` in the **To** box, don't enter a
value in the **From** box, and then choose
**Apply**.

If you use the Amazon Macie API to define a time range that uses this operator, you have to specify the date/time values as Unix timestamps in
milliseconds—for example, `1604616572653` for 22:49:32 UTC November 5, 2020.

Not equals (neq)

Doesn't match (≠) any value specified for the field. You can use the
_not equals_ operator with the following types
of values: array of text (strings), Boolean, date/time, number, and text
(string).

For many fields, you can use this operator and specify as many as 50 values for the
field. If you do this, Macie uses OR logic to join the values. This means
that a finding matches the criteria if it doesn't have _any_ of the values specified for the
field.

For example:

- To exclude findings that report occurrences of financial information,
  personal information, or both financial and personal information, add a
  condition that uses the **Sensitive data category** field
  and this operator, and specify _Financial
  information_ and _Personal
  information_ as the values for the field.
- To exclude findings that report occurrences of credit card numbers, add a condition for
  the **Sensitive data detection type** field, use
  this operator, and specify _CREDIT_CARD_NUMBER_ as the value
  for the field.
- To exclude findings that report occurrences of credit card numbers, mailing addresses,
  or both credit card numbers and mailing addresses, add a condition
  for the **Sensitive data detection type** field,
  use this operator, and specify _CREDIT_CARD_NUMBER_ and _ADDRESS_ as the values
  for the field.

If you use the Amazon Macie API to define a condition that uses this operator with a date/time value, specify the value as a Unix timestamp in
milliseconds—for example, `1604616572653` for 22:49:32 UTC November 5, 2020.
