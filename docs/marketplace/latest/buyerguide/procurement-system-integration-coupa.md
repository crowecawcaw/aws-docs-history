

# Configuring AWS Marketplace to integrate with Coupa

The topics in this section explain how to integrate AWS Marketplace with a Coupa procurement system.

## Step 1. Check the prerequisites
<a name="procurement-system-coupa-step1"></a>

Configuration starts in AWS Marketplace, where you create the connection, and finishes in Coupa, where you create the supplier and the punchout site. You use information from the AWS Marketplace connection to configure Coupa, so you need access to both systems.

For the permissions and the other prerequisites, see [Prerequisites for procurement system integration](procurement-system-prerequisites.md).

## Step 2. Create the connection in AWS Marketplace
<a name="procurement-system-coupa-step2"></a>

The connection holds the credentials that identify your Coupa system and AWS Marketplace to each other.

### Credentials you choose
<a name="procurement-system-coupa-credentials"></a>

The following credentials identify the two systems to each other. You choose them, enter them in AWS Marketplace here, and enter the same values again in Coupa in step 3. They have to match on both sides.

Buyer ID  
Your buyer identity. It identifies your organization as the buyer in the cXML exchange. In Coupa it is the **cXML identity**.

Supplier ID  
Your supplier identity. It identifies AWS Marketplace as the supplier in the cXML exchange. In Coupa it is the **cXML supplier identity**.

Shared secret  
Your shared secret. It authenticates the cXML messages between Coupa and AWS Marketplace. In Coupa it is the **cXML secret**.  
You own this credential. Rotate it on the schedule your organization applies to other shared secrets, changing it in AWS Marketplace and in Coupa together so that the two stay in step.

The identities aren't only labels. They're checked alongside the shared secret to authorize the exchange, so treat them as part of what protects the integration. We recommend generating each identity as a universally unique identifier (UUID) rather than choosing a name that someone could guess.

The shared secret is a credential, so generate it rather than choose it. We recommend a value of at least 32 characters from a cryptographically secure random generator, and a value used for this integration alone rather than one reused from another system.

Enter each of these values identically on both sides. They're compared exactly, so a difference in capitalization or a trailing space stops AWS Marketplace and Coupa recognizing each other, and purchase orders are rejected.

### Creating the connection
<a name="procurement-system-coupa-connection"></a>

**To create the connection in AWS Marketplace**

1. On the [**External system**](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?region=us-east-1&tab=external-system) tab of the **Approvers and routing** page, choose **Connect**.

1. Choose **Add new Coupa Connection**, and then complete the following fields in the form:
   + **Buyer ID** – Your buyer identity.
   + **Shared secret** – Your shared secret.
   + **Supplier ID** – Your supplier identity.
   + **Seller of Record** – Select the AWS Billing entities that match the AWS Billing entity that you are setting up. If you don't select any, the connection accepts purchases from all AWS Billing entities. Select specific entities if you plan to use different supplier configurations for different AWS Billing entities.
   + **Approval request redirect URL** – Where AWS Marketplace sends a buyer who started a purchase in AWS Marketplace rather than in Coupa, so that their request still reaches Coupa for approval. The address comes from Coupa, so leave this empty for now. You can add it after Coupa is configured, in step 4, and you can skip it altogether if your buyers always begin their purchases in Coupa.

1. Choose **Save** to complete the integration on the AWS Marketplace side.

The connection now appears in your list of procurement connections. Saving it also generates the cXML address that Coupa will send purchase orders to, which looks like this:

```
https://example12345.procurement-portal-cxml.us-east-1.on.aws/purchase-order
```

Copy that address from the connection, because you enter it in Coupa in step 3.

**Note**  
Creating a connection doesn't send any purchases to Coupa on its own. You decide which purchases go there by writing approval rules. For more information about approval rules, see [Routing purchases to your procurement system](procurement-system-routing.md).

### Managing your connections
<a name="procurement-system-coupa-managing-connections"></a>

You can add and manage additional connections for other billing entities from the same page. Each connection uses its own set of credentials and can be scoped to different AWS Billing entities.

If you previously onboarded to electronic invoice delivery or to cloud purchase order retrieval, you already have a connection to Coupa and don't need a new one. Edit the existing connection instead, and select **Enable AWS Marketplace PunchOut**, which makes that connection apply to AWS Marketplace as well.

**To manage your Coupa connections**

1. On the [**External system**](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?region=us-east-1&tab=external-system) tab of the **Approvers and routing** page, review your existing connections in the **Portal connections** table. Each row lists the connection's **Buyer ID**, **Supplier ID**, **Seller of Record**, and **AWS Marketplace PunchOut status**.

1. To turn AWS Marketplace PunchOut on or off for a connection, select the connection. An edit section appears, where you enable or disable it.
**Note**  
Disabling a connection is reversible. The connection remains in your account, and you can enable it again later.

1. To edit more of a connection's configuration than this page carries, including electronic invoicing and cloud purchase order retrieval, use the [AWS Billing and Cost Management console](https://console.aws.amazon.com/costmanagement/home#/e-invoicing-preference/procurement-portal-preference/).

## Step 3. Set up the supplier and punchout site in Coupa
<a name="procurement-system-coupa-step3"></a>

