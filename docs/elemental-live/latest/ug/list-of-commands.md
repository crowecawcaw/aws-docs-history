

# List of commands
<a name="list-of-commands"></a>


|  Nickname  |  Action  |  Signature  |  Description  | 
| --- | --- | --- | --- | 
| Add dynamic playlist inputs | POST | /live\_events/<event ID>/inputs | In the specified event (which must be currently running), add the specified input or inputs to the end of the dynamic playlist. | 
| Replace dynamic playlist | POST | /live\_events/<event ID>/playlist | In the specified event (which must be currently running), remove all non-Active inputs from the dynamic playlist and append the specified input or inputs. After this command, only the Active input remains from the original dynamic playlist. | 
| Get event | GET | /live\_events/<event ID> | Gets the contents of the event, including the list of inputs. | 
| Modify dynamic playlist input | PUT | /live\_events/<event ID>/inputs/ <input ID>  | In the specified event (which must be currently running), modify the specified dynamic playlist input (which must be non-Active). | 
|  | PUT | /live\_events/<event ID>/inputs/ by\_label/<input\_label>  | In the specified event (which must be currently running), modify the specified input (which must be non-Active). | 
| Delete dynamic playlist input | DELETE | /live\_events/<event ID>/inputs/ <input ID>  | In the specified event (which must be currently running), delete the specified non-Active input from the dynamic playlist.  | 
|  | DELETE | /live\_events/<event ID>/inputs/ by\_label/<input\_label>  | In the specified event (which must be currently running), delete the specified non-Active input from the dynamic playlist.  | 
| Activate dynamic playlist input | POST | /live\_events/<event ID>/ activate\_input  | In the specified event (which must be currently running), activate the specified dynamic playlist input either at the specified time or immediately. | 
| Prepare dynamic playlist input | POST | /live\_events/<event ID>/ prepare\_input  | In the specified event (which must be currently running), prepare the specified dynamic playlist input and optionally activate encoding at the specified time or immediately.  | 
| Get status | GET | /live\_events/<event ID>status | Gets the status of the specified event, including information about the stage and state of each input. | 