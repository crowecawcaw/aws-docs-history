

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

With inference pricing, buyers pay for the work your model does. You set one price per inference, and AWS Marketplace charges the buyer that price for each inference that your model reports. The price is the same on every instance type.

Buyers also pay SageMaker AI for the instances that run their endpoint. Your inference price is the software charge, billed in addition to those infrastructure costs.

**Note**  
Inference pricing applies to real-time endpoints. The following always use hourly pricing:  
Batch transform jobs
Training jobs for algorithm products
You set the price for each type independently of the inference pricing and of each other.

#### What counts as one inference
<a name="ml-pricing-inference-unit"></a>

By default, each successful request to a buyer's real-time endpoint counts as one inference. You can define a different unit. Your model reports how many inferences each request or streaming session used, and AWS Marketplace charges for that number. Choose a unit that matches how your buyers measure the value of your model.

The following table shows example units. The prices are examples only.


**Example inference units and charges**  

| Model | One inference equals | Example price | Buyer's usage | Inferences reported | Software charge | 
| --- | --- | --- | --- | --- | --- | 
| Image classification | One image | USD $0.002 | One request with 3 images | 3 | USD $0.006 | 
| Text generation, full response | 1,000 output tokens | USD $0.004 | One response of 2,000 tokens | 2 | USD $0.008 | 
| Speech-to-text, bidirectional stream | One minute of audio | USD $0.008 | A 12-minute call | 12 | USD $0.096 | 
| Text-to-speech, bidirectional stream | 1,000 characters | USD $0.015 | 3,000 characters synthesized | 3 | USD $0.045 | 

Counts can include decimals. For example, a text model priced per 1,000 tokens can report 2.5 for a response of 2,500 tokens. Describe how you count in your product description so buyers can predict their charges.

#### Choosing a price your unit supports
<a name="ml-pricing-inference-price"></a>

Prices can have up to three decimal places, so the lowest price per inference is USD $0.001. If your natural unit is too small for that, count a larger one. For example, a speech model can't charge USD $0.00013 per second, because that price has too many decimal places. It could charge USD $0.008 per minute instead.

Buyers see your price as a price per request on the product detail page. In your product description, say what one request means, for example "one request equals one minute of audio."

#### How your model reports inferences
<a name="ml-pricing-inference-reporting"></a>

What your model sends depends on how the buyer calls the endpoint.


**How usage is reported for each way of calling an endpoint**  

| How the buyer calls the endpoint | Charged without a report | How your model reports a count | 
| --- | --- | --- | 
| Real-time request (`InvokeEndpoint`) | One inference per successful request | `X-Amzn-Inference-Metering` response header | 
| Streaming response (`InvokeEndpointWithResponseStream`) | Nothing | The same header, sent before the response body | 
| Bidirectional stream (`InvokeEndpointWithBidirectionalStream`) | Nothing | Metering records on a companion metadata connection | 

For details and code examples, see [Reporting usage for inference pricing](ml-inference-metering.md).

#### Choosing inference pricing when you create the listing
<a name="ml-pricing-inference-choose"></a>

You choose the pricing model when you create your product. After you publish, you can't switch it between hourly and inference pricing. To change pricing models, create a new product.

In a private offer, you can give a buyer a lower price per inference, or a fixed fee for unlimited use during the contract. For more information, see [Private offers for ML products](private-offers-supported-product-types.md#ml-private-offers).

### Free trial
<a name="ml-pricing-free-trial"></a>

Optionally, you can create a free trial for your product and define the number of days of the free trial. When you set up a free trial in the AWS Marketplace Management Portal, it can last 5 to 31 days. With the AWS Marketplace Catalog API, it can last 5 to 120 days. During the free trial, buyers can run your software as much as they want and aren't charged for your software. Buyers are charged for the infrastructure costs during the free trial. After the trial ends, they are charged your normal software price, along with the infrastructure costs.

When buyers subscribe to a product with a free trial, they receive a welcome email message. The message includes the term of the free trial, a calculated expiration date, and details on unsubscribing. A reminder email message is sent three days before the expiration date.

If you offer a free trial for your product in AWS Marketplace, you agree to the specific [refund policy](https://docs.aws.amazon.com/marketplace/latest/userguide/refunds.html#refund-policy) for free trials. 

**Note**  
For information on Private offers for machine learning, see [Private offers](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-overview.html).