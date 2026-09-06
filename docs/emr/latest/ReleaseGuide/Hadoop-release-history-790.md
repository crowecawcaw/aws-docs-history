

# Amazon EMR 7.9.0 - Hadoop release notes
<a name="Hadoop-release-history-790"></a>

## Amazon EMR 7.9.0 - Hadoop changes
<a name="Hadoop-release-history-790-changes"></a>


| Type | Description | 
| --- | --- | 
| New Feature | Automatic Configuration Mapping: EMRFS filesystem configuration are automatically applied to corresponding S3A filessystem configuration enabling seamless migration from EMRFS to S3A. | 
| New Feature |  [YARN Conatainer bin-packing](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-container-yarn.html): scheduling policy for aggresive downscaling | 
| Backport |  YARN-11752 : Global Scheduler: Improve the container allocation time | 
| Bug Fix |  S3A: Fix IAMCredentialsProvider Returning Expired Credentials  | 
| Bug Fix |  Fix `yarn.log.server.url` configuration value for clusters with in-transit encryption enabled | 