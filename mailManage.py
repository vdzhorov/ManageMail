import imapclient
from sys import exit


class MailManage:
    def __init__(self, server, username, password, ssl=True, folder="INBOX"):
        try:
            self.conn = imapclient.IMAPClient(server, ssl=bool(ssl))
        except:
            raise Exception("Uname to connect to server.")
            exit(1)

        try:
            self.conn.login(username, password)
        except imapclient.exceptions.LoginError:
            raise Exception("Login failed.")
            sys.exit(1)

        try:
            self.conn.select_folder(folder)
        except:
            raise Exception(f"Unable to select folder {folder}")

    def delete_mails_since(self, delete_since):
        uids = self.conn.search(["SINCE", delete_since])
        if len(uids) <= 0:
            raise Exception(f"Found no mails since date {delete_since}")
        else:
            self.conn.delete_messages(uids)
            self.conn.expunge(uids)
            print(f"Successfully deleted messages since {delete_since}")
            self.conn.logout()

    def delete_mails_before(self, delete_before):
        uids = self.conn.search(["BEFORE", delete_before])
        if len(uids) <= 0:
            raise Exception(f"Found no mails before date {delete_before}")
        else:
            self.conn.delete_messages(uids)
            self.conn.expunge(uids)
            print(f"Successfully deleted messages before {delete_before}")
            self.conn.logout()
