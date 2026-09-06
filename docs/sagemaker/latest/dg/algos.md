

# Built-in algorithms and pretrained models in Amazon SageMaker
<a name="algos"></a>

Amazon SageMaker provides a suite of built-in algorithms, pre-trained models, and pre-built solution templates to help data scientists and machine learning practitioners get started on training and deploying machine learning models quickly. For someone who is new to SageMaker, choosing the right algorithm for your particular use case can be a challenging task. The following table provides a quick cheat sheet that shows how you can start with an example problem or use case and find an appropriate built-in algorithm offered by SageMaker that is valid for that problem type. Additional guidance organized by learning paradigms (supervised and unsupervised) and important data domains (text and images) is provided in the sections following the table.

Table: Mapping use cases to built-in algorithms



- **[Pre-trained models and pre-built solution templates](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)**
  - **** Problem types**:** Image Classification<br />Tabular Classification<br />Tabular Regression<br />Text Classification<br />Object Detection<br />Text Embedding<br />Question Answering<br />Sentence Pair Classification<br />Image Embedding<br />Named Entity Recognition<br />Instance Segmentation<br />Text Generation<br />Text Summarization<br />Semantic Segmentation<br />Machine Translation
  - ****Example problems and use cases**:** Here a few examples out of the 15 problem types that can be addressed by the pre-trained models and pre-built solution templates provided by Amazon SageMaker JumpStart:<br />Question answering: chatbot that outputs an answer for a given question.<br />Text analysis: analyze texts from models specific to an industry domain such as finance.
  - ****Data input format**:** Image, Text, Tabular
  - ****Built-in algorithms**:** Popular models, including Mobilenet, YOLO, Faster R-CNN, BERT, lightGBM, and CatBoost<br />For a list of pre-trained models available, see [JumpStart Models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html#jumpstart-models).<br />For a list of pre-built solution templates available, see [JumpStart Solutions](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html#jumpstart-solutions).

- ** [Supervised learning](#algorithms-built-in-supervised-learning) **
  - **** Problem types**:** Binary/multi-class classification / ****Example problems and use cases**:** Predict if an item belongs to a category: an email spam filter / ****Data input format**:** Tabular / ****Built-in algorithms**:** [AutoGluon-Tabular](autogluon-tabular.md), [CatBoost](catboost.md), [Factorization Machines Algorithm](fact-machines.md), [K-Nearest Neighbors (k-NN) Algorithm](k-nearest-neighbors.md), [LightGBM](lightgbm.md), [Linear Learner Algorithm](linear-learner.md), [TabTransformer](tabtransformer.md), [XGBoost algorithm with Amazon SageMaker AI](xgboost.md)
  - **** Problem types**:** Regression / ****Example problems and use cases**:** Predict a numeric/continuous value: estimate the value of a house / ****Data input format**:** Tabular / ****Built-in algorithms**:** [AutoGluon-Tabular](autogluon-tabular.md), [CatBoost](catboost.md), [Factorization Machines Algorithm](fact-machines.md), [K-Nearest Neighbors (k-NN) Algorithm](k-nearest-neighbors.md), [LightGBM](lightgbm.md), [Linear Learner Algorithm](linear-learner.md), [TabTransformer](tabtransformer.md), [XGBoost algorithm with Amazon SageMaker AI](xgboost.md)
  - **** Problem types**:** Time-series forecasting / ****Example problems and use cases**:** Based on historical data for a behavior, predict future behavior: predict sales on a new product based on previous sales data. / ****Data input format**:** Tabular / ****Built-in algorithms**:** [Use the SageMaker AI DeepAR forecasting algorithm](deepar.md)
  - **** Problem types**:** Embeddings: convert high-dimensional objects into low-dimensional space. / ****Example problems and use cases**:** Improve the data embeddings of the high-dimensional objects: identify duplicate support tickets or find the correct routing based on similarity of text in the tickets / ****Data input format**:** Tabular / ****Built-in algorithms**:** [Object2Vec Algorithm](object2vec.md)

- **[Unsupervised learning](#algorithms-built-in-unsupervised-learning)**
  - **** Problem types**:** Feature engineering: dimensionality reduction / ****Example problems and use cases**:** Drop those columns from a dataset that have a weak relation with the label/target variable: the color of a car when predicting its mileage. / ****Data input format**:** Tabular / ****Built-in algorithms**:** [Principal Component Analysis (PCA) Algorithm](pca.md)
  - **** Problem types**:** Anomaly detection / ****Example problems and use cases**:** Detect abnormal behavior in application: spot when an IoT sensor is sending abnormal readings / ****Data input format**:** Tabular / ****Built-in algorithms**:** [Random Cut Forest (RCF) Algorithm](randomcutforest.md)
  - **** Problem types**:** IP anomaly detection / ****Example problems and use cases**:** Protect your application from suspicious users: detect if an IP address accessing a service might be from a bad actor / ****Data input format**:** Tabular / ****Built-in algorithms**:** [IP Insights](ip-insights.md)
  - **** Problem types**:** Clustering or grouping / ****Example problems and use cases**:** Group similar objects/data together: find high-, medium-, and low-spending customers from their transaction histories / ****Data input format**:** Tabular / ****Built-in algorithms**:** [K-Means Algorithm](k-means.md)
  - **** Problem types**:** Topic modeling / ****Example problems and use cases**:** Organize a set of documents into topics (not known in advance): tag a document as belonging to a medical category based on the terms used in the document. / ****Data input format**:** Text / ****Built-in algorithms**:** [Latent Dirichlet Allocation (LDA) Algorithm](lda.md), [Neural Topic Model (NTM) Algorithm](ntm.md)

- ** [Textual analysis](#algorithms-built-in-text-analysis) **
  - **** Problem types**:** Text classification  / ****Example problems and use cases**:** Assign pre-defined categories to documents in a corpus: categorize books in a library into academic disciplines / ****Data input format**:** Text / ****Built-in algorithms**:** [BlazingText algorithm](blazingtext.md), [Text Classification - TensorFlow](text-classification-tensorflow.md)
  - **** Problem types**:** Machine translationalgorithm / ****Example problems and use cases**:** Convert text from one language to other: Spanish to English / ****Data input format**:** Text / ****Built-in algorithms**:** [Sequence-to-Sequence Algorithm](seq-2-seq.md)
  - **** Problem types**:** Text summarization / ****Example problems and use cases**:** Summarize a long text corpus: an abstract for a research paper / ****Data input format**:** Text / ****Built-in algorithms**:** [Sequence-to-Sequence Algorithm](seq-2-seq.md)
  - **** Problem types**:** Speech-to-text / ****Example problems and use cases**:** Convert audio files to text: transcribe call center conversations for further analysis / ****Data input format**:** Text / ****Built-in algorithms**:** [Sequence-to-Sequence Algorithm](seq-2-seq.md)

- **[Image processing](#algorithms-built-in-image-processing)**
  - **** Problem types**:** Image and multi-label classification / ****Example problems and use cases**:** Label/tag an image based on the content of the image: alerts about adult content in an image / ****Data input format**:** Image / ****Built-in algorithms**:** [Image Classification - MXNet](image-classification.md)
  - **** Problem types**:** Image classification / ****Example problems and use cases**:** Classify something in an image using transfer learning. / ****Data input format**:** Image / ****Built-in algorithms**:** [Image Classification - TensorFlow](image-classification-tensorflow.md)
  - **** Problem types**:** Object detection and classification / ****Example problems and use cases**:** Detect people and objects in an image: police review a large photo gallery for a missing person / ****Data input format**:** Image / ****Built-in algorithms**:** [Object Detection - MXNet](object-detection.md), [Object Detection - TensorFlow](object-detection-tensorflow.md)
  - **** Problem types**:** Computer vision / ****Example problems and use cases**:** Tag every pixel of an image individually with a category: self-driving cars prepare to identify objects in their way / ****Data input format**:** Image / ****Built-in algorithms**:** [Semantic Segmentation Algorithm](semantic-segmentation.md)



For important information about the following items common to all of the built-in algorithms provided by SageMaker AI, see [Parameters for Built-in Algorithms](common-info-all-im-models.md).
+ Docker registry paths
+ data formats
+ recommended Amazon EC2 instance types
+ CloudWatch logs

The following sections provide additional guidance for the Amazon SageMaker AI built-in algorithms grouped by the supervised and unsupervised learning paradigms to which they belong. For descriptions of these learning paradigms and their associated problem types, see [Types of Algorithms](algorithms-choose.md). Sections are also provided for the SageMaker AI built-in algorithms available to address two important machine learning domains: textual analysis and image processing.
+ [Pre-trained models and solution templates](#algorithms-built-in-jumpstart)
+ [Supervised learning](#algorithms-built-in-supervised-learning)
+ [Unsupervised learning](#algorithms-built-in-unsupervised-learning)
+ [Textual analysis](#algorithms-built-in-text-analysis)
+ [Image processing](#algorithms-built-in-image-processing)

## Pre-trained models and solution templates
<a name="algorithms-built-in-jumpstart"></a>

Amazon SageMaker JumpStart provides a wide range of pre-trained models, pre-built solution templates, and examples for popular problem types. These use the SageMaker SDK as well as Studio Classic. For more information about these models, solutions, and the example notebooks provided by Amazon SageMaker JumpStart, see [SageMaker JumpStart pretrained models](studio-jumpstart.md).

## Supervised learning
<a name="algorithms-built-in-supervised-learning"></a>

Amazon SageMaker AI provides several built-in general purpose algorithms that can be used for either classification or regression problems.
+ [AutoGluon-Tabular](autogluon-tabular.md)—an open-source AutoML framework that succeeds by ensembling models and stacking them in multiple layers. 
+ [CatBoost](catboost.md)—an implementation of the gradient-boosted trees algorithm that introduces ordered boosting and an innovative algorithm for processing categorical features.
+ [Factorization Machines Algorithm](fact-machines.md)—an extension of a linear model that is designed to economically capture interactions between features within high-dimensional sparse datasets.
+ [K-Nearest Neighbors (k-NN) Algorithm](k-nearest-neighbors.md)—a non-parametric method that uses the k nearest labeled points to assign a value. For classification, it is a label to a new data point. For regression, it is a predicted target value from the average of the k nearest points.
+ [LightGBM](lightgbm.md)—an implementation of the gradient-boosted trees algorithm that adds two novel techniques for improved efficiency and scalability. These two novel techniques are Gradient-based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB).
+ [Linear Learner Algorithm](linear-learner.md)—learns a linear function for regression or a linear threshold function for classification.
+ [TabTransformer](tabtransformer.md)—a novel deep tabular data modeling architecture built on self-attention-based Transformers. 
+ [XGBoost algorithm with Amazon SageMaker AI](xgboost.md)—an implementation of the gradient-boosted trees algorithm that combines an ensemble of estimates from a set of simpler and weaker models.

Amazon SageMaker AI also provides several built-in supervised learning algorithms used for more specialized tasks during feature engineering and forecasting from time series data.
+ [Object2Vec Algorithm](object2vec.md)—a new highly customizable multi-purpose algorithm used for feature engineering. It can learn low-dimensional dense embeddings of high-dimensional objects to produce features that improve training efficiencies for downstream models. While this is a supervised algorithm, there are many scenarios in which the relationship labels can be obtained purely from natural clusterings in data. Even though it requires labeled data for training, this can occur without any explicit human annotation.
+ [Use the SageMaker AI DeepAR forecasting algorithm](deepar.md)—a supervised learning algorithm for forecasting scalar (one-dimensional) time series using recurrent neural networks (RNN).

## Unsupervised learning
<a name="algorithms-built-in-unsupervised-learning"></a>

Amazon SageMaker AI provides several built-in algorithms that can be used for a variety of unsupervised learning tasks. These tasks includes things like clustering, dimension reduction, pattern recognition, and anomaly detection.
+ [Principal Component Analysis (PCA) Algorithm](pca.md)—reduces the dimensionality (number of features) within a dataset by projecting data points onto the first few principal components. The objective is to retain as much information or variation as possible. For mathematicians, principal components are eigenvectors of the data's covariance matrix.
+ [K-Means Algorithm](k-means.md)—finds discrete groupings within data. This occurs where members of a group are as similar as possible to one another and as different as possible from members of other groups.
+ [IP Insights](ip-insights.md)—learns the usage patterns for IPv4 addresses. It is designed to capture associations between IPv4 addresses and various entities, such as user IDs or account numbers.
+ [Random Cut Forest (RCF) Algorithm](randomcutforest.md)—detects anomalous data points within a data set that diverge from otherwise well-structured or patterned data.

## Textual analysis
<a name="algorithms-built-in-text-analysis"></a>

SageMaker AI provides algorithms that are tailored to the analysis of textual documents. This includes text used in natural language processing, document classification or summarization, topic modeling or classification, and language transcription or translation.
+ [BlazingText algorithm](blazingtext.md)—a highly optimized implementation of the Word2vec and text classification algorithms that scale to large datasets easily. It is useful for many downstream natural language processing (NLP) tasks.
+ [Sequence-to-Sequence Algorithm](seq-2-seq.md)—a supervised algorithm commonly used for neural machine translation. 
+ [Latent Dirichlet Allocation (LDA) Algorithm](lda.md)—an algorithm suitable for determining topics in a set of documents. It is an *unsupervised algorithm*, which means that it doesn't use example data with answers during training.
+ [Neural Topic Model (NTM) Algorithm](ntm.md)—another unsupervised technique for determining topics in a set of documents, using a neural network approach.
+ [Text Classification - TensorFlow](text-classification-tensorflow.md)—a supervised algorithm that supports transfer learning with available pretrained models for text classification.

## Image processing
<a name="algorithms-built-in-image-processing"></a>

SageMaker AI also provides image processing algorithms that are used for image classification, object detection, and computer vision.
+ [Image Classification - MXNet](image-classification.md)—uses example data with answers (referred to as a *supervised algorithm*). Use this algorithm to classify images.
+ [Image Classification - TensorFlow](image-classification-tensorflow.md)—uses pretrained TensorFlow Hub models to fine-tune for specific tasks (referred to as a *supervised algorithm*). Use this algorithm to classify images.
+ [Semantic Segmentation Algorithm](semantic-segmentation.md)—provides a fine-grained, pixel-level approach to developing computer vision applications.
+ [Object Detection - MXNet](object-detection.md)—detects and classifies objects in images using a single deep neural network. It is a supervised learning algorithm that takes images as input and identifies all instances of objects within the image scene.
+ [Object Detection - TensorFlow](object-detection-tensorflow.md)—detects bounding boxes and object labels in an image. It is a supervised learning algorithm that supports transfer learning with available pretrained TensorFlow models.

**Topics**
+ [Pre-trained models and solution templates](#algorithms-built-in-jumpstart)
+ [Supervised learning](#algorithms-built-in-supervised-learning)
+ [Unsupervised learning](#algorithms-built-in-unsupervised-learning)
+ [Textual analysis](#algorithms-built-in-text-analysis)
+ [Image processing](#algorithms-built-in-image-processing)
+ [Parameters for Built-in Algorithms](common-info-all-im-models.md)
+ [Built-in SageMaker AI Algorithms for Tabular Data](algorithms-tabular.md)
+ [Built-in SageMaker AI Algorithms for Text Data](algorithms-text.md)
+ [Built-in SageMaker AI Algorithms for Time-Series Data](algorithms-time-series.md)
+ [Unsupervised Built-in SageMaker AI Algorithms](algorithms-unsupervised.md)
+ [Built-in SageMaker AI Algorithms for Computer Vision](algorithms-vision.md)