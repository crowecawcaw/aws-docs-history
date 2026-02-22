# Work with Quick Sight topics using the

Amazon Quick Sight APIs

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

|                                               |
| --------------------------------------------- |
| Intended audience:<br>Amazon Quick developers |

Use this section to learn how to work with Quick Sight topics using the Amazon Quick Sight
command line interface (CLI).

**Prerequisites**

Before you begin, make sure that you have an AWS Identity and Access Management (IAM) role that grants the
CLI user access to call the Quick Sight API operations. The following table shows which
permissions must be added to the IAM policy to use specific API operations. To use all
of the topic API operations, add all of the permissions listed in the table.

| API operation                    | IAM policy                                           |
| -------------------------------- | ---------------------------------------------------- |
| `CreateTopic`                    | `quicksight:CreateTopic`<br>`quicksight:PassDataSet` |
| `ListTopics`                     | `quicksight:ListTopics`                              |
| `DescribeTopic`                  | `quicksight:DescribeTopic`                           |
| `DescribeTopicPermissions`       | `quicksight:DescribeTopicPermissions`                |
| `DescribeTopicRefresh`           | `quicksight:DescribeTopicRefresh`                    |
| `DeleteTopic`                    | `quicksight:DeleteTopic`                             |
| `UpdateTopic`                    | `quicksight:UpdateTopic`<br>`quicksight:PassDataSet` |
| `UpdateTopicPermissions`         | `quicksight:UpdateTopicPermissions`                  |
| `CreateTopicRefreshSchedule`     | `quicksight:CreateTopicRefreshSchedule`              |
| `ListTopicRefreshSchedules`      | `quicksight:ListTopicRefreshSchedules`               |
| `DescribeTopicRefreshSchedule`   | `quicksight:DescribeTopicRefreshSchedule`            |
| `UpdateTopicRefreshSchedule`     | `quicksight:UpdateTopicRefreshSchedule`              |
| `DeleteTopicRefreshSchedule`     | `quicksight:DeleteTopicRefreshSchedule`              |
| `BatchCreateTopicReviewedAnswer` | `quicksight:BatchCreateTopicReviewedAnswer`          |
| `BatchDeleteTopicReviewedAnswer` | `quicksight:BatchDeleteTopicReviewedAnswer`          |
| `ListTopicReviewedAnswers`       | `quicksight:ListTopicReviewedAnswers`                |

The following example shows an IAM policy that allows a user to use the
`ListTopics` API operation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "quicksight:ListTopics"
 ],
 "Resource": "*"
 }
 ]
}`

```

After you configure the permissions to create Quick Sight topics with the
Quick Sight APIs, use the following topics to create and work with Quick Sight topic
APIs.

###### Topics

- [Work with Quick Sight topics using the
  Quick Sight APIs](topic-cli-examples.md "topic-cli-examples.md")
- [Configure Quick Sight topic refresh
  schedules with the Quick Sight CLI](topic-refresh-apis.md "topic-refresh-apis.md")
- [Copy and migrate Quick Sight topics
  within and between AWS accounts](topic-cli-walkthroughs.md "topic-cli-walkthroughs.md")
- [Create and modify reviewed answers in
  Quick Sight topics with the Quick Sight APIs](topic-reviewed-answer-apis.md "topic-reviewed-answer-apis.md")
