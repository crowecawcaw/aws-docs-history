

# Deployment of Amazon Nova Forge Models in Amazon SageMaker Inference abuse detection
<a name="nova-sagemaker-inference-abuse-detection"></a>

AWS is committed to the responsible use of AI. To help prevent potential misuse, when you deploy Amazon Nova Forge Models in Amazon SageMaker Inference, SageMaker Inference implements automated abuse detection mechanisms to identify potential violations of AWS's [Acceptable Use Policy](https://aws.amazon.com/aup/) (AUP) and Service Terms, including the [Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

Our abuse detection mechanisms are fully automated, so there is no human review of, or access to, user inputs or model outputs.

Automated abuse detection includes:
+ **Categorize content** – We use classifiers to detect harmful content (such as content that incites violence) in user inputs and model outputs. A classifier is an algorithm that processes model inputs and outputs, and assigns type of harm and level of confidence. We may run these classifiers on Amazon Nova Forge Model usage. The classification process is automated and does not involve human review of user inputs or model outputs.
+ **Identify patterns** – We use classifier metrics to identify potential violations and recurring behavior. We may compile and share anonymized classifier metrics. Amazon SageMaker Inference does not store user input or model output.
+ **Detecting and blocking child sexual abuse material (CSAM)** – You are responsible for the content you (and your end users) upload to Amazon SageMaker Inference and must ensure this content is free from illegal images. To help stop the dissemination of CSAM, when deploying an Amazon Nova Forge Model in Amazon SageMaker Inference, SageMaker Inference may use automated abuse detection mechanisms (such as hash matching technology or classifiers) to detect apparent CSAM. If Amazon SageMaker Inference detects apparent CSAM in your image inputs, Amazon SageMaker Inference will block the request and you will receive an automated error message. Amazon SageMaker Inference may also file a report with the National Center for Missing and Exploited Children (NCMEC) or a relevant authority. We take CSAM seriously and will continue to update our detection, blocking, and reporting mechanisms. You might be required by applicable laws to take additional actions, and you are responsible for those actions.

Once our automated abuse detection mechanisms identify potential violations, we may request information about your use of Amazon SageMaker Inference and compliance with our terms of service. In the event that you are non-responsive, unwilling, or unable to comply with these terms or policies, AWS may suspend your access to Amazon SageMaker Inference. You may also be billed for the failed inference job if our automated tests detect model responses being inconsistent with our terms and policies.

Contact AWS Support if you have additional questions. For more information, see the [Amazon SageMaker FAQs](https://aws.amazon.com/sagemaker/ai/faqs/).