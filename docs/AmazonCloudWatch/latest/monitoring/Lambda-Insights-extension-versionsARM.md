# ARM64 platforms

This section lists the versions of the Lambda Insights extension for ARM64 platforms, and the ARNs to use
for these extensions in each AWS Region.

###### Important

Lambda Insights extensions 1.0.317.0 and later don't support Amazon Linux 1.

## 1.0.660.0

Version 1.0.660.0 includes Lambda Insights extension support for Lambda functions running on Lambda Managed Instances. For functions running on Lambda Managed Instances, the extension will send an EMF log event once every minute, creating 12 CloudWatch Metrics at one-minute granularity.

| Region                     | ARN                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| US East (N. Virginia)      | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:31`           |
| US East (Ohio)             | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:33`           |
| US West (N. California)    | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:29`           |
| US West (Oregon)           | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:31`           |
| Africa (Cape Town)         | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:30`          |
| Asia Pacific (Hong Kong)   | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:30`           |
| Asia Pacific (Hyderabad)   | `arn:aws:lambda:ap-south-2:891564319516:layer:LambdaInsightsExtension-Arm64:18`          |
| Asia Pacific (Jakarta)     | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:30`      |
| Asia Pacific (Malaysia)    | `arn:aws:lambda:ap-southeast-5:590183865173:layer:LambdaInsightsExtension-Arm64:7`       |
| Asia Pacific (Melbourne)   | `arn:aws:lambda:ap-southeast-4:158895979263:layer:LambdaInsightsExtension-Arm64:7`       |
| Asia Pacific (Mumbai)      | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:33`          |
| Asia Pacific (New Zealand) | `arn:aws:lambda:ap-southeast-6:727646510379:layer:LambdaInsightsExtension-Arm64:165`     |
| Asia Pacific (Osaka)       | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:28`      |
| Asia Pacific (Seoul)       | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:30`      |
| Asia Pacific (Singapore)   | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:31`      |
| Asia Pacific (Sydney)      | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:31`      |
| Asia Pacific (Taipei)      | `arn:aws:lambda:ap-east-2:145023102084:layer:LambdaInsightsExtension-Arm64:7`            |
| Asia Pacific (Thailand)    | `arn:aws:lambda:ap-southeast-7:761018874580:layer:LambdaInsightsExtension-Arm64:7`       |
| Asia Pacific (Tokyo)       | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:42`      |
| Canada (Central)           | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:29`        |
| Canada West (Calgary)      | `arn:aws:lambda:ca-west-1:946466191631:layer:LambdaInsightsExtension-Arm64:7`            |
| China (Beijing)            | `arn:aws-cn:lambda:cn-north-1:488211338238:layer:LambdaInsightsExtension-Arm64:4`        |
| China (Ningxia)            | `arn:aws-cn:lambda:cn-northwest-1:488211338238:layer:LambdaInsightsExtension-Arm64:4`    |
| Europe (Frankfurt)         | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:31`        |
| Europe (Ireland)           | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:31`           |
| Europe (London)            | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:31`           |
| Europe (Milan)             | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:30`          |
| Europe (Paris)             | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:29`           |
| Europe (Spain)             | `arn:aws:lambda:eu-south-2:352183217350:layer:LambdaInsightsExtension-Arm64:18`          |
| Europe (Stockholm)         | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:29`          |
| Europe (Zurich)            | `arn:aws:lambda:eu-central-2:033019950311:layer:LambdaInsightsExtension-Arm64:7`         |
| Israel (Tel Aviv)          | `arn:aws:lambda:il-central-1:459530977127:layer:LambdaInsightsExtension-Arm64:7`         |
| Mexico (Central)           | `arn:aws:lambda:mx-central-1:879381266642:layer:LambdaInsightsExtension-Arm64:7`         |
| Middle East (Bahrain)      | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:30`          |
| Middle East (UAE)          | `arn:aws:lambda:me-central-1:732604637566:layer:LambdaInsightsExtension-Arm64:7`         |
| South America (São Paulo)  | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:29`           |
| AWS GovCloud (US-East)     | `arn:aws-us-gov:lambda:us-gov-east-1:122132214140:layer:LambdaInsightsExtension-Arm64:6` |
| AWS GovCloud (US-West)     | `arn:aws-us-gov:lambda:us-gov-west-1:751350123760:layer:LambdaInsightsExtension-Arm64:6` |

