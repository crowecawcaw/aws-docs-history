

# Machine learning product pricing for AWS Marketplace
<a name="machine-learning-pricing"></a>

You can choose from several available pricing models for your Amazon SageMaker AI products in AWS Marketplace. Buyers who subscribe to your product run it in SageMaker AI within their own AWS account. The price for your buyers is a combination of the infrastructure costs for the resources running in their AWS account and the product pricing that you set. The following sections provide information about pricing models for SageMaker AI products in AWS Marketplace

**Topics**
+ [Infrastructure pricing](#ml-infrastructure-pricing)
+ [Software pricing](#ml-software-pricing)

## Infrastructure pricing
<a name="ml-infrastructure-pricing"></a>

Buyers are responsible for all the infrastructure costs of SageMaker AI while using your product. These costs are set by AWS and are available on the [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/) page.

## Software pricing
<a name="ml-software-pricing"></a>

You determine the software prices that AWS Marketplace charges the buyer for using your product. You set the pricing and terms when you add your machine learning product to AWS Marketplace.

All infrastructure and software prices per instance type are presented to the buyer on the product listing pages in AWS Marketplace before the buyer subscribes.

**Topics**
+ [Free pricing](#ml-pricing-free)
+ [Hourly pricing](#ml-pricing-hourly)
+ [Inference pricing](#ml-pricing-inference)
+ [Free trial](#ml-pricing-free-trial)

### Free pricing
<a name="ml-pricing-free"></a>

You can choose to offer your product for free. In this case, the buyer only pays for infrastructure costs.

### Hourly pricing
<a name="ml-pricing-hourly"></a>

You can offer your product with a price per hour per instance of your software running in SageMaker AI. You can charge a different hourly price for each instance type that your software runs on. While a buyer runs your software, AWS Marketplace tracks usage and then bills the buyer accordingly. Usage is prorated to the minute.

For *model package* products, buyer can run your software in two different ways. They can host an endpoint continuously to perform real-time inference or run a batch transform job on a dataset. You can set different pricing for both of the ways a buyer can run your software.

For *algorithm* products, in addition to determining the prices for performing inference, as mentioned earlier, you also determine an hourly price for training jobs. You can charge a different hourly price for each instance type that your training image supports.

### Inference pricing
<a name="ml-pricing-inference"></a>

When the buyer runs your software by hosting an endpoint to continuously perform real-time inference, you can choose to set a price per inference.

**Note**  
The following ML product types always use hourly pricing:  
Batch transform jobs
Asynchronous inference endpoints
Training jobs for algorithm products
You set the price for each type independently of the inference pricing and of each other.

By default, with inference pricing, AWS Marketplace charges your buyer for each invocation of your endpoint. However, in some cases, your software processes a batch of inferences in a single invocation (also known as a *mini-batch*). For an endpoint deployment, you can indicate a custom number of inferences that AWS Marketplace should charge the buyer for that single invocation. To do this, include a custom metering header in the HTTP response headers of your invocation, as in the following example. This example shows an invocation that charges the buyer for three inferences.

```
X-Amzn-Inference-Metering: {"Dimension": "inference.count", "ConsumedUnits": 3}
```

**Note**  
For inference pricing, AWS Marketplace only charges the buyer for requests where the HTTP response code is `2XX`.

### Free trial
<a name="ml-pricing-free-trial"></a>

Optionally, you can create a free trial for your product and define the number of days of the free trial. Free trials can be 5–31 days. During the free trial, buyers can run your software as much as they want and aren't charged for your software. Buyers are charged for the infrastructure costs during the free trial. After the trial ends, they are charged your normal software price, along with the infrastructure costs.

When buyers subscribe to a product with a free trial, they receive a welcome email message. The message includes the term of the free trial, a calculated expiration date, and details on unsubscribing. A reminder email message is sent three days before the expiration date.

If you offer a free trial for your product in AWS Marketplace, you agree to the specific [refund policy](https://docs.aws.amazon.com/marketplace/latest/userguide/refunds.html#refund-policy) for free trials. 

**Note**  
For information on Private offers for machine learning, see [Private offers](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-overview.html).