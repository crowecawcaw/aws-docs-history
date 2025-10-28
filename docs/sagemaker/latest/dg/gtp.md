# Use Amazon SageMaker Ground Truth Plus to Label Data

Amazon SageMaker Ground Truth Plus is a turnkey data labeling service that uses an
expert workforce to deliver high-quality annotations quickly and reduces costs by up
to 40%. Using SageMaker Ground Truth Plus, data scientists and business managers, such as data operations
managers and program managers, can create high-quality training datasets without having to
build labeling applications and manage labeling workforces on their own. You can get started
with Amazon SageMaker Ground Truth Plus by uploading data along with the labeling requirements
in Amazon S3.

###### Why use SageMaker Ground Truth Plus?

To train a machine learning (ML) model, data scientists need large, high-quality,
labeled datasets. As ML adoption grows, labeling needs increase. This forces data scientists
to spend weeks on building data labeling workflows and managing a data labeling workforce.
Unfortunately, this slows down innovation and increases cost. To ensure data scientists
can spend their time building, training, and deploying ML models, data scientists typically
task other in-house teams consisting of data operations managers and program managers to
produce high-quality training datasets. However, these teams typically don't have access to
skills required to deliver high-quality training datasets, which affects ML results.
As a result, you look for a data labeling partner that can help them create
high-quality training datasets at scale without consuming their in-house resources.

When you upload the data, SageMaker Ground Truth Plus sets up the data labeling workflows and
operates them on your behalf. From there, an expert workforce trained on a varierty of machine learning (ML) tasks
performs data labeling. SageMaker Ground Truth Plus currently offers two types of expert workforce: an Amazon employed workforce
and a curated list of third-party vendors. SageMaker Ground Truth Plus provides you with the flexibility to choose the labeling workforce.
AWS experts select the best labeling workforce based on your project
requirements. For example, if you need people proficient in labeling audio files, specify that in
the guidelines provided to SageMaker Ground Truth Plus, and the service automatically selects labelers with those
skills.

###### Important

SageMaker Ground Truth Plus does not support PHI, PCI or FedRAMP certified data, and you should not provide this data to SageMaker Ground Truth Plus.

###### How does SageMaker Ground Truth Plus work?

There are five main components to a workflow.

- Requesting a project
- Creating a project team
- Accessing the project portal to monitor progress of training datasets and review labeled data
- Creating a batch
- Receiving the labeled data

###### How do I use SageMaker Ground Truth Plus?

If you are a first-time user of SageMaker Ground Truth Plus, use [Getting Started with Amazon SageMaker Ground Truth Plus.](gtp-getting-started.md "gtp-getting-started.md") get started. To access SageMaker Ground Truth Plus using the SageMaker AI console, you must be in US East (N. Virginia) (`us-east-1`).
