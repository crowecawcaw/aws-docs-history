# Details for selecting a base image URI

###### Note

For Amazon EMR 6.9.0 releases and later, you can retrieve the base image from
Amazon ECR Public Gallery, so you don't need to construct the base image URI as the instructions
on this page direct. To find the container image tag for your base image, refer to the [release notes page](emr-eks-releases.md "emr-eks-releases.md") for the corresponding release of
Amazon EMR on EKS.

The base Docker images that you can select are stored in Amazon Elastic Container Registry (Amazon ECR).
The image URI follows this format:
``ECR-registry-account`.dkr.ecr.`Region`.amazonaws.com/spark/`container-image-tag``,
as the following example demonstrates.

```
`895885662937`.dkr.ecr.`us-west-2`.amazonaws.com/spark/`emr-7.12.0:latest`
```

The image URI for interactive endpoints follows this format:
``ECR-registry-account`.dkr.ecr.`Region`.amazonaws.com/notebook-spark/`container-image-tag``,
as the following example demonstrates. You need to use `notebook-spark` in the base
image URI, instead of `spark`.

```
`895885662937`.dkr.ecr.`us-west-2`.amazonaws.com/notebook-spark/`emr-7.12.0:latest`
```

Similarly, for non-Spark `python3` images for interactive endpoints,
the image URI is
``ECR-registry-account`.dkr.ecr.`Region`.amazonaws.com/notebook-python/`container-image-tag``.
The following example URI is correctly formatted:

```
`895885662937`.dkr.ecr.`us-west-2`.amazonaws.com/notebook-python/`emr-7.12.0:latest`
```

To find the container image tag for your base image, refer to the [release notes page](emr-eks-releases.md "emr-eks-releases.md") for the corresponding release of
Amazon EMR on EKS.

## Amazon ECR registry accounts by Region

To avoid high network latency, pull a base image from your closest AWS Region. Select
the Amazon ECR registry account that corresponds with the Region that you pull the image from
based on the following table.

| Regions          | Amazon ECR registry accounts |
| ---------------- | ---------------------------- |
| `ap-east-1`      | `736135916053`               |
| `ap-northeast-1` | `059004520145`               |
| `ap-northeast-2` | `996579266876`               |
| `ap-northeast-3` | `705689932349`               |
| `ap-southeast-3` | `946962994502`               |
| `ap-south-1`     | `235914868574`               |
| `ap-south-2`     | `691480105545`               |
| `ap-southeast-1` | `671219180197`               |
| `ap-southeast-2` | `038297999601`               |
| `ca-central-1`   | `351826393999`               |
| `eu-central-1`   | `107292555468`               |
| `eu-central-2`   | `314408114945`               |
| `eu-north-1`     | `830386416364`               |
| `eu-west-1`      | `483788554619`               |
| `eu-west-2`      | `118780647275`               |
| `eu-west-3`      | `307523725174`               |
| `eu-south-1`     | `238014973495`               |
| `eu-south-2`     | `350796622945`               |
| `il-central-1`   | `395734710648`               |
| `me-south-1`     | `008085056818`               |
| `me-central-1`   | `818935616732`               |
| `sa-east-1`      | `052806832358`               |
| `us-gov-west-1`  | `299385240661`               |
| `us-gov-east-1`  | `299393998622`               |
| `us-east-1`      | `755674844232`               |
| `us-east-2`      | `711395599931`               |
| `us-west-1`      | `608033475327`               |
| `us-west-2`      | `895885662937`               |
| `af-south-1`     | `358491847878`               |
| `cn-north-1`     | `068337069695`               |
| `cn-northwest-1` | `068420816659`               |
