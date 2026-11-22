

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create nodes with pre-built optimized images

You can deploy nodes with pre-built Amazon EKS optimized [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMIs) or your own custom AMIs when you use managed node groups or self-managed nodes. If you are running hybrid nodes, see [Prepare operating system for hybrid nodes](hybrid-nodes-os.md). For information about each type of Amazon EKS optimized AMI, see one of the following topics. For instructions on how to create your own custom AMI, see [Build a custom EKS-optimized Amazon Linux AMI](eks-ami-build-scripts.md).

**Nitro Sandboxes AMIs**  
EKS Auto Mode includes Nitro Sandbox support with no additional configuration. For managed node groups or self-managed nodes, build a compatible AMI that includes the Nitro Sandbox runtime. For more information, see [Create and update a Nitro Sandbox AMI](sandboxing-ami-create-update.md).

With Amazon EKS Auto Mode, EKS manages the EC2 instance including selecting and updating the AMI.

**Topics**
+ [Guide to EKS AL2 & AL2-Accelerated AMIs transition features](eks-ami-deprecation-faqs.md)
+ [Create nodes with optimized Amazon Linux AMIs](eks-optimized-ami.md)
+ [Create nodes with optimized Bottlerocket AMIs](eks-optimized-ami-bottlerocket.md)
+ [Create nodes with optimized Ubuntu Linux AMIs](eks-partner-amis.md)
+ [Create nodes with optimized Windows AMIs](eks-optimized-windows-ami.md)