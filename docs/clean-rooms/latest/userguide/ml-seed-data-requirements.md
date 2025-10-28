# Seed data requirements for

Clean Rooms ML

The seed data for a lookalike model can either come directly from an Amazon S3 bucket
or from the results of an SQL query.

Seed data that's provided directly must meet the following requirements:

- The seed data must be in JSON lines format with a list of user IDs.
- The seed size should be between 25 and 500,000 unique user IDs.
- The minimum number of seed users must match the minimum matching seed size
  value that was specified when you created the configured audience
  model.
  The following is an example of a valid training data set in CSV format

```
`{"user_id": "abc"}
{"user_id": "def"}
{"user_id": "ghijkl"}
{"user_id": "123"}
{"user_id": "456"}
{"user_id": "7890"}`

```
