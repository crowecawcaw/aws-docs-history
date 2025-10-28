# Submitting from

JavaScript

In some cases, it's necessary to collect data using mechanisms other than form fields.
For example, a task interface that prompts workers to draw a bounding box on an image
would capture the coordinates of the box workers drew as a JavaScript variable. To allow
workers to submit the data, you must place it in a `form` element that can be
submitted to Mechanical Turk.

There are two common ways to do this. The first is using a hidden form value within
your task as shown in the following code excerpt. The form includes hidden values for the
`assignmentId` and coordinates that we want to return. When workers choose
the **Submit** button, the `handleFormSubmit` function is
called. The function populates the values in the hidden form elements and then submits the
form.

```

<html>
...
<button onclick="handleFormSubmit()">Submit</button>
<form method='post' id='mturk_form' action='https://www.mturk.com/mturk/externalSubmit'>
  <input type="hidden" id="inputCoordinates" name="coordinates">
  <input type="hidden" id="inputAssignmentId" name="assignmentId">
</form>
 
<script>
function handleFormSubmit() {
  const urlParams = new URLSearchParams(window.location.search)
  document.getElementById('inputAssignmentId').value = urlParams.get('assignmentId')
  document.getElementById('inputCoordinates').value = JSON.stringify(coordinates)
  document.getElementById('mturk_form').submit()
}
</script>

```

You must include a value for `assignmentId` in your form submission so that
Mechanical Turk can correctly associate the response with the correct worker and HIT.

In cases where you don't want to include the form and hidden inputs in the HTML, you
can instead create and populate the elements dynamically from your JavaScript code as
shown in the following example. Note that in the following code, we're assigning the value
for action based on the `turkSubmitTo` value from the URL search parameters for
the task. This sets the correct value based on whether or not you are working in the
production or sandbox environment.

```

const handleClick = () => {
  const urlParams = new URLSearchParams(window.location.search)
 
  // create the form element and point it to the correct endpoint
  const form = document.createElement('form')
  form.action = (new URL('mturk/externalSubmit', urlParams.get('turkSubmitTo'))).href
  form.method = 'post'
 
  // attach the assignmentId
  const inputAssignmentId = document.createElement('input')
  inputAssignmentId.name = 'assignmentId'
  inputAssignmentId.value = urlParams.get('assignmentId')
  inputAssignmentId.hidden = true
  form.appendChild(inputAssignmentId)
 
  // attach data I want to send back
  const inputCoordinates = document.createElement('input')
  inputCoordinates.name = 'coordinates'
  inputCoordinates.value = JSON.stringify(coordinates)
  inputCoordinates.hidden = true
  form.appendChild(inputCoordinates)
 
  // attach the form to the HTML document and trigger submission
  document.body.appendChild(form)
  form.submit()
}

```
