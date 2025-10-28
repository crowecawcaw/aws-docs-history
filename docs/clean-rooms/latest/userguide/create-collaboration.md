# Creating a collaboration

There are three ways to create a collaboration in AWS Clean Rooms.

The most basic form is the [collaboration for queries](create-collab-queries.md "create-collab-queries.md"). This collaboration
focuses on SQL query analysis and maintains a simple structure with two main roles: one member
who can run queries and another who can receive results. This basic collaboration setup works
well for simple data analysis tasks.

The second form, [collaboration for queries and jobs](create-collab-queries-and-jobs.md "create-collab-queries-and-jobs.md"),
extends functionality by incorporating both SQL queries and PySpark jobs and requires Spark as
its analytics engine. This collaboration setup maintains the same basic role structure but
expands permissions to include job execution. A notable requirement is that the member who
creates PySpark analysis templates must also be the one receiving results, ensuring clear
accountability in the analysis process.

The third form, [collaboration for ML modeling](create-collab-ml-modeling.md "create-collab-ml-modeling.md"), is built for
machine learning workflows and requires Spark as its analytics engine. This collaboration setup
adds two more roles: one for users who need the results from trained models, and another for
users who need the results from using those models to make predictions. This collaboration setup
helps collaboration members work together on complex data projects while keeping everyone's
roles and permissions clear.

The following topics explain how to create collaborations for queries, jobs, and ML
modeling.

###### Topics

- [Creating a collaboration for queries](create-collab-queries.md "create-collab-queries.md")
- [Creating a collaboration for queries and
  jobs](create-collab-queries-and-jobs.md "create-collab-queries-and-jobs.md")
- [Creating a collaboration for ML modeling](create-collab-ml-modeling.md "create-collab-ml-modeling.md")
