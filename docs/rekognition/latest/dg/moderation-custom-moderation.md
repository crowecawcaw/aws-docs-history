

# Enhancing accuracy with Custom Moderation
<a name="moderation-custom-moderation"></a>

 Amazon Rekognition’s [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) API lets you detect content that is inappropriate, unwanted, or offensive. The Rekognition Custom Moderation feature allows you to enhance the accuracy of [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) by using adapters. Adapters are modular components that can be added to an existing Rekognition deep learning model, extending its capabilities for the tasks it’s trained on. By creating an adapter and providing it to the [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) operation, you can achieve better accuracy for the content moderation tasks related to your specific use case.

When customizing Rekognition’s content moderation model for specific moderation labels, you must create a project and train an adapter on a set of images you provide. You can then iteratively check the adapter’s performance and retrain the adapter to your desired level of accuracy. Projects are used to contain the different versions of adapters. 

You can use the Rekognition console to create projects and adapters. Alternatively, you can make use of an AWS SDK and the associated APIs to create a project, train an adapter, and manage your adapters. 

