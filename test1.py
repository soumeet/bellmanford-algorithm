import sys

n=0
cost=[]
spl=[]
prev=[]

def input_cost():
    print("enter number of vertices: ")
    n=int(input())
    for i in range(1,n+1):
        row=[]
        for j in range(1,n+1):
            row.append(int(input()))
        cost.append(row)

def display_cost():
    for row in cost:
        for item in row:
            print(item, end=' ')
        print()
        
def bellmanford():
    a=cost
    for i in range(1,n):
        for j in range(1,n):
            r=[]
    spl=[99]*n
    prev=[0]*n
    
    spl[1]=0
    x=0
    for k in range(1,n):
        for i in range(1,n):
            for j in range(1,n):
                if []


input_cost()
display_cost()

