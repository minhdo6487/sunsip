from rest_framework import serializers

from core.customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'gst_registered_no', 'uen_acra', 'postal_code', 'address', 'country', 'cus_type')

    def to_native(self, obj):
        serializers = super(CustomerSerializer, self).to_native(obj)
        return serializers