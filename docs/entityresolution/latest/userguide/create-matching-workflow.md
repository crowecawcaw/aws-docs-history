# Match input data using a matching workflow

A _matching workflow_ is a data processing job that
combines and compares data from different input sources and determines which of it matches based
on different matching techniques. It produces a data output table.

When you create a matching workflow, you first specify your data inputs, normalization
steps, and then choose your desired matching techniques and data output. AWS Entity Resolution reads your
data from your specified location or locations and finds a match between two or more records in
your data. It then assigns a [Match
ID](glossary.md#match-id-defin "glossary.md#match-id-defin") to the records in the matched set of data. AWS Entity Resolution then writes data output files to a
location that you choose. You can use AWS Entity Resolution to hash output data if desired – helping
you maintain control over your data.

A matching workflow can have multiple runs and the results (successes or errors) are written
to a folder with the `jobId` as the name.

The data output contains both a file for successful matches and a file for errors. The data
output can contain multiple fields. The successful results are written to a `success`
folder that contains multiple files, and each file contains a subset of the successful records.
Similarly, errors are written to an `error` folder with multiple fields, with each
containing a subset of the error records. For more information about troubleshooting errors, see
[Troubleshooting matching workflows](troubleshooting.md "troubleshooting.md").

The following diagram summarizes how to create a matching workflow.

![A summary of the four steps to create a matching workflow in AWS Entity Resolution](images/HIW-Matching-Workflow.png)

Before you create a matching workflow, you must first create a schema mapping. For more
information, see [Creating a schema mapping](create-schema-mapping.md "create-schema-mapping.md").

There are three ways to create a matching workflow, based on matching techniques: [rule-based](creating-matching-workflow-rule-based.md "creating-matching-workflow-rule-based.md"), [machine
learning-based](create-matching-workflow-ml.md "create-matching-workflow-ml.md"), or [provider service-based](create-matching-workflow-provider.md "create-matching-workflow-provider.md").

After you create and run a matching workflow, you can do the following:

- View the results in the S3 location you specified. Matching workflows generate IDs after
  the data is indexed.
- Use the output of [rule-based matching](creating-matching-workflow-rule-based.md "creating-matching-workflow-rule-based.md") or [machine
  learning (ML) matching](create-matching-workflow-ml.md "create-matching-workflow-ml.md") as an input to [provider service-based matching](create-matching-workflow-provider.md "create-matching-workflow-provider.md")
  or the other way around to meet your business needs.
  For example, to save provider subscription costs, you can first run [rule-based matching](creating-matching-workflow-rule-based.md "creating-matching-workflow-rule-based.md") to find
  matches on your data. Then, you can send a subset of unmatched records to [provider service-based matching](create-matching-workflow-provider.md "create-matching-workflow-provider.md").

###### Topics

- [Creating a rule-based matching
  workflow](creating-matching-workflow-rule-based.md "creating-matching-workflow-rule-based.md")
- [Creating a machine learning-based matching
  workflow](create-matching-workflow-ml.md "create-matching-workflow-ml.md")
- [Creating a provider service-based matching
  workflow](create-matching-workflow-provider.md "create-matching-workflow-provider.md")
- [Editing a matching workflow](edit-matching-workflow.md "edit-matching-workflow.md")
- [Deleting a matching workflow](delete-matching-workflow.md "delete-matching-workflow.md")
- [Modifying or generating a Match ID for a rule-based
  matching workflow](generate-match-id.md "generate-match-id.md")
- [Looking up a Match ID for a rule-based matching
  workflow](find-match-id.md "find-match-id.md")
- [Deleting records from a rule-based or ML-based matching
  workflow](delete-records.md "delete-records.md")
- [Troubleshooting matching workflows](troubleshooting.md "troubleshooting.md")
