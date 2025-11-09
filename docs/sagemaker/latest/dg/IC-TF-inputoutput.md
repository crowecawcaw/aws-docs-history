# Input and output interface for the Image

Classification - TensorFlow algorithm

Each of the pretrained models listed in TensorFlow Hub Models can be fine-tuned to any
dataset with any number of image classes. Be mindful of how to format your training data
for input to the Image Classification - TensorFlow model.

- **Training data input format:** Your training
  data should be a directory with as many subdirectories as the number of classes.
  Each subdirectory should contain images belonging to that class in .jpg, .jpeg,
  or .png format.
  The following is an example of an input directory structure. This example dataset has
  two classes: `roses` and `dandelion`. The image files in each
  class folder can have any name. The input directory should be hosted in an Amazon S3 bucket
  with a path similar to the following:
  `s3://`bucket_name`/`input_directory`/`.
  Note that the trailing `/` is required.

```
input_directory
    |--roses
        |--abc.jpg
        |--def.jpg
    |--dandelion
        |--ghi.jpg
        |--jkl.jpg
```

Trained models output label mapping files that map class folder names to the indices
in the list of output class probabilities. This mapping is in alphabetical order. For
example, in the preceding example, the dandelion class is index 0 and the roses class is
index 1.

After training, you have a fine-tuned model that you can further train using
incremental training or deploy for inference. The Image Classification - TensorFlow algorithm
automatically adds a pre-processing and post-processing signature to the fine-tuned
model so that it can take in images as input and return class probabilities. The file
mapping class indices to class labels is saved along with the models.

## Incremental training

You can seed the training of a new model with artifacts from a model that you
trained previously with SageMaker AI. Incremental training saves training time when you
want to train a new model with the same or similar data.

###### Note

You can only seed a SageMaker Image Classification - TensorFlow model with another Image Classification - TensorFlow model trained in SageMaker AI.

You can use any dataset for incremental training, as long as the set of classes
remains the same. The incremental training step is similar to the fine-tuning step,
but instead of starting with a pretrained model, you start with an existing
fine-tuned model. For an example of incremental training with the SageMaker AI
Image Classification - TensorFlow algorithm, see the [Introduction to SageMaker TensorFlow - Image Classification](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/image_classification_tensorflow/Amazon_TensorFlow_Image_Classification.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/image_classification_tensorflow/Amazon_TensorFlow_Image_Classification.ipynb") sample
notebook.

## Inference with the Image Classification - TensorFlow

algorithm

You can host the fine-tuned model that results from your TensorFlow Image
Classification training for inference. Any input image for inference must be in
`.jpg`, .`jpeg`, or `.png` format and be
content type `application/x-image`. The Image Classification - TensorFlow
algorithm resizes input images automatically.

Running inference results in probability values, class labels for all classes, and
the predicted label corresponding to the class index with the highest probability
encoded in JSON format. The Image Classification - TensorFlow model processes a single
image per request and outputs only one line. The following is an example of a JSON
format response:

```
accept: application/json;verbose

 {"probabilities": [prob_0, prob_1, prob_2, ...],
  "labels":        [label_0, label_1, label_2, ...],
  "predicted_label": predicted_label}
```

If `accept` is set to `application/json`, then the model
only outputs probabilities. For more information on training and inference with the
Image Classification - TensorFlow algorithm, see the [Introduction to SageMaker TensorFlow - Image Classification](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/image_classification_tensorflow/Amazon_TensorFlow_Image_Classification.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/image_classification_tensorflow/Amazon_TensorFlow_Image_Classification.ipynb") sample
notebook.
