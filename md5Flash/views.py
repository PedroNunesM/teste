import hashlib
import imp
import string
import random
import time
from hashlib import md5
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def random_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

data = {}
tempo_inicial = time.time()
md5Data = ''
def index(request):
    global data
    global tempo_inicial
    global md5Data
    data['flag'] = ''
    if request.method == 'POST':
        print(time.time() - tempo_inicial)
        if time.time() - tempo_inicial < 0.1:
            if request.POST['md5Flash'] == md5Data:
                data['flag'] = 'AcHaCTF'+'{'+'MaIs_RaPiDo_QuE_O_FlAsH'+'}'
            else:
                data['flag'] = 'Resposta errada'    
        else:
            data['flag'] = 'Lento demais, tente novamente!'
        return render(request, 'md5Flash/index.html', data)
    elif request.method == 'GET':
        tempo_inicial = time.time()
        palavra = random_generator()
        data['chave'] =  palavra
        md5Data = md5(palavra.encode()).hexdigest()
        print(md5Data)
        return render(request, 'md5Flash/index.html', data)