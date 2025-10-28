# Creating a user script

The user script must contain an entrypoint function (in other words, a handler). You can
name your user script file with any valid Python filename.

The following procedure describes how to create a user script to define the core
functionality of your PySpark analysis.

**Prerequisites**

- PySpark 1.0 (corresponds to
  Python
  3.11 and Spark
  3.5.3)
- Datasets in Amazon S3 can only be read as configured table associations in the Spark
  session you define.
- Your code can't directly call Amazon S3 and AWS Glue
- Your code can’t make network calls

###### To create a user script

1. Open a text editor or Integrated Development Environment (IDE) of your
   choice.

You can use any text editor or IDE (such as Visual Studio Code, PyCharm, or
Notepad++) that supports Python files. 2. Create a new Python file with a name of your choice (for example, `my_analysis.py`). 3. Define an entrypoint function that accepts a context object parameter.

```
def entrypoint(context)
```

The `context` object parameter is a dictionary that provides access to
essential Spark components and referenced tables. It contains Spark session access for
running Spark operations and the referenced tables:

Spark session access is available via `context['sparkSession']`

Referenced tables are available via `context['referencedTables']` 4. Define the results of the entrypoint function:

```
return results
```

The `results` must return an object containing a results dictionary of
filenames to an output DataFrame.

###### Note

AWS Clean Rooms automatically writes the DataFrame objects to the S3 bucket of the result
receiver. 5. You are now ready to:

    1. Store this user script in S3. For more information, see [Storing a user script and virtual environment in
     S3](store-artifacts-in-s3.md "store-artifacts-in-s3.md").
    2. Create the optional virtual environment to support any additional libraries
     required by your user script. For more information, see [Creating a virtual environment
     (optional)](create-virtual-environment.md "create-virtual-environment.md").

###### Example 1

The following example demonstrates a generic user script for a PySpark analysis
template.

```
# File name: my_analysis.py

def entrypoint(context):
    try:
        # Access Spark session
        spark = context['sparkSession']

        # Access input tables
        input_table1 = context['referencedTables']['table1_name']
        input_table2 = context['referencedTables']['table2_name']

        # Example data processing operations
        output_df1 = input_table1.select("column1", "column2")
        output_df2 = input_table2.join(input_table1, "join_key")
        output_df3 = input_table1.groupBy("category").count()

        # Return results - each key creates a separate output folder
        return {
            "results": {
                "output1": output_df1,        # Creates output1/ folder
                "output2": output_df2,        # Creates output2/ folder
                "analysis_summary": output_df3 # Creates analysis_summary/ folder
            }
        }

    except Exception as e:
        print(f"Error in main function: {str(e)}")
        raise e
```

The folder structure of this example is as follows:

```
analysis_results/
│
├── output1/ # Basic selected columns
│ ├── part-00000.parquet
│ └── _SUCCESS
│
├── output2/ # Joined data
│ ├── part-00000.parquet
│ └── _SUCCESS
│
└── analysis_summary/ # Aggregated results
├── part-00000.parquet
└── _SUCCESS
```

###### Example 2

The following example demonstrates a more complex user script for a PySpark
analysis template.

```
def entrypoint(context):
    try:
        # Get DataFrames from context
        emp_df = context['referencedTables']['employees']
        dept_df = context['referencedTables']['departments']

        # Apply Transformations
        emp_dept_df = emp_df.join(
            dept_df,
            on="dept_id",
            how="left"
        ).select(
            "emp_id",
            "name",
            "salary",
            "dept_name"
        )

        # Return Dataframes
        return {
            "results": {
                "outputTable": emp_dept_df
            }
        }

    except Exception as e:
        print(f"Error in entrypoint function: {str(e)}")
        raise e
```
