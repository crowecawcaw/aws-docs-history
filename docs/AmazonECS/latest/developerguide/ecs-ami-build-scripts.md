# Amazon ECS-optimized Linux AMI build script

Amazon ECS has open-sourced the build scripts that are used to build the Linux variants of
the Amazon ECS-optimized AMI. These build scripts are now available on GitHub. For more
information, see [amazon-ecs-ami](https://github.com/aws/amazon-ecs-ami "https://github.com/aws/amazon-ecs-ami") on GitHub.

If you need to customize the Amazon ECS-optimized AMI , see [Amazon ECS Optimized AMI Build
Recipies](https://github.com/aws/amazon-ecs-ami "https://github.com/aws/amazon-ecs-ami") on GitHub.

The build scripts repository includes a [HashiCorp
packer](https://developer.hashicorp.com/packer/docs "https://developer.hashicorp.com/packer/docs") template and build scripts to generate each of the Linux variants of
the Amazon ECS-optimized AMI. These scripts are the source of truth for Amazon ECS-optimized
AMI builds, so you can follow the GitHub repository to monitor changes to our AMIs.
For example, perhaps you want your own AMI to use the same version of Docker that the
Amazon ECS team uses for the official AMI.

For more information, see the Amazon ECS AMI repository at [aws/amazon-ecs-ami](https://github.com/aws/amazon-ecs-ami "https://github.com/aws/amazon-ecs-ami") on
GitHub.

###### To build an Amazon ECS-optimized Linux AMI

1. Clone the `aws/amazon-ecs-ami` GitHub repo.

```
`git clone https://github.com/aws/amazon-ecs-ami.git`
```

2. Add an environment variable for the AWS Region to use when creating the
   AMI. Replace the `us-west-2` value with the Region to use.

```
export REGION=`us-west-2`
```

3. A Makefile is provided to build the AMI. From the root directory of the
   cloned repository, use one of the following commands, corresponding to the Linux
   variant of the Amazon ECS-optimized AMI you want to build.
   - Amazon ECS-optimized Amazon Linux 2 AMI

   ```
   make al2
   ```

   - Amazon ECS-optimized Amazon Linux 2 (arm64) AMI

   ```
   make al2arm
   ```

   - Amazon ECS GPU-optimized AMI

   ```
   make al2gpu
   ```

   - Amazon ECS optimized Amazon Linux 2 (Neuron) AMI

   ```
   make al2inf
   ```

   - Amazon ECS-optimized Amazon Linux 2023 AMI

   ```
   make al2023
   ```

   - Amazon ECS-optimized Amazon Linux 2023 (arm64) AMI

   ```
   make al2023arm
   ```

   - Amazon ECS-optimized Amazon Linux 2023 GPU AMI

   ```
   make al2023gpu
   ```

   - Amazon ECS optimized Amazon Linux 2023 (Neuron) AMI

   ```
   make al2023neu
   ```
