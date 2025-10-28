# Using Spigot to sample your dataset

To test the transformations performed by your job, you might want to get a sample of the
data to check that the transformation works as intended. The _Spigot_
transform writes a subset of records from the dataset to a JSON file in an Amazon S3
bucket. The data sampling method can be either a specific number of records from the
beginning of the file or a probability factor used to pick records.

###### To add a Spigot transform node to your job diagram

1. (Optional) Open the Resource panel and then choose **Spigot** to add a new transform to
   your job diagram, if needed.
2. On the **Node properties** tab, enter a name for the node in
   the job diagram. If a node parent is not already selected, then choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. Choose the **Transform** tab in the node details
   panel.
4. Enter an Amazon S3 path or choose **Browse S3** to choose a
   location in Amazon S3. This is the location where the job writes the JSON file
   that contains the data sample.
5. Enter information for the sampling method. You can specify a value for
   **Number of records** to write starting from the beginning of the
   dataset and a **Probability threshold** (entered as a decimal value
   with a maximum value of 1) of picking any given record.

For example, to write the first 50 records from the dataset, you would set
**Number of records** to 50 and **Probability
threshold** to 1 (100%).
