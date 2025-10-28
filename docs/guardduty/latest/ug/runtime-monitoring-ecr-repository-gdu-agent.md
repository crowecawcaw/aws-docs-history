# Amazon ECR repository hosting GuardDuty

agent

The following sections list the Amazon Elastic Container Registry (Amazon ECR) repositories where GuardDuty hosts the security
agent that gets deployed on your Amazon EKS and Amazon ECS clusters.

The prerequisite to [Prerequisites for container image access](prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs "prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs") requires you to provide a task execution
role that has certain Amazon Elastic Container Registry (Amazon ECR) permissions. To further restrict these permissions, you
can add the Amazon ECR repository URI that hosts the GuardDuty agent for Fargate-Amazon ECS resources.

###### Contents

When you enable GuardDuty automated
configuration for Runtime Monitoring for EKS, GuardDuty will deploy this agent version to your Amazon EKS clusters. For information about
enabling automated agent, see [Managing security agent automatically
for Amazon EKS resources](managing-gdu-agent-eks-automatically.md "managing-gdu-agent-eks-automatically.md").

The following table shows the Amazon ECR repository URIs where the GuardDuty security agent versions
`1.11.0.eks.build.2`, `1.10.0.eks.build.2`, `1.9.0.eks.build.2`,
and `1.8.0.eks.build.2` for Amazon EKS are hosted.

