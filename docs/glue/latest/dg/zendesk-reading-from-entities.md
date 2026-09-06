

# Reading from Zendesk entities
<a name="zendesk-reading-from-entities"></a>

**Prerequisite**

A Zendesk Object you would like to read from. You will need the object name such as ticket or user or article, as mentioned in the following table.


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Ticket | Y | Y | Y | Y | N | 
| User | Y | Y | Y | Y | N | 
| Organization | Y | Y | Y | Y | N | 
| Article | Y | Y | N | Y | N | 
| Ticket Event | Y | Y | N | Y | N | 
| Ticket Metric Event | Y | Y | N | Y | N | 
| Ticket Comment | Y | Y | Y | Y | N | 
| Ticket Field | Y | Y | N | Y | N | 
| Ticket Metric | Y | Y | N | Y | N | 
| Ticket Activity | Y | Y | N | Y | N | 
| Ticket Skip | N | Y | N | Y | N | 
| Group | Y | Y | Y | Y | N | 
| Group Membership | N | Y | Y | Y | N | 
| Satisfaction Rating | Y | Y | N | Y | N | 
| View | Y | Y | Y | Y | N | 
| Trigger | Y | Y | Y | Y | N | 
| Trigger Category | N | Y | Y | Y | N | 
| Macro | Y | Y | Y | Y | N | 
| Automation | N | Y | Y | Y | N | 

**Example**:

```
Zendesk_read = glueContext.create_dynamic_frame.from_options(
    connection_type="Zendesk",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Account",
        "API_VERSION": "v2"
    }
```

**Zendesk entities and field details**:



- **articles**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** author\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** body / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** comments\_disabled / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** draft / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** edited\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** html\_url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** label\_names / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** locale / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** outdated / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** outdated\_locales / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** permission\_group\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** position / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** promoted / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** section\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** source\_locale / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** name / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** user\_segment\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** content\_tags\_id / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** vote\_count / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** vote\_sum / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** label\_name / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 

- **group**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** is\_public / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** name / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** description / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** default / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** deleted / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** exclude\_deleted / **Data type:** Boolean / **Supported operators:** EQUAL\_TO / **Comments:** 

- **automation**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** active / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** default / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** actions / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** positions / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** conditions / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** raw\_title / **Data type:** String / **Supported operators:**  / **Comments:** 

- **group-membership**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** user\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** group\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** default / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 

- **macro**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** active / **Data type:** Boolean / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** default / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** actions / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** position / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** description / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** raw\_title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** restriction / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** access / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** category / **Data type:** Integer / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** group\_id / **Data type:** Long / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** only\_viewable / **Data type:** Boolean / **Supported operators:** EQUAL\_TO / **Comments:** 

- **organizations**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** external\_id / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** name / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** domain\_names / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** details / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** notes / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** group\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** shared\_tickets / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** shared\_comments / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** tags / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** organization\_fields / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** DML\_STATUS / **Data type:** String / **Supported operators:**  / **Comments:** A user-defined field used to track the created, updated and deleted status of the record.

- **satisfaction-rating**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** assignee\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** comment / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** group\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** reason / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** reason\_code / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** reason\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** requester\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** score / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** ticket\_id / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** start\_time / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** end\_time / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** DML\_STATUS / **Data type:** String / **Supported operators:**  / **Comments:** A user-defined field used to track the created, updated and deleted status of the record.

- **ticket-activity**
  - **Field:** actor / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** actor\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** object / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** target / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** user / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** user\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** verb / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 

- **ticket-comment**
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** type / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** author\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** body / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** html\_body / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** plain\_body / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** public / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** attachments / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** audit\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** via / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** metadata / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** ticket\_id / **Data type:** Integer / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** include\_inline\_images / **Data type:** Boolean / **Supported operators:** EQUAL\_TO / **Comments:** 

- **ticket-events**
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** ticket\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** timestamp / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updater\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** child\_events / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** via / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** system / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** event\_type / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** comment\_present / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** comment\_public / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** via\_reference\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** DML\_STATUS / **Data type:** String / **Supported operators:**  / **Comments:** A user-defined field used to track the created, updated and deleted status of the record.

- **ticket-field**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** type / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** raw\_title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** description / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** raw\_description / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** position / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** active / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** required / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** collapsed\_for\_agents / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** regexp\_for\_validation / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** title\_in\_portal / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** raw\_title\_in\_portal / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** visible\_in\_portal / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** editable\_on\_portal / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** required\_in\_portal / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** tag / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** removable / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** agent\_description / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** custom\_field\_options / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** custom\_statuses / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** relationship\_filter / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** relationship\_target\_type / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** sub\_type\_id / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** system\_field\_options / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** locale / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 

