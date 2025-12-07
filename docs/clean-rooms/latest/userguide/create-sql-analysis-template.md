# Creating a SQL analysis template

**Prerequisites**

Before you create a SQL analysis template, you must have:

- An active AWS Clean Rooms collaboration
- Access to at least one configured table in the collaboration

For information about configuring tables in AWS Clean Rooms, see [Creating a configured table in
AWS Clean Rooms](create-configured-table.md "create-configured-table.md").

- Permissions to create analysis templates
- Basic knowledge of SQL query syntax
  The following procedure describes the process of creating a SQL analysis template using
  the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").

For information about how to create a SQL analysis template using the AWS SDKs, see
the [AWS Clean Rooms
API Reference](../apireference/Welcome.md "../apireference/Welcome.md").

###### To create a SQL analysis template

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with the AWS account that will function as the
   collaboration creator.
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Templates** tab, go to the **Analysis templates
   created by you** section.
5. Choose **Create analysis template**.
6. On the **Create analysis template** page, for
   **Details**,
   1. Enter a **Name** for the analysis template.
   2. (Optional) Enter a **Description**.
   3. For **Format**, leave the **SQL** option
      selected.

7. For **Tables**, view the configured tables associated with the
   collaboration.
8. For **Definition**,
   1. Enter the definition for the analysis template.
   2. Choose **Import from** to import a definition.
   3. (_Optional_) Specify a parameter in the SQL
      editor by entering a colon (`:`) in front of the parameter name.

   For example:

   `WHERE table1.date + :date_period > table1.date`

9. If you added parameters previously, under **Parameters –
   optional**, for each **Parameter name**, choose the
   **Type** and **Default value** (optional).
10. For **Synthetic data**, if you want to generate synthetic data for
    model training, select the **Require analysis template output to be
    synthetic** checkbox.

For more information, see [Privacy-enhanced
synthetic dataset generation](synthetic-data-generation.md "synthetic-data-generation.md").

    1. For **Column classification**, choose a
     **Column** from the dropdown list. At least five columns are
     required.


    	1. Choose a **Classification** from the dropdown list. This
    	 identifies the data type for each column.


    	Classification types include:




    		* **Numerical** – Continuous numerical values such
    		 as measurements or counts
    		* **Categorical** – Discrete values or categories
    		 such as labels or types
    	2. To remove a column, select **Remove**.
    	3. To add another column, select **Add another column**.
    	 Choose the **Column** and **Classification**
    	 from the dropdown lists.
    	4. For **Predictive value**, choose a
    	 **Column** from the dropdown list. This is the column the
    	 custom model uses for prediction after it's trained on the synthetic
    	 dataset.
    2. **Advanced settings** allow you to set the **Privacy
     level** and **Privacy threshold**. Adjust the settings
     to fit your needs.


    	1. For **Privacy level**, enter an epsilon value to determine
    	 how much noise the synthetic model adds to protect privacy in your generated
    	 dataset. The value must be between 0.0001 and 10.




    		* Lower values add more noise, providing stronger privacy protection but
    		 potentially reducing utility for downstream custom model trained on this
    		 data.
    		* Higher values add less noise, providing more accuracy but potentially
    		 reducing privacy protection.
    	For **Privacy threshold**, enter the highest allowed
    	 probability that a membership inference attack could identify members of the
    	 original dataset. The value must be between 50.0 and 100.




    		* Scores of 50% indicate that a membership inference attack can't
    		 successfully distinguish members from non-members better than a random
    		 guess.
    		* For no privacy limit, enter 100%.
    	The optimal value depends on your specific use case and privacy
    	 requirements. If the privacy threshold is exceeded, the ML input channel
    	 creation fails, and you can't use the synthetic dataset to train a model.###### Warning

Synthetic data generation protects against inferring individual attributes whether
specific individuals are present in the original dataset or learning attributes of
those individuals are present. However, it doesn't prevent literal values from the
original dataset, including personally identifiable information (PII) from appearing
in the synthetic dataset.

We recommend avoiding values in the input dataset that are associated with only
one data subject because these may re-identify a data subject. For example, if only
one user lives in a zip code, the presence of that zip code in the synthetic dataset
would confirm that user was in the original dataset. Techniques like truncating high
precision values or replacing uncommon catalogues with _other_ can be used to mitigate this risk. These transformations can be
part of the query used to create the ML input channel. 11. If you want to enable **Tags** for the resource, choose
**Add new tag** and then enter the **Key** and
**Value** pair. 12. Choose **Create**. 13. You are now ready to inform your collaboration member that they can [Review an analysis template](review-analysis-template.md "review-analysis-template.md"). (Optional if
you want to query your own data.)
