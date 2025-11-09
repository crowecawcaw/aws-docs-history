# Input and output interface for

the Object Detection - TensorFlow algorithm

Each of the pretrained models listed in TensorFlow Models can be fine-tuned to any dataset
with any number of image classes. Be mindful of how to format your training data for
input to the Object Detection - TensorFlow model.

- **Training data input format:** Your training
  data should be a directory with an `images` subdirectory and an
  `annotations.json` file.
  The following is an example of an input directory structure. The input directory
  should be hosted in an Amazon S3 bucket with a path similar to the following:
  `s3://`bucket_name`/`input_directory`/`.
  Note that the trailing `/` is required.

```
input_directory
    |--images
        |--abc.png
        |--def.png
    |--annotations.json
```

The `annotations.json` file should contain information for bounding boxes
and their class labels in the form of a dictionary `"images"` and
`"annotations"` keys. The value for the `"images"` key should
be a list of dictionaries. There should be one dictionary for each image with the
following information: `{"file_name": `image_name`,
 "height": `height`, "width":
 `width`, "id":
 `image_id`}`. The value for the
`"annotations"` key should also be a list of dictionaries. There should
be one dictionary for each bounding box with the following information:
`{"image_id": `image_id`, "bbox": `[xmin,
ymin, xmax, ymax]`, "category_id":
 `bbox_label`}`.

After training, a label mapping file and trained model are saved to your Amazon S3
bucket.

## Incremental training

You can seed the training of a new model with artifacts from a model that you
trained previously with SageMaker AI. Incremental training saves training time when you
want to train a new model with the same or similar data.

###### Note

You can only seed a SageMaker AI Object Detection - TensorFlow model with another Object Detection - TensorFlow model trained in SageMaker AI.

You can use any dataset for incremental training, as long as the set of classes
remains the same. The incremental training step is similar to the fine-tuning step,
but instead of starting with a pretrained model, you start with an existing
fine-tuned model. For more information about how to use incremental training with
the SageMaker AI Object Detection - TensorFlow, see the [Introduction to SageMaker TensorFlow - Object Detection](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/object_detection_tensorflow/Amazon_Tensorflow_Object_Detection.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/object_detection_tensorflow/Amazon_Tensorflow_Object_Detection.ipynb") notebook.

## Inference with the Object Detection - TensorFlow

algorithm

You can host the fine-tuned model that results from your TensorFlow Object Detection
training for inference. Any input image for inference must be in `.jpg`,
.`jpeg`, or `.png` format and be content type
`application/x-image`. The Object Detection - TensorFlow algorithm resizes
input images automatically.

Running inference results in bounding boxes, predicted classes, and the scores of
each prediction encoded in JSON format. The Object Detection - TensorFlow model processes
a single image per request and outputs only one line. The following is an example of
a JSON format response:

```
accept: application/json;verbose

{"normalized_boxes":[[`xmin1`, `xmax1`, `ymin1`, `ymax1`],....],
    "classes":[`classidx1`, `class_idx2`,...],
    "scores":[`score_1`, `score_2`,...],
    "labels": [`label1`, `label2`, ...],
    "tensorflow_model_output":`<original output of the model>`}
```

If `accept` is set to `application/json`, then the model
only outputs normalized boxes, classes, and scores.