Coupa needs a supplier record for AWS Marketplace and a punchout site that reaches the AWS Marketplace catalog. You create both in Coupa, using the credentials you chose in step 2 and the cXML address the connection gave you.

### Supplier settings
<a name="procurement-system-coupa-supplier"></a>

On the supplier record for AWS Marketplace, under **PO transmission**, configure the following settings.


| Setting | Value | 
| --- | --- | 
| PO method | cXML | 
| cXML URL | The cXML address you copied from the connection in step 2. | 
| cXML domain | NetworkID | 
| cXML identity | Your buyer identity. | 
| cXML supplier identity | Your supplier identity. | 
| cXML secret | Your shared secret. | 
| cXML protocol | cXML | 
| Enable mutual TLS for PO cXML | Selected. This setting is required. | 

**Important**  
Mutual Transport Layer Security (TLS) is required, and it is what makes this channel trustworthy. It authenticates both ends of the connection, so AWS Marketplace can establish that a purchase order genuinely came from your Coupa system rather than from someone impersonating it. Select this setting when you configure the supplier record.

#### Invoicing settings on the supplier
<a name="procurement-system-coupa-supplier-invoicing"></a>

Electronic invoice delivery is optional. The punchout carries purchases to Coupa, and invoices travel the other way. Most organizations want both, so that a purchase that began as a requisition in Coupa ends as an invoice there too.

If you want invoices delivered to Coupa, the invoicing settings on the same supplier record take the same values as the purchase order settings, so that invoices and purchase orders travel between the same two identities.


| Setting | Value | 
| --- | --- | 
| cXML invoicing supplier domain | NetworkID | 
| cXML invoicing supplier identity | Your supplier identity. | 
| cXML invoicing buyer domain | NetworkID | 
| cXML invoicing buyer identity | Your buyer identity. | 
| cXML invoicing shared key | Your shared secret. | 

For more information about electronic invoice delivery, see [Setting up electronic invoice delivery](procurement-system-invoicing.md).

### Punchout site settings
<a name="procurement-system-coupa-punchout-site"></a>

The punchout site is what takes your buyers from Coupa to the AWS Marketplace catalog. Configure the following settings.


| Setting | Value | 
| --- | --- | 
| Punchout URL | https://eprocurement.marketplace.us-east-1.amazonaws.com/v1/punchout/setup?start\_url= | 
| Domain | NetworkID | 
| Identity | Your supplier identity, the same value as cXML supplier identity on the supplier. | 
| Secret | Your shared secret, the same value as cXML secret on the supplier. | 
| Sender domain | NetworkID | 
| Sender identity | Your buyer identity, the same value as cXML identity on the supplier. | 
| Protocol | cXML | 

**Note**  
The punchout address ends with the `start_url` query parameter, which is part of the address and is the same for everyone. Its value is optional: leave it empty to send your buyers to the default AWS Marketplace landing page, or set it to the page you want them to land on when the punchout session starts.  
That is how you use the punchout for single sign-on, by pointing your buyers at your own identity provider instead of the default AWS sign-in page. For more information about single sign-on, see [Configuring single sign-on for procurement system integration](procurement-system-sso.md).

#### Letting buyers start in AWS Marketplace instead of Coupa
<a name="procurement-system-coupa-direct-punchout"></a>

By default, a buyer begins in Coupa and punches out from there to the AWS Marketplace catalog. That punchout is what establishes the session connecting the two systems.

Direct punchout, also called PunchOutAnywhere, removes that first step. Your buyers can begin in AWS Marketplace directly and still have their cart returned to Coupa, without starting in Coupa to set the session up. This suits organizations whose buyers naturally start by browsing the catalog rather than by starting their journey from within Coupa and punching out to the AWS Marketplace catalog.

To allow it, select **Allow 'Anywhere' punchout from suppliers** on the punchout site and copy the address that Coupa gives you. It looks like this:

```
https://your-instance.coupacloud.com/punchout/checkout?id=19
```

This address is what you apply to your AWS Marketplace connection, in step 4.

## Step 4. Add the approval redirection address (optional)
<a name="procurement-system-coupa-step4"></a>

Complete this step if you want to enforce the approval request to Coupa for those users that begin their journey natively in AWS Marketplace.

In AWS Marketplace, edit your connection and enter the address you copied from Coupa as the **Approval request redirect URL**. For where that address comes from, see [Letting buyers start in AWS Marketplace instead of Coupa](#procurement-system-coupa-direct-punchout).

With this in place, confirm that the whole path works, and that your users are permissioned to and know how to use Coupa before your buyers use it. For more information about testing, see [Testing your procurement system integration](procurement-system-testing.md).

## Coupa documentation
<a name="procurement-system-coupa-resources"></a>

For Coupa's own instructions on the Coupa side of the setup, see [Coupa Punchout Setup](https://success.coupa.com/Suppliers/For_Customers/Toolkit/Manage_Catalogs/Punchout_Catalogs/Punchout_Setup) and [Configuring a Supplier for cXML Purchase Orders](https://success.coupa.com/Suppliers/For_Customers/Toolkit/Document_Exchange/cXML/Configuring_a_Supplier_for_cXML_Purchase_Orders).