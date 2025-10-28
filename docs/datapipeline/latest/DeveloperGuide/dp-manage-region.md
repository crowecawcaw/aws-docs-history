AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Using a Pipeline with Resources in Multiple

Regions

By default, the `Ec2Resource` and `EmrCluster` resources run in
the same region as AWS Data Pipeline, however AWS Data Pipeline supports the ability to orchestrate data
flows across multiple regions, such as running resources in one region that consolidate
input data from another region. By allowing resources to run a specified region, you
also have the flexibility to co-locate your resources with their dependent datasets and
maximize performance by reducing latencies and avoiding cross-region data transfer
charges. You can configure resources to run in a different region than AWS Data Pipeline by using
the `region` field on `Ec2Resource` and `EmrCluster`.

The following example pipeline JSON file shows how to run an `EmrCluster`
resource in the Europe (Ireland) region, assuming that a large amount of data for the
cluster to work on exists in the same region. In this example, the only difference from
a typical pipeline is that the `EmrCluster` has a `region` field
value set to `eu-west-1`.

```
{
  "objects": [
    {
      "id": "Hourly",
      "type": "Schedule",
      "startDateTime": "2014-11-19T07:48:00",
      "endDateTime": "2014-11-21T07:48:00",
      "period": "1 hours"
    },
    {
      "id": "MyCluster",
      "type": "EmrCluster",
      "masterInstanceType": "m3.medium",
      "region": "eu-west-1",
      "schedule": {
        "ref": "Hourly"
      }
    },
    {
      "id": "MyEmrActivity",
      "type": "EmrActivity",
      "schedule": {
        "ref": "Hourly"
      },
      "runsOn": {
        "ref": "MyCluster"
      },
      "step": "/home/hadoop/contrib/streaming/hadoop-streaming.jar,-input,s3n://elasticmapreduce/samples/wordcount/input,-output,s3://eu-west-1-bucket/wordcount/output/#{@scheduledStartTime},-mapper,s3n://elasticmapreduce/samples/wordcount/wordSplitter.py,-reducer,aggregate"
    }
  ]
}
```

The following table lists the regions that you can choose and the associated region
codes to use in the `region` field.

###### Note

The following list includes regions in which AWS Data Pipeline can orchestrate workflows and
launch Amazon EMR or Amazon EC2 resources. AWS Data Pipeline may not be supported in these regions. For
information about regions in which AWS Data Pipeline is supported, see [AWS Regions and
Endpoints](../../../general/latest/gr/rande.md#datapipeline_region "../../../general/latest/gr/rande.md#datapipeline_region").

| Region Name               | Region Code    |
| ------------------------- | -------------- |
| US East (N. Virginia)     | us-east-1      |
| US East (Ohio)            | us-east-2      |
| US West (N. California)   | us-west-1      |
| US West (Oregon)          | us-west-2      |
| Canada (Central)          | ca-central-1   |
| Europe (Ireland)          | eu-west-1      |
| Europe (London)           | eu-west-2      |
| Europe (Frankfurt)        | eu-central-1   |
| Asia Pacific (Singapore)  | ap-southeast-1 |
| Asia Pacific (Sydney)     | ap-southeast-2 |
| Asia Pacific (Mumbai)     | ap-south-1     |
| Asia Pacific (Tokyo)      | ap-northeast-1 |
| Asia Pacific (Seoul)      | ap-northeast-2 |
| South America (São Paulo) | sa-east-1      |
