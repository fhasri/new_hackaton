from rest_framework import serializers
from .models import Product, ProductImage
from apps.comment.serializers import CommentSerializer
from apps.rating.serializers import RatingSerializer
from django.db.models import Avg


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image')

class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    # def get_rating(self, instance):
    #     return instance.ratings.aggregate(models.Avg('rating'))['rating__avg']
    def get_rating(self, instance):
        return instance.ratings.aggregate(Avg('rating'))['rating__avg']


    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        images_data = validated_data.pop('images', [])
        product = Product.objects.create(author=user, **validated_data)
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)
        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        instance = super().update(instance, validated_data)

        # Delete existing images not included in the update
        existing_image_ids = [image_data['id'] for image_data in images_data if 'id' in image_data]
        instance.images.exclude(id__in=existing_image_ids).delete()

        # Create or update images
        for image_data in images_data:
            image_id = image_data.get('id')
            if image_id:
                image = instance.images.filter(id=image_id).first()
                if image:
                    image.image = image_data.get('image', image.image)
                    image.save()
            else:
                ProductImage.objects.create(product=instance, **image_data)

        return instance



# from rest_framework import serializers
# from .models import Product, ProductImage
# from apps.comment.serializers import CommentSerializer
# from apps.rating.serializers import RatingSerializer

# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ('id', 'product', 'image')

# class ProductSerializer(serializers.ModelSerializer):
#     comments = CommentSerializer(many=True, read_only=True)
#     ratings = RatingSerializer(many=True, read_only=True)
#     likes_count = serializers.SerializerMethodField()
#     rating = serializers.SerializerMethodField()
#     images = ProductImageSerializer(many=True, read_only=True)

#     class Meta:
#         model = Product
#         fields = '__all__'

#     def get_likes_count(self, instance):
#         return instance.likes.count()

#     def get_rating(self, instance):
#         return instance.ratings.aggregate(models.Avg('rating'))['rating__avg']

#     def create(self, validated_data):
#         request = self.context.get('request')
#         user = request.user
#         images_data = validated_data.pop('images', [])
#         product = Product.objects.create(author=user, **validated_data)
#         for image_data in images_data:
#             ProductImage.objects.create(product=product, **image_data)
#         return product

#     def update(self, instance, validated_data):
#         images_data = validated_data.pop('images', [])
#         instance = super().update(instance, validated_data)

#         # Delete existing images not included in the update
#         existing_image_ids = [image_data['id'] for image_data in images_data if 'id' in image_data]
#         instance.images.exclude(id__in=existing_image_ids).delete()

#         # Create or update images
#         for image_data in images_data:
#             image_id = image_data.get('id')
#             if image_id:
#                 image = instance.images.filter(id=image_id).first()
#                 if image:
#                     image.image = image_data.get('image', image.image)
#                     image.save()
#             else:
#                 ProductImage.objects.create(product=instance, **image_data)

#         return instance
