

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Training Process
<a name="training-process"></a>

 To train an ML model, you need to specify the following: 
+  Input training datasource 
+  Name of the data attribute that contains the target to be predicted 
+  Required data transformation instructions 
+  Training parameters to control the learning algorithm 

 During the training process, Amazon ML automatically selects the correct learning algorithm for you, based on the type of target that you specified in the training datasource. 