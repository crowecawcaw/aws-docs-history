# Amazon ECS task definitions for 64-bit ARM workloads

Amazon ECS supports using 64-bit ARM applications. You can run your applications on the
platform that's powered by [AWS
Graviton Processors](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/"). It's suitable for a wide variety of workloads. This
includes workloads such as application servers, micro-services, high-performance computing,
CPU-based machine learning inference, video encoding, electronic design automation, gaming,
open-source databases, and in-memory caches.

## Considerations

Before you begin deploying task definitions that use the 64-bit ARM architecture,
consider the following:

- The applications can use the Fargate or EC2s.
- The applications can only use the Linux operating system.
- For the Fargate type, the applications must use Fargate platform version
  `1.4.0` or later.
- The applications can use Fluent Bit or CloudWatch for
  monitoring.
- For the Fargate, the following AWS Regions do not support
  64-bit ARM workloads:
  - US East (N. Virginia), the `us-east-1c` Availability Zone

- For the EC2, see the following to verify that the Region that
  you're in supports the instance type you want to use:

      + [Amazon EC2 M6g Instances](https://aws.amazon.com/ec2/instance-types/m6 "https://aws.amazon.com/ec2/instance-types/m6")
      + [Amazon EC2 T4g
       Instances](https://aws.amazon.com/ec2/instance-types/t4/ "https://aws.amazon.com/ec2/instance-types/t4/")
      + [Amazon EC2 C6g
       Instances](https://aws.amazon.com/ec2/instance-types/c6g/ "https://aws.amazon.com/ec2/instance-types/c6g/")
      + [Amazon EC2 R6gd
       Instances](https://aws.amazon.com/ec2/instance-types/r6/ "https://aws.amazon.com/ec2/instance-types/r6/")
      + [Amazon EC2 X2gd
       Instances](https://aws.amazon.com/ec2/instance-types/x2/ "https://aws.amazon.com/ec2/instance-types/x2/")

  You can also use the Amazon EC2 `describe-instance-type-offerings`
  command with a filter to view the instance offering for your Region.

```
`aws ec2 describe-instance-type-offerings --filters Name=instance-type,Values=`instance-type` --region `region``
```

The following example checks for the M6 instance type availability in the
US East (N. Virginia) (us-east-1) Region.

```
`aws ec2 describe-instance-type-offerings --filters "Name=instance-type,Values=m6*" --region us-east-1`
```

For more information, see [describe-instance-type-offerings](../../../cli/latest/reference/ec2/describe-instance-type-offerings.md "../../../cli/latest/reference/ec2/describe-instance-type-offerings.md") in the _Amazon EC2 Command Line Reference_.
