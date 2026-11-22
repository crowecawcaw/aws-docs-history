

# Remediating exposures for GCP Cloud Run services

AWS Security Hub can generate exposure findings for GCP Cloud Run services.

On the Security Hub console, the GCP Cloud Run service involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the `GetFindingsV2` operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Google Cloud resources. 

**Contents**
+ [Misconfiguration traits for GCP Cloud Run services](#gcp-run-misconfiguration)
  + [The Cloud Run service has cleartext credentials in environment variables](#cleartext-credentials-present)
+ [Reachability traits for GCP Cloud Run services](#gcp-run-reachability)
  + [The Cloud Run service may be reachable from the public internet](#potentially-internet-reachable)
  + [The Cloud Run service can be invoked by anyone](#publicly-invocable)

## Misconfiguration traits for GCP Cloud Run services
<a name="gcp-run-misconfiguration"></a>

Here are misconfiguration traits for GCP Cloud Run services and suggested remediation steps.

### The Cloud Run service has cleartext credentials in environment variables
<a name="cleartext-credentials-present"></a>

 A container environment variable whose name suggests a secret, such as a password, token, or key, has a literal value instead of a reference to a secret in Secret Manager. Anyone who can view the service's configuration can see the value, and the service's revision history keeps it. Following standard security principles, store credentials as secrets and reference them instead of setting literal values. 

**Remediation: Move credentials to Secret Manager**  
 Store each credential as a secret in Secret Manager, grant the service's runtime service account access to it, and update the service to reference the secret. Earlier revisions keep the literal values, so rotate the credentials in the systems that issued them. For more information, see [Configure secrets for services](https://docs.cloud.google.com/run/docs/configuring/services/secrets) on the Google Cloud website. 

## Reachability traits for GCP Cloud Run services
<a name="gcp-run-reachability"></a>

Here are reachability traits for GCP Cloud Run services and suggested remediation steps.

### The Cloud Run service may be reachable from the public internet
<a name="potentially-internet-reachable"></a>

 The service's ingress setting is All (`INGRESS_TRAFFIC_ALL`), which allows requests directly from the internet to the service's `run.app` URL. These requests bypass any load balancer in front of the service, including its Google Cloud Armor or Identity-Aware Proxy (IAP) protection. Following standard security principles, allow only the network ingress that your Cloud Run services need. 

**Remediation: Restrict network ingress**  
 Set the service's ingress to Internal, or to Internal and Cloud Load Balancers if an external Application Load Balancer is in front of the service. Without a load balancer, clients on the internet can no longer reach the service. For more information, see [Restrict network ingress](https://docs.cloud.google.com/run/docs/securing/ingress) on the Google Cloud website. 

### The Cloud Run service can be invoked by anyone
<a name="publicly-invocable"></a>

 The service's Identity and Access Management (IAM) policy grants a role, usually Cloud Run Invoker (`roles/run.invoker`), to `allUsers` or `allAuthenticatedUsers`, or the service's invoker IAM check is off. Anyone who can reach the service through its ingress settings can then invoke it, and its code runs with the permissions of its runtime service account. Following standard security principles, grant the Cloud Run Invoker role only to the principals that need to invoke the service. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Remove public principals**  
 Grant the Cloud Run Invoker role to the service accounts or users that call the service, and then remove `allUsers` and `allAuthenticatedUsers` from the service's IAM policy. Callers that don't authenticate stop working, so require internet users to sign in through IAP instead. The invoker IAM check must also be on. For more information, see [Access control with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access) on the Google Cloud website. 

**Turn the invoker IAM check back on**  
 If the service's invoker IAM check is off, turn it back on so that callers must authenticate. To address this exposure, you must also remove the public principals. For more information, see [Access control with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access) on the Google Cloud website. 