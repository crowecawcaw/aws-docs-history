

# Rules

Rules control which streams the output transport stream carries, and on which PIDs. Each rule has a **Match expression**, which selects streams, and an **Action**, which defines the action that MediaConnect applies to the selected streams. For each elementary stream that the Program Map Table (PMT) lists, MediaConnect:

1. Checks the rules in order.

1. Applies the action of the first rule that matches, and skips the remaining rules.

1. Applies the **Default action** if no rule matches.

You write match expressions and actions as short text expressions. In the console, you can also choose common ones from a list. Match expressions and actions are case-sensitive, so write them exactly as shown in the following tables.

## Match expressions
<a name="pid-remapping-match-expressions"></a>


| Match expression | Parameter | Selects | 
| --- | --- | --- | 
| `type` | `video`, `audio`, or `metadata` | The streams of that type, for example `type(audio)`. | 
| `pid` | A PID | The stream on that PID, for example `pid(100)`. | 
| `index` | A stream type and a position, counting from 0 | The stream at that position among the streams of that type, in order of PID number. For example, `index(audio, 0)` selects the audio stream with the lowest PID. | 
| `language` | One or more language codes | The streams whose language matches one of the codes, for example `language(eng, spa)`. If the PMT doesn't list a language for a stream, MediaConnect never selects that stream with a `language` expression. | 

You can combine match expressions using the logical operators `&&` (and), `||` (or), and `!` (not) to create advanced match expressions. For example, `type(audio) && !language(eng)` selects the audio streams that aren't in English. MediaConnect applies `!` first, then `&&`, and then `||`. Use parentheses to group expressions.

**Note**  
Keep the following in mind when you write match expressions:  
Each match expression can have up to 256 characters and up to 4 levels of nesting.
In the MediaConnect console, the **Language** option accepts three-letter language codes. To match a language value in a different format, choose **Custom** and enter the value in double quotes.
In the MediaConnect console, to define advanced match expressions, choose **Custom** for **Match expression**.

## Actions
<a name="pid-remapping-actions"></a>


| Action | Parameter | What it does | 
| --- | --- | --- | 
| `pass` | None | Keeps the stream on its input PID. | 
| `null` | None | Replaces the stream's packets with null packets. The output bitrate and packet timing stay the same. | 
| `drop` | None | Removes the stream's packets. The output bitrate goes down, and the packet timing changes. | 
| `mapPid` | A PID | Moves the stream to that PID, for example `mapPid(256)`. | 
| `mapPidRange` | First and last PID | Moves the matching streams to the PIDs in that range, in order of stream type (video, audio, and then metadata) and then PID number. For example, `mapPidRange(257, 271)`. | 
| `mapAuto` | None | Moves the stream to the next free PID in the auto map range, in the same order across all streams that use `mapAuto`. The **Starting PID** and **PIDs per program** in **Auto map settings** set the range, which by default starts at PID 512 and has 32 PIDs. | 

**Note**  
If the PID is already in use or the range is full, MediaConnect drops the stream.