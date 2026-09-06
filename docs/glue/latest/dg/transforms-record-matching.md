

# Using the Record Matching transform to invoke an existing data classification transform
<a name="transforms-record-matching"></a>

This transform invokes an existing Record Matching machine learning data classification transform.

The transform evaluates the current data against the trained model based on labels. A column "match\_id" is added to assign each row to a group of items that are considered equivalent based on the algorithm training. For more information, see [Record matching with Lake Formation FindMatches](https://docs.aws.amazon.com/glue/latest/dg/machine-learning.html).

**Note**  
The version of AWS Glue used by the visual job must match the version that AWS Glue used to create the Record Matching transform.

![The screenshot shows a data preview for the transform.](http://docs.aws.amazon.com/glue/latest/dg/images/recording-matching-transform-1.png)


**To add a Record Matching transform node to your job diagram**

1. Open the Resource panel, and then choose **Record Matching** to add a new transform to your job diagram. The node selected at the time of adding the node will be its parent.

1. In the node properties panel, you can enter a name for the node in the job diagram. If a node parent isn't already selected, choose a node from the **Node parents** list to use as the input source for the transform.

1. On the **Transform** tab, enter the ID taken from the **Machine learning transforms** page:  
![The screenshot shows the ID from the Machine learning transforms page.](http://docs.aws.amazon.com/glue/latest/dg/images/recording-matching-transform-2.png)

1. (Optional) On the **Transform** tab, you can check the option to add the confidence scores. At the cost of extra computing, the model will estimate a confidence score for each match as an additional column.