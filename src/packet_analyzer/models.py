from dataclasses import dataclass


@dataclass
class Packet:
    """
    Represents a parsed packet according to the project protocol.
    """

    sof: int
    version: int
    message_type: int
    flags: int
    payload_length: int
    sequence: int
    payload: bytes
    crc: int