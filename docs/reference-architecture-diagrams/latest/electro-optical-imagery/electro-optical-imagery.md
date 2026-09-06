

# Electro-Optical Imagery on AWS
<a name="electro-optical-imagery"></a>

Publication date: **May 13, 2021 ([Diagram history](#diagram-history))**

This diagram demonstrates how to extract, process, and store electro-optical satellite imagery by using AWS.

## Electro-Optical Imagery on AWS Diagram 1
<a name="diagram1"></a>

![Reference architecture diagram showing how to process electro-optical imagery on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/electro-optical-imagery/images/electro-optical-imagery-1.png)


1. Demodulate and decode: Extract baseband waveform from modulated carrier; remove forward error correction.

1. Convert into raw sensor data: Decommutate signal frames; decrypt data.

1. Process raw images and perform QA review.
   + QA review: Confirm Images are sufficient for processing.
   + **AWS Batch**: Run multiple jobs in parallel.
     + **AWS Fargate** and **AWS Lambda**:
     + Sensor correction: Apply corrections for optical distortions. 
     + Orthorectify: Sensor perspective.
     + Georeference: Apply image to spatial grid and assign known coordinate system.
     + Generate thumbnails: Create post-processed thumbnails for customer purchase.

1. Store metadata: Store information on latitude/longitude collection, Region collection, time and date of retrieval.

1. Storage: Store preprocessed images in a variety of **Amazon Simple Storage Service** (Amazon S3) services by balancing cost savings and time of retrieval

1. Post processing and analysis: Complete imagery processing.
   + Feature extraction: Identify features in images (such as ships).
   + Naming/tagging of features: Tag features by name or identification system.
   + Time series creation: Tag images to sort by time.

1. Storage and dissemination: Final storage of images and analytics for end customer.

1. Customer delivery: Deliver final images to end customers.

## Electro-Optical Imagery on AWS Diagram 2: Classified Processing
<a name="diagram2"></a>

![Reference architecture diagram showing how to process electro-optical imagery on AWS (classified processing).](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/electro-optical-imagery/images/electro-optical-imagery-2.png)


1. Demodulate and decode: Extract baseband waveform from modulated carrier; remove forward error correction.

1. Convert into raw sensor data: Decommutate signal frames; decrypt data.

1. Immutable transaction log: Cryptographically establish provenance and fidelity.

1. Optional classified processing: Throughout the image processing, move data to the appropriate regions for classified processing.

1. Process raw images: Process raw images and perform QA review:
   + QA Review: Confirm Images are sufficient for processing
   + **AWS Batch**: Run multiple jobs in parallel.
   + **AWS Fargate** and **AWS Lambda**:
     + Sensor correction: Apply corrections for optical distortions.
     + Orthorectify: Sensor perspective.
     + Georeference: Apply image to spatial grid and assign known coordinate system.
     + Generate thumbnails: Create post-processed thumbnails for customer purchase.

1. Store metadata: Store information on latitude/longitude collection, Region collection, time, and date of retrieval.

1. Storage: Store preprocessed images in a variety of Amazon S3 services by balancing cost savings and time of retrieval.

1. Post processing and analysis: Complete imagery processing.
   + Feature extraction: Identify features in images (such as ships).
   + Naming/tagging of features: Tag features by name/identification system.
   + Time seriesc reation: Tag images to sort by time.

1. Storage and dissemination: Final storage of images and analytics for end customer.

1. Customer delivery: Deliver final images to end customers.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | May 13, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.