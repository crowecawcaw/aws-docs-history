

# Configuring Amazon Inspector to integrate with Google Cloud Platform

Create a connector in Amazon Inspector to begin scanning your Google Cloud Platform (GCP) resources for vulnerabilities.

## To create a GCP connector
<a name="inspector-gcp-setup-inspector-create"></a>

1. Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home).

1. In the navigation pane, choose **Integrations**.

1. On the **GCP** card, choose **Add integration**.

1. Select **capabilities** to enable:
   + VM scanning (Amazon Inspector VM Scanner agent deployed to Compute Engine VM instances)
   + Cloud Run function scanning (code dependency analysis)
   + Artifact Registry image scanning (container image vulnerability detection)

   You can enable any combination. Capabilities can be changed later via `UpdateConnector`. To have Amazon Inspector install the Amazon Inspector VM Scanner agent, also select **Configure the Inspector VM Scanner automatically**.

1. Configure your **monitoring targets**:
   + **Organization ID** – Your numeric GCP organization ID. Amazon Inspector scans only projects in a GCP organization.
   + **GCP projects** – Choose whether to monitor all projects in your organization or specify individual project IDs, for all capabilities or per capability.
   + **GCP locations** – Choose whether to record all locations or select specific locations.

   GCP locations are matched exactly and independently, so select each location where your resources are: the zones of your Compute Engine VM instances, the regions of your Cloud Run functions, and the region or multi-region of each Artifact Registry repository. A multi-region, such as `us`, doesn't include the regions or zones in it. If you select VM scanning, include at least one zone.

1. Configure the **data connection**:

   Use the existing connection for your organization, or create a new one. To create one, enter your management project ID and the token issuer URL from **Account settings** in the IAM console. Copy the generated GCP setup script, run it in Google Cloud Shell (see [Configuring Google Cloud Platform to integrate with Amazon Inspector](inspector-gcp-setup-gcp.md)), enter the service account email and workload identity pool that the script prints, and then choose **Create data connection**. This creates the AWS Config connector for GCP in the current AWS Region. The AWS Config connector ARN is a required field in the API (`inspector2:CreateConnector`).

1. Provide the following information:
   + **Name** – A unique name for this connector. For name and description length constraints, see the CreateConnector operation in the Amazon Inspector API Reference.
   + **Description** (optional) – A description of this connector.
**Important**  
Names and descriptions are used to identify your content, and we recommend you do not include sensitive, confidential, or personally identifiable information (PII) in them.

1. If the console shows **IAM roles**, create the IAM roles described in [Managed Amazon Inspector VM Scanner deployment](#inspector-gcp-setup-inspector-managed), and then select **I confirm that I have created the required IAM roles in my account**.

1. Choose **Connect**.

## Managed Amazon Inspector VM Scanner deployment
<a name="inspector-gcp-setup-inspector-managed"></a>

If you enabled VM scanning with automatic install, Amazon Inspector uses Amazon EC2 Systems Manager Automation and VM Manager to deploy and manage the Amazon Inspector VM Scanner agent on your Compute Engine VM instances. With managed deployment:
+ No manual installation is required.
+ VM Manager installs the agent on each VM instance in scope and keeps it installed.
+ VM Manager can take up to 24 hours to apply the OS policy that installs the agent, so a VM instance can take up to 24 hours to get the agent.

To enable VM scanning, you must create the following IAM roles in your account. In each role name and policy, replace {{organization-id}} with your numeric GCP organization ID and {{account-id}} with your AWS account ID.

### Inspector2VmScannerRole-{{organization-id}}
<a name="inspector-gcp-setup-inspector-vm-scanner-role"></a>

Used by the Amazon Inspector VM Scanner agent running on Compute Engine VM instances to send scan telemetry to Amazon Inspector. This role trusts Google-signed ID tokens directly, so you don't need an IAM OIDC identity provider.

There is one trust policy for each way that the agent can get credentials. Use the one that you need:
+ `AllowListedServiceAccounts` trusts the service accounts that are attached to your VM instances. List the numeric unique ID of each service account in both `accounts.google.com:aud` and `accounts.google.com:sub`.
+ `AllowBridgeMinter` trusts the VM credential bridge that the setup script creates. With the bridge, new VM instances and service accounts need no change to the trust policy.

**Trust policy (service account allowlist):**

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowListedServiceAccounts",
            "Effect": "Allow",
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Principal": {
                "Federated": "accounts.google.com"
            },
            "Condition": {
                "StringEquals": {
                    "accounts.google.com:aud": [
                        "{{service-account-unique-id}}"
                    ],
                    "accounts.google.com:sub": [
                        "{{service-account-unique-id}}"
                    ],
                    "accounts.google.com:oaud": "api://AWSInspector"
                }
            }
        }
    ]
}
```

**Trust policy (VM credential bridge):**

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowBridgeMinter",
            "Effect": "Allow",
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Principal": {
                "Federated": "accounts.google.com"
            },
            "Condition": {
                "StringEquals": {
                    "accounts.google.com:oaud": "api://AWSInspector"
                },
                "StringLike": {
                    "accounts.google.com:email": "inspector-vmscan-{{account-id}}@*.iam.gserviceaccount.com"
                },
                "NumericEquals": {
                    "accounts.google.com:google/organization_number": "{{organization-id}}"
                }
            }
        }
    ]
}
```

