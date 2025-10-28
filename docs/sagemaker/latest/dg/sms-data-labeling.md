# Enhanced data labeling

Amazon SageMaker Ground Truth manages sending your data objects to workers to be labeled. Labeling each data
object is a _task_. Workers complete each task until the entire labeling
job is complete. Ground Truth divides the total number of tasks into smaller
_batches_ that are sent to workers. A new batch is sent to workers
when the previous one is finished.

Ground Truth provides two features that help improve the accuracy of your data labels and reduce
the total cost of labeling your data:

- _Annotation consolidation_ helps to improve the accuracy of your data
  object labels. It combines the results of multiple workers' annotation tasks into
  one high-fidelity label.
- _Automated data labeling_ uses machine learning to label portions of your
  data automatically without having to send them to human workers.

###### Topics

- [Control the flow of data objects sent to workers](sms-batching.md "sms-batching.md")
- [Annotation consolidation](sms-annotation-consolidation.md "sms-annotation-consolidation.md")
- [Automate data labeling](sms-automated-labeling.md "sms-automated-labeling.md")
- [Chaining labeling jobs](sms-reusing-data.md "sms-reusing-data.md")
