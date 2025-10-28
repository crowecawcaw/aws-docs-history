# Data retention in AWS Clean Rooms

Any data that is temporarily read into an AWS Clean Rooms collaboration is deleted after the query
completes.

When you create a lookalike model, Clean Rooms ML reads your training data, transforms it into a
format suitable for our ML model, and stores the trained model parameters inside Clean Rooms ML.
Clean Rooms ML does not retain a copy of your training data. AWS Clean Rooms SQL queries do not retain any of
your data after the query has run. Clean Rooms ML then uses the trained model to summarize the
behavior of all of your users. Clean Rooms ML stores a user-level data set for each user in your
data for as long as your lookalike model is active.

When you start a lookalike segment generation job, Clean Rooms ML reads the seed data, reads the
behavior summaries from the associated lookalike model, and creates a lookalike segment that
is stored within the AWS Clean Rooms service. Clean Rooms ML does not retain a copy of your seed data.
Clean Rooms ML stores the user-level output of the job as long as the job is active.

If your seed data comes from an SQL query, the output of that query is only stored in the
service for the duration of the job. The results of the query are encrypted at rest and in
transit.

If you want to remove your lookalike model or lookalike segment generation job data, use
the API to delete it. Clean Rooms ML asynchronously deletes all data associated with the model or
job. Once this process is complete, Clean Rooms ML deletes the metadata for the model or job and it
is no longer visible in the API. Clean Rooms ML retains deleted data for 3 days for disaster
recovery prevention. Once the job or model is no longer visible in the API and 3 days have
passed, all data associated with the model or job has been permanently deleted.
