

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Labels
<a name="labels"></a>

A label classifies an event as fraudulent or legitimate. Labels are associated with event types and used to train machine learning models in Amazon Fraud Detector. If you are planning to train either an Online Fraud Insights (OFI) or a Transaction Fraud Insights (TFI) model, a minimum of 400 events in your training dataset must be classified as either *fradulent* or *legitimate*. You can use any labels such as *fraud*, *legit*, *1*, or *0* for classifying events in your training dataset. After the training is complete, the trained model evaluates events for fraud and uses these values to classify events as fraudulent or legitimate.

You will have to first create the labels with the values used in your training dataset and then associate the labels with the event type that is used to build and train your fraud detection model.