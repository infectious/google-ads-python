# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/services/merchant_center_link_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.resources import merchant_center_link_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_merchant__center__link__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/services/merchant_center_link_service.proto',
  package='google.ads.googleads.v3.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v3.servicesB\036MerchantCenterLinkServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V3.Services\312\002 Google\\Ads\\GoogleAds\\V3\\Services\352\002$Google::Ads::GoogleAds::V3::Services'),
  serialized_pb=_b('\nIgoogle/ads/googleads_v3/proto/services/merchant_center_link_service.proto\x12 google.ads.googleads.v3.services\x1a\x42google/ads/googleads_v3/proto/resources/merchant_center_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\":\n\x1eListMerchantCenterLinksRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\"w\n\x1fListMerchantCenterLinksResponse\x12T\n\x15merchant_center_links\x18\x01 \x03(\x0b\x32\x35.google.ads.googleads.v3.resources.MerchantCenterLink\"j\n\x1cGetMerchantCenterLinkRequest\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\n+googleads.googleapis.com/MerchantCenterLink\"\x92\x01\n\x1fMutateMerchantCenterLinkRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12U\n\toperation\x18\x02 \x01(\x0b\x32=.google.ads.googleads.v3.services.MerchantCenterLinkOperationB\x03\xe0\x41\x02\"\xb6\x01\n\x1bMerchantCenterLinkOperation\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12G\n\x06update\x18\x01 \x01(\x0b\x32\x35.google.ads.googleads.v3.resources.MerchantCenterLinkH\x00\x12\x10\n\x06remove\x18\x02 \x01(\tH\x00\x42\x0b\n\toperation\"t\n MutateMerchantCenterLinkResponse\x12P\n\x06result\x18\x02 \x01(\x0b\x32@.google.ads.googleads.v3.services.MutateMerchantCenterLinkResult\"7\n\x1eMutateMerchantCenterLinkResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x83\x06\n\x19MerchantCenterLinkService\x12\xe7\x01\n\x17ListMerchantCenterLinks\x12@.google.ads.googleads.v3.services.ListMerchantCenterLinksRequest\x1a\x41.google.ads.googleads.v3.services.ListMerchantCenterLinksResponse\"G\x82\xd3\xe4\x93\x02\x33\x12\x31/v3/customers/{customer_id=*}/merchantCenterLinks\xda\x41\x0b\x63ustomer_id\x12\xdd\x01\n\x15GetMerchantCenterLink\x12>.google.ads.googleads.v3.services.GetMerchantCenterLinkRequest\x1a\x35.google.ads.googleads.v3.resources.MerchantCenterLink\"M\x82\xd3\xe4\x93\x02\x37\x12\x35/v3/{resource_name=customers/*/merchantCenterLinks/*}\xda\x41\rresource_name\x12\xfe\x01\n\x18MutateMerchantCenterLink\x12\x41.google.ads.googleads.v3.services.MutateMerchantCenterLinkRequest\x1a\x42.google.ads.googleads.v3.services.MutateMerchantCenterLinkResponse\"[\x82\xd3\xe4\x93\x02=\"8/v3/customers/{customer_id=*}/merchantCenterLinks:mutate:\x01*\xda\x41\x15\x63ustomer_id,operation\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x85\x02\n$com.google.ads.googleads.v3.servicesB\x1eMerchantCenterLinkServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V3.Services\xca\x02 Google\\Ads\\GoogleAds\\V3\\Services\xea\x02$Google::Ads::GoogleAds::V3::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_merchant__center__link__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_LISTMERCHANTCENTERLINKSREQUEST = _descriptor.Descriptor(
  name='ListMerchantCenterLinksRequest',
  full_name='google.ads.googleads.v3.services.ListMerchantCenterLinksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v3.services.ListMerchantCenterLinksRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
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
  serialized_start=328,
  serialized_end=386,
)


