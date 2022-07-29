from app.models import Section, Item, Modifiers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SectionCreateSerializer, SectionListSerializer, ItemListSerializer, \
    ItemCreateSerializer, ModifiersListSerializer, ModifiersCreateSerializer


class SectionListView(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SectionCreateSerializer
        else:
            return SectionListSerializer

    def get_queryset(self):
        return Section.objects.all().prefetch_related('item')


class SectionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SectionCreateSerializer

    def get_queryset(self):
        return Section.objects.all()


class ItemListView(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ItemCreateSerializer
        else:
            return ItemListSerializer

    def get_queryset(self):
        return Item.objects.all().prefetch_related('modifiers')


class ItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemCreateSerializer

    def get_queryset(self):
        return Item.objects.all()


class ModifiersListView(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ModifiersCreateSerializer
        else:
            return ModifiersListSerializer

    def get_queryset(self):
        return Modifiers.objects.all()


class ModifiersDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ModifiersListSerializer

    def get_queryset(self):
        return Modifiers.objects.all()