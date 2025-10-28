# Step G: Use the Router Inputs

When you create a profile or event, the inputs that you created
are displayed in the
**Input** field.

Note that you specify the input by identifying the router input, not
by identifying the SDI input. So you are giving the instruction "Use the
input that is coming in on Input 1 using the Videohub Ethernet Protocol."
When you run the event, Conductor Live directs this input to a free SDI
card. Each time you run the event, a different SDI input could be
used.

###### Avoid Direct Inputs

Typically, all of your SDI inputs are connected to your router. Therefore, you
should only ever specify the input by selecting one of the router inputs. You should
_not_ use any of the “direct inputs,” such as those
labeled as HD-SDI.

If your inputs are all connected to your router and you select a direct input in the
profile or event, when the event starts, an **`input not detected`**
error occurs.

You should only use the direct inputs for inputs on the Conductor Live node
that do not connect to the router but are instead direct inputs.
