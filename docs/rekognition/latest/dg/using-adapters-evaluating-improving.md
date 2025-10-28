# Evaluating and improving your adapter

After every round of adapter training, you’ll want to review the performance metrics
in the Rekognition Console tool to determine how close the adapter is to your desired level of
performance. You can then further improve your adapter’s accuracy for your images by
uploading a new batch of training images and training a new adapter inside your project.
Once you have created an improved version of the adapter, you can use the console to
delete any older versions of the adapter that you no longer need.

You can also retrieve metrics using the [DescribeProjectVersions](../APIReference/API_DescribeProjectVersions.md "../APIReference/API_DescribeProjectVersions.md") API operation.

## Performance metrics

Once you have finished the training process and created your adapter,
it's important to evaluate how well the adapter is extracting information from your images.

Two metrics are provided in the Rekognition Console to assist you in analyzing your adapter's performance:
false positive improvement and false negative improvement.

You can view these metrics for any adapter by selecting the "Adapter performance"
tab in the adapter portion of the console. The adapter performance panel shows the
False Positive Improvement and False Negative Improvement rates for the adapter that
you created.

False positive improvement measures how much the adapter’s recognition of false-positives has improved
over the base model. If the false positive improvement value is 25%, that means that the adapter
improved its recognition of false positives by 25% on the test dataset.

False negative improvement measures how much the adapter’s recognition of false-negatives
has improved over the base model. If the false negative improvement value is 25%, that means
that the adapter improved its recognition of false negatives by 25% on the test dataset.

The Per Label Performance tab can be used to compare the adapter and base model performance on each
label category. It shows counts of false positive and false negative predictions by
both the base model and the adapter, stratified by label category. By reviewing these metrics
you can determine where the adapter needs improvement.

For example, if the Base Model False Negative rate for the Alcohol label category is
15 while the Adapter False Negative Rate is 15 or higher, you know that you should
focus on adding more images containing the Alcohol label when creating a new adapter.

When using the Rekognition API operations, the F1-Score metric is returned when calling
the [DescribeProjectVersions](../APIReference/API_DescribeProjectVersions.md "../APIReference/API_DescribeProjectVersions.md") operationn.

## Improving your model

Adapter deployment is an iterative process, as you’ll likely need to train an
adapter several times to reach your target level of accuracy. After you create and
train your adapter, you’ll want to test and evaluate your adapter’s performance on
various types of labels.

If your adapter’s accuracy is lacking in any area, add new examples of those
images to increase the adapter’s performance for those labels. Try to provide the adapter
with additional, varied examples which reflects the cases where it struggles. Providing your adapter
with representative, varied images enables it to handle diverse real-world examples.

After adding new images to your training set, retrain the adapter, then
re-evaluate on your test set and labels. Repeat this process until the adapter
reaches your desired level of performance. If you provide more representative images and annotations,
false positive and false negative scores.
will gradually improve over successive training iterations.
