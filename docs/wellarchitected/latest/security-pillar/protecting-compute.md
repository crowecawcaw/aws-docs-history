# Protecting compute

Compute resources include EC2 instances, containers, AWS Lambda functions, database
services, IoT devices, and more. Each of these compute resource types require different
approaches to secure them. However, they do share common strategies that you need to consider:
defense in depth, vulnerability management, reduction in attack surface, automation of
configuration and operation, and performing actions at a distance. In this section, you will
find general guidance for protecting your compute resources for key services. For each AWS
service used, it’s important for you to check the specific security recommendations in the
service documentation.

###### Best practices

- [SEC06-BP01 Perform vulnerability management](sec_protect_compute_vulnerability_management.md "sec_protect_compute_vulnerability_management.md")
- [SEC06-BP02 Provision compute from hardened images](sec_protect_compute_hardened_images.md "sec_protect_compute_hardened_images.md")
- [SEC06-BP03 Reduce manual management and interactive
  access](sec_protect_compute_reduce_manual_management.md "sec_protect_compute_reduce_manual_management.md")
- [SEC06-BP04 Validate software integrity](sec_protect_compute_validate_software_integrity.md "sec_protect_compute_validate_software_integrity.md")
- [SEC06-BP05 Automate compute protection](sec_protect_compute_auto_protection.md "sec_protect_compute_auto_protection.md")