## 1.0.498.0

Version 1.0.498.0 includes bug fixes and performance improvements.

| Region                    | ARN                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:27`           |
| US East (Ohio)            | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:29`           |
| US West (N. California)   | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:25`           |
| US West (Oregon)          | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:27`           |
| Africa (Cape Town)        | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:26`          |
| Asia Pacific (Hong Kong)  | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:26`           |
| Asia Pacific (Mumbai)     | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:29`          |
| Asia Pacific (Hyderabad)  | `arn:aws:lambda:ap-south-2:891564319516:layer:LambdaInsightsExtension-Arm64:14`          |
| Asia Pacific (Singapore)  | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:27`      |
| Asia Pacific (Sydney)     | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:27`      |
| Asia Pacific (Jakarta)    | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:26`      |
| Asia Pacific (Melbourne)  | `arn:aws:lambda:ap-southeast-4:158895979263:layer:LambdaInsightsExtension-Arm64:3`       |
| Asia Pacific (Malaysia)   | `arn:aws:lambda:ap-southeast-5:590183865173:layer:LambdaInsightsExtension-Arm64:3`       |
| Asia Pacific (Thailand)   | `arn:aws:lambda:ap-southeast-7:761018874580:layer:LambdaInsightsExtension-Arm64:2`       |
| Asia Pacific (Tokyo)      | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:38`      |
| Asia Pacific (Seoul)      | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:26`      |
| Asia Pacific (Osaka)      | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:24`      |
| Canada (Central)          | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:25`        |
| Canada West (Calgary)     | `arn:aws:lambda:ca-west-1:946466191631:layer:LambdaInsightsExtension-Arm64:3`            |
| Europe (Frankfurt)        | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:27`        |
| Europe (Zurich)           | `arn:aws:lambda:eu-central-2:033019950311:layer:LambdaInsightsExtension-Arm64:3`         |
| Europe (Ireland)          | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:27`           |
| Europe (London)           | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:27`           |
| Europe (Paris)            | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:25`           |
| Europe (Stockholm)        | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:25`          |
| Europe (Milan)            | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:26`          |
| Europe (Spain)            | `arn:aws:lambda:eu-south-2:352183217350:layer:LambdaInsightsExtension-Arm64:14`          |
| Israel (Tel Aviv)         | `arn:aws:lambda:il-central-1:459530977127:layer:LambdaInsightsExtension-Arm64:3`         |
| Mexico (Central)          | `arn:aws:lambda:mx-central-1:879381266642:layer:LambdaInsightsExtension-Arm64:2`         |
| Middle East (Bahrain)     | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:26`          |
| Middle East (UAE)         | `arn:aws:lambda:me-central-1:732604637566:layer:LambdaInsightsExtension-Arm64:3`         |
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:25`           |
| China (Beijing)           | `arn:aws-cn:lambda:cn-north-1:488211338238:layer:LambdaInsightsExtension-Arm64:1`        |
| China (Ningxia)           | `arn:aws-cn:lambda:cn-northwest-1:488211338238:layer:LambdaInsightsExtension-Arm64:1`    |
| AWS GovCloud (US-East)    | `arn:aws-us-gov:lambda:us-gov-east-1:122132214140:layer:LambdaInsightsExtension-Arm64:6` |
| AWS GovCloud (US-West)    | `arn:aws-us-gov:lambda:us-gov-west-1:751350123760:layer:LambdaInsightsExtension-Arm64:6` |

## 1.0.404.0

Version 1.0.404.0 reduces the binary size of the Lambda Insights extension from ~9MB to ~5MB, and subsequently reduces the zip size of the Lambda Insights extension layer from ~3,7MB to ~2.5MB. It also
reduces the overall memory consumption of the agent from ~11MB to ~7MB.

