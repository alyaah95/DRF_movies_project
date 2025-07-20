from rest_framework import serializers
from .models import Category, Cast, Movie, Series

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        extra_kwargs = {
            'name': {'validators': []}  # تعطيل فحص التكرار
        }

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ['id', 'name']
        extra_kwargs = {
            'name': {'validators': []}  # تعطيل فحص التكرار
        }

class MovieSerializer(serializers.ModelSerializer):
    poster_image_url = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True )
    casts = CastSerializer(many=True)

    class Meta:
        model = Movie
        
        fields = ['id', 'title', 'description', 'release_date', 'categories', 'casts', 'poster_image', 'poster_image_url']
        extra_kwargs = {
            
            'poster_image': {'write_only': True} 
        }

    def get_poster_image_url(self, obj):
        if obj.poster_image:
            
            return obj.poster_image.url 
        return None

    def create(self, validated_data):
        
        categories_data = validated_data.pop('categories', []) 
        casts_data = validated_data.pop('casts', [])

        
        movie = Movie.objects.create(**validated_data) 

        for category_data in categories_data:
            category, created = Category.objects.get_or_create(name=category_data['name'])
            movie.categories.add(category)
        
        for cast_data in casts_data:
            cast, created = Cast.objects.get_or_create(name=cast_data['name'])
            movie.casts.add(cast)
        
        return movie


    def update(self, instance, validated_data):
        # تحديث الحقول العادية أولاً
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.poster_image = validated_data.get('poster_image', instance.poster_image)
        instance.save()

        # معالجة الفئات
        if 'categories' in validated_data:
            categories = []
            for cat_data in validated_data['categories']:
                try:
                    if 'id' in cat_data:
                        category = Category.objects.get(id=cat_data['id'])
                    elif 'name' in cat_data:
                        category, _ = Category.objects.get_or_create(name=cat_data['name'])
                    else:
                        continue
                    categories.append(category)
                except:
                    continue
            instance.categories.set(categories)

        # معالجة الممثلين
        if 'casts' in validated_data:
            casts = []
            for cast_data in validated_data['casts']:
                try:
                    if 'id' in cast_data:
                        cast = Cast.objects.get(id=cast_data['id'])
                    elif 'name' in cast_data:
                        cast, _ = Cast.objects.get_or_create(name=cast_data['name'])
                    else:
                        continue
                    casts.append(cast)
                except:
                    continue
            instance.casts.set(casts)

        return instance


class SeriesSerializer(serializers.ModelSerializer):
    poster_image_url = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True)
    casts = CastSerializer(many=True)

    class Meta:
        model = Series
       
        fields = ['id', 'title', 'description', 'release_date', 'categories', 'casts', 'poster_image', 'poster_image_url']
        extra_kwargs = {
           
            'poster_image': {'write_only': True} 
        }

    def get_poster_image_url(self, obj):
        if obj.poster_image:
           
            return obj.poster_image.url 
        return None

    def create(self, validated_data):
       
        categories_data = validated_data.pop('categories', [])
        casts_data = validated_data.pop('casts', [])

        
        series = Series.objects.create(**validated_data)

        for category_data in categories_data:
            category, created = Category.objects.get_or_create(name=category_data['name'])
            series.categories.add(category)
        
        for cast_data in casts_data:
            cast, created = Cast.objects.get_or_create(name=cast_data['name'])
            series.casts.add(cast)
        
        return series

    
    def update(self, instance, validated_data):
        # تحديث الحقول العادية أولاً
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.poster_image = validated_data.get('poster_image', instance.poster_image)
        instance.save()

        # معالجة الفئات
        if 'categories' in validated_data:
            categories = []
            for cat_data in validated_data['categories']:
                try:
                    if 'id' in cat_data:
                        category = Category.objects.get(id=cat_data['id'])
                    elif 'name' in cat_data:
                        category, _ = Category.objects.get_or_create(name=cat_data['name'])
                    else:
                        continue
                    categories.append(category)
                except:
                    continue
            instance.categories.set(categories)

        # معالجة الممثلين
        if 'casts' in validated_data:
            casts = []
            for cast_data in validated_data['casts']:
                try:
                    if 'id' in cast_data:
                        cast = Cast.objects.get(id=cast_data['id'])
                    elif 'name' in cast_data:
                        cast, _ = Cast.objects.get_or_create(name=cast_data['name'])
                    else:
                        continue
                    casts.append(cast)
                except:
                    continue
            instance.casts.set(casts)

        return instance

    