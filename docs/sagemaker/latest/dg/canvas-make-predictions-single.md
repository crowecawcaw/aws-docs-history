# Make single predictions

###### Note

This section describes how to get single predictions from your model inside the
Canvas application. For information about making real-time invocations in a production
environment by deploying your model to an endpoint, see
[Deploy your models to an endpoint](canvas-deploy-model.md "canvas-deploy-model.md").

Make single predictions if you want to get a prediction for a single data point. You
can use this feature to get real-time predictions or to experiment with changing
individual values to see how they impact the prediction outcome. Note that single
predictions rely on an Asynchronous Inference endpoint, which shuts down after being idle (or not
receiving any prediction requests) for two hours.

Choose one of the following procedures based on your model type.

## Make single predictions with

numeric and categorical prediction models

To make a single prediction for a numeric or categorical prediction model, do the
following:

1. In the left navigation pane of the Canvas application, choose **My
   models**.
2. On the **My models** page, choose your model.
3. After opening your model, choose the **Predict** tab.
4. On the **Run predictions** page, choose **Single
   prediction**.
5. For each **Column** field, which represents the columns of
   your input data, you can change the **Value**. Select the
   dropdown menu for the **Value** you want to change. For numeric
   fields, you can enter a new number. For fields with labels, you can select a
   different label.
6. When you’re ready to generate the prediction, in the right
   **Prediction** pane, choose
   **Update**.

In the right **Prediction** pane, you’ll see the prediction result.
You can **Copy** the prediction result chart, or you can also choose
**Download** to either download the prediction result chart as an
image or to download the values and prediction as a CSV file.

## Make single predictions with

time series forecasting models

To make a single prediction for a time series forecasting model, do the
following:

1. In the left navigation pane of the Canvas application, choose **My
   models**.
2. On the **My models** page, choose your model.
3. After opening your model, choose the **Predict** tab.
4. Choose **Single prediction**.
5. For **Item**, select the item for which you want to forecast values.
6. If you used a group by column to train the model, then select the group by category for the item.

The prediction result loads in the pane below, showing you a chart with the forecast for each quantile.
Choose **Schema view** to see the numeric predicted values.
You can also choose **Download** to download the prediction results as either an
image or a CSV file.

## Make single predictions with image prediction

models

To make a single prediction for a single-label image prediction model, do the
following:

1. In the left navigation pane of the Canvas application, choose **My
   models**.
2. On the **My models** page, choose your model.
3. After opening your model, choose the **Predict** tab.
4. On the **Run predictions** page, choose **Single
   prediction**.
5. Choose **Import image**.
6. You’ll be prompted to upload an image. You can upload an image from your local
   computer or from an Amazon S3 bucket.
7. Choose **Import** to import your image and generate the
   prediction.

In the right **Prediction results** pane, the model lists the
possible labels for the image along with a **Confidence** score for
each label. For example, the model might predict the label **Sea** for
an image, with a confidence score of 96%. The model may have predicted the image as a
**Glacier** with only a confidence score of 4%. Therefore, you can
determine that your model is fairly confident in predicting images of the sea.

## Make single predictions with text prediction

models

To make a single prediction for a multi-category text prediction model, do the
following:

1. In the left navigation pane of the Canvas application, choose **My
   models**.
2. On the **My models** page, choose your model.
3. After opening your model, choose the **Predict** tab.
4. On the **Run predictions** page, choose **Single
   prediction**.
5. For the **Text field**, enter the text for which you’d like
   to get a prediction.
6. Choose **Generate prediction results** to get your
   prediction.

In the right **Prediction results** pane, you receive an analysis of
your text in addition to a **Confidence** score for each possible
label. For example, if you entered a good review for a product, you might get
**Positive** with a confidence score of 85%, while the confidence
score for **Neutral** might be 10% and the confidence score for
**Negative** only 5%.