| Region                    | ARN                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:23`           |
| US East (Ohio)            | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:25`           |
| US West (N. California)   | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:21`           |
| US West (Oregon)          | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:23`           |
| Africa (Cape Town)        | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:21`          |
| Asia Pacific (Hong Kong)  | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:21`           |
| Asia Pacific (Hyderabad)  | `arn:aws:lambda:ap-south-2:891564319516:layer:LambdaInsightsExtension-Arm64:9`           |
| Asia Pacific (Jakarta)    | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:21`      |
| Asia Pacific (Mumbai)     | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:25`          |
| Asia Pacific (Osaka)      | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:20`      |
| Asia Pacific (Seoul)      | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:22`      |
| Asia Pacific (Singapore)  | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:23`      |
| Asia Pacific (Sydney)     | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:23`      |
| Asia Pacific (Tokyo)      | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:34`      |
| Canada (Central)          | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:21`        |
| Europe (Frankfurt)        | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:23`        |
| Europe (Ireland)          | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:23`           |
| Europe (London)           | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:23`           |
| Europe (Milan)            | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:21`          |
| Europe (Paris)            | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:21`           |
| Europe (Spain)            | `arn:aws:lambda:eu-south-2:352183217350:layer:LambdaInsightsExtension-Arm64:9`           |
| Europe (Stockholm)        | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:21`          |
| Middle East (Bahrain)     | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:21`          |
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:21`           |
| AWS GovCloud (US-East)    | `arn:aws-us-gov:lambda:us-gov-east-1:122132214140:layer:LambdaInsightsExtension-Arm64:6` |
| AWS GovCloud (US-West)    | `arn:aws-us-gov:lambda:us-gov-west-1:751350123760:layer:LambdaInsightsExtension-Arm64:6` |

## 1.0.391.0

###### Important

Version 1.0.391.0 changes how Lambda Insights collects and reports thread usage. In previous versions of the extension, the `threads_max` metric
reported the maximum number of threads running in the process that has the process ID of 1. Starting with version 1.0.391.0, this metric reports the maximum number of threads that were running at any point of
time during the function’s execution, across all processes in the execution environment. This includes the Lambda function's processes, extensions' processes, system/runtime specific processes, and so on.
This makes the `threads_max` metric more comprehensive while assessing the remaining threads left for your use. For more information about thread and process quotas,
see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md").

| Region                    | ARN                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:22`           |
| US East (Ohio)            | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:24`           |
| US West (N. California)   | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:20`           |
| US West (Oregon)          | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:22`           |
| Africa (Cape Town)        | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:20`          |
| Asia Pacific (Hong Kong)  | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:20`           |
| Asia Pacific (Hyderabad)  | `arn:aws:lambda:ap-south-2:891564319516:layer:LambdaInsightsExtension-Arm64:8`           |
| Asia Pacific (Jakarta)    | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:20`      |
| Asia Pacific (Mumbai)     | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:24`          |
| Asia Pacific (Osaka)      | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:19`      |
| Asia Pacific (Seoul)      | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:21`      |
| Asia Pacific (Singapore)  | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:22`      |
| Asia Pacific (Sydney)     | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:22`      |
| Asia Pacific (Tokyo)      | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:33`      |
| Canada (Central)          | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:20`        |
| Europe (Frankfurt)        | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:22`        |
| Europe (Ireland)          | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:22`           |
| Europe (London)           | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:22`           |
| Europe (Milan)            | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:20`          |
| Europe (Paris)            | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:20`           |
| Europe (Spain)            | `arn:aws:lambda:eu-south-2:352183217350:layer:LambdaInsightsExtension-Arm64:8`           |
| Europe (Stockholm)        | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:20`          |
| Middle East (Bahrain)     | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:20`          |
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:20`           |
| AWS GovCloud (US-East)    | `arn:aws-us-gov:lambda:us-gov-east-1:122132214140:layer:LambdaInsightsExtension-Arm64:5` |
| AWS GovCloud (US-West)    | `arn:aws-us-gov:lambda:us-gov-west-1:751350123760:layer:LambdaInsightsExtension-Arm64:5` |

## 1.0.333.0

Version 1.0.333.0 includes bug fixes.

