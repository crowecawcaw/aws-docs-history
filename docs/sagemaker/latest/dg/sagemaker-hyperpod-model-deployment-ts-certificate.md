

# Certificate download timeout
<a name="sagemaker-hyperpod-model-deployment-ts-certificate"></a>

When deploying a SageMaker AI endpoint, the creation process fails due to the inability to download the certificate authority (CA) certificate in a VPC environment. For detailed configuration steps, refer to the [Admin guide](https://github.com/aws-samples/sagemaker-genai-hosting-examples/blob/main/SageMakerHyperpod/hyperpod-inference/Hyperpod_Inference_Admin_Notebook.ipynb).

**Error message:**

The following error appears in the SageMaker AI endpoint CloudWatch logs: 

```
Error downloading CA certificate: Connect timeout on endpoint URL: "https://****.s3.<REGION>.amazonaws.com/****/***.pem"
```

**Root cause:**
+ This issue occurs when the inference operator cannot access the self-signed certificate in Amazon S3 within your VPC
+ Proper configuration of the Amazon S3 VPC endpoint is essential for certificate access

**Resolution:**

1. If you don't have an Amazon S3 VPC endpoint:
   + Create an Amazon S3 VPC endpoint following the configuration in section 5.3 of the [Admin guide](https://github.com/aws-samples/sagemaker-genai-hosting-examples/blob/main/SageMakerHyperpod/hyperpod-inference/Hyperpod_Inference_Admin_Notebook.ipynb).

1. If you already have an Amazon S3 VPC endpoint:
   + Ensure that the subnet route table is configured to point to the VPC endpoint (if using gateway endpoint) or that private DNS is enabled for interface endpoint.
   + Amazon S3 VPC endpoint should be similar to the configuration mentioned in section 5.3 Endpoint creation step