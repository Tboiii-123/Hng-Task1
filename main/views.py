from django.shortcuts import render

from rest_framework import status
import requests
from django.http import JsonResponse


def number_classification(request):



    try:
        #A dict
        
        number = request.GET.get('number')
        if not number:

            data={
                "number":None,
                "error":True
            }
            return JsonResponse(
            data,
            status=status.HTTP_200_OK


            )

            
        else:

            
            
            sum_outer =[]
            properties=[]
            digit_sum_list=[]


            #removing the minus
            num =number.strip('-')

            #Checking negative
            handler =int(number)
            def is_positive(handler):
                return handler >0

            print(is_positive(handler))
            for i in num:
                int_num=int(i)
                digit_sum_list.append(int_num)


            digit_sum= sum(digit_sum_list)
            
            for i in num:

                whole_number=int(num)
        
                int_num =int(i)
                
                a=int_num**len(num)
                sum_outer.append(a)

                #and len(num)> 1
                if int(num) == sum(sum_outer) and whole_number %2 ==0  and is_positive(handler) == True :
                    properties.append("armstrong")
                    properties.append("even")
                
                elif int(num) == sum(sum_outer) and whole_number %2 ==1  and is_positive(handler) == True:
                    if len(sum_outer)==len(num) :
                        properties.append("armstrong")
                        properties.append("odd")
                        

                elif whole_number % 2 == 0:
                    if len(sum_outer)==len(num) :
                        properties.append("even")
                        

                elif whole_number % 2 == 1 :
                    if len(sum_outer)==len(num) :
                        properties.append("odd")


            num=int(num)
            #For Prime Number
            if num %2 == 0:
            #  print('not a prime number')
                is_prime=False

            else:
            #   print('a prime number')
                is_prime= True


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




            
            fun_fact_url = f"http://numbersapi.com/{int(number)}/math"
            fun_fact = requests.get(fun_fact_url).text



            data={
                "number":int(number),
                "is_prime":is_prime ,
                "is_perfect": is_perfect,
                "properties":properties,
                
                "digit_sum":digit_sum,
                 "fun_fact":fun_fact




            }
        
            return JsonResponse(
            data,
            status=status.HTTP_200_OK


            )
    
    except ValueError as e:

        data={
                 "number":number,
                 "error":True
            }
        
        return JsonResponse(
            data=data,
            status=status.HTTP_400_BAD_REQUEST
        )




