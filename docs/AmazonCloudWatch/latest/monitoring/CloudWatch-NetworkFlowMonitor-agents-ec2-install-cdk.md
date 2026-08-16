# Install agents for EC2 instances by using CDK

You can use AWS Cloud Development Kit (AWS CDK) to install the Network Flow Monitor agent as part of your infrastructure-as-code deployment.
Add the agent installation to your EC2 instance user data in your CDK stack.

The following example shows how to install the Network Flow Monitor agent on an Amazon Linux instance using CDK with TypeScript:

```
// Create an EC2 instance
const ec2Instance = new ec2.Instance(this, 'Instance', {
  vpc,
  instanceType: ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
  machineImage: ec2.MachineImage.latestAmazonLinux2023(),
  vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS },
});

// Install Network Flow Monitor Agent via RPM on Amazon Linux (x86_64)
ec2Instance.addUserData(
  "sudo yum install https://networkflowmonitoragent.awsstatic.com/latest/x86_64/network-flow-monitor-agent.rpm -y"
);

// Attach the required permissions policy to your EC2 instance role
ec2Instance.role.addManagedPolicy(
  iam.ManagedPolicy.fromAwsManagedPolicyName('CloudWatchNetworkFlowMonitorAgentPublishPolicy')
);
```

For ARM64 (Graviton) instances, replace the RPM URL with the ARM64 variant:

```
ec2Instance.addUserData(
  "sudo yum install https://networkflowmonitoragent.awsstatic.com/latest/arm64/network-flow-monitor-agent.rpm -y"
);
```

For Debian/Ubuntu instances, use the DEB package instead:

```
ec2Instance.addUserData(
  "wget https://networkflowmonitoragent.awsstatic.com/latest/x86_64/network-flow-monitor-agent.deb && sudo apt-get install ./network-flow-monitor-agent.deb -y"
);
```
