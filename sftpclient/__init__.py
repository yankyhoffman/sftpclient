from contextlib import contextmanager, suppress
from io import TextIOWrapper
from tempfile import TemporaryFile

import pysftp


class SFTPClient:
    """
        Username/Password SFTP Client class

        Args:
            `host`: Remote SFTP hostname.
            `username`: Username to authenticate with at the remote SFTP server.
            `password`: Password to authenticate with at the remote SFTP server.
            `use_known_hosts`: Set to `False` to disable server public key
                checking (use with caution).
    """
    def __init__(self, host, username, password, use_known_hosts=True):
        self._host = host
        self._username = username
        self._password = password
        self._cnopts = pysftp.CnOpts()
        if not use_known_hosts:
            self._cnopts.hostkeys = None

    @contextmanager
    def _connect(self):
        """
            Connect and authenticate with the SFTP server.
            Automatically closes the connection when done.
        """
        with pysftp.Connection(
            host=self._host,
            username=self._username,
            password=self._password,
            cnopts=self._cnopts,
        ) as conn:
            yield conn

    def upload(self, filehandle, destination='/'):
        """
            Upload `filehandle` contents to `destination` path on remote SFTP server.
        """
        with self._connect() as conn:
            with suppress(OSError):
                # OSErrors have been observed when passing non-ascii characters
                # even though the upload was successful.
                conn.putfo(flo=filehandle, remotepath=destination)

    def download(self, filepath, *, text=False):
        """
            Download contents of file at `filepath` (read as bytes) on remote
            SFTP server.

            Pass `text=True` to return a file readable as text.
        """
        tf = TemporaryFile(mode='w+b')
        with self._connect() as conn:
            conn.getfo(remotepath=filepath, flo=tf)
        # reset the filehandle cursor to the start fo the file.
        tf.seek(0)

        if text:
            return TextIOWrapper(tf)
        return tf
