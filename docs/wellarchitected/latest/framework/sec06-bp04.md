

# SEC06-BP04 Validate software integrity

 Software artifacts can be altered between when a vendor publishes them and when your workload runs them. Use cryptographic signatures to confirm an artifact was not altered and came from its claimed source. Sign your own code and images so your compute environments run only what you approved. 

 **Desired outcome:** 
+  You obtain all artifacts from trusted sources and validate vendor website certificates before downloading. 
+  You cryptographically verify downloaded artifacts against the publisher's signature, not only a hash. 
+  You cryptographically sign your own software, code, and libraries. 
+  Your compute environments verify those signatures before running your code. 

 **Common anti-patterns:** 
+  Teams trust a reputable vendor site but ignore certificate expiration warnings and download anyway. 
+  Teams validate a site certificate but never verify the signature of the artifact they downloaded. 
+  Integrity checks rely on a hash alone, which proves the file is unchanged but says nothing about its source. 
+  Internally built software, code, and libraries go unsigned, even when used only in the team's own deployments. 

 **Benefits of establishing this best practice:** 
+  Verifying artifact integrity helps keep malware out of your compute environments. 
+  Signing your own software guards against unauthorized code running in those environments. 
+  Signature verification establishes provenance, which a hash cannot. 
+  A signed, verified supply chain gives auditors and responders a clear chain of trust. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Many operating system images, container images, and code artifacts ship with a digest or hash. You compute the hash of what you downloaded and compare it to the published value. This confirms the bytes did not change in transit but does not identify who produced the changed bytes. If an unauthorized party replaces both the artifact and its published hash, the check still passes. *Provenance*, or proof that an artifact came from a specific source, requires a signature made with a private key that only the trusted publisher holds. 

 A certificate issued by a recognized authority binds the signing key to an identity. Validate the certificate, including its expiration, as part of the check. When you obtain software from a vendor, look for a published public key and verification instructions. Many publishers, including AWS, provide both for the agents and tools they distribute. 

 The code and images your teams build are also artifacts. Anyone with unauthorized access can take advantage of unsigned internal software. When you sign your own artifacts, your compute environments can refuse anything unsigned or altered. Manage the code-signing lifecycle: generate and protect signing keys, sign during the build, and verify at deployment and at run time. Automate these steps in your CI/CD pipeline to keep the practice consistent. As cryptographic standards evolve, verify that your signing and verification tooling is up to date so you can adopt stronger algorithms without disrupting your release process. 

 In the AWS Cloud, use [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) to manage the code-signing lifecycle and verify signatures. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) and [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html) integrate with Signer to verify signatures before code or images run. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Verify downloaded artifacts before use:** For each vendor artifact, validate the site certificate, obtain the publisher's public key, and verify the signature, not just a hash, before the artifact enters your build or runtime. Follow the publisher's documented verification steps, such as those for the [AWSTOE installer](https://docs.aws.amazon.com/imagebuilder/latest/userguide/awstoe-verify-sig.html), the [SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/verify-agent-signature.html), and the [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/verify-CloudWatch-Agent-Package-Signature.html). 

1.  **Fold verification into image hardening:** Add signature verification to the processes that obtain and build your images, so unverified artifacts never reach a hardened image. 

1.  **Establish a code-signing lifecycle for your own artifacts:** Use [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) to generate and protect signing keys and to sign your code and images during the build. 

1.  **Verify your signatures at deployment and run time:** Configure [code signing for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) and container image signing for [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-signing.html) so only signed, unaltered artifacts run in your compute environments. 

1.  **Automate signing and verification in CI/CD:** Wire signing and verification into your pipelines, so every build is signed and every deployment is checked without manual steps. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC06-BP02 Provision compute from hardened images](sec06-bp02.md) 
+  [SEC06-BP05 Automate compute protection](sec06-bp05.md) 
+  [SEC06-BP01 Perform vulnerability management](sec06-bp01.md) 
+  [SEC11-BP06 Centralize services for packages and dependencies](sec11-bp06.md) 

 **Related documents:** 
+  [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) 
+  [Configure code signing for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) 
+  [Verify the signature of the AWSTOE installation download](https://docs.aws.amazon.com/imagebuilder/latest/userguide/awstoe-verify-sig.html) 
+  [Verify the signature of the SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/verify-agent-signature.html) 
+  [Verify the signature of the CloudWatch agent package](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/verify-CloudWatch-Agent-Package-Signature.html) 

 **Related examples:** 
+  [Amazon ECR managed container image signing](https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html) 
+  [Best practices to help secure your container image build pipeline by using AWS Signer](https://aws.amazon.com/blogs/security/best-practices-to-help-secure-your-container-image-build-pipeline-by-using-aws-signer/) 
+  [Announcing container image signing with AWS Signer and Amazon EKS](https://aws.amazon.com/blogs/containers/announcing-container-image-signing-with-aws-signer-and-amazon-eks/) 
+  [Signing and validating OCI artifacts with AWS Signer](https://aws.amazon.com/blogs/containers/signing-and-validating-oci-artifacts-with-aws-signer/) 

 **Related tools:** 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) 
+  [AWS Key Management Service](https://aws.amazon.com/kms/) 
+  [AWS CodeArtifact](https://aws.amazon.com/codeartifact/) 