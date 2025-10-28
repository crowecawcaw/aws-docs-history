# Fields for an HTML5 asset

| Field on web interface | Tag in the XML       | Type    | Description                                                                                                                                                              |
| ---------------------- | -------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Insertion Mode         | <insertion_mode>     | String  | Choose `HTML`.                                                                                                                                                           |
| Input                  | <uri>                | String  |                                                                                                                                                                          |
| Username Password      | <username><password> | String  |                                                                                                                                                                          |
| Active                 | <active>             | Boolean | Always select this box.                                                                                                                                                  |
| Enable REST Control    | <enable_rest>        | Boolean | Select this field only if you chose to use the REST API to [control the asset](step-design-controls-html5.md "step-design-controls-html5.md").                           |
| Enable SCTE 35 Control | <enable_scte35>      | Boolean | Select this field only if you chose to use SCTE 35 messages in the source content to [control the asset](step-design-controls-html5.md "step-design-controls-html5.md"). |
