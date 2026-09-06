

# Built-in Task Types
<a name="sms-task-types"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

Amazon SageMaker Ground Truth has several built-in task types. Ground Truth provides a worker task template for built-in task types. Additionally, some built in task types support [Automate data labeling](sms-automated-labeling.md). The following topics describe each built-in task type and demo the worker task templates that are provided by Ground Truth in the console. To learn how to create a labeling job in the console using one of these task types, select the task type page.



| Label Images | Label Text | Label Videos and Video Frames | Label 3D Point Clouds | 
| --- | --- | --- | --- | 
|  +  [Classify image objects using a bounding box](sms-bounding-box.md) <br />+  [Create an image classification job (Single Label)](sms-image-classification.md) <br />+  [Create an image classification job (Multi-label)](sms-image-classification-multilabel.md) <br />+  [Identify image contents using semantic segmentation](sms-semantic-segmentation.md) <br />+  [Label verification and adjustment](sms-verification-data.md)   |  +  [Extract text information using named entity recognition](sms-named-entity-recg.md) <br />+  [Categorize text with text classification (Single Label)](sms-text-classification.md) <br />+  [Categorize text with text classification (Multi-label)](sms-text-classification-multilabel.md)   |  +  [Classify videos](sms-video-classification.md) <br />+  [Identify objects using video frame object detection](sms-video-object-detection.md) <br />+  [Track objects in video frames using video frame object tracking](sms-video-object-tracking.md)   |  +  [Classify objects in a 3D point cloud with object detection](sms-point-cloud-object-detection.md) <br />+  [Understand the 3D point cloud object tracking task type](sms-point-cloud-object-tracking.md) <br />+  [Understand the 3D point cloud semantic segmentation task type](sms-point-cloud-semantic-segmentation.md)   | 

**Note**  
Each of the video frame and 3D point cloud task types has an *adjustment* task type that you use to verify and adjust labels from a previous labeling job. Select a video frame or 3D point cloud task type page above to learn how to adjust labels created using that task type. 