# Running SQL and Spark code

You can run code against multiple compute in one Jupyter notebook using different
programming languages through the use of Jupyter cell magics %%pyspark, %%sql, %%scalaspark.

For example, to run pyspark code on Spark compute, you can run the following code:

```

%%pyspark `compute_name`
spark.createDataFrame([('Alice', 1)])

```

The following table represents the supported compute types of each magic:

| magic        | supported compute types                                                |
| ------------ | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| %%sql        | Redshift, Athena, EMR on EC2, EMR Serverless, Glue Interactive Session |
| %%pyspark    | EMR on EC2, EMR Serverless, Glue Interactive Session                   |
| %%scalaspark | EMR on EC2, EMR Serverless, Glue Interactive Session                   | The dropdown available at the top of active cells allows you to select the Connection and Compute type. If no selection is made the code in the cell will be run against the Compute hosting JupyterLab (“Local Python” / “project.python”). The option selected for Connection type dictates the Compute available. The selections dictate the magics code generated in the cell and determine where your code runs. When a new cell is created, it will select the same connection and compute type as the previous cell automatically. To configure the dropdown, go to Settings → Settings editor → Connection magics settings. |
