# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: username_proof.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14username_proof.proto\"|\n\rUserNameProof\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\x0c\x12\r\n\x05owner\x18\x03 \x01(\x0c\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12\x0b\n\x03\x66id\x18\x05 \x01(\x04\x12\x1b\n\x04type\x18\x06 \x01(\x0e\x32\r.UserNameType*Y\n\x0cUserNameType\x12\x16\n\x12USERNAME_TYPE_NONE\x10\x00\x12\x17\n\x13USERNAME_TYPE_FNAME\x10\x01\x12\x18\n\x14USERNAME_TYPE_ENS_L1\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'username_proof_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USERNAMETYPE']._serialized_start=150
  _globals['_USERNAMETYPE']._serialized_end=239
  _globals['_USERNAMEPROOF']._serialized_start=24
  _globals['_USERNAMEPROOF']._serialized_end=148
# @@protoc_insertion_point(module_scope)
