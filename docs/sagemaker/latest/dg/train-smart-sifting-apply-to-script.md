# SageMaker smart sifting within your training

script

The SageMaker smart sifting library is packaged in the [SageMaker AI framework DLCs](train-smart-sifting-what-is-supported.md#train-smart-sifting-supported-frameworks "train-smart-sifting-what-is-supported.md#train-smart-sifting-supported-frameworks") as a
complementary library. It provides a filtering logic against training samples that have
relatively lower impact on model training, and your model can reach the desired model
accuracy with fewer training samples when compared to the model training with full data
samples.

To learn how to implement the smart sifting tool into your training script, choose one
of the following based on the framework you use.

###### Topics

- [Apply SageMaker smart sifting to
  your PyTorch script](train-smart-sifting-apply-to-pytorch-script.md "train-smart-sifting-apply-to-pytorch-script.md")
- [Apply SageMaker smart sifting to your Hugging Face Transformers script](train-smart-sifting-apply-to-hugging-face-transformers-script.md "train-smart-sifting-apply-to-hugging-face-transformers-script.md")
