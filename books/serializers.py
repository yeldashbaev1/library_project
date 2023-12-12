# Convert datas some formates from Data base
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','title', 'content', 'subtitle', 'author', 'isbn', 'price',)
    #hamme fieldti alip qalegenin tekseresen
    def validate(self, data):
        title = data.get('title',None)
        author = data.get('author', None)

        # check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitobni sarlavhasi harflardan tashkil topgan bolishi kerak"
                }
            )
        # check author and title from database existence
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Kitob molifi va sarlavhasi bir xil bolgan kitob yuklay olmaysiz'
                }
            )
        return data
    #qalegen fieldti alip valdatsiya qilasan
    def validate_price(self, price):
        if price < 0 or price > 999999999999:
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Narx notogri kiritilgan'
                }
            )