

# Test the training data
<a name="testing-the-model"></a>

After training the model, Amazon Comprehend tests the custom classifier model. If you don't provide a test dataset, Amazon Comprehend trains the model with 90 percent of the training data. It reserves 10 percent of the training data to use for testing. If you do provide a test dataset, the test data must include at least one example for each unique label in the training dataset. 

Testing the model provides you with metrics that you can use to estimate the accuracy of the model. The console displays the metrics in the **Classifier performance** section of the **Classifier details** page in the console. They're also returned in the `Metrics` fields returned by the [DescribeDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeDocumentClassifier.html) operation.

In the following example training data, there are five labels, DOCUMENTARY, DOCUMENTARY, SCIENCE\_FICTION, DOCUMENTARY, ROMANTIC\_COMEDY. There are three unique classes: DOCUMENTARY, SCIENCE\_FICTION, ROMANTIC\_COMEDY. 


| Column 1 | Column 2 | 
| --- | --- | 
| DOCUMENTARY | document text 1 | 
| DOCUMENTARY | document text 2 | 
| SCIENCE\_FICTION | document text 3 | 
| DOCUMENTARY | document text 4 | 
| ROMANTIC\_COMEDY | document text 5 | 

For auto split (where Amazon Comprehend reserves 10 percent of the training data to use for testing), if the training data contains limited examples of a specific label, the test dataset may contain zero examples of that label. For instance, if the training dataset contains 1000 instances of the DOCUMENTARY class, 900 instances of SCIENCE\_FICTION, and a single instance of the ROMANTIC\_COMEDY class, the test dataset might contain 100 DOCUMENTARY and 90 SCIENCE\_FICTION instances, but no ROMANTIC\_COMEDY instances, as there is a single example available. 

After you finish training your model, the training metrics provide information that you can use to decide if the model is sufficiently accurate for your needs. 