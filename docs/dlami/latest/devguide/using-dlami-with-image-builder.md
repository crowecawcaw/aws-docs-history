

# Using Deep Learning AMIs with EC2 Image Builder
<a name="using-dlami-with-image-builder"></a>

AWS Deep Learning AMIs (DLAMIs) are now available as Amazon-managed images on [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) service. This integration simplifies the usage of DLAMIs as Base Images and ensures the latest version is used at any given time.

## Available DLAMIs
<a name="available-dlamis"></a>

The following DLAMIs are available as Amazon-managed images found under the **Images section** of the service:
+ [Base AMI with Single CUDA (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-base-with-single-cuda-ami-amazon-linux-2023.html)
+ [Base AMI with Single CUDA (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-base-with-single-cuda-ami-ubuntu-22-04.html)
+ [ARM64 Base AMI with Single CUDA (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-base-with-single-cuda-ami-amazon-linux-2023.html)
+ [ARM64 Base AMI with Single CUDA (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-base-with-single-cuda-ami-ubuntu-22-04.html)

![Amazon Managed Deep Learning Base X86 AMI](http://docs.aws.amazon.com/dlami/latest/devguide/images/deep-learning-base.png)


![Amazon Managed Deep Learning Base ARM64 AMI](http://docs.aws.amazon.com/dlami/latest/devguide/images/deep-learning-arm.png)


## Using DLAMIs as Base Image
<a name="using-dlamis-base-image"></a>

DLAMIs can be used as Base Image during Image Recipe creation.

1. Go to the Image Builder console

1. Select **Image recipes**

1. Select **Create image recipe**

1. In the **Base image** section, select **Quick Start (Amazon-managed)**

1. From the dropdown menu, choose one of the available DLAMIs based on your **Image Operating System (OS)** selection
   + If **Amazon Linux** is selected:
     + Deep Learning Base AMI with Single CUDA Amazon Linux 2023
     + Deep Learning ARM64 Base AMI with Single CUDA Amazon Linux 2023  
![Image Builder recipe creation for Amazon Linux](http://docs.aws.amazon.com/dlami/latest/devguide/images/image-recipe-creation-al2023.png)
   + If **Ubuntu** is selected:
     + Deep Learning Base AMI with Single CUDA Ubuntu 22-04
     + Deep Learning ARM64 Base AMI with Single CUDA Ubuntu 22-04  
![Image Builder recipe creation for Ubuntu](http://docs.aws.amazon.com/dlami/latest/devguide/images/image-recipe-creation-ul22.png)