_LISTMERCHANTCENTERLINKSRESPONSE = _descriptor.Descriptor(
  name='ListMerchantCenterLinksResponse',
  full_name='google.ads.googleads.v3.services.ListMerchantCenterLinksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='merchant_center_links', full_name='google.ads.googleads.v3.services.ListMerchantCenterLinksResponse.merchant_center_links', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=388,
  serialized_end=507,
)


_GETMERCHANTCENTERLINKREQUEST = _descriptor.Descriptor(
  name='GetMerchantCenterLinkRequest',
  full_name='google.ads.googleads.v3.services.GetMerchantCenterLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.GetMerchantCenterLinkRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A-\n+googleads.googleapis.com/MerchantCenterLink'), file=DESCRIPTOR),
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
  serialized_start=509,
  serialized_end=615,
)


_MUTATEMERCHANTCENTERLINKREQUEST = _descriptor.Descriptor(
  name='MutateMerchantCenterLinkRequest',
  full_name='google.ads.googleads.v3.services.MutateMerchantCenterLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v3.services.MutateMerchantCenterLinkRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='google.ads.googleads.v3.services.MutateMerchantCenterLinkRequest.operation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
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
  serialized_start=618,
  serialized_end=764,
)


_MERCHANTCENTERLINKOPERATION = _descriptor.Descriptor(
  name='MerchantCenterLinkOperation',
  full_name='google.ads.googleads.v3.services.MerchantCenterLinkOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v3.services.MerchantCenterLinkOperation.update_mask', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v3.services.MerchantCenterLinkOperation.update', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v3.services.MerchantCenterLinkOperation.remove', index=2,
      number=2, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v3.services.MerchantCenterLinkOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=767,
  serialized_end=949,
)


_MUTATEMERCHANTCENTERLINKRESPONSE = _descriptor.Descriptor(
  name='MutateMerchantCenterLinkResponse',
  full_name='google.ads.googleads.v3.services.MutateMerchantCenterLinkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='google.ads.googleads.v3.services.MutateMerchantCenterLinkResponse.result', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=951,
  serialized_end=1067,
)


_MUTATEMERCHANTCENTERLINKRESULT = _descriptor.Descriptor(
  name='MutateMerchantCenterLinkResult',
  full_name='google.ads.googleads.v3.services.MutateMerchantCenterLinkResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.MutateMerchantCenterLinkResult.resource_name', index=0,
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
  serialized_start=1069,
  serialized_end=1124,
)

