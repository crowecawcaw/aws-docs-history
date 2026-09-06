

# ECR repository for GuardDuty agent on ECS-EC2 Bottlerocket
<a name="ecs-ec2-bottlerocket-runtime-agent-ecr-image-uri"></a>

On Bottlerocket Amazon ECS-Amazon EC2 instances, the GuardDuty security agent runs as a host container. The agent container image is hosted in Amazon ECR. For information about prerequisites including network connectivity and required IAM permissions, see [Prerequisites for ECS-EC2 Bottlerocket support](prereq-runtime-monitoring-ecs-ec2-bottlerocket-support.md). The instance profile must include the `AmazonSSMManagedInstanceCore` and `AmazonEC2ContainerRegistryReadOnly` managed policies.

The following table shows the Amazon ECR repositories that host the GuardDuty agent for Amazon ECS-Amazon EC2 Bottlerocket instances for each AWS Region.


| **AWS Region** | **Amazon ECR repository URI** | 
| --- | --- | 
| US East (N. Virginia) | `593207742271.dkr.ecr.us-east-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| US East (Ohio) | `307168627858.dkr.ecr.us-east-2.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| US West (N. California) | `684579721401.dkr.ecr.us-west-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| US West (Oregon) | `733349766148.dkr.ecr.us-west-2.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Europe (Ireland) | `694911143906.dkr.ecr.eu-west-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Europe (London) | `892757235363.dkr.ecr.eu-west-2.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Europe (Paris) | `665651866788.dkr.ecr.eu-west-3.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Europe (Frankfurt) | `323658145986.dkr.ecr.eu-central-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Europe (Zurich) | `529164026651.dkr.ecr.eu-central-2.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Europe (Stockholm) | `591436053604.dkr.ecr.eu-north-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Europe (Milan) | `266869475730.dkr.ecr.eu-south-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Europe (Spain) | `919611009337.dkr.ecr.eu-south-2.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Tokyo) | `533107202818.dkr.ecr.ap-northeast-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Seoul) | `914738172881.dkr.ecr.ap-northeast-2.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Osaka) | `273192626886.dkr.ecr.ap-northeast-3.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Singapore) | `174946120834.dkr.ecr.ap-southeast-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Sydney) | `005257825471.dkr.ecr.ap-southeast-2.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Jakarta) | `510637619217.dkr.ecr.ap-southeast-3.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Melbourne) | `251357961535.dkr.ecr.ap-southeast-4.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Mumbai) | `251508486986.dkr.ecr.ap-south-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Hyderabad) | `950823858135.dkr.ecr.ap-south-2.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Hong Kong) | `258348409381.dkr.ecr.ap-east-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Canada (Central) | `354763396469.dkr.ecr.ca-central-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Canada West (Calgary) | `339712888787.dkr.ecr.ca-west-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| South America (São Paulo) | `758426053663.dkr.ecr.sa-east-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Middle East (Bahrain) | `536382113932.dkr.ecr.me-south-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Middle East (UAE) | `000014521398.dkr.ecr.me-central-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Africa (Cape Town) | `197869348890.dkr.ecr.af-south-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Israel (Tel Aviv) | `870907303882.dkr.ecr.il-central-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Malaysia) | `156041399949.dkr.ecr.ap-southeast-5.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Thailand) | `054037130133.dkr.ecr.ap-southeast-7.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Mexico (Central) | `311141559934.dkr.ecr.mx-central-1.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 
| Asia Pacific (Taipei) | `259886477082.dkr.ecr.ap-east-2.amazonaws.com/aws-guardduty-agent-ecs-ec2` | 