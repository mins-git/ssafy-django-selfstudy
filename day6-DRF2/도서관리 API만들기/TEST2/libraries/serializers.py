from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content', 'score',)

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
    review_set = ReviewDetailSerializer(read_only=True, many=True)    
    number_of_review = serializers.IntegerField(source='review_set.count', read_only=True)



class BookIsbnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('isbn',)

class ReviewListSerializer(serializers.ModelSerializer):
    book = BookIsbnSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('content', 'score','book',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)