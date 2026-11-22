

# Integrating AWS Marketplace with procurement systems

Most large organizations don't let employees buy software directly without a system recorded approval. Purchases go through a *procurement system*, also called a procure-to-pay or P2P system: the application where someone raises a request to buy something, where that request travels to the people who have to agree to it, and where the resulting purchase order and invoice are recorded.

Because every purchase passes through it, your procurement system holds your purchasing rules. It knows who can request what, who approves which kinds of spending and in what order, and which budget receives the charge. It is also the one place to answer what was bought, by whom, and who agreed to it.

## Integration overview
<a name="procurement-system-integration-what-it-does"></a>

With this integration, your buyers can shop in AWS Marketplace while your procurement system continues to be the place where approvals are recorded.

It works through a *punchout*: an access point from your procurement system into an outside catalog. A buyer who punches out is still working inside your procurement process, but browsing the AWS Marketplace catalog. Their cart comes back to your procurement system as a purchase requisition, travels through your own approval workflow, and completes as a purchase order. The messages that carry the cart and the purchase order between the two systems use the commerce extensible markup language (cXML) protocol.

## How purchases flow
<a name="procurement-system-integration-how-it-flows"></a>

The following diagram shows how a subscription request travels from your procurement system to AWS Marketplace and back again, from the buyer searching for a product through to the request being submitted for approval.

The buyer starts in your procurement system and reaches the AWS Marketplace catalog from it. They arrive at a product details page in AWS Marketplace, choose **Continue to subscribe**, and reach the AWS Marketplace checkout page. Choosing **Request Approval** there returns the cart to your procurement system, where it is submitted for approval.

 ![Flow chart for procurement system subscription request](https://docs.aws.amazon.com/marketplace/latest/buyerguide/images/procurement-flow-01.png) 

The following diagram shows the approval process that then runs inside your procurement system, and what reaching the end of it produces in AWS Marketplace.

Approval request notifications reach an approver in your procurement system. Each approver decides in turn. After it has the final approval, your procurement system issues a purchase order, which subscribes the buyer in AWS Marketplace and produces a subscription invoice and a subscription notification.

 ![Flowchart for procurement system subscription approval](https://docs.aws.amazon.com/marketplace/latest/buyerguide/images/procurement-flow-02.png) 

The buyer doesn't need to return to AWS Marketplace to complete the purchase, though they might want to for instructions on how to use what they bought. AWS Marketplace sends an email message to the AWS account used to access AWS Marketplace, telling the recipient that the subscription succeeded and the software is available.

## What you control
<a name="procurement-system-integration-what-you-control"></a>

Connecting a procurement system doesn't send anything to it on its own. You decide which purchases go there, by writing approval rules that define which purchases need approval.

So a connection and a set of rules do different jobs: the connection makes your procurement system available as a destination, and the rules decide what arrives there. The rest of this chapter covers both, starting with the rules.
+ For more information about writing approval rules, see [Routing purchases to your procurement system](procurement-system-routing.md).
+ For more information about the arrangements that work well in practice, see [Best practices for procurement system integration](procurement-system-best-practices.md).