

# Application owner questionnaire

Your inventory describes your servers. Your application owners know more: which applications must move together, when they can move, and how critical they are. AWS Transform creates an application questionnaire that your application owners fill in, so that your migration plan reflects that knowledge. Answering the questionnaire is optional, and partial answers are welcome.

## Receiving the questionnaire
<a name="transform-vmware-application-questionnaire-when"></a>

After you upload inventory data that includes applications, AWS Transform attaches a questionnaire to a chat message. When application grouping adds applications that an earlier questionnaire didn't cover, AWS Transform attaches another questionnaire for those applications only. You can also ask for the questionnaire again at any time.

The questionnaire is a Microsoft Excel workbook, `Application_Questionnaire.xlsx`, with one worksheet for each application. AWS Transform prefills each worksheet with what it already knows from your inventory, such as the application's description, servers, and dependencies. Each question has a **Current information** column, a **Your response** column, and a **Response status** column. To get the questionnaire in another format, such as Word, PDF, or CSV, ask in the chat.

## What the questionnaire asks
<a name="transform-vmware-application-questionnaire-questions"></a>

The questions are grouped into the following topics:
+ **Application description** – whether the summary, servers, tiers, and data stores are correct
+ **Dependencies and environments** – applications that must migrate together or first, connections that can stay in place between waves, and the application's environments
+ **Business impact and migration order** – how severe an outage would be, from Critical to Low, and whether the application should migrate earlier or later
+ **Timing and availability** – deadlines, migration windows, blackout dates, and permitted downtime
+ **Strategy and lifecycle** – the preferred migration strategy, such as Rehost or Retire, license restrictions, and planned refresh or retirement events
+ **Delivery and readiness** – the teams needed for cutover and testing, and the prerequisites that must be ready
+ **Users and usage** – usage peaks, and current risks or operational problems

## Returning the questionnaire
<a name="transform-vmware-application-questionnaire-return"></a>

Before you start, make sure that you have received the questionnaire in the chat. When you finish, the owners' answers are saved with your application data.

**To return the questionnaire**

1. In the chat, download the questionnaire.

1. Share the questionnaire with your application owners, and ask them to fill in what they know.

1. Upload the completed workbook to the chat. For example, "The application owners filled in the migration questionnaire and I've uploaded it. Can you go through their answers?"

1. Review the application owners' answers that AWS Transform summarizes.

1. Tell AWS Transform which answers to save. It saves answers only after you agree. You can save all of them, or save everything except the answers that you want to confirm with the owners first.

## How the answers affect your migration plan
<a name="transform-vmware-application-questionnaire-effect"></a>
+ **Wave order** – applications that others must follow migrate first. Then applications whose owners prefer to migrate earlier come before those that prefer later. Then less critical applications migrate first, so that they can serve as a pilot. These answers only break ties that your own wave planning rules leave.
+ **Migration strategy** – an owner's preferred strategy appears in the R-strategy (7Rs) report with the source `application questionnaire`. A decision that you record in migration planning takes precedence over it.
+ **Business criticality** – an owner's answer sets the criticality of an application that doesn't already have one.

AWS Transform saves your other answers, such as deadlines and blackout windows, with your application data. Migration planning doesn't apply them automatically.