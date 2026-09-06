

# Add dynamic playlist inputs
<a name="add-dynamic-playlist-inputs"></a>

In the specified event (which must be currently running), add the specified input or inputs (maximum 29 inputs for a total of 30, including the Active input) to the end of the dynamic playlist. 

## HTTP request and response
<a name="add-dynamic-playlist-http-request-and-response"></a>

### HTTP URL
<a name="add-dynamic-playlist-http-url"></a>

```
POST http://<Live IP address>/live_events/<event ID>/inputs
```

### Body of HTTP
<a name="add-dynamic-playlist-body-of-http"></a>

XML content consisting of one:
+ One inputs element that contains:
  + One or more input elements that each contains one or more of the regular input tags. See [Elements and tags in an event input XML](elements-and-tags.md).

### Tips for elements and tags
<a name="add-dynamic-playlist-tips-for-elements-and-tags"></a>

Here are some notes about tags of particular interest:
+ input\_label: It is recommended that you include the input\_label tag. If you include this tag, you can reference the input later on using this label (rather than using the input ID, which you first have to query for using Get Event).

  An input label must be unique among all the inputs in the event when you add inputs – the existing inputs and the new inputs. 

  If you add an input with label X and later remove the input, you can add another input with label X, even if the input actually has different content. Elemental Live does not track the content, it just enforces the rule for label uniqueness at a given time.
+ loop\_source: This tag can be used to loop the dynamic playlist. If you set this tag to true for input X, it is a good idea to set an activate time for the next intended input, otherwise input X will process forever. See [Activating using placeholders](general-procedure.md#activating-using-placeholders) for a typical use case for loop\_source. 

  When this tag is true and Elemental Live is at the last input listed in the event XML, the first input in the dynamic playlist may be considered as the Next-in-line input.
+ order: This tag is ignored in determining the dynamic playlist order.
+ For the input source, include one of: network\_input or device\_input or router\_input or file\_input. Different inputs can have a different source.
+ audio\_selector, caption\_selector: All inputs must have the same number of these elements: none or more than one. So if the first input has two audio\_selector elements, all inputs must have two audio\_selectors. This rule applies to the lifetime of the event: as soon as it starts, the count of audio\_selector and caption\_selectors is fixed and cannot vary.
+ input\_clipping: Can be used to process only a specific section of a live or file input.

### Response
<a name="add-dynamic-playlist-response"></a>

200 OK for a successful request.

## Example
<a name="add-dynamic-playlist-example"></a>

This request adds two inputs to the event with the ID 31. The first input is a live input, the second is a file input.

```
POST http://10.4.136.92/live_events/31/inputs
---------------------------------------------
<inputs>
  <input>
    <input_label>movie08E45_section_1</input_label>
    <loop_source>false</loop_source>
    <network_input>
      <quad>false</quad>
      <uri>udp://10.0.0.1:5005</uri>
    </network_input>
    <audio_selector>
      <default_selection>true</default_selection>
      <track>1</track>
    </audio_selector>
  </input>
  <input>
    <input_label>enigmatic_car_ad</input_label>
    <loop_source></loop_source>
    <file_input>
      <uri>/data/server/ad13978.mp4</uri>
    </file_input>
    <audio_selector>
      <default_selection>true</default_selection>
      <track>1</track>
    </audio_selector>
  </input>
</inputs>
```