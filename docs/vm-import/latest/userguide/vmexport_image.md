# Export a VM from an Amazon Machine Image (AMI) using VM Import/Export

Exporting a VM file based on an Amazon Machine Image (AMI) is useful when you want to
deploy a new, standardized instance in your virtualization environment. You can
export most AMIs to Citrix Xen, Microsoft Hyper-V, or VMware vSphere.

When you export an image, you are charged the standard Amazon S3 rates for the bucket
where the exported VM is stored. In addition, there might be a small charge for the
temporary use of an Amazon EBS snapshot. For more information about Amazon S3 pricing, see [Amazon Simple Storage Service Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Contents

- [Prerequisites for exporting an
  image from Amazon EC2](prerequisites-image-export.md "prerequisites-image-export.md")
- [Considerations for image export](limits-image-export.md "limits-image-export.md")
- [Start an export image task](start-image-export.md "start-image-export.md")
- [Monitor an export image task](monitor-image-export.md "monitor-image-export.md")
- [Cancel an export image task](cancel-image-export.md "cancel-image-export.md")
