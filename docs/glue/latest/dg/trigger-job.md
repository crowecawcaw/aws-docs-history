# Starting jobs and crawlers using triggers

In AWS Glue, you can create Data Catalog objects called triggers, which you can use to either
manually or automatically start one or more crawlers or extract, transform, and load (ETL)
jobs. Using triggers, you can design a chain of dependent jobs and crawlers.

###### Note

You can accomplish the same thing by defining _workflows_.
Workflows are preferred for creating complex multi-job ETL operations. For more
information, see [Performing complex ETL activities using
blueprints and workflows in AWS Glue](orchestrate-using-workflows.md "orchestrate-using-workflows.md").

###### Topics

- [AWS Glue triggers](about-triggers.md "about-triggers.md")
- [Adding triggers](console-triggers.md "console-triggers.md")
- [Activating and deactivating triggers](activate-triggers.md "activate-triggers.md")
