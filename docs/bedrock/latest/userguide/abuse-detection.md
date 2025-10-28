# Amazon Bedrock abuse detection

AWS is committed to the responsible use of AI. To help prevent potential misuse,
Amazon Bedrock implements automated abuse detection mechanisms to identify potential violations of
AWS’s [Acceptable Use
Policy](https://aws.amazon.com/aup/ "https://aws.amazon.com/aup/") (AUP) and Service Terms, including the [Responsible AI
Policy](https://aws.amazon.com/machine-learning/responsible-ai/policy/ "https://aws.amazon.com/machine-learning/responsible-ai/policy/") or a third-party model provider’s AUP.

Our abuse detection mechanisms are fully automated, so there is no human review of, or
access to, user inputs or model outputs.

Automated abuse detection includes:

- **Categorize content** — We use classifiers to
  detect harmful content (such as content that incites violence) in user inputs and
  model outputs. A classifier is an algorithm that processes model inputs and outputs,
  and assigns type of harm and level of confidence. We may run these classifiers on
  both Titan and third-party model usage. This may include models that are fine-tuned using Amazon Bedrock's model customization. The classification process is
  automated and does not involve human review of user inputs or model outputs.
- **Identify patterns** — We use classifier
  metrics to identify potential violations and recurring behavior. We may compile and
  share anonymized classifier metrics with third-party model providers. Amazon Bedrock
  does not store user input or model output and does not share these with third-party
  model providers.
- **Detecting and blocking child sexual abuse material (CSAM)** —
  You are responsible for the content you (and your end users) upload to Amazon Bedrock and must ensure
  this content is free from illegal images. To help stop the dissemination of CSAM, Amazon Bedrock may use
  automated abuse detection mechanisms (such as hash matching technology or classifiers) to detect apparent CSAM.
  If Amazon Bedrock detects apparent CSAM in your image inputs, Amazon Bedrock will block the request and you
  will receive an automated error message. Amazon Bedrock may also file a report with the National Center for
  Missing and Exploited Children (NCMEC) or a relevant authority. We take CSAM seriously and will continue
  to update our detection, blocking, and reporting mechanisms. You might be required by applicable laws to take
  additional actions, and you are responsible for those actions.
  Once our automated abuse detection mechanisms identify potential violations, we may
  request information about your use of Amazon Bedrock and compliance with our terms of service or a
  third-party provider’s AUP. In the event that you are non-responsive, unwilling, or
  unable to comply with these terms or policies, AWS may suspend your access to Amazon Bedrock.
  You may also be billed for the failed fine-tuning jobs if our automated tests detect model
  responses being inconsistent with third-party model-providers' license terms and
  policies.

Contact AWS Support if you have additional questions. For more information, see the
[Amazon Bedrock FAQs](https://aws.amazon.com/bedrock/faqs/?refid=6f95042b-28fe-493f-8858-601fe99cea89 "https://aws.amazon.com/bedrock/faqs/?refid=6f95042b-28fe-493f-8858-601fe99cea89").
