# DNS addressing and custom domains in AWS Global Accelerator

This chapter explains how AWS Global Accelerator does DNS routing and includes information about using a
custom domain with Global Accelerator. It also includes the steps for configuring bring your own IP (BYOIP) addresses
to use with accelerators in Global Accelerator.

- **DNS addressing**: When you create an accelerator, Global Accelerator
  assigns a default Domain Name System (DNS) name to your accelerator.
- **Custom domain name**: You can configure DNS to use your custom domain name (such as
  `www.example.com`) with your accelerator, instead of using the assigned static IP
  addresses or the default DNS name.
- **BYOIP IP addresses**: You can bring your own IP addresses to AWS to add to an accelerator instead of,
  or together with, the static IP addresses that Global Accelerator assigns to you.

###### Contents

- [Support for DNS addressing](dns-addressing-custom-domains.md "dns-addressing-custom-domains.md")
- [Route custom domain traffic to your
  accelerator](dns-addressing-custom-domains.md "dns-addressing-custom-domains.md")
- [Bring your own IP addresses](using-byoip.md "using-byoip.md")
