

# EUCSUS06-BP01 Stop image builders and app block builders when not in use
<a name="eucsus06-bp01"></a>

 In WorkSpaces Applications, image builders and app block builders are two instances used only when creating your baseline image or application package. There is no requirement to keep them running. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-100"></a>

 The [Cost Optimizer for Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/cost-optimizer-for-amazon-appstream-2-0-on-the-solutionist/) monitors your WorkSpaces Applications image builders, notifying you and halting them when they are active for longer than specified thresholds. 