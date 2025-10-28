We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Evaluation Alerts

Amazon ML provides insights to help you validate whether you evaluated the model correctly. If
any of the validation criteria are not met by the evaluation, the Amazon ML console alerts
you by displaying the validation criterion that has been violated, as
follows.

- **Evaluation of ML model is done on held-out data**

Amazon ML alerts you if
you use the same datasource for training and evaluation. If you use Amazon ML to split your data,
you will meet this validity criterion. If you do not use Amazon ML to split your data, make sure
to evaluate your ML model with a datasource other than the training datasource.

- **Sufficient data was used for the evaluation of the predictive
  model**

Amazon ML alerts you if
the number of observations/records in your evaluation data is less than 10% the number of
observations you have in your training datasource. To properly evaluate your model, it is
important to provide a sufficiently large data sample. This criterion provides a check to
let you know if you are using too little data. The amount of data required to evaluate your
ML model is subjective. 10% is selected here as a stop gap in the absence of a better
measure.

- **Schema matched**

Amazon ML alerts you if the schema for the training and evaluation datasource are not the
same. If you have certain attributes that do not exist in the evaluation datasource or if
you have additional attributes, Amazon ML displays this alert.

- **All records from evaluation files were used for predictive model
  performance evaluation**

It is important to know if all the records provided for evaluation were actually used
for evaluating the model. Amazon ML alerts
you if some records in the evaluation datasource were invalid and were not included in the
accuracy metric computation. For example, if the target variable is missing for some of the
observations in the evaluation
datasource, Amazon ML is unable to check if the ML model's predictions for these observations are correct. In
this case, the records with missing target values are considered invalid.

- **Distribution of target variable**

Amazon ML shows you the
distribution of the target attribute from the training and evaluation datasources so
that you can
review whether the target is distributed similarly in both datasources. If the model was
trained on training data with a target distribution that differs from the distribution of
the target on the evaluation data, then the quality of the evaluation could suffer because it is
being computed on data with very different statistics. It is best to have the data
distributed similarly over training and evaluation data, and have these datasets mimic as
much as possible the data that the model will encounter when making predictions.

If this alert triggers, try using the random split strategy to split the
data into training and evaluation datasources. In rare cases, this
alert might erroneously warn you about target distribution differences even though you split your
data randomly. Amazon ML uses approximate data statistics to evaluate the data
distributions,
occasionally triggering this alert in error.
