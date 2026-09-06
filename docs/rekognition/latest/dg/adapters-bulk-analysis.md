

# Bulk analysis and verification
<a name="adapters-bulk-analysis"></a>

With this approach, you upload a large number of images you want to use as training data and then use Rekognition to get predictions for these images, which automatically assigns labels to them. You can use these predictions as a starting point for your adapter. You can verify the accuracy of the predictions, and then train the adapter based on the verified predictions. This can be done with the AWS console.



 The following video demonstrates how to use Rekognition's Bulk Analysis capability to obtain and verify predictions for a large number of images, and then train an adapter with those predictions. 

[![AWS Videos](http://img.youtube.com/vi/IGGMHPnPZLs?si=5eoidzFPbL6i5FfY/0.jpg)](http://www.youtube.com/watch?v=IGGMHPnPZLs?si=5eoidzFPbL6i5FfY)


## Upload images for bulk analysis
<a name="adapters-bulk-analysis-upload-images"></a>

To create a training dataset for your adapter, upload images in bulk for Rekognition to predict labels for. For best results, provide as many images for training as possible up to the limit of 10000, and ensure the images are representative of all aspects of your use-case. 

When using the AWS Console you can upload images directly from your computer or provide an Amazon Simple Storage Service bucket that stores your images. However, when using the Rekognition APIs with an SDK, you must provide a manifest file that references images stored in an Amazon Simple Storage Service bucket. See [Bulk analysis](https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis.html) for more information.

## Review predictions
<a name="adapters-bulk-analysis-review-predictions"></a>

Once you have uploaded your images to the Rekognition console, Rekognition will generate labels for them. You can then verify the predictions as one of the following categories: true positive, false positive, true negative, false negative. After you have verified the predictions you can train an adapter on your feedback.

## Train the adapter
<a name="adapters-bulk-analysis-train-adapter"></a>

Once you have finished verifying the predictions returned by bulk analysis, you can initiate the training process for your adapter. 

## Get the AdapterId
<a name="adapters-bulk-analysis-get-adapter"></a>

Once the adapter has been trained, you can get the unique ID for your adapter to use with Rekognition’s image analysis APIs.

## Call the API Operation
<a name="adapters-bulk-analysis-call-operation"></a>

To apply your custom adapter, provide its ID when calling one of the image analysis APIs that supports adapters. This enhances the accuracy of predictions for your images.