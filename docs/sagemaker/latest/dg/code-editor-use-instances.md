# Code Editor application instances and images

Only some instances are compatible with Code Editor applications. You can choose the instance
type that is compatible with your use case from the **Instance** dropdown
menu.

The **Fast launch** instances start up much faster than the other
instances. For more information about fast launch instance types in Studio, [Instance Types Available for Use With
Amazon SageMaker Studio Classic Notebooks](notebooks-available-instance-types.md "notebooks-available-instance-types.md").

###### Note

If you use a GPU instance type when configuring your Code Editor application, you must also
use a GPU-based image. The Code Editor space UI automatically selects a compatible image when you
select your instance type.

Within a space, your data is stored in an Amazon EBS volume that persists independently from
the life of an instance. You won't lose your data when you change instances. If your Code Editor
space is `Running`, you must stop your space before changing instance
types.

The following table lists the ARNs of the available Code Editor CPU and GPU images for each
Region.

| Region         | CPU                                                                            | GPU                                                                            |
| -------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| us-east-1      | arn:aws:sagemaker:us-east-1:885854791233:image/sagemaker-distribution-cpu      | arn:aws:sagemaker:us-east-1:885854791233:image/sagemaker-distribution-gpu      |
| us-east-2      | arn:aws:sagemaker:us-east-2:37914896644:image/sagemaker-distribution-cpu       | arn:aws:sagemaker:us-east-2:37914896644:image/sagemaker-distribution-gpu       |
| us-west-1      | arn:aws:sagemaker:us-west-1:053634841547:image/sagemaker-distribution-cpu      | arn:aws:sagemaker:us-west-1:053634841547:image/sagemaker-distribution-gpu      |
| us-west-2      | arn:aws:sagemaker:us-west-2:542918446943:image/sagemaker-distribution-cpu      | arn:aws:sagemaker:us-west-2:542918446943:image/sagemaker-distribution-gpu      |
| af-south-1     | arn:aws:sagemaker:af-south-1:238384257742:image/sagemaker-distribution-cpu     | arn:aws:sagemaker:af-south-1:238384257742:image/sagemaker-distribution-gpu     |
| ap-east-1      | arn:aws:sagemaker:ap-east-1:523751269255:image/sagemaker-distribution-cpu      | arn:aws:sagemaker:ap-east-1:523751269255:image/sagemaker-distribution-gpu      |
| ap-south-1     | arn:aws:sagemaker:ap-south-1:245090515133:image/sagemaker-distribution-cpu     | arn:aws:sagemaker:ap-south-1:245090515133:image/sagemaker-distribution-gpu     |
| ap-northeast-2 | arn:aws:sagemaker:ap-northeast-2:064688005998:image/sagemaker-distribution-cpu | arn:aws:sagemaker:ap-northeast-2:064688005998:image/sagemaker-distribution-gpu |
| ap-southeast-1 | arn:aws:sagemaker:ap-southeast-1:022667117163:image/sagemaker-distribution-cpu | arn:aws:sagemaker:ap-southeast-1:022667117163:image/sagemaker-distribution-gpu |
| ap-southeast-2 | arn:aws:sagemaker:ap-southeast-2:648430277019:image/sagemaker-distribution-cpu | arn:aws:sagemaker:ap-southeast-2:648430277019:image/sagemaker-distribution-gpu |
| ap-northeast-1 | arn:aws:sagemaker:ap-northeast-1:010972774902:image/sagemaker-distribution-cpu | arn:aws:sagemaker:ap-northeast-1:010972774902:image/sagemaker-distribution-gpu |
| ca-central-1   | arn:aws:sagemaker:ca-central-1:481561238223:image/sagemaker-distribution-cpu   | arn:aws:sagemaker:ca-central-1:481561238223:image/sagemaker-distribution-gpu   |
| eu-central-1   | arn:aws:sagemaker:eu-central-1:545423591354:image/sagemaker-distribution-cpu   | arn:aws:sagemaker:eu-central-1:545423591354:image/sagemaker-distribution-gpu   |
| eu-west-1      | arn:aws:sagemaker:eu-west-1:819792524951:image/sagemaker-distribution-cpu      | arn:aws:sagemaker:eu-west-1:819792524951:image/sagemaker-distribution-gpu      |
| eu-west-2      | arn:aws:sagemaker:eu-west-2:021081402939:image/sagemaker-distribution-cpu      | arn:aws:sagemaker:eu-west-2:021081402939:image/sagemaker-distribution-gpu      |
| eu-west-3      | arn:aws:sagemaker:eu-west-3:856416204555:image/sagemaker-distribution-cpu      | arn:aws:sagemaker:eu-west-3:856416204555:image/sagemaker-distribution-gpu      |
| eu-north-1     | arn:aws:sagemaker:eu-north-1:175620155138:image/sagemaker-distribution-cpu     | arn:aws:sagemaker:eu-north-1:175620155138:image/sagemaker-distribution-gpu     |
| eu-south-1     | arn:aws:sagemaker:eu-south-1:810671768855:image/sagemaker-distribution-cpu     | arn:aws:sagemaker:eu-south-1:810671768855:image/sagemaker-distribution-gpu     |
| sa-east-1      | arn:aws:sagemaker:sa-east-1:567556641782:image/sagemaker-distribution-cpu      | arn:aws:sagemaker:sa-east-1:567556641782:image/sagemaker-distribution-gpu      |
| ap-northeast-3 | arn:aws:sagemaker:ap-northeast-3:564864627153:image/sagemaker-distribution-cpu | arn:aws:sagemaker:ap-northeast-3:564864627153:image/sagemaker-distribution-gpu |
| ap-southeast-3 | arn:aws:sagemaker:ap-southeast-3:370607712162:image/sagemaker-distribution-cpu | arn:aws:sagemaker:ap-southeast-3:370607712162:image/sagemaker-distribution-gpu |
| me-south-1     | arn:aws:sagemaker:me-south-1:523774347010:image/sagemaker-distribution-cpu     | arn:aws:sagemaker:me-south-1:523774347010:image/sagemaker-distribution-gpu     |
| me-central-1   | arn:aws:sagemaker:me-central-1:358593528301:image/sagemaker-distribution-cpu   | arn:aws:sagemaker:me-central-1:358593528301:image/sagemaker-distribution-gpu   |
| il-central-1   | arn:aws:sagemaker:il-central-1:080319125002:image/sagemaker-distribution-cpu   | arn:aws:sagemaker:il-central-1:080319125002:image/sagemaker-distribution-gpu   |
| cn-north-1     | arn:aws:sagemaker:cn-north-1:674439102856:image/sagemaker-distribution-cpu     | arn:aws:sagemaker:cn-north-1:674439102856:image/sagemaker-distribution-gpu     |
| cn-northwest-1 | arn:aws:sagemaker:cn-northwest-1:651871951035:image/sagemaker-distribution-cpu | arn:aws:sagemaker:cn-northwest-1:651871951035:image/sagemaker-distribution-gpu |
| us-gov-west-1  | arn:aws:sagemaker:us-gov-west-1:300992924816:image/sagemaker-distribution-cpu  | arn:aws:sagemaker:us-gov-west-1:300992924816:image/sagemaker-distribution-gpu  |
| us-gov-east-1  | arn:aws:sagemaker:us-gov-east-1:300993876623:image/sagemaker-distribution-cpu  | arn:aws:sagemaker:us-gov-east-1:300993876623:image/sagemaker-distribution-gpu  |

If you encounter instance limits, contact your administrator. To get more storage and
compute for a user, administrators can request an increase to a user's AWS quotas. For
more information about requesting a quota increase, see [Amazon SageMaker AI endpoints and quotas](../../../general/latest/gr/sagemaker.md "../../../general/latest/gr/sagemaker.md").
