# Interpret your results

Analyze evaluation metrics from your text classification model comparison to make data-driven decisions for production deployment.

## Understanding evaluation metrics

The evaluation provides several key metrics for each model across all datasets:

### Accuracy

Measures the percentage of correct predictions and works best for balanced datasets. However, it can be misleading with imbalanced data and may show artificially high results when one class dominates.

### Precision

Evaluates how well the model avoids false positives by measuring what percentage of positive predictions were correct. This metric ranges from 0.0 to 1.0 (higher is better) and becomes critical when false positives are costly.

### Recall

Assesses how well the model catches all positive cases by measuring what percentage of actual positives were found. It ranges from 0.0 to 1.0 (higher is better) and becomes critical when missing positives is costly.

### F1-score

Provides the harmonic mean of precision and recall, balancing both metrics into a single score that ranges from 0.0 to 1.0 (higher is better).

### Matthews Correlation Coefficient (MCC)

Measures overall binary classification quality and serves as the best metric for imbalanced data. It ranges from -1.0 to 1.0, where higher values indicate better performance and 0 represents random guessing.

### Area Under the Curve Receiver Operating Characteristic

Evaluates how well the model distinguishes between classes. It ranges from 0.0 to 1.0, where 1.0 represents perfect classification and 0.5 represents random guessing.

### Average inference time

Measures prediction speed, which becomes critical for real-time applications. Consider both speed and consistency when evaluating this metric.

###### Note

Don't rely solely on accuracy for model selection. For imbalanced datasets, precision, recall, and MCC provide more reliable indicators of real-world performance.

## Compare performance across dataset types

The **balanced dataset** shows how well your models perform under ideal conditions with equal representation of positive and negative examples. Strong performance here indicates the model has learned fundamental text classification patterns.

The **skewed dataset** reveals how models handle real-world class imbalance, which is common in production scenarios.

The **challenging dataset** tests model robustness on ambiguous or edge cases that might appear in production.

## Model selection

Use this systematic approach to select the optimal model for your specific use case.

### Define your business priorities

Before choosing a model, determine which performance factors matter most for your use case.

1. Identify your accuracy requirements and minimum acceptable performance threshold.
2. Determine your latency constraints, including whether you need real-time (<100ms) or batch processing.
3. Establish your cost considerations and budget for inference and scaling.
4. Analyze your data characteristics to understand if your production data is balanced, skewed, or highly variable.

### When to choose each model

Based on your evaluation results, choose the model that best fits your use case:

- **Choose DistilBERT** when you need faster inference with good accuracy, such as real-time sentiment analysis in customer service chatbots, content moderation systems, or applications where response time under 100ms is critical.
- **Choose BERT** when maximum accuracy is more important than speed, such as legal document classification, medical text analysis, or compliance applications where precision is paramount and batch processing is acceptable.

### Prioritize your evaluation datasets

Focus on the datasets that best represent your real-world use case.

1. Give more weight to the dataset that most closely resembles your real-world data.
2. Consider the importance of edge cases in your application and prioritize challenging dataset performance accordingly.
3. Balance optimization across multiple scenarios rather than focusing on just one dataset type.

Compare your evaluation results against these priorities to select the model that best balances your accuracy, speed, and cost requirements.

Now that you've selected your preferred model, you're ready for production deployment. Continue to [Deploy your model at scale](jumpstart-text-classification-scale.md "jumpstart-text-classification-scale.md").
