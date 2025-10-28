# Visualizing results

%display is a magic that customers can apply against any DataFrame to invoke a
visualization for tabular data. use the visualization to scroll through a DataFrame or results
of a Redshift or Athena query.

There are four different views:

- **Table**. You can change the sampling method, sample size, and rows
  per page that are displayed.
- **Summary**. Each column in the summary tab has a button labeled with
  the column’s name. Clicking on one of these buttons opens the a sub-tab in the column view
  in Tab 3 for the column that was clicked.
- **Column**. For each column selected in the column selector above, a
  sub-tab appears with more details about the contents of the column.
- **Plotting**. In the default plotting view you can change the graph
  type, axes, value types, and aggregation functions for plotting. By installing an optional
  supported third-party plotting library on the Jupyterlab space (pygwalker,
  ydata-profiling, or dataprep) and running the display magic you can visualize your data
  using the installed library.

## Shared Project Storage

The JupyterLab visualization widget offers an option to store visualization data in a shared Amazon S3 location within your project bucket. The data is stored using the following structure:

```

s3://bucket/domain/project/dev/user/{sts_user_identity}/query-result/{data_uuid}/

├── dataframe/           # Contains DataFrame in parquet format
├── head/100/            # Sample data (100 rows)
│   ├── metadata.json
│   ├── summary_schema.json
│   └── column_schema/
└── tail/                # Additional sample data

```

## Storage Options

The visualization widget supports two storage modes controlled by the `--query-storage` parameter:

- **Cell storage** (`--query-storage cell`): Data stored locally in notebook output (current default behavior)
- **S3 storage** (`--query-storage s3`): Data stored in project's shared S3 bucket for persistence and sharing
  - Choose **Store query result in S3** to store the data in project's shared S3 bucket.

## Data Access and Security

When using Amazon S3 storage, the visualization data is accessible to all project members. Data persists beyond individual JupyterLab sessions. No individual user permissions can be set on stored visualizations. You should consider data classification before storing sensitive information. The storage uses the project's default runtime role for access control.

###### Note

The Amazon S3 storage location is shared across the entire project. All project members can access visualization data stored by any team member.
