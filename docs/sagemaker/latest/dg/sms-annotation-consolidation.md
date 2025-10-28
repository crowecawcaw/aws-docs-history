# Annotation consolidation

An _annotation_ is the result of a single worker's labeling task.
_Annotation consolidation_ combines the annotations of two or
more workers into a single label for your data objects. A label, which is assigned to
each object in the dataset, is a probabilistic estimate of what the true label should
be. Each object in the dataset typically has multiple annotations, but only one label or
set of labels.

You decide how many workers annotate each object in your dataset. Using
more workers can increase the accuracy of your labels, but also increases the cost of
labeling. To learn more about Ground Truth pricing, see [Amazon SageMaker Ground Truth pricing](https://aws.amazon.com/sagemaker/groundtruth/pricing/ "https://aws.amazon.com/sagemaker/groundtruth/pricing/") .

If you use the Amazon SageMaker AI console to create a labeling job, the following are the
defaults for the number of workers who can annotate objects:

- Text classification—3 workers
- Image classification—3 workers
- Bounding boxes—5 workers
- Semantic segmentation—3 workers
- Named entity recognition—3 workers
  When you use the [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md") operation, you set the number of workers to
  annotate each data object with the `NumberOfHumanWorkersPerDataObject`
  parameter. You can override the default number of workers that annotate a data object
  using the console or the [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md") operation.

Ground Truth provides an annotation consolidation function for each of its predefined
labeling tasks: bounding box, image classification, name entity recognition, semantic
segmentation, and text classification. These are the functions:

- Multi-class annotation consolidation for image and text classification uses a
  variant of the [Expectation Maximization](https://en.wikipedia.org/wiki/Expectation-maximization_algorithm "https://en.wikipedia.org/wiki/Expectation-maximization_algorithm") approach to annotations. It estimates
  parameters for each worker and uses Bayesian inference to estimate the true
  class based on the class annotations from individual workers.
- Bounding box annotation consolidates bounding boxes from multiple workers.
  This function finds the most similar boxes from different workers based on the
  [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index "https://en.wikipedia.org/wiki/Jaccard_index"), or intersection over union, of the boxes and
  averages them.
- Semantic segmentation annotation consolidation treats each pixel in a single
  image as a multi-class classification. This function treats the pixel
  annotations from workers as "votes," with more information from surrounding
  pixels incorporated by applying a smoothing function to the image.
- Named entity recognition clusters text selections by Jaccard similarity and
  calculates selection boundaries based on the mode, or the median if the mode
  isn't clear. The label resolves to the most assigned entity label in the
  cluster, breaking ties by random selection.
  You can use other algorithms to consolidate annotations. For information, see
  [Annotation consolidation function
  creation](consolidation-lambda.md "consolidation-lambda.md").
