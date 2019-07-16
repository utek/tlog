Simple tool to log work on Tempo
---------------------------------

# Usage

Create .tlog file in your HOMEDIR and provide following values there

```
[default]
API_KEY = <your api key for tempo>
USER_ID = <your jira user id>
```

Now you can use use tool as

`> tlog <issue number> <time> <message>`

for example:

`> tlog abc-123 1:40 My message`

This will add the work on issue ABC-123 for 1 hour and 40 minutes with description "My message"
