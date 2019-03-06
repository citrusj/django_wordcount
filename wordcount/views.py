from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    dic = {}
    for word in word_list:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1
    maxwo = sorted(dic, key=dic.get, reverse=True)[0]
    return render(request, 'count.html', {'maxword':maxwo, 'fulltext':full_text, 'total':len(word_list), 'dictionary':dic.items(), 'tt':len(dic)})