

# Prerequisites for integrating Amazon Inspector with Google Cloud Platform

Before you create a connector, verify that your AWS account and Google Cloud Platform (GCP) environment meet the following requirements. The GCP setup script handles most GCP configuration for you: workload identity federation, the service account and its roles, audit logs, log sinks, the Cloud Asset Inventory feed, and Pub/Sub topics and subscriptions.

## AWS account setup – all capabilities
<a name="inspector-gcp-prereqs-aws"></a>

IAM outbound identity federation  
Your AWS account must have IAM outbound identity federation turned on. Note the token issuer URL. You give it to the GCP setup script, and Amazon Inspector uses it to get short-lived tokens for GCP.  
If you already turned on outbound identity federation for another AWS security service (such as AWS Security Hub or AWS Security Hub CSPM), you don't need to do it again. For more information, see [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.  
On the GCP side, the setup script creates the workload identity pool and provider that trust your AWS token issuer. You don't need to configure them yourself.

Service-linked role  
Amazon Inspector creates its service-linked role, `AWSServiceRoleForAmazonInspector2ThirdParty`, when you create the connector. You don't need to create it yourself.

AWS Config connector  
An AWS Config connector for GCP. The API requires its ARN when you create a connector. In the console, you can choose an existing AWS Config connector or create one when you create the Amazon Inspector connector. Create the AWS Config connector in the AWS Region that you gave the setup script.

Console IAM permissions  
The IAM principal (user or role) that creates the connector requires the following permissions:  

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "config:GetConnector",
        "config:ListConnectors",
        "config:PutConnector",
        "inspector2:CreateConnector",
        "inspector2:DeleteConnector",
        "inspector2:ListConnectors",
        "inspector2:ListTagsForResource",
        "inspector2:TagResource",
        "inspector2:UntagResource",
        "inspector2:UpdateConnector"
      ],
      "Resource": "*"
    }
  ]
}
```

## AWS account setup – VM scanning only
<a name="inspector-gcp-prereqs-aws-vm"></a>

In addition to the requirements above, VM scanning requires:
+ Amazon EC2 Systems Manager in the same AWS Region as the connector.
+ The following four IAM roles. Replace {{organization-id}} with your numeric GCP organization ID. The names must match exactly. For the trust and permission policies of each role, see [Configuring Amazon Inspector to integrate with Google Cloud Platform](inspector-gcp-setup-inspector.md).
  + `Inspector2VmScannerRole-{{organization-id}}`
  + `Inspector2SSMFederationRole-{{organization-id}}`
  + `Inspector2SSMDispatchRole-{{organization-id}}`
  + `Inspector2SSMAssumeRole-{{organization-id}}`

## GCP setup
<a name="inspector-gcp-prereqs-gcp"></a>

Before you run the GCP setup script, make sure that you have the following:

GCP organization and management project  
A GCP organization, and a management project in it with billing enabled and the IAM API (`iam.googleapis.com`) turned on. The setup script turns on the other APIs that it needs. The management project can sit directly under the organization or in a folder. The setup script creates the workload identity pool and provider, the service account, and the Pub/Sub topics and subscriptions in this project.  
Amazon Inspector doesn't support projects that don't belong to an organization.

Google Cloud Terms of Service  
You must accept the Google Cloud Terms of Service. Otherwise, enabling APIs fails with the error `UREQ_TOS_NOT_ACCEPTED`.

Command-line tools  
The gcloud CLI with the `beta` component installed, and signed in with `gcloud auth login`. The script is tested with version 580.0.0. With an older version, the script prints a warning and continues. The script also needs `jq` and a `timeout` command that supports `--foreground` (GNU coreutils, or `gtimeout` on macOS). Google Cloud Shell has both.

GCP roles  
The person who runs the setup script needs the following roles:  
+ On the organization: permission to get and set its IAM policy (for example, Organization Administrator), Cloud Asset Owner (`roles/cloudasset.owner`), Logs Configuration Writer (`roles/logging.configWriter`), and Organization Role Administrator (`roles/iam.organizationRoleAdmin`), to create the custom roles.
+ On the management project: Owner, or the narrower roles listed in [Configuring Google Cloud Platform to integrate with Amazon Inspector](inspector-gcp-setup-gcp.md).

Data Access audit logs  
The setup script turns on Data Access audit logs. Don't exempt any principal from them.  
The script stops if your organization has exemptions. The script can't see exemptions on folders or projects, so check those yourself.

Organization policies  
The following controls can block setup:  
+ An organization policy that limits the allowed workload identity pool providers. The allowed issuers must include your AWS token issuer URL. For VM scanning with the VM credential bridge, they must also include `https://accounts.google.com`.
+ An organization policy that turns off service account creation. With the VM credential bridge, the script creates a service account in each VM project, so the policy must allow service account creation there too.
+ Domain restricted sharing.
+ VPC Service Controls.

**Note**  
The person who sets up GCP doesn't need to be the person who creates the connector in the Amazon Inspector console.

## GCP setup – VM scanning only
<a name="inspector-gcp-prereqs-gcp-vm"></a>

In addition to the requirements above, VM scanning requires:
+ VM Manager in each project that has VM instances to scan. The setup script turns it on. GCP charges for VM Manager for each VM instance that runs an active OS Config agent in those projects, not only the VM instances that Amazon Inspector scans. For more information, see VM Manager pricing on the Google Cloud website.
+ With the VM credential bridge (the default), the IAM API (`iam.googleapis.com`) and the IAM Service Account Credentials API (`iamcredentials.googleapis.com`) in each of those projects. The setup script turns them on.
+ Billing enabled on each of those projects.
+ Permissions for the person who runs the setup script. On the organization and in each VM project, they need permission to create the OS Config and Progressive Rollout service identities. In each VM project, they also need Service Usage Admin, Project IAM Admin, and the `resourcemanager.projects.get`, `compute.projects.get`, `compute.projects.setCommonInstanceMetadata`, `compute.globalOperations.get`, and `osconfig.projectFeatureSettings.update` permissions. With the VM credential bridge, they also need Service Account Admin (`roles/iam.serviceAccountAdmin`) and a role with the `iam.serviceAccountKeys.list` permission (for example, Service Account Viewer, `roles/iam.serviceAccountViewer`) in each VM project, or on the organization when `GCP_TARGET_PROJECTS` is `ALL_PROJECTS_IN_ORG`.
+ The OS Config agent running on each VM instance. Most Google-provided images include it.
+ An attached service account on each VM instance. The scanner gets the VM's identity token through this service account. With the VM credential bridge, the VM scanner role doesn't need to trust this service account. If the bridge isn't set up or fails, the scanner falls back to the service account allowlist, and the VM scanner role must trust the attached service account. For more information, see [Configuring Amazon Inspector to integrate with Google Cloud Platform](inspector-gcp-setup-inspector.md).

**Important**  
Turn on VM scanning for a VM instance from only one AWS account and AWS Region. If two connectors in different AWS accounts or Regions cover the same VM instance, they continually reinstall the scanner over each other, and findings for that instance can move between the two accounts.

Each AWS account and Region that turns on VM scanning uses one OS policy orchestrator in your GCP organization or project, and one OS policy assignment in each project and zone in scope. These count against your Google Cloud OS Config quotas, including the orchestrators and assignments of a deleted connector. Before you turn on VM scanning from several AWS accounts or Regions, check your current usage and quotas in the Google Cloud console.