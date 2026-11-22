

# SEC06-BP02 Provision compute from hardened images

 A hardened image is a base operating system, container, or dependency set stripped to only what the workload needs and configured to a known secure standard. Provisioning compute from hardened images reduces the available vectors for unauthorized use and limits the impact if unintended access occurs. Acquire runtime dependencies only from trusted sources, verify their signatures, and store approved versions where your build and deploy processes can reference them. 

 **Desired outcome:** 
+  Your compute resources launch from hardened baseline images configured to a recognized standard. 
+  You retrieve external dependencies only from trusted registries and verify their signatures before use. 
+  Your approved images and libraries live in private registries that your build and deployment processes reference. 
+  You rescan and rebuild images and dependencies on a schedule, so newly discovered vulnerabilities are addressed. 

 **Common anti-patterns:** 
+  Teams pull images and libraries from trusted registries but skip signature verification and vulnerability scans before use. 
+  Teams harden an image once and never retest it for new vulnerabilities or update it to a current version. 
+  Software packages that a workload never uses remain installed on the image throughout its lifecycle. 
+  Teams rely on patching alone, which lets resources drift from the hardened standard and cannot remove malware left behind by unauthorized access. 

 **Benefits of establishing this best practice:** 
+  Fewer installed packages and open paths mean fewer opportunities for unintended access. 
+  Any unauthorized access has a smaller impact, because the image carries only the capabilities the workload needs. 
+  Verified signatures give confidence that images and libraries came from their stated source and were not altered. 
+  Rebuilding from updated images keeps the fleet consistent and removes the drift that patching alone leaves behind. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Start from the current version of the operating system, container image, or library. Apply patches for known issues, and remove what you do not use, including extra applications, services, drivers, default accounts, and open ports. Then add back only the specific agents and processes the workload requires, such as monitoring or vulnerability management. 

 You do not have to define a hardened standard from scratch. Published baselines from the [Center for Internet Security](https://www.cisecurity.org/) (CIS) and the Defense Information Systems Agency (DISA) [Security Technical Implementation Guides](https://docs.aws.amazon.com/imagebuilder/latest/userguide/ib-stig.html) (STIGs) encode years of consensus on secure configuration. A strict baseline sometimes prevents your software from running. When that happens, start from a non-hardened base, install your software, and apply controls one at a time to find which one breaks it. Where a CIS control blocks the workload, test whether a finer-grained DISA STIG setting achieves similar protection. Record the controls you can apply, and use them to define your image hardening recipes in [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html). 

 Application libraries need the same provenance controls as operating systems. Packages pulled from public repositories through tools such as pip, npm, Maven, and NuGet enter your build with everything built into them, regardless of which party modified the package. Place a private registry between your builds and the public repositories as a control point. [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html) retrieves, stores, and updates approved packages, and your build can test the current version alongside the application using software composition analysis (SCA), static application security testing (SAST), and dynamic application security testing (DAST). 

 For containers, treat the image as an immutable unit, built from a hardened base and scanned before you push it to a registry such as [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html). For serverless functions, package shared dependencies separately from function code and maintain them through their own build process. This provides a single place to keep common libraries current across many functions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Harden operating systems:** Build hardened AMIs from trusted [base images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) using [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html), applying the CIS and DISA STIG controls you validated for your workload. Automate the pipeline so every image is built the same way. 

1.  **Harden container images:** Build containers from hardened base images and run [Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) in your build pipeline and on a schedule against the repository to find CVEs before deployment. 

1.  **Manage dependencies through a private registry:** Integrate [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html) with trusted public repositories, and run SCA, SAST, and DAST against packages during the build so only tested versions reach your application. 

1.  **Harden serverless dependencies:** Use [Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) to separate shared libraries from function code, and configure [code signing for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) so only trusted code runs in your functions. 

1.  **Rescan and rebuild on a schedule:** Re-evaluate images and dependencies for newly discovered vulnerabilities, and rebuild from updated sources rather than patching resources in place. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC06-BP04 Validate software integrity](sec06-bp04.md) 
+  [SEC06-BP01 Perform vulnerability management](sec06-bp01.md) 
+  [SEC06-BP05 Automate compute protection](sec06-bp05.md) 
+  [SEC11-BP06 Centralize services for packages and dependencies](sec11-bp06.md) 
+  [OPS03-BP05 Design for efficient patch management](ops03-bp05.md) 

 **Related documents:** 
+  [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) 
+  [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) 
+  [Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) 
+  [AWS Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) 
+  [Configure code signing for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) 
+  [Center for Internet Security (CIS)](https://www.cisecurity.org/) 
+  [Amazon managed STIG hardening components for Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/ib-stig.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Implementing security best practices for serverless applications (CNS360)](https://www.youtube.com/watch?v=yDhR5VwcnYo) 

 **Related examples:** 
+  [How to manage the lifecycle of Amazon Machine Images using AMI Lineage for AWS](https://aws.amazon.com/blogs/security/how-to-manage-the-lifecycle-of-amazon-machine-images-using-ami-lineage-for-aws/) 
+  [DISA STIG for Amazon Linux 2023 is now available](https://aws.amazon.com/blogs/compute/disa-stig-for-amazon-linux-2023-is-now-available/) 
+  [Image hardening and instance refresh for Amazon ECS](https://github.com/aws-samples/ecs-image-hardening-and-instance-refresh) 

 **Related services:** 
+  [AWS CodeArtifact](https://aws.amazon.com/codeartifact/) 
+  [Amazon ECR](https://aws.amazon.com/ecr/) 
+  [EC2 Image Builder](https://aws.amazon.com/image-builder/) 