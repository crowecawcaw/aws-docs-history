# EC2 compute images

AWS CodeBuild supports the following Docker images that are available for EC2 compute in CodeBuild.

###### Note

The base image of the Windows Server Core 2019 platform is only available in the following
regions:

- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- Europe (Ireland)

| Platform                 | Image identifier                                       | Definition                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Linux 2           | `aws/codebuild/amazonlinux-x86_64-standard:4.0`        | [al/standard/4.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/4.0 "https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/4.0")                      |
| Amazon Linux 2023        | `aws/codebuild/amazonlinux-x86_64-standard:5.0`        | [al/standard/5.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/5.0 "https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/5.0")                      |
| Amazon Linux 2           | `aws/codebuild/amazonlinux-x86_64-standard:corretto8`  | [al/standard/corretto8](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/corretto8 "https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/corretto8")    |
| Amazon Linux 2           | `aws/codebuild/amazonlinux-x86_64-standard:corretto11` | [al/standard/corretto11](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/corretto11 "https://github.com/aws/aws-codebuild-docker-images/tree/master/al/x86_64/standard/corretto11") |
| Amazon Linux 2           | `aws/codebuild/amazonlinux-aarch64-standard:2.0`       | [al/aarch64/standard/2.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/aarch64/standard/2.0 "https://github.com/aws/aws-codebuild-docker-images/tree/master/al/aarch64/standard/2.0")            |
| Amazon Linux 2023        | `aws/codebuild/amazonlinux-aarch64-standard:3.0`       | [al/aarch64/standard/3.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/al/aarch64/standard/3.0 "https://github.com/aws/aws-codebuild-docker-images/tree/master/al/aarch64/standard/3.0")            |
| Ubuntu 20.04             | `aws/codebuild/standard:5.0`                           | [ubuntu/standard/5.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/ubuntu/standard/5.0 "https://github.com/aws/aws-codebuild-docker-images/tree/master/ubuntu/standard/5.0")                        |
| Ubuntu 22.04             | `aws/codebuild/standard:6.0`                           | [ubuntu/standard/6.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/ubuntu/standard/6.0 "https://github.com/aws/aws-codebuild-docker-images/tree/master/ubuntu/standard/6.0")                        |
| Ubuntu 22.04             | `aws/codebuild/standard:7.0`                           | [ubuntu/standard/7.0](https://github.com/aws/aws-codebuild-docker-images/tree/master/ubuntu/standard/7.0 "https://github.com/aws/aws-codebuild-docker-images/tree/master/ubuntu/standard/7.0")                        |
| Windows Server Core 2019 | `aws/codebuild/windows-base:2019-1.0`                  | N/A                                                                                                                                                                                                                   |
| Windows Server Core 2019 | `aws/codebuild/windows-base:2019-2.0`                  | N/A                                                                                                                                                                                                                   |
| Windows Server Core 2019 | `aws/codebuild/windows-base:2019-3.0`                  | N/A                                                                                                                                                                                                                   |
| Windows Server Core 2022 | `aws/codebuild/windows-base:2022-1.0`                  | N/A                                                                                                                                                                                                                   |
| macOS                    | `aws/codebuild/macos-arm-base:14`                      | N/A                                                                                                                                                                                                                   |

###### Note

On November 22nd, 2024, the aliases for Linux-based standard runtime images were updated from
`amazonlinux2` to `amazonlinux`. No manual update is required as the previous
aliases are still valid.
