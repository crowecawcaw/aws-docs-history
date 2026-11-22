

# Question and version limits

The following table lists the limits for each question set.


| Item | Limit | 
| --- | --- | 
| Scored items in one version | Up to 100. To learn how to count scored items, see the list that follows this table. | 
| Questions in one version | At least 1, across all three lists | 
| yesNo questions | Up to 50 | 
| yesNoPerOption questions | Up to 10, each with 1–50 options | 
| chooseOne questions | Up to 10, each with 2–26 options | 
| Versions | Up to 99 for each question set: DRAFT plus up to 98 published versions | 
| Feeds that use a version | No limit | 

Elemental Inference counts scored items as follows:
+ Each `yesNo` question counts as 1.
+ Each option of a `yesNoPerOption` question counts as 1. For example, a `yesNoPerOption` question with 5 options counts as 5.
+ Each `chooseOne` question counts as 1, no matter how many options it has.

For example, a version has 20 `yesNo` questions, 2 `yesNoPerOption` questions with 10 options each, and 5 `chooseOne` questions. It has 20 \+ 20 \+ 5 = 45 scored items.

When a question set reaches the version limit, `CreateQuestionSetVersion` fails with a `ServiceQuotaExceededException`. To publish again, delete a version that you no longer need, or create a new question set.

Each AWS account can have up to 50 question sets in each AWS Region. When your account has 50 question sets, `CreateQuestionSet` fails with a `ServiceQuotaExceededException`. To create another question set, delete a question set that you no longer need.