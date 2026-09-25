\# Packet Protocol Specification



\## 1. Overview



This document defines the generic binary packet format used by the Python Packet Analyzer project.



The protocol is designed for demonstrating packet parsing, validation, decoding, CRC verification and automated testing.



\## 2. Packet Structure



```text

+--------+---------+------+-------+--------------+--------+---------+-------+

| SOF    | VERSION | TYPE | FLAGS | PAYLOAD LEN  | SEQ    | PAYLOAD | CRC32 |

| 1 Byte | 1 Byte  |1 Byte|1 Byte | 2 Bytes      |2 Bytes | N Bytes |4 Bytes|

+--------+---------+------+-------+--------------+--------+---------+-------+

## 3. Byte Order

Multi-byte fields use Little Endian byte order.

- Payload Length: 2 bytes
- Sequence Number: 2 bytes
- CRC32: 4 bytes

## 4. Field Definition

| Field | Size | Description |
|---|---:|---|
| SOF | 1 byte | Start of Frame |
| VERSION | 1 byte | Protocol version |
| TYPE | 1 byte | Message type |
| FLAGS | 1 byte | Control flags |
| PAYLOAD LENGTH | 2 bytes | Payload size in bytes |
| SEQUENCE | 2 bytes | Packet sequence number |
| PAYLOAD | N bytes | Application data |
| CRC32 | 4 bytes | Integrity check |

## 5. SOF

The Start of Frame value is:

```text
0xAA