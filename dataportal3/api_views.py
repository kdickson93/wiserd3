from dataportal3.models import *
from dataportal3.serializer import *
from rest_framework import viewsets


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserPreferencesViewSet(viewsets.ModelViewSet):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer


class DcInfoViewSet(viewsets.ModelViewSet):
    queryset = DcInfo.objects.all()
    serializer_class = DcInfoSerializer


class DublincoreFormatViewSet(viewsets.ModelViewSet):
    queryset = DublincoreFormat.objects.all()
    serializer_class = DublincoreFormatSerializer


class DublincoreLanguageViewSet(viewsets.ModelViewSet):
    queryset = DublincoreLanguage.objects.all()
    serializer_class = DublincoreLanguageSerializer


class DublincoreTypeViewSet(viewsets.ModelViewSet):
    queryset = DublincoreType.objects.all()
    serializer_class = DublincoreTypeSerializer


class ThematicGroupViewSet(viewsets.ModelViewSet):
    queryset = ThematicGroup.objects.all()
    serializer_class = ThematicGroupSerializer


class ThematicTagViewSet(viewsets.ModelViewSet):
    queryset = ThematicTag.objects.all()
    serializer_class = ThematicTagSerializer


class QTypeViewSet(viewsets.ModelViewSet):
    queryset = QType.objects.all()
    serializer_class = QTypeSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ResponseTypeViewSet(viewsets.ModelViewSet):
    queryset = ResponseType.objects.all()
    serializer_class = ResponseTypeSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class RouteTypeViewSet(viewsets.ModelViewSet):
    queryset = RouteType.objects.all()
    serializer_class = RouteTypeSerializer


class SpatialLevelViewSet(viewsets.ModelViewSet):
    queryset = SpatialLevel.objects.all()
    serializer_class = SpatialLevelSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SurveyFrequencyViewSet(viewsets.ModelViewSet):
    queryset = SurveyFrequency.objects.all()
    serializer_class = SurveyFrequencySerializer


class SurveyQuestionsLinkViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestionsLink.objects.all()
    serializer_class = SurveyQuestionsLinkSerializer


class SpatialSurveyLinkViewSet(viewsets.ModelViewSet):
    queryset = SpatialSurveyLink.objects.all()
    serializer_class = SpatialSurveyLinkSerializer


class SurveySpatialLinkViewSet(viewsets.ModelViewSet):
    queryset = SurveySpatialLink.objects.all()
    serializer_class = SurveySpatialLinkSerializer


class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer


class ShapeFileUploadViewSet(viewsets.ModelViewSet):
    queryset = ShapeFileUpload.objects.all()
    serializer_class = ShapeFileUploadSerializer


class FeatureCollectionStoreViewSet(viewsets.ModelViewSet):
    queryset = FeatureCollectionStore.objects.all()
    serializer_class = FeatureCollectionStoreSerializer


class FeatureStoreViewSet(viewsets.ModelViewSet):
    queryset = FeatureStore.objects.all()
    serializer_class = FeatureStoreSerializer


class NomisSearchViewSet(viewsets.ModelViewSet):
    queryset = NomisSearch.objects.all()
    serializer_class = NomisSearchSerializer
    filter_fields = ('user', 'search_type', 'uuid')


# class Aberystwyth_Locality_DissolvedViewSet(viewsets.ModelViewSet):
#     queryset = Aberystwyth_Locality_Dissolved.objects.all()
#     serializer_class = Aberystwyth_Locality_DissolvedSerializer
#
#
# class Bangor_Locality_DissolvedViewSet(viewsets.ModelViewSet):
#     queryset = Bangor_Locality_Dissolved.objects.all()
#     serializer_class = Bangor_Locality_DissolvedSerializer
#
#
# class Heads_of_the_ValleysViewSet(viewsets.ModelViewSet):
#     queryset = Heads_of_the_Valleys.objects.all()
#     serializer_class = Heads_of_the_ValleysSerializer


class QualDcInfoViewSet(viewsets.ModelViewSet):
    queryset = QualDcInfo.objects.all()
    serializer_class = QualDcInfoSerializer


class QualCalaisViewSet(viewsets.ModelViewSet):
    queryset = QualCalais.objects.all()
    serializer_class = QualCalaisSerializer


class QualTranscriptDataViewSet(viewsets.ModelViewSet):
    queryset = QualTranscriptData.objects.all()
    serializer_class = QualTranscriptDataSerializer


class QualStatsViewSet(viewsets.ModelViewSet):
    queryset = QualStats.objects.all()
    serializer_class = QualStatsSerializer


class SurveyVisibilityViewSet(viewsets.ModelViewSet):
    queryset = SurveyVisibility.objects.all()
    serializer_class = SurveyVisibilitySerializer


class SurveyVisibilityMetadataViewSet(viewsets.ModelViewSet):
    queryset = SurveyVisibilityMetadata.objects.all()
    serializer_class = SurveyVisibilityMetadataSerializer


class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer


class UserGroupSurveyCollectionViewSet(viewsets.ModelViewSet):
    queryset = UserGroupSurveyCollection.objects.all()
    serializer_class = UserGroupSurveyCollectionSerializer
