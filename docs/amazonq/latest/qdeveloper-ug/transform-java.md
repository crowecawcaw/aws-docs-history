# Transforming Java applications with Amazon Q Developer

Amazon Q supports the following types of transformations for Java applications:

- Java language and dependency version upgrades
- Embedded SQL conversion for Oracle to PostgreSQL database migration
  To get started, see the topic for the type of transformation you'd like to perform.

###### Topics

- [Quotas](#quotas-java-transformation-ide "#quotas-java-transformation-ide")
- [Upgrading Java versions with Amazon Q Developer](code-transformation.md "code-transformation.md")
- [Converting embedded SQL in Java applications with Amazon Q Developer](transform-sql.md "transform-sql.md")
- [Transforming code on the command line with Amazon Q Developer](transform-CLI.md "transform-CLI.md")
- [Viewing transformation job history](transformation-job-history.md "transformation-job-history.md")
- [Troubleshooting issues with Java transformations](troubleshooting-code-transformation.md "troubleshooting-code-transformation.md")

## Quotas

Java application transformations with Amazon Q in the IDE and command line maintain the
following quotas:

- **Lines of code per job** – The
  maximum number of code lines that Amazon Q can transform in a given transformation
  job.
- **Lines of code per month** – The
  maximum number of code lines that Amazon Q can transform in a month.
- **Concurrent jobs** – The maximum number of
  transformation jobs you can run at the same time. This quota applies to all
  transformations in the IDE, including [.NET transformations in Visual Studio](transform-dotnet-IDE.md "transform-dotnet-IDE.md").
- **Jobs per month** – The
  maximum number of transformation jobs you can run in one month.

| Resource                | Quotas                                  |
| ----------------------- | --------------------------------------- |
| Lines of code per job   | Free tier: 1000 lines of code           |
| Lines of code per month | Free tier: 2000 lines of code           |
| Concurrent jobs         | 1 job per user 25 jobs per AWS account  |
| Jobs per month          | Pro tier: 1000 jobs Free tier: 100 jobs |
