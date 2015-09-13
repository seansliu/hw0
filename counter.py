# Sean Liu
# hw0 Script

def main():
    matches = 0
    search = 'single malt scotch'
    f = open('iowa_liquor_sales.csv', 'r')
    for record in f:
        if search in record.lower():
            matches += 1
    print 'Number of matches for ' + search + ':', matches

main()