| Region                    | ARN                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:20`           |
| US East (Ohio)            | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:22`           |
| US West (N. California)   | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:18`           |
| US West (Oregon)          | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:20`           |
| Africa (Cape Town)        | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:18`          |
| Asia Pacific (Hong Kong)  | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:18`           |
| Asia Pacific (Hyderabad)  | `arn:aws:lambda:ap-south-2:891564319516:layer:LambdaInsightsExtension-Arm64:6`           |
| Asia Pacific (Jakarta)    | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:18`      |
| Asia Pacific (Mumbai)     | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:22`          |
| Asia Pacific (Osaka)      | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:17`      |
| Asia Pacific (Seoul)      | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:19`      |
| Asia Pacific (Singapore)  | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:20`      |
| Asia Pacific (Sydney)     | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:20`      |
| Asia Pacific (Tokyo)      | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:31`      |
| Canada (Central)          | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:18`        |
| Europe (Frankfurt)        | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:20`        |
| Europe (Ireland)          | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:20`           |
| Europe (London)           | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:20`           |
| Europe (Milan)            | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:18`          |
| Europe (Paris)            | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:18`           |
| Europe (Spain)            | `arn:aws:lambda:eu-south-2:352183217350:layer:LambdaInsightsExtension-Arm64:6`           |
| Europe (Stockholm)        | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:18`          |
| Middle East (Bahrain)     | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:18`          |
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:18`           |
| AWS GovCloud (US-East)    | `arn:aws-us-gov:lambda:us-gov-east-1:122132214140:layer:LambdaInsightsExtension-Arm64:3` |
| AWS GovCloud (US-West)    | `arn:aws-us-gov:lambda:us-gov-west-1:751350123760:layer:LambdaInsightsExtension-Arm64:3` |

## 1.0.317.0

Version 1.0.317.0 includes the removal of support for the Amazon Linux 1 platform, and bug fixes.
It also includes
support for AWS GovCloud (US) Regions.

| Region                    | ARN                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:19`           |
| US East (Ohio)            | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:21`           |
| US West (N. California)   | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:17`           |
| US West (Oregon)          | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:19`           |
| Africa (Cape Town)        | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:17`          |
| Asia Pacific (Hong Kong)  | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:17`           |
| Asia Pacific (Hyderabad)  | `arn:aws:lambda:ap-south-2:891564319516:layer:LambdaInsightsExtension-Arm64:5`           |
| Asia Pacific (Jakarta)    | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:17`      |
| Asia Pacific (Mumbai)     | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:21`          |
| Asia Pacific (Osaka)      | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:16`      |
| Asia Pacific (Seoul)      | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:18`      |
| Asia Pacific (Singapore)  | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:19`      |
| Asia Pacific (Sydney)     | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:19`      |
| Asia Pacific (Tokyo)      | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:30`      |
| Canada (Central)          | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:17`        |
| Europe (Frankfurt)        | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:19`        |
| Europe (Ireland)          | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:19`           |
| Europe (London)           | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:19`           |
| Europe (Milan)            | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:17`          |
| Europe (Paris)            | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:17`           |
| Europe (Spain)            | `arn:aws:lambda:eu-south-2:352183217350:layer:LambdaInsightsExtension-Arm64:5`           |
| Europe (Stockholm)        | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:17`          |
| Middle East (Bahrain)     | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:17`          |
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:17`           |
| AWS GovCloud (US-East)    | `arn:aws-us-gov:lambda:us-gov-east-1:122132214140:layer:LambdaInsightsExtension-Arm64:1` |
| AWS GovCloud (US-West)    | `arn:aws-us-gov:lambda:us-gov-west-1:751350123760:layer:LambdaInsightsExtension-Arm64:1` |

## 1.0.295.0

Version 1.0.295.0 includes dependency updates for all compatible runtimes.

