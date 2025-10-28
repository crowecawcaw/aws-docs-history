# Question definitions

Mechanical Turk provides three XML schemas that you can use to define your questions:

- [`HTMLQuestion`](../AWSMturkAPI/ApiReference_HTMLQuestionArticle.md "../AWSMturkAPI/ApiReference_HTMLQuestionArticle.md")
- [`ExternalQuestion`](../AWSMturkAPI/ApiReference_ExternalQuestionArticle.md "../AWSMturkAPI/ApiReference_ExternalQuestionArticle.md")
- [`QuestionForm`](../AWSMturkAPI/ApiReference_QuestionFormDataStructureArticle.md "../AWSMturkAPI/ApiReference_QuestionFormDataStructureArticle.md")
  Use the following topics to learn more about these schemas.

###### Topics

- [HTMLQuestion](#mturk-hits-defining-questions-definitions-htmlquestion "#mturk-hits-defining-questions-definitions-htmlquestion")
- [ExternalQuestion](#mturk-hits-defining-questions-definitions-externalquestions "#mturk-hits-defining-questions-definitions-externalquestions")
- [QuestionForm](#mturk-hits-defining-questions-definitions-questionform "#mturk-hits-defining-questions-definitions-questionform")

## `HTMLQuestion`

Most developers use the [`HTMLQuestion`](../AWSMturkAPI/ApiReference_HTMLQuestionArticle.md "../AWSMturkAPI/ApiReference_HTMLQuestionArticle.md") schema to create HITs. `HTMLQuestion`
wraps an HTML form that is displayed to workers. This typically takes the following form:

```

<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
  <HTMLContent><![CDATA[
    <!DOCTYPE html>
    <script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
    <crowd-form>
      <p>Describe the current weather where you live</p>
      <p><textarea name="weather" cols="80" rows="3"></textarea></p>
    </crowd-form>
  ]]></HTMLContent>
  <FrameHeight>0</FrameHeight>
</HTMLQuestion>

```

​As you can see in the preceding XML, the HTML content is enclosed in a CDATA element
within the XML and includes the elements that define how your question appears to workers.
More information on defining your HTML can be found in [Use HTML to define questions](mturk-hits-defining-questions-html.md "mturk-hits-defining-questions-html.md").

## `ExternalQuestion`

When you create a task using the `HTMLQuestion` format, your HTML is hosted
by Mechanical Turk. Using Mechanical Turk to host your task helps ensure that it is in a highly available
location. If, however, you want to host the task interface on your own servers or cloud
resources, you can use the [`ExternalQuestion`](../AWSMturkAPI/ApiReference_ExternalQuestionArticle.md "../AWSMturkAPI/ApiReference_ExternalQuestionArticle.md") format.

To use `ExternalQuestion`, your URL must meet the following criteria:

- The location specified by the URL must support HTTPS.
- The location must be highly available and able to respond quickly when workers
  accept or preview your task.
- The URL cannot include any of the reserved query parameters
  (`assignmentId`, `hitId`, `turkSubmitTo`, and
  `workerId`) that is appended by Mechanical Turk, as described in [How Mechanical Turk tasks are rendered](mturk-hits-defining-questions-html-rendered.md "mturk-hits-defining-questions-html-rendered.md") .
- The location specified by the URL must perform a form `POST` operation
  with the `assignmentId` when the task is completed, as described in [Use HTML to define questions](mturk-hits-defining-questions-html.md "mturk-hits-defining-questions-html.md").

Amazon S3 is a great option for hosting your task HTML. When you use an S3-hosted layout,
you need to add a `ContentType` header and set the ACL to public read, as shown
in the following Python SDK `PutObject` call:

```

s3_client.put_object(
   ACL='public-read',
   Body=HTML layout,
   Bucket=S3 bucket name,
   Key=Object name,
   ContentType="text/html"
)
 

```

When using this schema, you simply need to indicate the URL you want to use.

```

<?xml version="1.0" encoding="UTF-8"?>
<ExternalQuestion xmlns=" http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/ExternalQuestion.xsd">
  <ExternalURL>https://tictactoe.amazon.com/gamesurvey.cgi?gameid=01523</ExternalURL>
  <FrameHeight>0</FrameHeight>
</ExternalQuestion>
 

```

When you use `ExternalQuestion`, you can make the served HTML as complex or
simple as necessary for your particular task.  However, you must use of a form element to
submit a POST to Mechanical Turk when the task is complete. This directs the browser to advance and
notify Mechanical Turk that the task is complete.

## `QuestionForm`

`QuestionForm` is a legacy XML format that can be used to define Mechanical Turk
tasks using an XML schema. While it is still supported, we recommend building your task
using `HTMLQuestion` or `ExternalQuestion`.
