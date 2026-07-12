This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Modify saved item in room

Wickr generates this message when a file is saved, renamed, moved, or deleted in a
room's Saved Items (File Vault). The **filevaultinfo** object describes
the action taken.

```
{
  "control": {
    "bor": 0,
    "changemask": 64,
    "description": "",
    "filevaultinfo": {
      "filehash": "4eab763c5f3211ca93966a...d3e461c27f5432c1",
      "guid": "D094F147-0490-4A14-9A65-6F23C896A8B4",
      "key": "EXAMPLEKEY...",
      "domain": "messaging.wickr.us-gov-west-1.amazonaws.com",
      "filemgtaction": {
        "action": "save",
        "target": "file",
        "name": "report.pdf",
        "path": "/shared",
        "modifiedbyuser": "user001",
        "modifiedtimestamp": "2026-06-22 09:43:44"
      }
    },
    "masters": ["user002", "user001"],
    "members": ["user002", "user001"],
    "msgtype": 4004,
    "title": "Project Files",
    "ttl": 2592000
  },
  "message_id": "c3cb62e08dff11eab641a549111a64cb",
  "msg_ts": "1588594022.000000",
  "msgtype": 4004,
  "sender": "user001",
  "sender_type": "normal",
  "time": "5/4/20 3:07 PM",
  "time_iso": "2020-05-04 15:07:02.000",
  "vgroupid": "S243f2ec645d3961bdd531f51f3244205d292b8d0fbd41802827746271d31d41"
}
```

The **filemgtaction** action field can have the following
values.

| Action | Description                   |
| ------ | ----------------------------- |
| create | A new folder was created.     |
| upload | A file was uploaded.          |
| save   | A file was saved.             |
| rename | A file or folder was renamed. |
| move   | A file or folder was moved.   |
| delete | A file or folder was deleted. |