_LISTMERCHANTCENTERLINKSRESPONSE.fields_by_name['merchant_center_links'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_merchant__center__link__pb2._MERCHANTCENTERLINK
_MUTATEMERCHANTCENTERLINKREQUEST.fields_by_name['operation'].message_type = _MERCHANTCENTERLINKOPERATION
_MERCHANTCENTERLINKOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_MERCHANTCENTERLINKOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_merchant__center__link__pb2._MERCHANTCENTERLINK
_MERCHANTCENTERLINKOPERATION.oneofs_by_name['operation'].fields.append(
  _MERCHANTCENTERLINKOPERATION.fields_by_name['update'])
_MERCHANTCENTERLINKOPERATION.fields_by_name['update'].containing_oneof = _MERCHANTCENTERLINKOPERATION.oneofs_by_name['operation']
_MERCHANTCENTERLINKOPERATION.oneofs_by_name['operation'].fields.append(
  _MERCHANTCENTERLINKOPERATION.fields_by_name['remove'])
_MERCHANTCENTERLINKOPERATION.fields_by_name['remove'].containing_oneof = _MERCHANTCENTERLINKOPERATION.oneofs_by_name['operation']
_MUTATEMERCHANTCENTERLINKRESPONSE.fields_by_name['result'].message_type = _MUTATEMERCHANTCENTERLINKRESULT
DESCRIPTOR.message_types_by_name['ListMerchantCenterLinksRequest'] = _LISTMERCHANTCENTERLINKSREQUEST
DESCRIPTOR.message_types_by_name['ListMerchantCenterLinksResponse'] = _LISTMERCHANTCENTERLINKSRESPONSE
DESCRIPTOR.message_types_by_name['GetMerchantCenterLinkRequest'] = _GETMERCHANTCENTERLINKREQUEST
DESCRIPTOR.message_types_by_name['MutateMerchantCenterLinkRequest'] = _MUTATEMERCHANTCENTERLINKREQUEST
DESCRIPTOR.message_types_by_name['MerchantCenterLinkOperation'] = _MERCHANTCENTERLINKOPERATION
DESCRIPTOR.message_types_by_name['MutateMerchantCenterLinkResponse'] = _MUTATEMERCHANTCENTERLINKRESPONSE
DESCRIPTOR.message_types_by_name['MutateMerchantCenterLinkResult'] = _MUTATEMERCHANTCENTERLINKRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListMerchantCenterLinksRequest = _reflection.GeneratedProtocolMessageType('ListMerchantCenterLinksRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTMERCHANTCENTERLINKSREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.merchant_center_link_service_pb2'
  ,
  __doc__ = """Request message for
  [MerchantCenterLinkService.ListMerchantCenterLinks][google.ads.googleads.v3.services.MerchantCenterLinkService.ListMerchantCenterLinks].
  
  
  Attributes:
      customer_id:
          Required. The ID of the customer onto which to apply the
          Merchant Center link list operation.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.ListMerchantCenterLinksRequest)
  ))
_sym_db.RegisterMessage(ListMerchantCenterLinksRequest)

ListMerchantCenterLinksResponse = _reflection.GeneratedProtocolMessageType('ListMerchantCenterLinksResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTMERCHANTCENTERLINKSRESPONSE,
  __module__ = 'google.ads.googleads_v3.proto.services.merchant_center_link_service_pb2'
  ,
  __doc__ = """Response message for
  [MerchantCenterLinkService.ListMerchantCenterLinks][google.ads.googleads.v3.services.MerchantCenterLinkService.ListMerchantCenterLinks].
  
  
  Attributes:
      merchant_center_links:
          Merchant Center links available for the requested customer
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.ListMerchantCenterLinksResponse)
  ))
_sym_db.RegisterMessage(ListMerchantCenterLinksResponse)

GetMerchantCenterLinkRequest = _reflection.GeneratedProtocolMessageType('GetMerchantCenterLinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETMERCHANTCENTERLINKREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.merchant_center_link_service_pb2'
  ,
  __doc__ = """Request message for
  [MerchantCenterLinkService.GetMerchantCenterLink][google.ads.googleads.v3.services.MerchantCenterLinkService.GetMerchantCenterLink].
  
  
  Attributes:
      resource_name:
          Required. Resource name of the Merchant Center link.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.GetMerchantCenterLinkRequest)
  ))
_sym_db.RegisterMessage(GetMerchantCenterLinkRequest)

MutateMerchantCenterLinkRequest = _reflection.GeneratedProtocolMessageType('MutateMerchantCenterLinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEMERCHANTCENTERLINKREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.merchant_center_link_service_pb2'
  ,
  __doc__ = """Request message for
  [MerchantCenterLinkService.MutateMerchantCenterLink][google.ads.googleads.v3.services.MerchantCenterLinkService.MutateMerchantCenterLink].
  
  
  Attributes:
      customer_id:
          Required. The ID of the customer being modified.
      operation:
          Required. The operation to perform on the link
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateMerchantCenterLinkRequest)
  ))
_sym_db.RegisterMessage(MutateMerchantCenterLinkRequest)

