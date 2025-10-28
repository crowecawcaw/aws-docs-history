# Exporting AWS Data Exchange asset revisions to an S3 bucket (AWS

SDKs)

You can use the AWS SDKs to export AWS Data Exchange asset revisions to an S3 bucket using the
following instructions.

###### To export a revision to an S3 bucket (AWS SDKs)

1. Create a `CreateJob` request of type `EXPORT_REVISIONS_TO_S3`.
2. Include the following in the request:
   - `DataSetId`
   - `Encryption`
     - `KmsKeyArn`
     - `Type`

   - `RevisionDestinations`
     - `Bucket`
     - `KeyPattern`
     - `RevisionId`

3. Start the `CreateJob` request with a `StartJob` operation that
   requires the `JobId` returned in step 1.
4. The newly created assets have a name property equal to the original S3 object's key.
   The Amazon S3 object key defaults to the key pattern `${Asset.Name}`.

You can update the assets' name property after they are created.

For more information about key patterns, see [Key patterns when exporting asset revisions
from AWS Data Exchange](revision-export-keypatterns.md "revision-export-keypatterns.md").

###### Note

If you are using `DataSet.Name` as the dynamic reference, you must have the
IAM permission `dataexchange:GetDataSet`. For more information, see [AWS Data Exchange API permissions: actions and resources
reference](api-permissions-ref.md "api-permissions-ref.md").
