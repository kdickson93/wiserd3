import os
from django.contrib.gis.geos import GEOSGeometry
from django.db import OperationalError, IntegrityError
from django.db import connection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wiserd3.settings")
import django
django.setup()
from dataportal3.utils.ReadQual import ReadQual
import json
import pprint

__author__ = 'ubuntu'

from old_qual import models as old_qual_models
from dataportal3 import models as new_qual_models


class CreateQualTables():

    def __init__(self):
        self.rq = ReadQual()

    def check_old(self):
        for old_qual_dc in old_qual_models.DcInfo.objects.all()[:1]:

            for model_field in old_qual_models.DcInfo._meta.get_fields():
                print '\n'

                print '***', model_field.name

                try:
                    o = getattr(old_qual_dc, model_field.name)
                    print model_field.name, ':\n', type(o), ':\n', o
                except Exception as e24:
                    print 'error24', e24

            # print pprint.pformat(self.rq.get_coverage_items(old_qual_dc['coverage']))
            try:
                calais_text = old_qual_dc.calais.strip().rstrip(',')
                calais_text = '{"data": [' + calais_text + ']}'
                print '*' + calais_text + '*'
                calais_object = json.loads(calais_text, strict=False)
                # print pprint.pformat(calais_object)
            except Exception as e:
                print 'error', e

            try:
                calais_text = old_qual_dc.words.strip().rstrip(',')
                calais_text = '{"data": [' + calais_text + ']}'
                print '*' + calais_text + '*'
                calais_object = json.loads(calais_text, strict=False)
                # print pprint.pformat(calais_object)
            except Exception as e:
                print 'error', e

    def get_word_usages(self, words):

        words_text = words.strip().rstrip(',')
        words_text = '{"data": [' + words_text + ']}'
        # print '*' + words_text + '*'
        words_object = json.loads(words_text, strict=False)

        word_dict = {}
        for word in words_object['data']:
            try:
                word_dict[word['word']] = word['count']
            except Exception as e984273:
                print e984273, word
        return word_dict

    def get_geom(self, geom_string):
        print type(geom_string), geom_string[:3]
        if geom_string[:3] == 'SRID':
            srid_split = geom_string[geom_string.index(';')]
            print srid_split[0]
            print srid_split[1]

            geom = GEOSGeometry(srid_split[1], srid=srid_split[0])
            return geom
        else:
            raise

    def full_copy(self):

        errors = []

        to_save = []
        for old_qual_dc in old_qual_models.DcInfo.objects.all():
            # q_dc_info = new_qual_models.QualDcInfo()

            q_dc_info, created = new_qual_models.QualDcInfo.objects.get_or_create(
                identifier=old_qual_dc.identifier.strip()
            )

            q_dc_info.identifier = old_qual_dc.identifier.strip()
            q_dc_info.title = old_qual_dc.title.strip()
            q_dc_info.creator = old_qual_dc.creator.strip()
            q_dc_info.subject = old_qual_dc.subject.strip()
            q_dc_info.description = old_qual_dc.description.strip()
            q_dc_info.publisher = old_qual_dc.publisher.strip()
            q_dc_info.contributor = old_qual_dc.contributor.strip()
            q_dc_info.date = old_qual_dc.date
            q_dc_info.type = old_qual_dc.type.strip()
            q_dc_info.format = old_qual_dc.format.strip()
            q_dc_info.source = old_qual_dc.source.strip()
            q_dc_info.language = old_qual_dc.language.strip()
            q_dc_info.relation = old_qual_dc.relation.strip()

            # coverage_object = self.rq.get_coverage_items(old_qual_dc.coverage)
            # q_dc_info.coverage = coverage_object

            q_dc_info.rights = old_qual_dc.rights.strip()
            q_dc_info.user_id = old_qual_dc.user_id
            q_dc_info.created = old_qual_dc.created

            words_arr = self.get_word_usages(old_qual_dc.words)
            # print pprint.pformat(words_arr, indent=4)
            q_dc_info.words = words_arr

            q_dc_info.calais = str(old_qual_dc.calais).strip()

            q_dc_info.vern_geog = old_qual_dc.vern_geog.strip()

            q_dc_info.tier = old_qual_dc.tier

            # geom_string = old_qual_dc.the_geom
            # print geom_string
            # geom = self.get_geom(geom_string)
            q_dc_info.the_geom = old_qual_dc.the_geom

            q_dc_info.save()

            # if thematics:
            q_dc_info.thematic_group = old_qual_dc.thematic_group
            if len(old_qual_dc.thematic_group.strip()):
                for tg in old_qual_dc.thematic_group.strip().split(','):
                    try:
                        tg_model = new_qual_models.ThematicGroup.objects.get(grouptitle=tg.strip())
                        # print tg_model.__dict__
                        q_dc_info.thematic_groups_set.add(tg_model)
                    except Exception as e:
                        print e, tg.strip()

            q_dc_info.save()

            calais_objects = self.rq.get_calais_object(old_qual_dc.calais)
            for calais_object in calais_objects['data']:
                calais_model = new_qual_models.QualCalais()
                calais_model.value = calais_object['Value'].strip()
                calais_model.opencalais = calais_object['ID'].strip()
                try:
                    lat = float(calais_object['lat'])
                    lon = float(calais_object['lon'])
                    calais_model.geo_point = GEOSGeometry('POINT(%s %s)' % (calais_object['lat'], calais_object['lon']))
                    calais_model.lat = calais_object['lat']
                    calais_model.lon = calais_object['lon']
                except Exception as e789432:
                    # print e789432
                    pass
                calais_model.tagName = calais_object['tagName'].strip()
                calais_model.count = calais_object['Count']

                calais_model.qual_dc = q_dc_info
                calais_model.save()

        # new_qual_models.QualDcInfo.objects.bulk_create(to_save)

        for old_qual_trans in old_qual_models.TranscriptData.objects.all():
            q_trans, created = new_qual_models.QualTranscriptData.objects.get_or_create(
                identifier=old_qual_trans.id.strip()
            )

            q_trans.identifier = old_qual_trans.id.strip()
            q_trans.rawtext = old_qual_trans.rawtext.strip()
            q_trans.pages = old_qual_trans.pages
            q_trans.errors = old_qual_trans.errors.strip()

            try:
                qual_trans_dc = new_qual_models.QualDcInfo.objects.get(identifier=old_qual_trans.id.strip())
                q_trans.dc_info = qual_trans_dc
            except:
                errors.append('dc ' + str(old_qual_trans.id.strip()) + ' not found')
                print 'dc ' + str(old_qual_trans.id.strip()) + ' not found'
                pass

            try:
                q_trans.save()

                stats_objects = self.rq.read_trans_stats(old_qual_trans.stats)
                for stats in stats_objects:
                    stats_model = new_qual_models.QualStats()
                    stats_model.name = stats['name']
                    stats_model.page_counts = stats['page_counts']
                    stats_model.transcript_data = q_trans

                    stats_model.save()
            except IntegrityError as ie:
                print ie

        print errors


# thematics = False
quals = CreateQualTables()
# quals.check_old()
quals.full_copy()