# Amazon EC2 instance mutability in AMS

You and AMS can maintain the Amazon Elastic Compute Cloud (Amazon EC2) instances in your infrastructure in
one of two manners:

- Immutable: This model uses Amazon Machine Images (AMIs) _baked_ (created)
  with the necessary features. When deploying an update, the existing instances
  are torn down and completely replaced with new ones created from an updated AMI.
  To minimize down-time, this rolling process leaves some instances not updated
  and accessible while others are being updated until, eventually, the new change
  is completely deployed.
- Mutable: In this model, the infrastructure is updated with new code being deployed on existing systems in the Cloud. This model is a mix of manually
  pushing updates and using infrastructure-as-code to deploy updates and does not rely on new AMIs.
  These maintenance models are discussed in more detail in later sections of this guide.
