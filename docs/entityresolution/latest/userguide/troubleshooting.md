# Troubleshooting matching workflows

Use the following information to help you diagnose and fix common issues that you might
encounter when running matching workflows.

## I received an error file after running a matching

workflow

### Common cause

A matching workflow can have multiple runs and the results (successes or errors) are written
to a folder with the `jobId` as the name.

The successful results for a matching workflow are written to a `success` folder
that contains multiple files, and each file contains a subset of the successful records.

The errors for a matching workflow are written to an `error` folder with
multiple fields, with each containing a subset of the error records.

The error file can be created for the following reasons:

- The [Unique ID](glossary.md#unique-id-defn "glossary.md#unique-id-defn") is:
  - null
  - missing in a row of data
  - missing in a record in the data table
  - repeated in another row of data in the data table
  - not specified
  - not unique within the same source
  - not unique across multiple sources
  - overlaps across sources
  - exceeds 38 characters (rule-based matching workflow only)

- One of the fields in the [schema mapping](glossary.md#schema-mapping-definition "glossary.md#schema-mapping-definition")
  includes a reserved name:
  - EmailAddress
  - InputSourceARN
  - MatchRule
  - MatchID
  - HashingProtocol
  - ConfidenceLevel
  - Source

###### Note

If the record in the error file is created due to the reasons listed previously, you are
charged, because it incurs processing cost for the service. If the record in the error file is
because of an internal server error, you aren't charged.

### Resolution

###### To resolve this issue

1. Check to see if the [Unique ID](glossary.md#unique-id-defn "glossary.md#unique-id-defn") is valid.

If the [Unique ID](glossary.md#unique-id-defn "glossary.md#unique-id-defn") isn't valid, update the Unique ID
in your data table, save the new data table, create a new schema mapping, and run the matching
workflow again. 2. Check if one of the fields in the [schema
mapping](glossary.md#schema-mapping-definition "glossary.md#schema-mapping-definition") includes a reserved name.

If one of the fields includes a reserved name, create a new schema mapping with a new
name, and run the matching workflow again.
