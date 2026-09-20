

# Understanding the generated network artifacts
<a name="transform-migrations-generated-artifacts"></a>

AWS Transform generates your target network as Infrastructure as Code (IaC) so you can review and deploy it using your own tools and processes. It produces the network in a fraction of the time, and you decide how and when to deploy it: check it against your own standards, adjust it to fit how your team works, deploy it the way you already deploy infrastructure, and keep it in version control so you can track changes and deploy again later.

You can find these artifacts in an Amazon S3 bucket in your target AWS account. AWS Transform writes AWS CDK and CloudFormation for every migration, plus any other formats you selected, to the same location. The bucket is in the AWS account and AWS Region that you specified for the connector and starts with `transform-vmware-target-`. For more information about the connector, see [Step 3: Connector configuration](transform-vmware-connect-target-account.md#transform-vmware-cta-connector).

Use the link provided in AWS Transform to open the generated artifacts in that bucket. The generated artifacts include a `README.md` file that explains how to use the generated templates.

**Important**  
To verify the downloaded file hasn't been corrupted or tampered with, generate and download a checksum, then compare it to a locally generated hash using `openssl dgst -sha256 -binary <file.zip> | base64` command.

## Output directory structure
<a name="transform-migrations-generated-artifacts-layout"></a>

Each IaC format has its own output directory (`cdk/` and `cfn/`, `cdk_l2/`, `terraform/`, or `lza/`). Each contains a `network_segments/` directory for network definitions and a `security/` directory for security definitions. The following trees show the structure of each format, where `<segment>` is a placeholder for each segment:

**CloudFormation** (`cfn/`) contains CloudFormation templates.

```
cfn/
├── network_segments/
│   └── <segment>/                        # CloudFormation template JSON
└── security/
    ├── <segment>_security/
    └── <segment>_security_dependencies/   # only when the segment has cross-VPC rules
```

**CDK L1** (`cdk/`) contains a AWS CDK project. It includes a `README.md` file.

```
cdk/
├── README.md
├── network_segments/
│   └── <segment>/
└── security/
    ├── security-interface.json
    ├── validate-references.py
    ├── <segment>_security/
    └── <segment>_security_dependencies/   # only when the segment has cross-VPC rules
```

**CDK L2** (`cdk_l2/`) contains AWS CDK projects that use higher-level (L2) constructs from the AWS CDK Construct Library. L2 constructs provide sensible defaults and less boilerplate than the L1 constructs that CDK L1 uses. For more information, see [Constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html) in the *AWS Cloud Development Kit (AWS CDK) Developer Guide*. Workload segments are delivered as complete project zip files, and the deployment `README.md` is inside each zip.

```
cdk_l2/
├── network_segments/
│   ├── <segment>/                         # hub and spoke CDK app (.ts source)
│   └── <segment>/                         # workload segment (.zip)
└── security/
    ├── security-interface.json
    ├── validate-references.py
    ├── <segment>_security/                # .zip
    └── <segment>_security_dependencies/   # .ts source, only when the segment has cross-VPC rules
```

**Terraform** (`terraform/`) is delivered as a single zip file.

```
terraform/
├── README.md, LICENSE.txt, main.tf, outputs.tf
├── modules/                                # networking, vpc, workload-vpc
├── network_segments/
│   └── <segment>/                         # main.tf, outputs.tf, variables.tf, versions.tf, terraform.tfvars
└── security/                               # standalone Terraform root
    ├── main.tf, locals.tf, variables.tf, terraform.tfvars
    ├── security-interface.json
    ├── validate-references.py
    ├── modules/security/
    └── security_segments/
        ├── <segment>_security/            # main.tf, variables.tf, terraform.tfvars (plus versions.tf for cross-account segments)
        └── <segment>_security_dependencies/   # only when the segment has cross-VPC rules
```

**LZA** (`lza/`) contains Landing Zone Accelerator configuration files and per-VPC AWS CDK applications.

```
lza/
├── README.md
├── network_segments/
│   ├── network-config.yaml
│   └── replacements-config.yaml
└── security/
    ├── <segment>/                          # one CDK app per VPC segment
    │   ├── <stack_name>.ts                 #   security group stack
    │   ├── app.ts
    │   ├── cdk.json
    │   ├── tsconfig.json
    │   └── package.json
    └── <segment>_dependencies/             # same file set; only when the segment has cross-VPC rules
```

## Security definitions
<a name="transform-migrations-generated-artifacts-security"></a>

Within `security/`, security groups are split per segment. Each segment's own security groups are in its `<segment>_security/` directory. If a segment has rules that reference another segment, its cross-VPC rules are separated into a `<segment>_security_dependencies/` directory that deploys last, after the security groups it references exist.

A segment whose VPC already exists in the account keeps its original name under `security/<segment>/` with no suffix.

The `cdk/`, `cdk_l2/`, and `terraform/` outputs include two additional files in `security/`:
+ `security-interface.json` lists the network identifiers each segment consumes, with one entry per segment. The identifier type depends on the format: CloudFormation export names for CloudFormation, CDK L1, and CDK L2, or SSM parameter names for Terraform. A segment that imports nothing has no entry.
+ `validate-references.py` is a script you run before you deploy a segment. It confirms that the network identifiers in `security-interface.json` already exist in your AWS account. Running it requires the AWS CLI, with credentials configured for the target account and Region.

**Note**  
Deploy the resources in `network_segments/` before those in `security/`. The security definitions reference the network resources' exports and parameters, which must already exist.

## Multi-account output
<a name="transform-migrations-generated-artifacts-accounts"></a>

A multi-account deployment adds one per-format manifest file at the root of the output directory. A single-account deployment has no manifest files. Each format has its own manifest:
+ `manifest-cdk_l1.json` for the AWS CDK L1 format.
+ `manifest-cdk_l2.json` for the AWS CDK L2 format.
+ `manifest-terraform.json` for the Terraform format, at the `terraform/` root.
+ `manifest-lza.json` for the LZA format.

Account assignment is not shown by the folder structure. It is carried in data fields: each manifest lists its segments with a target account (the manifest's `segments[].targetAccount` field), and each entry in `security-interface.json` has a `targetAccount` field.