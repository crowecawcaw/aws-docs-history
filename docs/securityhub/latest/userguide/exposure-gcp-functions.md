

# Remediating exposures for GCP Cloud Run functions

AWS Security Hub can generate exposure findings for GCP Cloud Run functions.

On the Security Hub console, the GCP Cloud Run function involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the `GetFindingsV2` operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Google Cloud resources. 

**Contents**
+ [Misconfiguration traits for GCP Cloud Run functions](#gcp-functions-misconfiguration)
  + [The Cloud Run function is deployed outside a VPC](#deployed-outside-private-network)
+ [Reachability traits for GCP Cloud Run functions](#gcp-functions-reachability)
  + [The Cloud Run function can be invoked by anyone](#publicly-invocable)
+ [Vulnerability traits for GCP Cloud Run functions](#gcp-functions-vulnerability)
  + [The Cloud Run function has network-exploitable software vulnerabilities with a high likelihood of exploitation](#high-priority-vulnerability)
  + [The Cloud Run function has software vulnerabilities](#low-priority-vulnerability)
  + [The Cloud Run function has malicious software packages](#malicious-package)
  + [The Cloud Run function has a vulnerability in the code](#code-vulnerability)

## Misconfiguration traits for GCP Cloud Run functions
<a name="gcp-functions-misconfiguration"></a>

Here are misconfiguration traits for GCP Cloud Run functions and suggested remediation steps.

### The Cloud Run function is deployed outside a VPC
<a name="deployed-outside-private-network"></a><a name="deployed-outside-vpc"></a>

 The function isn't connected to a Virtual Private Cloud (VPC) network through Direct VPC egress or a Serverless VPC Access connector. Without either one, the function can reach other resources only through their public endpoints, not over internal IP addresses. Following standard security principles, connect your Cloud Run functions to a VPC network. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Configure Direct VPC egress on the function**  
 Configure Direct VPC egress in the function's configuration, not only on its backing Cloud Run service. The subnet must have an IPv4 range of /26 or larger. Cloud Run functions (1st gen) don't support Direct VPC egress, so use a connector instead. For more information, see [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) and [gcloud functions deploy](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) on the Google Cloud website. 

**Use a Serverless VPC Access connector**  
 Create a Serverless VPC Access connector in the function's region, and configure the function to use it. For more information, see [Serverless VPC Access connectors](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors) and, for 1st gen functions, [Connect to a VPC network](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc) on the Google Cloud website. 

## Reachability traits for GCP Cloud Run functions
<a name="gcp-functions-reachability"></a>

Here are reachability traits for GCP Cloud Run functions and suggested remediation steps.

### The Cloud Run function can be invoked by anyone
<a name="publicly-invocable"></a>

 The function's Identity and Access Management (IAM) policy, or the IAM policy of its backing Cloud Run service, grants a role to `allUsers` or `allAuthenticatedUsers`, or the service's invoker IAM check is off. Anyone who can reach the function through its ingress settings can then invoke it, and its code runs with the permissions of the function's service account. Following standard security principles, grant the invoker role only to the principals that need to invoke the function. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Remove public principals**  
 Remove `allUsers` and `allAuthenticatedUsers` from the IAM policies of the function and its backing Cloud Run service, and grant the invoker role only to the callers that need it. Callers that don't authenticate, such as webhook senders, stop working. The invoker IAM check must also be on. For more information, see [Authorize access with IAM](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam) and [Authorize access with IAM (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam) on the Google Cloud website. 

**Turn the Cloud Run invoker IAM check back on**  
 If the invoker IAM check is off on the function's backing Cloud Run service, turn it back on so that callers must authenticate. To address this exposure, you must also remove the public principals. For more information, see [Access control with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access) on the Google Cloud website. 

## Vulnerability traits for GCP Cloud Run functions
<a name="gcp-functions-vulnerability"></a>

Here are vulnerability traits for GCP Cloud Run functions and suggested remediation steps.

### The Cloud Run function has network-exploitable software vulnerabilities with a high likelihood of exploitation
<a name="high-priority-vulnerability"></a>

 Common Vulnerabilities and Exposures (CVEs) can affect the dependencies that your function uses. A high-priority vulnerability is network-exploitable with a high likelihood of exploitation. Such a vulnerability is an immediate security threat because public exploit code might already exist and attackers might be using it. Patch these vulnerabilities promptly to protect your function. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Update affected dependencies**  
 Review the affected CVEs in the finding, update the vulnerable dependencies to fixed versions, and then redeploy the function. We recommend pinning dependency versions with a lock file so that a rebuild doesn't pull different versions. For more information, see [Deploy Cloud Run functions](https://docs.cloud.google.com/run/docs/deploy-functions) on the Google Cloud website. 

**Future considerations**  
 To prevent future occurrences, scan your function's dependencies for vulnerabilities in your build pipeline, before you deploy. 

### The Cloud Run function has software vulnerabilities
<a name="low-priority-vulnerability"></a>

 Common Vulnerabilities and Exposures (CVEs) can affect the dependencies that your function uses. Noncritical vulnerabilities are security weaknesses with lower severity or exploitability than high-priority vulnerabilities. They pose less immediate risk, but attackers can still exploit them to compromise the confidentiality, integrity, or availability of data, or to access other systems. Following security best practices, patch these vulnerabilities to protect your function. 

**Remediation: Update affected dependencies**  
 Review the affected CVEs in the finding, update the vulnerable dependencies to fixed versions, and then redeploy the function. We recommend pinning dependency versions with a lock file so that a rebuild doesn't pull different versions. For more information, see [Deploy Cloud Run functions](https://docs.cloud.google.com/run/docs/deploy-functions) on the Google Cloud website. 

### The Cloud Run function has malicious software packages
<a name="malicious-package"></a>

 The function's dependencies include one or more known malicious open-source packages. Malicious packages contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data. Code from these packages can run with the permissions of the function's service account. Following security best practices, remove malicious packages to protect your function from potential attacks. 

**Remediation: Investigate and remove malicious packages**  
 Remove the malicious packages from the function's dependencies, and then redeploy the function from a clean build. Treat the function's service account as compromised. Delete any keys that the service account has, rotate secrets that the function can access, and review the service account's activity. For more information, see [Deploy Cloud Run functions](https://docs.cloud.google.com/run/docs/deploy-functions) on the Google Cloud website. 

### The Cloud Run function has a vulnerability in the code
<a name="code-vulnerability"></a>

 Amazon Inspector code scanning found a security vulnerability in the function's code. Attackers can exploit code vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems. Following security best practices, fix code vulnerabilities to protect your function. 

**Remediation: Fix the vulnerable code**  
 Fix the code at the location that the finding reports, and then redeploy the function. If the finding reports a hardcoded secret, rotate the secret, and store the new value in Secret Manager instead of in your code. For more information, see [Configure secrets for services](https://docs.cloud.google.com/run/docs/configuring/services/secrets) and [Deploy Cloud Run functions](https://docs.cloud.google.com/run/docs/deploy-functions) on the Google Cloud website. 