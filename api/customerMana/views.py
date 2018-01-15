from rest_framework.parsers import JSONParser, FormParser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from core.customer.models import Customer
from api.customerMana.serializers import CustomerSerializer

from utils.rest.code import code
from utils.django.models import get_or_none

import datetime

class CustomerViewSet(viewsets.ModelViewSet):
    """ Viewset handle for requesting course information
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)
    parser_classes = (JSONParser, FormParser,)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            # user has login before register
            return Response({'status': '400', 'code': 'E_IS_LOGIN',
                             'detail ': code['E_IS_LOGIN']},
                            status=400)

        serializer = self.serializer_class(data=request.DATA)
        if not serializer.is_valid():
            return Response({'status': '400', 'code': 'E_INVALID_PARAMETER_VALUES',
                             'detail': serializer.errors}, status=400)

        '''
            tk
                => need for authenticate
            customer
            gst
            uen
            postal
            address
            c_type
        '''
        try:
            cus = request.DATA['customer'].lower()
            gst = request.DATA['gst']
            uen = request.DATA['uen']
            postal = request.DATA['postal']
            addr = request.DATA['address']
            c_type = request.DATA['c_type']
        except Exception as e:
            return Response({'status': '100','code': 'E_INVALID_PARAMETER_VALUES'}, status=400)

        customer, created = Customer.objects.get_or_create(name=cus)

        if not created:
            return Response({'status': '500', 'detail': 'Register error.'}, status=500)

        if created:
            customer.name = cus
            customer.gst_registered_no = gst
            customer.uen_acra = uen
            customer.postal_code = postal
            customer.address = addr
            customer.cus_type = c_type
            customer.save()

        resp = {
            'id'          : customer.id,
            'status'      : '200',
            'code'        : 'OK',
            'detail'      : 'Register successfully',
            'customer': customer.name,
            'gst'     : customer.gst_registered_no,
            'uen'      : customer.uen_acra,
            'postal' : customer.postal_code,
            'c_type'       : customer.cus_type,
        }

        return Response(resp, status=200)

    def list(self, request, *args, **kwargs):
         # = self.queryset
        recent = request.QUERY_PARAMS.get('recent', '')
        if recent == 'true':
            today = datetime.datetime.today()
            all_cus = self.queryset.order_by('-date_create')


    def partial_update(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        try:
            cid = request.DATA['cid']
            cus = request.DATA['customer'].lower()
            gst = request.DATA['gst']
            uen = request.DATA['uen']
            postal = request.DATA['postal']
            addr = request.DATA['address']
            c_type = request.DATA['c_type']
        except Exception as e:
            return Response({'status': '100','code': 'E_INVALID_PARAMETER_VALUES'}, status=400)

        customer = get_or_none(Customer, pk = cid)
        if not customer:
            return Response({'status': '400', 'code': 'E_USER_NOT_FOUND'}, status=400)
        else:
            customer.name = cus
            customer.gst_registered_no = gst
            customer.uen_acra = uen
            customer.postal_code = postal
            customer.address = addr
            customer.cus_type = c_type
            customer.save()

        resp = {
            'id': customer.id,
            'status': '200',
            'code': 'OK',
            'detail': 'Update successfully',
            'customer': customer.name,
            'gst': customer.gst_registered_no,
            'uen': customer.uen_acra,
            'postal': customer.postal_code,
            'c_type': customer.cus_type,
        }

        return Response(resp, status=200)

    def retrieve(self, request, *args, **kwargs):
        pass