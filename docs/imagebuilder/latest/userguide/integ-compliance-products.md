

# Compliance products for your Image Builder images
<a name="integ-compliance-products"></a>

With constantly evolving security standards, it can be a challenge to maintain compliance and safeguard your organization from cyber threats. To help ensure that your custom images are compliant, and stay that way through automatic updates when publishers release new versions, Image Builder integrates with AWS Marketplace compliance products and Image Builder components.

Image Builder integrates with the following compliance products:
+ 

**Center for Internet Security (CIS) Benchmarks hardening**  
To build custom images that comply with CIS Benchmarks Level 1 guidelines, subscribe to a CIS hardening component in AWS Marketplace, and add it to an image recipe whose parent image runs an operating system that the component supports. For more information, see [CIS hardening components](toe-cis.md).
+ 

**Security Technical Implementation Guides (STIG)**  
For STIG compliance, use can use Amazon-managed AWS Task Orchestrator and Executor (AWSTOE) STIG components in your Image Builder recipes. STIG components scan your build instance for misconfigurations and run a remediation script to correct issues that they find. We can't guarantee STIG compliance for the images that you build with Image Builder. You must work with your organization's compliance team to verify that your final image is compliant. For a complete list of AWSTOE STIG components that you can use in your Image Builder recipes, see [Amazon managed STIG hardening components for Image Builder](ib-stig.md).