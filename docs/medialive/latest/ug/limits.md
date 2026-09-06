

# Quotas in MediaLive
<a name="limits"></a>

There are quotas (formerly referred to as limits) that apply to the resources and operations of AWS Elemental MediaLive. A *quota* is a resource or operation cap that you can increase. 

## Requesting a quota increase
<a name="limit-quota-request"></a>

Use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/medialive/quotas) to request an increase on any quota and to view information about your current quotas. 

## Quotas versus constraints
<a name="limit-quota-vs-constraints"></a>

MediaLive has quotas. It also has *constraints*, which are limits that you can't change. For more information about these constraints, see [MediaLive feature rules and limits](eml-limitations-and-rules.md).

**Note**  
There is a limit on the number of actions that a channel schedule can contain. This limit isn't listed here because it's not a quota that you can change. This limit is documented in [MediaLive feature rules and limits](eml-limitations-and-rules.md).

## Quotas for Elemental Inference
<a name="limit-quota-elemental-inference"></a>

There are quotas, separate from MediaLive quotas, that apply if you use the Elemental Inference features of MediaLive. These quotas are part of the AWS Elemental Inference service. For more information, see [Elemental Inference quotas](elemental-inference.md#elemental-inference-in-eml-quotas).<a name="limit-quota-defaults"></a>