| AWS Region                                          | Amazon ECR repository URI                                                       |
| --------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US West (Oregon)                                    | `602401143452.dkr.ecr.us-west-2.amazonaws.com`                                  |
| `039403964562.dkr.ecr.us-west-2.amazonaws.com`      |
| Europe (Paris)                                      | `602401143452.dkr.ecr.eu-west-3.amazonaws.com`                                  |
| `113643092156.dkr.ecr.eu-west-3.amazonaws.com`      |
| Asia Pacific (Mumbai)                               | `602401143452.dkr.ecr.ap-south-1.amazonaws.com`                                 |
| `610108029387.dkr.ecr.ap-south-1.amazonaws.com`     |
| Asia Pacific (Hyderabad)                            | `900889452093.dkr.ecr.ap-south-2.amazonaws.com`                                 |
| `618745550137.dkr.ecr.ap-south-2.amazonaws.com`     |
| Canada (Central)                                    | `602401143452.dkr.ecr.ca-central-1.amazonaws.com`                               |
| `001188825231.dkr.ecr.ca-central-1.amazonaws.com`   |
| Canada West (Calgary)                               | `761377655185.dkr.ecr.ca-west-1.amazonaws.com`                                  |
| –                                                   |
| Middle East (UAE)                                   | `759879836304.dkr.ecr.me-central-1.amazonaws.com`                               |
| `601769779514.dkr.ecr.me-central-1.amazonaws.com`   |
| Europe (London)                                     | `602401143452.dkr.ecr.eu-west-2.amazonaws.com`                                  |
| `109118265657.dkr.ecr.eu-west-2.amazonaws.com`      |
| US West (N. California)                             | `602401143452.dkr.ecr.us-west-1.amazonaws.com`                                  |
| `373421517865.dkr.ecr.us-west-1.amazonaws.com`      |
| US East (N. Virginia)                               | `602401143452.dkr.ecr.us-east-1.amazonaws.com`                                  |
| `031903291036.dkr.ecr.us-east-1.amazonaws.com`      |
| US East (Ohio)                                      | `602401143452.dkr.ecr.us-east-2.amazonaws.com`                                  |
| `591382732059.dkr.ecr.us-east-2.amazonaws.com`      |
| Europe (Ireland)                                    | `602401143452.dkr.ecr.eu-west-1.amazonaws.com`                                  |
| `673884943994.dkr.ecr.eu-west-1.amazonaws.com`      |
| South America (São Paulo)                           | `602401143452.dkr.ecr.sa-east-1.amazonaws.com`                                  |
| `941219317354.dkr.ecr.sa-east-1.amazonaws.com`      |
| Europe (Stockholm)                                  | `602401143452.dkr.ecr.eu-north-1.amazonaws.com`                                 |
| `366771026645.dkr.ecr.eu-north-1.amazonaws.com`     |
| Europe (Frankfurt)                                  | `602401143452.dkr.ecr.eu-central-1.amazonaws.com`                               |
| `409493279830.dkr.ecr.eu-central-1.amazonaws.com`   |
| Europe (Zurich)                                     | `900612956339.dkr.ecr.eu-central-2.amazonaws.com`                               |
| `718440343717.dkr.ecr.eu-central-2.amazonaws.com`   |
| Asia Pacific (Singapore)                            | `602401143452.dkr.ecr.ap-southeast-1.amazonaws.com`                             |
| `584580519942.dkr.ecr.ap-southeast-1.amazonaws.com` |
| Asia Pacific (Sydney)                               | `602401143452.dkr.ecr.ap-southeast-2.amazonaws.com`                             |
| `011662287384.dkr.ecr.ap-southeast-2.amazonaws.com` |
| Asia Pacific (Jakarta)                              | `296578399912.dkr.ecr.ap-southeast-3.amazonaws.com`                             |
| `617474730032.dkr.ecr.ap-southeast-3.amazonaws.com` |
| Asia Pacific (Tokyo)                                | `602401143452.dkr.ecr.ap-northeast-1.amazonaws.com`                             |
| `781592569369.dkr.ecr.ap-northeast-1.amazonaws.com` |
| Asia Pacific (Seoul)                                | `602401143452.dkr.ecr.ap-northeast-2.amazonaws.com`                             |
| `732248494576.dkr.ecr.ap-northeast-2.amazonaws.com` |
| Asia Pacific (Osaka)                                | `602401143452.dkr.ecr.ap-northeast-3.amazonaws.com`                             |
| `810724417379.dkr.ecr.ap-northeast-3.amazonaws.com` |
| Asia Pacific (Hong Kong)                            | `800184023465.dkr.ecr.ap-east-1.amazonaws.com`                                  |
| `790429075973.dkr.ecr.ap-east-1.amazonaws.com`      |
| Middle East (Bahrain)                               | `558608220178.dkr.ecr.me-south-1.amazonaws.com`                                 |
| `541829937850.dkr.ecr.me-south-1.amazonaws.com`     |
| Europe (Milan)                                      | `590381155156.dkr.ecr.eu-south-1.amazonaws.com`                                 |
| `528450769569.dkr.ecr.eu-south-1.amazonaws.com`     |
| Europe (Spain)                                      | `455263428931.dkr.ecr.eu-south-2.amazonaws.com`                                 |
| `531047660167.dkr.ecr.eu-south-2.amazonaws.com`     |
| Africa (Cape Town)                                  | `877085696533.dkr.ecr.af-south-1.amazonaws.com`                                 |
| `379032919888.dkr.ecr.af-south-1.amazonaws.com`     |
| Asia Pacific (Melbourne)                            | `491585149902.dkr.ecr.ap-southeast-4.amazonaws.com`                             |
| `750462861327.dkr.ecr.ap-southeast-4.amazonaws.com` |
| Israel (Tel Aviv)                                   | `066635153087.dkr.ecr.il-central-1.amazonaws.com`                               |
| `292660727137.dkr.ecr.il-central-1.amazonaws.com`   |
| Asia Pacific (Malaysia)                             | `151610086707.dkr.ecr.ap-southeast-5.amazonaws.com`                             |
| Asia Pacific (Thailand)                             | `121268973566.dkr.ecr.ap-southeast-7.amazonaws.com`                             |
| Mexico (Central)                                    | `730335286997.dkr.ecr.mx-central-1.amazonaws.com`                               |
| Asia Pacific (Taipei)                               | `533267051163.dkr.ecr.ap-east-2.amazonaws.com`                                  | This section provides the Amazon ECR repository for the Amazon EKS agent version **1.8.1 (v1.8.1-eks-build.1)**. If you're using v1.8.1-eks-build.1, GuardDuty recommends switching to the default agent version which is usually the latest agent version. To do so, identify the latest agent from [Released agent versions for Amazon EKS resources](runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history "runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history"), and then perform the steps in [Updating security agent manually for Amazon EKS resources](eksrunmon-update-security-agent.md "eksrunmon-update-security-agent.md"). The following table shows the Amazon ECR repository URIs where GuardDuty security agent version `1.8.1-eks-build.1` for Amazon EKS is hosted. |
| **AWS Region**                                      | **Amazon ECR repository URI**                                                   |
| ---                                                 | ---                                                                             |
| US West (Oregon)                                    | `039403964562.dkr.ecr.us-west-2.amazonaws.com`                                  |
| Europe (Paris)                                      | `113643092156.dkr.ecr.eu-west-3.amazonaws.com`                                  |
| Asia Pacific (Mumbai)                               | `610108029387.dkr.ecr.ap-south-1.amazonaws.com`                                 |
| Asia Pacific (Hyderabad)                            | `618745550137.dkr.ecr.ap-south-2.amazonaws.com`                                 |
| Canada (Central)                                    | `001188825231.dkr.ecr.ca-central-1.amazonaws.com`                               |
| Middle East (UAE)                                   | `601769779514.dkr.ecr.me-central-1.amazonaws.com`                               |
| Europe (London)                                     | `109118265657.dkr.ecr.eu-west-2.amazonaws.com`                                  |
| US West (N. California)                             | `373421517865.dkr.ecr.us-west-1.amazonaws.com`                                  |
| US East (N. Virginia)                               | `031903291036.dkr.ecr.us-east-1.amazonaws.com`                                  |
| US East (Ohio)                                      | `591382732059.dkr.ecr.us-east-2.amazonaws.com`                                  |
| Europe (Ireland)                                    | `673884943994.dkr.ecr.eu-west-1.amazonaws.com`                                  |
| South America (São Paulo)                           | `941219317354.dkr.ecr.sa-east-1.amazonaws.com`                                  |
| Europe (Stockholm)                                  | `366771026645.dkr.ecr.eu-north-1.amazonaws.com`                                 |
| Europe (Frankfurt)                                  | `409493279830.dkr.ecr.eu-central-1.amazonaws.com`                               |
| Europe (Zurich)                                     | `718440343717.dkr.ecr.eu-central-2.amazonaws.com`                               |
| Asia Pacific (Singapore)                            | `584580519942.dkr.ecr.ap-southeast-1.amazonaws.com`                             |
| Asia Pacific (Sydney)                               | `011662287384.dkr.ecr.ap-southeast-2.amazonaws.com`                             |
| Asia Pacific (Jakarta)                              | `617474730032.dkr.ecr.ap-southeast-3.amazonaws.com`                             |
| Asia Pacific (Tokyo)                                | `781592569369.dkr.ecr.ap-northeast-1.amazonaws.com`                             |
| Asia Pacific (Seoul)                                | `732248494576.dkr.ecr.ap-northeast-2.amazonaws.com`                             |
| Asia Pacific (Osaka)                                | `810724417379.dkr.ecr.ap-northeast-3.amazonaws.com`                             |
| Asia Pacific (Hong Kong)                            | `790429075973.dkr.ecr.ap-east-1.amazonaws.com`                                  |
| Middle East (Bahrain)                               | `541829937850.dkr.ecr.me-south-1.amazonaws.com`                                 |
| Europe (Milan)                                      | `528450769569.dkr.ecr.eu-south-1.amazonaws.com`                                 |
| Europe (Spain)                                      | `531047660167.dkr.ecr.eu-south-2.amazonaws.com`                                 |
| Africa (Cape Town)                                  | `379032919888.dkr.ecr.af-south-1.amazonaws.com`                                 |
| Asia Pacific (Melbourne)                            | `750462861327.dkr.ecr.ap-southeast-4.amazonaws.com`                             |
| Israel (Tel Aviv)                                   | `292660727137.dkr.ecr.il-central-1.amazonaws.com`                               | As a prerequisite to using Runtime Monitoring for Amazon ECS-Fargate, you must [Prerequisites for container image access](prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs "prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs"). The GuardDuty agent sidecar container image is stored in Amazon ECR, with its image layers stored in Amazon S3. For more information, see [How Runtime Monitoring works with Fargate (Amazon ECS only)](how-runtime-monitoring-works-ecs-fargate.md "how-runtime-monitoring-works-ecs-fargate.md"). The following table shows the Amazon ECR repositories that hosts the GuardDuty agent for AWS Fargate (Amazon ECS only) for each AWS Region.                                                                                                                       |
| **AWS Region**                                      | **Amazon ECR repository URI**                                                   |
| ---                                                 | ---                                                                             |
| US West (Oregon)                                    | `733349766148.dkr.ecr.us-west-2.amazonaws.com/aws-guardduty-agent-fargate`      |
| Europe (Paris)                                      | `665651866788.dkr.ecr.eu-west-3.amazonaws.com/aws-guardduty-agent-fargate`      |
| Asia Pacific (Mumbai)                               | `251508486986.dkr.ecr.ap-south-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Asia Pacific (Hyderabad)                            | `950823858135.dkr.ecr.ap-south-2.amazonaws.com/aws-guardduty-agent-fargate`     |
| Canada (Central)                                    | `354763396469.dkr.ecr.ca-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Middle East (UAE)                                   | `000014521398.dkr.ecr.me-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Europe (London)                                     | `892757235363.dkr.ecr.eu-west-2.amazonaws.com/aws-guardduty-agent-fargate`      |
| US West (N. California)                             | `684579721401.dkr.ecr.us-west-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| US East (N. Virginia)                               | `593207742271.dkr.ecr.us-east-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| US East (Ohio)                                      | `307168627858.dkr.ecr.us-east-2.amazonaws.com/aws-guardduty-agent-fargate`      |
| Europe (Ireland)                                    | `694911143906.dkr.ecr.eu-west-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| South America (São Paulo)                           | `758426053663.dkr.ecr.sa-east-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| Europe (Stockholm)                                  | `591436053604.dkr.ecr.eu-north-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Europe (Frankfurt)                                  | `323658145986.dkr.ecr.eu-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Europe (Zurich)                                     | `529164026651.dkr.ecr.eu-central-2.amazonaws.com/aws-guardduty-agent-fargate`   |
| Asia Pacific (Singapore)                            | `174946120834.dkr.ecr.ap-southeast-1.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Sydney)                               | `005257825471.dkr.ecr.ap-southeast-2.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Jakarta)                              | `510637619217.dkr.ecr.ap-southeast-3.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Tokyo)                                | `533107202818.dkr.ecr.ap-northeast-1.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Seoul)                                | `914738172881.dkr.ecr.ap-northeast-2.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Osaka)                                | `273192626886.dkr.ecr.ap-northeast-3.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Hong Kong)                            | `258348409381.dkr.ecr.ap-east-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| Middle East (Bahrain)                               | `536382113932.dkr.ecr.me-south-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Europe (Milan)                                      | `266869475730.dkr.ecr.eu-south-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Europe (Spain)                                      | `919611009337.dkr.ecr.eu-south-2.amazonaws.com/aws-guardduty-agent-fargate`     |
| Africa (Cape Town)                                  | `197869348890.dkr.ecr.af-south-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Asia Pacific (Melbourne)                            | `251357961535.dkr.ecr.ap-southeast-4.amazonaws.com/aws-guardduty-agent-fargate` |
| Israel (Tel Aviv)                                   | `870907303882.dkr.ecr.il-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Asia Pacific (Malaysia)                             | `156041399949.dkr.ecr.ap-southeast-5.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Thailand)                             | `054037130133.dkr.ecr.ap-southeast-7.amazonaws.com/aws-guardduty-agent-fargate` |
| Canada West (Calgary)                               | `339712888787.dkr.ecr.ca-west-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| Mexico (Central)                                    | `311141559934.dkr.ecr.mx-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Asia Pacific (Taipei)                               | `259886477082.dkr.ecr.ap-east-2.amazonaws.com/aws-guardduty-agent-fargate`      |
