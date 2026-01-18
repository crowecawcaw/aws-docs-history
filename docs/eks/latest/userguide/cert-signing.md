**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Secure workloads with Kubernetes certificates

The Kubernetes Certificates API automates [X.509](https://www.itu.int/rec/T-REC-X.509 "https://www.itu.int/rec/T-REC-X.509") credential provisioning. The API features a command line interface for Kubernetes API clients to request and obtain [X.509 certificates](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/ "https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/") from a Certificate Authority (CA). You can use the `CertificateSigningRequest` (CSR) resource to request that a denoted signer sign the certificate. Your requests are either approved or denied before they’re signed. Kubernetes supports both built-in signers and custom signers with well-defined behaviors. This way, clients can predict what happens to their CSRs. To learn more about certificate signing, see [signing requests](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/ "https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/").

One of the built-in signers is `kubernetes.io/legacy-unknown`. The `v1beta1` API of CSR resource honored this legacy-unknown signer. However, the stable `v1` API of CSR doesn’t allow the `signerName` to be set to `kubernetes.io/legacy-unknown`.

If you want to use Amazon EKS CA for generating certificates on your clusters, you must use a custom signer. To use the CSR `v1` API version and generate a new certificate, you must migrate any existing manifests and API clients. Existing certificates that were created with the existing `v1beta1` API are valid and function until the certificate expires. This includes the following:

- Trust distribution: None. There’s no standard trust or distribution for this signer in a Kubernetes cluster.
- Permitted subjects: Any
- Permitted x509 extensions: Honors subjectAltName and key usage extensions and discards other extensions
- Permitted key usages: Must not include usages beyond ["key encipherment", "digital signature", "server auth"]

###### Note

Client certificate signing is not supported.

- Expiration/certificate lifetime: 1 year (default and maximum)
- CA bit allowed/disallowed: Not allowed

## Example CSR generation with signerName

These steps shows how to generate a serving certificate for DNS name `myserver.default.svc` using `signerName: beta.eks.amazonaws.com/app-serving`. Use this as a guide for your own environment.

1. Run the `openssl genrsa -out myserver.key 2048` command to generate an RSA private key.

```
 openssl genrsa -out myserver.key 2048
```

2. Run the following command to generate a certificate request.

```
 openssl req -new -key myserver.key -out myserver.csr -subj "/CN=myserver.default.svc"
```

3. Generate a `base64` value for the CSR request and store it in a variable for use in a later step.

```
 base_64=$(cat myserver.csr | base64 -w 0 | tr -d "
")
```

4. Run the following command to create a file named `mycsr.yaml`. In the following example, `beta.eks.amazonaws.com/app-serving` is the `signerName`.

```
 cat >mycsr.yaml <<EOF
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: myserver
spec:
  request: $base_64
  signerName: beta.eks.amazonaws.com/app-serving
  usages:
    - digital signature
    - key encipherment
    - server auth
EOF
```

5. Submit the CSR.

```
 kubectl apply -f mycsr.yaml
```

6. Approve the serving certificate.

```
 kubectl certificate approve myserver
```

7. Verify that the certificate was issued.

```
 kubectl get csr myserver
```

An example output is as follows.

```
 NAME       AGE     SIGNERNAME                           REQUESTOR          CONDITION
myserver   3m20s   beta.eks.amazonaws.com/app-serving   kubernetes-admin   Approved,Issued
```

8. Export the issued certificate.

```
 kubectl get csr myserver -o jsonpath='{.status.certificate}'| base64 -d > myserver.crt
```
