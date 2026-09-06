

# Compute images supported with the CodeBuild-hosted GitHub Actions runner
<a name="sample-github-action-runners-update-yaml.images"></a>

In the label you configured in [Tutorial: Configure a CodeBuild-hosted GitHub Actions runner](action-runner.md), you can override your Amazon EC2 environment settings by using the values in the first three columns. CodeBuild provides the following Amazon EC2 compute images. For more information about 

<a name="build-env-ref.supported-images"></a>

- ** `linux` **
  - **Image identifier:** `4.0`
  - **Instance size:** `small`<br />`medium`<br />`large`<br />`xlarge`<br />`2xlarge`<br />`gpu_small`<br />`gpu_large`
  - **Platform:** Amazon Linux 2
  - **Resolved image:** aws/codebuild/amazonlinux-x86\_64-standard:4.0
  - **Definition:** [al/standard/4.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/4.0)

- ** `linux` **
  - **Image identifier:** `5.0`
  - **Platform:** Amazon Linux 2023
  - **Resolved image:** aws/codebuild/amazonlinux-x86\_64-standard:5.0
  - **Definition:** [al/standard/5.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/5.0)

- ** `linux-ec2` **
  - **Image identifier:** `latest`
  - **Instance size:** `small`<br />`medium`<br />`large`
  - **Platform:**  Amazon Linux 2023 
  - **Resolved image:** aws/codebuild/ami/amazonlinux-x86\_64-base:latest
  - **Definition:**  None 

- ** `arm` **
  - **Image identifier:** `2.0`
  - **Instance size:** `small`<br />`medium`<br />`large`<br />`xlarge`<br />`2xlarge`
  - **Platform:** Amazon Linux 2
  - **Resolved image:** aws/codebuild/amazonlinux-aarch64-standard:2.0
  - **Definition:** [al/aarch64/standard/2.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/aarch64/standard/2.0)

- ** `arm` **
  - **Image identifier:** `3.0`
  - **Platform:** Amazon Linux 2023
  - **Resolved image:** aws/codebuild/amazonlinux-aarch64-standard:3.0
  - **Definition:** [al/aarch64/standard/3.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/aarch64/standard/3.0)

- ** `arm-ec2` **
  - **Image identifier:** `latest`
  - **Instance size:** `small`<br />`medium`<br />`large`
  - **Platform:**  Amazon Linux 2023 
  - **Resolved image:** aws/codebuild/ami/amazonlinux-arm-base:latest
  - **Definition:**  None 

- ** `ubuntu` **
  - **Image identifier:** `5.0`
  - **Instance size:** `small`<br />`medium`<br />`large`<br />`xlarge`<br />`2xlarge`<br />`gpu_small`<br />`gpu_large`
  - **Platform:** Ubuntu 20.04
  - **Resolved image:** aws/codebuild/standard:5.0
  - **Definition:** [ubuntu/standard/5.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/ubuntu/standard/5.0)

- ** `ubuntu` **
  - **Image identifier:** `6.0`
  - **Platform:** Ubuntu 22.04
  - **Resolved image:** aws/codebuild/standard:6.0
  - **Definition:** [ubuntu/standard/6.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/ubuntu/standard/6.0)

- ** `ubuntu` **
  - **Image identifier:** `7.0`
  - **Platform:** Ubuntu 22.04
  - **Resolved image:** aws/codebuild/standard:7.0
  - **Definition:** [ubuntu/standard/7.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/ubuntu/standard/7.0)

- ** `windows` **
  - **Image identifier:** `1.0`
  - **Instance size:** `medium`<br />`large`
  - **Platform:** Windows Server Core 2019 / **Resolved image:** aws/codebuild/windows-base:2019-1.0 / **Definition:** N/A
  - **Platform:** Windows Server Core 2022 / **Resolved image:** aws/codebuild/windows-base:2022-1.0 / **Definition:** N/A

- ** `windows` **
  - **Image identifier:** `2.0`
  - **Platform:** Windows Server Core 2019
  - **Resolved image:** aws/codebuild/windows-base:2019-2.0
  - **Definition:** N/A

- ** `windows` **
  - **Image identifier:** `3.0`
  - **Platform:** Windows Server Core 2019
  - **Resolved image:** aws/codebuild/windows-base:2019-3.0
  - **Definition:** N/A

- ** `windows-ec2` **
  - **Image identifier:** `2022`
  - **Instance size:** `medium`<br />`large`
  - **Platform:** Windows Server Core 2022 
  - **Resolved image:** aws/codebuild/ami/windows-base:2022
  - **Definition:**  None 



In addition, you can override your Lambda environment settings by using the following values. For more information about CodeBuild Lambda compute, see [Run builds on AWS Lambda compute](lambda.md). CodeBuild supports the following Lambda compute images:

<a name="lambda.supported-images"></a>
<table>
<thead>
  <tr><th>Environment type</th><th>Image identifier</th><th>Instance size</th><th></th><th></th><th></th></tr>
</thead>
<tbody>
  <tr><td><code>linux-lambda</code></td><td rowspan="2"><code>dotnet6</code><br /><code>go1.21</code><br /><code>corretto11</code><br /><code>corretto17</code><br /><code>corretto21</code><br /><code>nodejs18</code><br /><code>nodejs20</code><br /><code>python3.11</code><br /><code>python3.12</code><br /><code>ruby3.2</code></td><td rowspan="2"><code>1GB</code><br /><code>2GB</code><br /><code>4GB</code><br /><code>8GB</code><br /><code>10GB</code></td><td></td><td></td><td></td></tr>
  <tr><td><code>arm-lambda</code></td><td></td><td></td><td></td></tr>
</tbody>
</table>


For more information, see [Build environment compute modes and types](build-env-ref-compute-types.md) and [Docker images provided by CodeBuild](build-env-ref-available.md).