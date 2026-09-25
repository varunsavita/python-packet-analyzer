from src.packet_analyzer.models import Packet


def test_packet_creation():
    packet = Packet(
        sof=0xAA,
        version=0x01,
        message_type=0x01,
        flags=0x00,
        payload_length=4,
        sequence=1,
        payload=b"\x10\x20\x30\x40",
        crc=0x12345678,
    )

    assert packet.sof == 0xAA
    assert packet.version == 0x01
    assert packet.message_type == 0x01
    assert packet.flags == 0x00
    assert packet.payload_length == 4
    assert packet.sequence == 1
    assert packet.payload == b"\x10\x20\x30\x40"
    assert packet.crc == 0x12345678