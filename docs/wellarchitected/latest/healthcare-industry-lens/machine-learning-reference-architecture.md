

# Machine learning reference architecture
<a name="machine-learning-reference-architecture"></a>

This section depicts a typical machine learning lifecycle and data flow.

![Diagram of the machine learning lifecycle.](http://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/images/machine-learning-lifecycle.png)


The following steps detail the end-to-end data flow for machine learning:

1.  Data is collected and pre-processed using a data lake, as described in the preceding *healthcare analytics* scenario. 

1.  Features representing clinically valid events, concepts, and processes of care are extracted from raw data and stored in feature stores for model training. 

1.  The ground truth of data labels is populated and reviewed by humans, which can be used to build supervised classification or regression models. 

1.  Standard ML training, tuning, and evaluation workflows are used to develop models. 

1.  Models are reviewed by cross-functional stakeholders, such as clinical leaders and regulatory reviewers. Models are evaluated based on performance and explainability requirements 

1.  Accepted models may be integrated with IT systems used for care delivery, such as EHRs and medical devices. 

1.  Model inferences are incorporated in clinical workflows. Providers may be trained on how to use the models as they deliver care. 

1.  Model inferencing pipelines are monitored, and the performance of deployed models is periodically checked. 