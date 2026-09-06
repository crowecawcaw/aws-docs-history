

# Release notes for AWS PCS sample AMIs
<a name="ami-release-notes"></a>

AMIs for the latest supported major versions of the scheduler receive security updates and critical bug fixes. These incremental security patches aren't included in official release notes.

**Important**  
Sample AMIs related to old scheduler versions aren't supported and don't receive updates.

**Important**  
Sample AMIs are for demonstration purposes and are not recommended for production workloads.

**Contents**
+ [Sample AMIs for x86\_64](#ami-release-notes_x86)
+ [Sample AMIs for Arm64](#ami-release-notes_arm64)

## AWS PCS sample AMIs for x86\_64
<a name="ami-release-notes_x86"></a>

### Slurm 25.11
<a name="ami-release-notes_x86_slurm-25.11"></a>

**AMI name**
+  `aws-pcs-sample_ami-al2023-x86_64-slurm-25.11` 

**Supported EC2 instances**
+ All instances with an 64-bit x86 processor. To find compatible instances, navigate to the Amazon EC2 console. Choose Instance Types, then search for Architectures=x86\_64.

**AMI contents**
+ Supported AWS Service: AWS PCS
+ Operating System: Amazon Linux 2023
+ Compute Architecture: x86\_64
+ EBS volume type: gp2
+ EFA Installer: 1.47.0
+ GDRCopy: 2.5.1
+ NVIDIA Driver: 590.48.01
+ NVIDIA CUDA: 13.1\_590.48.01

### Slurm 25.05
<a name="ami-release-notes_x86_slurm-25.05"></a>

**AMI name**
+  `aws-pcs-sample_ami-amzn2-x86_64-slurm-25.05` 

**Supported EC2 instances**
+ All instances with an 64-bit x86 processor. To find compatible instances, navigate to the Amazon EC2 console. Choose Instance Types, then search for Architectures=x86\_64.

**AMI contents**
+ Supported AWS Service: AWS PCS
+ Operating System: Amazon Linux 2
+ Compute Architecture: x86\_64
+ EBS volume type: gp2
+ EFA Installer: 1.43.1
+ GDRCopy: 2.5.1
+ NVIDIA Driver: 550.127.08
+ NVIDIA CUDA: 12.4.1\_550.54.15

### Slurm 24.11
<a name="ami-release-notes_x86_slurm-24.11"></a>

**Note**  
AWS PCS supports accounting for Slurm 24.11 and later. For more information, see [Slurm accounting in AWS PCS](slurm-accounting.md). 

**AMI name**
+  `aws-pcs-sample_ami-amzn2-x86_64-slurm-24.11` 

**Supported EC2 instances**
+  All instances with an 64-bit x86 processor. To find compatible instances, navigate to the [Amazon EC2 console](https://console.aws.amazon.com/ec2). Choose **Instance Types**, then search for `Architectures=x86_64`.

**AMI contents**
+ Supported AWS Service: AWS PCS
+  Operating System: Amazon Linux 2
+  Compute Architecture: x86\_64
+  EBS volume type: gp2
+  EFA Installer: 1.33.0
+  GDRCopy: 2.4
+  NVIDIA Driver: 550.127.08
+  NVIDIA CUDA: 12.4.1\_550.54.15

### Slurm 24.05
<a name="ami-release-notes_x86_slurm-24.05"></a>

**AMI name**
+  `aws-pcs-sample_ami-amzn2-x86_64-slurm-24.05` 

**Supported EC2 instances**
+  All instances with an 64-bit x86 processor. To find compatible instances, navigate to the [Amazon EC2 console](https://console.aws.amazon.com/ec2). Choose **Instance Types**, then search for `Architectures=x86_64`.

**AMI contents**
+ Supported AWS Service: AWS PCS
+  Operating System: Amazon Linux 2
+  Compute Architecture: x86\_64
+  EBS volume type: gp2
+  EFA Installer: 1.33.0
+  GDRCopy: 2.4
+  NVIDIA Driver: 550.127.08
+  NVIDIA CUDA: 12.4.1\_550.54.15

### Slurm 23.11
<a name="ami-release-notes_x86_slurm-23.11"></a>

**AMI name**
+  `aws-pcs-sample_ami-amzn2-x86_64-slurm-23.11` 

**Supported EC2 instances**
+  All instances with an 64-bit x86 processor. To find compatible instances, navigate to the [Amazon EC2 console](https://console.aws.amazon.com/ec2). Choose **Instance Types**, then search for `Architectures=x86_64`.

**AMI contents**
+ Supported AWS Service: AWS PCS
+  Operating System: Amazon Linux 2
+  Compute Architecture: x86\_64
+  EBS volume type: gp2
+  EFA Installer: 1.33.0
+  GDRCopy: 2.4
+  NVIDIA Driver: 550.127.08
+  NVIDIA CUDA: 12.4.1\_550.54.15

## AWS PCS sample AMIs for Arm64
<a name="ami-release-notes_arm64"></a>

### Slurm 25.11
<a name="ami-release-notes_arm64_slurm-25.11"></a>

**AMI name**
+  `aws-pcs-sample_ami-al2023-arm64-slurm-25.11` 

**Supported EC2 instances**
+ All instances with a 64-bit Arm processor. To find compatible instances, navigate to the Amazon EC2 console. Choose Instance Types, then search for Architectures=arm64.

**AMI contents**
+ Supported AWS Service: AWS PCS
+ Operating System: Amazon Linux 2023
+ Compute Architecture: arm64
+ EBS volume type: gp2
+ EFA Installer: 1.47.0
+ GDRCopy: 2.5.1
+ NVIDIA Driver: 590.48.01
+ NVIDIA CUDA: 13.1\_590.48.01

### Slurm 25.05
<a name="ami-release-notes_arm64_slurm-25.05"></a>

**AMI name**
+  `aws-pcs-sample_ami-amzn2-arm64-slurm-25.05` 

**Supported EC2 instances**
+ All instances with an 64-bit Arm processor. To find compatible instances, navigate to the Amazon EC2 console. Choose Instance Types, then search for Architectures=arm64.

**AMI contents**
+ Supported AWS Service: AWS PCS
+ Operating System: Amazon Linux 2
+ Compute Architecture: arm64
+ EBS volume type: gp2
+ EFA Installer: 1.43.1
+ GDRCopy: 2.5.1
+ NVIDIA Driver: 550.127.08
+ NVIDIA CUDA: 12.4.1\_550.54.15

### Slurm 24.11
<a name="ami-release-notes_arm64_slurm-24.11"></a>

**Note**  
AWS PCS supports accounting for Slurm 24.11 and later. For more information, see [Slurm accounting in AWS PCS](slurm-accounting.md). 

**AMI name**
+  `aws-pcs-sample_ami-amzn2-arm64-slurm-24.11` 

**Supported EC2 instances**
+  All instances with an 64-bit Arm processor. To find compatible instances, navigate to the [Amazon EC2 console](https://console.aws.amazon.com/ec2). Choose **Instance Types**, then search for `Architectures=arm64`.

**AMI contents**
+ Supported AWS Service: AWS PCS
+  Operating System: Amazon Linux 2
+  Compute Architecture: arm64
+  EBS volume type: gp2
+  EFA Installer: 1.33.0
+  GDRCopy: 2.4
+  NVIDIA Driver: 550.127.08
+  NVIDIA CUDA: 12.4.1\_550.54.15

### Slurm 24.05
<a name="ami-release-notes_arm64_slurm-24.05"></a>

**AMI name**
+  `aws-pcs-sample_ami-amzn2-arm64-slurm-24.05` 

**Supported EC2 instances**
+  All instances with an 64-bit Arm processor. To find compatible instances, navigate to the [Amazon EC2 console](https://console.aws.amazon.com/ec2). Choose **Instance Types**, then search for `Architectures=arm64`.

**AMI contents**
+ Supported AWS Service: AWS PCS
+  Operating System: Amazon Linux 2
+  Compute Architecture: arm64
+  EBS volume type: gp2
+  EFA Installer: 1.33.0
+  GDRCopy: 2.4
+  NVIDIA Driver: 550.127.08
+  NVIDIA CUDA: 12.4.1\_550.54.15

### Slurm 23.11
<a name="ami-release-notes_arm64_slurm-23.11"></a>

**AMI name**
+  `aws-pcs-sample_ami-amzn2-arm64-slurm-23.11` 

**Supported EC2 instances**
+  All instances with an 64-bit Arm processor. To find compatible instances, navigate to the [Amazon EC2 console](https://console.aws.amazon.com/ec2). Choose **Instance Types**, then search for `Architectures=arm64`.

**AMI contents**
+ Supported AWS Service: AWS PCS
+  Operating System: Amazon Linux 2
+  Compute Architecture: arm64
+  EBS volume type: gp2
+  EFA Installer: 1.33.0
+  GDRCopy: 2.4
+  NVIDIA Driver: 550.127.08
+  NVIDIA CUDA: 12.4.1\_550.54.15