**Permission policy (TelemetryPolicy):**

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "inspector2-telemetry:*",
            "Resource": "*"
        }
    ]
}
```

**Tags:**
+ `inspector-managed` = `true`

### Inspector2SSMFederationRole-{{organization-id}}
<a name="inspector-gcp-setup-inspector-ssm-federation-role"></a>

Enables OIDC federation to GCP for secure cross-cloud authentication. This role is assumed by the AssumeRole and DispatchRole, and by Amazon EC2 Systems Manager, to obtain web identity tokens for GCP operations.

**Trust policy:**

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "AWS": "arn:aws:iam::{{account-id}}:root"
            },
            "Condition": {
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::{{account-id}}:role/Inspector2SSMAssumeRole-{{organization-id}}",
                        "arn:aws:iam::{{account-id}}:role/Inspector2SSMDispatchRole-{{organization-id}}"
                    ]
                },
                "StringEquals": {
                    "aws:PrincipalTag/caller": "SSM"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": [
                    "ssm.amazonaws.com"
                ]
            }
        }
    ]
}
```

**Permission policy (FederationPolicy):**

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:GetWebIdentityToken",
                "sts:TagGetWebIdentityToken"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "sts:IdentityTokenAudience": [
                        "https://sts.googleapis.com"
                    ]
                }
            }
        }
    ]
}
```

**Tags:**
+ `caller` = `SSM`
+ `inspector-managed` = `true`

### Inspector2SSMAssumeRole-{{organization-id}}
<a name="inspector-gcp-setup-inspector-ssm-assume-role"></a>

Executes Amazon EC2 Systems Manager Automation to install the Amazon Inspector VM Scanner agent on Compute Engine VM instances. This role assumes the FederationRole, retrieves automation documents, starts and reads automation executions, and reports install results to Amazon EC2 Systems Manager.

**Trust policy:**

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": [
                    "ssm.amazonaws.com"
                ]
            },
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{account-id}}"
                }
            }
        }
    ]
}
```

**Permission policy (AssumeRolePolicy):**

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/Inspector2SSMFederationRole-{{organization-id}}"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/Inspector2SSMAssumeRole-{{organization-id}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "ssm.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/AmazonEC2RunCommandRoleForManagedInstances",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "ssm.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:CreateActivation",
                "ssm:DeleteActivation",
                "ssm:DescribeActivations",
                "ssm:DescribeInstanceInformation",
                "ssm:PutConfigurePackageResult",
                "iam:ListRoleTags"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ssm:AddTagsToResource",
            "Resource": [
                "arn:aws:ssm:*:{{account-id}}:activation/*",
                "arn:aws:ssm:*:{{account-id}}:managed-instance/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "ssm:GetDocument",
            "Resource": [
                "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnGcp",
                "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnGcp-VerifyInstallation",
                "arn:aws:ssm:*:*:document/AWS-InstallSSMAgentOnGCP",
                "arn:aws:ssm:*::document/AmazonInspector2-InspectorVmScanner"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "ssm:StartAutomationExecution",
            "Resource": [
                "arn:aws:ssm:*:*:document/AWS-InstallSSMAgentOnGCP-*",
                "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnGcp-*",
                "arn:aws:ssm:*:*:automation-definition/AWS-InstallDistributorPackageOnGcp-VerifyInstallation:*",
                "arn:aws:ssm:*:{{account-id}}:automation-execution/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetAutomationExecution",
                "ssm:DescribeAutomationExecutions",
                "ssm:DescribeAutomationStepExecutions"
            ],
            "Resource": "arn:aws:ssm:*:{{account-id}}:automation-execution/*"
        },
        {
            "Effect": "Allow",
            "Action": "ssm:GetCloudConnector",
            "Resource": "*"
        }
    ]
}
```

**Tags:**
+ `caller` = `SSM`
+ `inspector-managed` = `true`

### Inspector2SSMDispatchRole-{{organization-id}}
<a name="inspector-gcp-setup-inspector-ssm-dispatch-role"></a>

Dispatches Amazon Inspector VM Scanner agent installation via Amazon EC2 Systems Manager Automation. This role starts automation executions and passes the AssumeRole to Amazon EC2 Systems Manager.

**Trust policy:**

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": [
                    "ssm.amazonaws.com"
                ]
            },
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{account-id}}"
                }
            }
        }
    ]
}
```

