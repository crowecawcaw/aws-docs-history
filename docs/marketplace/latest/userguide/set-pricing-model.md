

# Step 4: Configure the pricing model
<a name="set-pricing-model"></a>

 Choose how buyers pay for your software. You can't change the pricing model after you publish the product, so if you plan to charge per inference, choose it now. With per-inference pricing, your container reports the inferences, as described in [Reporting usage for inference pricing](ml-inference-metering.md). For help choosing, see [Machine learning product pricing for AWS Marketplace](machine-learning-pricing.md). 

1.  Choose a pricing model: **Free**, **Usage - hourly**, or **Usage - per inference request**. Batch transform jobs and algorithm training jobs are always free or charged hourly by instance. 
   +  If you chose to offer your product for free, choose **Next** and continue the wizard. 
   +  If you chose usage pricing, continue these steps. 

1.  If you chose **Usage - hourly**, enter a price for each instance type. You can apply one price to multiple instance types. If you chose **Usage - per inference request**, enter one price per inference for real-time inference, plus an hourly price for each batch transform and training instance type. 

1.  Select **Yes, offer a free trial** if you'd like to offer a free trial of your product. 

1. Choose **Next** to move to the next step in the wizard.