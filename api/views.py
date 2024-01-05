from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .models import File
from .serializers import FileSerializer


latin_letter = {
            'А': 'A', 'Б': 'B', 'Ц': 'C', 'Д': 'D', 'Е': 'E', 'Ф': 'F', 'Г': 'G', 'Х': 'H', 'И': 'I', 'Й': 'Y',
            'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'К': 'Q', 'Р': 'R', 'С': 'S', 'Т': 'T',
            'У': 'U', 'В': 'V', 'Ш': 'Sh', 'Х': 'X', 'Ј': 'Y', 'З': 'Z',
            'а': 'a', 'б': 'b', 'ц': 'c', 'д': 'd', 'е': 'e', 'ф': 'f', 'г': 'g', 'х': 'h', 'и': 'i', 'й': 'y',
            'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'к': 'k', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'в': 'v', 'ш': 'sh', 'x': 'x', 'ј': 'y', 'з': 'z', 'ё': 'yo', 'ў': "o'", 'ь': ''
        }

cyrillic_letter = {
            'A': 'А', 'B': 'Б', 'C': 'Ц', 'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Х', 'I': 'И', 'J': 'Ј',
            'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П', 'Q': 'К', 'R': 'Р', 'S': 'С', 'T': 'Т',
            'U': 'У', 'V': 'В', 'W': 'Ш', 'X': 'КС', 'Y': 'Ј', 'Z': 'З',
            'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'ј',
            'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'q': 'к', 'r': 'р', 's': 'с', 't': 'т',
            'u': 'у', 'v': 'в', 'w': 'ш', 'x': 'х', 'y': 'й', 'z': 'з', 'sh': 'ш', 'ch': 'ч'
        }


class ConvertText(APIView):
    def post(self, request):
        context = request.data.get('context')
        pattern = request.data.get('pattern')

        result = self.convert(context, pattern)
        return Response({'result': result})

    def convert(self, context, pattern):
        if pattern == 'cyrillic':
            result = ''
            for letter in context:
                if letter in cyrillic_letter:
                    result += cyrillic_letter[letter]
                else:
                    result += letter
        elif pattern == 'latin':
            result = ''
            for letter in context:
                if letter in latin_letter:
                    result += latin_letter[letter]
                else:
                    result += letter
        else:
            result = "error: must be context and pattern(latin or cyrillic)"
        return result


class FileConverter(CreateAPIView):
    queryset = File
    serializer_class = FileSerializer

    def post(self, request):
        filename = request.FILES['file']
        pattern = request.data['pattern']

        if filename.name.endswith('.txt'):
            content = filename.read().decode('utf-8')
            if pattern == 'cyrillic':
                result = ''
                for each in content:
                    if each in cyrillic_letter:
                        result += cyrillic_letter[each]
                    else:
                        result += each
            elif pattern == 'latin':
                result = ''
                for each in content:
                    if each in latin_letter:
                        result += latin_letter[each]
                    else:
                        result += each
            else:
                return Response({'error: must be context and pattern(latin or cyrillic)'})
            with open('C:/Users/Dilmurod/Desktop/result.txt', 'w', encoding='utf-8') as f:
                f.write(result)
            return Response({'result': result})


def migration(request):
    import os
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate --no-input')
    return HttpResponse('Migration Done')
