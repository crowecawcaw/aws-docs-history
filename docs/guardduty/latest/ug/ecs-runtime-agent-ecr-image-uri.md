# ECR Repository for GuardDuty agent on AWS Fargate

(Amazon ECS only)

As a prerequisite to using Runtime Monitoring for Amazon ECS-Fargate, you must
[Prerequisites for container image access](prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs "prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs"). The GuardDuty
agent sidecar container image is stored in Amazon ECR, with its image layers stored in Amazon S3. For more information, see
[How Runtime Monitoring works with Fargate
(Amazon ECS only)](how-runtime-monitoring-works-ecs-fargate.md "how-runtime-monitoring-works-ecs-fargate.md").

The following table shows the Amazon ECR repositories that hosts the GuardDuty agent for
AWS Fargate (Amazon ECS only) for each AWS Region.

| **AWS Region**            | **Amazon ECR repository<br>URI**                                                |
| ------------------------- | ------------------------------------------------------------------------------- |
| US West (Oregon)          | `733349766148.dkr.ecr.us-west-2.amazonaws.com/aws-guardduty-agent-fargate`      |
| Europe (Paris)            | `665651866788.dkr.ecr.eu-west-3.amazonaws.com/aws-guardduty-agent-fargate`      |
| Asia Pacific (Mumbai)     | `251508486986.dkr.ecr.ap-south-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Asia Pacific (Hyderabad)  | `950823858135.dkr.ecr.ap-south-2.amazonaws.com/aws-guardduty-agent-fargate`     |
| Canada (Central)          | `354763396469.dkr.ecr.ca-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Middle East (UAE)         | `000014521398.dkr.ecr.me-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Europe (London)           | `892757235363.dkr.ecr.eu-west-2.amazonaws.com/aws-guardduty-agent-fargate`      |
| US West (N. California)   | `684579721401.dkr.ecr.us-west-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| US East (N. Virginia)     | `593207742271.dkr.ecr.us-east-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| US East (Ohio)            | `307168627858.dkr.ecr.us-east-2.amazonaws.com/aws-guardduty-agent-fargate`      |
| Europe (Ireland)          | `694911143906.dkr.ecr.eu-west-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| South America (São Paulo) | `758426053663.dkr.ecr.sa-east-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| Europe (Stockholm)        | `591436053604.dkr.ecr.eu-north-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Europe (Frankfurt)        | `323658145986.dkr.ecr.eu-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Europe (Zurich)           | `529164026651.dkr.ecr.eu-central-2.amazonaws.com/aws-guardduty-agent-fargate`   |
| Asia Pacific (Singapore)  | `174946120834.dkr.ecr.ap-southeast-1.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Sydney)     | `005257825471.dkr.ecr.ap-southeast-2.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Jakarta)    | `510637619217.dkr.ecr.ap-southeast-3.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Tokyo)      | `533107202818.dkr.ecr.ap-northeast-1.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Seoul)      | `914738172881.dkr.ecr.ap-northeast-2.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Osaka)      | `273192626886.dkr.ecr.ap-northeast-3.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Hong Kong)  | `258348409381.dkr.ecr.ap-east-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| Middle East (Bahrain)     | `536382113932.dkr.ecr.me-south-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Europe (Milan)            | `266869475730.dkr.ecr.eu-south-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Europe (Spain)            | `919611009337.dkr.ecr.eu-south-2.amazonaws.com/aws-guardduty-agent-fargate`     |
| Africa (Cape Town)        | `197869348890.dkr.ecr.af-south-1.amazonaws.com/aws-guardduty-agent-fargate`     |
| Asia Pacific (Melbourne)  | `251357961535.dkr.ecr.ap-southeast-4.amazonaws.com/aws-guardduty-agent-fargate` |
| Israel (Tel Aviv)         | `870907303882.dkr.ecr.il-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Asia Pacific (Malaysia)   | `156041399949.dkr.ecr.ap-southeast-5.amazonaws.com/aws-guardduty-agent-fargate` |
| Asia Pacific (Thailand)   | `054037130133.dkr.ecr.ap-southeast-7.amazonaws.com/aws-guardduty-agent-fargate` |
| Canada West (Calgary)     | `339712888787.dkr.ecr.ca-west-1.amazonaws.com/aws-guardduty-agent-fargate`      |
| Mexico (Central)          | `311141559934.dkr.ecr.mx-central-1.amazonaws.com/aws-guardduty-agent-fargate`   |
| Asia Pacific (Taipei)     | `259886477082.dkr.ecr.ap-east-2.amazonaws.com/aws-guardduty-agent-fargate`      |
