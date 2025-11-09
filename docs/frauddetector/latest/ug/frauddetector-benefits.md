Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Benefits

Amazon Fraud Detector provides the following benefits. These benefits make it possible for you to detect fraud fast without needing to invest the time and
resources that are traditionally required to build and maintain a fraud management system.

Automated fraud model creation

Amazon Fraud Detector’s fraud detection models are fully automated machine learning models customized to
meet your specific business needs. You can use Amazon Fraud Detector models to identify potential fraud in
any online transactions such as new account creations, online payments, and guest
checkout.

Because fraud models are created through an automated process, you can forgo many of the steps associated
with creating and training a model. These steps include data validation and enrichment, feature engineering,
algorithm selection, hyperparameter tuning, and model deployment.

To create a fraud detection model using Amazon Fraud Detector, you only upload your company’s historical fraud dataset and select the model
type. Then, Amazon Fraud Detector automatically finds the most suitable fraud detection algorithm for
your use case and creates the model. You do not need to know coding or have machine
learning expertise to create fraud detection models.

Fraud models that evolve and learn

Fraud detection models must constantly evolve to keep up with the changing fraud landscape.
Amazon Fraud Detector does this automatically by calculating information including account age, time since last activity, and
activity count. The result is that your model learns the difference between trusted customers who frequently make transactions and
the continued attempts typical of fraudsters. This helps to maintain the performance of your model longer between retraining sessions.

Fraud model performance visualization

After your model is trained using the data that you provide, Amazon Fraud Detector validates your
model performance. It also provides visual tools for you to assess the performance. For each
model that you train, you can see the model performance score, the score distribution
graph, the confusion matrix, the threshold table, and all of the inputs that you
provided ranked by their impact on model performance. Using these performance tools, you
can learn how your model is performing and what inputs are driving your model
performance. If required, you can tweak your model to improve its overall performance.

Fraud prediction

Amazon Fraud Detector generates fraud prediction for your organization’s business activities. Fraud
prediction is an evaluation of a business activity for fraud risk. Amazon Fraud Detector generates
predictions using the prediction logic with the data that's associated with the
activity. You provided this data when you created your fraud detection model. You can get fraud predictions for
a single activity in real time or get fraud predictions offline for a set of activities.

Fraud prediction explanation visualization

Amazon Fraud Detector generates prediction explanations as part of the fraud prediction process. Prediction
explanations provide insight into how each data element used to train your model has
impacted your model’s fraud prediction score. Prediction explanations are provided using
the visual tools such as tables and graphs. You can use these tools to identify visually
how much influence each data element has on the prediction scores. Then, you can use
this information to analyze the fraud patterns across your data set and detect bias, if
any. Last you can also use the prediction explanations to identify top risk indicators during a
manual fraud investigation process. This helps you narrow down the root causes that lead to false positive predictions.

Rule-based actions

After your fraud detection model is
trained you can add rules to take actions on the evaluated data, such as accept the data, send
data for review, or collect more data. A rule is a condition that tells Amazon Fraud Detector how to interpret data during fraud prediction. For example, you can
create a rule that flags suspicious customer accounts to be reviewed. You can set this
rule to be initiated if both the detected model score is greater than your predetermined
threshold and if the account payment’s authorization code (AUTH_CODE) isn’t valid.
