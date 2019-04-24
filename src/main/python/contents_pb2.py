# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contents.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contents.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x63ontents.proto\"\x14\n\x04\x46ood\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x18\n\x08\x46oodResp\x12\x0c\n\x04name\x18\x01 \x01(\t2)\n\x08\x43ontents\x12\x1d\n\x07\x41\x64\x64\x46ood\x12\x05.Food\x1a\t.FoodResp\"\x00\x62\x06proto3')
)




_FOOD = _descriptor.Descriptor(
  name='Food',
  full_name='Food',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Food.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=38,
)


_FOODRESP = _descriptor.Descriptor(
  name='FoodResp',
  full_name='FoodResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='FoodResp.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=64,
)

DESCRIPTOR.message_types_by_name['Food'] = _FOOD
DESCRIPTOR.message_types_by_name['FoodResp'] = _FOODRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Food = _reflection.GeneratedProtocolMessageType('Food', (_message.Message,), dict(
  DESCRIPTOR = _FOOD,
  __module__ = 'contents_pb2'
  # @@protoc_insertion_point(class_scope:Food)
  ))
_sym_db.RegisterMessage(Food)

FoodResp = _reflection.GeneratedProtocolMessageType('FoodResp', (_message.Message,), dict(
  DESCRIPTOR = _FOODRESP,
  __module__ = 'contents_pb2'
  # @@protoc_insertion_point(class_scope:FoodResp)
  ))
_sym_db.RegisterMessage(FoodResp)



_CONTENTS = _descriptor.ServiceDescriptor(
  name='Contents',
  full_name='Contents',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=66,
  serialized_end=107,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddFood',
    full_name='Contents.AddFood',
    index=0,
    containing_service=None,
    input_type=_FOOD,
    output_type=_FOODRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTENTS)

DESCRIPTOR.services_by_name['Contents'] = _CONTENTS

# @@protoc_insertion_point(module_scope)