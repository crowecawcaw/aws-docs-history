

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Amazon EC2 instance mutability in AMS
<a name="compute-instance-mutability-aog"></a>

You and AMS can maintain the Amazon Elastic Compute Cloud (Amazon EC2) instances in your infrastructure in one of two manners:
+ Immutable: This model uses Amazon Machine Images (AMIs) *baked* (created) with the necessary features. When deploying an update, the existing instances are torn down and completely replaced with new ones created from an updated AMI. To minimize down-time, this rolling process leaves some instances not updated and accessible while others are being updated until, eventually, the new change is completely deployed.
+ Mutable: In this model, the infrastructure is updated with new code being deployed on existing systems in the Cloud. This model is a mix of manually pushing updates and using infrastructure-as-code to deploy updates and does not rely on new AMIs.

 These maintenance models are discussed in more detail in later sections of this guide.