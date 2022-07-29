from rest_framework import serializers
from app.models import Section, Item, Modifiers


class SectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title', 'description']


class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'price', 'section']


class SectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifiers
        fields = ['id', 'title', 'description']


class ModifiersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifiers
        fields = ['id', 'title', 'description', 'item']


class ModifiersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifiers
        fields = ['id', 'title', 'description']


class ItemDetailSerializer(serializers.ModelSerializer):
    modifiers = ModifiersDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'price', 'modifiers']


class SectionListSerializer(serializers.ModelSerializer):
    item = ItemDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'description', 'item']


class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'price', 'section']


class ItemListSerializer(serializers.ModelSerializer):
    section = SectionDetailSerializer(read_only=True)
    modifiers = ModifiersDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'price', 'section', 'modifiers']


class ModifiersListSerializer(serializers.ModelSerializer):
    item = ItemDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Modifiers
        fields = ['id', 'title', 'description', 'item']