| Region                    | ARN                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------- |
| US East (N. Virginia)     | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:18`      |
| US East (Ohio)            | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:20`      |
| US West (N. California)   | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:16`      |
| US West (Oregon)          | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:18`      |
| Africa (Cape Town)        | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:16`     |
| Asia Pacific (Hong Kong)  | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:16`      |
| Asia Pacific (Hyderabad)  | `arn:aws:lambda:ap-south-2:891564319516:layer:LambdaInsightsExtension-Arm64:4`      |
| Asia Pacific (Jakarta)    | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:16` |
| Asia Pacific (Mumbai)     | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:20`     |
| Asia Pacific (Osaka)      | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:15` |
| Asia Pacific (Seoul)      | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:17` |
| Asia Pacific (Singapore)  | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:18` |
| Asia Pacific (Sydney)     | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:18` |
| Asia Pacific (Tokyo)      | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:29` |
| Canada (Central)          | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:16`   |
| Europe (Frankfurt)        | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:18`   |
| Europe (Ireland)          | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:18`      |
| Europe (London)           | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:18`      |
| Europe (Milan)            | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:16`     |
| Europe (Paris)            | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:16`      |
| Europe (Spain)            | `arn:aws:lambda:eu-south-2:352183217350:layer:LambdaInsightsExtension-Arm64:4`      |
| Europe (Stockholm)        | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:16`     |
| Middle East (Bahrain)     | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:16`     |
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:16`      |

## 1.0.275.0

Version 1.0.275.0 includes bug fixes for all compatible runtimes and support for
the Europe (Spain) and Asia Pacific (Hyderabad) Regions.

| Region                    | ARN                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------- |
| US East (N. Virginia)     | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:16`      |
| US East (Ohio)            | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:18`      |
| US West (N. California)   | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:14`      |
| US West (Oregon)          | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:16`      |
| Africa (Cape Town)        | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:14`     |
| Asia Pacific (Hong Kong)  | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:14`      |
| Asia Pacific (Hyderabad)  | `arn:aws:lambda:ap-south-2:891564319516:layer:LambdaInsightsExtension-Arm64:2`      |
| Asia Pacific (Jakarta)    | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:14` |
| Asia Pacific (Mumbai)     | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:18`     |
| Asia Pacific (Osaka)      | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:13` |
| Asia Pacific (Seoul)      | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:15` |
| Asia Pacific (Singapore)  | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:16` |
| Asia Pacific (Sydney)     | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:16` |
| Asia Pacific (Tokyo)      | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:27` |
| Canada (Central)          | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:14`   |
| Europe (Frankfurt)        | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:16`   |
| Europe (Ireland)          | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:16`      |
| Europe (London)           | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:16`      |
| Europe (Milan)            | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:14`     |
| Europe (Paris)            | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:14`      |
| Europe (Spain)            | `arn:aws:lambda:eu-south-2:352183217350:layer:LambdaInsightsExtension-Arm64:2`      |
| Europe (Stockholm)        | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:14`     |
| Middle East (Bahrain)     | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:14`     |
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:14`      |

## 1.0.273.0

Version 1.0.273.0 includes bug fixes for all compatible runtimes.

| Region                    | ARN                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------- |
| US East (N. Virginia)     | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:12`      |
| US East (Ohio)            | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:14`      |
| US West (N. California)   | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:9`       |
| US West (Oregon)          | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:12`      |
| Africa (Cape Town)        | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:9`      |
| Asia Pacific (Hong Kong)  | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:9`       |
| Asia Pacific (Jakarta)    | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:9`  |
| Asia Pacific (Mumbai)     | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:14`     |
| Asia Pacific (Osaka)      | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:9`  |
| Asia Pacific (Seoul)      | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:11` |
| Asia Pacific (Singapore)  | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:12` |
| Asia Pacific (Sydney)     | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:12` |
| Asia Pacific (Tokyo)      | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:23` |
| Canada (Central)          | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:10`   |
| Europe (Frankfurt)        | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:12`   |
| Europe (Ireland)          | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:12`      |
| Europe (London)           | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:12`      |
| Europe (Milan)            | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:9`      |
| Europe (Paris)            | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:10`      |
| Europe (Stockholm)        | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:10`     |
| Middle East (Bahrain)     | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:9`      |
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:10`      |

## 1.0.229.0

Version 1.0.229.0 includes bug fixes for all compatible runtimes. It also adds support for the following
Regions:

- US West (N. California)
- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Jakarta)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Canada (Central)
- Europe (Milan)
- Europe (Paris)
- Europe (Stockholm)
- Middle East (Bahrain)
- South America (São Paulo)