MerchantCenterLinkOperation = _reflection.GeneratedProtocolMessageType('MerchantCenterLinkOperation', (_message.Message,), dict(
  DESCRIPTOR = _MERCHANTCENTERLINKOPERATION,
  __module__ = 'google.ads.googleads_v3.proto.services.merchant_center_link_service_pb2'
  ,
  __doc__ = """A single update on a Merchant Center link.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The operation to perform
      update:
          Update operation: The merchant center link is expected to have
          a valid resource name.
      remove:
          Remove operation: A resource name for the removed merchant
          center link is expected, in this format:  ``customers/{custome
          r_id}/merchantCenterLinks/{merchant_center_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MerchantCenterLinkOperation)
  ))
_sym_db.RegisterMessage(MerchantCenterLinkOperation)

MutateMerchantCenterLinkResponse = _reflection.GeneratedProtocolMessageType('MutateMerchantCenterLinkResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEMERCHANTCENTERLINKRESPONSE,
  __module__ = 'google.ads.googleads_v3.proto.services.merchant_center_link_service_pb2'
  ,
  __doc__ = """Response message for Merchant Center link mutate.
  
  
  Attributes:
      result:
          Result for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateMerchantCenterLinkResponse)
  ))
_sym_db.RegisterMessage(MutateMerchantCenterLinkResponse)

MutateMerchantCenterLinkResult = _reflection.GeneratedProtocolMessageType('MutateMerchantCenterLinkResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEMERCHANTCENTERLINKRESULT,
  __module__ = 'google.ads.googleads_v3.proto.services.merchant_center_link_service_pb2'
  ,
  __doc__ = """The result for the Merchant Center link mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateMerchantCenterLinkResult)
  ))
_sym_db.RegisterMessage(MutateMerchantCenterLinkResult)


DESCRIPTOR._options = None
_LISTMERCHANTCENTERLINKSREQUEST.fields_by_name['customer_id']._options = None
_GETMERCHANTCENTERLINKREQUEST.fields_by_name['resource_name']._options = None
_MUTATEMERCHANTCENTERLINKREQUEST.fields_by_name['customer_id']._options = None
_MUTATEMERCHANTCENTERLINKREQUEST.fields_by_name['operation']._options = None

_MERCHANTCENTERLINKSERVICE = _descriptor.ServiceDescriptor(
  name='MerchantCenterLinkService',
  full_name='google.ads.googleads.v3.services.MerchantCenterLinkService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=1127,
  serialized_end=1898,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListMerchantCenterLinks',
    full_name='google.ads.googleads.v3.services.MerchantCenterLinkService.ListMerchantCenterLinks',
    index=0,
    containing_service=None,
    input_type=_LISTMERCHANTCENTERLINKSREQUEST,
    output_type=_LISTMERCHANTCENTERLINKSRESPONSE,
    serialized_options=_b('\202\323\344\223\0023\0221/v3/customers/{customer_id=*}/merchantCenterLinks\332A\013customer_id'),
  ),
  _descriptor.MethodDescriptor(
    name='GetMerchantCenterLink',
    full_name='google.ads.googleads.v3.services.MerchantCenterLinkService.GetMerchantCenterLink',
    index=1,
    containing_service=None,
    input_type=_GETMERCHANTCENTERLINKREQUEST,
    output_type=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_merchant__center__link__pb2._MERCHANTCENTERLINK,
    serialized_options=_b('\202\323\344\223\0027\0225/v3/{resource_name=customers/*/merchantCenterLinks/*}\332A\rresource_name'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateMerchantCenterLink',
    full_name='google.ads.googleads.v3.services.MerchantCenterLinkService.MutateMerchantCenterLink',
    index=2,
    containing_service=None,
    input_type=_MUTATEMERCHANTCENTERLINKREQUEST,
    output_type=_MUTATEMERCHANTCENTERLINKRESPONSE,
    serialized_options=_b('\202\323\344\223\002=\"8/v3/customers/{customer_id=*}/merchantCenterLinks:mutate:\001*\332A\025customer_id,operation'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MERCHANTCENTERLINKSERVICE)

DESCRIPTOR.services_by_name['MerchantCenterLinkService'] = _MERCHANTCENTERLINKSERVICE

# @@protoc_insertion_point(module_scope)
