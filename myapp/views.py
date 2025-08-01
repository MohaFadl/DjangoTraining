from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q , F , Value , Func , ExpressionWrapper
from django.db.models.aggregates import Max , Min , Count , Avg , Sum
from django.db.models.functions import Concat
from myapp.models import Client
from django.db import transaction , connection


# Create your views here.
def test(request):
    x = 5
    x = 6
    try:
        obj1 = Client.objects.get(pk = 1)
    except ObjectDoesNotExist:
        pass


    with transaction.atomic():
        client_obj = Client()

        # there is another way to do it .. a smarter way


        obj2 = Client.objects.filter(pk__gte=5).exists() 
        
        client = Client.objects.all()
        c = Client.objects.raw('Select * from myapp.Client')
        ca = connection.cursor
   
    #This is if statment (where last_name equal first_name)
    client = Client.objects.filter(last_name=F('first_name'))

    #We can count , avg and so on # we can also use count and group the count
    #increased_salary ExpressionWrapper(F('salary') * 1.2 , output_field= DecimalField() )  # to change datatypes safely 
    clinet = Client.objects.aggregate(count = Count('first_name'))
    #THIS IS THE OR OPERATOR AND ~ IS NOT


    client = Client.objects.filter(Q(pk=1) | ~Q(Q(pk=5)))
    #ORDERING ASC BY FIRSTNAME ADD - TO DESC WE CAN ALSO USE .reverse()
    #we can acess a query set by adding at the end [] and the index or splitting 
    #we can use.earliest or latest (arrange and then get the first one)
    client = Client.objects.order_by('-first_name')



    #concat!!!!! hehehe 
    client = Client.objects.annotate(
        full_name = Func(F('first_name'),Value(' '), F('last_name') , function = 'CONCAT')
    )

    #easier to concat hehehehe
    client = Client.objects.annotate(
        full_name = Concat(F('first_name'),Value(' '), F('last_name'))
    )



    return render(request, 'testpage.html' , {'Name':'Mohamed Medhat','clients':list(client)})

