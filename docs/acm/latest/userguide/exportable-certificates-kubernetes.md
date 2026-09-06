

# Secure Kubernetes Workloads with ACM Certificates
<a name="exportable-certificates-kubernetes"></a>

You can use AWS Certificate Manager exportable public certificates with AWS Controllers for Kubernetes (ACK) to issue and export public TLS certificates from ACM to your Kubernetes workloads. This integration enables you to secure Amazon Elastic Kubernetes Service (Amazon EKS) pods and terminate TLS at your Kubernetes Ingress. To get started, see the [ACM Controller for Kubernetes](https://github.com/aws-controllers-k8s/acm-controller) on GitHub.

**Tip**  
If you use [cert-manager](https://cert-manager.io/) or another industry-standard ACME client in your Kubernetes cluster, you can automate certificate issuance from ACM through the ACME protocol instead. In this approach, the ACME client generates and holds the private key. For more information, see [ACME certificate automation](acm-acme.md).

AWS Controllers for Kubernetes (ACK) extends the Kubernetes API to manage AWS resources using native Kubernetes manifests. The ACK service controller for ACM provides automated certificate lifecycle management within your Kubernetes workflow. When you create an ACM Certificate resource in Kubernetes, the ACK controller performs the following actions:

1. Requests a certificate from ACM, which generates the certificate signing request (CSR).

1. Waits for domain validation to complete and for ACM to issue the certificate.

1. If the `exportTo` field is specified, exports the issued certificate and private key and stores them in your specified Kubernetes Secret.

1. If the `exportTo` field is specified and the certificate is eligible for renewal, updates the Kubernetes Secret with renewed certificates before expiration.

Publicly issued certificates require [domain validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) before ACM can issue them. You can use the [ACK service controller for Amazon Route 53](https://github.com/aws-controllers-k8s/route53-controller) to automatically create the required DNS validation CNAME records in your hosted zone.

## Certificate usage options
<a name="kubernetes-ack-certificate-usage"></a>

You can use ACM certificates with Kubernetes in a few ways:

![ELB connects to Ingress, which routes to Service distributing traffic across Pod1, Pod2, and Pod3.](http://docs.aws.amazon.com/acm/latest/userguide/images/kubernetes-acm.png)


1. *Load balancer termination (without export)*: Issue certificates through ACK and use them to terminate TLS at an AWS load balancer. The certificate remains in ACM and is automatically discovered by the [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.1/guide/ingress/cert_discovery/). This approach does not require exporting the certificate.

1. *Ingress termination (with export)*: Export certificates from ACM and store them in Kubernetes Secrets for TLS termination at the Ingress level. This enables you to use certificates directly within your Kubernetes workloads.

**Note**  
For use cases that require private certificates, see [AWS Private CA Connector for Kubernetes](https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes-concepts.html), a cert-manager plugin.

## Prerequisites
<a name="kubernetes-ack-prerequisites"></a>

Before you install the ACK service controller for ACM, ensure you have the following:
+ A Kubernetes cluster.
+ Helm installed.
+ `kubectl` configured to communicate with your cluster.
+ `eksctl` installed for configuring pod identity associations on EKS.

## Install the ACK service controller for ACM
<a name="kubernetes-ack-installation"></a>

Use Helm to install the ACK service controller for ACM in your Amazon EKS cluster.

1. Create a namespace for the ACK controller.

   ```
   $ kubectl create namespace ack-system --dry-run=client -o yaml | kubectl apply -f -
   ```

1. Create a pod identity association for the ACK controller. Replace {{CLUSTER\_NAME}} with your cluster name and {{REGION}} with your AWS Region.

   ```
   $ eksctl create podidentityassociation --cluster {{CLUSTER_NAME}} --region {{REGION}} \
       --namespace ack-system \
       --create-service-account \
       --service-account-name ack-acm-controller \
       --permission-policy-arns arn:aws:iam::aws:policy/AWSCertificateManagerFullAccess
   ```

1. Log in to the Amazon ECR Public registry.

   ```
   $ aws ecr-public get-login-password --region us-east-1 | helm registry login --username AWS --password-stdin public.ecr.aws
   ```

1. Install the ACK service controller for ACM. Replace {{REGION}} with your AWS Region.

   ```
   $ helm install -n ack-system ack-acm-controller oci://public.ecr.aws/aws-controllers-k8s/acm-chart --set serviceAccount.create=false --set serviceAccount.name=ack-acm-controller --set aws.region={{REGION}}
   ```

1. Verify the controller is running.

   ```
   $ kubectl get pods -n ack-system
   ```

For more information about pod identity associations, see [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) in the *Amazon EKS User Guide*.

## Example: Terminate TLS at the Ingress
<a name="kubernetes-ack-example"></a>

The following example demonstrates how to export an ACM certificate and use it to terminate TLS at the Kubernetes Ingress level. This configuration creates an ACM certificate, exports it to a Kubernetes Secret, and configures an Ingress resource to use the certificate for TLS termination.

In this example:
+ Secret is created to store the exported certificate (`exported-cert-secret`)
+ The ACK Certificate resource requests a certificate from ACM for your domain and exports it to the `exported-cert-secret` Secret.
+ The Ingress resource references the `exported-cert-secret` to terminate TLS for incoming traffic.

Replace `${HOSTNAME}` with your domain name.

```
apiVersion: v1
kind: Secret
type: kubernetes.io/tls
metadata:
  name: exported-cert-secret
  namespace: demo-app
data:
  tls.crt: ""
  tls.key: ""
---
apiVersion: acm.services.k8s.aws/v1alpha1
kind: Certificate
metadata:
  name: exportable-public-cert
  namespace: demo-app
spec:
  domainName: ${HOSTNAME}
  options:
    certificateTransparencyLoggingPreference: ENABLED
  exportTo: 
    namespace: demo-app
    name: exported-cert-secret
    key: tls.crt
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-traefik
  namespace: demo-app
spec:
  tls:
  - hosts:
    - ${HOSTNAME}
    secretName: exported-cert-secret
  ingressClassName: traefik
  rules:
  - host: ${HOSTNAME}
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: whoami
            port:
              number: 80
```

Once deployed, the ACK service controller for ACM automatically manages the certificate lifecycle, including renewals. When ACM renews the certificate, the controller updates the `exported-cert-secret` Secret with the new certificate, ensuring your Ingress continues to use valid certificates without manual intervention.