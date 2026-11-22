

# Tagging and access control for question sets

You can tag question sets. To add tags when you create a question set, use `--tags` with `create-question-set`. To add or remove tags later, use the `tag-resource` and `untag-resource` commands with the ARN of the question set. To view tags, use `list-tags-for-resource`.

You can use tags to control access to question sets. Use the `aws:ResourceTag/${TagKey}` condition key with question set actions. Use the `aws:RequestTag/${TagKey}` and `aws:TagKeys` condition keys with `CreateQuestionSet`. For more information, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*.

The IAM resource type for question sets is `question-set`. The IAM actions for question sets are the following:
+ `elemental-inference:CreateQuestionSet`
+ `elemental-inference:GetQuestionSet`
+ `elemental-inference:UpdateQuestionSet`
+ `elemental-inference:DeleteQuestionSet`
+ `elemental-inference:ListQuestionSets`
+ `elemental-inference:CreateQuestionSetVersion`
+ `elemental-inference:ListQuestionSetVersions`
+ `elemental-inference:DeleteQuestionSetVersion`