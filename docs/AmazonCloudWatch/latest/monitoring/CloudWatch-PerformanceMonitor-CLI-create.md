

# Create a monitor

The following `create-performance-monitor` example creates a monitor that targets two VPCs.

```
aws networkflowmonitor create-performance-monitor \
    --monitor-name production-vpc-monitor \
    --targets '[{"type":"AWS::EC2::VPC","identifier":"arn:aws:ec2:us-east-1:111122223333:vpc/vpc-0a1b2c3d4e5f67890"},{"type":"AWS::EC2::VPC","identifier":"arn:aws:ec2:us-east-1:111122223333:vpc/vpc-1b2c3d4e5f6a78901"}]'
```