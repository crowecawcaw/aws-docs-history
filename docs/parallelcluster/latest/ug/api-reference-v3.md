# AWS ParallelCluster API

**What is AWS ParallelCluster API?**

AWS ParallelCluster API is a serverless application that, once deployed to your AWS account,
provides programmatic access to AWS ParallelCluster features through an API.

AWS ParallelCluster API is distributed as a self-contained [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") template that includes an
[Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md")
endpoint, that exposes AWS ParallelCluster features, and an [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") function, that takes care of processing
the invoked features.

The following image shows a high-level architecture diagram of the AWS ParallelCluster API
infrastructure.

![a high-level architecture diagram of the ParallelCluster API infrastructure](images/API-Architecture-r2.png)

## AWS ParallelCluster API Documentation

The OpenAPI specification file that describes the AWS ParallelCluster API can be downloaded
from:

```
https://`<REGION>`-aws-parallelcluster.s3.`<REGION>`.amazonaws.com/parallelcluster/`<VERSION>`/api/ParallelCluster.openapi.yaml
```

Starting from the OpenAPI specification file, you can use one of the many available tools
such as [Swagger UI](https://swagger.io/tools/swagger-ui/ "https://swagger.io/tools/swagger-ui/") or [Redoc](https://github.com/Redocly/redoc "https://github.com/Redocly/redoc") to generate documentation for the
AWS ParallelCluster API.

**How to deploy AWS ParallelCluster API**

To deploy AWS ParallelCluster API you need to be an Administrator of the AWS account.

The template used to deploy the API is available at the following URL:

```
https://`<REGION>`-aws-parallelcluster.s3.`<REGION>`.amazonaws.com/parallelcluster/`<VERSION>`/api/parallelcluster-api.yaml
```

where `<REGION>` is the AWS Region where the
API needs to be deployed to and `<VERSION>` is
the AWS ParallelCluster version (e.g. 3.14.0).

AWS Lambda uses a Lambda layer interface with the [AWS ParallelCluster Python library API](pc-py-library-v3.md "pc-py-library-v3.md") to process the API invoked features.

###### Warning

Any user in the AWS account, that has privileged access to AWS Lambda or Amazon API Gateway services,
automatically inherits permissions to administer AWS ParallelCluster API resources.
