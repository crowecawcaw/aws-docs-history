

# Card connections in Infrastructure Composer
<a name="using-composer-connecting"></a>

In AWS Infrastructure Composer, a connection between two cards is visually displayed by a line. These lines represent event-driven relationships within your application.

**Topics**
+ [Connections between cards](#using-composer-connecting-cards)
+ [Connections between enhanced component cards](#using-composer-connecting-enhanced)
+ [Connections to and from standard IaC resource cards](#using-composer-connecting-standard)

## Connections between cards
<a name="using-composer-connecting-cards"></a>

How you connect cards together varies depending on the card type. Each enhanced card has at least one connector port. To connect them, you simply select one connector port and drag it to the port of another card, and Infrastructure Composer will connect the two resources or display a message stating this configuration isn’t supported. 

![An API Gateway card connected to a Lambda function.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_use_con_01.png)


As seen above, lines between enhanced component cards are solid. Conversely, standard IaC resource cards (also referred to as standard component cards) do not have connector ports. For these cards, you must specify these event-driven relationships in your application's template, and Infrastructure Composer will automatically detect their connections and visualize them with a dotted line between your cards.

![An image of a standard component card connected to an enhanced component card.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_use_con_04.png)


To learn more, see the sections below.

## Connections between enhanced component cards
<a name="using-composer-connecting-enhanced"></a>

In Infrastructure Composer, a connection between two enhanced component cards is visually displayed by a solid line. These lines represent event-driven relationships within your application.

To connect two cards, click on a port from one card and drag it onto a port on another card.

![Selecting a port from one resource card and connecting it to another resource card on the Infrastructure Composer canvas.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_ref_08.gif)


**Note**  
Standard IaC resource cards do not have connector ports. For these cards, you must specify their event-driven relationships in your application's template, and Infrastructure Composer will automatically detect their connections and visualize them with a dotted line between your cards.

For more information, see [Connect cards on Infrastructure Composer's visual canvas](reference-navigation-gestures-connect.md).

### What enhanced component cards provision
<a name="using-composer-connecting-enhanced-provisioned"></a>

Connections between two cards, visually indicated by a line, provision the following when necessary:
+ AWS Identity and Access Management (IAM) policies
+ Environment variables
+ Events

#### IAM policies
<a name="using-composer-connecting-enhanced-provisioned-iam"></a>

When a resource needs permission to invoke another resource, Infrastructure Composer provisions resource-based policies using AWS Serverless Application Model (AWS SAM) policy templates.
+ To learn more about IAM permissions and policies, see [Overview of access management: Permissions and policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html) in the *IAM User Guide*.
+ To learn more about AWS SAM policy templates, see [AWS SAM policy templates](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-policy-templates.html) in the *AWS Serverless Application Model Developer Guide*.

#### Environment variables
<a name="using-composer-connecting-enhanced-provisioned-env"></a>

Environment variables are temporary values that can be changed to affect the behavior of your resources. When necessary, Infrastructure Composer defines the infrastructure code to utilize environment variables between resources.

#### Events
<a name="using-composer-connecting-enhanced-provisioned-events"></a>

Resources can invoke another resource through different types of events. When necessary, Infrastructure Composer defines the infrastructure code necessary for resources to interact through event types.

## Connections to and from standard IaC resource cards
<a name="using-composer-connecting-standard"></a>

All CloudFormation resources are available to use as standard IaC resource cards from the **Resources** palette. When you drag a standard IaC resource card onto the canvas, a standard IaC resource card becomes a standard component card, and this prompts Infrastructure Composer to create a starting template for your resource in your application.

For more information, see [Standard cards in Infrastructure Composer](using-composer-standard-cards.md).