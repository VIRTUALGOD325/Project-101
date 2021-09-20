from os import *
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def file_upload(self, file_from, file_to):
        db = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            db.files_upload(f.read(), file_to)

def main():
    access_token = 'XoCgXDHO3boAAAAAAAAAAVo4OrWeNxHZD18__qDcDWvM2jpN8lh3O_wvAgrwjT-m'
    transferData = TransferData(access_token)

    file_from = input('ENTER THE FILE/PATH TO BE UPLOADED ON DROPBOX')
    file_to = input('GIVE THE LOCATION TO UPLOAD THE FILE')
    file_to = "/test/"+file_to

    transferData.file_upload(file_from,file_to)
    print("THE FILE HAS BEEN UPLOADED SUCCESSFULLY")

main()  