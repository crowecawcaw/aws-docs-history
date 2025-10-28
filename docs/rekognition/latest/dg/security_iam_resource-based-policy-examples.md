# Examples of Amazon Rekognition

resource-based policy

Amazon Rekognition Custom Labels uses resource-based polices, known as _project policies_,
to manage copy permissions for a model version.

A project policy gives or denies permission to copy a model version from a source
project to a destination project. You need a project policy if the destination project
is in a different AWS account or if you want to restrict access within an AWS account, For example,
you might want to deny copy permissions to a specific IAM role. For more information, see [Copying a
model](../customlabels-dg/md-copy-model-overview.md "../customlabels-dg/md-copy-model-overview.md").

## Giving permission to copy a model version

The following example allows the principal `arn:aws:iam::123456789012:role/Admin` to copy
the model version `arn:aws:rekognition:us-east-1:123456789012:project/my_project/version/test_1/1627045542080`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::123456789012:role/Admin"
 },
 "Action":"rekognition:CopyProjectVersion",
 "Resource":"arn:aws:rekognition:us-east-1:123456789012:project/my_project/version/test_1/1627045542080"
 }
 ]
}`

```
