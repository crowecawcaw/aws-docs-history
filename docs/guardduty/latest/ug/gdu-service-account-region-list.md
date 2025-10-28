# GuardDuty service accounts by

AWS Region

When a snapshot gets created and shared with a GuardDuty service account, a new event gets
created in your CloudTrail logs. This event specifies the corresponding `snapshotId` and
`userId` (GuardDuty service account for that AWS Region). For more information, see
[How GuardDuty scans EBS
volumes for malware detection](guardduty_malware_protection-ebs-volume-data.md "guardduty_malware_protection-ebs-volume-data.md").

The following example is a snippet from a CloudTrail event that shows the request body for the
`ModifySnapshotAttribute` request:

```
"requestParameters": {
        "snapshotId": "snap-1234567890abcdef0",
        "createVolumePermission": {
            "add": {
                "items": [
                    {
                        "userId": "111122223333"
                    }
                ]
            }
        },
        "attributeType": "CREATE_VOLUME_PERMISSION"
    }
```

The following table shows the GuardDuty service accounts for each Region. The
`userId` is the GuardDuty service account and depends on the selected Region.

| AWS Region                        | Region code    | GuardDuty service account ID (`userId`) |
| --------------------------------- | -------------- | --------------------------------------- |
| US East (N. Virginia)             | us-east-1      | 652050842985                            |
| US East (Ohio)                    | us-east-2      | 178123968615                            |
| US West (N. California)           | us-west-1      | 669213148797                            |
| US West (Oregon)                  | us-west-2      | 447226417196                            |
| Asia Pacific (Mumbai)             | ap-south-1     | 913179291432                            |
| Asia Pacific (Osaka)              | ap-northeast-3 | 089661699081                            |
| Asia Pacific (Seoul)              | ap-northeast-2 | 039163547507                            |
| Asia Pacific (Tokyo)              | ap-northeast-1 | 874749492622                            |
| Asia Pacific (Singapore)          | ap-southeast-1 | 247460962669                            |
| Asia Pacific (Sydney)             | ap-southeast-2 | 124839743349                            |
| Canada (Central)                  | ca-central-1   | 175877067165                            |
| Canada West (Calgary)             | ca-west-1      | 894794104037                            |
| Europe (Frankfurt)                | eu-central-1   | 002294850712                            |
| Europe (Ireland)                  | eu-west-1      | 283769539786                            |
| Europe (London)                   | eu-west-2      | 310125036783                            |
| Europe (Paris)                    | eu-west-3      | 866607715269                            |
| Europe (Stockholm)                | eu-north-1     | 693780578038                            |
| China (Beijing)                   | cn-north-1     | 448721096076                            |
| China (Ningxia)                   | cn-northwest-1 | 480864352451                            |
| South America (São Paulo)         | sa-east-1      | 546914126324                            |
| Asia Pacific (Hyderabad) (Opt-in) | ap-south-2     | 682251015962                            |
| Asia Pacific (Melbourne) (Opt-in) | ap-southeast-4 | 353488359550                            |
| Asia Pacific (Malaysia) (Opt-in)  | ap-southeast-5 | 009160069308                            |
| Asia Pacific (Thailand) (Opt-in)  | ap-southeast-7 | 941377115582                            |
| Europe (Spain) (Opt-in)           | eu-south-2     | 936182149045                            |
| Europe (Zurich) (Opt-in)          | eu-central-2   | 867642063380                            |
| Israel (Tel Aviv) (Opt-in)        | il-central-1   | 619233833001                            |
| Europe (Milan) (Opt-in)           | eu-south-1     | 977238331021                            |
| Asia Pacific (Hong Kong) (Opt-in) | ap-east-1      | 249472122084                            |
| Middle East (Bahrain) (Opt-in)    | me-south-1     | 404001805210                            |
| Africa (Cape Town) (Opt-in)       | af-south-1     | 957664736811                            |
| Asia Pacific (Jakarta) (Opt-in)   | ap-southeast-3 | 452118225523                            |
| Middle East (UAE) (Opt-in)        | me-central-1   | 828603743433                            |
| Mexico (Central) (Opt-in)         | mx-central-1   | 557690616787                            |
| Asia Pacific (Taipei)             | ap-east-2      | 863518437308                            |
| AWS GovCloud (US-East)            | us-gov-east-1  | 226283551151                            |
| AWS GovCloud (US-West)            | us-gov-west-1  | 226300430612                            |
