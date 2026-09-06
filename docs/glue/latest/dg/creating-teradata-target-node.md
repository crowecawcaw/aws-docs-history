

# Creating a Teradata target node
<a name="creating-teradata-target-node"></a>

## Prerequisites needed
<a name="creating-teradata-target-node-prerequisites"></a>
+ A AWS Glue Teradata Vantage connection, configured with an AWS Secrets Manager secret, as described in the previous section, [Creating a Teradata Vantage connection](creating-teradata-connection.md).
+ Appropriate permissions on your job to read the secret used by the connection.
+ A Teradata table you would like to write to, {{tableName}}.

## Adding a Teradata data target
<a name="creating-teradata-target-node-add"></a>

**To add a **Data target – Teradata** node:**

1.  Choose the connection for your Teradata data source. Since you have created it, it should be available in the dropdown. If you need to create a connection, choose **Create Teradata connection**. For more information, see [ Overview of using connectors and connections ](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html#using-connectors-overview). 

    Once you have chosen a connection, you can view the connection properties by clicking **View properties**. 

1. Configure **Table name** by providing {{tableName}}.

1.  In **Custom Teradata properties**, enter parameters and values as needed. 