- **ticket-metric-events**
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** time / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** ticket\_id / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** metric / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** instance\_id / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** type / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** DML\_STATUS / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** A user-defined field used to track the created, updated and deleted status of the record.

- **ticket-metric**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** ticket\_id / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** group\_stations / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** assignee\_stations / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** reopens / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** replies / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** assignee\_updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** requester\_updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** initially\_assigned\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** assigned\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** solved\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** last\_comment\_added\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** reply\_time\_in\_minutes / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** first\_resolution\_time\_in\_minutes / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** full\_resolution\_time\_in\_minutes / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** agent\_wait\_time\_in\_minutes / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** requester\_wait\_time\_in\_minutes / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** on\_hold\_time\_in\_seconds / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** reply\_time\_in\_seconds / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** custom\_status\_updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 

- **ticket-skip**
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** reason / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** ticket / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** ticket\_id / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** user\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 

- **tickets**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** external\_id / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** type / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** subject / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** raw\_subject / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** description / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** priority / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** status / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** recipient / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** requester / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** requester\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** submitter\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** assignee\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** organization\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** group\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** collaborator\_ids / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** emails\_cc\_ids / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** follower\_ids / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** forum\_topic\_id / **Data type:** Ling / **Supported operators:**  / **Comments:** 
  - **Field:** problem\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** has\_incidents / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** due\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** tags / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** via / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** custom\_fields / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** satisfaction\_rating / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** sharing\_agreement\_ids / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** followup\_ids / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** via\_followup\_source\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** ticket\_form\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** brand\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** allow\_channelback / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** allow\_attachments / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** is\_public / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** from\_messaging\_channel / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** assignee\_email / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** attribute\_value\_ids / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** collaborators / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** comment / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** custom\_status\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** email\_ccs / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** followers / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** macro\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** macros\_ids / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** metadata / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** safe\_update / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_stamp / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** via\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** voice\_comment / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** DML\_STATUS / **Data type:** String / **Supported operators:**  / **Comments:** A user-defined field used to track the created, updated and deleted status of the record.

- **trigger-category**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** name / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** position / **Data type:** Integer / **Supported operators:**  / **Comments:** 

- **trigger**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** active / **Data type:** Boolean / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** default / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** actions / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** conditions / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** description / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** position / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** raw\_title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** category\_id / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 

- **users**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** external\_id / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** email / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** active / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** alias / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** chat\_only / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** custom\_roll\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** roll\_type / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** details / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** last\_login\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** locale / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** locale\_id / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** moderator / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** notes / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** name / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** only\_private\_comments / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** organization\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** default\_group\_id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** phone / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** photo / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** remote\_photo\_url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** restricted\_agent / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** role / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** shared / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** shared\_agent / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** tag / **Data type:** List / **Supported operators:**  / **Comments:** 
  - **Field:** signature / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** suspended / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** ticket\_restriction / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** time\_zone / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** iana\_time\_zone / **Data type:**  / **Supported operators:**  / **Comments:** 
  - **Field:** two\_factor\_auth\_enabled / **Data type:**  / **Supported operators:**  / **Comments:** 
  - **Field:** user\_fields / **Data type:**  / **Supported operators:**  / **Comments:** 
  - **Field:** verified / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** report\_csv / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** permission\_set / **Data type:** Long / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** shared\_phone\_number / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** DML\_STATUS / **Data type:** String / **Supported operators:**  / **Comments:** A user-defined field used to track the created, updated and deleted status of the record.

- **view**
  - **Field:** url / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** id / **Data type:** Long / **Supported operators:**  / **Comments:** 
  - **Field:** title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** active / **Data type:** Boolean / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** updated\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:**  / **Comments:** 
  - **Field:** default / **Data type:** Boolean / **Supported operators:**  / **Comments:** 
  - **Field:** position / **Data type:** Integer / **Supported operators:**  / **Comments:** 
  - **Field:** description / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** execution / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** restriction / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** raw\_title / **Data type:** String / **Supported operators:**  / **Comments:** 
  - **Field:** conditions / **Data type:** Struct / **Supported operators:**  / **Comments:** 
  - **Field:** access / **Data type:** String / **Supported operators:** EQUAL\_TO / **Comments:** 
  - **Field:** group\_id / **Data type:** Long / **Supported operators:** EQUAL\_TO / **Comments:** 



**Note**  
Struct and List data types are converted to String data type in the response of the connector.

## Partitioning queries
<a name="zendesk-reading-partitioning-queries"></a>

Partitions are not supported in Zendesk.