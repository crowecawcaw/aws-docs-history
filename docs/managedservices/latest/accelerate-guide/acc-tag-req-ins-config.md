# Configuring tags for EC2 instances in Accelerate

AMS Accelerate manages agents on your Amazon EC2 instances, such as the SSM agent and the CloudWatch agent. For more information
about this service offering, see [Automated instance configuration in AMS Accelerate](acc-inst-auto-config.md "acc-inst-auto-config.md")

To opt-in to have your Amazon EC2 instances managed by AMS Accelerate, you must apply the following
tag to your Amazon EC2 instances:

| Key                | Value |
| ------------------ | ----- |
| ams:rt:ams-managed | true  |
