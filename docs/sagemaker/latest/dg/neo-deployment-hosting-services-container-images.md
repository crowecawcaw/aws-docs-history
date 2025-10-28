# Inference

Container Images

SageMaker Neo now provides inference image URI information for `ml_*`
targets. For more information see [DescribeCompilationJob](../APIReference/API_DescribeCompilationJob.md#sagemaker-DescribeCompilationJob-response-InferenceImage "../APIReference/API_DescribeCompilationJob.md#sagemaker-DescribeCompilationJob-response-InferenceImage").

Based on your use case, replace the highlighted portion in the inference image URI
template provided below with appropriate values.

```
`aws_account_id`.dkr.ecr.`aws_region`.amazonaws.com/xgboost-neo:latest
```

Replace `aws_account_id` from the table at the end of this page based on the `aws_region` you used.

```
`aws_account_id`.dkr.ecr.`aws_region`.amazonaws.com/sagemaker-neo-keras:fx_version-instance_type-py3
```

Replace `aws_account_id` from the table at the end of
this page based on the `aws_region` you used.

Replace `fx_version` with
`2.2.4`.

Replace `instance_type` with
either `cpu` or `gpu`.

CPU or GPU instance types

```
`aws_account_id`.dkr.ecr.`aws_region`.amazonaws.com/sagemaker-inference-mxnet:`fx_version`-`instance_type`-py3
```

Replace `aws_account_id` from the table at the end of
this page based on the `aws_region` you used.

Replace `fx_version` with
`1.8.0`.

Replace `instance_type` with
either `cpu` or `gpu`.

Inferentia1

```
`aws_account_id`.dkr.ecr.`aws_region`.amazonaws.com/sagemaker-neo-mxnet:`fx_version`-`instance_type`-py3
```

Replace `aws_region` with
either `us-east-1` or `us-west-2`.

Replace `aws_account_id` from the table at the end
of this page based on the `aws_region` you used.

Replace `fx_version` with
`1.5.1`.

Replace `instance_type` with `inf`.

```
`aws_account_id`.dkr.ecr.`aws_region`.amazonaws.com/sagemaker-neo-onnx:fx_version-instance_type-py3
```

Replace `aws_account_id` from the table at the end of
this page based on the `aws_region` you used.

Replace `fx_version` with
`1.5.0`.

Replace `instance_type` with
either `cpu` or `gpu`.

CPU or GPU instance types

```
`aws_account_id`.dkr.ecr.`aws_region`.amazonaws.com/sagemaker-inference-pytorch:`fx_version`-`instance_type`-py3
```

Replace `aws_account_id` from the table at the end of
this page based on the `aws_region` you used.

Replace `fx_version` with `1.4`, `1.5`,
`1.6`, `1.7`, `1.8`, `1.12`, `1.13`, or `2.0`.

Replace `instance_type` with
either `cpu` or `gpu`.

Inferentia1

```
`aws_account_id`.dkr.ecr.`aws_region`.amazonaws.com/sagemaker-neo-pytorch:`fx_version`-`instance_type`-py3
```

Replace `aws_region` with
either `us-east-1` or `us-west-2`.

Replace `aws_account_id` from the table at the end
of this page based on the `aws_region` you used.

Replace `fx_version` with
`1.5.1`.

Replace `instance_type` with `inf`.

Inferentia2 and Trainium1

```
763104351884.dkr.ecr.`aws_region`.amazonaws.com/pytorch-inference-neuronx:1.13.1-neuronx-py38-sdk2.10.0-ubuntu20.04
```

Replace `aws_region` with
`us-east-2` for Inferentia2, and
`us-east-1` for Trainium1.

CPU or GPU instance types

```
`aws_account_id`.dkr.ecr.`aws_region`.amazonaws.com/sagemaker-inference-tensorflow:`fx_version`-`instance_type`-py3
```

Replace `aws_account_id` from the table at the end of
this page based on the `aws_region` you used.

Replace `fx_version` with
`1.15.3` or `2.9`.

Replace `instance_type` with
either `cpu` or `gpu`.

Inferentia1

```
`aws_account_id`.dkr.ecr.`aws_region`.amazonaws.com/sagemaker-neo-tensorflow:`fx_version`-`instance_type`-py3
```

Replace `aws_account_id` from the table at the end of this page based on the `aws_region` you used.
Note that for instance type `inf` only `us-east-1` and `us-west-2` are supported.

Replace `fx_version` with `1.15.0`

Replace `instance_type` with `inf`.

Inferentia2 and Trainium1

```
763104351884.dkr.ecr.`aws_region`.amazonaws.com/tensorflow-inference-neuronx:2.10.1-neuronx-py38-sdk2.10.0-ubuntu20.04
```

Replace `aws_region` with
`us-east-2` for Inferentia2, and
`us-east-1` for Trainium1.

The following table maps `aws_account_id`
with `aws_region`.
Use this table to find the correct inference image URI
you need for your application.

| aws_account_id | aws_region     |
| -------------- | -------------- |
| 785573368785   | us-east-1      |
| 007439368137   | us-east-2      |
| 710691900526   | us-west-1      |
| 301217895009   | us-west-2      |
| 802834080501   | eu-west-1      |
| 205493899709   | eu-west-2      |
| 254080097072   | eu-west-3      |
| 601324751636   | eu-north-1     |
| 966458181534   | eu-south-1     |
| 746233611703   | eu-central-1   |
| 110948597952   | ap-east-1      |
| 763008648453   | ap-south-1     |
| 941853720454   | ap-northeast-1 |
| 151534178276   | ap-northeast-2 |
| 925152966179   | ap-northeast-3 |
| 324986816169   | ap-southeast-1 |
| 355873309152   | ap-southeast-2 |
| 474822919863   | cn-northwest-1 |
| 472730292857   | cn-north-1     |
| 756306329178   | sa-east-1      |
| 464438896020   | ca-central-1   |
| 836785723513   | me-south-1     |
| 774647643957   | af-south-1     |
| 275950707576   | il-central-1   |
