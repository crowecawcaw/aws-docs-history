# Deploy Deadline Cloud farms with the AWS CDK

The
[starter\_farm](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cdk/farm_templates/starter_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cdk/farm_templates/starter_farm")
AWS CDK app in the deadline-cloud-samples repository on the GitHub website deploys Deadline Cloud
farms from reusable TypeScript constructs that wrap the `CfnFarm`,
`CfnQueue`, and `CfnFleet` L1 resources from
`aws-cdk-lib/aws-deadline`. For a comparison of the AWS CDK with CloudFormation and
Terraform, see [Manage Deadline Cloud infrastructure as code](infrastructure-as-code.md "infrastructure-as-code.md").

The app contains four example farms, each a separate AWS CDK stack:

- `SimpleFarm` – A single Linux fleet on one queue. Deploy
  `SimpleFarm` when you are getting started.
- `StarterFarm` – Adds a private conda channel and a queue that
  builds packages for it.
- `CudaFarm` – A GPU fleet, with `conda-forge` for
  the CUDA toolchain.
- `MultiPlatformFarm` – One queue reaching Linux, Windows,
  and GPU fleets.
  Every stack creates a farm and an Amazon S3 bucket for job attachments. Each stack also
  includes at least one queue with a conda queue environment, at least one
  service-managed fleet, and one IAM role for each queue and each fleet.

To deploy, you need Node.js 18 or later, AWS credentials, an account and region
bootstrapped for the AWS CDK, and a Deadline Cloud monitor. Then run:

```
cd cdk/farm_templates/starter_farm
npm ci
npx cdk deploy SimpleFarm
```
