# Supervised Fine-Tuning

###### Note

Detailed documentation is provided once subscribed

Data mixing allows combining custom training datasets with Amazon Nova's proprietary
training data for more nuanced fine-tuning, minimizing risk of catastrophic forgetting,
and preserving foundational capabilities. **This feature is
available for both Amazon Nova 1.0 and Amazon Nova 2.0 models** and supports both
text and multimodal data.

###### How to Enable Data Mixing

Add the `data_mixing` section to the recipe with the appropriate
percentage distribution across dataset categories. The `nova_data`
percentages must sum to 100.
