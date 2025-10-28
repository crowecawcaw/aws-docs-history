# Accessing metadata

You can view metadata for your project in the notebook terminal within Amazon SageMaker Unified Studio. This
shows you information such as the `ProjectS3Path`, which is the Amazon S3 bucket where
your project data is stored. The project metadata is written to a file named
resource-metadata.json in the folder /opt/ml/metadata/. You can get the metadata by opening a
terminal from within the notebook.

1. Navigate to the Code page within the project you want to view metadata for.
2. Choose File > New > Terminal.
3. Enter in the following command:

```
cat /opt/ml/metadata/resource-metadata.json
```

The metadata file information then appears in the terminal window.
