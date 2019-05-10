import sys

def main():
    year = int(sys.argv[1])
    month = int(sys.argv[2])

    # convert to integer
    year = int( year )
    month = int( month )

    # if section
    if month in [ 1, 3, 5, 7, 8, 10, 12 ]:
    	num_days = 31
    elif month in [ 4, 6, 9, 11 ]:
    	num_days = 30
    else:
        judge = (int(year%4==0) + int(year%100==0) + int(year%400==0)) % 2
        if judge == 1:
            num_days = 29
        else:
            num_days = 28

    print("Month of ", month, "/", year, " has ", num_days, " days.", sep='')

if __name__ == '__main__':
    main()
