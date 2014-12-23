# -*- coding: utf-8 -*-
from django.db import models
from south.db import db
from south.utils import datetime_utils as datetime
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Status.replies_count'
        db.add_column(u'twitter_api_status', 'replies_count',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Status.replies_count'
        db.delete_column(u'twitter_api_status', 'replies_count')

    models = {
        u'twitter_api.status': {
            'Meta': {'object_name': 'Status'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'to': u"orm['twitter_api.User']"}),
            'contributors': ('annoying.fields.JSONField', [], {'null': 'True'}),
            'coordinates': ('annoying.fields.JSONField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'entities': ('annoying.fields.JSONField', [], {}),
            'favorited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'favorites_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'geo': ('annoying.fields.JSONField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'in_reply_to_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'replies'", 'null': 'True', 'to': u"orm['twitter_api.Status']"}),
            'in_reply_to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'replies'", 'null': 'True', 'to': u"orm['twitter_api.User']"}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'place': ('annoying.fields.JSONField', [], {'null': 'True'}),
            'replies_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': 'None', 'null': 'True'}),
            'retweeted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'retweeted_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'retweets'", 'null': 'True', 'to': u"orm['twitter_api.Status']"}),
            'retweets_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'truncated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'twitter_api.user': {
            'Meta': {'object_name': 'User'},
            'contributors_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'default_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default_profile_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'entities': ('annoying.fields.JSONField', [], {}),
            'favorites_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'follow_request_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'followings'", 'symmetrical': 'False', 'to': u"orm['twitter_api.User']"}),
            'followers_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'following': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'friends_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'geo_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'is_translator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'listed_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notifications': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profile_background_color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'profile_background_image_url': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'profile_background_image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'profile_background_tile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profile_banner_url': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'profile_image_url': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'profile_image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'profile_link_color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'profile_sidebar_border_color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'profile_sidebar_fill_color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'profile_text_color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'profile_use_background_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'statuses_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '300', 'null': 'True'}),
            'utc_offset': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['twitter_api']
