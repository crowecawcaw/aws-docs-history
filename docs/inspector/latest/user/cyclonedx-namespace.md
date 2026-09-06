

# Using CycloneDX namespaces with Amazon Inspector
<a name="cyclonedx-namespace"></a>

 Amazon Inspector provides you with CycloneDX namespaces and property names that you can use with SBOMs. This section describes all of the custom key/value properties that might be added to components in CycloneDX SBOMs. For more information, see [CycloneDX property taxonomy](https://github.com/CycloneDX/cyclonedx-property-taxonomy) on the GitHub website. 

## `amazon:inspector:sbom_scanner` namespace taxonomy
<a name="scan-namespaces"></a>

 The Amazon Inspector Scan API uses the `amazon:inspector:sbom_scanner` namespace and has the following properties: 


| **Property** | **Description** | 
| --- | --- | 
| amazon:inspector:sbom\_scanner:cisa\_kev\_date\_added | Indicates when the vulnerability was added to the CISA Known Exploited Vulnerabilities catalog. | 
| amazon:inspector:sbom\_scanner:cisa\_kev\_date\_due | Indicates when the vulnerability fix is due according to the CISA Known Exploited Vulnerabilities catalog. | 
| amazon:inspector:sbom\_scanner:critical\_vulnerabilities | Count of the total number of critical severity vulnerabilities found in the SBOM. | 
| amazon:inspector:sbom\_scanner:exploit\_available | Indicates if an exploit is available for the given vulnerability. | 
| amazon:inspector:sbom\_scanner:exploit\_last\_seen\_in\_public | Indicates when an exploit was last seen in public for the given vulnerability. | 
| amazon:inspector:sbom\_scanner:fixed\_version:{{component\_bom\_ref}} | Provides the fixed version of the indicated component for the given vulnerability. | 
| amazon:inspector:sbom\_scanner:high\_vulnerabilities | Count of the total number of high severity vulnerabilities found in the SBOM. | 
| amazon:inspector:sbom\_scanner:info | Provides scan context for a given component, for example: "Component scanned: no vulnerabilities found." | 
| amazon:inspector:sbom\_scanner:is\_malicious | Indicates if OpenSSF identifies affected components as malicious. | 
| amazon:inspector:sbom\_scanner:low\_vulnerabilities | Count of the total number of low severity vulnerabilities found in the SBOM. | 
| amazon:inspector:sbom\_scanner:medium\_vulnerabilities | Count of the total number of medium severity vulnerabilities found in the SBOM. | 
| amazon:inspector:sbom\_scanner:path | The path to the file that yields the subject package information. | 
| amazon:inspector:sbom\_scanner:priority |  The recommended priority for fixing a given vulnerability. The values in descending order are "IMMEDIATE", "URGENT", "MODERATE", and "STANDARD".  | 
| amazon:inspector:sbom\_scanner:priority\_intelligence |  The quality of intelligence used to determine the priority for a given vulnerability. The values include "VERIFIED" or "UNVERIFIED".  | 
| amazon:inspector:sbom\_scanner:warning | Provides context for a why a given component was not scanned, for example: "Component skipped: no purl provided." | 

## `amazon:inspector:sbom_generator` namespace taxonomy
<a name="sbomgen-namespaces"></a>

 The Amazon Inspector SBOM Generator uses the `amazon:inspector:sbom_generator` namespace and has the following properties: 


| **Property** | **Description** | 
| --- | --- | 
| amazon:inspector:sbom\_generator:cpu\_architecture | The CPU architecture of the system being inventoried (x86\_64). | 
| amazon:inspector:sbom\_generator:ec2:instance\_id | The Amazon EC2 instance ID. | 
| amazon:inspector:sbom\_generator:ec2:instance\_type | The Amazon EC2 Instance type | 
| amazon:inspector:sbom\_generator:live\_patching\_enabled | A boolean value indicating whether live patching is enabled on Amazon EC2 Amazon Linux. | 
| amazon:inspector:sbom\_generator:live\_patched\_cves | A list of CVEs patched through live patching on Amazon EC2 Amazon Linux. | 
| amazon:inspector:sbom\_generator:dockerfile\_finding:{{inspector\_finding\_id}} | Indicates that an Amazon Inspector finding in a component is related to Dockerfile checks. | 
| amazon:inspector:sbom\_generator:image\_id | The hash belonging to the container image config file (also known as the Image ID). | 
| amazon:inspector:sbom\_generator:image\_arch | The architecture of the container image. | 
| amazon:inspector:sbom\_generator:image\_author | The author of the container image. | 
| amazon:inspector:sbom\_generator:image:cmd:{{count}} | An absolute directory within the container image defined in default CMD configured at image build time. | 
| amazon:inspector:sbom\_generator:image:entrypoint:{{count}} | An absolute directory within the container image defined in default ENTRYPOINT configured at image build time. | 
| amazon:inspector:sbom\_generator:image:workdir | The WORKDIR directory of the container image configured at image build time. | 
| amazon:inspector:sbom\_generator:image\_docker\_version | The docker version used to build the container image. | 
| amazon:inspector:sbom\_generator:is\_duplicate\_package | Indicates that the subject package was found by more than one file scanner. | 
| amazon:inspector:sbom\_generator:duplicate\_purl | Indicates the duplicated package PURL found by another scanner. | 
| amazon:inspector:sbom\_generator:kernel\_name | The kernel name of the system being inventoried. | 
| amazon:inspector:sbom\_generator:kernel\_version | The kernel version of the system being inventoried. | 
| amazon:inspector:sbom\_generator:kernel\_component | A boolean value indicating whether a subject package is a kernel component | 
| amazon:inspector:sbom\_generator:running\_kernel | A boolean value that indicates if a subject package is the running kernel | 
| amazon:inspector:sbom\_generator:layer\_diff\_id | The hash of the uncompressed container image layer. | 
| amazon:inspector:sbom\_generator:replaced\_by | The value that replaces the current Go module. | 
| amazon:inspector:sbom\_generator:os\_hostname | The hostname of the system being inventoried. | 
| amazon:inspector:sbom\_generator:source\_file\_scanner | The scanner that found the file that contains package information, for example: /var/lib/dpkg/status. | 
| amazon:inspector:sbom\_generator:source\_package\_collector | The collector that extracted the package name and version from a specific file. | 
| amazon:inspector:sbom\_generator:source\_path | The path to the file that the subject package information was extracted from. | 
| amazon:inspector:sbom\_generator:file\_size\_bytes | Indicates file size of a given artifact. | 
| amazon:inspector:sbom\_generator:unresolved\_version | Indicates a version string that has not been resolved by package manager.. | 
| amazon:inspector:sbom\_generator:experimental:transitive\_dependency | Indicates indirect dependencies from a package manager. | 
| amazon:inspector:sbom\_generator:subscription:enabled | A boolean value indicating whether a subscription is enabled, such as RHEL EUS/E4S or Ubuntu Pro. | 
| amazon:inspector:sbom\_generator:subscription:name | The name of the active subscription (e.g., EUS, E4S, Pro). | 
| amazon:inspector:sbom\_generator:subscription:locked\_version | The version locked by the active RHEL subscription (RHEL EUS/E4S only). | 
| amazon:inspector:sbom\_generator:metadata:host:hostname | The hostname of the scanned system. | 
| amazon:inspector:sbom\_generator:metadata:host:kernel\_name | The kernel name of the operating system (e.g., Linux, Darwin, Windows\_NT). | 
| amazon:inspector:sbom\_generator:metadata:host:kernel\_version | The kernel version string of the operating system. | 
| amazon:inspector:sbom\_generator:metadata:host:cpu\_architecture | The CPU architecture of the system (e.g., x86\_64, arm64). | 
| amazon:inspector:sbom\_generator:metadata:host:bootdisk\_id | Unique identifier of the boot disk. | 
| amazon:inspector:sbom\_generator:metadata:host:boot\_id | Unique identifier for the current boot session. | 
| amazon:inspector:sbom\_generator:metadata:host:boot\_time | System boot time in ISO 8601 format. | 
| amazon:inspector:sbom\_generator:metadata:host:system\_id | Persistent system identifier (machine-id on Linux, MachineGuid on Windows). | 
| amazon:inspector:sbom\_generator:metadata:host:system\_serial | Hardware serial number from system firmware. | 
| amazon:inspector:sbom\_generator:metadata:host:network\_interfaces:{{name}}:hardware | MAC address of the network interface. | 
| amazon:inspector:sbom\_generator:metadata:host:network\_interfaces:{{name}}:ipv4 | IPv4 address(es) assigned to the interface. | 
| amazon:inspector:sbom\_generator:metadata:host:network\_interfaces:{{name}}:ipv6 | IPv6 address(es) assigned to the interface. | 
| amazon:inspector:sbom\_generator:metadata:host:sbomgen\_tag:{{key}} | Custom user-defined tags passed via the --tag CLI argument. | 
| amazon:inspector:sbom\_generator:metadata:imds:provider | The cloud provider detected via IMDS (aws, azure, gcp). | 
| amazon:inspector:sbom\_generator:metadata:imds:instance\_id | The Amazon EC2 instance ID or Azure VM name. | 
| amazon:inspector:sbom\_generator:metadata:imds:instance\_type | The instance type (e.g., t3.micro, Standard\_D2s\_v3). | 
| amazon:inspector:sbom\_generator:metadata:imds:instance\_location | The region/location of the instance. | 
| amazon:inspector:sbom\_generator:metadata:imds:instance\_partition | The cloud partition (aws, aws-cn, aws-us-gov for AWS, or AzurePublicCloud for Azure). | 
| amazon:inspector:sbom\_generator:metadata:imds:account\_id | The AWS account ID of the Amazon EC2 instance, obtained from the instance identity document (AWS only). | 
| amazon:inspector:sbom\_generator:metadata:imds:resource\_type | The type of cloud resource being scanned (e.g., aws\_ec2\_instance). | 
| amazon:inspector:sbom\_generator:metadata:imds:instance\_managed\_id | Amazon EC2 Systems Manager managed instance ID (AWS only). | 
| amazon:inspector:sbom\_generator:metadata:imds:tenant\_id | The Microsoft Entra ID tenant the instance's subscription belongs to (Azure only, populated when a managed identity is assigned to the VM). | 
| amazon:inspector:sbom\_generator:metadata:imds:resource\_group | The Azure resource group the instance belongs to (Azure only). | 
| amazon:inspector:sbom\_generator:metadata:imds:subscription\_id | The Azure subscription ID associated with the instance (Azure only). | 
| amazon:inspector:sbom\_generator:metadata:imds:vm\_id | Azure VM unique identifier (Azure only). | 
| amazon:inspector:sbom\_generator:metadata:imds:project\_id | The Google Cloud project ID the instance belongs to (GCP only). | 
| amazon:inspector:sbom\_generator:metadata:imds:numeric\_project\_id | The numeric Google Cloud project ID the instance belongs to (GCP only). | 
| amazon:inspector:sbom\_generator:metadata:imds:instance\_name | The instance name as reported by the GCP metadata service (GCP only). | 
| amazon:inspector:sbom\_generator:metadata:host:open\_port:{{port}}:{{protocol}} | Indicates an open port of a runtime resource (i.e. EC2) | 
| amazon:inspector:sbom\_generator:hardened\_image:vendor | The vendor of a hardened container image | 