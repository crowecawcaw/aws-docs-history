

# Understand Release, Stop and Resume, and Decline Task Options
<a name="sms-video-worker-instructions-skip-reject-ot"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

When you open the labeling task, three buttons on the top right allow you to decline the task (**Decline task**), release it (**Release task**), and stop and resume it at a later time (**Stop and resume later**). The following list describes what happens when you select one of these options:
+ **Decline task**: You should only decline a task if something is wrong with the task, such as unclear video frame images or an issue with the UI. If you decline a task, you will not be able to return to the task.
+ **Release Task**: Use this option to release a task and allow others to work on it. When you release a task, you loose all work done on that task and other workers on your team can pick it up. If enough workers pick up the task, you may not be able to return to it. When you select this button and then select **Confirm**, you are returned to the worker portal. If the task is still available, its status will be **Available**. If other workers pick it up, it will disappear from your portal. 
+ **Stop and resume later**: You can use the **Stop and resume later** button to stop working and return to the task at a later time. You should use the **Save** button to save your work before you select **Stop and resume later**. When you select this button and then select **Confirm**, you are returned to the worker portal, and the task status is **Stopped**. You can select the same task to resume work on it. 

  Be aware that the person that creates your labeling tasks specifies a time limit in which all tasks much be completed by. If you do not return to and complete this task within that time limit, it will expire and your work will not be submitted. Contact your administrator for more information. 

![Gif showing the locations of Decline task, Release task, and Stop and resume later in the UI.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/sms/video/reject-decline-task.gif)
