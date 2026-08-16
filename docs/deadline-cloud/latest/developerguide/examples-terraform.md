# Deploy Deadline Cloud farms with Terraform

The
[terraform](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/terraform "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/terraform")
directory in the deadline-cloud-samples repository on the GitHub website contains
Terraform configurations that deploy Deadline Cloud farms with
`awscc_deadline_*` resources from the AWSCC provider. For a comparison of
Terraform with CloudFormation and the AWS CDK, see
[Manage Deadline Cloud infrastructure as code](infrastructure-as-code.md "infrastructure-as-code.md").

The
[starter\_farm](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/terraform/farm_templates/starter_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/terraform/farm_templates/starter_farm")
configuration on the GitHub website is the Terraform equivalent of the
CloudFormation starter farm ([Deploy a starter Deadline Cloud farm with CloudFormation](examples-cfn-starter-farm.md "examples-cfn-starter-farm.md")). It deploys a farm
with a production queue and a package build queue. The farm includes up to three
service-managed fleets: CPU Linux, CPU Windows, and CUDA Linux. A conda queue
environment uses a private conda channel on an Amazon S3 bucket you provide, plus the
`deadline-cloud` channel.

To deploy the starter farm, you need Terraform 1.0 or later, AWS
credentials, an Amazon S3 bucket for job attachments and the conda channel, and a Deadline Cloud
monitor. Set the required `job_attachments_bucket_name` variable, then
run:

```
cd terraform/farm_templates/starter_farm
terraform init
terraform apply
```

The
[knfsd\_xregion\_cache](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/terraform/farm_templates/knfsd_xregion_cache "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/terraform/farm_templates/knfsd_xregion_cache")
configuration on the GitHub website deploys a service-managed fleet that reads a
distant NFS filer through a KNFSD read cache over a VPC resource endpoint. Use it as a
starting point when your fleet caches reads from an on-premises or otherwise-distant
filer.
