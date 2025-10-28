# Reference policies

- **List Amazon EMR policies**: This policy allows
  performing the following actions:
  - `AllowPresignedUrl` allows generating pre-signed URLs for
    accessing the Spark UI from within Studio.
  - `AllowClusterDiscovery` and
    `AllowClusterDetailsDiscovery` allows listing and
    describing Amazon EMR clusters in the provided region and account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPresignedUrl",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:CreatePersistentAppUI",
 "elasticmapreduce:DescribePersistentAppUI",
 "elasticmapreduce:GetPersistentAppUIPresignedURL",
 "elasticmapreduce:GetOnClusterAppUIPresignedURL"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:`us-east-1`:`111122223333`:cluster/*"
 ]
 },
 {
 "Sid": "AllowClusterDetailsDiscovery",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:DescribeCluster",
 "elasticmapreduce:ListInstances",
 "elasticmapreduce:ListInstanceGroups",
 "elasticmapreduce:DescribeSecurityConfiguration"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:`us-east-1`:`111122223333`:cluster/*"
 ]
 },
 {
 "Sid": "AllowClusterDiscovery",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:ListClusters"
 ],
 "Resource": "*"
 }
 ]
}`

```

- **Create Amazon EMR clusters policies**: This policy
  allows performing the following actions:

      + `AllowEMRTemplateDiscovery` allows searching for Amazon EMR
       templates in the Service Catalog. Studio and Studio Classic use this to show
       available templates.
      + `AllowSagemakerProjectManagement` enables the creation of
       [What is a SageMaker AI Project?](sagemaker-projects-whatis.md "sagemaker-projects-whatis.md"). In
       Studio or Studio Classic, access to the AWS Service Catalog is managed
       through [What is a SageMaker AI Project?](sagemaker-projects-whatis.md "sagemaker-projects-whatis.md").

  The IAM policy defined in the provided JSON grants those permissions.
  Replace `region` and
  `accountID` with your actual region and AWS
  account ID values before copying the list of statements to the inline policy of
  your role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEMRTemplateDiscovery",
 "Effect": "Allow",
 "Action": [
 "servicecatalog:SearchProducts"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSagemakerProjectManagement",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateProject",
 "sagemaker:DeleteProject"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:project/*"
 }
 ]
}`

```

- **Domain, user profile, and space update actions policy** : The following policy grants permissions to update SageMaker AI domains,
  user profiles, and spaces within the specified region and AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SageMakerUpdateResourcesPolicy",
 "Effect": "Allow",
 "Action": [
 "sagemaker:UpdateDomain",
 "sagemaker:UpdateUserprofile",
 "sagemaker:UpdateSpace"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`111122223333`:domain/*",
 "arn:aws:sagemaker:`us-east-1`:`111122223333`:user-profile/*"
 ]
 }
 ]
}`

```
