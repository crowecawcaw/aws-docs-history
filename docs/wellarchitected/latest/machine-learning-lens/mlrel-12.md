# MLREL-12: Allow automatic scaling of the model endpoint

Implement capabilities that allow the automatic scaling of
model endpoints. This helps ensure the reliable processing of
predictions to meet changing workload demands. Include
monitoring on endpoints to identify a threshold that initiates
the addition or removal of resources to support current
demand.

After a request to scale is received, put in place a solution
to scale backend resources supporting that endpoint.

## Implementation plan

- **Configure automatic scaling for
  Amazon SageMaker AI Endpoints**- Amazon SageMaker AI
  supports
  [automatic
  scaling (autoscaling)](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md") for your hosted models.
  SageMaker AI Endpoints can be configured with autoscaling.
  This ensures that as traffic increases in your application
  your endpoint can maintain the same level of service
  availability. Automatic scaling is a key feature of the
  cloud. It allows you to automatically provision new
  resources horizontally to handle increased user demand
  or system load. Automatic scaling is also a key
  component of creating event-driven architectures and is
  a necessary capability of any distributed system.
- **Use Amazon Elastic Inference**- With
  [Amazon Elastic Inference](https://aws.amazon.com/machine-learning/elastic-inference/ "https://aws.amazon.com/machine-learning/elastic-inference/"), you can choose the CPU
  instance in AWS that is best suited to the overall
  compute and memory needs of your application. Separately
  configure the right amount of GPU-powered inference
  acceleration, allowing you to efficiently utilize
  resources and reduce costs.
- **Use Amazon Elastic Inference
  with EC2 Auto Scaling** - When you create an
  Auto Scaling group, you can specify the information
  required to configure the
  [Amazon EC2](https://aws.amazon.com/pm/ec2/?trk=ps_a134p000004f2ZFAAY&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_US&sc_publisher=Google&sc_category=Cloud%20Computing&sc_country=US&sc_geo=NAMER&sc_outcome=acq&sc_detail=amazon%20ec2&sc_content=EC2_e&sc_matchtype=e&sc_segment=467723097970&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CCloud%20Computing%7CEC2%7CUS%7CEN%7CText&s_kwcid=AL!4422!3!467723097970!e!!g!!amazon%20ec2&ef_id=EAIaIQobChMIqsWT8Z7H8gIVAo7ICh3pVAfhEAAYASAAEgLFu_D_BwE%3AG%3As&s_kwcid=AL!4422!3!467723097970!e!!g!!amazon%20ec2 "https://aws.amazon.com/pm/ec2/?trk=ps_a134p000004f2ZFAAY&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_US&sc_publisher=Google&sc_category=Cloud%20Computing&sc_country=US&sc_geo=NAMER&sc_outcome=acq&sc_detail=amazon%20ec2&sc_content=EC2_e&sc_matchtype=e&sc_segment=467723097970&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CCloud%20Computing%7CEC2%7CUS%7CEN%7CText&s_kwcid=AL!4422!3!467723097970!e!!g!!amazon%20ec2&ef_id=EAIaIQobChMIqsWT8Z7H8gIVAo7ICh3pVAfhEAAYASAAEgLFu_D_BwE%3AG%3As&s_kwcid=AL!4422!3!467723097970!e!!g!!amazon%20ec2") instances. This includes Elastic Inference
  accelerators. To do this, specify a launch template with
  your instance configuration and the Elastic Inference
  accelerator.

## Documents

- [Automatically
  Scale Amazon SageMaker AI Model](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md")
- [What
  is Amazon Elastic Inference?](../../../elastic-inference/latest/developerguide/what-is-ei.md "../../../elastic-inference/latest/developerguide/what-is-ei.md")

## Blogs

- [Configuring
  autoscaling inference endpoints in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/")

## Videos

- [Build,
  Train and Deploy ML Models at Scale with Amazon SageMaker AI](https://www.youtube.com/watch?v=HSTK-9r2WVM "https://www.youtube.com/watch?v=HSTK-9r2WVM")
- [Deploy
  Your ML Models to Production at Scale with Amazon SageMaker AI](https://www.youtube.com/watch?v=KFuc2KWrTHs "https://www.youtube.com/watch?v=KFuc2KWrTHs")

## Examples

- [Automatically
  Scale Amazon SageMaker AI Models](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/endpoint-auto-scaling.md "https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/endpoint-auto-scaling.md")
