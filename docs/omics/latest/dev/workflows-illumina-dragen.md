

# Illumina DRAGEN on HealthOmics private workflows
<a name="workflows-illumina-dragen"></a>

Illumina DRAGEN v4.6 includes a software mode (SW mode) that runs on standard x86 CPU instances and produces results that match FPGA-based DRAGEN. You can run DRAGEN SW mode as a task in a HealthOmics private workflow in all AWS Regions where HealthOmics is available. DRAGEN SW mode doesn't use FPGA instances, and you don't specify a task accelerator.

**Note**  
DRAGEN is third-party software licensed by Illumina. HealthOmics does not provide DRAGEN licenses.

## How Illumina DRAGEN works with HealthOmics
<a name="dragen-how-it-works"></a>

To run DRAGEN, start the run in `VPC` networking mode. Use a virtual private cloud (VPC) that routes outbound traffic through a NAT gateway. Each DRAGEN task validates its license with Illumina when the task starts, and license validation requires outbound internet access.

**Important**  
By default, HealthOmics runs use `RESTRICTED` networking mode, which allows access only to Amazon S3 and Amazon ECR in the same Region and blocks the public internet. A run that uses `RESTRICTED` mode can't validate the license, and the DRAGEN task fails.

DRAGEN SW mode runs on x86 CPU instances, available in all Regions where HealthOmics supports private workflows. To see which DRAGEN pipelines are supported in SW mode, see the latest Illumina DRAGEN release notes.

## Prerequisites
<a name="dragen-prerequisites"></a>

