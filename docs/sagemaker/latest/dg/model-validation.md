# Validation of models in production

With SageMaker AI, you can test multiple models or model versions behind the same endpoint using variants. A variant
consists of an ML instance and the serving components specified in a SageMaker AI model. You can have multiple variants
behind an endpoint. Each variant can have a different instance type or a SageMaker AI model that can be autoscaled
independently of the others. The models within the variants can be trained using different datasets, different
algorithms, different ML frameworks, or any combination of all of these. All the variants behind an endpoint
share the same inference code. SageMaker AI supports two types of variants, production variants and shadow variants.

If you have multiple production variants behind an endpoint, then you can allocate a portion of your inference
requests to each variant. Each request is routed to only one of the production variants. The production variant
to which the request was routed provides the response to the caller. You can compare how the production variants
perform relative to each other.

You can also have a shadow variant corresponding to a production variant behind an endpoint. A portion of the
inference requests that goes to the production variant is replicated to the shadow variant. The responses of the
shadow variant are logged for comparison and not returned to the caller. This lets you test the performance of
the shadow variant without exposing the caller to the response produced by the shadow variant.

###### Topics

- [Testing models with production variants](model-ab-testing.md "model-ab-testing.md")
- [Testing models with shadow variants](model-shadow-deployment.md "model-shadow-deployment.md")
