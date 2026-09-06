

# Speed up container startup with SOCI
<a name="soci-indexing"></a>

SOCI (Seekable Open Container Initiative) indexing enables lazy loading of custom container images in [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.html). SOCI significantly reduces startup times by roughly 30-70% for your custom [Bring your own image (BYOI)](studio-updated-byoi.md) containers. Latency improvement varies depending on the size of the image, hosting instance availability, and other application dependencies. SOCI creates an index that allows containers to launch with only necessary components, fetching additional files on-demand as needed.

SOCI addresses slow container startup times, that interrupt iterative machine learning (ML) development workflows, for custom images. As ML workloads become more complex, container images have grown larger, creating startup delays that hamper development cycles.

**Topics**
+ [Key benefits](#soci-indexing-key-benefits)
+ [How SOCI indexing works](#soci-indexing-how-works)
+ [Architecture components](#soci-indexing-architecture-components)
+ [Supported tools](#soci-indexing-supported-tools)
+ [Permissions for SOCI indexing](soci-indexing-setup.md)
+ [Create SOCI indexes with nerdctl and SOCI CLI example](soci-indexing-example-create-indexes.md)
+ [Integrate SOCI-indexed images with Studio example](soci-indexing-example-integrate-studio.md)

## Key benefits
<a name="soci-indexing-key-benefits"></a>
+ **Faster iteration cycles**: Reduce container startup, depending on image and instance types
+ **Universal optimization**: Extend performance benefits to all custom BYOI containers in Studio

## How SOCI indexing works
<a name="soci-indexing-how-works"></a>

SOCI creates a specialized metadata index that maps your container image's internal file structure. This index enables access to individual files without downloading the entire image. The SOCI index is stored as an OCI (Open Container Initiative) compliant artifact in [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) and linked to your original container image, preserving image digests and signature validity.

When you launch a container in Studio, the system uses the SOCI index to identify and download only essential files needed for startup. Additional components are fetched in parallel as your application requires them.

## Architecture components
<a name="soci-indexing-architecture-components"></a>
+ **Original container image**: Your base container stored in Amazon ECR
+ **SOCI index artifact**: Metadata mapping your image's file structure
+ **OCI Image Index manifest**: Links your original image and SOCI index
+ **Finch container runtime**: Enables lazy loading integration with Studio

## Supported tools
<a name="soci-indexing-supported-tools"></a>


| Tool | Integration | 
| --- | --- | 
| nerdctl | Requires containerd setup | 
| Finch CLI | Native SOCI support | 
| Docker \+ SOCI CLI | Additional tooling required | 

**Topics**
+ [Key benefits](#soci-indexing-key-benefits)
+ [How SOCI indexing works](#soci-indexing-how-works)
+ [Architecture components](#soci-indexing-architecture-components)
+ [Supported tools](#soci-indexing-supported-tools)
+ [Permissions for SOCI indexing](soci-indexing-setup.md)
+ [Create SOCI indexes with nerdctl and SOCI CLI example](soci-indexing-example-create-indexes.md)
+ [Integrate SOCI-indexed images with Studio example](soci-indexing-example-integrate-studio.md)