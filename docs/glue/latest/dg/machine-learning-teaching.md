# Teaching the Find Matches transform

Each `FindMatches` transform must be taught what should be considered a match
and what should not be considered a match. You teach your transform by adding labels to a file
and uploading your choices to AWS Glue.

You can orchestrate this labeling on the AWS Glue console or by using the AWS Glue machine
learning API operations.

###### How many times should I add labels? How many labels do I need?

The answers to these questions are mostly up to you. You must evaluate whether
`FindMatches` is delivering the level of accuracy that you need and whether
you think the extra labeling effort is worth it for you. The best way to decide this is to
look at the “Precision,” “Recall,” and “Area under the precision recall curve” metrics that
you can generate when you choose **Estimate quality** on the AWS Glue console.
After you label more sets of tasks, rerun these metrics and verify whether they have
improved. If, after labeling a few sets of tasks, you don't see improvement on the metric
that you are focusing on, the transform quality might have reached a plateau.

###### Why are both true positive and true negative labels needed?

The `FindMatches` transform needs both positive and negative examples to
learn what you think is a match. If you are labeling `FindMatches`-generated
training data (for example, using the **I do not have labels** option),
`FindMatches` tries to generate a set of “label set ids” for you. Within each
task, you give the same “label” to some records and different “labels” to other records. In
other words, the tasks generally are not either all the same or all different (but it's okay
if a particular task is all “the same” or all “not the same”).

If you are teaching your `FindMatches` transform using the **Upload
labels from S3** option, try to include both examples of matching and nonmatching
records. It's acceptable to have only one type. These labels help you build a more accurate
`FindMatches` transform, but you still need to label some records that you
generate using the **Generate labeling file** option.

###### How can I enforce that the transform matches exactly as I taught it?

The `FindMatches` transform learns from the labels that you provide, so it
might generate records pairs that don't respect the provided labels. To enforce that the
`FindMatches` transform respects your labels, select
**EnforceProvidedLabels** in
**FindMatchesParameter**.

###### What techniques can you use when an ML transform identifies items as matches that are

not true matches?

You can use the following techniques:

- Increase the `precisionRecallTradeoff` to a higher value. This eventually results
  in finding fewer matches, but it should also break up your big cluster when it reaches a
  high enough value.
- Take the output rows corresponding to the incorrect results and reformat them as a labeling
  set (removing the `match_id` column and adding a `labeling_set_id`
  and `label` column). If necessary, break up (subdivide) into multiple labeling
  sets to ensure that the labeler can keep each labeling set in mind while assigning labels.
  Then, correctly label the matching sets and upload the label file and append it to your
  existing labels. This might teach your transformer enough about what it is looking for to
  understand the pattern.
- (Advanced) Finally, look at that data to see if there is a pattern that you can detect that
  the system is not noticing. Preprocess that data using standard AWS Glue functions to
  _normalize_ the data. Highlight what you want the algorithm to learn
  from by separating data that you know to be differently important into their own columns.
  Or construct combined columns from columns whose data you know to be related.