**Permission policy (DispatchPolicy):**

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/Inspector2SSMAssumeRole-{{organization-id}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "ssm.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "ssm:StartAutomationExecution",
            "Resource": [
                "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnGcp",
                "arn:aws:ssm:*:{{account-id}}:automation-execution/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/Inspector2SSMFederationRole-{{organization-id}}"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeInstanceInformation",
                "ssm:ListCloudConnectors",
                "ssm:GetCloudConnector",
                "iam:ListRoleTags"
            ],
            "Resource": "*"
        }
    ]
}
```

**Tags:**
+ `caller` = `SSM`
+ `inspector-managed` = `true`

Each target Compute Engine VM instance must have an attached service account, and VM Manager must be enabled in its project. The setup script enables VM Manager.

Each target VM instance must also run a supported operating system. For more information, see [Supported operating systems](supported.md#supported-os).

For more information about the Amazon Inspector VM Scanner agent, see [Amazon Inspector VM Scanner](inspector-vm-scanner.md).

If you clear **Configure the Inspector VM Scanner automatically**, Amazon Inspector doesn't install the agent on your VM instances.

To exclude specific Compute Engine VM instances from scanning, apply the following label to the VM instance:
+ **Key:** `amazoninspectorvmexclusion`
+ **Value:** Any value

## Adjusting the scope of a connector
<a name="inspector-gcp-setup-inspector-scope"></a>

After you create a connector, you can adjust its scope by changing the GCP projects or GCP locations that it monitors. If you adjust the scope, most changes take effect within approximately 15 minutes.

Before you adjust the scope, note the following:
+ If you add projects for VM scanning, or the connector covers **All projects** and you create a project in your GCP organization or move one into it, run the setup script again. When you add projects to the scope, the console generates an updated setup script for them. In each new project, the script turns on VM Manager and grants the service agent roles that the OS policy rollout needs to install the Amazon Inspector VM Scanner. If you use the VM credential bridge, it also sets up the bridge for the project, including its minter service account. For more information, see [Running the setup script](inspector-gcp-setup-gcp.md#inspector-gcp-setup-gcp-running). Then make sure that the agent can get credentials in the new projects:
  + If the trust policy of `Inspector2VmScannerRole-{{organization-id}}` lists service accounts, add the unique IDs of the service accounts that the VM instances in the new projects use.
  + If you use the VM credential bridge, make sure that each new project has its minter service account, `inspector-vmscan-{{account-id}}`.
+ If you remove projects or zones from a connector with VM scanning, Amazon Inspector uninstalls the Amazon Inspector VM Scanner from the VM instances that are no longer in scope. Removing the scanner is best effort. In the removed projects and zones, GCP keeps the OS policy assignments that Systems Manager created. They are named `amazoninspector2-{{account-id}}-{{aws-region}}` and set to uninstall.
  + If you add a project or zone back from the same AWS account and AWS Region, Amazon Inspector reuses its assignments.
  + Before you turn on VM scanning for those VM instances from a different AWS account or AWS Region, delete the assignments. Otherwise, they can remove the scanner that the new connector installs.
  + After VM Manager shows the VM instances as compliant with the assignments, you can delete the assignments on the **OS policies** page in the Google Cloud console.
+ If you switch a connector with VM scanning between **All projects** and a list of projects, the OS policy orchestrator moves. With **All projects**, it is in your GCP organization. With a list of projects, it is in the management project. Systems Manager doesn't delete the orchestrator in the old location. It doesn't install the Amazon Inspector VM Scanner while that orchestrator exists. The automation fails with a message that tells you to delete the orchestrator in the other location.

  Delete the orchestrator `amazoninspector2-{{account-id}}-{{aws-region}}` in the old location. Its OS policy assignments can stay, because the orchestrator in the new location takes them over. Systems Manager then runs the installation again on its six-hour schedule.
+ If a service-linked connector exists (created via AWS Security Hub), you cannot reduce its scope in Amazon Inspector directly. Modify the scope in AWS Security Hub instead.
+ The scope of a AWS Security Hub connector can never be less than any existing customer-managed connector in Amazon Inspector for the same GCP organization.

## Verifying the connector
<a name="inspector-gcp-setup-inspector-verify"></a>

After you create the connector, Amazon Inspector begins discovering and scanning your GCP resources. It can take up to 24 hours for the initial set of findings to appear. To verify that the connector is working:

1. In the Amazon Inspector console, navigate to **Summary** to confirm GCP resource counts are populating.

1. Navigate to **Coverage** to verify GCP resources appear with scan status.

1. Navigate to **Integrations**, select your integration to Google Cloud Platform, and verify the connector health shows `CONNECTED`.

1. For VM scanning, verify that Compute Engine VM instances appear with Amazon Inspector VM Scanner agent status in the Coverage view.

1. Navigate to **Findings** and filter by resource type to view GCP resource findings.

**Note**  
Connector health status is eventually consistent. When a permission or configuration issue occurs, the connector status changes to `DEGRADED` or `FAILED_TO_CONNECT` quickly with an actionable message. However, after you fix the issue, the status can take up to 24 hours to return to `CONNECTED`.  
A `DEGRADED` or `FAILED_TO_CONNECT` status after a recent fix does not necessarily indicate an ongoing problem.

## Troubleshooting
<a name="inspector-gcp-setup-inspector-troubleshooting"></a>

If the connector status shows `FAILED_TO_CONNECT` or resources are not appearing after 24 hours, review the following:

Connector shows FAILED\_TO\_CONNECT status  
Verify that IAM outbound identity federation is turned on in your AWS account, that the token issuer URL that you gave the setup script matches your account's issuer, and that the AWS roles can impersonate the GCP service account.

Unable to record some GCP resources  
The error can occur for any of the following reasons:  
+ The GCP environment doesn't meet the prerequisites for resource recording.
+ A required API isn't enabled in the management project.
+ The service account's read roles aren't granted at the organization level.
+ Your organization exempts principals from the required Data Access audit logs.
To address the error, review [Prerequisites for integrating Amazon Inspector with Google Cloud Platform](inspector-gcp-prereqs.md), and then run the setup script again.

Resources not appearing  
Verify that the AWS Config connector is in the AWS Region that you gave the setup script.

Existing images or functions not appearing yet  
Images and functions that existed before you created the connector can take up to 24 hours to appear.

VMs not scanning  
Verify that the connector's locations include the zones of your VM instances, that each VM instance has an attached service account, that the trust policy of `Inspector2VmScannerRole-{{organization-id}}` allows the VM's service account or the VM credential bridge, and that VM instances have outbound network access and run a supported operating system.

VM scanner keeps reinstalling  
Another AWS account or AWS Region also scans the VM instance. Turn on VM scanning for a VM instance from only one AWS account and AWS Region.

VM scanner still installed after you remove scope  
Removing the scanner is best effort. Check the OS policy compliance of the VM instance in VM Manager.

Artifact Registry images not appearing  
Verify that the repository is a standard Docker-format repository and that the connector's locations include the repository's location. For a repository in a multi-region, such as `us`, `europe`, or `asia`, add the multi-region itself. Selecting a region or zone in that multi-region doesn't cover the repository.

Older images not scanned  
Amazon Inspector scans existing images that were pushed in the last 7 days. Push or pull an older image to scan it.

Image last pulled date not updating  
Amazon Inspector updates the last pulled date once a day.

Deleted images still appearing  
After you delete an image package or repository, its images can stay in coverage for up to 24 hours.

Functions not scanning  
Verify that the function is a Cloud Run function (1st gen or 2nd gen). Amazon Inspector doesn't scan Cloud Run services or jobs.

Function tags not appearing  
Amazon Inspector reads the tags of a function from the labels of the function itself. For a 2nd gen function, labels that you change on its Cloud Run service don't appear in Amazon Inspector. Update the labels on the function instead.

Scope change not taking effect  
When you change the connector scope to add projects for VM scanning, the console regenerates the setup script. You must re-run the updated script to prepare the new projects.

## How Amazon Inspector handles resource identifiers
<a name="inspector-gcp-setup-inspector-resource-ids"></a>

By enabling your GCP integration for Amazon Inspector, resource identifiers from other cloud providers will be stored in AWS Config, Amazon Inspector, and other AWS services (as needed) as metadata related to the management of the corresponding resource configuration data collected from the other cloud providers. Such resource identifiers do not constitute Your Content, and we recommend you do not include sensitive, confidential, or personally identifiable information in them.

The following identifiers from your connected cloud environment are stored and used by AWS to provide multicloud security capabilities:
+ **Resource identifiers:** Google Organization ID, Project ID, Location, Resource ID (IDs or Names, Resource Type)

Relationships among these identifiers - including how resources relate to one another and how findings relate to resources - are also stored as service metadata. AWS uses these identifiers for resource correlation, associating findings to resources, service operational logging, and de-duplication.