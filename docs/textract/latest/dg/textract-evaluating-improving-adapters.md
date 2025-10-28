# Evaluating and improving your

adapters

Once you have finished the training process and created your adapter, it's important
to evaluate how well the adapter is extracting information from your documents.

###### Performance metrics

Three metrics are provided in the Amazon Textract console to assist you in analyzing
your adapter's performance:

1. Precision - Precision measures the percentage of extracted information
   (predictions) that are correct. The higher the precision rating, the fewer false
   positives there are.
2. Recall - Recall measures the percentage of total relevant items that are
   successfully identified and extracted by the model. The higher the recall value,
   the fewer false negatives there are.
3. F1 Score - The F1 score combines precision and recall into a single metric,
   providing a balanced measurement for overall extraction accuracy.
   The values for these measurements range from 0 to 1, with 1 being perfect
   extraction.

These metrics are calculated by comparing the adapter's extractions to the "ground
truth" annotations on the test set. By analyzing the F1, precision, and recall, you can
determine where the adapter needs improvement.

For example, low precision means many of the model’s predictions are false positives,
therefore the adapter is extracting irrelevant data. In contrast, a low recall value
means that the model is missing relevant data. Using these insights, you can refine the
training data and retrain the adapter to increase performance.

You can also check the performance of your model by testing it with new documents and
queries that you specify. Use the **Try Adapter** option in
the console to get predictions for these documents. This way, you can evaluate the
adapter with your own test queries and documents and see real-world examples of how the
adapter is performing.

You can also retrieve metrics for an adapter version by using the [GetAdapterVersion](API_GetAdapterVersion.md "API_GetAdapterVersion.md") operation
using an SDK or the CLI. Get a list of adapters that you want to retrieve metrics for by
using the [ListAdapterVersions](API_ListAdapterVersions.md "API_ListAdapterVersions.md") API operation. Delete an adapter you no
longer need with the [DeleteAdapterVersion](API_DeleteAdapterVersion.md "API_DeleteAdapterVersion.md") operation.

###### Improving your model

Adapter deployment is an iterative process, as you’ll likely need to retrain
several times to reach your target level of accuracy. After you create and train
your adapter, you’ll want to test and evaluate your adapter’s performance on various
metrics and queries.

If your adapter’s accuracy is lacking in any area, add new examples of those documents
to increase the adapter’s performance for those queries. Try to provide the adapter with
additional, varied examples that reflect the cases where it struggles. Providing your
adapter with representative, varied documents enables it to handle diverse real-world
examples.

After adding new documents to your training set, retrain the adapter. Then re-evaluate
on your test set and queries. Repeat this process until the adapter reaches your desired
level of performance. Precision, recall, and F1 scores should gradually improve over
successive training iterations.
