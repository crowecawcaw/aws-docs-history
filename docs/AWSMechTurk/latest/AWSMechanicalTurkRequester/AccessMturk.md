# Access Amazon Mechanical Turk

You can access Amazon Mechanical Turk (Mechanical Turk) using the Mechanical Turk
requester
user
interface, the AWS Command Line Interface (AWS CLI), or the Mechanical Turk API.

###### Topics

- [Use
  the Mechanical Turk Requester UI](#access-mturk-req-ui "#access-mturk-req-ui")
- [Use
  the
  Mechanical Turk API](#access-mturk-use-api "#access-mturk-use-api")
- [Use the AWS CLI](#access-mturk-use-cli "#access-mturk-use-cli")

## Use

the Mechanical Turk Requester UI

The Mechanical Turk Requester User Interface (RUI) provides access to
Mechanical Turk
functionality using a graphical user interface. You can use the Mechanical Turk RUI to:

- Create projects that define tasks you want
  workers
  to complete
- Submit batches of tasks to the Mechanical Turk
  marketplace
- Monitor and review the results of batches
- Approve and reject task submissions
- Manage
  workers
- Create and modify qualification types

For more information on using the RUI, visit the [Amazon
Mechanical Turk Requester UI Guide](../RequesterUI/index.md "../RequesterUI/index.md").

HITs
created from the API or AWS CLI cannot be viewed from the Requester UI.

## Use

the
Mechanical Turk API

The AWS SDKs provide broad support for Mechanical Turk in [Java](https://aws.amazon.com/sdk-for-java "https://aws.amazon.com/sdk-for-java"), [JavaScript in the browser](https://aws.amazon.com/sdk-for-browser "https://aws.amazon.com/sdk-for-browser"),
[.NET](https://aws.amazon.com/sdk-for-net "https://aws.amazon.com/sdk-for-net"), [Node.js](https://aws.amazon.com/sdk-for-node-js "https://aws.amazon.com/sdk-for-node-js"), [PHP](https://aws.amazon.com/sdk-for-php "https://aws.amazon.com/sdk-for-php"), [Python](https://aws.amazon.com/sdk-for-python "https://aws.amazon.com/sdk-for-python"), [Ruby](https://aws.amazon.com/sdk-for-ruby "https://aws.amazon.com/sdk-for-ruby"), [C++](https://aws.amazon.com/sdk-for-cpp "https://aws.amazon.com/sdk-for-cpp"), and [Go](https://aws.amazon.com/sdk-for-go "https://aws.amazon.com/sdk-for-go"). To get started quickly with many
of these languages, see the [Amazon Mechanical Turk Code
Samples](https://github.com/aws-samples/mturk-code-samples "https://github.com/aws-samples/mturk-code-samples").

Before you
can use the AWS SDKs with Mechanical Turk, you must get an AWS access key ID and secret access key.
For more information, see [Set up Amazon Mechanical Turk](SetUpMturk.md "SetUpMturk.md").

## Use the AWS CLI

You can use the AWS Command Line Interface (AWS CLI) to control multiple AWS services from the command
line and automate them through scripts. This includes posting Mechanical Turk HITs and retrieving
results, either on an
ad-hoc
basis or within utility scripts.

Before you
can use the AWS CLI with Mechanical Turk, you must get an access key ID and secret access key. For
more information, see
Get
an AWS access key.

For a
complete listing of all the commands available for Mechanical Turk in the AWS CLI, see the [AWS CLI
Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md").

### Download and

configure
the AWS CLI

The AWS CLI is available at [https://aws.amazon.com/cli](https://aws.amazon.com/cli "https://aws.amazon.com/cli"). It runs on Windows,
MacOS,
or Linux. After you download the AWS CLI, follow these steps to install and configure
it:

- Go to the
  [AWS Command Line Interface User
  Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").
- Follow
  the instructions for
  [Installing the AWS CLI](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md")
  and
  [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").

### Use the AWS CLI with Mechanical Turk

The command line format consists of
a Mechanical Turk
operation name followed by the parameters for that operation. The AWS CLI supports a
shorthand syntax for the parameter values, as well as JSON.

For
example, the following command returns a list of the HITs that have been created for
in your account.

```

$ aws mturk list-hits

```

The
next command creates a new HIT in the Mechanical Turk marketplace (for easier readability, long
commands in this section are broken into separate lines).

###### Important

Creating
the following HIT
results
in a charge of $0.12 to your account.

```

$ aws mturk create-hit \
         --title "Describe the weather" \
         --description "Describe the current weather where you live" \
         --reward "0.10" \
         --lifetime-in-seconds 14400 \
         --assignment-duration-in-seconds 300 \
         --question '<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
                    <HTMLContent><![CDATA[
                    <!DOCTYPE html>
                    <script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
                    <crowd-form>
                    <p>Describe the current weather where you live</p>
                    <p><textarea name="weather" cols="80" rows="3"></textarea></p>
                    </crowd-form>
                    ]]>
                    </HTMLContent>
                    <FrameHeight>0</FrameHeight>
                    </HTMLQuestion>'

```

This
returns
the attributes of the HIT you created. After the task is completed, you can retrieve
the results by using the `ListAssignmentsForHIT` operation.

```

$ aws mturk list-assignments-for-hit \
          --hit-id <The HITId from the previous step>

```

On the
command line, it can be difficult to compose valid HTML for your task when calling
`CreateHIT`. However, the AWS CLI can read XML files. For
example, consider the
following,
which creates a HIT using a question stored in a file
_question.xml_.

```

$ aws mturk create-hit \
     --title "Describe the weather" \
     --description "Describe the current weather where you live" \
     --reward "0.10" \
     --lifetime-in-seconds 14400 \
     --assignment-duration-in-seconds 300 \
     --question file://question.xml

```
