def main():
    while(True):
        n=int(input())
        if n==0:
            break;
        else:
            grid = [0]*(n)
            ban=False
            for j in range(0,n):
                x,y=input().split()
                numCar=int(x)
                gan=int(y)
                value=j+gan
             
                if value >= 0 and value<n and grid[value]==0:
                    grid[value]=int(numCar)
                    #break
                else:
                    ban=True
            if ban==True:
                print("-1")   
            else:
                grid_Initial=str(grid[0])
                for j in range(1,n):
                    grid_Initial=grid_Initial+" "+str(grid[j])
                    
                print(grid_Initial)       
if __name__ == '__main__':
    main()