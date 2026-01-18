# Working with parameters in PySpark analysis templates

Parameters increase the flexibility of your PySpark analysis templates by allowing different values to be provided at job submission time. Parameters are accessible through the context object passed to your entrypoint function.

###### Note

Parameters are user-provided strings that can contain arbitrary content.

- Review the code to ensure parameters are handled safely to prevent unexpected behavior in your analysis.
- Design parameter handling to work safely regardless of what parameter values are provided at submission time.

## Accessing parameters

Parameters are available in the `context['analysisParameters']` dictionary. All parameter values are strings.

###### Example Accessing parameters safely

```
def entrypoint(context):
    # Access parameters from context
    parameters = context['analysisParameters']
    threshold = parameters['threshold']
    table_name = parameters['table_name']

    # Continue with analysis using parameters
    spark = context['sparkSession']
    input_df = context['referencedTables'][table_name]

    # Convert threshold value
    threshold_val = int(threshold)

    # Use parameter in DataFrame operation
    filtered_df = input_df.filter(input_df.amount > threshold_val)

    return {
        "results": {
            "output": filtered_df
        }
    }
```

## Parameter security best practices

###### Warning

Parameters are user-provided strings that can contain arbitrary content. You must handle parameters safely to prevent security vulnerabilities in your analysis code.

**Unsafe parameter handling patterns to avoid:**

- **Executing parameters as code** – Never use `eval()` or `exec()` on parameter values

```
# UNSAFE - Don't do this
eval(parameters['expression'])  # Can execute arbitrary code
```

- **SQL string interpolation** – Never concatenate parameters directly into SQL strings

```
# UNSAFE - Don't do this
sql = f"SELECT * FROM table WHERE column = '{parameters['value']}'"  # SQL injection risk
```

- **Unsafe file path operations** – Never use parameters directly in file system operations without validation

```
# UNSAFE - Don't do this
file_path = f"/data/{parameters['filename']}"  # Path traversal risk
```

**Safe parameter handling patterns:**

- **Use parameters in DataFrame operations** – Spark DataFrames handle parameter values safely

```
# SAFE - Use parameters in DataFrame operations
threshold = int(parameters['threshold'])
filtered_df = input_df.filter(input_df.value > threshold)
```

- **Validate parameter values** – Check that parameters meet expected formats before use

```
# SAFE - Validate parameters before use
def validate_date(date_str):
    try:
        from datetime import datetime
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

date_param = parameters['date_filter'] or '2024-01-01'
if not validate_date(date_param):
    raise ValueError(f"Invalid date format: {date_param}")
```

- **Use allowlists for parameter values** – When possible, validate parameters against known good values

```
# SAFE - Use allowlists
allowed_columns = ['column1', 'column2', 'column3']
column_param = parameters['column_name']
if column_param not in allowed_columns:
    raise ValueError(f"Invalid column: {column_param}")
```

- **Type conversion with error handling** – Convert string parameters to expected types safely

```
# SAFE - Convert with error handling
try:
    batch_size = int(parameters['batch_size'] or '1000')
    if batch_size <= 0 or batch_size > 10000:
        raise ValueError(f"Batch size must be between 1 and 10000")
except ValueError as e:
    print(f"Invalid parameter: {e}")
    raise
```

###### Important

Remember that parameters bypass code review when job runners provide different values. Design your parameter handling to work safely regardless of what parameter values are provided.

## Complete parameter example

###### Example Using parameters safely in a PySpark script

```
def entrypoint(context):
    try:
        # Access Spark session and tables
        spark = context['sparkSession']
        input_table = context['referencedTables']['sales_data']

        # Access parameters - fail fast if analysisParameters missing
        parameters = context['analysisParameters']

        # Validate and convert numeric parameter (handles empty strings with default)
        try:
            threshold = int(parameters['threshold'] or '100')
            if threshold <= 0:
                raise ValueError("Threshold must be positive")
        except (ValueError, TypeError) as e:
            print(f"Invalid threshold parameter: {e}")
            raise

        # Validate date parameter (handles empty strings with default)
        date_filter = parameters['start_date'] or '2024-01-01'
        from datetime import datetime
        try:
            datetime.strptime(date_filter, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Invalid date format: {date_filter}")

        # Use parameters safely in DataFrame operations
        filtered_df = input_table.filter(
            (input_table.amount > threshold) &
            (input_table.date >= date_filter)
        )

        result_df = filtered_df.groupBy("category").agg(
            {"amount": "sum"}
        )

        return {
            "results": {
                "filtered_results": result_df
            }
        }

    except Exception as e:
        print(f"Error in analysis: {str(e)}")
        raise
```
