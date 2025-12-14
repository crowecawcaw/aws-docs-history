# Cloud game development (CGD)

Cloud game development (CGD) refers to the infrastructure and
tools that are required for the game development lifecycle to
build, test, and develop a game. Game development is collaborative
between users and the infrastructure requirements frequently
change throughout the stages of development.

Many game developers are embracing globally distributed and remote
development teams, which requires technology that supports this
type of development. Game developers can host all or part of these
environments in AWS and use the global availability of AWS Regions
to place resources closer to users and manage their development
environments more cost-effectively by scaling compute and storage
as needed.

The environments can vary depending on game developer needs, but
they typically include developer workstations for artists,
designers, engineers, QA testers, contractors, and other personnel
to perform their work. These environments also typically include a
build farm comprised of source code repositories for users to
check-in their changes and the CI/CD infrastructure for building,
packaging, and testing the developed artifacts.

These game production architectures have the following
characteristics:

- Users should be able to access a virtual workstation through a
  web browser or local desktop client, such as
  [Amazon DCV](https://aws.amazon.com/hpc/dcv/ "https://aws.amazon.com/hpc/dcv/"), that provides them with a low latency streaming
  session to access the same software and tools that they would
  have access to if they were working on a machine in an office
  or development studio. These virtual workstations, typically a
  cloud-based server, should allow a user to collaborate and
  work on their projects entirely in a cloud environment over a
  LAN or WAN. When users are not actively using the machines,
  their work should be backed up to durable cloud storage, for
  example a source control repository or file system such
  as [Amazon Elastic File System (EFS)](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") and
  [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/"), and their machine should be shut down to reduce
  costs.
- Source control repositories, such as Perforce, should be
  designed with high availability using replication between
  Availability Zones or between on-premises environments with
  backups stored in cloud storage such
  as [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"). For example, a cloud-based Perforce server should
  include a primary commit server hosted in one Availability
  Zone with replication to a standby server hosted in another
  Availability Zone in the same Region.
- Game development build farm resources should be designed with
  automatic scaling so that compute resources are provisioned as
  they are required,
  and [EC2
  Spot Instances](https://aws.amazon.com/ec2/spot/ "https://aws.amazon.com/ec2/spot/") should be used to reduce the costs
  incurred when scaling out the number of servers required for
  builds.
