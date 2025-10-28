# Creating a project policy

document

Rekognition Custom Labels uses a resource-based policy, known as _project
policy_, to manage copy permissions for a model version. A project
policy is a JSON format document.

A project policy allows or denies a [principal](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal") permission to copy a model version from a source project to a
destination project. You need a project policy if the destination project is in a
different AWS account. That's also true if the destination project is in the same
AWS account as the source project and you want to restrict access to specific
model versions. For example, you might want to deny copy permissions to a specific
IAM role within an AWS account.

The following example allows the principal
`arn:aws:iam::111111111111:role/Admin` to copy the model version
`arn:aws:rekognition:us-east-1:123456789012:project/my_project/version/test_1/1627045542080`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::111111111111:role/Admin"
 },
 "Action":"rekognition:CopyProjectVersion",
 "Resource":"arn:aws:rekognition:us-east-1:111111111111:project/my_project/version/test_1/1627045542080"
 }
 ]
}`

```

###### Note

`Action`, `Resource`, `Principal`, and
`Effect` are required fields in a project policy document.

The only supported `action` is
`rekognition:CopyProjectVersion`.

`NotAction`, `NotResource`, and
`NotPrincipal` are prohibited fields and must not be present in
the project policy document.

If you don't specify a project policy, a principal in the same AWS account as
the source project can still copy a model, if the principal has an Identity-based
policy, such as `AmazonRekognitionCustomLabelsFullAccess`, that gives
permission to call `CopyProjectVersion`.

The following procedure creates a project policy document file that you can use
with the Python example in [Attaching a project policy (SDK)](md-attach-project-policy.md "md-attach-project-policy.md"). If you are using the
`put-project-policy` AWS CLI command, you supply the project policy as
a JSON string.

###### To create a project policy document

1. In a text editor, create the following document. Change the following
   values:
   - Effect – Specify `ALLOW` to grant copy
     permission. Specify `DENY` to deny copy permission.
   - Principal – To the principal that you want to allow or deny
     access to the model versions that you specify in
     `Resource`. For example you can specify the [AWS account principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-accounts "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-accounts") for a different AWS account. We
     don't restrict the principals that you can use. For more
     information, see [Specifying a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#Principal_specifying "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#Principal_specifying").
   - Resource – The Amazon Resource Name (ARN) of the model
     version for which you want to specify copy permissions. If you want
     to grant permissions to all model versions within the source
     project, use the following format
     `arn:aws:rekognition:`region`:`account`:project/`source
     project`/version/*`

2. Save the project policy to your computer.
3. Attach the project policy to the source project by following the
   instructions at [Attaching a project policy (SDK)](md-attach-project-policy.md "md-attach-project-policy.md").
