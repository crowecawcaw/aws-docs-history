# Amazon EMR 7.9.0 - Hadoop release notes

## Amazon EMR 7.9.0 - Hadoop changes

| Type        | Description                                                                                                                                                                             |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Feature | Automatic Configuration Mapping: EMRFS filesystem configuration are automatically applied to corresponding S3A filessystem configuration enabling seamless migration from EMRFS to S3A. |
| New Feature | [YARN Conatainer bin-packing](Hadoop-container-yarn.md "Hadoop-container-yarn.md"): scheduling policy for aggresive downscaling                                                         |
| Backport    | YARN-11752 : Global Scheduler: Improve the container allocation time                                                                                                                    |
| Bug Fix     | S3A: Fix IAMCredentialsProvider Returning Expired Credentials                                                                                                                           |
| Bug Fix     | Fix `yarn.log.server.url` configuration value for clusters with in-transit encryption enabled                                                                                           |