Before you run DRAGEN SW mode, make sure that you have the following:
+ A DRAGEN license from Illumina.
+ A private Amazon ECR repository in the Region where you run the workflow.
+ A VPC with private subnets, a NAT gateway, and a security group that allows outbound HTTPS (port 443). For more information, see [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md). For an example VPC setup, see [ HealthOmics VPC configuration on the GitHub website](https://github.com/aws-samples/sample-healthomics-vpc-configuration).
+ A HealthOmics service role with access to your Amazon ECR repository and your Amazon S3 input and output locations. For more information about service roles, see [Service roles for AWS HealthOmics](permissions-service.md).

## Get a DRAGEN license
<a name="dragen-get-license"></a>

Subscribe to DRAGEN through Illumina. After you subscribe, Illumina provides the API key that the DRAGEN container uses to validate the license. For options to store the key and pass it to the task, see [Managing license keys](#dragen-license-keys).

## Build the DRAGEN container image and push it to Amazon ECR
<a name="dragen-build-image"></a>

HealthOmics runs container images from private Amazon ECR repositories in the same Region as the workflow. Build the DRAGEN image before you push it to your repository. HealthOmics supports `x86_64` containers. For installation instructions, see the [DRAGEN software mode reference](https://help.dragen.illumina.com/dragen-v4.6/reference/software-mode).

Before you build the image, extract the DRAGEN installer (`.run` file) without running it, and inspect the RPM Package Manager (RPM) packages that it contains:

```
sh dragen-4.6.2-*.multi.el9.x86_64.run --noexec --keep --target ./extracted
ls ./extracted            # Contains RPMs, flavors/, installer/, and wrapper.
```

Install only the packages required for SW mode. Skip the FPGA driver, host services, and bitstream packages. The following table lists the RPMs to install and the RPMs to skip.


| Install | Skip and reason | 
| --- | --- | 
| dragen-paths | dragen\_drv – FPGA XDMA kernel drivers (a container can't load kernel modules) | 
| dragen-host | dragen-host-services – no systemd in a task | 
| dragen | dragen-bitstream-\* – unused in SW mode | 
| dragen-platform-aws | None | 

The following is a sample Dockerfile. It copies only the four SW mode RPMs by name. Broader patterns such as `dragen-host-*.rpm` also match the `dragen-host-services` and `dragen-bitstream` RPMs that you skip.

```
FROM oraclelinux:9
ARG DRAGEN_VERSION=4.6.2

RUN dnf -y install bzip2-libs coreutils gawk gdb perl procps-ng rsync sed \
        libgcc libstdc++ libgomp xz-libs zlib systemd-libs \
    && dnf clean all && rm -rf /var/cache/dnf

COPY dragen-paths-${DRAGEN_VERSION}-*.rpm \
     dragen-host-${DRAGEN_VERSION}-*.rpm \
     dragen-${DRAGEN_VERSION}-*.el9.x86_64.rpm \
     dragen-platform-aws-${DRAGEN_VERSION}-*.noarch.rpm /tmp/rpms/

# --nodeps: the RPMs declare driver/host-services dependencies that you intentionally exclude.
RUN rpm -ivh --nodeps /tmp/rpms/*.rpm && rm -rf /tmp/rpms

ENV PATH="/opt/dragen/${DRAGEN_VERSION}/bin:${PATH}"
RUN dragen --version          # sanity check: must succeed with no FPGA/driver
CMD ["dragen", "--version"]
```

This sample Dockerfile does not include the AWS CLI. If you use the Amazon SageMaker AI retrieval pattern described in [Managing license keys](#dragen-license-keys), add `aws-cli` to the `dnf install` line, because the task calls `aws secretsmanager get-secret-value` directly from inside the container.

HealthOmics requires `linux/amd64` images. If you build the image with the `--platform` flag, you can cross-compile from an Apple silicon machine.

```
docker build --platform linux/amd64 -f docker/Dockerfile -t dragen:4.6.2-sw extracted/
```

Create an Amazon ECR private repository, and then push your DRAGEN image to the repository. For more information, see [Pushing a Docker image to an Amazon ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) in the *Amazon ECR User Guide*.

Create a file named `ecr-omics-policy.json` that contains the following repository policy, so that HealthOmics can pull the container image:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [{
    "Sid": "OmicsAccess",
    "Effect": "Allow",
    "Principal": { "Service": "omics.amazonaws.com" },
    "Action": ["ecr:BatchGetImage","ecr:GetDownloadUrlForLayer","ecr:BatchCheckLayerAvailability"]
  }]
}
```

Apply the policy to your repository. In the following command, replace {{dragen}} with the name of your repository, and replace `us-east-2` with your Region. Make the same Region replacement in the other commands and policies on this page.

```
aws ecr set-repository-policy --repository-name {{dragen}} --region us-east-2 \
  --policy-text file://ecr-omics-policy.json
```

For more HealthOmics requirements, see [Container images for private workflows](workflows-ecr.md).

## Configure VPC networking for license validation
<a name="dragen-vpc"></a>

Create the network resources and a HealthOmics configuration resource, as described in [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md). Your runs must use `VPC` networking mode with an active HealthOmics configuration that meets the following requirements:


| Setting | Requirement | 
| --- | --- | 
| Subnets | Private subnets, one per Availability Zone, in Availability Zones where HealthOmics operates. | 
| Routing | Route 0.0.0.0/0 from the private subnets to a NAT gateway, so that the task reaches license.dragen.illumina.com. | 
| Security group | Allow outbound TCP 443. To restrict the rule to specific destinations, use the Illumina license endpoints. | 

Verify that your configuration meets these requirements:

```
aws omics get-configuration --name {{my-vpc-config}} --region us-east-2
```

You can reuse the configuration for all DRAGEN runs in the Region.

## Managing license keys
<a name="dragen-license-keys"></a>

You can keep a copy of your license key in Amazon SageMaker AI. HealthOmics does not inject secrets into the task environment. Your task must call SageMaker AI at runtime to retrieve the key before it runs `dragen`.

Store the key as a secret:

```
aws secretsmanager create-secret \
  --name dragen/illumina-api-key \
  --secret-string file://illumina-api-key.txt \
  --region us-east-2
```

Grant your service role permission to read the secret (see [IAM service role](#dragen-iam)), and then retrieve the key inside the task before you invoke `dragen`. The DRAGEN container image must include the AWS CLI (or an AWS SDK) to make the call.

For example, add the following to the task's command block, before the `dragen` call. It writes the key to a plain text file named `/tmp/illumina-api-key.txt`, which you then pass to `--api-key-file`.

```
dragen_api_key=$(aws secretsmanager get-secret-value \
  --secret-id dragen/illumina-api-key \
  --region us-east-2 \
  --query SecretString --output text)

if [ -z "$dragen_api_key" ]; then
  echo "Error: failed to retrieve the DRAGEN API key." >&2
  exit 1
fi

echo "$dragen_api_key" > /tmp/illumina-api-key.txt
```

The task already runs in `VPC` networking mode to reach the Illumina license server. By default, the same NAT gateway route provides access to the SageMaker AI API endpoint. To avoid routing this call through the NAT gateway, add a VPC interface endpoint for SageMaker AI.

You can also stage the license key as an SSE-encrypted Amazon S3 object and specify the object as an input file for the workflow or workflow tasks. This keeps the key out of the workflow definition and out of Amazon CloudWatch.

```
aws s3 cp illumina-api-key.txt \
  s3://{{amzn-s3-demo-bucket}}/secrets/illumina-api-key.txt \
  --sse AES256 --region us-east-2
```

Grant the HealthOmics service role read access to that object (see [IAM service role](#dragen-iam)), and then reference it as a workflow parameter:

```
{
  "api_key_file": "s3://{{amzn-s3-demo-bucket}}/secrets/illumina-api-key.txt"
}
```

Make sure that the Illumina API key in the workflow inputs is scoped to DRAGEN tasks only.

## Define the DRAGEN task
<a name="dragen-task"></a>

The following WDL example shows the structure of a sample DRAGEN task. You can pass the license key as part of the workflow input parameters, either as a JSON file or as inline values. Also pass the image URI as a workflow input, so that HealthOmics can verify access before the run starts. For more information, see [HealthOmics run inputs](workflows-run-inputs.md).

The `dragen` command line and the resource values depend on your analysis. For more information, see [Task resources in a HealthOmics workflow definition](task-resources.md).

**Note**  
Give each DRAGEN task at least 16 vCPUs and 128 GiB of memory, which matches the `omics.r.4xlarge` instance type. Illumina recommends up to 64 vCPUs and 256 GiB of memory for some tasks. For details, see the DRAGEN software mode reference that is linked earlier in this topic.

DRAGEN analysis is I/O intensive, and disk throughput can limit performance and increase total runtime. For optimal performance, use local ephemeral storage volumes. To request more per-task ephemeral storage, use the `disks` directive (or equivalent) in your workflow definition. For more information, see [Configuring ephemeral storage size](workflows-ephemeral-storage.md#ephemeral-storage-configure-size).

**Sample DRAGEN task (WDL)**

```
task DragenGermline {
    input {
        File api_key_file  # the SSE-encrypted S3 object, specified in inputs.json at StartRun.
        File hashtable_tar
        File fastq_1
        File fastq_2
        String sample_id
        String dragen_container
    }

    command <<<
        set -eu
        mkdir -p output reference

        tar -xf "~{hashtable_tar}" -C reference

        # To validate the key first without analysis or billing, add --metering-preview to the command below.
        dragen \
            --sw-mode \
            --api-key-file "~{api_key_file}" \
            -r reference \
            -1 "~{fastq_1}" -2 "~{fastq_2}" \
            --RGID "~{sample_id}-rg" --RGSM "~{sample_id}" \
            --enable-map-align true --enable-variant-caller true \
            --validate-pangenome-reference false \
            --output-directory output --output-file-prefix "~{sample_id}"
    >>>

    runtime {
        container: dragen_container
        cpu: 16
        memory: "128 GiB"
        disks: "64 GiB"
    }
}
```

## Create your workflow
<a name="dragen-create-workflow"></a>

Follow the steps in [Create a private workflow](create-private-workflow.md) to create the workflow by using the console, the AWS CLI, or one of the AWS SDKs.

```
aws omics create-workflow --name dragen-sw-germline \
  --definition-zip fileb://workflow.zip --engine WDL --main main.wdl ...
```

You can use the HealthOmics linter for WDL or Nextflow to resolve errors before you create the workflow. For more information, see [Workflow linters in HealthOmics](workflows-linter.md).

## IAM service role
<a name="dragen-iam"></a>

Create a dedicated least-privilege service role. For more information, see [IAM permissions for HealthOmics](omics-permissions.md).

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "S3",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
      ]
    },
    {
      "Sid": "Logs",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams"
      ],
      "Resource": "arn:aws:logs:us-east-2:{{123456789012}}:log-group:/aws/omics/*"
    },
    {
      "Sid": "ECRPull",
      "Effect": "Allow",
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage"
      ],
      "Resource": "arn:aws:ecr:us-east-2:{{123456789012}}:repository/{{dragen}}"
    },
    {
      "Sid": "ECRAuth",
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    }
  ]
}
```

If you use Amazon SageMaker AI, add a statement that grants permission to read the secret:

```
{
  "Sid": "ReadDragenApiKeySecret",
  "Effect": "Allow",
  "Action": "secretsmanager:GetSecretValue",
  "Resource": "arn:aws:secretsmanager:us-east-2:{{123456789012}}:secret:{{secret-name}}-*"
}
```

## Start the run with VPC networking
<a name="dragen-start-run"></a>

Start a run in `VPC` networking mode with your configuration, and set `scratch-storage-mode` to `LOCAL` to redirect scratch I/O to local disk. In the following command, replace {{1234567}}, {{123456789012}}, {{dragen-sw-omics-role}}, {{amzn-s3-demo-bucket}}, and {{my-vpc-config}} with your own values.

```
aws omics start-run \
  --workflow-id {{1234567}} \
  --name dragen-sw-germline-run \
  --role-arn arn:aws:iam::{{123456789012}}:role/{{dragen-sw-omics-role}} \
  --output-uri s3://{{amzn-s3-demo-bucket}}/runs/ \
  --parameters file://parameters.json \
  --networking-mode VPC \
  --configuration-name {{my-vpc-config}} \
  --storage-type DYNAMIC \
  --scratch-storage-mode LOCAL \
  --region us-east-2
```

For more information about run storage types, see [Run storage types in HealthOmics workflows](workflows-run-types.md).

## Considerations
<a name="dragen-considerations"></a>

Local disk  
For best performance, run DRAGEN with fast local disk on the compute node. To enable scratch ephemeral storage mounted at `/tmp`, set `scratchStorageMode` to `LOCAL`. For more information, see [Ephemeral storage for HealthOmics workflow tasks](workflows-ephemeral-storage.md).

Public internet connection  
DRAGEN validates its license over the internet, but the default `RESTRICTED` networking mode in HealthOmics blocks outbound calls to the public internet. To run DRAGEN, start the run with `VPC` networking mode. Provide a configuration with subnets that route outbound traffic through a NAT gateway. The task then reaches `license.dragen.illumina.com` over HTTPS. For more information, see [Internet access for VPC-connected workflows](workflows-vpc-internet.md).

Call caching  
If you use call caching, exclude tasks that perform license checks. License validation contacts an external service, and a run cache could affect task outputs. You can exclude a task from caching by using a directive in the workflow definition. For more information, see [Engine-specific caching features](workflow-cache-per-engine.md).

## Troubleshooting DRAGEN runs
<a name="dragen-troubleshooting"></a>


| Symptom | Likely cause | Action | 
| --- | --- | --- | 
| Task fails at start with a license or connection error in the Amazon CloudWatch Logs log. | Run started in RESTRICTED mode. | Start the run with --networking-mode VPC and a configuration name. | 
| Same error in VPC mode. | Private subnet has no route to a NAT gateway, or the security group blocks port 443. | Check the route table and security group. Run the connectivity test in [Testing VPC connectivity](workflows-vpc-internet.md#vpc-testing-connectivity). | 
| License rejected. | Expired trial, exhausted iCredits, or wrong credentials. | Check the status of your subscription with Illumina. | 
| AccessDenied when pulling the image. | Service role or repository policy lacks Amazon ECR permissions. | See [Amazon ECR permissions](permissions-ecr.md). | 
| License step fails immediately with HTTP 403. | Used --lic-server (legacy credentials) instead of --api-key-file. | Switch to --api-key-file (or --lic-credentials). --lic-server is not supported in SW mode. | 
| Task fails before any license check, even with minimal or test inputs. | DRAGEN enforces a minimum of 16 vCPUs and 120 GiB of memory to validate the command line. | Use at least omics.r.4xlarge (16 vCPUs, 128 GiB) for any DRAGEN SW mode task, including dry runs. | 

## Related topics
<a name="dragen-related"></a>
+ [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md)
+ [Internet access for VPC-connected workflows](workflows-vpc-internet.md)
+ [Container images for private workflows](workflows-ecr.md)
+ [Requesting Sentieon licenses for private workflows](private-workflows-subscribe.md)