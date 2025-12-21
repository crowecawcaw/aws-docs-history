# Speed up container startup with SOCI

SOCI (Seekable Open Container Initiative) indexing enables lazy loading of custom container
images in Amazon SageMaker Unified Studio or [Amazon SageMaker Unified Studio](../../../sagemaker/latest/dg/studio-updated.md "../../../sagemaker/latest/dg/studio-updated.md"). SOCI significantly reduces
startup times by roughly 30-70% for your custom [Bring your own image (BYOI)](byoi.md "byoi.md")
containers. Latency improvement varies depending on the size of the image, hosting instance
availability, and other application dependencies. SOCI creates an index that allows containers
to launch with only necessary components, fetching additional files on-demand as needed.

SOCI addresses slow container startup times, that interrupt iterative machine learning (ML)
development workflows, for custom images. As ML workloads become more complex, container images
have grown larger, creating startup delays that hamper development cycles.

For more information on SOCI indexing and how to use them, see [Speed up container startup with SOCI](../../../sagemaker/latest/dg/soci-indexing.md "../../../sagemaker/latest/dg/soci-indexing.md") in
the _Amazon SageMaker Unified Studio Developer Guide_.
