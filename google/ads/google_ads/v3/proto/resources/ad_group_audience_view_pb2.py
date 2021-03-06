# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/ad_group_audience_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/ad_group_audience_view.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\030AdGroupAudienceViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\nDgoogle/ads/googleads_v3/proto/resources/ad_group_audience_view.proto\x12!google.ads.googleads.v3.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xd9\x01\n\x13\x41\x64GroupAudienceView\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0\x41\x03\xfa\x41.\n,googleads.googleapis.com/AdGroupAudienceView:u\xea\x41r\n,googleads.googleapis.com/AdGroupAudienceView\x12\x42\x63ustomers/{customer}/adGroupAudienceViews/{ad_group_audience_view}B\x85\x02\n%com.google.ads.googleads.v3.resourcesB\x18\x41\x64GroupAudienceViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPAUDIENCEVIEW = _descriptor.Descriptor(
  name='AdGroupAudienceView',
  full_name='google.ads.googleads.v3.resources.AdGroupAudienceView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.AdGroupAudienceView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003\372A.\n,googleads.googleapis.com/AdGroupAudienceView'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352Ar\n,googleads.googleapis.com/AdGroupAudienceView\022Bcustomers/{customer}/adGroupAudienceViews/{ad_group_audience_view}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=415,
)

DESCRIPTOR.message_types_by_name['AdGroupAudienceView'] = _ADGROUPAUDIENCEVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupAudienceView = _reflection.GeneratedProtocolMessageType('AdGroupAudienceView', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPAUDIENCEVIEW,
  __module__ = 'google.ads.googleads_v3.proto.resources.ad_group_audience_view_pb2'
  ,
  __doc__ = """An ad group audience view. Includes performance data from interests and
  remarketing lists for Display Network and YouTube Network ads, and
  remarketing lists for search ads (RLSA), aggregated at the audience
  level.
  
  
  Attributes:
      resource_name:
          Output only. The resource name of the ad group audience view.
          Ad group audience view resource names have the form:  ``custom
          ers/{customer_id}/adGroupAudienceViews/{ad_group_id}~{criterio
          n_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.AdGroupAudienceView)
  ))
_sym_db.RegisterMessage(AdGroupAudienceView)


DESCRIPTOR._options = None
_ADGROUPAUDIENCEVIEW.fields_by_name['resource_name']._options = None
_ADGROUPAUDIENCEVIEW._options = None
# @@protoc_insertion_point(module_scope)
