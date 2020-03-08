# Simple Username/Password based SFTP Client.

`sftpclient` is a simple to use sftp client to connect to remote FTP servers over ssh (SFTP) using username/password combo.

Uploads and downloads work with file-handles by default so as to not fill up the working directory with downloaded files when the desire was just to read and parse the data available at the remote server.

Default downloads are in `bytes` mode `mode=rb`, use an `io.TextIOWrapper` to read the file as text.

Sample usage

``` python
from sftpclient import SFTPClient


# create client instance.
client = SFTPClient(
    host=SFTPHOST,
    username=YOURSFTPUSERNAME,
    password=YOURSFTPPASSWORD,
    use_known_hosts=UPTOYOUTODECIDE,
)

# Uploading files;
# 1. open a file (or use a `tempfile.TemporaryFile`).
with open('somefile') as file_to_upload:
    # 2. use the `SFTPClient` `upload` method to pass the open file handle to
    # the remote `destination`.
    client.upload(file_to_upload, destination='/uploads')

# Downloading files;
file = client.download('/data/consume.txt', text=True)
# use `text=True` when downloading text files, default is `bytes` mode.
for line in file:
    # continue with processing the file as desired, or just write it out to
    # local disk.
