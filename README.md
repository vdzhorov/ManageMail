# ManageMail
Really simple Python script for automated mail operations

## Usage and examples

Authenticating to mailbox:

```
from mailManage import MailManage

new_mail = MailManage('mail.server.com', 'username@mail.com', 'mymailpassword')
```

Deleting mails BEFORE date:

```
from datetime import datetime

new_mail.delete_mails_before(datetime(2021, 5, 17)) # Deletes mails before 2021-05-17
```

Deleting mails SINCE date:

```
from datetime import datetime

new_mail.delete_mails_since(datetime(2021, 5, 17)) # Deletes mails since 2021-05-17
```

Deleting mails SINCE date on non-default folder("INBOX")

```
from mailManage import MailManage

new_mail = MailManage('mail.server.com', 'username@mail.com', 'mymailpassword', ssl=True, folder="custom_folder") # "custom_folder" must exist on the remote mail server
```
