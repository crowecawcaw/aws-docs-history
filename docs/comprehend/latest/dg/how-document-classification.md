# Custom classification

Use _custom classification_ to organize your documents into categories (classes) that you
define. Custom classification is a two-step process. First, you train a custom classification model (also called a
classifier) to recognize the classes that are of interest to you. Then you use your model to classify any number of
document sets.

For example, you can categorize the content of support requests so that you can route the request to the proper
support team. Or you can categorize emails received from customers to provide guidance based on the type of customer
request. You can combine Amazon Comprehend with Amazon Transcribe to convert speech to text and then classify the requests coming from
support phone calls.

You can run custom classification on a single document synchronously (in real time) or start an asynchronous job
to classify a set of documents. You can have multiple custom classifiers in your account, each trained using
different data. Custom classification supports a variety of input document types, such as plain text, PDF, Word, and
images.

When you submit a classification job, you choose the classifier model to use, based on the type of documents
that you need to analyze. For example, to analyze plain-text documents, you achieve the most accurate results by
using a model that you trained with plain-text documents. To analyze semi-structured documents (such as PDF, Word,
images, Amazon Textract output, or scanned files) , you achieve the most accurate results by using a model that you
trained with native documents.

###### Topics

- [Preparing classifier training data](prep-classifier-data.md "prep-classifier-data.md")
- [Training classification models](training-classifier-model.md "training-classifier-model.md")
- [Running real-time analysis](running-class-sync.md "running-class-sync.md")
- [Running asynchronous jobs](running-classifiers.md "running-classifiers.md")
