# Manually configuring a Neptune notebook for Neptune ML

Neptune SageMaker AI notebooks come pre-loaded with a variety of sample notebooks for
Neptune ML. You can preview these samples in the [open
source graph-notebook GitHub repository](https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/notebooks/04-Machine-Learning "https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/notebooks/04-Machine-Learning").

You can use one of the existing Neptune notebooks, or if you want you can create
one of your own, following the instructions in [Using the Neptune workbench to host Neptune notebooks](graph-notebooks.md#graph-notebooks-workbench "graph-notebooks.md#graph-notebooks-workbench").

You can also configure a default Neptune notebook for use with Neptune ML
by following these steps:

###### Modify a notebook for Neptune ML

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the navigation pane on the left, choose **Notebook**,
   then **Notebook Instances**. Look for the name of the Neptune notebook
   that you would like to use for Neptune ML and select it to go to its details page.
3. If the notebook instance is running, select the **Stop**
   button at the top right of the notebook details page.
4. In **Notebook instance settings**, under **Lifecycle
   Configuration**, select the link to open the page for the notebook's lifecycle.
5. Select **Edit** at the top right, then **Continue**.
6. In the **Start notebook** tab, modify the script to include
   additional export commands and to fill in the fields for your Neptune ML IAM role and
   Export service URI, something like this depending on your shell:

```
echo "export NEPTUNE_ML_ROLE_ARN=`(your Neptune ML IAM role ARN)`" >> ~/.bashrc
echo "export NEPTUNE_EXPORT_API_URI=`(your export service URI)`" >> ~/.bashrc
```

7. Select **Update**.
8. Return to the notebook instance page. Under **Permissions and
   encryption** there is a field for **IAM role ARN**.
   Select the link in this field to go to the IAM role that this notebook instance
   runs with.
9. Create a new inline policy like this:
10. Save this new policy and attach it to the IAM role in Step 8.
11. Select **Start** at the top right of of
    the SageMaker AI notebook instance details page to start the notebook instance.
