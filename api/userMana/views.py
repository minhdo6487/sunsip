import datetime

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum, Q
from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from api.userMana.serializers import UserSerializer

from core.user.models import UserSetting, UserProfile
from utils.django.models import get_or_none
from utils.rest.code import code
from utils.rest.permissions import UserIsOwnerOrRead
from utils.rest.viewsets import GetAndUpdateViewSet, OnlyGetViewSet

@api_view(['POST'])
def get_group(request):
    email_list = request.DATA.get('email', "''")
    if email_list == "''":
        return Response({'detail': 'Are You Kidding me???'}, status=404)
    return_data = []
    i = 1
    for item in email_list:
        s = 'p' + str(i)
        user = get_or_none(User, username=item[s])
        if user is not None:
            return_data.append({s: {'name': user.last_name + ' ' + user.first_name, 'id': user.id}})
        else:
            return_data.append({s: {'name': '', 'id': -1}})
        i += 1
    return Response(return_data, status=404)


class UserViewSet(OnlyGetViewSet):
    """ Viewset handle for managing Get Another User profile and friend list
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (JSONParser, FormParser,)
    permission_classes = (IsAuthenticated,)

    # get user detail by pk

    def list(self, request, *args, **kwargs):
        email = request.QUERY_PARAMS.get('email', '')
        if email:
            user = get_or_none(User, username=email)
            if user:
                serialize = UserDisplaySerializer(user)
                return Response(serialize.data, status=200)
        return Response([], status=200)

    def retrieve(self, request, pk=None, **kwargs):
        user = get_or_none(User, pk=pk)
        if user is None:
            return Response({'status': '404', 'code': 'E_NOT_FOUND',
                             'detail': 'Cannot find user'}, status=404)
        privacy = UserPrivacy.objects.filter(user=user, target=request.user, action='D').first()
        context = {
            'is_block': True if privacy else False
        }
        # get usersetting by PK
        setting_queryset = UserSetting.objects.get(user_id=pk)

        # if user not public and not get itself
        if not setting_queryset.public_profile and request.user.id != int(pk):
            return Response({'status': '405', 'code': 'E_GET_NOT_ALLOW',
                             'detail': code['E_GET_NOT_ALLOW']}, status=405)

        serializer = UserSerializer(user, context=context)

        response_data = serializer.data

        # checking friend with current user
        response_data['current_user_id'] = request.user.id

        return Response(response_data, status=200)


class ProfileView(GetAndUpdateViewSet):
    """ Viewset handle for user profile
        HEADER :
            GET
            PATCH
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # TODO: More rule for action
    permission_classes = (IsAuthenticated, UserIsOwnerOrRead)
    parser_classes = (JSONParser, FormParser,)

    def initial(self, request, *args, **kwargs):
        """ Override init function of django to add pk to the request, before calling any other actions
        """
        super().initial(request, *args, **kwargs)
        self.kwargs['pk'] = request.user.pk

    def partial_update(self, request, *args, **kwargs):
        # add encode password to request
        return super(ProfileView, self).partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ProfileView, self).update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        device = request.QUERY_PARAMS.get('device', '')
        if device == 'mobile':
            user_profile = UserProfile.objects.only('display_name', 'gender', 'handicap_us', 'profile_picture').get(
                user=request.user)
            return Response({
                "display_name": user_profile.display_name,
                "gender": user_profile.gender,
                "handicap_us": user_profile.handicap_us,
                "profile_picture": user_profile.profile_picture
            })
        return super(ProfileView, self).retrieve(request, *args, **kwargs)

