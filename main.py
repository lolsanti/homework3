#########################1###############################

#value = 1002000
#value_str = str(value)
#count_zero = value_str.count('0')
#print(f"{value} содержит столько {count_zero} нулей")

###########################2#############################

#value = 1002000
#value_str = str(value)
#last_zero = len(value_str) - len(value_str.rstrip('0'))
#print(last_zero)

#########################3###############################

#my_list_1 = [1, 2, 3, 4]
#my_list_2 = [5, 6, 7, 8]         #Сначало так понял задачу.Ниже переделал жалко удалять
#my_result = []
#for letter in my_list_1 + my_list_2:
    #if letter % 2 == 0:
        #my_result.append(letter)

#print(my_result)

#########################3###############################

#my_list_1 = [1, 2, 3, 4]
#my_list_2 = [5, 6, 7, 8]  #Надеюсь правильно все понял
#my_result = my_list_1[1::2] + my_list_2[1::2]
#print(my_result)

##########################4##############################

#my_list = [1, 2, 3, 4]
#new_list = [4, 3, 2, my_list[0]] #хотел сделать по другому но пайтон исправил так
#print(new_list)

#############################4###########################

#my_list = [1, 2, 3, 4]
#new_list = []
#for i in my_list[1:]:
    #new_list.append(i)
                                   #4 задание просто по другому
#new_list.append(my_list[0])
#print(new_list)

###########################5#############################

#my_list = [1, 2, 3, 4]
#new_list = [4, 3, 2]
#symbol = my_list.pop(0)
#new_list.append(symbol)
#print(new_list)

############################6############################

#my_str = "20 більше ніж 30 , але менше ніж 50"
#words = my_str.split()
#result = 0
#for i in words:
    #if i.isdigit():
        #result += int(i)

#print(result)

#если втулить запятую ровно перед 30 будет проблмка и оно не засчитает 30
############################7############################

#my_list = [1, 4, 2, 1, 9, 5, 6, 2]
#count = 0
#for i in range(1, len(my_list) - 1):
    #if my_list[i] > my_list[i-1] + my_list[i+1]:
        #count += 1
#print(count)
#Тяжеловато как-то далось
############################8############################

#my_list = [1, 2, 3, "11", "22", 33]
#new_list = []
#for item in my_list:
    #if isinstance(item, str):
        #new_list.append(item)

#print(new_list)

############################9############################

#my_str = "кохайтеся чорнобриві та не з москалями"
#my_list = []
#for letter in my_str:
    #if my_str.count(letter) == 1:
        #my_list.append(letter)

#print(my_list)
#Я немного не понял стоит ли выводить единожды повторяющиеся символы
###########################9############################ ленивый вариант

#my_str = "кохайтеся чорнобриві та не з москалями"
#uniq_chr = list(set(my_str))
#print(uniq_chr)

###########################10############################

#my_str = "i like pepsi"
#your_str = "do you like fanta"
#set_1 = set(my_str)
#set_2 = set(your_str)

#common_letter = list(set_1.intersection(set_2))

#print(common_letter)

###########################11############################

#my_str = "Othermm sing"
#your_str = "samme thing"
#set_1 = set(my_str)
#set_2 = set(your_str)
#result_set = set()
#for letter in set_1.intersection(set_2):
    #if my_str.count(letter) == 1 and your_str.count(letter) == 1:
        #result_set.add(letter)

#result_list = list(result_set)
#print(result_list)

#Большое спасибо.Прекрасное количесво примеров для практики 








































