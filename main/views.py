from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests


@api_view(["GET"])
def number_classification(request):



    try:
        #A dict
        num = request.GET.get('num')
        
        sum_outer =[]
        properties=[]
        
        for i in num:

            whole_number=int(num)
    
            int_num =int(i)
            a=int_num**len(num)
            sum_outer.append(a)
            if int(num) == sum(sum_outer) and whole_number %2 ==0 and len(num)> 1 :
                properties.append("Armstrong")
                properties.append("even")
            
            elif int(num) == sum(sum_outer) and whole_number %2 ==1 and len(num)> 1:
                if len(sum_outer)==len(num) :
                    properties.append("Armstrong")
                    properties.append("Odd")
                    

            elif whole_number % 2 == 0:
                if len(sum_outer)==len(num) :
                    properties.append("Even")
                    

            elif whole_number % 2 == 1 :
                if len(sum_outer)==len(num) :
                    properties.append("Odd")


        num=int(num)
        #For Prime Number
        if num %2 == 0:
          #  print('not a prime number')
            is_prime=True

        else:
         #   print('a prime number')
            is_prime= False


        #For Perfect Number
        
        list =[]
        for i in range(1,num):
            
            if num % i ==0:
                list.append(i)

            else:
                continue

        if sum(list) == num:
         #   print(f"{num} is a perfect number")
            is_perfect =True

        else:
        #    print("Not a perfect number")
        
            is_perfect =False




           
        fun_fact_url = f"http://numbersapi.com/{num}/math"
        fun_fact = requests.get(fun_fact_url).text


        data={
            "Number":num,
            "is_prime":is_prime ,
            "is_perfect": is_perfect,
            "properties":properties,
            "fun_fact":fun_fact


        }
    
        return Response(
        data,
        status=status.HTTP_200_OK

        )
    
    except ValueError:

        data={
                 "number":"alphabet",
                 "error":True
            }
        
        return Response(
            data=data,
            status=status.HTTP_400_BAD_REQUEST
        )




