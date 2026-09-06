

# Running a PySpark job on a configured table using a PySpark analysis template
<a name="run-jobs-with-analysis-template"></a>

This procedure demonstrates how to use a PySpark analysis template in the AWS Clean Rooms console to analyze configured tables with the **Custom** analysis rule. 

**To run a PySpark job on a configured table using a PySpark analysis template**

Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration that has **Your member abilities** status of **Run jobs**.

1. On the **Analysis** tab, under the **Tables** section, view the tables and their associated analysis rule type (**Custom analysis rule**).
**Note**  
If you don’t see the tables that you expect in the list, it might be for the following reasons:  
The tables haven't been [associated](associate-configured-table.md).
The tables don't have an [analysis rule configured](add-analysis-rule.md).

1. Under the **Analysis** section, for **Analysis mode**, select **Run analysis templates**.

1. Choose the PySpark analysis template from the **Analysis template** dropdown list.

   The parameters from the PySpark analysis template will automatically populate in the **Definition**.

1. If the analysis template has parameters defined, under **Parameters**, provide values for the parameters:

   1. For each parameter, view the **Parameter name** and **Default value** (if configured).

   1. Enter a **Value** for each parameter you want to override.
**Note**  
If you don't provide a value but a default value exists, the default value will be used.
**Important**  
Parameter values can be up to 1,000 characters and support UTF-8 encoding. All parameter values are treated as strings and passed to your user script through the context object.  
Ensure that your user script validates and handles parameter values safely. For more information about secure parameter handling, see [Working with parameters in PySpark analysis templates](pyspark-parameter-handling.md).

1. Specify the supported **Worker type** and the **Number of workers**. 

   Use the following table to determine the type and number or workers you need for your use case.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/run-jobs-with-analysis-template.html)
**Note**  
Different worker types and number of workers have associated costs. To learn more about the pricing, see [AWS Clean Rooms pricing](https://aws.amazon.com/clean-rooms/pricing/).

1. Specify the supported **Spark properties**.

   1. Select **Add Spark properties**.

   1. On the **Spark properties** dialog box, choose a **Property name** from the dropdown list and enter a **Value**.

   The following tables provide a definition for each property.

   For more information about Spark properties, see [Spark Properties](https://spark.apache.org/docs/latest/configuration.html#spark-properties) in the Apache Spark documentation. 
**Note**  
You can configure a maximum of 50 Spark properties. Each property value can be up to 500 characters.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/run-jobs-with-analysis-template.html)    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/run-jobs-with-analysis-template.html)

1. (Optional) For **Compute payer**, select the collaboration member who pays for job compute costs.
**Note**  
If there is only one payer candidate for job compute in the collaboration, it defaults to that payer.

1. Choose **Run**.
**Note**  
You can't run the job if the member who can receive results hasn’t configured the job results settings.

1. Continue to adjust parameters and run your job again, or choose the **\+** button to start a new job in a new tab.