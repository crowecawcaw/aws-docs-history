

# Supported Frameworks, AWS Regions, Instance Types, and Tested Models
<a name="training-compiler-support"></a>

**Important**  
Amazon Web Services (AWS) announces that there will be no new releases or versions of SageMaker Training Compiler. You can continue to utilize SageMaker Training Compiler through the existing AWS Deep Learning Containers (DLCs) for SageMaker Training. It is important to note that while the existing DLCs remain accessible, they will no longer receive patches or updates from AWS, in accordance with the [AWS Deep Learning Containers Framework Support Policy](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/support-policy.html).

Before using SageMaker Training Compiler, check if your framework of choice is supported, the instance types are available in your AWS account, and your AWS account is in one of the supported AWS Regions.

**Note**  
SageMaker Training Compiler is available in the SageMaker Python SDK v2.70.0 or later.

## Supported Frameworks
<a name="training-compiler-supported-frameworks"></a>

SageMaker Training Compiler supports the following deep learning frameworks and is available through AWS Deep Learning Containers.

**Topics**
+ [PyTorch](#training-compiler-supported-frameworks-pytorch)
+ [TensorFlow](#training-compiler-supported-frameworks-tensorflow)

### PyTorch
<a name="training-compiler-supported-frameworks-pytorch"></a>



- **PyTorch**
  - **Framework version:** PyTorch v1.13.1 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/pytorch-trcomp-training:1.12.0-gpu-py38-cu113-ubuntu20.04-sagemaker / **Extendable for Docker customization:** No
  - **Framework version:** PyTorch v1.12.0 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/pytorch-trcomp-training:1.13.1-gpu-py39-cu117-ubuntu20.04-sagemaker / **Extendable for Docker customization:** No

- **PyTorch with Hugging Face Transformers**
  - **Framework version:** Transformers v4.21.1<br />PyTorch v1.11.0 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/huggingface-pytorch-trcomp-training:1.11.0-transformers4.21.1-gpu-py38-cu113-ubuntu20.04 / **Extendable for Docker customization:** No
  - **Framework version:** Transformers v4.17.0<br />PyTorch v1.10.2 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/huggingface-pytorch-trcomp-training:1.10.2-transformers4.17.0-gpu-py38-cu113-ubuntu20.04 / **Extendable for Docker customization:** No
  - **Framework version:** Transformers v4.11.0<br />PyTorch v1.9.0 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/huggingface-pytorch-training-comp:1.9.0-transformers4.11.0-gpu-py38-cu111-ubuntu20.04 / **Extendable for Docker customization:** No



### TensorFlow
<a name="training-compiler-supported-frameworks-tensorflow"></a>



- **TensorFlow**
  - **Framework version:** TensorFlow v2.11.0 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/tensorflow-training:2.11.0-gpu-py39-cu112-ubuntu20.04-sagemaker / **Extendable for Docker customization:** Yes
  - **Framework version:** TensorFlow v2.10.0 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/tensorflow-training:2.10.0-gpu-py39-cu112-ubuntu20.04-sagemaker / **Extendable for Docker customization:** Yes
  - **Framework version:** TensorFlow v2.9.1 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/tensorflow-training:2.9.1-gpu-py39-cu112-ubuntu20.04-sagemaker / **Extendable for Docker customization:** Yes

- **TensorFlow with Hugging Face Transformers**
  - **Framework version:** Transformers v4.17.0<br />TensorFlow v2.6.3 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/huggingface-tensorflow-trcomp-training:2.6.3-transformers4.17.0-gpu-py38-cu112-ubuntu20.04 / **Extendable for Docker customization:** No
  - **Framework version:** Transformers v4.11.0<br />TensorFlow v2.5.1 / **Deep Learning Container URI:** 763104351884.dkr.ecr.{{<region>}}.amazonaws.com/huggingface-tensorflow-training-comp:2.5.1-transformers4.11.0-gpu-py37-cu112-ubuntu18.04 / **Extendable for Docker customization:** No



For more information, see [Available Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md) in the *AWS Deep Learning Containers GitHub repository*.

## AWS Regions
<a name="training-compiler-availablity-zone"></a>

The [SageMaker Training Compiler Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-training-compiler-containers) are available in the AWS Regions where [AWS Deep Learning Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md) are in service except the China regions.

## Supported Instance Types
<a name="training-compiler-supported-instance-types"></a>

SageMaker Training Compiler is tested on and supports the following ML instance types.
+ P4 instances
+ P3 instances
+ G4dn instances
+ G5 instances

For specs of the instance types, see the **Accelerated Computing** section in the [Amazon EC2 Instance Types page](https://aws.amazon.com/ec2/instance-types/). For information about instance pricing, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/).

If you encountered an error message similar to the following, follow the instructions at [Request a service quota increase for SageMaker AI resources](https://docs.aws.amazon.com/sagemaker/latest/dg/regions-quotas.html#service-limit-increase-request-procedure).

```
ResourceLimitExceeded: An error occurred (ResourceLimitExceeded) when calling
the CreateTrainingJob operation: The account-level service limit 'ml.p3dn.24xlarge
for training job usage' is 0 Instances, with current utilization of 0 Instances
and a request delta of 1 Instances.
Please contact AWS support to request an increase for this limit.
```

## Tested Models
<a name="training-compiler-tested-models"></a>

The following table includes a list of the models that have been tested with SageMaker Training Compiler. For reference, the largest batch size that is able to fit into memory is also included alongside other training parameters. SageMaker Training Compiler can change the memory footprint of the model training process; as a result, a larger batch size can often be used during the training process, further decreasing total training time. In some cases, SageMaker Training Compiler intelligently promotes caching which leads to a decrease in the largest batch size that can fit on the GPU. You must retune your model hyperparameters and find an optimal batch size for your case. To save time, use the following reference tables to look up a batch size that can be a good starting point for your use case.

**Note**  
The batch sizes are local batch size that fit into each individual GPU in the respective instance type. You should also adjust the learning rate when changing the batch size.

### PyTorch 1.13.1
<a name="training-compiler-tested-models-pt1131"></a>

**Natural language processing (NLP) models**

The following models are tested for training jobs for all combinations of single-node and multi-node with single or multi GPU cores and Automatic Mixed Precision (AMP) as indicated.


<table>
<thead>
  <tr><th colspan="7">Single-node/multi-node single-GPU/multi-GPU</th></tr>
  <tr><th>Model</th><th>Dataset</th><th>Instance type</th><th>Precision</th><th>Sequence Length</th><th>Batch size for native frameworks </th><th>Batch size for SageMaker Training Compiler </th></tr>
</thead>
<tbody>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>128</td><td>80</td><td>192</td></tr>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>128</td><td>332</td></tr>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>128</td><td>80</td><td>224</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>160</td><td>288</td></tr>
  <tr><td>camembert-base</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>160</td><td>280</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>240</td><td>472</td></tr>
  <tr><td>distilgpt2</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>128</td><td>77</td><td>128</td></tr>
  <tr><td>distilgpt2</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>138</td><td>390</td></tr>
  <tr><td>distilgpt2</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>128</td><td>96</td><td>256</td></tr>
  <tr><td>distilroberta-base</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>128</td><td>96</td><td>192</td></tr>
  <tr><td>distilroberta-base</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>171</td><td>380</td></tr>
  <tr><td>distilroberta-base</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>128</td><td>112</td><td>256</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>128</td><td>52</td><td>152</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>84</td><td>240</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>128</td><td>58</td><td>164</td></tr>
  <tr><td>microsoft/deberta-base</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>128</td><td>48</td><td>128</td></tr>
  <tr><td>microsoft/deberta-base</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>84</td><td>207</td></tr>
  <tr><td>microsoft/deberta-base</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>128</td><td>53</td><td>133</td></tr>
  <tr><td>roberta-base</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>125</td><td>224</td></tr>
  <tr><td>xlm-roberta-base</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>128</td><td>16</td><td>31</td></tr>
  <tr><td>xlm-roberta-base</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>128</td><td>18</td><td>50</td></tr>
  <tr><td>xlnet-base-cased</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>128</td><td>240</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-103-v1</td><td>g5.48xlarge</td><td>float16</td><td>512</td><td>29</td><td>50</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-103-v1</td><td>g5.48xlarge</td><td>float16</td><td>512</td><td>45</td><td>64</td></tr>
  <tr><td>gpt2</td><td>wikitext-103-v1</td><td>g5.48xlarge</td><td>float16</td><td>512</td><td>18</td><td>45</td></tr>
  <tr><td>roberta-base</td><td>wikitext-103-v1</td><td>g5.48xlarge</td><td>float16</td><td>512</td><td>23</td><td>44</td></tr>
  <tr><td>gpt2</td><td>wikitext-103-v1</td><td>p4d.24xlarge</td><td>float16</td><td>512</td><td>36</td><td>64</td></tr>
</tbody>
</table>


**Computer Vision (CV) models**

Tested using [TensorFlow Model Garden](https://github.com/tensorflow/models) with Automatic Mixed Precision (AMP) as indicated.


<table>
<thead>
  <tr><th colspan="6">Single/multi-node single/multi-GPU</th></tr>
  <tr><th>Model</th><th>Dataset</th><th>Instance type</th><th>Precision</th><th>Batch size for native frameworks </th><th>Batch size for SageMaker Training Compiler </th></tr>
</thead>
<tbody>
  <tr><td>ResNet152</td><td>food101</td><td>g4dn.16xlarge</td><td>float16</td><td>128</td><td>144</td></tr>
  <tr><td>ResNet152</td><td>food101</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>192</td></tr>
  <tr><td>ResNet152</td><td>food101</td><td>p3.2xlarge</td><td>float16</td><td>152</td><td>156</td></tr>
  <tr><td>ViT</td><td>food101</td><td>g4dn.16xlarge</td><td>float16</td><td>512</td><td>512</td></tr>
  <tr><td>ViT</td><td>food101</td><td>g5.4xlarge</td><td>float16</td><td>992</td><td>768</td></tr>
  <tr><td>ViT</td><td>food101</td><td>p3.2xlarge</td><td>float16</td><td>848</td><td>768</td></tr>
</tbody>
</table>


### PyTorch 1.12.0
<a name="training-compiler-tested-models-pt1120"></a>

**Natural language processing (NLP) models**

The following models are tested for training jobs for all combinations of single-node and multi-node with single or multi GPU cores and Automatic Mixed Precision (AMP) as indicated.


<table>
<thead>
  <tr><th colspan="7">Single-node/multi-node single-GPU/multi-GPU</th></tr>
  <tr><th>Model</th><th>Dataset</th><th>Instance type</th><th>Precision</th><th>Sequence Length</th><th>Batch size for native frameworks </th><th>Batch size for SageMaker Training Compiler </th></tr>
</thead>
<tbody>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>128</td><td>248</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>160</td><td>288</td></tr>
  <tr><td>camembert-base</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>160</td><td>279</td></tr>
  <tr><td>camembert-base</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>128</td><td>105</td><td>164</td></tr>
  <tr><td>distilgpt2</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>136</td><td>256</td></tr>
  <tr><td>distilgpt2</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>128</td><td>80</td><td>118</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>84</td><td>240</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>128</td><td>80</td><td>119</td></tr>
  <tr><td>microsoft/deberta-base</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>93</td><td>197</td></tr>
  <tr><td>microsoft/deberta-base</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>128</td><td>113</td><td>130</td></tr>
  <tr><td>roberta-base</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>125</td><td>224</td></tr>
  <tr><td>roberta-base</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>128</td><td>78</td><td>112</td></tr>
  <tr><td>xlnet-base-cased</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>138</td><td>240</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-103-v1</td><td>ml.p4d.24xlarge</td><td>float16</td><td>512</td><td></td><td>52</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-103-v1</td><td>ml.p4d.24xlarge</td><td>float16</td><td>512</td><td></td><td>160</td></tr>
  <tr><td>gpt2</td><td>wikitext-103-v1</td><td>ml.p4d.24xlarge</td><td>float16</td><td>512</td><td></td><td>25</td></tr>
  <tr><td>roberta-base</td><td>wikitext-103-v1</td><td>ml.p4d.24xlarge</td><td>float16</td><td>512</td><td></td><td>64</td></tr>
</tbody>
</table>


### TensorFlow 2.11.0
<a name="training-compiler-tested-models-tf2110"></a>

**Computer Vision (CV) models**

Tested using [TensorFlow Model Garden](https://github.com/tensorflow/models) with Automatic Mixed Precision (AMP) as indicated.


<table>
<thead>
  <tr><th colspan="6">Single/multi-node single/multi-GPU</th></tr>
  <tr><th>Model</th><th>Dataset</th><th>Instance type</th><th>Precision</th><th>Batch size for native frameworks </th><th>Batch size for SageMaker Training Compiler </th></tr>
</thead>
<tbody>
  <tr><td>MaskRCNN-ResNet50-FPN</td><td>COCO-2017</td><td>ml.g5.2xlarge</td><td>float16</td><td>6</td><td>8</td></tr>
  <tr><td>MaskRCNN-ResNet50-FPN</td><td>COCO-2017</td><td>ml.p3.2xlarge</td><td>float16</td><td>4</td><td>6</td></tr>
  <tr><td>ResNet50</td><td>ImageNet</td><td>ml.g5.2xlarge</td><td>float16</td><td>192</td><td>256</td></tr>
  <tr><td>ResNet50</td><td>ImageNet</td><td>ml.p3.2xlarge</td><td>float16</td><td>256</td><td>256</td></tr>
  <tr><td>ResNet101</td><td>ImageNet</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>256</td></tr>
  <tr><td>ResNet101</td><td>ImageNet</td><td>ml.p3.2xlarge</td><td>float16</td><td>128</td><td>128</td></tr>
  <tr><td>ResNet152</td><td>ImageNet</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>224</td></tr>
  <tr><td>ResNet152</td><td>ImageNet</td><td>ml.p3.2xlarge</td><td>float16</td><td>128</td><td>128</td></tr>
  <tr><td>VisionTransformer</td><td>ImageNet</td><td>ml.g5.2xlarge</td><td>float16</td><td>112</td><td>144</td></tr>
  <tr><td>VisionTransformer</td><td>ImageNet</td><td>ml.p3.2xlarge</td><td>float16</td><td>96</td><td>128</td></tr>
</tbody>
</table>


**Natural Language Processing (NLP) models**

Tested using [Transformer models](https://github.com/huggingface/transformers) with `Sequence_Len=128` and Automatic Mixed Precision (AMP) as indicated.


<table>
<thead>
  <tr><th colspan="6">Single/multi-node single/multi-GPU</th></tr>
  <tr><th>Model</th><th>Dataset</th><th>Instance type</th><th>Precision</th><th>Batch size for native frameworks </th><th>Batch size for SageMaker Training Compiler </th></tr>
</thead>
<tbody>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>160</td><td>197</td></tr>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>95</td><td>127</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>160</td><td>128</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>104</td><td>111</td></tr>
  <tr><td>bert-large-uncased</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>65</td><td>48</td></tr>
  <tr><td>bert-large-uncased</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>40</td><td>35</td></tr>
  <tr><td>camembert-base</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>162</td></tr>
  <tr><td>camembert-base</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>105</td><td>111</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>256</td><td>264</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>128</td><td>169</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>120</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>80</td><td>83</td></tr>
  <tr><td>jplu/tf-xlm-roberta-base</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>32</td><td>32</td></tr>
  <tr><td>jplu/tf-xlm-roberta-base</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>32</td><td>36</td></tr>
  <tr><td>microsoft/mpnet-base</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>144</td><td>160</td></tr>
  <tr><td>microsoft/mpnet-base</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>106</td><td>110</td></tr>
  <tr><td>roberta-base</td><td>wikitext-2-raw-v1</td><td>ml.g5.2xlarge</td><td>float16</td><td>128</td><td>128</td></tr>
  <tr><td>roberta-base</td><td>wikitext-2-raw-v1</td><td>ml.p3.2xlarge</td><td>float16</td><td>72</td><td>98</td></tr>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>ml.g5.48xlarge</td><td>float16</td><td>128</td><td>192</td></tr>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>ml.p3.16xlarge</td><td>float16</td><td>95</td><td>96</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-2-raw-v1</td><td>ml.g5.48xlarge</td><td>float16</td><td>256</td><td>256</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-2-raw-v1</td><td>ml.p3.16xlarge</td><td>float16</td><td>140</td><td>184</td></tr>
  <tr><td>google/electra-small-discriminator</td><td>wikitext-2-raw-v1</td><td>ml.g5.48xlarge</td><td>float16</td><td>256</td><td>384</td></tr>
  <tr><td>google/electra-small-discriminator</td><td>wikitext-2-raw-v1</td><td>ml.p3.16xlarge</td><td>float16</td><td>256</td><td>268</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>ml.g5.48xlarge</td><td>float16</td><td>116</td><td>116</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>ml.p3.16xlarge</td><td>float16</td><td>85</td><td>83</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>ml.p4d.24xlarge</td><td>float16</td><td>94</td><td>110</td></tr>
  <tr><td>microsoft/mpnet-base</td><td>wikitext-2-raw-v1</td><td>ml.g5.48xlarge</td><td>float16</td><td>187</td><td>164</td></tr>
  <tr><td>microsoft/mpnet-base</td><td>wikitext-2-raw-v1</td><td>ml.p3.16xlarge</td><td>float16</td><td>106</td><td>111</td></tr>
</tbody>
</table>


### TensorFlow 2.10.0
<a name="training-compiler-tested-models-tf2100"></a>

**Computer Vision (CV) models**

Tested using [TensorFlow Model Garden](https://github.com/tensorflow/models) with Automatic Mixed Precision (AMP) as indicated.


<table>
<thead>
  <tr><th colspan="6">Single-node single-GPU/multi-GPU</th></tr>
  <tr><th>Model</th><th>Dataset</th><th>Instance type</th><th>Precision</th><th>Batch size for native frameworks </th><th>Batch size for SageMaker Training Compiler </th></tr>
</thead>
<tbody>
  <tr><td>DetectionTransformer-ResNet50</td><td>COCO-2017</td><td>ml.g4dn.2xlarge</td><td>float32</td><td>2</td><td>4</td></tr>
  <tr><td>DetectionTransformer-ResNet50</td><td>COCO-2017</td><td>ml.g5.2xlarge</td><td>float32</td><td>3</td><td>6</td></tr>
  <tr><td>DetectionTransformer-ResNet50</td><td>COCO-2017</td><td>ml.p3.2xlarge</td><td>float32</td><td>2</td><td>4</td></tr>
  <tr><td>MaskRCNN-ResNet50-FPN</td><td>COCO-2017</td><td>ml.g4dn.2xlarge</td><td>float16</td><td>4</td><td>6</td></tr>
  <tr><td>MaskRCNN-ResNet50-FPN</td><td>COCO-2017</td><td>ml.g5.2xlarge</td><td>float16</td><td>6</td><td>8</td></tr>
  <tr><td>MaskRCNN-ResNet50-FPN</td><td>COCO-2017</td><td>ml.g5.48xlarge</td><td>float16</td><td>48</td><td>64</td></tr>
  <tr><td>MaskRCNN-ResNet50-FPN</td><td>COCO-2017</td><td>ml.p3.2xlarge</td><td>float16</td><td>4</td><td>6</td></tr>
  <tr><td>ResNet50</td><td>ImageNet</td><td>ml.g4dn.2xlarge</td><td>float16</td><td>224</td><td>256</td></tr>
  <tr><td>ResNet50</td><td>ImageNet</td><td>ml.g5.2xlarge</td><td>float16</td><td>192</td><td>160</td></tr>
  <tr><td>ResNet50</td><td>ImageNet</td><td>ml.g5.48xlarge</td><td>float16</td><td>2048</td><td>2048</td></tr>
  <tr><td>ResNet50</td><td>ImageNet</td><td>ml.p3.2xlarge</td><td>float16</td><td>224</td><td>160</td></tr>
  <tr><td>ResNet101</td><td>ImageNet</td><td>ml.g4dn.2xlarge</td><td>float16</td><td>160</td><td>128</td></tr>
  <tr><td>ResNet101</td><td>ImageNet</td><td>ml.g5.2xlarge</td><td>float16</td><td>192</td><td>256</td></tr>
  <tr><td>ResNet101</td><td>ImageNet</td><td>ml.g5.48xlarge</td><td>float16</td><td>2048</td><td>2048</td></tr>
  <tr><td>ResNet101</td><td>ImageNet</td><td>ml.p3.2xlarge</td><td>float16</td><td>160</td><td>224</td></tr>
  <tr><td>ResNet152</td><td>ImageNet</td><td>ml.g4dn.2xlarge</td><td>float16</td><td>128</td><td>128</td></tr>
  <tr><td>ResNet152</td><td>ImageNet</td><td>ml.g5.2xlarge</td><td>float16</td><td>192</td><td>224</td></tr>
  <tr><td>ResNet152</td><td>ImageNet</td><td>ml.g5.48xlarge</td><td>float16</td><td>1536</td><td>1792</td></tr>
  <tr><td>ResNet152</td><td>ImageNet</td><td>ml.p3.2xlarge</td><td>float16</td><td>128</td><td>160</td></tr>
  <tr><td>VisionTransformer</td><td>ImageNet</td><td>ml.g4dn.2xlarge</td><td>float16</td><td>80</td><td>128</td></tr>
  <tr><td>VisionTransformer</td><td>ImageNet</td><td>ml.g5.2xlarge</td><td>float16</td><td>112</td><td>144</td></tr>
  <tr><td>VisionTransformer</td><td>ImageNet</td><td>ml.g5.48xlarge</td><td>float16</td><td>896</td><td>1152</td></tr>
  <tr><td>VisionTransformer</td><td>ImageNet</td><td>ml.p3.2xlarge</td><td>float16</td><td>80</td><td>128</td></tr>
</tbody>
</table>


**Natural Language Processing (NLP) models**

Tested using [Transformer models](https://github.com/huggingface/transformers) with `Sequence_Len=128` and Automatic Mixed Precision (AMP) as indicated.


<table>
<thead>
  <tr><th colspan="6">Single-node single-GPU/multi-GPU</th></tr>
  <tr><th>Model</th><th>Dataset</th><th>Instance type</th><th>Precision</th><th>Batch size for native frameworks </th><th>Batch size for SageMaker Training Compiler </th></tr>
</thead>
<tbody>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>128</td><td>112</td></tr>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>128</td><td>128</td></tr>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>p3.8xlarge</td><td>float16</td><td>128</td><td>135</td></tr>
  <tr><td>albert-base-v2</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>191</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>64</td><td>94</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>96</td><td>101</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-2-raw-v1</td><td>p3.8xlarge</td><td>float16</td><td>96</td><td>96</td></tr>
  <tr><td>bert-base-uncased</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>128</td></tr>
  <tr><td>bert-large-uncased</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>35</td><td>21</td></tr>
  <tr><td>bert-large-uncased</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>39</td><td>26</td></tr>
  <tr><td>bert-large-uncased</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>60</td><td>50</td></tr>
  <tr><td>camembert-base</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>96</td><td>90</td></tr>
  <tr><td>camembert-base</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>96</td><td>98</td></tr>
  <tr><td>camembert-base</td><td>wikitext-2-raw-v1</td><td>p3.8xlarge</td><td>float16</td><td>96</td><td>96</td></tr>
  <tr><td>camembert-base</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>128</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>256</td><td>160</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>128</td><td>176</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-2-raw-v1</td><td>p3.8xlarge</td><td>float16</td><td>128</td><td>160</td></tr>
  <tr><td>distilbert-base-uncased</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>256</td><td>258</td></tr>
  <tr><td>google_electra-small-discriminator</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>256</td><td>216</td></tr>
  <tr><td>google_electra-small-discriminator</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>256</td><td>230</td></tr>
  <tr><td>google_electra-small-discriminator</td><td>wikitext-2-raw-v1</td><td>p3.8xlarge</td><td>float16</td><td>256</td><td>224</td></tr>
  <tr><td>google_electra-small-discriminator</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>256</td><td>320</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>80</td><td>64</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>80</td><td>77</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>p3.8xlarge</td><td>float16</td><td>80</td><td>72</td></tr>
  <tr><td>gpt2</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>120</td></tr>
  <tr><td>jplu_tf-xlm-roberta-base</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>28</td><td>24</td></tr>
  <tr><td>jplu_tf-xlm-roberta-base</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>32</td><td>24</td></tr>
  <tr><td>jplu_tf-xlm-roberta-base</td><td>wikitext-2-raw-v1</td><td>p3.8xlarge</td><td>float16</td><td>32</td><td>26</td></tr>
  <tr><td>jplu_tf-xlm-roberta-base</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>66</td><td>52</td></tr>
  <tr><td>microsoft_mpnet-base</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>96</td><td>92</td></tr>
  <tr><td>microsoft_mpnet-base</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>96</td><td>101</td></tr>
  <tr><td>microsoft_mpnet-base</td><td>wikitext-2-raw-v1</td><td>p3.8xlarge</td><td>float16</td><td>96</td><td>101</td></tr>
  <tr><td>microsoft_mpnet-base</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>152</td></tr>
  <tr><td>roberta-base</td><td>wikitext-2-raw-v1</td><td>g4dn.16xlarge</td><td>float16</td><td>64</td><td>72</td></tr>
  <tr><td>roberta-base</td><td>wikitext-2-raw-v1</td><td>p3.2xlarge</td><td>float16</td><td>64</td><td>84</td></tr>
  <tr><td>roberta-base</td><td>wikitext-2-raw-v1</td><td>p3.8xlarge</td><td>float16</td><td>64</td><td>86</td></tr>
  <tr><td>roberta-base</td><td>wikitext-2-raw-v1</td><td>g5.4xlarge</td><td>float16</td><td>128</td><td>128</td></tr>
</tbody>
</table>


### TensorFlow 2.9.1
<a name="training-compiler-tested-models-tf291"></a>

Tested using [TensorFlow Model Garden](https://github.com/tensorflow/models) with Automatic Mixed Precision (AMP).


<table>
<thead>
  <tr><th colspan="5">Single-node single-GPU/multi-GPU</th></tr>
  <tr><th>Model</th><th>Dataset</th><th>Instance type</th><th>Batch size for native frameworks </th><th>Batch size for SageMaker Training Compiler </th></tr>
</thead>
<tbody>
  <tr><td>ResNet50</td><td>ImageNet</td><td>ml.g4dn.2xlarge</td><td>192</td><td>256*</td></tr>
  <tr><td rowspan="3">ResNet101</td><td rowspan="3">ImageNet</td><td>ml.g4dn.2xlarge</td><td>128</td><td>160</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>224</td><td>256*</td></tr>
  <tr><td>ml.p3.16xlarge</td><td>1536</td><td>1792</td></tr>
  <tr><td rowspan="3">ResNet152</td><td rowspan="3">ImageNet</td><td>ml.g5.2xlarge</td><td>192</td><td>224</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>160</td><td>160</td></tr>
  <tr><td>ml.p3.16xlarge</td><td>1024</td><td>1280</td></tr>
  <tr><td rowspan="4">VisionTransformer</td><td rowspan="4">ImageNet</td><td>ml.g4dn.2xlarge</td><td>80</td><td>128*</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>112</td><td>128*</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>56</td><td>128*</td></tr>
  <tr><td>ml.p3.16xlarge</td><td>640</td><td>1024*</td></tr>
  <tr><td rowspan="4">DetectionTransformer-ResNet50</td><td rowspan="4">COCO-2017</td><td>ml.g4dn.2xlarge</td><td>2</td><td>2</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>3</td><td>6</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>2</td><td>4</td></tr>
  <tr><td>ml.p3.16xlarge</td><td>8</td><td>32</td></tr>
  <tr><td rowspan="3">MaskRCNN-ResNet50-FPN</td><td rowspan="3">COCO-2017</td><td>ml.g4dn.2xlarge</td><td>4</td><td>4</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>6</td><td>8</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>4</td><td>6</td></tr>
</tbody>
</table>


\* The batch sizes marked with the asterisk symbol (\*) indicate the largest batch size tested by the SageMaker Training Compiler developer team. For the marked cells, the instance may be able to fit a larger batch size than what is indicated.

### Transformers 4.21.1 with PyTorch 1.11.0
<a name="training-compiler-tested-models-hf421-pt111"></a>

Tested with `Sequence_Len=512` and Automatic Mixed Precision (AMP).


<table>
<thead>
  <tr><th colspan="6">Single-node single-GPU</th></tr>
  <tr><th>Model </th><th>Dataset</th><th>Instance type</th><th>Instance count</th><th>Batch size for native frameworks</th><th>Batch size for Training Compiler</th></tr>
</thead>
<tbody>
  <tr><td rowspan="3">albert-base-v2</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>14</td><td>28</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>18</td><td>40</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>14</td><td>32</td></tr>
  <tr><td rowspan="3">bert-base-cased</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>12</td><td>24</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>28</td><td>44</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>16</td><td>20</td></tr>
  <tr><td rowspan="3">camembert-base</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>16</td><td>28</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>24</td><td>40</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>16</td><td>24</td></tr>
  <tr><td rowspan="4">distilbert-base-uncased</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>28</td><td>52</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>40</td><td>76</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>32</td><td>48</td></tr>
  <tr><td>wikitext-103-v1</td><td>ml.p4d.24xlarge</td><td>4</td><td>82</td><td>160</td></tr>
  <tr><td rowspan="3">distilgpt2</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>6</td><td>18</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>12</td><td>28</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>6</td><td>16</td></tr>
  <tr><td rowspan="3">distilroberta-base</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>20</td><td>40</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>28</td><td>56</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>24</td><td>40</td></tr>
  <tr><td rowspan="3">EleutherAI/gpt-neo-125M</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>4</td><td>8</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>6</td><td>14</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>4</td><td>10</td></tr>
  <tr><td rowspan="4">gpt2</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>4</td><td>8</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>6</td><td>16</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>4</td><td>10</td></tr>
  <tr><td>wikitext-103-v1</td><td>ml.p4d.24xlarge</td><td>4</td><td>13</td><td>25</td></tr>
  <tr><td rowspan="4">roberta-base</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>12</td><td>20</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>24</td><td>36</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>12</td><td>20</td></tr>
  <tr><td>wikitext-103-v1</td><td>ml.p4d.24xlarge</td><td>4</td><td>36</td><td>64</td></tr>
  <tr><td rowspan="3">xlnet-base-cased</td><td rowspan="3">wikitext-2</td><td>ml.g4dn.2xlarge</td><td>1</td><td>2</td><td>6</td></tr>
  <tr><td>ml.g5.2xlarge</td><td>1</td><td>2</td><td>10</td></tr>
  <tr><td>ml.p3.2xlarge</td><td>1</td><td>2</td><td>8</td></tr>
  <tr><td rowspan="4">bert-base-uncased</td><td rowspan="4">wikitext-103-v1</td><td rowspan="4">ml.p4d.24xlarge</td><td>2</td><td>32</td><td>64</td></tr>
  <tr><td>4</td><td>32</td><td>64</td></tr>
  <tr><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>16</td><td>32</td><td>64</td></tr>
  <tr><td>roberta-large</td><td>wikitext-103-v1</td><td>ml.p4d.24xlarge</td><td>4</td><td>16</td><td>24</td></tr>
  <tr><td>microsoft/deberta-v3-base</td><td>wikitext-103-v1</td><td>ml.p4d.24xlarge</td><td>16</td><td>9</td><td>23</td></tr>
</tbody>
</table>


### Transformers 4.17.0 with PyTorch 1.10.2
<a name="training-compiler-tested-models-hf417-pt110"></a>

Tested with `Sequence_Len=512` and Automatic Mixed Precision (AMP).


<table>
<thead>
  <tr><th colspan="4">Single-node single-GPU</th></tr>
  <tr><th>Model </th><th>Instance type</th><th>Batch size for native frameworks</th><th>Batch size for Training Compiler</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">albert-base-v2</td><td>ml.p3.2xlarge</td><td>14</td><td>28</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>14</td><td>24</td></tr>
  <tr><td rowspan="2">bert-base-cased</td><td>ml.p3.2xlarge</td><td>16</td><td>24</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>12</td><td>24</td></tr>
  <tr><td rowspan="2">bert-base-uncased</td><td>ml.p3.2xlarge</td><td>16</td><td>24</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>12</td><td>28</td></tr>
  <tr><td rowspan="2">camembert-base</td><td>ml.p3.2xlarge</td><td>12</td><td>24</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>12</td><td>28</td></tr>
  <tr><td rowspan="2">distilbert-base-uncased</td><td>ml.p3.2xlarge</td><td>28</td><td>48</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>24</td><td>52</td></tr>
  <tr><td rowspan="2">distilgpt2</td><td>ml.p3.2xlarge</td><td>6</td><td>12</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>6</td><td>14</td></tr>
  <tr><td rowspan="2">distilroberta-base</td><td>ml.p3.2xlarge</td><td>20</td><td>40</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>12</td><td>40</td></tr>
  <tr><td rowspan="2">EleutherAI/gpt-neo-125M</td><td>ml.p3.2xlarge</td><td>2</td><td>10</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>2</td><td>8</td></tr>
  <tr><td rowspan="2">facebook/bart-base</td><td>ml.p3.2xlarge</td><td>2</td><td>6</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>2</td><td>6</td></tr>
  <tr><td rowspan="2">gpt2</td><td>ml.p3.2xlarge</td><td>4</td><td>8</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>2</td><td>8</td></tr>
  <tr><td rowspan="2">roberta-base</td><td>ml.p3.2xlarge</td><td>12</td><td>20</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>12</td><td>20</td></tr>
  <tr><td rowspan="2">xlnet-base-cased</td><td>ml.p3.2xlarge</td><td>2</td><td>8</td></tr>
  <tr><td>ml.g4dn.2xlarge</td><td>4</td><td>6</td></tr>
</tbody>
</table>


### Transformers 4.11.0 with PyTorch 1.9.0
<a name="training-compiler-tested-models-hf411-pt190"></a>

Tested with `Sequence_Len=512` and Automatic Mixed Precision (AMP).


<table>
<thead>
  <tr><th colspan="4">Single-node single-GPU</th></tr>
  <tr><th>Model </th><th>Instance type</th><th>Batch size for native</th><th>Batch size for Training Compiler</th></tr>
</thead>
<tbody>
  <tr><td>albert-base-v2 </td><td>ml.p3.2xlarge</td><td>12</td><td>32</td></tr>
  <tr><td>bert-base-cased </td><td>ml.p3.2xlarge</td><td>14</td><td>24</td></tr>
  <tr><td>bert-base-chinese</td><td>ml.p3.2xlarge</td><td>16</td><td>24</td></tr>
  <tr><td>bert-base-multilingual-cased </td><td>ml.p3.2xlarge</td><td>4</td><td>16</td></tr>
  <tr><td>bert-base-multilingual-uncased </td><td>ml.p3.2xlarge</td><td>8</td><td>16</td></tr>
  <tr><td>bert-base-uncased </td><td>ml.p3.2xlarge</td><td>12</td><td>24</td></tr>
  <tr><td>cl-tohoku/bert-base-japanese-whole-word-masking</td><td>ml.p3.2xlarge</td><td>12</td><td>24</td></tr>
  <tr><td>cl-tohoku/bert-base-japanese </td><td>ml.p3.2xlarge</td><td>12</td><td>24</td></tr>
  <tr><td>distilbert-base-uncased </td><td>ml.p3.2xlarge</td><td>28</td><td>32</td></tr>
  <tr><td>distilbert-base-uncased-finetuned-sst-2-english</td><td>ml.p3.2xlarge</td><td>28</td><td>32</td></tr>
  <tr><td>distilgpt2 </td><td>ml.p3.2xlarge</td><td>16</td><td>32</td></tr>
  <tr><td>facebook/bart-base </td><td>ml.p3.2xlarge</td><td>4</td><td>8</td></tr>
  <tr><td>gpt2</td><td>ml.p3.2xlarge</td><td>6</td><td>20</td></tr>
  <tr><td>nreimers/MiniLMv2-L6-H384-distilled-from-RoBERTa-Large </td><td>ml.p3.2xlarge</td><td>20</td><td>32</td></tr>
  <tr><td>roberta-base </td><td>ml.p3.2xlarge</td><td>12</td><td>20</td></tr>
</tbody>
</table>



<table>
<thead>
  <tr><th colspan="4">Single-node multi-GPU</th></tr>
  <tr><th>Model </th><th>Instance type</th><th>Batch size for native</th><th>Batch size for Training Compiler</th></tr>
</thead>
<tbody>
  <tr><td>bert-base-chinese </td><td>ml.p3.8xlarge</td><td>16</td><td>26</td></tr>
  <tr><td>bert-base-multilingual-cased </td><td>ml.p3.8xlarge</td><td>6</td><td>16</td></tr>
  <tr><td>bert-base-multilingual-uncased</td><td>ml.p3.8xlarge</td><td>6</td><td>16</td></tr>
  <tr><td>bert-base-uncased </td><td>ml.p3.8xlarge</td><td>14</td><td>24</td></tr>
  <tr><td>distilbert-base-uncased </td><td>ml.p3.8xlarge</td><td>14</td><td>32</td></tr>
  <tr><td>distilgpt2</td><td>ml.p3.8xlarge</td><td>6</td><td>32</td></tr>
  <tr><td>facebook/bart-base</td><td>ml.p3.8xlarge</td><td>8</td><td>16</td></tr>
  <tr><td>gpt2 </td><td>ml.p3.8xlarge</td><td>8</td><td>20</td></tr>
  <tr><td>roberta-base </td><td>ml.p3.8xlarge</td><td>12</td><td>20</td></tr>
</tbody>
</table>


### Transformers 4.17.0 with TensorFlow 2.6.3
<a name="training-compiler-tested-models-hf417-tf263"></a>

Tested with `Sequence_Len=128` and Automatic Mixed Precision (AMP).


| Model  | Instance type | Batch size for native frameworks | Batch size for Training Compiler | 
| --- | --- | --- | --- | 
| albert-base-v2 | ml.g4dn.16xlarge | 136 | 208 | 
| albert-base-v2 | ml.g5.4xlarge | 219 | 312 | 
| albert-base-v2 | ml.p3.2xlarge | 152 | 208 | 
| albert-base-v2 | ml.p3.8xlarge | 152 | 192 | 
| bert-base-uncased | ml.g4dn.16xlarge | 120 | 101 | 
| bert-base-uncased | ml.g5.4xlarge | 184 | 160 | 
| bert-base-uncased | ml.p3.2xlarge | 128 | 108 | 
| bert-large-uncased | ml.g4dn.16xlarge | 37 | 28 | 
| bert-large-uncased | ml.g5.4xlarge | 64 | 55 | 
| bert-large-uncased | ml.p3.2xlarge | 40 | 32 | 
| camembert-base | ml.g4dn.16xlarge | 96 | 100 | 
| camembert-base | ml.g5.4xlarge | 190 | 160 | 
| camembert-base | ml.p3.2xlarge | 129 | 108 | 
| camembert-base | ml.p3.8xlarge | 128 | 104 | 
| distilbert-base-uncased | ml.g4dn.16xlarge | 210 | 160 | 
| distilbert-base-uncased | ml.g5.4xlarge | 327 | 288 | 
| distilbert-base-uncased | ml.p3.2xlarge | 224 | 196 | 
| distilbert-base-uncased | ml.p3.8xlarge | 192 | 182 | 
| google\_electra-small-discriminator | ml.g4dn.16xlarge | 336 | 288 | 
| google\_electra-small-discriminator | ml.g5.4xlarge | 504 | 384 | 
| google\_electra-small-discriminator | ml.p3.2xlarge | 352 | 323 | 
| gpt2 | ml.g4dn.16xlarge | 89 | 64 | 
| gpt2 | ml.g5.4xlarge | 140 | 146 | 
| gpt2 | ml.p3.2xlarge | 94 | 96 | 
| gpt2 | ml.p3.8xlarge | 96 | 88 | 
| jplu\_tf-xlm-roberta-base | ml.g4dn.16xlarge | 52 | 16 | 
| jplu\_tf-xlm-roberta-base | ml.g5.4xlarge | 64 | 44 | 
| microsoft\_mpnet-base | ml.g4dn.16xlarge | 120 | 100 | 
| microsoft\_mpnet-base | ml.g5.4xlarge | 192 | 160 | 
| microsoft\_mpnet-base | ml.p3.2xlarge | 128 | 104 | 
| microsoft\_mpnet-base | ml.p3.8xlarge | 130 | 92 | 
| roberta-base | ml.g4dn.16xlarge | 108 | 64 | 
| roberta-base | ml.g5.4xlarge | 176 | 142 | 
| roberta-base | ml.p3.2xlarge | 118 | 100 | 
| roberta-base | ml.p3.8xlarge | 112 | 88 | 

### Transformers 4.11.0 with TensorFlow 2.5.1
<a name="training-compiler-tested-models-hf411-tf251"></a>

Tested with `Sequence_Len=128` and Automatic Mixed Precision (AMP).


<table>
<thead>
  <tr><th colspan="4">Single-node single-GPU</th></tr>
  <tr><th>Model </th><th>Instance type</th><th>Batch size for native</th><th>Batch size for Training Compiler</th></tr>
</thead>
<tbody>
  <tr><td>albert-base-v2 </td><td>ml.p3.2xlarge</td><td>128</td><td>128</td></tr>
  <tr><td>bart-base </td><td>ml.p3.2xlarge</td><td>12</td><td>64</td></tr>
  <tr><td>bart-large </td><td>ml.p3.2xlarge</td><td>4</td><td>28</td></tr>
  <tr><td>bert-base-cased </td><td>ml.p3.2xlarge</td><td>16</td><td>128</td></tr>
  <tr><td>bert-base-chinese</td><td>ml.p3.2xlarge</td><td>16</td><td>128</td></tr>
  <tr><td>bert-base-multilingual-cased </td><td>ml.p3.2xlarge</td><td>12</td><td>64</td></tr>
  <tr><td>bert-base-multilingual-uncased </td><td>ml.p3.2xlarge</td><td>16</td><td>96</td></tr>
  <tr><td>bert-base-uncased</td><td>ml.p3.2xlarge</td><td>16</td><td>96</td></tr>
  <tr><td>bert-large-uncased </td><td>ml.p3.2xlarge</td><td>4</td><td>24</td></tr>
  <tr><td>cl-tohoku/bert-base-japanese </td><td>ml.p3.2xlarge</td><td>16</td><td>128</td></tr>
  <tr><td>cl-tohoku/bert-base-japanese-whole-word-masking </td><td>ml.p3.2xlarge</td><td>16</td><td>128</td></tr>
  <tr><td>distilbert-base-sst2 </td><td>ml.p3.2xlarge</td><td>32</td><td>128</td></tr>
  <tr><td>distilbert-base-uncased </td><td>ml.p3.2xlarge</td><td>32</td><td>128</td></tr>
  <tr><td>distilgpt2</td><td>ml.p3.2xlarge</td><td>32</td><td>128</td></tr>
  <tr><td>gpt2 </td><td>ml.p3.2xlarge</td><td>12</td><td>64</td></tr>
  <tr><td>gpt2-large </td><td>ml.p3.2xlarge</td><td>2</td><td>24</td></tr>
  <tr><td>jplu/tf-xlm-roberta-base </td><td>ml.p3.2xlarge</td><td>12</td><td>32</td></tr>
  <tr><td>roberta-base </td><td>ml.p3.2xlarge</td><td>4</td><td>64</td></tr>
  <tr><td>roberta-large </td><td>ml.p3.2xlarge</td><td>4</td><td>64</td></tr>
  <tr><td>t5-base </td><td>ml.p3.2xlarge</td><td>64</td><td>64</td></tr>
  <tr><td>t5-small </td><td>ml.p3.2xlarge</td><td>128</td><td>128</td></tr>
</tbody>
</table>
