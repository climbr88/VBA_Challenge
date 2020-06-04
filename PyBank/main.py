import os
import csv



csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')  

#Set counts 
count = 0 
total = 0 # profit/loss
largest_loss = []
largest_profit = []
with open(csvpath) as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

   #print(csvreader)

    # Read the header row 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
 
    
    for row in csvreader:
        print(row)
        count += 1
   
        total += int(row[1])
        
             

    
    print(f"Total months: {count}")
    
    print(f"Total Profit/Loss: {total}")
    

# Add the candy at the index chosen to the candy_cart list
#    largest_profit.append(candy_list[int(selected)]) - update the ()
# write code that says if profit of month 2 - profit of month 1 is greater than
# 0, append to largest profit list, then same for <0 to profit loss
# then get the largest value in each list?
    


