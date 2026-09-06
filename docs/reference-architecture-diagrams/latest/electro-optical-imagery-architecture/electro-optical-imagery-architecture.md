

# Electro-Optical Imagery Reference Architecture
<a name="electro-optical-imagery-architecture"></a>

Publication date: **May 12, 2021 ([Diagram history](#diagram-history))**

This architecture enables you to process electro-optical imagery on AWS.

## Electro-Optical Imagery Reference Architecture
<a name="diagram1"></a>

![Reference architecture diagram showing how you can use AWS services to process elctro-optical imagery on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/electro-optical-imagery-architecture/images/electro-optical-imagery-architecture.png)


1. Demodulate and Decode: Extract baseband waveform from modulated carrier; remove forward error correction. 

1. Convert into raw sensor data: Decommutate signal frames; decrypt data .

1. Process Raw Images: Process Raw Images and Perform QA Review 
   + QA Review: Confirm Images are sufficient for processing 
   + **AWS Batch**: Run multiple jobs in parallel 
   + **AWS Fargate** and **AWS Lambda**: 
     + Sensor Correction: Apply corrections for optical distortions 
     + Orthorectify: Sensor perspective 
     + Georeference: Apply image to spatial grid and assign known coordinate system 
     + Generate Thumbnails: Create post-processed thumbnails for customer purchase 

1. Store metadata: Store information on latitude/longitude collection, region collection, time and date of retrieval .

1. Storage: Store preprocessed images in a variety of **Amazon S3** services by balancing cost savings and time of retrieval. 

1. Post Processing and Analysis: Complete imagery processing. 
   + Feature Extraction: Identify features in images (such as ships) 
   + Naming/Tagging of Features: Tag features by name/identification system 
   + Time Series Creation: Tag images to sort 

1. Storage and Dissemination: Final storage of images and analytics for end customer. 

1. Customer Delivery: Deliver final images to end customers 

## Electro-Optical Imagery Reference Architecture (Classified Processing)
<a name="diagram2"></a>

![Reference architecture diagram showing how to process classified electro-optical imagery on AWS](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/electro-optical-imagery-architecture/images/electro-optical-imagery-architecture2.png)


1. Demodulate and Decode: Extract baseband waveform from modulated carrier; remove forward error correction. 

1. Convert into raw sensor data: Decommutate signal frames; decrypt data . 

1. Immutable transaction log: Cryptographically establish provenance and fidelity .

1. Optional Classified Processing: Throughout the image processing, move data to the appropriate regions for classified processing. 

1. Process Raw Images: Process Raw Images and Perform QA Review 
   + QA Review: Confirm Images are sufficient for processing 
   + **AWS Batch**: Run multiple jobs in parallel 
   + **AWS Fargate** and **AWS Lambda**: 
     + Sensor Correction: Apply corrections for optical distortions 
     + Orthorectify: Sensor perspective 
     + Georeference: Apply image to spatial grid and assign known coordinate system 
     + Generate Thumbnails: Create post-processed thumbnails for customer purchase 

1. Store metadata: Store information on latitude/longitude collection, region collection, time and date of retrieval .

1. Storage: Store preprocessed images in a variety of **Amazon S3** services by balancing cost savings and time of retrieval. 

1. Post Processing and Analysis: Complete imagery processing. 
   + Feature Extraction: Identify features in images (such as ships) 
   + Naming/Tagging of Features: Tag features by name/identification system 
   + Time Series Creation: Tag images to sort 

1. Storage and Dissemination: Final storage of images and analytics for end customer. 

1. Customer Delivery: Deliver final images to end customers 

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | May 12, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.