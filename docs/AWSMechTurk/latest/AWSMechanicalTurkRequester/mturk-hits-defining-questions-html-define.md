# Defining an HTML form

The example below describes a simple HTML form that prompts workers to answer a single
question. The centerpiece of this task is the `form` element that directs the
form to submit the worker response to '[https://www.mturk.com/mturk/externalSubmit](https://www.mturk.com/mturk/externalSubmit "https://www.mturk.com/mturk/externalSubmit")' with an HTTP POST call. This
element contains a `textarea` input element with a `name` attribute
that is associated with the worker's response. You can include as many input elements as
you wish in your form, but each element must have a unique `name` attribute.

```

<!DOCTYPE html>
<script type='text/javascript' src='https://s3.amazonaws.com/mturk-public/externalHIT_v1.js'></script>
<form method='post' id='mturk_form' action='https://www.mturk.com/mturk/externalSubmit'>
  <p>Describe the current weather where you live</p>
  <p><textarea name="weather" cols="80" rows="3"></textarea></p>
  <p><input type="submit" id="submitButton" class="btn btn-primary" value="Submit"/></p>
</form>
<script language='Javascript'>turkSetAssignmentID()</script>

```

To be able to successfully process the worker's response, Mechanical Turk needs the form response
to include the `assignmentId` that was provided in the query parameters for
this task. The two `script` elements in the example above use a Mechanical Turk library
that will automatically populate the `assignmentId` value in the form.

Note that the form `action` attribute in the preceding example explicitly
specifies the URL to which the form should be submitted. If you are testing in the sandbox
environment, you need to modify this value to
`https://workersandbox.mturk.com/mturk/externalSubmit`, or construct it using
the value provided in the `turkSubmitTo` query parameter.

The HTML you include in your task can be as simple or complex as necessary to allow
workers to provide the data you need. It's not uncommon for developers to include CSS and
JavaScript code to provide a rich interface to workers, and in many cases, developers have
leveraged React or other frontend libraries. Regardless of how you present the task to
workers, you must use of a form element to submit a POST to Mechanical Turk when the task is
complete. This directs the browser to advance and notify Mechanical Turk that the task is complete.
For Mechanical Turk to accept the POST operation, it must include the `assignmentId` field
so that Mechanical Turk can associate it with the worker's submission.
