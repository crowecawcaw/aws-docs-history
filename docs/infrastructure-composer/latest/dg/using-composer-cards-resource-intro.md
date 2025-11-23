# Standard component cards in Infrastructure Composer

Before a standard component card is placed on Infrastructure Composer's visual canvas, it is listed as a **Standard (IaC) resource** card on the **Resources** palette in Infrastructure Composer.
A standard (IaC) resource card represents a single CloudFormation resource. Each standard IaC resource card, once placed on the visual canvas, becomes a card labeled **Standard component**,
and may be combined to represent multiple CloudFormation resources.

![Standard IaC resource cards in the Resources palette.](images/aac_cards_12.png)
Each standard IaC resource card can be identified by its CloudFormation resource type. The following is an example of a standard IaC resource card that represents an
`AWS::ECS::Cluster` CloudFormation resource type:

![A standard IaC resource cluster card.](images/aac_cards_08.png)
Each standard component card visualizes the CloudFormation resources that it contains. The following is an example of a standard
component card that includes two standard IaC resources:

![A DemoLambdaFunction standard component card that includes two standard IaC resource cards.](images/aac_cards_13.png)
As you configure the properties of your standard component cards, Infrastructure Composer may combine related cards together. For example, here are two standard component cards:

![Two standard component cards. One is an AWS::Lambda::Function card and the other is an AWS::IAM::Role card.](images/aac_cards_14.png)
In the **Resource properties** panel of the standard component card representing an `AWS::Lambda::Function` resource,
we reference the AWS Identity and Access Management (IAM) role by its logical ID:

![The Resource properties panel for the AWS::Lambda::Function standard component card.](images/aac_cards_15.png)
After saving our template, the two standard component cards combine into a single standard component card.

![A standard component card that includes two CloudFormation resources.](images/aac_cards_16.png)
