

# Illumina DRAGEN on HealthOmics private workflows
<a name="workflows-illumina-dragen"></a>

Illumina DRAGEN v4.6 includes a software mode (SW mode) that runs on standard x86 CPU instances and produces results that match FPGA-based DRAGEN. You can run DRAGEN SW mode as a task in a HealthOmics private workflow in all Regions where HealthOmics is available. DRAGEN SW mode doesn't use FPGA instances, and you don't specify a task accelerator.

**Note**  
DRAGEN is third-party software licensed by Illumina. HealthOmics does not provide DRAGEN licenses.

## How Illumina DRAGEN works with HealthOmics
<a name="dragen-how-it-works"></a>

Each DRAGEN task validates its license with Illumina when the task starts. License validation requires outbound internet access. By default, HealthOmics runs use `RESTRICTED` networking mode, which allows access only to Amazon S3 and Amazon ECR in the same Region and blocks the public internet. To run DRAGEN, you start the run in `VPC` networking mode with a VPC that routes outbound traffic through a NAT gateway. A run that uses `RESTRICTED` mode can't validate the license and the DRAGEN task fails. DRAGEN SW mode runs on x86 CPU instances, available in all Regions where HealthOmics supports private workflows.

To see which DRAGEN pipelines are supported in DRAGEN SW mode, see the latest Illumina DRAGEN release notes.

