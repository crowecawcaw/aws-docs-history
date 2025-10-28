# Dynamic input

switching

The dynamic input switching feature lets you use REST API commands to
switch inputs in an AWS Elemental Live event. This method of input switching has two key
features:

- The switching control (the REST API) is built into
  Elemental Live. You don't need an external server to control
  switching.
- You can modify the _playlist_
  of inputs without stopping the event. This ability to
  dynamically change the playlist is useful when you can't
  identify all of the inputs that you want to use in advance
  (before starting the event).
  You can also switch inputs by using virtual input switching with an
  ESAM server. For more information, see [Virtual input switching](feature-vips.md "feature-vips.md").

###### Note

Use only one mechanism to control input switching. Don't give
control of the input switching logic to both an ESAM server and a
REST-based application. We strongly recommend against implementing a
combination of these input switching features.

**How dynamic input switching
works**

The dynamic input switching feature works as follows. When you create
the event, you set up only the first input that you plan to
process.

After you start the event, use the Elemental Live REST API to add more
inputs to the event. You can create a playlist consisting of any number
of live inputs, or file inputs, or both. This gives you a playlist
consisting of the first input (which is currently being processed) and
the inputs that you added using the REST API.

An input switch can occur in one of these ways:

- REST API-triggered switch. You switch to a different input by
  entering a REST API command to activate that input. This input
  can be any input in the playlist. You can set it up so that an
  input becomes active immediately or at a specific time.
- Automatic switch. If Elemental Live gets to the end of a file
  input that is not set up to loop, then Elemental Live switches to
  the next input in the list of inputs in the
  event.

This method works well when you have a series of file inputs
such as ad content. In this case, you let Elemental Live go
through the inputs one by one. Before the series ends, enter a
REST API command to activate a different input (perhaps a live
input). This is to break out of the event order.
You can modify the playlist to add and remove inputs. If your event
runs on a 24/7 basis, you will typically remove old inputs and add a
fresh set of inputs on a regular basis.
