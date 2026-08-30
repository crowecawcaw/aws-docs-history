# Accelerated transcoding

AWS Elemental MediaConvert jobs that create premium content may have high computational requirements
and can take longer to complete. Such jobs may include Ultra High Definition (UHD) or High
Dynamic Range (HDR) content. To reduce the transcoding time required to run these jobs, you
can use Accelerated transcoding. Consider using Accelerated transcoding for jobs that would otherwise take 10
minutes or longer to run.

For example, jobs that generate the following assets might benefit from
Accelerated transcoding:

- Ultra High Definition content
- High dynamic range content in HEVC
- Any long-duration, visually complex video

###### Note

Accelerated transcoding is a Professional tier feature. You pay more per minute of transcoded
output for outputs that use Professional tier features. Accelerated transcoding might also read source files from Amazon S3 multiple times. If your source files use a storage class with per-retrieval fees (for example, S3 Glacier Instant Retrieval), we charge separately for each read. For more information about MediaConvert
pricing tiers, see [MediaConvert
pricing](https://aws.amazon.com/mediaconvert/pricing/ "https://aws.amazon.com/mediaconvert/pricing/").

###### Topics

- [Configuring a job with Accelerated transcoding](setting-up-accelerated-transcoding.md "setting-up-accelerated-transcoding.md")
- [Example accelerated transcoding job settings JSON](sample-acceleration-job-settings-in-json.md "sample-acceleration-job-settings-in-json.md")
- [Accelerated transcoding job settings requirements](job-requirements.md "job-requirements.md")
