import dropbox
class TransferData:
    def __init__(self,token):
        self.token=token
    def uploadFile(self,source,destination):
        dbx=dropbox.Dropbox(self.token)
        file=open(source,"rb")
        dbx.files_upload(file.read(),destination)
def main():
    token="sl.BJRM-j5lRY6rCuDv8qKLN4doiVniJfsh9qcezCm9og_toj0E4qQEFdC4wWYnBpFhb6yweAzZ_FEKnCFHXP_JqbOnkCQXBQ6aLigpdT4V05o139lffazWDvRhn28ICRnF2QbjX8ijuY0"
    transferData=TransferData(token)
    source=input("enter the file path to transfer=")
    destination=input("enter the path to the dropbox=")
    transferData.uploadFile(source,destination)
    print("file has been moved ")
main()
