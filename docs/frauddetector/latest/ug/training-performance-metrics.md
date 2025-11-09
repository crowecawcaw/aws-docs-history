Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Model performance metrics

After model training is complete, Amazon Fraud Detector validates model performance using
15% of your data that was not used to train the model. You can expect your
trained Amazon Fraud Detector model to have real-world fraud detection performance that is
similar to the validation performance metrics.

As a business, you must balance between detecting more fraud, and adding more
friction to legitimate customers. To assist in choosing the right balance, Amazon Fraud Detector
provides the following tools to assess model performance:

- **Score distribution chart** – A histogram of model score distributions assumes an example population of 100,000 events. The left Y axis represents the legitimate events and the right Y axis represents the fraud events. You can select a specific model threshold by clicking on the chart area. This will update the corresponding views in the confusion matrix and ROC chart.
- **Confusion matrix** – Summarizes the model accuracy for a given score threshold by comparing model predictions versus actual results. Amazon Fraud Detector assumes an example population of 100,000 events. The distribution of fraud and legitimate events simulates the fraud rate in your businesses.
  - **True positives** – The model predicts fraud and the event is actually fraud.
  - **False positives** – The model predicts fraud but the event is actually legitimate.
  - **True negatives** – The model predicts legitimate and the event is actually legitimate.
  - **False negatives** – The model predicts legitimate but the event is actually fraud.
  - **True positive rate (TPR)** – Percentage of total
    fraud the model detects. Also known as capture rate.
  - **False positive rate (FPR)** – Percentage of total
    legitimate events that are incorrectly predicted as fraud.

- **Receiver Operator Curve (ROC)** – Plots the true positive rate as a function of false positive rate over all possible model score thresholds. View this chart by choosing **Advanced Metrics**.
- **Area under the curve (AUC)** – Summarizes TPR and FPR across all possible model score thresholds. A model with no predictive power has an AUC of 0.5, whereas a perfect model has a score of 1.0.
- **Uncertainty range** – It shows the range of AUC expected from the model. Larger range (difference in upper and lower bound of AUC > 0.1) means higher
  model uncertainty. If the uncertainty range is large (>0.1), consider providing more labeled events and retrain the model.

###### To use the model performance metrics

1. Start with the **Score distribution** chart to review the distribution of model scores for your fraud and legitimate events. Ideally, you will have a clear separation between the fraud and legitimate events. This indicates the model can accurately identify which events are fraudulent and which are legitimate. Select a model threshold by clicking on the chart area. You can see how adjusting the model score threshold impacts your true positive and false positive rates.

###### Note

The score distribution chart plots the fraud and legitimate events on two different Y axis. The left Y axis represents the legitimate events and the right Y axis represents the fraud events. 2. Review the **Confusion matrix**. Depending on your selected model score threshold, you can see the simulated impact based on a sample of 100,000 events. The distribution of fraud and legitimate events simulates the fraud rate in your businesses. Use this information to find the right balance between true positive rate and false positive rate. 3. For additional details, choose **Advanced Metrics**. Use the ROC chart to understand the relationship between true positive rate and false positive rate for any model score threshold. The ROC curve can help you fine-tune the tradeoff between true positive rate and false positive rate.

###### Note

You can also review metrics in table form by choosing **Table**.

The table view also shows the metric **Precision**. **Precision** is the percentage of fraud events correctly predicted as fraudulent as compared to all events predicted as fraudulent. 4. Use the performance metrics to determine the optimal model thresholds for
your businesses based on your goals and fraud-detection use case. For
example, if you plan to use the model to classify new account registrations
as either high, medium, or low risk, you need to identify two threshold
scores so you can draft three rule conditions as follows:

    * Scores > X are high risk
    * Scores < X but > Y are medium risk
    * Scores < Y are low risk