## Prerequisites
<a name="dragen-prerequisites"></a>
+ A DRAGEN license from Illumina.
+ A private Amazon ECR repository in the Region where you run the workflow.
+ A VPC with private subnets, a NAT gateway, and a security group that allows outbound HTTPS (port 443). For an example VPC setup, see the [ HealthOmics VPC configuration](https://github.com/aws-samples/sample-healthomics-vpc-configuration) on GitHub.
+ A HealthOmics service role with access to your Amazon ECR repository and your Amazon S3 input and output locations. See [Service roles for AWS HealthOmics](permissions-service.md).

## Get a DRAGEN license
<a name="dragen-get-license"></a>

Subscribe to DRAGEN through Illumina. After you subscribe, Illumina provides the credentials that the DRAGEN container uses to validate the license.

## Build the DRAGEN container image and push it to Amazon ECR
<a name="dragen-build-image"></a>

HealthOmics runs container images from private Amazon ECR repositories in the same Region as the workflow. You need to build the DRAGEN image before you push it to your repository. HealthOmics supports `x86_64` containers. For installation instructions, see the [DRAGEN software mode reference](https://help.dragen.illumina.com/dragen-v4.6/reference/software-mode).

Download the DRAGEN SW mode RPM for DRAGEN 4.6.2 or later from Illumina. For example, the package for version 4.6.2 is `dragen-softwaremode-4.6.2-4.6.2-1.el9.x86_64.rpm`.

Before building the image, extract the DRAGEN installer (`.run` file) without executing it, and inspect the RPMs it contains:

```
sh dragen-4.6.2-*.multi.el9.x86_64.run --noexec --keep --target ./extracted
ls ./extracted            # RPMs, flavors/, installer/, wrapper
```

Install only the packages required for SW mode, and skip the FPGA driver, host services, and bitstream packages:


| Install | Skip (and why) | 
| --- | --- | 
| dragen-paths | dragen\_drv FPGA XDMA kernel drivers (a container can't load kernel modules) | 
| dragen-host | dragen-host-services (no systemd in a task) | 
| dragen | dragen-bitstream-\* (unused in SW mode) | 
| dragen-platform-aws | None | 

Sample Dockerfile:

```
FROM oraclelinux:9
ARG DRAGEN_VERSION=4.6.2

# dnf resolves the RPM's declared deps (bzip2-libs, procps-ng, libgomp, ...)
COPY dragen-softwaremode-${DRAGEN_VERSION}-${DRAGEN_VERSION}-1.el9.x86_64.rpm /tmp/
RUN dnf -y install /tmp/dragen-softwaremode-*.rpm unzip \
    && rm -f /tmp/*.rpm \
    && dnf clean all && rm -rf /var/cache/dnf

# AWS CLI v2, used by tasks that fetch the API key from Secrets Manager
RUN curl -sSL "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o /tmp/awscli.zip \
    && unzip -q /tmp/awscli.zip -d /tmp && /tmp/aws/install && rm -rf /tmp/aws /tmp/awscli.zip

ENV PATH="/opt/dragen/${DRAGEN_VERSION}/bin:${PATH}"
CMD ["dragen", "--version"]
```

HealthOmics requires `linux/amd64` images. Building the image with the `--platform` flag lets you cross-compile from an Apple silicon machine.

```
docker build --platform linux/amd64 -t dragen:4.6.2-sw .
```

Create an Amazon ECR private repository, and then push your DRAGEN Docker image to your Amazon ECR private repository. For more information, see [Pushing a Docker image to an Amazon ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) in the *Amazon ECR User Guide*.

Add a repository policy so that HealthOmics can pull the container image.

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

Add the file that contains all policy statements.

```
aws ecr set-repository-policy --repository-name {{repository-name}} --region us-east-2 \
  --policy-text file://ecr-omics-policy.json
```

For more HealthOmics requirements, see [Container images for private workflows](workflows-ecr.md).

## Configure VPC networking for license validation
<a name="dragen-vpc"></a>

Create the network resources and a HealthOmics configuration resource, as described in [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md). Your runs must use `VPC` networking mode with an active HealthOmics configuration that meets the following requirements:


| Setting | Requirement | 
| --- | --- | 
| Subnets | Private subnets, one per Availability Zone, in Availability Zones where HealthOmics operates. | 
| Routing | Route 0.0.0.0/0 from the private subnets to a NAT gateway, so the task reaches license.dragen.illumina.com. | 
| Security group | Allow outbound TCP 443. To restrict the rule to specific destinations, use the Illumina license endpoints. | 

Verify that your configuration meets the above requirements:

```
aws omics get-configuration --name {{my-vpc-config}} --region us-east-2
```

You can reuse the configuration for all DRAGEN runs in the Region.

## Managing license keys
<a name="dragen-license-keys"></a>

You can keep a copy of your license key in AWS Secrets Manager. Because HealthOmics does not inject secrets into the task environment, the task itself must call Secrets Manager at runtime to retrieve the key before running `dragen`.

Store the key as a secret:

```
aws secretsmanager create-secret \
  --name dragen/illumina-api-key \
  --secret-string file://illumina-api-key.txt \
  --region us-east-2
```

Grant your service role permission to read the secret (see [IAM service execution role](#dragen-iam)), and then retrieve the key inside the task before invoking `dragen`. The DRAGEN container image must include the AWS CLI (or an AWS SDK) to make the call.

For example, add the following to a task's command block, before the `dragen` call. It creates a plain text file named `illumina-api-key.txt` in the `/tmp/` directory. Pass `/tmp/illumina-api-key.txt` to `--api-key-file`.

```
# Fetch the API key at runtime; never echo it.
KEY_FILE=/tmp/illumina-api-key.txt
REGION=$(echo "~{api_key_secret_arn}" | cut -d: -f4)
(umask 077; aws secretsmanager get-secret-value \
  --secret-id "~{api_key_secret_arn}" --region "${REGION}" \
  --query SecretString --output text > "${KEY_FILE}")
```

Because the task already runs in `VPC` networking mode to reach the Illumina license server, the same NAT gateway route provides access to the Secrets Manager API endpoint. To avoid routing this call through the NAT gateway, add a VPC interface endpoint for Secrets Manager instead.

You can also stage the license key as an SSE-encrypted Amazon S3 object and specify the key in the input files for the workflow or workflow tasks. This ensures that the key never appears in the workflow definition or in Amazon CloudWatch.

Amazon S3 file input:

```
aws s3 cp illumina-api-key.txt \
  s3://{{amzn-s3-demo-bucket}}/secrets/illumina-api-key.txt \
  --sse AES256 --region us-east-2
```

Grant the HealthOmics service role read access to that object (see [IAM service execution role](#dragen-iam)), and then reference it as a workflow parameter:

```
{
  "api_key_file": "s3://{{amzn-s3-demo-bucket}}/secrets/illumina-api-key.txt"
}
```

Ensure that the Illumina API key in the workflow inputs is scoped to DRAGEN tasks only.

## Define the DRAGEN task
<a name="dragen-task"></a>

The following WDL example shows the structure of a sample DRAGEN task. You can pass the license key as part of the workflow input parameters, either as a JSON file or inline values. You should also pass the image URI as a workflow input so that HealthOmics can verify access before the run starts. For more information, see [HealthOmics run inputs](workflows-run-inputs.md).

The `dragen` command line process and the resource values depend on your analysis. A minimum of 16 vCPUs and 128 GiB of memory is required to run the process. Illumina recommends up to 64 vCPUs and 256 GiB of memory for some tasks. For more information, see [Task resources in a HealthOmics workflow definition](task-resources.md).

DRAGEN analysis is I/O intensive, and disk throughput can limit performance, affecting total runtime. Illumina recommends local ephemeral storage volumes for optimal performance. You can request increased per-task ephemeral storage using the `disks` directive (or equivalent) in your workflow definition. See [Configuring ephemeral storage size](workflows-ephemeral-storage.md#ephemeral-storage-configure-size).

See the [IlluminaDRAGEN v4.6 User Guide](https://help.dragen.illumina.com/dragen-v4.6/reference/software-mode) for more information on required resources.

**Sample DRAGEN task (WDL)**

```
version 1.0

workflow DragenSwGermline {
    input {
        String dragen_container
        File? hashtable_tar             # reuse an existing hash table; built from ref_fasta when absent
        File? ref_fasta
        File fastq_1
        File fastq_2
        String sample_id
        String api_key_secret_arn       # Secrets Manager ARN; the key itself never becomes a WDL value
        Boolean metering_preview = true # validate the API key without analysis or billing
    }

    call CheckLicenseSecret {
        input:
            secret_arn = api_key_secret_arn,
            dragen_container = dragen_container
    }

    if (!defined(hashtable_tar)) {
        call BuildHashTable {
            input:
                ref_fasta = select_first([ref_fasta]),
                dragen_container = dragen_container
        }
    }

    call DragenGermline {
        input:
            hashtable_tar = select_first([hashtable_tar, BuildHashTable.hashtable]),
            fastq_1 = fastq_1,
            fastq_2 = fastq_2,
            sample_id = sample_id,
            api_key_secret_arn = CheckLicenseSecret.checked_secret_arn,
            metering_preview = metering_preview,
            dragen_container = dragen_container
    }

    output {
        File? hashtable = BuildHashTable.hashtable
        Array[File] dragen_outputs = DragenGermline.outputs
        File dragen_log = DragenGermline.log
    }
}

# Fails fast if the run role can't read the secret or it's empty. Outputs only the ARN.
task CheckLicenseSecret {
    meta {
        volatile: true  # re-check access on every run
    }

    input {
        String secret_arn
        String dragen_container
    }

    command <<<
        set -euo pipefail
        REGION=$(echo "~{secret_arn}" | cut -d: -f4)
        KEY=$(aws secretsmanager get-secret-value \
            --secret-id "~{secret_arn}" --region "${REGION}" \
            --query SecretString --output text)
        if [ -z "${KEY}" ] || [ "${KEY}" = "None" ]; then
            echo "Secret has no SecretString; store it with --secret-string" >&2
            exit 1
        fi
        echo "API key secret is readable (${#KEY} characters)"
    >>>

    runtime {
        container: dragen_container
        cpu: 1
        memory: "2 GiB"
    }

    output {
        String checked_secret_arn = secret_arn
    }
}

# No license check, so this task is safe to call-cache.
task BuildHashTable {
    input {
        File ref_fasta
        String dragen_container
    }

    command <<<
        set -euo pipefail
        mkdir -p hashtable
        dragen --sw-mode --build-hash-table true \
            --ht-reference "~{ref_fasta}" \
            --ht-alt-liftover /opt/dragen/4.6.2/resources/ht_builder/hg38/bwa-kit_hs38DH_liftover.sam \
            --ht-num-threads 16 \
            --output-directory hashtable
        tar -cf hashtable.tar -C hashtable .
    >>>

    runtime {
        container: dragen_container
        cpu: 16
        memory: "128 GiB"
        disks: "200 GiB"
    }

    output {
        File hashtable = "hashtable.tar"
    }
}

task DragenGermline {
    meta {
        volatile: true  # contacts the license server; never reuse cached results
    }

    input {
        File hashtable_tar
        File fastq_1
        File fastq_2
        String sample_id
        String api_key_secret_arn
        Boolean metering_preview
        String dragen_container
    }

    command <<<
        set -euo pipefail
        mkdir -p output /tmp/reference /tmp/dragen-intermediate

        # Fetch the API key at runtime; never echo it.
        KEY_FILE=/tmp/illumina-api-key.txt
        REGION=$(echo "~{api_key_secret_arn}" | cut -d: -f4)
        (umask 077; aws secretsmanager get-secret-value \
            --secret-id "~{api_key_secret_arn}" --region "${REGION}" \
            --query SecretString --output text > "${KEY_FILE}")

        tar -xf "~{hashtable_tar}" -C /tmp/reference

        set +e
        dragen --sw-mode \
            --api-key-file "${KEY_FILE}" \
            -r /tmp/reference \
            -1 "~{fastq_1}" -2 "~{fastq_2}" \
            --RGID "~{sample_id}-rg" --RGSM "~{sample_id}" \
            --enable-map-align true --enable-map-align-output true \
            --enable-variant-caller true \
            --validate-pangenome-reference false \
            --intermediate-results-dir /tmp/dragen-intermediate \
            --output-directory output --output-file-prefix "~{sample_id}" \
            ~{if metering_preview then "--metering-preview" else ""} \
            2>&1 | tee dragen.log
        RC=${PIPESTATUS[0]}
        set -e
        rm -f "${KEY_FILE}"
        [ "${RC}" -eq 0 ] || { echo "DRAGEN failed (${RC})" >&2; exit "${RC}"; }
        touch output/.keep  # metering preview writes no outputs
    >>>

    runtime {
        container: dragen_container
        cpu: 16
        memory: "128 GiB"
        disks: "300 GiB"
    }

    output {
        Array[File] outputs = glob("output/*")
        File log = "dragen.log"
    }
}
```

## Create your workflow
<a name="dragen-create-workflow"></a>

Follow the steps in [Create a private workflow](create-private-workflow.md) using the console, AWS CLI commands, or one of the AWS SDKs.

```
aws omics create-workflow --name dragen-sw-germline \
  --definition-zip fileb://workflow.zip --engine WDL --main main.wdl ...
```

You can use the HealthOmics linter for miniwdl or Nextflow to resolve all errors before deploying.

## IAM service execution role
<a name="dragen-iam"></a>

Create a dedicated least-privilege role. For more detailed instructions, see [IAM permissions for HealthOmics](omics-permissions.md).

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

If you are using AWS Secrets Manager, you need permission to read the secret.

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

Start a run in `VPC` networking mode with your configuration applied and `scratch-storage-mode` set to `LOCAL` to redirect scratch I/O to local disk.

```
aws omics start-run \
  --configuration-name {{my-vpc-config}} \
  --name dragen-sw-germline-run \
  --networking-mode VPC \
  --output-uri s3://{{amzn-s3-demo-bucket}}/runs/ \
  --parameters file://parameters.json \
  --region us-east-2 \
  --role-arn arn:aws:iam::{{123456789012}}:role/dragen-sw-omics-role \
  --scratch-storage-mode LOCAL \
  --storage-type DYNAMIC \
  --workflow-id {{workflow-id}}
```

For more information on setting your run storage type, see [Run storage types in HealthOmics workflows](workflows-run-types.md).

## Considerations
<a name="dragen-considerations"></a>

Local disk  
We recommend that you run DRAGEN with fast local disk on the compute node. You can enable scratch ephemeral storage mounted at `/tmp` by setting `scratchStorageMode` to `LOCAL`. For more information, see [Ephemeral storage for HealthOmics workflow tasks](workflows-ephemeral-storage.md).

Public internet connection  
DRAGEN validates its license over the internet, but the default HealthOmics `RESTRICTED` networking mode blocks outbound calls to the public internet. To run DRAGEN, start the run with `VPC` networking mode enabled and provide a configuration with subnets that route outbound traffic through a NAT gateway to reach `license.dragen.illumina.com` over HTTPS. To learn more, see [Internet access for VPC-connected workflows](workflows-vpc-internet.md).

Call caching  
If you are using call caching, you should exclude tasks that require license checks. The license validation contacts an external service, and a run cache could affect task outputs. You can exclude a task from caching by using a directive in the workflow definition. For instructions on how to exclude a task from call caching, see [Engine-specific caching features](workflow-cache-per-engine.md).

## Troubleshooting
<a name="dragen-troubleshooting"></a>


| Symptom | Likely cause | Action | 
| --- | --- | --- | 
| Task fails at start with a license or connection error in the Amazon CloudWatch Logs log | Run started in RESTRICTED mode | Start the run with --networking-mode VPC and a configuration name. | 
| Same error in VPC mode | Private subnet has no route to a NAT gateway, or the security group blocks port 443 | Check the route table and security group. Run the connectivity test in [Testing VPC connectivity](workflows-vpc-internet.md#vpc-testing-connectivity). | 
| License rejected | Expired trial, exhausted iCredits, or wrong credentials | Check the status of your subscription with Illumina. | 
| AccessDenied pulling the image | Service role or repository policy lacks Amazon ECR permissions | See [Amazon ECR permissions](permissions-ecr.md). | 
| License step fails immediately with HTTP 403 | Used --lic-server (legacy credentials) instead of --api-key-file | Switch to --api-key-file (or --lic-credentials). --lic-server is not supported in SW mode. | 
| Task fails before any license check, even with minimal or test inputs | DRAGEN enforces a hard floor of 16 vCPUs and 120\+ GiB of memory just to validate the command line | Use at least omics.r.4xlarge (16 vCPUs, 128 GiB) for any DRAGEN SW mode task, including dry runs. | 

## Related topics
<a name="dragen-related"></a>
+ [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md)
+ [Internet access for VPC-connected workflows](workflows-vpc-internet.md)
+ [Container images for private workflows](workflows-ecr.md)
+ [Requesting Sentieon licenses for private workflows](private-workflows-subscribe.md)