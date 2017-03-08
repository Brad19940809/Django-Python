from datetime import datetime

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')


from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

serializer=CommentSerializer(comment) #comment is an instance,
print(serializer.data)                #and a data also can be transfered into
                                      #the second parameter
#############################################################
from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
print(json)

#############################################################
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

stream = BytesIO(json)
data = JSONParser().parse(stream)
serializer = CommentSerializer(data=data)
print(serializer.is_valid())
print(serializer.validated_data)
######################################

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance

comment = serializer.save()
serializer = CommentSerializer(data=data)
serializer = CommentSerializer(comment, data=data)
serializer.save(owner=request.user)