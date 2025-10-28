# Creating and using adapters

Adapters are modular components that can be added to the existing Rekognition deep learning
model, extending its capabilities for the tasks it’s trained on. By training a deep
learning model with adapters, you can achieve better accuracy for image analysis tasks
related to your specific use case.

To create and use an adapter, you must provide training and testing data to
Rekognition. You can accomplish this in one of two different ways:

- Bulk analysis and verification - You can create a training dataset by bulk
  analyzing images that Rekognition will analyze and assign labels to. You can then
  review the generated annotations for your images and verify or correct the
  predictions. For more information on how the Bulk analysis of images works,
  see [Bulk
  analysis](bulk-analysis.md "bulk-analysis.md").
- Manual annotation - With this approach you create your training data by
  uploading and annotating images. You create your test data by either
  uploading and annotating images or by auto-splitting.
  Choose one of the following topics to learn more:

###### Topics

- [Bulk analysis and verification](adapters-bulk-analysis.md "adapters-bulk-analysis.md")
- [Manual annotation](adapters-manual-annotation.md "adapters-manual-annotation.md")
