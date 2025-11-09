# Instance type compute table

The following table lists the AWS Region, instance family keyword, and available
instance families. AWS Batch will try to allocate an instance from the latest family but because
instance family availability varies by AWS Region you may get an earlier instance family
generation.

| default_x86_64                                                                                                      | Region               | Instance families |
| ------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------- |
| All AWS Regions that support [AWS Batch](../../../general/latest/gr/batch.md "../../../general/latest/gr/batch.md") | m6i, c6i, r6i<br>c7i |

| default_arm64                                                                                                       | Region               | Instance families |
| ------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------- |
| All AWS Regions that support [AWS Batch](../../../general/latest/gr/batch.md "../../../general/latest/gr/batch.md") | m6g, c6g, r6g<br>c7g |

| Optimal                                                                                                                                                                                                                                                                                                                                                                                                | Region     | Instance families |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ----------------- |
| • ap-northeast-1<br>• ap-northeast-2<br>• ap-south-1<br>• ap-southeast-1<br>• ap-southeast-2<br>• ca-central-1<br>• cn-north-1<br>• cn-northwest-1<br>• eu-central-1<br>• eu-west-1<br>• eu-west-2<br>• sa-east-1<br>• us-east-1<br>• us-east-2<br>• us-gov-west-1<br>• us-west-1<br>• us-west-2                                                                                                       | m4, c4, r4 |
| • af-south-1<br>• ap-east-1<br>• ap-northeast-3<br>• ap-south-2<br>• ap-southeast-3<br>• ap-southeast-4<br>• ca-west-1<br>• eu-central-2<br>• eu-north-1<br>• eu-south-1<br>• eu-south-2<br>• eu-west-3<br>• il-central-1<br>• me-central-1<br>• me-south-1<br>• us-gov-east-1<br>• us-isob-east-1<br>• us-iso-east-1<br>• us-isof-south-1<br>• us-isof-east-1<br>• eu-isoe-west-1<br>• us-northeast-1 | m5, c5, r5 |
| • ap-southeast-5<br>• ap-southeast-7<br>• ap-east-2<br>• mx-central-1                                                                                                                                                                                                                                                                                                                                  | m6, c6, r6 |
