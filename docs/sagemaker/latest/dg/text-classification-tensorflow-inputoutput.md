# Input and output interface

for the Text Classification - TensorFlow algorithm

Each of the pretrained models listed in TensorFlow Hub Models can be fine-tuned to any
dataset made up of text sentences with any number of classes. The pretrained model
attaches a classification layer to the Text Embedding model and initializes the layer
parameters to random values. The output dimension of the classification layer is
determined based on the number of classes detected in the input data.

Be mindful of how to format your training data for input to the Text Classification -
TensorFlow model.

- **Training data input format:** A directory
  containing a `data.csv` file. Each row of the first column should
  have integer class labels between 0 and the number of classes. Each row of the
  second column should have the corresponding text data.
  The following is an example of an input CSV file. Note that the file should not have
  any header. The file should be hosted in an Amazon S3 bucket with a path similar to the
  following:
  `s3://`bucket_name`/`input_directory`/`.
  Note that the trailing `/` is required.

````
|   |  |
|---|---|
|0 |hide new secretions from the parental units|
|0 |contains no wit , only labored gags|
|1 |that loves its characters and communicates something rather beautiful about human nature|
|...|...| ``` ## Incremental training You can seed the training of a new model with artifacts from a model that you trained previously with SageMaker AI. Incremental training saves training time when you want to train a new model with the same or similar data. ###### Note You can only seed a SageMaker AI Text Classification - TensorFlow model with another Text Classification - TensorFlow model trained in SageMaker AI. You can use any dataset for incremental training, as long as the set of classes remains the same. The incremental training step is similar to the fine-tuning step, but instead of starting with a pretrained model, you start with an existing fine-tuned model. For more information on using incremental training with the SageMaker AI Text Classification - TensorFlow algorithm, see the [Introduction to JumpStart - Text Classification](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/jumpstart_text_classification/Amazon_JumpStart_Text_Classification.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/jumpstart_text_classification/Amazon_JumpStart_Text_Classification.ipynb") sample notebook. ## Inference with the Text Classification - TensorFlow algorithm You can host the fine-tuned model that results from your TensorFlow Text Classification training for inference. Any raw text formats for inference must be content type `application/x-text`. Running inference results in probability values, class labels for all classes, and the predicted label corresponding to the class index with the highest probability encoded in JSON format. The Text Classification - TensorFlow model processes a single string per request and outputs only one line. The following is an example of a JSON format response: ``` accept: application/json;verbose {"probabilities": [`prob_0`, `prob_1`, `prob_2`, ...], "labels": [`label_0`, `label_1`, `label_2`, ...], "predicted_label": `predicted_label`} ``` If `accept` is set to `application/json`, then the model only outputs probabilities.
````
