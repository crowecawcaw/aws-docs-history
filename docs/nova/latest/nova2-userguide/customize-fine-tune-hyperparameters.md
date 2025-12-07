# Selecting hyperparameters

We recommend that you start with the default hyperparameters, which are based on our assessment across tasks of
different complexity and data sizes. But you might need to adjust and optimize certain hyperparameters based on your use
case as you evaluate the performance.

###### Topics

- [Guidance for adjusting hyperparameters](#fine-tune-hyperparameter-guidance "#fine-tune-hyperparameter-guidance")

## Guidance for adjusting hyperparameters

The following general guidance can help you determine how to adjust the hyperparameters when fine-tuning a model.

- **Tweak the Epochs Based on Sample Size**: The default epoch number is 2, which works for most cases. In general, larger data sets require less epochs to converge, while smaller data sets require a larger training epoch to converge. We recommend that you tweak your epochs based on data sample size.
- **Prompt Structure:** Optimizing the prompting strategy can improve the performance of a fine-tuned model. It is worth investing time to optimize the prompt templates on existing models before using them for fine-tuning. We recommend that you abide by the prompting best practices followed by Amazon Nova to achieve the best performance results.
- **Increasing Effective Epochs:** As Amazon Bedrock Customization service limits the epochs to 5, this might hinder under-training on smaller datasets. Hence, for smaller samples (<1K) we recommend that you duplicate the data to make the "Effective epoch" higher. For example, if the dataset is duplicated to 2x times, training 5 epochs would be effectively mean 10 epochs on the original data. For larger samples (up to 5k) we recommend 2 epochs, for sample sizes greater than 5k we recommend using 1 epoch for faster convergence.
- **Avoid a Large Warm up Number for Small Sample:** The learning rate will gradually increase to the set value during warm up. Therefore, you should avoid a large warm up number for a small training sample because your learning rate might never reach the set value during the training process. We recommend setting the warmup steps by dividing the dataset size by 640 for Amazon Nova Micro, 160 for Nova 2 Lite and 320 for rounding the number.
- **Bigger learning rate for smaller models:** Amazon Nova Micro may benefit from a larger learning rate due to the effective batch size used on the back end.
- **Quality over Quantity**: The quality of the training data is more important than the quantity. Begin with a small, high-quality dataset for initial fine-tuning and performance evaluation, then iterate and expand based on the results.
- **Data Refinement:** For certain use cases, cleaning and improving the training data using Amazon Nova models might be beneficial. This refined data can then be used to fine-tune smaller models effectively.
- **Diversify and Augment:** You can improve the model performance by increasing the variation and diversity in your customization dataset. Your fine-tuning data and evaluation data should be consistent with the actual traffic distribution that the model will see.
- **Distillation:** Nova 2 Lite and can be used to generate training data for fine-tuning Amazon Nova Micro models. This method can be very effective if the larger models are already highly capable at the target task.

**When to Distill or Fine Tune?**

We recommend that you use distillation when

- You do not have labeled data and the larger models in the family (aka, Teacher models) are highly capable on the target task.
- Larger models are better than smaller model on the target task but you need the latency and cost profile of smaller model with the accuracy of larger models.

We recommend that you use custom fine-tuning when

- You do not see good performance, even on a larger model and there is a intelligence gap in the model.
- Your use case is in a very narrow domain and not general enough for the model to know about it.

There are 3 hyperparameters that you can adjust when fine-tuning an Understanding model.

| Hyperparameter             | Type    | Minimum  | Maximum  | Default  |
| -------------------------- | ------- | -------- | -------- | -------- |
| Epochs                     | integer | 1        | 5        | 2        |
| Learning rate              | float   | 1.00E-06 | 1.00E-04 | 1.00E-05 |
| Learning rate warmup steps | integer | 0        | 20       | 10       |