| Region                    | ARN                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------- |
| US East (N. Virginia)     | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:5`       |
| US East (Ohio)            | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:7`       |
| US West (N. California)   | `arn:aws:lambda:us-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:3`       |
| US West (Oregon)          | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:5`       |
| Africa (Cape Town)        | `arn:aws:lambda:af-south-1:012438385374:layer:LambdaInsightsExtension-Arm64:2`      |
| Asia Pacific (Hong Kong)  | `arn:aws:lambda:ap-east-1:519774774795:layer:LambdaInsightsExtension-Arm64:2`       |
| Asia Pacific (Jakarta)    | `arn:aws:lambda:ap-southeast-3:439286490199:layer:LambdaInsightsExtension-Arm64:2`  |
| Asia Pacific (Mumbai)     | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:7`      |
| Asia Pacific (Osaka)      | `arn:aws:lambda:ap-northeast-3:194566237122:layer:LambdaInsightsExtension-Arm64:2`  |
| Asia Pacific (Seoul)      | `arn:aws:lambda:ap-northeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:4`  |
| Asia Pacific (Singapore)  | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:5`  |
| Asia Pacific (Sydney)     | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:5`  |
| Asia Pacific (Tokyo)      | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:11` |
| Canada (Central)          | `arn:aws:lambda:ca-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:3`    |
| Europe (Frankfurt)        | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:5`    |
| Europe (Ireland)          | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:5`       |
| Europe (London)           | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:5`       |
| Europe (Spain)            | `arn:aws:lambda:eu-south-1:339249233099:layer:LambdaInsightsExtension-Arm64:2`      |
| Europe (Paris)            | `arn:aws:lambda:eu-west-3:580247275435:layer:LambdaInsightsExtension-Arm64:3`       |
| Europe (Stockholm)        | `arn:aws:lambda:eu-north-1:580247275435:layer:LambdaInsightsExtension-Arm64:3`      |
| Middle East (Bahrain)     | `arn:aws:lambda:me-south-1:285320876703:layer:LambdaInsightsExtension-Arm64:2`      |
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:3`       |

## 1.0.135.0

Version 1.0.135.0 includes bug fixes for how Lambda Insights collects and reports disk and file descriptor usage.
In previous versions of the extension, the `tmp_free` metric reported the maximum free space in the
`/tmp` directory while a function runs. This version changes the metric to report the
minimum value instead, making it more useful when assessing disk usage.
For more information about `tmp` directory storage quotas, see
[Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md").

Version 1.0.135.0 also now reports file descriptor usage (`fd_use` and `fd_max`) as
the maximum value across processes rather than reporting the operating system level.

| Region                   | ARN                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------- |
| US East (N. Virginia)    | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:2`      |
| US East (Ohio)           | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:2`      |
| US West (Oregon)         | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:2`      |
| Asia Pacific (Mumbai)    | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:2`     |
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:2` |
| Asia Pacific (Sydney)    | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:2` |
| Asia Pacific (Tokyo)     | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:2` |
| Europe (Frankfurt)       | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:2`   |
| Europe (Ireland)         | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:2`      |
| Europe (London)          | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:2`      |

## 1.0.119.0

| Region                   | ARN                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------- |
| US East (N. Virginia)    | `arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension-Arm64:1`      |
| US East (Ohio)           | `arn:aws:lambda:us-east-2:580247275435:layer:LambdaInsightsExtension-Arm64:1`      |
| US West (Oregon)         | `arn:aws:lambda:us-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:1`      |
| Asia Pacific (Mumbai)    | `arn:aws:lambda:ap-south-1:580247275435:layer:LambdaInsightsExtension-Arm64:1`     |
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:1` |
| Asia Pacific (Sydney)    | `arn:aws:lambda:ap-southeast-2:580247275435:layer:LambdaInsightsExtension-Arm64:1` |
| Asia Pacific (Tokyo)     | `arn:aws:lambda:ap-northeast-1:580247275435:layer:LambdaInsightsExtension-Arm64:1` |
| Europe (Frankfurt)       | `arn:aws:lambda:eu-central-1:580247275435:layer:LambdaInsightsExtension-Arm64:1`   |
| Europe (Ireland)         | `arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension-Arm64:1`      |
| Europe (London)          | `arn:aws:lambda:eu-west-2:580247275435:layer:LambdaInsightsExtension-Arm64:1`      |
