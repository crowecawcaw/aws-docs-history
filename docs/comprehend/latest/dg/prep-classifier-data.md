# Preparing classifier training data

For custom classification, you train the model in either multi-class mode or multi-label mode. Multi-class mode
associates a single class with each document. Multi-label mode associates one or more classes with each document.
The input file formats are different for each mode, so choose the mode to use before you create the training data.

###### Note

The Amazon Comprehend console refers to multi-class mode as single-label mode.

Custom classification supports models that you train with plain-text documents and models that you train with
native documents (such as PDF, Word, or images). For more information about classifier models and their supported
document types, see [Training classification models](training-classifier-model.md "training-classifier-model.md").

To prepare data to train a custom classifier model:

1. Identify the classes that you want this classifier to analyze. Decide which mode to use (multi-class or
   multi-label).
2. Decide on the classifier model type, based on whether the model is for analyzing plain-text documents or
   semi-structured documents.
3. Gather examples of documents for each of the classes. For minimum training requirements, see [General quotas for document classification](guidelines-and-limits.md#limits-class-general "guidelines-and-limits.md#limits-class-general").
4. For a plain-text model, choose the training file format to use (CSV file or augmented manifest file). To
   train a native document model, you always use a CSV file.

###### Topics

- [Classifier training file formats](prep-class-data-format.md "prep-class-data-format.md")
- [Multi-class mode](prep-classifier-data-multi-class.md "prep-classifier-data-multi-class.md")
- [Multi-label mode](prep-classifier-data-multi-label.md "prep-classifier-data-multi-label.md")
