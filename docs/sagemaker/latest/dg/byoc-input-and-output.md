# How Amazon SageMaker Processing Configures Input and Output For

Your Processing Container

When you create a processing job using the `CreateProcessingJob`
operation, you can specify multiple `ProcessingInput` and
`ProcessingOutput`. values.

You use the `ProcessingInput` parameter to specify an Amazon Simple Storage Service (Amazon S3)
URI to download data from, and a path in your processing container to download the
data to. The `ProcessingOutput` parameter configures a path in your
processing container from which to upload data, and where in Amazon S3 to upload that
data to. For both `ProcessingInput` and `ProcessingOutput`,
the path in the processing container must begin with `/opt/ml/processing/` .

For example, you might create a processing job with one
`ProcessingInput` parameter that downloads data from
`s3://your-data-bucket/path/to/input/csv/data` into
`/opt/ml/processing/csv` in your processing container, and a
`ProcessingOutput` parameter that uploads data from
`/opt/ml/processing/processed_csv` to
`s3://your-data-bucket/path/to/output/csv/data`. Your processing job
would read the input data, and write output data to
`/opt/ml/processing/processed_csv`. Then it uploads the data written
to this path to the specified Amazon S3 output location.

###### Important

Symbolic links (symlinks) can not be used to upload output data to Amazon S3.
Symlinks are not followed when uploading output data.
