## lsit is a common extensive which is used in many languages as
## list have many features like adding,removing,modifying etc
to_do_list = ["BuyingGroceries","cleanhouse","pay_bills"]
## adding to task
to_do_list.append("sechdule meeting")
to_do_list.append("go for run")
## removing a task
to_do_list.remove("cleanhouse")
## checking if a task is in list
#if "pay_bills" in to_do_list:
 #   print("pay the bills it is due")
#print("to do list:")
#for task in to_do_list:
    #print(f"-{task}")    
#    print(task) # this will also work 

## organizing student grades
grades=[89,90,91,93,94,95,99]
## adding a new grade
grades.append(97)
## calculating the average grade
avg= sum(grades)/len(grades)
#print("average grade:",avg)
## finding the highest and lowest grade
highest_grade=max(grades)
lowest_grade=min(grades)
#print("highest grade:",highest_grade)
#print("lowest grade:",lowest_grade)

## managing inventory in a store
#inventory=["apples","bananas","oranges","grapes"]
# adding new items
#inventory.append("watermelon")
# removing an item which is out of stock
#inventory.remove("oranges")
# checking if an item is in stock
#if "oranges" in inventory:
#    print("GREAT we have oranges in stock")
#else:  
#    print("SORRY we are out of stock for oranges")
## printing the inventory
#print("current inventory:")
#for i in inventory:
#     print(f"-{i}")# this is used for formatting the output with a dash before each item

## Collecting User Feedback
#feedback=[]
#while True:
   # input_feedback=input("PLEASE PROVIDE YOUR FEEDBACK (type exit to stop ):")

  #  if input_feedback.lower()=="exit":
 #       break
 #   feedback.append(input_feedback.lower())# storing all feedback in lowercase to maintain consistency
#print("the collected feedback:")
#for fb in feedback:
#     print(f"-{fb}")# by using loop we get the data in row format not in list format
#print(feedback) # as this will print the feedback in lsit format
## to count the number of feedback is collected
#count=feedback.count('good')
#print(count)   
## another way of collecting feedback
feedback=["GOOD","EXCELLENT","AVERAGE","POOR","GOod","Excellent"]
## adding a new feedback
feedback.append("Average")
## counting specific feedback
positive_feedback=sum(1 for fb in feedback if "good" in fb.lower() or "excellent" in fb.lower())
print(f"POSITIVE FEEDBACK ARE:{positive_feedback}")

## printing all feedback 
print("all feedback:")
for i in feedback:
    print(f"-{i}")
