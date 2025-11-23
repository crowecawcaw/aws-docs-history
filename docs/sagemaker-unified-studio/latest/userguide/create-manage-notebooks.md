# Create and manage notebooks

## Overview

You can create new notebooks in Amazon SageMaker Unified Studio to start data analysis workflows. Notebooks are automatically saved as you work, and you can organize them within your project structure.

The notebook interface provides access to sample notebooks that demonstrate common data analysis patterns. You can copy these samples to create starting points for your own analysis.

## Procedure

1. Navigate to the Notebooks section in your Amazon SageMaker Unified Studio project.
2. Click Create notebook to start a new notebook.
3. Enter a name for your notebook or use the auto-generated name.
4. A Python cell is added by default. You can begin by adding Python code or adding cells to your notebook using the buttons (Python, SQL, Markdown, Table, Charts).
5. Your notebook saves automatically as you work.

To access sample notebooks:

1. In the Notebooks section, review the Build with sample data section.
2. Select a sample notebook that matches your use case.
3. Click on the sample to open it in read-only mode.
4. Copy the sample notebook to create your own editable version.

You can view all your notebooks in the notebooks list, which shows the name, ID, last updated information, and creation details for each notebook.

## Examples

Amazon SageMaker Unified Studio comes with loaded sample notebooks for easy getting started and understanding the available capabilities. To view the available samples, go to the overview or notebooks pages in Amazon SageMaker Unified Studio. In addition, here are some cell code examples to demonstrate different cell types you can use in your notebooks:

Python cell example:

```

import pandas as pd
import numpy as np

# Create sample data
sample_data = {
    'product_id': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories'],
    'price': [999.99, 29.99, 79.99, 299.99, 149.99],
    'in_stock': [True, True, False, True, True]
}

df = pd.DataFrame(sample_data)
df

```

SQL cell example:

```

SELECT
    category,
    COUNT(*) as product_count,
    AVG(price) as avg_price,
    SUM(CASE WHEN in_stock THEN 1 ELSE 0 END) as in_stock_count
FROM df
GROUP BY category
ORDER BY avg_price DESC;

```

Markdown cell example:

```

# Data Analysis Report

## Overview
This notebook analyzes product inventory and pricing data.

## Key Findings
1. Electronics have higher average prices than accessories
2. Inventory levels are generally well-maintained
3. Price distribution shows clear category segmentation

## Next Steps
1. Analyze seasonal trends
2. Review pricing strategy
3. Optimize inventory levels

```

Spark cell example in Python:

```

from pyspark.sql.connect import functions as F

# Create Spark DataFrame
spark_df = spark.createDataFrame(df)

# Perform aggregations using Spark Connect
result = (
    spark_df.groupBy("category")
    .agg(
        F.count("*").alias("product_count"),
        F.avg("price").alias("avg_price"),
        F.count(F.when(F.col("in_stock") == True, 1)).alias("in_stock_count"),
    )
    .orderBy(F.col("avg_price").desc())
)
result.show()

```
