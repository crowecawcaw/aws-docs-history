# Creating database migration assessment reports with

DMS Schema Conversion

An important part of DMS Schema Conversion is the report that it generates to help you convert your
schema. This _database migration assessment report_ summarizes all of the
schema conversion tasks. It also details the action items for schema that can't be converted
to the DB engine of your target DB instance. You can view the report in the AWS DMS console or
save a copy of this report as a PDF or comma-separated value (CSV) files.

The migration assessment report includes the following:

- An executive summary
- Recommendations, including conversion of server objects, backup suggestions, and
  linked server changes
  When you have items that DMS Schema Conversion can't convert automatically, the report provides
  estimates showing how much effort is required to write the equivalent code for your target
  DB instance.

###### Topics

- [Creating a database migration assessment
  report for DMS Schema Conversion](assessment-reports.md "assessment-reports.md")
- [Viewing your database migration assessment
  report for DMS Schema Conversion](assessment-reports-view.md "assessment-reports-view.md")
- [Saving your database migration assessment
  report for DMS Schema Conversion](assessment-reports-save.md "assessment-reports-save.md")
