"""TLS communication."""
import logging

from pymodbus.client.asynchronous.async_io import (
    init_tls_client,
    ReconnectingAsyncioModbusTlsClient,
)
from pymodbus.constants import Defaults
from pymodbus.factory import ClientDecoder
from pymodbus.transaction import ModbusTlsFramer

_logger = logging.getLogger(__name__)


class AsyncModbusTLSClient(ReconnectingAsyncioModbusTlsClient):
    """Actual Async TLS Client to be used.

    To use do::
        from pymodbus.client.asynchronous.tls import AsyncModbusTLSClient
    """

    def __new__(
        cls,
        host="127.0.0.1",
        port=Defaults.TLSPort,
        framer=None,
        sslctx=None,
        server_hostname=None,
        **kwargs
    ):
        """Do setup of client.

        :param host: Target server"s name, also matched for certificate
        :param port: Port
        :param framer: Modbus Framer to use
        :param sslctx: The SSLContext to use for TLS (default None and auto create)
        :param certfile: The optional client"s cert file path for TLS server request
        :param keyfile: The optional client"s key file path for TLS server request
        :param password: The password for for decrypting client"s private key file
        :param source_address: source address specific to underlying backend
        :param timeout: Time out in seconds
        :param kwargs: Other extra args specific to Backend being used
        :return:
        """
        framer = framer or ModbusTlsFramer(ClientDecoder())
        proto_cls = kwargs.pop("proto_cls", None)

        client = init_tls_client(
            proto_cls, host, port, sslctx, server_hostname, framer, **kwargs
        )
        return client
