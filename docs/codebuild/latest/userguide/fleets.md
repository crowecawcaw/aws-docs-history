# Reserved capacity fleet

properties

A reserved capacity fleet contains the following properties. For more
information about reserved capacity fleets, see [Run builds on reserved capacity fleets](fleets.md "fleets.md").

**Operating system**

The operating system. The following operating systems are
available:

- Amazon Linux
- macOS
- Windows Server 2019
- Windows Server 2022

**Architecture**

The processor architecture. The following architectures are
available:

- x86_64
- Arm64

**Environment type**

The environment types available when **Amazon Linux** is selected. The following environment types are
available:

- Linux EC2
- Linux GPU

**Compute instance type**

The compute configurations for fleet instances.

**Guided selection**

Specify different compute types by
selecting vCPU, memory and disk space settings. For information about compute type availability
by region, see [About reserved capacity environment types](build-env-ref-compute-types.md#environment-reserved-capacity.types "build-env-ref-compute-types.md#environment-reserved-capacity.types").

**Custom instance**

Manually specify the desired instance type.

**Capacity**

The initial number of machines allocated to the fleet, which defines the
number of builds that can run in parallel.

**Overflow behavior**

Defines the behavior when the number of builds exceeds the fleet
capacity.

**On-demand**

Overflow builds run on CodeBuild on-demand.

###### Note

If you choose to set your overflow behavior to on-demand
while creating a VPC-connected fleet, make sure that you add
the required VPC permissions to your project service role.
For more information, see [Example policy statement to allow CodeBuild access to AWS
services required to create a VPC network
interface](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-create-vpc-network-interface "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-create-vpc-network-interface").

###### Important

If you choose to set your overflow behavior to on-demand,
note that overflow builds will be billed separately, similar
to on-demand Amazon EC2. For more information, see [https://aws.amazon.com/codebuild/pricing/](https://aws.amazon.com/codebuild/pricing/ "https://aws.amazon.com/codebuild/pricing/").

**Queue**

Build runs are placed in a queue until a machine is available.
This limits additional costs because no additional machines are
allocated.

**Amazon Machine Images (AMI)**

The Amazon Machine Image (AMI) properties for your fleet. The following properties are supported by CodeBuild:

| AWS Regions      | Organization ARN                                                | Organization ID |
| ---------------- | --------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `us-east-1`      | `arn:aws:organizations::851725618577:organization/o-c6wcu152r1` | `o-c6wcu152r1`  |
| `us-east-2`      | `arn:aws:organizations::992382780434:organization/o-seufr2suvq` | `o-seufr2suvq`  |
| `us-west-2`      | `arn:aws:organizations::381491982620:organization/o-0412o99a4r` | `o-0412o99a4r`  |
| `ap-northeast-1` | `arn:aws:organizations::891376993293:organization/o-b6k3sjqavm` | `o-b6k3sjqavm`  |
| `ap-south-1`     | `arn:aws:organizations::891376924779:organization/o-krtah1lkeg` | `o-krtah1lkeg`  |
| `ap-southeast-1` | `arn:aws:organizations::654654522137:organization/o-mcn8uvc3tp` | `o-mcn8uvc3tp`  |
| `ap-southeast-2` | `arn:aws:organizations::767398067170:organization/o-6crt0f6bu4` | `o-6crt0f6bu4`  |
| `eu-central-1`   | `arn:aws:organizations::590183817084:organization/o-lb2lne3te6` | `o-lb2lne3te6`  |
| `eu-west-1`      | `arn:aws:organizations::891376938588:organization/o-ullrrg5qf0` | `o-ullrrg5qf0`  |
| `sa-east-1`      | `arn:aws:organizations::533267309133:organization/o-db63c45ozw` | `o-db63c45ozw`  | **Additional configuration** **VPC - optional** The VPC that your CodeBuild fleet will access. For more information, see [Use AWS CodeBuild with Amazon Virtual Private Cloud](vpc-support.md "vpc-support.md"). ###### Note If a fleet override is specified when calling the StartBuild API, CodeBuild will ignore the project VPC configuration. **Subnets** The VPC subnets that CodeBuild uses to set up your VPC configuration. Note that reserved capacity fleets support only one subnet in a single Availablity Zone. Also, ensure that your subnets include a NAT gateway. **Security groups** The VPC security groups that CodeBuild uses with your VPC. Ensure that your security groups allow outbound connections. **Fleet Service Role** Defines the service role for your fleet from an existing service role in your account. **Define proxy configurations - optional** Proxy configurations that apply network access control to your reserved capacity instances. For more information, see [Use AWS CodeBuild with a managed proxy server](run-codebuild-in-managed-proxy-server.md "run-codebuild-in-managed-proxy-server.md"). ###### Note Proxy configurations don't support VPC, Windows, or MacOS. **Default behavior** Defines the behavior of outgoing traffic. **Allow** Allows outgoing traffic to all destinations by default. **Deny** Denies outgoing traffic to all destinations by default. **Proxy rules** Specifies destination domains or IPs to allow or deny network access control to. |
